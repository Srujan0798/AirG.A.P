# W3 — Workflow Wedge Selection

**Role:** Principal Product Architect  
**Task:** Compare candidate workflows for an offline agentic platform  
**Date:** 2026-11-11  
**Status:** Complete

## Verdict

**Recommended MVP: Test Generation** with a read-only Repository Understanding context layer. Second workflow: Defect Investigation. Third: Requirements Traceability.

Test Generation scores highest on the combined rubric because it produces reviewable output (diffable test code + patch proposals), runs entirely in a network-isolated sandbox on a non-production dataset, yields objective measurable value (coverage %, pass/fail, regression rate), and has strong local-model feasibility. It avoids autonomous control of live OT by construction — human approval is required before any write is merged or exported.

## Workflow scoring table (1–5; higher = more)

| Workflow | Pain | Freq | Value | Data | Review | Safety | Integration | Local Feas. | Procurement | Expansion |
|---|---|---|---|---|---|---|---|---|---|---|
| Repository Understanding | 4 | 4 | 4 | 5 | 2 | 2 | 3 | 5 | 3 | 5 |
| Requirements Traceability | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 |
| Code Modernization | 5 | 2 | 4 | 2 | 5 | 4 | 5 | 3 | 3 | 3 |
| Test Generation | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 4 | 3 | 4 |
| Defect Investigation | 5 | 3 | 4 | 3 | 4 | 4 | 4 | 3 | 3 | 4 |
| Document Intelligence | 3 | 3 | 3 | 4 | 2 | 2 | 3 | 5 | 2 | 3 |
| Engineering Change Mgmt | 4 | 3 | 4 | 3 | 5 | 4 | 5 | 3 | 4 | 4 |
| Model Lifecycle | 3 | 2 | 3 | 2 | 4 | 3 | 4 | 3 | 4 | 5 |

## Dimension notes

- **Test Generation** — Best measurable value (5): coverage delta, pass/fail, regression escapes are objective. High data availability (5): code+test+framework pairs abound. Review burden (3) is manageable because proposals are diffable. Local feasibility (4) — test generation is a well-solved local LLM task. Lowest safety risk among code-writing workflows when sandboxed.
- **Repository Understanding** — Best safety (2) and local feasibility (5), read-only by default. Foundation context layer for every other workflow. Value (4) is real but harder to monetize directly (comprehension is a means, not an end).
- **Code Modernization** — Highest pain (5) but lowest frequency (2), scarce legacy-language data (2), highest review burden (5), highest integration complexity (5). Too risky for MVP; defer.
- **Defect Investigation** — High pain (5) but incident-driven (3), unstructured log data (3), safety-critical if wrong (4). Strong follow-on after Test Generation.
- **Requirements Traceability** — High pain in regulated domains but scattered data (3) and high review burden (4). Slower sales cycle; good third workflow for defense/aerospace buyers.
- **Document Intelligence** — Easy locally (5), low burden (2), but lower measurable value (3). Knowledge-layer feature, not wedge.
- **Engineering Change Management** — High burden (5), integration (5), procurement (4). Too many stakeholders for a first wedge.
- **Model Lifecycle** — Expansion potential (5) but immature data (2), infrequent (2), hardware/procurement heavy (4). Platform layer, not customer wedge.

## Recommended MVP

**Scope:** Index a customer-approved, non-production repository and local docs (read-only by default). Given a bounded issue or function, propose tests and optionally a minimal patch. Execute tests in a disposable, network-isolated sandbox. Human reviews and approves before anything is merged or exported. Every result cites source locations, model/runtime versions, and tool calls.

**Why this wins:** reviewable output (diffable tests/patches), evaluable on non-production data, no live OT control, objective metrics, local-model feasible, feeds expansion into defect investigation and change-impact analysis.

## Explicit non-goals (first release)

- No autonomous changes to live power-grid, nuclear, medical, or industrial control systems (OT).
- No frontier foundation model training from scratch.
- No support for every model, GPU, OS, IDE, vertical, or deployment topology.
- No claim of full regulatory compliance or "zero data leakage."
- No replacement of human software engineers; humans approve all consequential actions.
- No shipping of 30 third-party skills as a runtime dependency.
- No custom hardware before customers demonstrate a requirement standard servers cannot meet.
- No silent subsystem replacement in legacy modernization; modernization is a follow-on, not MVP.

## Success metrics (Gate D)

- Test coverage delta on baseline task suite
- Engineer time per task vs. baseline
- Human review/correction effort per proposal
- Regression and escape rate
- Evidence traceability (each finding links to source, test, model version)
- Offline reliability (egress-blocked run success rate)
- Security-policy violations / denied action attempts

## Open questions

1. Which local model/runtime pair meets quality/latency/cost on the target hardware profile? (Gate B)
2. Which non-production repo and baseline task suite will the design partner provide? (Gate A/E)
3. What does the security approver require for artifact provenance, SBOM, and signed updates within the pilot boundary? (Gate C)
4. Does test generation alone carry enough willingness-to-pay, or must it bundle with defect investigation at pilot? (Gate E)
5. What is the acceptable human review effort threshold before the workflow is deemed uneconomic?

See WORKFLOW_WEDGE.md for full per-workflow rationale.
