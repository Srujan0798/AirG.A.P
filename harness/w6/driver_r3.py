#!/usr/bin/env python3
"""W6 round 3: coverage-guided test generation, offline.

Same model (qwen2.5-coder:7b), same 10 functions, same sandbox as round 2.
No new downloads.

Difference from round 2: the model is told which exact lines are uncovered and
what those lines contain, and after each attempt the loop reports back which
target lines still were not executed. Max 4 attempts.

Also fixes round 2's two systematic prompt errors:
  - the correct import path is stated per function (not just the module top name)
  - when the target is a method, the prompt says an instance is required

Record per function: attempts, pass/fail/error, target lines hit
(yes/partial/no), coverage before/after, tok/s, wall.
"""
import ast
import importlib
import inspect
import json
import os
import re
import subprocess
import sys
import threading
import time

import psutil

ROOT = "/Users/srujansai/Desktop/AirG.A.P/harness/w6"
SANDBOX = os.path.join(ROOT, "sandbox", "click")
LOGDIR = os.path.join(ROOT, "logs")
VENVPY = os.path.join(ROOT, "venv", "bin", "python")
MODEL = "qwen2.5-coder:7b"
OLLAMA_URL = "http://localhost:11434/api/generate"
MAX_ATTEMPTS = 4
os.makedirs(LOGDIR, exist_ok=True)

TARGETS = [
    ("click.exceptions", "_join_param_hints"),
    ("click._textwrap", "TextWrapper._handle_long_word"),
    ("click.formatting", "wrap_text"),
    ("click.testing", "EchoingStdin.readline"),
    ("click.testing", "make_input_stream"),
    ("click.decorators", "custom_version_option"),
    ("click.exceptions", "BadParameter.format_message"),
    ("click.types", "ParamType.convert"),
    ("click.utils", "_make_default_short_help"),
    ("click.decorators", "confirmation_option"),
]

ENV = dict(os.environ)
ENV["VIRTUAL_ENV"] = os.path.join(ROOT, "venv")
ENV["PATH"] = os.path.join(ROOT, "venv", "bin") + os.pathsep + ENV.get("PATH", "")

# Target lines as claimed in the round-2 report table, kept only for
# cross-reference. Round 3 computes the real uncovered lines per function
# (intersection of the module's missing lines with the function's line range).
R2_CLAIMED_TARGET_LINES = {
    "_join_param_hints": [21],
    "TextWrapper._handle_long_word": [63, 64],
    "wrap_text": [80],
    "EchoingStdin.readline": [79],
    "make_input_stream": [245],
    "custom_version_option": [585],
    "BadParameter.format_message": [148, 152],
    "ParamType.convert": [203],
    "_make_default_short_help": [33],
    "confirmation_option": [389, 390, 391, 392, 393, 394, 395, 396, 397, 398,
                            399, 400, 401],
}


def ollama_generate(prompt):
    payload = {"model": MODEL, "prompt": prompt, "stream": False,
               "options": {"num_predict": 512, "temperature": 0.2}}
    stop = threading.Event()
    peak = [0.0]

    def sampler():
        while not stop.is_set():
            try:
                total = 0.0
                for p in psutil.process_iter(["name", "memory_info"]):
                    n = (p.info["name"] or "").lower()
                    if "ollama" in n or "llama" in n:
                        total += p.info["memory_info"].rss / (1024 * 1024)
                if total > peak[0]:
                    peak[0] = total
            except Exception:
                pass
            time.sleep(0.2)

    t = threading.Thread(target=sampler, daemon=True)
    t.start()
    t0 = time.time()
    try:
        r = subprocess.run(["curl", "-s", "-X", "POST", OLLAMA_URL,
                            "-H", "Content-Type: application/json",
                            "-d", json.dumps(payload)],
                           capture_output=True, text=True, timeout=300)
    finally:
        stop.set()
    t.join(timeout=5)
    wall = time.time() - t0
    try:
        d = json.loads(r.stdout)
    except Exception:
        return "", {"error": r.stdout[:500], "wall": round(wall, 2)}, peak[0]
    ec = d.get("eval_count", 0)
    ed = d.get("eval_duration", 0)
    metrics = {
        "eval_count": ec,
        "eval_duration_s": round(ed / 1e9, 3) if ed else None,
        "tokens_per_sec": round(ec / (ed / 1e9), 1) if ed else None,
        "total_duration_s": round(d.get("total_duration", 0) / 1e9, 3),
        "wall_s": round(wall, 2),
        "load_duration_s": round(d.get("load_duration", 0) / 1e9, 3),
    }
    return d.get("response", ""), metrics, peak[0]


