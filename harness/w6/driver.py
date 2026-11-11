#!/usr/bin/env python3
"""W6 feasibility driver: local model test generation, offline, measured.

Runs qwen2.5:7b (Ollama, local, no network after model load) to generate pytest
unit tests for 10 under-tested click functions, then runs them with coverage and
records pass/fail (generated tests only), coverage delta, tokens/sec, peak memory,
wall time.
"""
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
MODEL = "qwen2.5:7b"
OLLAMA_URL = "http://localhost:11434/api/generate"

os.makedirs(LOGDIR, exist_ok=True)

FUNCTIONS = [
    ("click.utils", "_posixify"),
    ("click.utils", "get_app_dir"),
    ("click._textwrap", "_truncate_visible"),
    ("click._textwrap", "TextWrapper.indent_only"),
    ("click._textwrap", "TextWrapper.extra_indent"),
    ("click.formatting", "measure_table"),
    ("click.formatting", "join_options"),
    ("click.exceptions", "_join_param_hints"),
    ("click.exceptions", "_format_possibilities"),
    ("click.utils", "make_str"),
]

FILEMAP = {
    "click.utils": "src/click/utils.py",
    "click._textwrap": "src/click/_textwrap.py",
    "click.formatting": "src/click/formatting.py",
    "click.exceptions": "src/click/exceptions.py",
}

ENV = dict(os.environ)
ENV["VIRTUAL_ENV"] = os.path.join(ROOT, "venv")
ENV["PATH"] = os.path.join(ROOT, "venv", "bin") + os.pathsep + ENV.get("PATH", "")
ENV["COVERAGE_FILE"] = os.path.join(LOGDIR, ".coverage")


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
    mod = __import__(modpath, fromlist=[parts[0]])
    obj = mod
    for p in parts:
        obj = getattr(obj, p)
    import inspect
    return inspect.getsource(obj)


def coverage_module_percent(json_path, modpath_key):
    try:
        with open(json_path) as fh:
            j = json.load(fh)
    except Exception:
        return None
    target = FILEMAP[modpath_key]
    files = j.get("files", {})
    if isinstance(files, dict):
        for path, info in files.items():
            if path.endswith(target):
                return info.get("summary", {}).get("percent_covered")
    else:
        for f in files:
            if f.get("filename", "").endswith(target):
                return f.get("summary", {}).get("percent_covered")
    return None


def coverage_run(args, data_suffix):
    """Parallel coverage run; writes .cov<suffix>.*. Returns pytest text."""
    datafile = os.path.join(LOGDIR, f".cov{data_suffix}")
    for f in os.listdir(LOGDIR):
        if f.startswith(f".cov{data_suffix}"):
            try:
                os.remove(os.path.join(LOGDIR, f))
            except Exception:
                pass
    e = dict(ENV)
    e["COVERAGE_FILE"] = datafile
    cmd = [VENVPY, "-m", "coverage", "run", "-p", "-m", "pytest", "-q", "-p", "no:cacheprovider"] + args
    r = subprocess.run(cmd, cwd=SANDBOX, capture_output=True, text=True, env=e, timeout=300)
    return r.stdout + r.stderr


def coverage_combine_and_json(out_json):
    covfiles = [os.path.join(LOGDIR, f) for f in os.listdir(LOGDIR) if f.startswith(".cov")]
    if covfiles:
        subprocess.run([VENVPY, "-m", "coverage", "combine"] + covfiles,
                       cwd=LOGDIR, capture_output=True, text=True, env=ENV, timeout=120)
    combined = os.path.join(LOGDIR, ".coverage")
    e = dict(ENV)
    e["COVERAGE_FILE"] = combined
    subprocess.run([VENVPY, "-m", "coverage", "json", "-o", out_json],
                   cwd=LOGDIR, capture_output=True, text=True, env=e, timeout=120)
    for f in covfiles:
        try:
            os.remove(f)
        except Exception:
            pass
    try:
        os.remove(combined)
    except Exception:
        pass


def parse_pytest(text):
    passed = failed = error = 0
    m = re.search(r"(\d+) passed", text)
    if m:
        passed = int(m.group(1))
    m = re.search(r"(\d+) failed", text)
    if m:
        failed = int(m.group(1))
    m = re.search(r"(\d+) error", text)
    if m:
        error = int(m.group(1))
    return passed, failed, error


