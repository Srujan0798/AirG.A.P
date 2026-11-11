# 06 — Customized Hybrid Engineering Methodology & Startup Execution System

**Purpose:** Combine traditional systems engineering, independent research, agentic workflows, plugin-assisted development and custom integrations into one repeatable product-building method.

---

## 1. The decision: customized hybrid, not “traditional versus plugins”

The final approach is not a 50/50 blend or an instruction to install every plugin. It is a division of responsibility:

- **Traditional engineering owns correctness, authority, state, safety, security and operations.**
- **AI agents own bounded reasoning, synthesis, code proposals, analysis and selected parallel work.**
- **Plugins accelerate specific developer tasks but remain replaceable.**
- **Research discovers better methods and challenges existing decisions.**
- **Custom integration connects proven capabilities into a coherent system.**
- **Evaluation decides whether the combination is actually better.**

This is the engineering ideology that matches the founder's stated intent while avoiding plugin dependence.

## 2. Hybrid operating architecture

| Concern | Traditional foundation | Agent/plugin leverage | Final hybrid form |
|---|---|---|---|
| Product definition | Requirements, stakeholder analysis, measurable outcomes. | Product-discovery agents, planning skills. | Evidence-backed PRD with explicit assumptions and decision log. |
| Architecture | Boundaries, interfaces, state machines, threat models, ADRs. | Research agents, codebase mapping, diagram skills. | Architecture validated by evidence, prototypes and adversarial review. |
| Development | Git, modular code, type checks, tests, code review. | TDD/debug/review skills, coding agents, parallel subagents. | Isolated task branches with deterministic integration gates. |
| Orchestration | Durable workflow state, queues, policy engine. | LLM planning and tool selection within limits. | Model proposes; control plane authorizes and records. |
| Memory | Versioned docs, relational records, source control. | Summarization, retrieval, graph and memory tools. | Canonical versioned facts plus rebuildable retrieval/graph indexes. |
| Security | OS isolation, identity, network controls, provenance. | Security review agents and attack-case generation. | Enforced runtime controls plus independent testing. |
| Model strategy | Benchmark methodology, license review, hardware planning. | Model discovery and evaluation agents. | Model/runtime selected from workload data, with adapter boundaries. |
| Release | Signed builds, SBOM, reproducible artifacts, approvals. | Release assistants and documentation skills. | Verified, approved offline bundles with rollback evidence. |
| Go-to-market | Customer interviews, pilots, contracts and measured ROI. | Research and writing skills. | Evidence-led selling with no unsupported security or productivity claims. |

## 3. Hybrid development loop

```text
CUSTOMER EVIDENCE
      ↓
REQUIREMENT + SUCCESS METRIC
      ↓
ARCHITECTURE / THREAT MODEL / ADR
      ↓
TASK BREAKDOWN + ACCEPTANCE TESTS
      ↓
DETERMINISTIC ORCHESTRATOR AUTHORIZES WORK
      ↓
AGENTS WORK IN ISOLATED BRANCHES / SANDBOXES
      ↓
UNIT + INTEGRATION + SECURITY + EVALUATION
      ↓
INDEPENDENT REVIEW + HUMAN APPROVAL
      ↓
MERGE / RELEASE BUNDLE / AUDIT EVIDENCE
      ↓
PILOT MEASUREMENT + INCIDENT/FAILURE LEARNING
      ↺
UPDATE REQUIREMENTS AND ARCHITECTURE
```

### Operating rules

1. No multi-file feature starts without a clear spec and test plan.
2. No agent is allowed to grant itself a new tool or permission.
3. Parallel work is permitted only when tasks are independent and workspace isolation exists.
4. Every output is labelled proposal, verified result or unresolved.
5. Tests are executed in a controlled environment; agent statements are not test evidence.
6. Security review is not optional for boundary-changing work.
7. Human approval is required for merge/release and any high-impact action.
8. A completed sprint ends with measurement and a retro, not just a code diff.

## 4. Product-development methodology

### Stage 0 — Problem and customer validation

Deliverables:
- Interview notes with consent and data-handling rules.
- Customer/problem evidence register.
- Workflow maps and current-process baselines.
- Buyer/champion/security-approver map.
- Initial willingness-to-pilot evidence.

Exit gate: At least one workflow is repeatedly reported as costly, constrained by isolation requirements, and owned by an identifiable buyer. The founder must understand the customer environment well enough to write a realistic acceptance test.

### Stage 1 — Product requirements and architecture

Deliverables:
- PRD and user stories.
- Non-functional requirements.
- Deployment/isolation profile.
- System context and trust-boundary diagrams.
- Threat model.
- ADRs for data, inference, state, agent permissions, sandbox and update architecture.
- Definition of Done.

