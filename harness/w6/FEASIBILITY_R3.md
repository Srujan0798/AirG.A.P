# W6 FEASIBILITY_R3 — Coverage-Guided Test Generation (Offline)

**Round:** WAVE2-FEASIBILITY-R3 (round 3 of W6)
**Model:** qwen2.5-coder:7b (Qwen2.5-Coder-7B-Instruct), Q4_K_M, 4.68 GB, Ollama id `dae161e27b0e`
**Licence:** Apache-2.0, commercial use permitted — https://huggingface.co/Qwen/Qwen2.5-Coder-7B (grade C)
**Runtime:** Ollama `http://localhost:11434/api/generate`, non-streaming, `num_predict=512, temperature=0.2` — fully offline after model load (grade A)
**Repo:** https://github.com/pallets/click (BSD-3), `harness/w6/sandbox/click` (grade A)
**No new downloads.** Same model, same 10 functions, same sandbox as round 2.

## Design change vs round 2

Round 2 proved the repair loop works but coverage barely moved, because **nothing told the
model which lines to hit**. Round 3 adds a *coverage-guided* loop:

1. Compute, per function, the lines **not executed by the repo's own test suite**
   (intersection of coverage.py's missing lines with the function's line range).
2. Put those exact line numbers **and their source text** in the prompt.
3. After every attempt, run the generated tests **under coverage.py** and check which
   target lines executed.
4. If the tests pass but the target lines still did not execute, send back
   *"lines X-Y still not executed"* plus the code of those lines, and retry.
5. Max 4 attempts.

Round 2's two systematic prompt errors are fixed:

- **Correct import path** is stated per function (`from <module> import <name>`), derived
  from the resolved module, not guessed.
- **Method vs function** is stated explicitly: for a method the prompt says
  *"it is a METHOD. You must create an instance first (e.g. `obj = ClassName(...)`) and
  then call `obj.method(...)`. Calling `method(...)` as a bare function will fail."*

## Commands used

```
# no download: model already present
ollama list                                     # qwen2.5-coder:7b  dae161e27b0e  4.7GB
ollama show qwen2.5-coder:7b                    # quantization Q4_K_M, licence Apache 2.0
cat ~/.ollama/models/manifests/registry.ollama.ai/library/qwen2.5-coder/7b   # layer digests

# baseline coverage of the repo's own suite (per-function uncovered lines)
. venv/bin/activate
python -m coverage run -m pytest -q -p no:cacheprovider tests
python -m coverage json -o logs/base_r3.json

# per attempt: generate, then run under coverage, then check target-line execution
curl -s -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen2.5-coder:7b","prompt":"<coverage-guided prompt>","stream":false,
       "options":{"num_predict":512,"temperature":0.2}}'

python -m coverage run -m pytest -q -p no:cacheprovider test_r3_<fn>.py
python -m coverage json -o logs/.json_r3_<fn>_<n>
# -> missing_lines of the target module intersected with the function's line range
#    => executed = target_lines - missing_now

# per attempt, verbose per-test status
python -m pytest -v -p no:cacheprovider test_r3_<fn>.py

# coverage after: repo suite + kept generated tests
python -m coverage run -m pytest -q -p no:cacheprovider tests test_kept3_<fn>.py
python -m coverage json -o logs/after_r3_<fn>.json

# driver (all of the above)
./venv/bin/python driver_r3.py
```

Driver: `harness/w6/driver_r3.py`. Logs: `harness/w6/logs/r3_*.log` (prompt, response,
metrics, pytest output, per attempt) and `logs/r3_driver.out`. Results:
`harness/w6/results_r3.json`.

## Per-function results (grade A — measured)

