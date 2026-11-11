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

## Prompt 2 — Customer discovery and vertical selection (validation mode)

**Superseded 2026-11-11:** `09_INITIAL_WEDGE_DISCOVERY.md` already answers this task (dated 30 Oct 2026, zero interviews). Per the founder's decision, W2 validates that document instead of starting fresh — see `harness/PASTES.md` for the exact paste in use.

```text
ROLE: Enterprise Product Discovery Lead, acting as adversarial validator — not a fresh researcher.

CONTEXT: A document already exists at 09_INITIAL_WEDGE_DISCOVERY.md (project root) that claims to answer this exact task (customer segment + workflow wedge selection), dated 30 October 2026, zero customer interviews completed. Your job is to validate and stress-test that document, not redo it from scratch.

TASK:
1. Read 09_INITIAL_WEDGE_DISCOVERY.md in full, and re-read 01_MASTER_VISION_AND_STRATEGY.md section 9 (Gates A-E) and section 10 (execution sequence) that it claims to satisfy.
2. For each of the following in 09, judge SOLID / WEAK / UNSUPPORTED, with your reasoning: the role-identification matrix (section 2), the scoring rubric (section 4), the ranked segments (section 5), the contradictions/open risks list (section 6), and the recommended ICP (section 7).
3. Independently check: does the chosen ICP (defense/aerospace isolated engineering lab, change-impact-analysis workflow) actually follow from the scoring rubric as applied, or does it look like the conclusion was picked first and the scores fitted to match? Show your own re-scoring of the top 3 segments using 09's own rubric (section 4) and say whether you land on the same rank order.
4. Identify what evidence 09 is missing that real interviews (per its own section 1 interview guide) would be needed to confirm — list the single most load-bearing unvalidated claim.
5. Only produce NEW segment/workflow analysis if you find 09's reasoning is unsupported and a different segment should lead instead. Do not duplicate work that already exists and holds up.

OUTPUT: A validation verdict (ACCEPT AS-IS / ACCEPT WITH FLAGGED GAPS / REJECT — redo needed), your re-scoring table, the single most load-bearing unvalidated claim, and — only if REJECT — an alternative ranked-segment analysis. No market-size number without a cited methodology.
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