Exit gate: Every MVP requirement has a test or a documented reason why it cannot yet be tested.

### Stage 2 — Technical feasibility spike

Build the smallest end-to-end path:

1. Prepare a local model and runtime on the selected hardware.
2. Block outbound network at the infrastructure layer.
3. Load one non-sensitive repository and documentation corpus.
4. Perform source-grounded analysis with references.
5. Propose a bounded test or patch.
6. Execute only in a disposable, no-egress sandbox.
7. Show results, limitations and a complete audit trail.

Exit gate: The complete workflow operates under the selected offline profile and meets the pre-defined minimum task-quality and performance criteria.

### Stage 3 — MVP platform hardening

Add only requirements revealed by the pilot:
- Identity and roles.
- Policy enforcement and approval workflow.
- Durable state and restart recovery.
- Sandboxed worker lifecycle.
- Artifact intake and integrity verification.
- Audit and diagnostic facilities.
- Backup, restore and rollback.
- Repeatable installation.

Exit gate: A second environment can be installed from pinned artifacts and run the same acceptance suite reproducibly.

### Stage 4 — Design-partner pilot

- Deploy in a customer-approved non-production environment.
- Run a baseline task set against the current process.
- Capture accepted results, corrections, time saved, defects and failures.
- Run security and operational tests.
- Have users judge the value, not only the builder.

Exit gate: The customer agrees the measurable result is useful enough to support continued use, procurement or a paid pilot.

### Stage 5 — Repeatability and productization

- Support a narrowly defined hardware/OS/model matrix.
- Standardize installation, update and recovery.
- Create admin and security documentation.
- Add monitoring and incident response.
- Reduce bespoke consulting work.
- Build partner/systems-integrator enablement.

Exit gate: A new customer deployment does not require a full redesign or founder-only rescue work.

## 5. Model strategy: use, adapt, train — in that order

### First: use existing open-weight models

Select two or three candidates after measuring them on the actual workflow. Check each exact checkpoint's license, commercial rights, acceptable-use terms, redistribution and derivative conditions. Model licenses change; a family name is not enough.

### Second: adapt the system around the model

Usually test these before fine-tuning:
- Better source indexing and retrieval.
- More reliable tool schemas.
- Smaller bounded tasks.
- Clearer state/context management.
- Better test feedback.
- Model routing by task complexity.
- Retrieval grounded in customer-approved knowledge.
- Domain-specific evaluation and guardrails.

### Third: fine-tune/adapt only if evidence supports it

A LoRA/adapter or fine-tune is justified only when:
- The task distribution is stable and recurring.
- There is lawful, high-quality training/evaluation data.
- A baseline demonstrates the failure mode.
- Fine-tuning improves held-out customer tasks and does not degrade security or general reliability.
- The customer accepts the model lifecycle, provenance and maintenance burden.

### Do not train a foundation model at the beginning

The opportunity is to deliver controlled frontier capability inside the customer's boundary. Training a foundation model would consume capital, compute, data and time before the workflow or buyer is proven. Model ownership can begin with customer-controlled artifacts, adapters, retrieval, evaluations and portability.

## 6. Research-to-build feedback loop

Research is not a one-time Phase I activity. Keep it operating throughout Phase II, but with stricter scopes.

- Phase I research discovers the opportunity and first product hypothesis.
- During architecture, focused research validates hard design choices.
- During implementation, implementation agents consult only the sources needed for the ticket.
- During testing, research agents identify attack methods and benchmark weaknesses.
- During pilot, customer evidence updates product priorities.
- After release, monitoring and public-source research track new vulnerabilities, model changes and ecosystem shifts.

Every research finding that changes architecture must become an ADR with its source and impact.

## 7. Evaluation system

### Product quality metrics

- Accepted task completion rate.
- Time from task acceptance to usable result.
- Human correction/review time.
- Regression rate.
- Test quality and coverage of relevant behaviour.
- Source-grounding accuracy.
- Requirements-to-code traceability completeness.
- Repeatability across runs.

### Platform metrics

- Install success on supported profiles.
- Offline startup success and time.
- Task recovery after process/host interruption.
- Mean time to diagnose failure.
- Model latency, throughput and memory footprint.
- Update/rollback success.
- Audit reconstruction completeness.

### Security metrics

- Unauthorized tool calls blocked.
- Prompt-injection attack success rate.
- Secret access attempts blocked.
- Unexpected egress attempts blocked and recorded.
- Sandbox boundary test results.
- Artifact signature/provenance verification rate.
- Unapproved state transitions prevented.

### Measurement discipline