| # | function | target lines | att | p/f/e | target hit | kept | cov before | cov after | delta | tok/s | wall s | peak MB |
|---|----------|--------------|-----|-------|-----------|------|------------|-----------|-------|--------|-------|--------|
| 1 | _join_param_hints | [21] | 1 | 1/0/0 | **yes** | 1 | 86.43 | 87.33 | **+0.90** | 41.7 | 8.14 | 4806 |
| 2 | TextWrapper._handle_long_word | [63, 64] | 2 | 1/0/0 | **yes** | 1 | 73.20 | 75.82 | **+2.61** | 38.3 | 3.92 | 4806 |
| 3 | wrap_text | [80] | 4 | 0/1/0 | no | 0 | 94.47 | — | — | 37.2 | 2.40 | 4806 |
| 4 | EchoingStdin.readline | [79] | 4 | 0/1/0 | no | 0 | 95.54 | — | — | 39.3 | 2.13 | 4806 |
| 5 | make_input_stream | [245] | 4 | 0/1/0 | no | 0 | 95.54 | — | — | 40.2 | 1.88 | 4806 |
| 6 | custom_version_option | [585] | 4 | 0/1/0 | no | 0 | 79.21 | — | — | 38.3 | 2.09 | 4806 |
| 7 | BadParameter.format_message | [148, 152] | 1 | 2/0/0 | **yes** | 2 | 86.43 | 88.24 | **+1.81** | 39.9 | 3.72 | 4806 |
| 8 | ParamType.convert | [203] | 1 | 1/0/0 | **yes** | 1 | 87.56 | 87.71 | **+0.15** | 39.5 | 2.85 | 4806 |
| 9 | _make_default_short_help | *(none)* | 4 | 0/1/0 | n/a | 0 | 78.96 | — | — | 35.1 | 6.32 | 4806 |
| 10 | confirmation_option | [389,390,391,393,394,396,397,398,399,400,401] | 4 | 0/0/1 | no | 0 | 79.21 | — | — | 39.5 | 6.20 | 4806 |

**Totals:** 29 attempts (max 4). Final attempts: 5 pass / 4 fail / 1 collection error.
**5 tests kept across 4 of 10 functions. Every kept test moved coverage** (sum of deltas
on the four hits = **+5.47**). 4 of 10 functions reached their target lines; 6 produced
nothing usable.

## Target-line computation correction (round 2 data error)

Round 2's report table listed uncovered lines per function but the round-2 driver never
computed function-scoped missing lines. Round 3 computes them properly. Comparing:

- 8 of 10 functions match round 2's claim exactly.
- **`_make_default_short_help`: round 2 claimed line [33]. Line 33 is the body of
  `_posixify` in `click/utils.py`. `_make_default_short_help` occupies lines 62–100 and
  has *no* uncovered lines — the repo's own suite already covers it.** Round 2's
  attribution was wrong; round 3 reports `n/a` for this function.
- `confirmation_option`: round 2 claimed the contiguous range 389–401; coverage.py reports
  11 uncovered lines (392 and 395 are not flagged).

Both facts are recorded in `results_r3.json` (`r2_claimed_target_lines`,
`r2_claim_matches_computed`, `r2_claim_note`).

## Failure modes (grade A — measured)

Error census across all 29 attempts:

| Error | Count | Concentrated in |
|---|---|---|
| ImportError (collection) | 7 | `confirmation_option` — every attempt |
| NameError | 13 | `make_input_stream` (5), `EchoingStdin.readline` (7), `wrap_text` (1) |
| AttributeError | 13 | `custom_version_option` (7), `wrap_text` (6) |
| AssertionError | 7 | `_make_default_short_help` (5), `_handle_long_word` (2) |
| SyntaxError | 2 | `_make_default_short_help` |

**The dominant failure mode is scaffolding, not reasoning.** 4 of the 5 functions that
failed to hit their target failed on import or API-surface errors:

- `make_input_stream` — `NameError: name 'pytest' is not defined`. The model used
  `pytest.raises` but **the prompt never asked it to import pytest**.
- `EchoingStdin.readline` — `NameError: name 'io' is not defined`. Missing stdlib import.
- `wrap_text` — `NameError: name 'wrap_text' is not defined`, i.e. it dropped the import
  it was explicitly told to use.
