#!/usr/bin/env python3
"""W6 round 2: context + repair-loop test generation, offline.

Per function (each has uncovered lines per coverage.py):
  Round 1 (one-shot): function source only -> generate tests -> run -> record aggregate.
  Round 2 (context+repair): function source + module imports + one existing test
      example -> generate -> run pytest in sandbox; on failure/collection error,
      send error back; max 3 attempts. Keep only tests that pass on the final
      attempt; measure coverage delta of kept tests.
Record: attempts, final pass/fail/error, tests kept, coverage before/after,
tok/s, wall. Fully offline via Ollama (qwen2.5-coder:7b).
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
        return "", {"error": r.stdout[:500], "wall": wall}, peak[0]
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


def source_for(modpath, qualname):
    parts = qualname.split(".")
    mod = importlib.import_module(modpath)
    obj = mod
    for p in parts:
        obj = getattr(obj, p)
    return inspect.getsource(obj)


def module_imports(modpath):
    mod = importlib.import_module(modpath)
    path = mod.__file__
    imports = []
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("import ") or line.startswith("from "):
                imports.append(line)
    return imports


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
        return "# (no existing test references this function in repo)"
    p, txt = min(hits, key=lambda x: len(x[1]))
    tree = ast.parse(txt)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
            body = ast.get_source_segment(txt, node) or ""
            if name in body:
                return body
    return txt[:800]


def coverage_module_percent(json_path, modpath):
    try:
        with open(json_path) as fh:
            j = json.load(fh)
    except Exception:
        return None
    target = "src/click/" + modpath.split(".")[-1] + ".py"
    files = j.get("files", {})
    if isinstance(files, dict):
        for path, info in files.items():
            if path.endswith(target):
                return info.get("summary", {}).get("percent_covered")
    return None


def coverage_run(args):
    datafile = os.path.join(LOGDIR, f".cov{os.getpid()}_{int(time.time()*1000)}")
    try:
        os.remove(datafile)
    except Exception:
        pass
    e = dict(ENV)
    e["COVERAGE_FILE"] = datafile
    cmd = [VENVPY, "-m", "coverage", "run", "-m", "pytest", "-q", "-p", "no:cacheprovider"] + args
    r = subprocess.run(cmd, cwd=SANDBOX, capture_output=True, text=True, env=e, timeout=300)
    out = r.stdout + r.stderr
    jpath = os.path.join(LOGDIR, f".json{os.getpid()}")
    e2 = dict(ENV)
    e2["COVERAGE_FILE"] = datafile
    subprocess.run([VENVPY, "-m", "coverage", "json", "-o", jpath],
                   cwd=LOGDIR, capture_output=True, text=True, env=e2, timeout=120)
    try:
        os.remove(datafile)
    except Exception:
        pass
    return out, jpath


def parse_pytest_verbose(text):
    """Return (passed, failed, error, kept_test_names)."""
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
    # fallback aggregate if verbose not used
    if passed == 0 and failed == 0 and error == 0:
        ma = re.search(r"(\d+) passed", text)
        if ma:
            passed = int(ma.group(1))
        ma = re.search(r"(\d+) failed", text)
        if ma:
            failed = int(ma.group(1))
        ma = re.search(r"(\d+) error", text)
        if ma:
            error = int(ma.group(1))
    return passed, failed, error, kept


def build_prompt_round1(src):
    return (
        "You are a test-generation engineer. Write pytest unit tests for the "
        "single Python function below. Output ONLY one python code block "
        "(```python ... ```). Tests must be deterministic, use no network, "
        "no secrets. Import what you need from click. Function source:\n\n" + src
    )


def build_prompt_round2(src, imports, example, import_hint, feedback=""):
    imp = "\n".join(imports) if imports else "# (no import lines found)"
    fb = ("\n\nPREVIOUS ATTEMPT ERRORS (fix these):\n" + feedback) if feedback else ""
    return (
        "You are a test-generation engineer. Write pytest unit tests for the "
        "single Python function below. Output ONLY one python code block "
        "(```python ... ```). Tests must be deterministic, use no network, "
        "no secrets. Import what you need from click. Match the style of the "
        "existing test example.\n\nModule imports available:\n" + imp +
        "\nCorrect import for the function under test:\n" + import_hint +
        "\n\nExisting test style example:\n" + example + fb +
        "\n\nFunction source:\n\n" + src
    )


def write_kept(code, kept_names):
    """Extract only kept test functions from code."""
    tree = ast.parse(code)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in kept_names:
            out.append(ast.get_source_segment(code, node))
    # add imports from top of code
    imports = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.get_source_segment(code, node))
    return "\n".join(imports + out) + "\n"


def main():
    results = []
    base_out, base_j = coverage_run(["tests"])
    base_json = os.path.join(LOGDIR, "base_r2.json")
    subprocess.run(["cp", base_j, base_json], capture_output=True)
    baseline = {m: coverage_module_percent(base_json, m) for m, _ in TARGETS}

    for modpath, qualname in TARGETS:
        tag = qualname.split(".")[-1]
        src = source_for(modpath, qualname)
        imports = module_imports(modpath)
        example = find_test_example(modpath, qualname)
        rec = {"module": modpath, "function": qualname,
               "baseline_cov": baseline.get(modpath)}

        # ---- Round 1: one-shot, source only ----
        r1log = os.path.join(LOGDIR, f"r1_{tag}.log")
        resp1, m1, peak1 = ollama_generate(build_prompt_round1(src))
        code1 = extract_code_block(resp1)
        t1 = os.path.join(SANDBOX, f"test_r1_{tag}.py")
        open(t1, "w").write(code1 + "\n")
        r = subprocess.run([VENVPY, "-m", "pytest", "-v", "-p", "no:cacheprovider", t1],
                           cwd=SANDBOX, capture_output=True, text=True, env=ENV, timeout=300)
        p1f, p1a, p1e, _ = parse_pytest_verbose(r.stdout + r.stderr)
        with open(r1log, "w") as fh:
            fh.write("=== ROUND1 PROMPT ===\n" + build_prompt_round1(src) +
                     "\n=== RESPONSE ===\n" + resp1 + "\n=== METRICS ===\n" +
                     json.dumps(m1, indent=1) + f"\npeak_rss_mb={round(peak1,1)}\n" +
                     "\n=== PYTEST ===\n" + (r.stdout + r.stderr))
        rec["r1_pass"] = p1f
        rec["r1_fail"] = p1a
        rec["r1_error"] = p1e
        rec["r1_tok_s"] = m1.get("tokens_per_sec")
        rec["r1_wall_s"] = m1.get("wall_s")
        try:
            os.remove(t1)
        except Exception:
            pass

        # ---- Round 2: context + repair loop (max 3 attempts) ----
        r2log = os.path.join(LOGDIR, f"r2_{tag}.log")
        top_name = qualname.split(".")[0]
        import_hint = f"from {modpath} import {top_name}"
        prompt = build_prompt_round2(src, imports, example, import_hint)
        attempts = 0
        feedback = ""
        final_pass = final_fail = final_err = 0
        kept_names = []
        final_code = ""
        for attempt in range(1, 4):
            attempts = attempt
            resp, m, peak = ollama_generate(build_prompt_round2(src, imports, example, import_hint, feedback))
            code = extract_code_block(resp)
            final_code = code
            t2 = os.path.join(SANDBOX, f"test_r2_{tag}.py")
            open(t2, "w").write(code + "\n")
            r = subprocess.run([VENVPY, "-m", "pytest", "-v", "-p", "no:cacheprovider", t2],
                               cwd=SANDBOX, capture_output=True, text=True, env=ENV, timeout=300)
            out = r.stdout + r.stderr
            pf, pa, pe, names = parse_pytest_verbose(out)
            final_pass, final_fail, final_err = pf, pa, pe
            with open(r2log, "a") as fh:
                fh.write(f"\n=== ATTEMPT {attempt} ===\n" +
                         json.dumps({"tok_s": m.get("tokens_per_sec"), "wall_s": m.get("wall_s"),
                                     "peak_rss_mb": round(peak, 1)}, indent=1) +
                         "\n=== RESPONSE ===\n" + resp + "\n=== PYTEST ===\n" + out)
            if pf > 0 and pa == 0 and pe == 0:
                kept_names = names
                break
            feedback = out[-1500:]
            try:
                os.remove(t2)
            except Exception:
                pass
        # If no fully-clean attempt, keep passing tests from the final attempt
        if not kept_names and final_pass > 0:
            t2 = os.path.join(SANDBOX, f"test_r2_{tag}.py")
            open(t2, "w").write(final_code + "\n")
            r = subprocess.run([VENVPY, "-m", "pytest", "-v", "-p", "no:cacheprovider", t2],
                               cwd=SANDBOX, capture_output=True, text=True, env=ENV, timeout=300)
            _, _, _, kept_names = parse_pytest_verbose(r.stdout + r.stderr)
        tests_kept = len(kept_names)

        # coverage after: full suite + kept tests
        cov_after = None
        if tests_kept > 0:
            kept_code = write_kept(final_code, kept_names)
            tk = os.path.join(SANDBOX, f"test_kept_{tag}.py")
            open(tk, "w").write(kept_code)
            out_a, j_a = coverage_run(["tests", tk])
            after_json = os.path.join(LOGDIR, f"after_r2_{tag}.json")
            subprocess.run(["cp", j_a, after_json], capture_output=True)
            cov_after = coverage_module_percent(after_json, modpath)
            try:
                os.remove(tk); os.remove(j_a); os.remove(after_json)
            except Exception:
                pass

        rec["r2_attempts"] = attempts
        rec["r2_pass"] = final_pass
        rec["r2_fail"] = final_fail
        rec["r2_error"] = final_err
        rec["r2_tests_kept"] = tests_kept
        rec["r2_after_cov"] = cov_after
        rec["r2_cov_delta"] = (round(cov_after - baseline[modpath], 1)
                               if (cov_after is not None and baseline.get(modpath) is not None) else None)
        rec["r2_tok_s"] = m.get("tokens_per_sec")
        rec["r2_wall_s"] = m.get("wall_s")
        rec["r2_peak_rss_mb"] = round(peak, 1)
        results.append(rec)

    print(f"{'function':34} {'r1p':>4} {'r1f':>4} {'r1e':>4} | {'r2att':>4} {'r2p':>4} {'r2f':>4} {'r2e':>4} {'kept':>4} | {'cov_b':>7} {'cov_a':>7} {'dcov':>6} | {'r2tok':>6} {'r2wall':>6} {'r2MB':>6}")
    for r in results:
        print(f"{r['function']:34} {r['r1_pass']:>4} {r['r1_fail']:>4} {r['r1_error']:>4} | "
              f"{r['r2_attempts']:>4} {r['r2_pass']:>4} {r['r2_fail']:>4} {r['r2_error']:>4} {r['r2_tests_kept']:>4} | "
              f"{str(r['baseline_cov']):>7} {str(r['r2_after_cov']):>7} {str(r['r2_cov_delta']):>6} | "
              f"{str(r['r2_tok_s']):>6} {str(r['r2_wall_s']):>6} {str(r['r2_peak_rss_mb']):>6}")
    with open(os.path.join(ROOT, "results_r2.json"), "w") as fh:
        json.dump(results, fh, indent=1)
    print("\nLogs:", LOGDIR)


if __name__ == "__main__":
    main()