def extract_code_block(text):
    m = re.search(r"```(?:python)?\n(.*?)```", text, re.S)
    return m.group(1) if m else text.strip()


def resolve(modpath, qualname):
    """Return (obj, class_name_or_None, func_name)."""
    parts = qualname.split(".")
    mod = importlib.import_module(modpath)
    obj = mod
    for p in parts:
        obj = getattr(obj, p)
    cls = parts[0] if len(parts) > 1 else None
    return obj, cls, parts[-1]


def source_for(modpath, qualname):
    obj, _, _ = resolve(modpath, qualname)
    return inspect.getsource(obj)


def line_range(obj):
    lines, start = inspect.getsourcelines(obj)
    return start, start + len(lines) - 1


def module_file(modpath):
    mod = importlib.import_module(modpath)
    return mod.__file__


def module_imports(modpath):
    path = module_file(modpath)
    out = []
    with open(path) as fh:
        for line in fh:
            s = line.rstrip("\n")
            if s.startswith("import ") or s.startswith("from "):
                out.append(s)
    return out


def find_test_example(modpath, qualname):
    name = qualname.split(".")[-1]
    hits = []
    for root, _, files in os.walk(os.path.join(SANDBOX, "tests")):
        for fn in files:
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            try:
                txt = open(p).read()
            except Exception:
                continue
            if name in txt:
                hits.append((p, txt))
    if not hits:
        return "# (no existing test references this function in the repo)"
    p, txt = min(hits, key=lambda x: len(x[1]))
    tree = ast.parse(txt)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
            body = ast.get_source_segment(txt, node) or ""
            if name in body:
                return body
    return txt[:800]


def coverage_run(args, label):
    datafile = os.path.join(LOGDIR, f".cov_{label}_{os.getpid()}_{int(time.time()*1000)}")
    try:
        os.remove(datafile)
    except Exception:
        pass
    e = dict(ENV)
    e["COVERAGE_FILE"] = datafile
    cmd = [VENVPY, "-m", "coverage", "run", "-m", "pytest", "-q", "-p", "no:cacheprovider"] + args
    r = subprocess.run(cmd, cwd=SANDBOX, capture_output=True, text=True, env=e, timeout=300)
    out = r.stdout + r.stderr
    jpath = os.path.join(LOGDIR, f".json_{label}_{os.getpid()}_{int(time.time()*1000)}")
    e2 = dict(ENV)
    e2["COVERAGE_FILE"] = datafile
    subprocess.run([VENVPY, "-m", "coverage", "json", "-o", jpath],
                   cwd=LOGDIR, capture_output=True, text=True, env=e2, timeout=120)
    for p in (datafile,):
        try:
            os.remove(p)
        except Exception:
            pass
    return out, jpath


def cov_file_info(json_path, modpath):
    """Return dict for the target module file in a coverage json."""
    try:
        with open(json_path) as fh:
            j = json.load(fh)
    except Exception:
        return None
    suffix = "src/click/" + modpath.split(".")[-1] + ".py"
    for path, info in j.get("files", {}).items():
        if path.endswith(suffix):
            return info
    return None


def module_percent(json_path, modpath):
    info = cov_file_info(json_path, modpath)
    if not info:
        return None
    return info.get("summary", {}).get("percent_covered")


def target_missing(json_path, modpath, lo, hi):
    """Lines in [lo,hi] that coverage reports as missing."""
    info = cov_file_info(json_path, modpath)
    if not info:
        return None
    miss = set(info.get("missing_lines", []) or [])
    return sorted(n for n in miss if lo <= n <= hi)


def parse_pytest_verbose(text):
    passed = failed = error = 0
    kept = []
    for line in text.splitlines():
        m = re.match(r"(\S+::test_\S+) (PASSED|FAILED|ERROR)", line)
        if not m:
            continue
        nodeid, status = m.group(1), m.group(2)
        if status == "PASSED":
            passed += 1
            kept.append(nodeid.split("::")[-1])
        elif status == "FAILED":
            failed += 1
        else:
            error += 1
    if passed == 0 and failed == 0 and error == 0:
        for pat, key in ((r"(\d+) passed", "p"), (r"(\d+) failed", "f"), (r"(\d+) error", "e")):
            m = re.search(pat, text)
            if m:
                if key == "p":
                    passed += int(m.group(1))
                elif key == "f":
                    failed += int(m.group(1))
                else:
                    error += int(m.group(1))
    return passed, failed, error, kept


def write_kept(code, kept_names):
    tree = ast.parse(code)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in kept_names:
            out.append(ast.get_source_segment(code, node))
    imports = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.get_source_segment(code, node))
    return "\n".join(imports + out) + "\n"


