# W6 REPORT — Local Model Test Generation Feasibility (Offline)

**Verdict: marginal.** A local open-weight model runs fully offline on this Mac at ~40 tok/s and produces plausible pytest, but only ~10 of ~30 generated test cases pass; 4 files fail collection and many assertions are wrong (platform assumptions, unimported names). Coverage delta = 0.0 on every module. Feasible to RUN offline; output requires human review — consistent with the human-approval design in `01 §5` / `04 §12`. Not useful unsupervised; marginal as a Day-1 wedge without review gating.

## Model (grade A — measured via Ollama API)
- `qwen2.5:7b` → Qwen2.5-7B-Instruct, Q4_K_M, 4.68 GB (≤5 GB cap), digest `845dbda0ea48...`
- Licence: Qwen model licence, commercial use permitted — https://huggingface.co/Qwen/Qwen2.5-7B-Instruct (grade C)
- Runtime: Ollama `http://localhost:11434/api/generate`, non-streaming, `num_predict=512, temperature=0.2`. No network used for generation.

## Repo (grade A — cloned)
- https://github.com/pallets/click (BSD-3), 10 under-tested functions (0 refs in `tests/`).

## Results (all 10 runs, grade A — measured)

| # | function | pass | fail | err | tok/s | wall_s | peakRSS MB |
|---|----------|------|------|-----|-------|--------|------------|
| 1 | _posixify | 1 | 0 | 0 | 40.3 | 3.35 | 344 |
| 2 | get_app_dir | 0 | 0 | 1 | 40.6 | 13.16 | 372 |
| 3 | _truncate_visible | 0 | 9 | 0 | 41.0 | 8.63 | 421 |
| 4 | indent_only | 1 | 0 | 0 | 41.2 | 5.78 | 382 |
| 5 | extra_indent | 0 | 0 | 1 | 41.6 | 7.93 | 368 |
| 6 | measure_table | 0 | 0 | 1 | 41.1 | 8.83 | 385 |
| 7 | join_options | 0 | 0 | 1 | 39.6 | 10.68 | 372 |
| 8 | _join_param_hints | 4 | 1 | 0 | 41.0 | 5.11 | 383 |
| 9 | _format_possibilities | 0 | 5 | 0 | 39.5 | 8.54 | 374 |
| 10 | make_str | 4 | 1 | 0 | 40.8 | 7.27 | 385 |

**Totals: 10 pass / 16 fail / 4 collection errors.** Coverage before = after on every module (delta 0.0); baseline `click.utils` 79.0, `_textwrap` 73.2, `formatting` 94.5, `exceptions` 86.4.

## Failure modes
1. Collection errors: generated tests reference unimported names / have syntax errors → pytest aborts.
2. Wrong assertions: platform-specific expectations (Windows paths on macOS), incorrect return values → fail.
3. Non-determinism: same function re-generated gives different pass/fail counts.
4. Zero coverage delta: existing suite already covers the exercised lines.

## Hardware for a lab
- Model 4.68 GB Q4_K_M → provision ≥ 8 GB RAM (model + KV cache + OS). Measured ollama/llama RSS 344–421 MB during generation; on-disk model size is the binding constraint.
- ~40 tok/s, wall 3–13 s/function. CPU-only sufficient (no GPU); Apple Silicon or x86-64 AVX2.
- Fully offline after model load.

## Evidence
- `harness/w6/results.json`, `harness/w6/logs/*.log`, `harness/w6/driver.py` (grade A).
- FEASIBILITY.md has full table and every command used.

## Open questions
1. Does a larger/quantised-differently coding model (e.g. Qwen2.5-Coder-7B) materially improve pass rate at acceptable tok/s on this hardware? (Gate B in `01 §9`)
2. What human-review-effort threshold makes test generation economic? (`03 §5` Gate D)
3. Can retrieval over the repo (symbols, docstrings) improve test correctness enough to pass Gate A?

---

## Round 2 — context + repair loop (qwen2.5-coder:7b) (grade A — measured)

**Round-2 verdict: marginally better, still not useful unsupervised.** Adding module imports, the correct import hint, one existing repo test as a style example, and a 3-attempt repair loop lifted generated tests from 0 pass (round 1, measured generated-only) to 14 passing / 14 kept tests across 5 of 10 functions; collection errors dropped 6→2. Coverage delta stayed ≈0.0 (only `BadParameter.format_message` +0.9), because the existing suite already covers these lines. Output still requires human review — consistent with the human-approval design in `01 §5` / `04 §12`. Not useful unsupervised; marginal as a Day-1 wedge without review gating. Full table and every command: `harness/w6/FEASIBILITY_R2.md`.

### Round 1 vs Round 2 (same 10 functions, same hardware, generated tests only)

| Measure | Round 1 (one-shot, source only) | Round 2 (context + import hint + repair, max 3 att) |
|---|---|---|
| Model | qwen2.5:7b (4.68 GB) | qwen2.5-coder:7b (4.68 GB) |
| Generated tests pass | 0 | 14 |
| Generated tests fail | 9 | 9 |
| Collection errors | 6 | 2 |
| Tests kept (pass final attempt) | n/a | 14 |
| Functions with ≥1 kept test | 0 | 5 of 10 |
| Coverage delta (best) | 0.0 | +0.9 (`BadParameter.format_message`) |
| Tokens/sec | ~38-41 | ~39-41 |
| Peak RSS during gen | ~344-421 MB | ~4.7 GB (model fully resident) |

Round 1 re-measured generated-only (excluding the pre-existing suite): 0 pass / 9 fail / 6 collection error. The round-1 table above is kept intact as originally measured.

### Round 2 hardware implication for a lab
- Model 4.68 GB Q4_K_M → provision ≥ 8 GB RAM. Peak ollama/llama RSS ≈ 4.7 GB (model fully resident); on-disk model size is the binding constraint.
- ~39-41 tok/s; wall 3–15 s/function. CPU-only sufficient (no GPU); Apple Silicon or x86-64 AVX2.
- Fully offline after model load.

### Round 2 evidence
- `harness/w6/results_r2.json`, `harness/w6/logs/r1_*.log`, `r2_*.log`, `harness/w6/driver_r2.py` (grade A).
- `harness/w6/FEASIBILITY_R2.md` — full table and every command.

### Open questions (unchanged, plus round-2)
1. Does repair-loop context (imports, examples) plus a coding model raise the kept-test rate enough to pass Gate A on real customer code?
2. What human-review-effort threshold makes test generation economic? (`03 §5` Gate D)
3. Can retrieval over the repo (symbols, docstrings) improve test correctness enough to pass Gate A?

