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

ROLE: Enterprise Product Discovery Lead.

TASK: Determine which customer segment and workflow should be the initial wedge.

CANDIDATE VERTICALS: defense and aerospace suppliers; industrial/embedded software vendors; critical-infrastructure engineering teams; financial institutions; healthcare and research institutions; public-sector technology teams; other segments discovered independently.

METHOD:
- Build an interview guide that asks about current process before solution pitching.
- Identify user, champion, economic buyer, security approver and procurement path.
- Gather evidence of task frequency, consequence, current manual effort, existing substitutes, data boundaries, hardware and deployment restrictions.
- Score urgency, budget ownership, access, pilot feasibility, sales cycle and product repeatability.

OUTPUT: Ranked segments, evidence quality, interview questions, contradictions and one recommended initial customer profile. No market-size number without a cited methodology.

OUTPUT PATHS:
- Write your findings to harness/w2/REPORT.md — max ~150 lines: Verdict/summary, ranked segment table, evidence log, open questions.
- If detail runs long, put it in harness/w2/CUSTOMER_DISCOVERY.md and keep REPORT.md short.
- Append one line to harness/STATUS.log: "YYYY-MM-DD HH:MM | W2 | WAVE1-CUSTOMER <short description> | done"
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
