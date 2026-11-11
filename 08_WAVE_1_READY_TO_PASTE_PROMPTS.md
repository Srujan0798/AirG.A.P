# 08 — Wave 1 Ready-to-Paste Prompts

**Purpose:** The four Wave 1 prompts from `07_NEXT_STEPS_DISPATCH_PROTOCOL.md`, copied verbatim from `02_INDEPENDENT_RESEARCH_AGENT_PROTOCOLS.md` so they can be pasted directly to the founder's own agent without reopening `02`.

**Handoff note:** The founder assigns these; the orchestrator (Claude, this project's boss/strategist) reviews what comes back, checks sourcing against the evidence-grade schema in `02` §6, and synthesizes before anything reaches a pitch deck.

---

## Prompt 1 — Competitor and substitute analyst

```text
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
```

## Prompt 2 — Customer discovery and vertical selection

```text
ROLE: Enterprise Product Discovery Lead.

TASK: Determine which customer segment and workflow should be the initial wedge.

CANDIDATE VERTICALS: defense and aerospace suppliers; industrial/embedded software vendors; critical-infrastructure engineering teams; financial institutions; healthcare and research institutions; public-sector technology teams; other segments discovered independently.

METHOD:
- Build an interview guide that asks about current process before solution pitching.
- Identify user, champion, economic buyer, security approver and procurement path.
- Gather evidence of task frequency, consequence, current manual effort, existing substitutes, data boundaries, hardware and deployment restrictions.
- Score urgency, budget ownership, access, pilot feasibility, sales cycle and product repeatability.

OUTPUT: Ranked segments, evidence quality, interview questions, contradictions and one recommended initial customer profile. No market-size number without a cited methodology.
```

## Prompt 3 — Workflow and product wedge analyst

```text
ROLE: Principal Product Architect.

TASK: Compare candidate workflows for an offline agentic platform: repository understanding, requirements traceability, code modernization, test generation, defect investigation, document intelligence, engineering change management, model lifecycle and other validated workflows.

For each workflow score: pain intensity, task frequency, measurable value, data availability, human review burden, safety criticality, integration complexity, local model feasibility, procurement barrier and expansion potential.

Recommend an MVP with explicit non-goals. Prefer a workflow that can be evaluated on a non-production dataset and produces reviewable output. Avoid autonomous control of live OT in the first release.
```

## Prompt 4 — Adversarial investment committee

```text
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
```
