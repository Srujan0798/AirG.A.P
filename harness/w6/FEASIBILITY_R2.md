# W6 FEASIBILITY_R2 — Context + Repair-Loop Test Generation (Offline)

**Round:** WAVE2-FEASIBILITY-R2 (round 2 of W6)  
**Model:** qwen2.5-coder:7b (Qwen2.5-Coder-7B-Instruct), Q4_K_M, 4.68 GB, digest `dae161e27b0e90dd`  
**Licence:** Apache-2.0, commercial use permitted — https://huggingface.co/Qwen/Qwen2.5-Coder-7B (grade C)  
**Runtime:** Ollama `http://localhost:11434/api/generate`, non-streaming, `num_predict=512, temperature=0.2` — fully offline after model load (grade A)  
**Repo:** https://github.com/pallets/click (BSD-3), `harness/w6/sandbox/click` (grade A)

## Design

Each target function has uncovered lines per coverage.py baseline.
- Round 1 (one-shot): function source only → generate tests → run pytest → record.
- Round 2 (context + repair): function source + module imports + correct import hint + one existing repo test as style example → generate → run pytest in sandbox; on failure/collection error, send error back to model; max 3 attempts. Keep only tests that pass on the final attempt; measure coverage delta of kept tests.

## Commands used

```
ollama pull qwen2.5-coder:7b                            # one new model, 4.68 GB ≤ 5 GB cap
. venv/bin/activate
python3 -m coverage run -m pytest -q -p no:cacheprovider tests   # baseline coverage
python3 -m coverage json -o base.json                    # baseline module coverage
curl -s -X POST http://localhost:11434/api/generate \
  -d '{"model":"qwen2.5-coder:7b","prompt":"...","stream":false}'   # per attempt
python3 -m pytest -v -p no:cacheprovider test_r2_XX.py   # per attempt (verbose)
# kept tests re-run under coverage:
python3 -m coverage run -m pytest -q -p no:cacheprovider tests test_kept_XX.py
python3 -m coverage json -o after.json
```
Driver: `harness/w6/driver_r2.py`. Raw logs: `harness/w6/logs/r1_*.log` and `r2_*.log`. Results: `harness/w6/results_r2.json`.

## Per-function results (grade A — measured)

| # | function | uncovered lines (baseline) | R1 pass/fail/err | R2 att | R2 pass/fail/err | kept | cov_before | cov_after | delta | r2 tok/s | r2 wall_s | r2 peak MB |
|---|----------|---------------------------|------------------|--------|------------------|------|------------|-----------|-------|----------|-----------|------------|
| 1 | _join_param_hints | [21] | 0/0/1 | 3 | 2/1/0 | 2 | 86.43 | 86.43 | 0.0 | 41.9 | 3.41 | 4711 |
| 2 | TextWrapper._handle_long_word | [63,64] | 0/2/0 | 3 | 0/2/0 | 0 | 73.20 | — | — | 40.1 | 5.59 | 4780 |
| 3 | wrap_text | [80] | 0/0/1 | 3 | 2/3/0 | 2 | 94.47 | 94.47 | 0.0 | 40.2 | 10.04 | 4820 |
| 4 | EchoingStdin.readline | [79] | 0/4/0 | 3 | 0/0/1 | 0 | 95.54 | — | — | 41.0 | 2.70 | 4706 |
| 5 | make_input_stream | [245] | 0/0/1 | 1 | 5/0/0 | 5 | 95.54 | 95.54 | 0.0 | 41.4 | 7.13 | 4743 |
| 6 | custom_version_option | [585] | 0/0/1 | 3 | 0/1/0 | 0 | 79.21 | — | — | 40.2 | 4.18 | 4799 |
| 7 | BadParameter.format_message | [148,152] | 0/3/0 | 2 | 3/0/0 | 3 | 86.43 | 87.33 | +0.9 | 39.4 | 5.47 | 4720 |
| 8 | ParamType.convert | [203] | 0/5/0 | 1 | 2/0/0 | 2 | 87.56 | 87.56 | 0.0 | 37.7 | 10.13 | 4773 |
| 9 | _make_default_short_help | [33] | 0/0/1 | 3 | 0/1/1 | 0 | 78.96 | — | — | 39.4 | 9.76 | 4801 |
| 10 | confirmation_option | [389-401] | 0/1/0 | 3 | 0/1/0 | 0 | 79.21 | — | — | 32.4 | 6.09 | 4767 |

**Totals:** Round 1 generated-only: 0 pass / 9 fail / 6 collection error. Round 2 final attempt: 14 pass / 9 fail / 2 error; 14 tests kept; 5 of 10 functions with ≥1 kept test. Coverage delta +0.9 on one function, 0.0 on the rest (kept tests exercise already-covered lines).

## Failure modes observed (grade A — measured)

1. Collection errors (round 1: 6; round 2: 2): wrong import module (`from click.utils import _join_param_hints` when it lives in `click.exceptions`), missing imports, syntax errors → pytest aborts collection.
2. Wrong assertions: platform-specific expectations, incorrect return values → fail.
3. Methods need instantiation (`TextWrapper()._handle_long_word(...)`) — model often calls as bare function.
4. Coverage delta ≈ 0: existing suite already covers the exercised lines; generated tests add little new coverage.

## Hardware implication for a lab

- Model artifact 4.68 GB Q4_K_M → provision ≥ 8 GB RAM. Peak ollama/llama RSS during generation ≈ 4.7 GB (model fully resident); on-disk model size is the binding constraint.
- ~39-41 tok/s; wall 3-15 s/function. CPU-only sufficient (no GPU); Apple Silicon or x86-64 AVX2.
- Fully offline after model load.

## Evidence

- `harness/w6/results_r2.json` — per-run numbers (grade A).
- `harness/w6/logs/r1_*.log`, `r2_*.log` — prompt, response, metrics, pytest output per run (grade A).
- `harness/w6/driver_r2.py` — measurement harness (grade A).
