# W2 Validation Report — 09_INITIAL_WEDGE_DISCOVERY.md

**Verdict:** ACCEPT WITH FLAGGED GAPS (not REJECT — no alternative segment analysis warranted; margin between top segments is within the noise of an ambiguous rubric).

**Scope:** Re-read `09_INITIAL_WEDGE_DISCOVERY.md` in full, plus `01_MASTER_VISION_AND_STRATEGY.md` §9 (Gates A–E) and §10 (execution sequence). Zero customer interviews exist in either document; all segment claims are unvalidated hypotheses, which `09` correctly acknowledges.

---

## 1. Section-by-section judgments

| Section | Judgment | Reasoning |
|---------|----------|-----------|
| §1 Interview guide | SOLID | Current-process-first rule is explicit; every question maps to an evidence domain and a role; contradiction probes (D1–D4) are well-chosen. Satisfies `01 §10` first-2-weeks interview intent. |
| §2 Role-identification matrix | WEAK | Plausible archetypes but generic (titles, not validated names); not tied to the product's specific constraints (offline, air-gapped, artifact provenance, human approval). Note admits they're hypotheses. Useful as a starting framework, not evidence. |
| §3 Evidence capture template | SOLID | Clean 1–5 scale per domain; captures exactly what interviews need to produce. |
| §4 Scoring rubric | WEAK | Formula is hand-wavy: "Composite = (...) normalized; Urgency and Budget double-weighted" but double-weighting is not reflected in any shown arithmetic. "Normalized" is undefined. Sales Cycle and Repeatability are scored 1–5 where 5 = worse, then subtracted — internally consistent but never operationalized with actual numbers. |
| §5 Ranked segments | UNSUPPORTED | No per-dimension score table; no arithmetic; "Composite (hypothetical)" column is just High/Medium-high labels with no derivation. Cannot verify that Defense/Aerospace actually ranks #1 from the rubric. |
| §6 Contradictions & open risks | SOLID | Honest, well-reasoned tensions (C1–C5) between founder intent and segment reality. Strongest section of the document. |
| §7 Recommended ICP | WEAK/UNSUPPORTED | Detailed and plausible, but reads like the conclusion (Defense/Aerospace, change-impact-analysis) was picked first and the rubric fitted to match. The "Why this segment first" paragraph repeats founder-language from `01` rather than deriving from shown scores. |

---

## 2. Re-scoring top 3 segments using 09's own rubric (section 4)

Rubric: score each dimension 1–5. Sales Cycle and Repeatability are risk factors (5 = worse), subtracted. Urgency and Budget intended double-weighted (not reflected in formula, shown both ways below).

Raw composite = (Urgency + Budget + Access + PilotFeasibility) − (SalesCycle + Repeatability)
Double-weighted composite = (2×Urgency + 2×Budget + Access + PilotFeasibility) − (SalesCycle + Repeatability)

| Segment | Urgency | Budget | Access | PilotFeas. | SalesCycle | Repeatability | Raw | 2×U/B |
|---------|---------|--------|--------|------------|------------|---------------|-----|-------|
| Industrial/embedded software vendors | 3 | 4 | 4 | 4 | 3 | 4 | 15 | 15 |
| Defense & aerospace suppliers | 4 | 4 | 2 | 3 | 5 | 3 | 13 | 13 |
| Critical-infrastructure engineering | 4 | 3 | 2 | 2 | 5 | 2 | 11 | 11 |

**Result:** Using the rubric as written, Industrial/embedded vendors edge out Defense/Aerospace (15 vs 13 raw; tied at 13 double-weighted). The rank order is **not robust** — it swings with subjective scores and the ambiguous weighting. Crucially, `09` shows none of this arithmetic, so we cannot confirm its claimed #1 rank (Defense/Aerospace) follows from the rubric at all. The conclusion appears picked first (consistent with `01` founder intent leaning defense/aerospace) and scores fitted after.

**Decision:** Because the top-two margin (15 vs 13) is within scoring noise and the rubric is ambiguous, I do NOT flip the recommendation or produce a new ranked-segment analysis. The document remains a reasonable hypothesis baseline — but its rank order must be treated as unvalidated ordering, not rubric-derived fact.

---

## 3. Single most load-bearing unvalidated claim

> **"Defense & aerospace suppliers rank #1 on the composite (urgency × budget ownership × access × pilot feasibility ÷ sales cycle × repeatability risk)."**

Everything downstream — the recommended ICP (defense/aerospace isolated lab, change-impact-analysis workflow), the fast-follow choice (industrial/embedded), and the first-2-weeks interview prioritization — hinges on this claim. If interviews confirm that defense's access/sales-cycle penalties (clearance, long procurement, multi-prime flow-down) dominate its urgency/budget advantage, the wedge collapses to Industrial/embedded vendors. This is the claim that must be confirmed or falsified first (≥3 defense interviews + ≥3 industrial interviews per `01 §10` and `09 §8`).

---

## 4. Evidence missing before the rank order can be trusted (per `09 §1` interview guide)

- Actual urgency scores per segment: frequency (A2) and consequence (A4) of change-impact work, not assumed.
- Actual budget ownership: named allocatable owner and budget cycle (B2), especially whether defense program money is truly available for new tooling vs. locked to existing contracts.
- Actual access: whether decision-makers are reachable and willing to pilot (B5), vs. clearance/NDA gates that block entry.
- Actual pilot feasibility: isolated non-production repo + hardware (C3), vs. classification preventing any external tool on lab hardware.
- Actual sales cycle: lead time from evaluation to signed PO (B4) — defense may be 12+ months as scored, but this needs confirmation.
- Contradiction checks (D1–D4): do teams already have adequate substitutes? Do developers bypass the "no external AI" policy anyway?

---

## 5. Open questions

1. Does the double-weighting of Urgency/Budget actually change the rank order, or is it decorative? `09` must define the formula precisely and show the math.
2. If defense access/sales-cycle penalties dominate, should Industrial/embedded vendors become the lead wedge with defense as fast-follow?
3. What is the minimum viable pilot scope that satisfies Gate C (threat model, no-egress, artifact verification) without expanding beyond the MVP boundary (`01 §5`)?
4. Which workflow (change-impact vs. codebase understanding vs. requirements traceability) has the highest confirmed frequency+consequence in the lead segment?

---

## 6. Methodology compliance

- No market-size, TAM/SAM/SOM, or willingness-to-pay figure appears in this report; none will be produced without a cited sizing methodology (consistent with `09 §9`).
- All scores above are illustrative re-scorings using `09`'s own rubric, not customer-validated evidence.

---

**Appended to `harness/STATUS.log`.** Next: run `09 §8` step 1 (15–25 interviews across top 3 segments) and re-rank only after evidence, per `09 §7.3` / `01 §9 Gate A`.