- `confirmation_option` — `ImportError: cannot import name 'option' from 'click.core'`.
  Wrong import path for the decorator.

Scanning the 10 model responses: **only 1 of 10 included `import pytest`.** The other 9
worked only because they needed no pytest construct.

**This is the load-bearing result of round 3.** The model demonstrably understood *what
to target* — the coverage guidance worked, and hits came in 1–2 attempts. What it does
not reliably do is emit boilerplate scaffolding. That is a **control-plane responsibility,
not a model responsibility**: the harness must inject `import pytest`, the exact target
import, and the test scaffolding deterministically, and ask the model only for the
arrangement that reaches the target line.

## Hardware implication for a lab

- Model artifact 4.68 GB Q4_K_M → provision ≥ 8 GB RAM. Peak ollama/llama RSS ≈ 4.8 GB
  during generation (model fully resident); on-disk model size is the binding constraint.
- 35.1–41.7 tok/s; wall 1.9–8.1 s per attempt. CPU-only sufficient (no GPU); Apple
  Silicon or x86-64 AVX2.
- Fully offline after model load. No API keys needed.

## Round 1 → 2 → 3

| Measure | R1 (one-shot, source only) | R2 (context + repair, max 3) | R3 (coverage-guided, max 4) |
|---|---|---|---|
| Model | qwen2.5:7b | qwen2.5-coder:7b | qwen2.5-coder:7b |
| Tests passing (final attempt) | 0 | 14 | 5 |
| Tests kept | n/a | 14 | 5 |
| Functions with ≥1 kept test | 0 | 5 of 10 | 4 of 10 |
| **Functions where kept tests moved coverage** | 0 of 10 | **1 of 10** | **4 of 10** |
| Coverage delta | 0.0 everywhere | +0.9 on one function | **+0.15 … +2.61, sum +5.47 on four functions** |
| Attempts | 10 | ≤30 | 29 |
| Tokens/sec | ~40 | ~39–41 | 35–42 |

**Fewer passing tests than round 2, but each one is worth more.** Round 2's 14 kept tests
added ≈ 0 coverage because they re-exercised already-covered lines. Round 3's 5 kept
tests all moved coverage. For a product whose evaluator *is* coverage, round 3 is the
better result.

## Gate B verdict across all three rounds

**Still not passed, but the blocker is now named and fixable.**

- Gate B (`01_MASTER_VISION_AND_STRATEGY.md` §9) requires useful quality/latency/cost on
  **actual customer hardware**. This is one Mac, one 4.68 GB model, a 10-function toy
  benchmark on a mature open-source repo. It is not customer hardware and it is not
  customer code.
- **Usability for the Day-1 workflow: still marginal, gated on human review.** 6 of 10
  functions produced nothing usable. 5 usable tests from 29 attempts is not a throughput
  a team would accept unsupervised.
- **But the trend is decisive and in the right direction.** Coverage-directed feedback is
  what turns "generates plausible tests" into "generates tests that move coverage":
  1/10 → 4/10. When the model hit a target it did so in 1–2 attempts at ~40 tok/s.
- **And the remaining blocker is deterministic, not probabilistic.** 4 of 5 misses were
  missing/wrong imports. Injecting `import pytest` + the exact target import
  deterministically is a control-plane change, not a model improvement. Round 4 should
  test exactly that: model supplies only the test body, harness supplies the scaffolding.

**Recommendation:** proceed with offline test generation as the Day-1 workflow **only**
with the human approval gate that is already designed into `01 §5`, and only after a
round 4 that moves scaffolding into the control plane and re-measures on the same 10
functions. Do not present current numbers as "useful unsupervised".

## Evidence

- `harness/w6/results_r3.json` — per-run numbers incl. target lines, executed/not-executed, R2 cross-reference (grade A).
- `harness/w6/logs/r3_*.log` — prompt, response, metrics, pytest output, per attempt (grade A).
- `harness/w6/logs/r3_driver.out` — driver stdout, per-function result lines (grade A).
- `harness/w6/driver_r3.py` — measurement harness (grade A).