- Keep a customer task set separate from public benchmark training/evaluation data where possible.
- Use fresh tasks and hidden evaluation where possible.
- Do not rely solely on SWE-bench Verified. OpenAI reported in February 2026 that it found contamination and test issues in that benchmark; later work also identified problems in coding benchmarks. Use multiple benchmarks plus a private, customer-grounded suite.
- Record exact model, scaffold, prompts, tools, hardware, settings and task versions.
- Do not compare results across different scaffolds or hardware as if they were identical.

## 8. First 90-day execution plan

This is a suggested sequence, not a guarantee of delivery or market traction.

### Days 1–15 — Evidence and customer access

- Complete the research protocol.
- Interview target users, buyers and security approvers.
- Choose one workflow and one pilot boundary.
- Audit competitors and 30 plugin candidates.
- Identify one test server/workstation profile.
- Create baseline tasks and acceptance metrics.

**Decision:** Continue only if there is a repeated customer problem and a feasible pilot path.

### Days 16–30 — Vertical feasibility

- Implement local inference adapter.
- Build read-only repository indexing and evidence retrieval.
- Add one bounded agent workflow.
- Use an isolated execution worker for tests/patch proposal.
- Verify operation with egress blocked.

**Decision:** Continue only if local models provide useful quality at acceptable resource cost.

### Days 31–60 — Controlled MVP

- Add workflow state, identity, permissions and audit.
- Add test harness, security test suite and artifact manifest.
- Build installer and restore path.
- Measure on the private task suite.

**Decision:** Continue only if the system is more useful than the best available substitute on a customer-valued metric.

### Days 61–90 — Pilot and commercial decision

- Run in a customer-approved test environment.
- Capture baseline versus product results.
- Obtain independent security review of the pilot scope.
- Produce customer-facing operations/security documentation.
- Seek a paid pilot, procurement path or signed design-partner commitment.

**Decision:** Scale, narrow, pivot or stop based on evidence.

## 9. Startup and team execution

The founder's core responsibilities:

- Own the problem, product trade-offs and technical direction.
- Conduct customer discovery and secure design partners.
- Review architecture and threat boundaries.
- Build or recruit the missing systems/security expertise.
- Set the evaluation and acceptance standard.
- Own commercial conversations and procurement learning.

Potential early capability gaps to cover, whether through hiring, advisers or partners:

1. Systems/platform engineering and Linux infrastructure.
2. Applied ML/inference optimization.
3. Product security and secure software supply chain.
4. Domain engineering in the first target vertical.
5. Enterprise sales/procurement and implementation.

Do not infer that one person or a large agent swarm can replace domain access, security review or enterprise trust. Agents accelerate work; customers and qualified specialists validate it.

## 10. Business and distribution plan

### Initial business shape

- Software platform license per secure deployment/site.
- Paid deployment/integration for the first pilots.
- Ongoing support and controlled update service.
- Optional appliance/validated hardware bundle after demand is proven.

### Commercial sequence

1. Founder-led technical interviews.
2. A specific design partner and non-production workflow.
3. A paid or clearly committed pilot.
4. Repeatable deployment and measured reference result.
5. Partner channels with secure infrastructure/system integrators.
6. Expand to additional workflows and verticals.

### What to sell

Sell a measurable engineering outcome under an explicit data boundary—not “30 agents,” “unlimited intelligence,” “zero leakage,” or “fully autonomous enterprise software.”

## 11. YC and fundraising note

YC's Winter 2027 RFS explicitly calls for AI for the Air-Gapped Economy and describes the opportunity areas. The RFS is an opportunity signal, not proof of market demand or a guarantee of selection.

As of the 30 October 2026 date baseline, YC's official apply page lists the on-time Winter 2027 deadline as **2 November 2026 at 8pm Pacific Time**. If applying, use the official form, verify the live deadline and describe the true state of the project: idea, prototype, user interviews, pilot or revenue. Do not claim a product exists if it does not.

[YC Apply](https://www.ycombinator.com/apply) · [YC Requests for Startups](https://www.ycombinator.com/rfs)

## 12. Final operating doctrine

- Architecture before implementation; experiments before architecture freeze.
- Research independently; use plugins as replaceable accelerators.
- Traditional systems engineering owns control and safety.
- Agents may reason and propose; deterministic code authorizes and records.
- Multi-agent parallelism requires isolation, task ownership and integration gates.
- Offline means no hidden runtime network dependency, not merely a local model endpoint.
- Model weights, data, code and plugins are supply-chain artifacts that must be reviewed.
- AST checks, prompts and “air gap” labels are never complete security guarantees.
- Start with a narrow workflow, a real buyer and measurable value.
- Expand only after repeatable customer evidence.

**The product must win on validated customer outcomes, security and operational reliability—not on the number of agents, plugins, frameworks or diagrams.**

