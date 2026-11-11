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


---

## Round 3 — coverage-guided loop (qwen2.5-coder:7b) (grade A — measured)

**Round-3 verdict: marginal, materially improved, blocker now named and deterministic.**
Telling the model *which exact lines are uncovered* (with their source text) and feeding
back *"lines X-Y still not executed"* between attempts converts the loop from "generates
plausible tests" into "generates tests that move coverage". Functions where the kept
tests actually moved coverage went **1 of 10 (round 2) → 4 of 10 (round 3)**. Kept-test
count fell (14 → 5) but every kept test in round 3 moved coverage, whereas round 2's 14
added ≈ 0. Sum of coverage deltas on the four hits: **+5.47**.

Still **not** Gate B passed: 6 of 10 functions produced nothing usable, and this is one
Mac on a 10-function toy benchmark, not customer hardware.

**The load-bearing finding:** the dominant failure mode is *scaffolding, not reasoning*.
4 of the 5 misses were missing or wrong imports — `NameError: name 'pytest' is not
defined`, `NameError: name 'io' is not defined`, the model dropping the import it was
told to use, and `ImportError: cannot import name 'option' from 'click.core'`. Scanning
the 10 model responses, **only 1 of 10 imported pytest** — the prompt never asked for it.
The model understood *what to target* (hits came in 1–2 attempts); it does not reliably
emit boilerplate. That is a **control-plane responsibility**: the harness must inject
`import pytest`, the exact target import and the test scaffolding, and ask the model only
for the arrangement that reaches the target line. This is the strongest empirical
support yet for the "deterministic control plane over a replaceable agent" positioning
(`harness/w7/MOAT.md`).

### Round 1 vs Round 2 vs Round 3

| Measure | R1 (one-shot, source only) | R2 (context + repair, max 3 att) | R3 (coverage-guided, max 4 att) |
|---|---|---|---|
| Model | qwen2.5:7b | qwen2.5-coder:7b | qwen2.5-coder:7b |
| Tests passing (final attempt) | 0 | 14 | 5 |
| Tests kept | n/a | 14 | 5 |
| Functions with ≥1 kept test | 0 | 5 of 10 | 4 of 10 |
| **Functions where kept tests moved coverage** | 0 of 10 | **1 of 10** | **4 of 10** |
| Coverage delta | 0.0 everywhere | +0.9 on one function | **+0.15 … +2.61 (sum +5.47)** |
| Attempts | 10 | ≤30 | 29 |
| Tokens/sec | ~40 | ~39–41 | 35–42 |
| Peak RSS during gen | ~344–421 MB | ~4.7 GB | ~4.8 GB |

### Round 3 data correction to round 2

Round 3 computes function-scoped uncovered lines properly; round 2's driver never did.
8 of 10 functions match round 2's claim exactly. **`_make_default_short_help`: round 2
claimed line [33], but line 33 is the body of `_posixify` in `click/utils.py`;
`_make_default_short_help` (lines 62–100) has no uncovered lines — the repo's own suite
already covers it.** Round 3 reports `n/a`. `confirmation_option`: round 2 claimed the
contiguous range 389–401; coverage.py reports 11 uncovered lines (392 and 395 are not
flagged). Both recorded in `results_r3.json`.

### Final Gate B verdict across all three rounds

**Not passed — but the blocker is named, deterministic, and fixable.**

1. **Gate B is not passed.** It requires useful quality/latency/cost on *actual customer
   hardware*; this is one Mac, one 4.68 GB model, a 10-function toy benchmark on a mature
   open-source repo (`01_MASTER_VISION_AND_STRATEGY.md` §9).
2. **Still marginal for Day-1, gated on human review.** 6 of 10 functions produced
   nothing usable; 5 usable tests from 29 attempts is not throughput anyone accepts
   unsupervised. Consistent with the human-approval design in `01 §5` / `04 §12`.
3. **The direction is decisive.** Coverage-directed feedback is what makes this a
   *coverage* product rather than a *text* product: 1/10 → 4/10 functions with real
   coverage gain.
4. **The remaining blocker is deterministic, not probabilistic.** 4 of 5 misses were
   imports. A control-plane change (inject scaffolding) should convert most of them.
   **Round 4 should test exactly that** — model supplies the test body only, harness
   supplies the scaffolding — and re-measure on the same 10 functions.
5. **Do not present current numbers as "useful unsupervised."**

### Round 3 evidence
- `harness/w6/results_r3.json`, `harness/w6/logs/r3_*.log`, `harness/w6/logs/r3_driver.out`, `harness/w6/driver_r3.py` (grade A).
- `harness/w6/FEASIBILITY_R3.md` — full table, every command, failure-mode census, round 1–2–3 comparison.
