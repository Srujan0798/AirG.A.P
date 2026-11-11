# Harness Paste Board — Wave 1

One ACTIVE block per window. Copy the whole block (including the "You are W#" line) into one idle OpenCode window. See `harness/BOSS_GUIDE.md` for the convention.

---

## ACTIVE — W1

```text
You are W1. This text is the only task.

ROLE: B2B Infrastructure Market Intelligence Lead.

TASK: Map direct competitors, adjacent platforms, open-source substitutes and customer-built alternatives for air-gapped AI and secure engineering automation.

COVER:
- Enterprise model/inference platforms.
- Offline Kubernetes and container management.
- Local coding assistants and autonomous coding agents.
- Secure software development, artifact and SBOM platforms.
- Enterprise search/knowledge and domain model products.
- System integrators and hardware appliance vendors.

For each solution record: buyer, workflow, deployment/isolation mode, offline support evidence, model/runtime, agent capabilities, security/identity, integrations, updates, license, support model, pricing evidence, limitations and customer proof. Do not call a product a direct competitor if it solves a different layer. Identify gaps only after checking docs and tests.

For every claim, record source title, URL, date accessed and an evidence grade (A/B/C/D per the schema in 02_INDEPENDENT_RESEARCH_AGENT_PROTOCOLS.md section 6 of the project root).

OUTPUT PATHS:
- Write your findings to harness/w1/REPORT.md — max ~150 lines: Verdict/summary, competitor matrix table, evidence log, open questions.
- If the full matrix is longer, put the complete version in harness/w1/COMPETITOR_MATRIX.md and keep REPORT.md as the short version.
- Append one line to harness/STATUS.log: "YYYY-MM-DD HH:MM | W1 | WAVE1-COMPETITOR <short description> | done"
- End by printing: "W1 done gates=PASS blocked=<none|list>"
```

---

## ACTIVE — W2

```text
You are W2. This text is the only task.

ROLE: Enterprise Product Discovery Lead, acting as adversarial validator — not a fresh researcher.

CONTEXT: A document already exists at 09_INITIAL_WEDGE_DISCOVERY.md (project root) that claims to answer this exact task (customer segment + workflow wedge selection), dated 30 October 2026, zero customer interviews completed. Your job is to validate and stress-test that document, not redo it from scratch.

TASK:
1. Read 09_INITIAL_WEDGE_DISCOVERY.md in full, and re-read 01_MASTER_VISION_AND_STRATEGY.md section 9 (Gates A-E) and section 10 (execution sequence) that it claims to satisfy.
2. For each of the following in 09, judge SOLID / WEAK / UNSUPPORTED, with your reasoning: the role-identification matrix (section 2), the scoring rubric (section 4), the ranked segments (section 5), the contradictions/open risks list (section 6), and the recommended ICP (section 7).
3. Independently check: does the chosen ICP (defense/aerospace isolated engineering lab, change-impact-analysis workflow) actually follow from the scoring rubric as applied, or does it look like the conclusion was picked first and the scores fitted to match? Show your own re-scoring of the top 3 segments using 09's own rubric (section 4) and say whether you land on the same rank order.
4. Identify what evidence 09 is missing that real interviews (per its own section 1 interview guide) would be needed to confirm — list the single most load-bearing unvalidated claim.
5. Only produce NEW segment/workflow analysis if you find 09's reasoning is unsupported and a different segment should lead instead. Do not duplicate work that already exists and holds up.

OUTPUT: A validation verdict (ACCEPT AS-IS / ACCEPT WITH FLAGGED GAPS / REJECT — redo needed), your re-scoring table, the single most load-bearing unvalidated claim, and — only if REJECT — an alternative ranked-segment analysis. No market-size number without a cited methodology.

OUTPUT PATHS:
- Write your findings to harness/w2/REPORT.md — max ~150 lines: verdict, re-scoring table, load-bearing claim, open questions.
- If detail runs long, put it in harness/w2/CUSTOMER_DISCOVERY_VALIDATION.md and keep REPORT.md short.
- Append one line to harness/STATUS.log: "YYYY-MM-DD HH:MM | W2 | WAVE1-CUSTOMER-VALIDATION <short description> | done"
- End by printing: "W2 done gates=PASS blocked=<none|list>"
```

---

## ACTIVE — W3

```text
You are W3. This text is the only task.

ROLE: Principal Product Architect.

TASK: Compare candidate workflows for an offline agentic platform: repository understanding, requirements traceability, code modernization, test generation, defect investigation, document intelligence, engineering change management, model lifecycle and other validated workflows.

For each workflow score: pain intensity, task frequency, measurable value, data availability, human review burden, safety criticality, integration complexity, local model feasibility, procurement barrier and expansion potential.

Recommend an MVP with explicit non-goals. Prefer a workflow that can be evaluated on a non-production dataset and produces reviewable output. Avoid autonomous control of live OT in the first release.

OUTPUT PATHS:
- Write your findings to harness/w3/REPORT.md — max ~150 lines: Verdict/summary, workflow scoring table, recommended MVP + non-goals, open questions.
- If detail runs long, put it in harness/w3/WORKFLOW_WEDGE.md and keep REPORT.md short.
- Append one line to harness/STATUS.log: "YYYY-MM-DD HH:MM | W3 | WAVE1-WORKFLOW <short description> | done"
- End by printing: "W3 done gates=PASS blocked=<none|list>"
```

---

## ACTIVE — W4

```text
You are W4. This text is the only task.

ROLE: Independent red-team investment committee. Your task is to argue against the startup recommendation.

CHALLENGE:
- Is the pain real, frequent and funded?
- Is it already solved by NVIDIA, Red Hat, existing coding assistants, integrators or internal teams?
- Is the chosen wedge too broad or too hard to certify?
- Does offline model quality meet useful engineering thresholds?
- Is the founder/team able to sell into the market?
- Are there hidden costs in deployment, support, hardware and security?
- Does the product have a moat or just integration work?
- Could a customer solve this with a local model plus existing tools?

Return the five strongest reasons not to build, the evidence for each, what would change your mind, the narrowest viable pivot and a clear go / conditional go / no-go verdict.

OUTPUT PATHS:
- Write your findings to harness/w4/REPORT.md — max ~150 lines: the five reasons with evidence, go/conditional-go/no-go verdict, narrowest pivot.
- If detail runs long, put it in harness/w4/ADVERSARIAL_REVIEW.md and keep REPORT.md short.
- Append one line to harness/STATUS.log: "YYYY-MM-DD HH:MM | W4 | WAVE1-ADVERSARIAL <short description> | done"
- End by printing: "W4 done gates=PASS blocked=<none|list>"
```
