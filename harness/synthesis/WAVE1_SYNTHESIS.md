# Wave 1 Synthesis — FINAL

All four windows done, reviewed, logged in `harness/kb/reviews.jsonl`. Full reports: `harness/w1/REPORT.md`, `harness/w2/REPORT.md`, `harness/w3/REPORT.md`, `harness/w4/REPORT.md`.

## The one finding that changes the pitch

**W1 (competitor map, 38 solutions surveyed, evidence-graded):** no product in the surveyed set directly competes with "secure offline agentic engineering workbench" — but that's because **every layer underneath it is already occupied** (inference: NVIDIA NIM/vLLM/llama.cpp/SGLang; disconnected clusters: OpenShift/RKE2/K3s/GDC; SBOM/supply chain: Anchore/Sonatype/GitLab; local coding agents: Cline/Continue/LocalPilot/Sovereign/LocalCode/DeskAI — all free or commodity, none enterprise-governed).

**The real gap, found with Grade A/C evidence across multiple independent vendors:** nobody has a published identity model, RBAC, immutable approval ledger, provenance-checked asset intake, or standardized offline update path for this kind of system. Seven vendors each hand-rolled their own disconnected-update mechanism — nobody has solved it generally.

**This means the product is not "an agentic workbench."** It's **the governance + lifecycle control plane that sits around a replaceable local agent** — deterministic policy, provenance, audit, in-boundary updates, accreditation evidence. This is a sharper, more defensible claim than anything in the original `01` framing, and it's independently consistent with W4's "the moat is integration work, not the agent" finding and `01`'s own "a swarm of agents is not a moat" principle.

**Caveat, stated plainly:** W1's own summary counts are internally inconsistent (header says 27 solutions, STATUS.log says a breakdown summing to 33, the actual table has 38 rows) — the qualitative finding is solid and well-sourced, but don't quote an exact "N competitors surveyed" number in the pitch without a recount.

## How all four windows now fit together

| Window | Finding | Status |
|---|---|---|
| W1 | No direct competitor; real gap is the governance/lifecycle layer, not the agent layer | Accepted, count-flag noted |
| W2 | `09`'s Defense/Aerospace #1 ranking is plausible but not rubric-derived; Industrial/embedded is a near-tie (15 vs 13) | Accepted with flagged gaps |
| W3 | Test Generation is the strongest MVP workflow (reviewable, sandboxable, measurable) — not change-impact-analysis | Accepted |
| W4 | NO-GO on the full workbench as constituted; narrowest pivot = one read-only codebase-understanding/change-impact tool | Accepted |

**Resolved tension:** W1 gives W4's "narrowest pivot" a sharper target. The pivot isn't just "smaller scope" — it's specifically **the control-plane layer**, which W1 shows is unoccupied, versus the agent/inference/cluster layers, which W1 shows are saturated. Pitch: narrow in workflow (per W3/W4), sharp in positioning (per W1), honest on segment (per W2/09 — still open).

**Unresolved, by design — founder's call:** which segment to lead with in the pitch (Defense/Aerospace vs. Industrial/embedded). Evidence is genuinely close; interviews settle it, not more analysis.

## What changes in the PPT

- Slide 4 ("what we're building") sharpens from generic "agentic workbench" to "governed control plane around a replaceable local agent."
- Slide 7 ("why the honesty is the pitch") gains a concrete, evidence-backed differentiation claim instead of a hypothesis.
- Slide 8 (competitor landscape) now has real content.
