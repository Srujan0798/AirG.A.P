# W6 — Feasibility: Local Model Test Generation (Offline)

**Project:** AI for the Air-Gapped Economy  
**Window:** W6 (task WAVE2-FEASIBILITY)  
**Role:** Enterprise Product Discovery Lead (adversarial feasibility check)  
**Date:** 2026-11-11  
**Grade key:** A = measured/test · B = independent eval · C = vendor page · D = inference

## Verdict (preview)

**Marginal.** A local open-weight model (qwen2.5-7b Q4_K_M) runs fully offline on this Mac at ~40 tok/s and produces syntactically plausible pytest, but only ~10 of ~30 generated test cases pass; several files fail collection (missing imports / platform assumptions) and many assertions are wrong. Coverage delta = 0 (existing suite already covers these modules). The model is feasible to RUN offline, but its test output requires human review — consistent with the human-approval design in `01 §5` / `04 §12`. Not yet useful unsupervised; marginal as a Day-1 wedge without review gating.

## Model used (grade A — measured via Ollama API)

- Name: `qwen2.5:7b` (Ollama) → Qwen2.5-7B-Instruct
- Size: 4.68 GB (≤ 5 GB cap ✓); quantisation Q4_K_M
- Digest: `845dbda0ea48...`
- Licence: Qwen model licence, commercial use permitted — https://huggingface.co/Qwen/Qwen2.5-7B-Instruct (grade C)
- Runtime: Ollama REST API `http://localhost:11434/api/generate` (non-streaming), `num_predict=512, temperature=0.2`
- Runs entirely local after model load; no network used for generation (grade A).

## Target repo (grade A — cloned)

- https://github.com/pallets/click, BSD-3 licence, cloned `--depth 1` into `harness/w6/sandbox/click`
- 10 under-tested functions chosen (0 references in `tests/`): see table below.

## Commands used

```
git clone --depth 1 https://github.com/pallets/click.git        # into harness/w6/sandbox/
python3 -m venv venv
. venv/bin/activate && pip install -e sandbox/click coverage pytest
nohup ollama serve > /tmp/ollama_serve.log 2>&1 &               # local inference server
curl -s -X POST http://localhost:11434/api/generate \
  -d '{"model":"qwen2.5:7b","prompt":"...","stream":false}'     # test generation (per function)
python3 -m pytest -q -p no:cacheprovider test_gen_XX.py         # generated tests only (pass/fail)
coverage run -p -m pytest tests                                 # baseline suite (coverage before)
coverage run -p -m pytest tests test_gen_XX.py                  # suite + generated test (coverage after)
coverage combine && coverage json -o after.json                 # merged coverage report
```

Driver: `harness/w6/driver.py` (orchestrates prompt → model → test file → pytest → coverage, per function). Raw output per run saved to `harness/w6/logs/01__posixify.log` … `10_make_str.log`.

## Results table (all 10 runs)

| # | function | module | gen_pass | gen_fail | gen_err | cov_before | cov_after | delta | tok/s | wall_s | peak RSS MB |
|---|----------|--------|----------|----------|---------|------------|-----------|-------|-------|--------|-------------|
| 1 | _posixify | click.utils | 1 | 0 | 0 | 78.96 | 78.96 | 0.0 | 40.3 | 3.35 | 344 |
| 2 | get_app_dir | click.utils | 0 | 0 | 1 | 78.96 | 78.96 | 0.0 | 40.6 | 13.16 | 372 |
| 3 | _truncate_visible | click._textwrap | 0 | 9 | 0 | 73.20 | 73.20 | 0.0 | 41.0 | 8.63 | 421 |
| 4 | TextWrapper.indent_only | click._textwrap | 1 | 0 | 0 | 73.20 | 73.20 | 0.0 | 41.2 | 5.78 | 382 |
| 5 | TextWrapper.extra_indent | click._textwrap | 0 | 0 | 1 | 73.20 | 73.20 | 0.0 | 41.6 | 7.93 | 368 |
| 6 | measure_table | click.formatting | 0 | 0 | 1 | 94.47 | 94.47 | 0.0 | 41.1 | 8.83 | 385 |
| 7 | join_options | click.formatting | 0 | 0 | 1 | 94.47 | 94.47 | 0.0 | 39.6 | 10.68 | 372 |
| 8 | _join_param_hints | click.exceptions | 4 | 1 | 0 | 86.43 | 86.43 | 0.0 | 41.0 | 5.11 | 383 |
| 9 | _format_possibilities | click.exceptions | 0 | 5 | 0 | 86.43 | 86.43 | 0.0 | 39.5 | 8.54 | 374 |
| 10 | make_str | click.utils | 4 | 1 | 0 | 78.96 | 78.96 | 0.0 | 40.8 | 7.27 | 385 |

**Totals:** 10 pass / 16 fail / 4 collection errors across generated tests. Coverage delta 0.0 on every module (existing `tests/` suite already covers these lines; generated tests add no new module coverage).

Baseline module coverage (grade A, measured): `click.utils` 79.0, `click._textwrap` 73.2, `click.formatting` 94.5, `click.exceptions` 86.4.

## Failure modes observed (grade A — measured)

1. **Collection errors (4):** generated test files reference names never imported (e.g. `get_app_dir` used without `from click.utils import get_app_dir`) or have syntax errors → pytest aborts collection.
2. **Wrong assertions (most failures):** tests encode platform-specific expectations (Windows paths on macOS), incorrect return values, or wrong parameter counts → fail on this machine.
3. **Non-determinism:** re-running generation for the same function yields different pass/fail counts (e.g. `make_str` 5 pass/3 fail → 4 pass/1 fail).
4. **Zero coverage delta:** even passing generated tests exercise lines already covered by the existing suite, so measured delta is 0.

## Hardware implication for a lab

- Model artifact: 4.68 GB (Q4_K_M); provision ≥ 8 GB RAM (model + KV cache + OS overhead). Measured ollama/llama process RSS during generation: 344–421 MB (process-resident; model on-disk size is the binding constraint).
- ~40 tok/s on this Mac; generation wall time 3–13 s per function. CPU-only is sufficient (no GPU required), Apple Silicon or x86-64 with AVX2.
- Fully offline after model load: no network needed for inference (grade A).

## Evidence log

- `harness/w6/results.json` — per-run numbers (grade A).
- `harness/w6/logs/*.log` — prompt, raw model response, metrics, peak RSS per run (grade A).
- `harness/w6/driver.py` — measurement harness (grade A).
- Model/licence/source: ollama API, HuggingFace Qwen page, GitHub pallets/click (grades A/C).