def main():
    results = []
    # baseline: full existing suite coverage (parallel file .covbase)
    base_out = coverage_run(["tests"], "base")
    base_json = os.path.join(LOGDIR, "base.json")
    coverage_combine_and_json(base_json)
    baseline = {m: coverage_module_percent(base_json, m) for m in FILEMAP}

    for i, (modpath, qualname) in enumerate(FUNCTIONS, 1):
        tag = f"{i:02d}_{qualname.replace('.', '_')}"
        logpath = os.path.join(LOGDIR, f"{tag}.log")
        test_path = os.path.join(SANDBOX, f"test_gen_{tag}.py")
        try:
            src = source_for(modpath, qualname)
        except Exception as e:
            src = f"# SOURCE UNAVAILABLE: {e}"
        prompt = (
            "You are a test-generation engineer. Write pytest unit tests for the "
            "single Python function below. Output ONLY one python code block "
            "(```python ... ```). Tests must be deterministic, use no network, "
            "no secrets, and avoid platform-specific assertions where possible. "
            "Import what you need from click. Function source:\n\n" + src
        )
        resp, metrics, peak_rss = ollama_generate(prompt)
        code = extract_code_block(resp)
        with open(test_path, "w") as fh:
            fh.write(code + "\n")
        with open(logpath, "w") as fh:
            fh.write("=== PROMPT ===\n" + prompt + "\n\n=== MODEL RESPONSE ===\n" + resp +
                     "\n\n=== METRICS ===\n" + json.dumps(metrics, indent=1) +
                     f"\npeak_rss_mb={round(peak_rss,1)}\n")
        # generated-tests-only pass/fail (no coverage)
        r = subprocess.run([VENVPY, "-m", "pytest", "-q", "-p", "no:cacheprovider", test_path],
                           cwd=SANDBOX, capture_output=True, text=True, env=ENV, timeout=300)
        g_passed, g_failed, g_error = parse_pytest(r.stdout + r.stderr)
        # coverage after: full suite (parallel) + generated test (parallel), then combine
        cov_full = coverage_run(["tests"], f"full{i}")
        cov_gen = coverage_run([test_path], f"gen{i}")
        after_json = os.path.join(LOGDIR, f"after_{tag}.json")
        coverage_combine_and_json(after_json)
        before = baseline.get(modpath)
        after = coverage_module_percent(after_json, modpath)
        results.append({
            "n": i, "function": qualname, "module": modpath, "file": FILEMAP[modpath],
            "gen_passed": g_passed, "gen_failed": g_failed, "gen_error": g_error,
            "before_cov": before, "after_cov": after,
            "cov_delta": (round(after - before, 1) if (after is not None and before is not None) else None),
            "tokens_per_sec": metrics.get("tokens_per_sec"),
            "total_s": metrics.get("total_duration_s"),
            "wall_s": metrics.get("wall_s"),
            "peak_rss_mb": round(peak_rss, 1),
            "log": logpath,
        })
        try:
            os.remove(test_path)
        except Exception:
            pass
        for p in (after_json,):
            if os.path.exists(p):
                os.remove(p)

    print(f"{'#':>2} {'function':32} {'g_pass':>6} {'g_fail':>6} {'g_err':>6} {'cov_b':>7} {'cov_a':>7} {'d_cov':>6} {'tok/s':>7} {'wall_s':>7} {'peakMB':>7}")
    for r in results:
        print(f"{r['n']:>2} {r['function']:32} {r['gen_passed']:>6} {r['gen_failed']:>6} {r['gen_error']:>6} "
              f"{str(r['before_cov']):>7} {str(r['after_cov']):>7} {str(r['cov_delta']):>6} "
              f"{str(r['tokens_per_sec']):>7} {r['wall_s']:>7} {r['peak_rss_mb']:>7}")
    with open(os.path.join(ROOT, "results.json"), "w") as fh:
        json.dump(results, fh, indent=1)
    print("\nLogs:", LOGDIR)
    print("Baseline module coverage:", {k: (round(v, 1) if v is not None else None) for k, v in baseline.items()})


if __name__ == "__main__":
    main()