def fmt_lines(lines, text_lines):
    out = []
    for n in lines:
        txt = text_lines[n - 1].rstrip("\n") if 0 < n <= len(text_lines) else ""
        out.append(f"line {n}: {txt}")
    return "\n".join(out)


def build_prompt(src, imports, example, import_hint, method_note, numbered_src,
                 target_lines, text_lines, feedback=""):
    imp = "\n".join(imports) if imports else "# (no import lines found)"
    tgt = fmt_lines(target_lines, text_lines)
    if not target_lines:
        tgt = ("(none - every line of this function is already executed by the existing test "
               "suite. Write a test that exercises this function and passes.)")
    fb = ("\n\n=== FEEDBACK FROM THE PREVIOUS ATTEMPT ===\n" + feedback) if feedback else ""
    return (
        "You are a test-generation engineer. Write pytest unit tests whose ONLY goal is to "
        "execute the specific uncovered lines listed below.\n\n"
        "Hard rules:\n"
        "1. Output ONLY one python code block (```python ... ```).\n"
        "2. Tests must be deterministic. No network access, no secrets, no sleeps.\n"
        "3. Import EXACTLY as shown in the 'Correct import' block. Do not guess another module.\n"
        "4. The test must PASS. Avoid assertions on values you are not sure about unless the "
        "target line requires it.\n"
        "5. Every line in the TARGET LINES list must actually be executed by your test.\n\n"
        "Correct import for the function under test:\n" + import_hint + "\n" + method_note +
        "\n\nModule imports available in the file under test:\n" + imp +
        "\n\nExisting test style example:\n" + example +
        "\n\nTARGET LINES currently NOT executed (your test MUST execute all of these):\n" + tgt +
        fb +
        "\n\nFunction source (with line numbers):\n\n" + numbered_src
    )


def main():
    # baseline coverage of the repo's own suite
    base_out, base_j = coverage_run(["tests"], "base_r3")
    base_json = os.path.join(LOGDIR, "base_r3.json")
    subprocess.run(["cp", base_j, base_json], capture_output=True)

    results = []
    for modpath, qualname in TARGETS:
        tag = qualname.split(".")[-1]
        obj, cls, fname = resolve(modpath, qualname)
        src = source_for(modpath, qualname)
        imports = module_imports(modpath)
        example = find_test_example(modpath, qualname)
        lo, hi = line_range(obj)
        mf = module_file(modpath)
        with open(mf) as fh:
            text_lines = fh.readlines()
        baseline_pct = module_percent(base_json, modpath)
        tgt = target_missing(base_json, modpath, lo, hi) or []
        target_lines = tgt
        numbered_src = "".join(f"{lo+i:>4}: {l}" for i, l in enumerate(text_lines[lo-1:hi]))

        if cls:
            import_hint = f"from {modpath} import {cls}"
            method_note = (f"\nNOTE: {cls}.{fname} is a METHOD. You must create an instance "
                           f"first (for example `obj = {cls}(...)`) and then call "
                           f"`obj.{fname}(...)`. Calling `{fname}(...)` as a bare function will fail.")
        else:
            import_hint = f"from {modpath} import {fname}"
            method_note = ""

        rec = {"module": modpath, "function": qualname,
               "baseline_cov": baseline_pct,
               "target_lines": target_lines,
               "target_lines_text": fmt_lines(target_lines, text_lines),
               "r2_claimed_target_lines": R2_CLAIMED_TARGET_LINES.get(qualname),
               "r2_claim_matches_computed": (R2_CLAIMED_TARGET_LINES.get(qualname) == target_lines)}

        log = os.path.join(LOGDIR, f"r3_{tag}.log")
        open(log, "w").write("=== BASELINE MISSING IN FUNCTION RANGE ===\n" +
                             fmt_lines(target_lines, text_lines) + "\n")
        attempts = 0
        feedback = ""
        final_pass = final_fail = final_err = 0
        kept_names = []
        final_code = ""
        hit_state = "no"
        hit_detail = {}
        m = {}
        peak = 0.0
        for attempt in range(1, MAX_ATTEMPTS + 1):
            attempts = attempt
            prompt = build_prompt(src, imports, example, import_hint, method_note,
                                  numbered_src, target_lines, text_lines, feedback)
            resp, m, peak = ollama_generate(prompt)
            code = extract_code_block(resp)
            final_code = code
            tf = os.path.join(SANDBOX, f"test_r3_{tag}.py")
            open(tf, "w").write(code + "\n")
            # run under coverage so we can see which target lines executed
            out_c, j_c = coverage_run([os.path.basename(tf)], f"r3_{tag}_{attempt}")
            missing_now = target_missing(j_c, modpath, lo, hi)
            if missing_now is None:
                missing_now = list(target_lines)
            executed = [n for n in target_lines if n not in set(missing_now)]
            not_exec = [n for n in target_lines if n in set(missing_now)]
            if not target_lines:
                hit_state = "no-target"
            elif not not_exec:
                hit_state = "yes"
            elif executed:
                hit_state = "partial"
            else:
                hit_state = "no"
            hit_detail = {"executed": executed, "not_executed": not_exec}
            # also get per-test verbose status
            r = subprocess.run([VENVPY, "-m", "pytest", "-v", "-p", "no:cacheprovider",
                                os.path.basename(tf)],
                               cwd=SANDBOX, capture_output=True, text=True, env=ENV, timeout=300)
            vout = r.stdout + r.stderr
            pf, pa, pe, names = parse_pytest_verbose(vout)
            final_pass, final_fail, final_err = pf, pa, pe
            with open(log, "a") as fh:
                fh.write(f"\n=== ATTEMPT {attempt} ===\n" +
                         json.dumps({"tok_s": m.get("tokens_per_sec"),
                                     "wall_s": m.get("wall_s"),
                                     "peak_rss_mb": round(peak, 1),
                                     "pass": pf, "fail": pa, "error": pe,
                                     "target_hit": hit_state,
                                     "executed": executed,
                                     "not_executed": not_exec}, indent=1) +
                         "\n=== PROMPT ===\n" + prompt +
                         "\n=== RESPONSE ===\n" + resp +
                         "\n=== PYTEST ===\n" + vout)
            try:
                os.remove(tf)
                os.remove(j_c)
            except Exception:
                pass
            if pf > 0 and pa == 0 and pe == 0 and hit_state in ("yes", "no-target"):
                kept_names = names
                break
            # build feedback
            parts = []
            if pa or pe:
                parts.append("The previous test file did not pass. Pytest output:\n" +
                             vout[-1800:])
            if not_exec and pf > 0 and pa == 0 and pe == 0:
                parts.append("The tests passed but the target lines are still NOT executed: "
                             + ", ".join(str(n) for n in not_exec) +
                             ".\nYou must construct inputs that reach those exact statements:\n" +
                             fmt_lines(not_exec, text_lines) +
                             "\nRe-check the function source: what condition must hold for "
                             "those lines to run?")
            elif not_exec:
                parts.append("Target lines still not executed: " +
                             ", ".join(str(n) for n in not_exec) + ".")
            feedback = "\n\n".join(parts)
        # keep passing tests from the final attempt
        if not kept_names and final_pass > 0:
            kept_names = names
        tests_kept = len(kept_names)

        cov_after = None
        if tests_kept > 0:
            kept_code = write_kept(final_code, kept_names)
            tk = os.path.join(SANDBOX, f"test_kept3_{tag}.py")
            open(tk, "w").write(kept_code)
            out_a, j_a = coverage_run(["tests", os.path.basename(tk)], f"after3_{tag}")
            after_json = os.path.join(LOGDIR, f"after_r3_{tag}.json")
            subprocess.run(["cp", j_a, after_json], capture_output=True)
            cov_after = module_percent(after_json, modpath)
            for p in (tk, j_a, after_json):
                try:
                    os.remove(p)
                except Exception:
                    pass

        rec.update({
            "attempts": attempts,
            "pass": final_pass, "fail": final_fail, "error": final_err,
            "target_hit": hit_state,
            "target_executed": hit_detail.get("executed", []),
            "target_not_executed": hit_detail.get("not_executed", []),
            "tests_kept": tests_kept,
            "after_cov": cov_after,
            "cov_delta": (round(cov_after - baseline_pct, 2)
                          if (cov_after is not None and baseline_pct is not None) else None),
            "tok_s": m.get("tokens_per_sec"),
            "wall_s": m.get("wall_s"),
            "peak_rss_mb": round(peak, 1),
        })
        results.append(rec)
        print(json.dumps({k: rec[k] for k in
                          ("function", "attempts", "pass", "fail", "error", "target_hit",
                           "tests_kept", "baseline_cov", "after_cov", "cov_delta",
                           "tok_s", "wall_s")}, indent=None), flush=True)

    with open(os.path.join(ROOT, "results_r3.json"), "w") as fh:
        json.dump(results, fh, indent=1)
    print("\nLogs:", LOGDIR)


if __name__ == "__main__":
    main()
