# W3 — Workflow Wedge Detail

Full per-workflow scoring rationale supporting REPORT.md.

## Scoring conventions

1–5 scale per dimension. Higher = more of that attribute. Review burden, safety criticality, integration complexity, and procurement barrier are cost/risk factors (higher = harder/more expensive). Scores are hypotheses pending customer interviews (Gate A).

## 1. Repository Understanding

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 4 | Engineers spend significant time manually mapping modules, dependencies, entry points, data flows. |
| Task frequency | 4 | Recurs with every new codebase, onboarding, and refactor. |
| Measurable value | 4 | Time-to-comprehension, query accuracy, source-reference precision. |
| Data availability | 5 | Source code itself is the dataset; abundant and self-describing. |
| Human review burden | 2 | Read-only Q&A; answers cite sources and are cheap to verify. |
| Safety criticality | 2 | Read-only analysis; no writes to production or OT. |
| Integration complexity | 3 | Needs repo indexing + docs corpus; modest integration. |
| Local model feasibility | 5 | Code Q&A is a well-solved local LLM task. |
| Procurement barrier | 3 | Read-only analysis lowers security approver concern. |
| Expansion potential | 5 | Shared context layer beneath every other workflow. |

Verdict: Best safety profile and best local feasibility. Foundation layer, not a monetizable wedge by itself.

## 2. Requirements Traceability

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 4 | High in regulated domains (defense, medtech); manual traceability matrices are error-prone. |
| Task frequency | 3 | Driven by audits, change requests, compliance reviews — periodic, not continuous. |
| Measurable value | 4 | Missing-link count, traceability matrix completeness, audit-pass rate. |
| Data availability | 3 | Requirements, code, tests, and change history often live in separate systems. |
| Human review burden | 4 | Links require expert validation; false positives/negatives are costly. |
| Safety criticality | 3 | Missing traceability can mask safety-relevant gaps. |
| Integration complexity | 4 | Needs links across requirements mgmt, source control, test systems, change history. |
| Local model feasibility | 4 | Semantic matching across artifacts is feasible locally but data-sparse. |
| Procurement barrier | 4 | Regulated buyers demand accreditation evidence; longer sales cycle. |
| Expansion potential | 4 | Strong differentiator for defense/aerospace buyers once baseline is proven. |

Verdict: High pain in regulated domains but scattered data and high review burden make it a slower, third workflow.

## 3. Code Modernization

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 5 | Legacy systems are expensive to maintain; modernization is a top pain point. |
| Task frequency | 2 | Major migrations are infrequent, project-bounded events. |
| Measurable value | 4 | Migration speed, defect escape rate, subsystem replacement correctness. |
| Data availability | 2 | Legacy-language code + documentation pairs are scarce; few public benchmarks. |
| Human review burden | 5 | Entire subsystems at stake; every patch needs expert review. |
| Safety criticality | 4 | Modernizing safety-critical code can introduce failures. |
| Integration complexity | 5 | Touches build systems, dependencies, deployment pipelines, runtime contracts. |
| Local model feasibility | 3 | Legacy-language support in local models is weaker. |
| Procurement barrier | 3 | Moderate; depends on vertical and certification scope. |
| Expansion potential | 3 | High value but narrow applicability per customer stack. |

Verdict: Highest pain but too infrequent, data-sparse, review-heavy, and integration-complex for MVP. Defer; small reviewable patches only as a follow-on.

## 4. Test Generation (RECOMMENDED MVP)

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 4 | Writing and maintaining tests is a recurring engineering burden. |
| Task frequency | 4 | Every feature, bug fix, and refactor generates test work. |
| Measurable value | 5 | Coverage delta, pass/fail count, regression escapes, engineer time saved — all objective. |
| Data availability | 5 | Code + test + framework pairs are abundant; SWE-bench-style held-out tasks exist. |
| Human review burden | 3 | Proposed tests and patches are diffable; reviewers can accept/reject/edit. |
| Safety criticality | 3 | Tests run in sandbox; wrong tests cause delays, not production harm. |
| Integration complexity | 3 | Needs repo index, test runner sandbox, approval gate; modest. |
| Local model feasibility | 4 | Test generation is a well-solved local LLM task; fine-tuning data is plentiful. |
| Procurement barrier | 3 | Read-only analysis by default; sandboxed execution lowers approver concern. |
| Expansion potential | 4 | Feeds directly into defect investigation and regression triage. |

Verdict: Highest composite score. Reviewable output, non-production evaluable, no live OT control, objective metrics, strong local feasibility.

## 5. Defect Investigation

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 5 | Root-cause analysis is time-consuming and expensive when it escapes. |
| Task frequency | 3 | Incident-driven; unpredictable volume. |
| Measurable value | 4 | Mean-time-to-root-cause, escape rate, repeat-defect rate. |
| Data availability | 3 | Logs + repo context are unstructured and scattered. |
| Human review burden | 4 | Candidate root causes and patch proposals need expert validation. |
| Safety criticality | 4 | Wrong root cause on safety-critical systems is harmful. |
| Integration complexity | 4 | Needs log ingestion, repo context, sandboxed reproduction. |
| Local model feasibility | 3 | Log analysis + code correlation is feasible but data-sparse per domain. |
| Procurement barrier | 3 | Moderate; log data may be classified or sensitive. |
| Expansion potential | 4 | Natural follow-on to Test Generation; shares sandbox + approval infrastructure. |

Verdict: Strong second workflow. Shares sandbox/approval infra with Test Generation; incident-driven frequency is the main limiter.

## 6. Document Intelligence

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 3 | Finding and summarizing docs is annoying but rarely blocking. |
| Task frequency | 3 | Recurring but low urgency. |
| Measurable value | 3 | Time-to-answer, summary accuracy; softer metrics. |
| Data availability | 4 | Docs and specs are usually available locally. |
| Human review burden | 2 | Summaries are cheap to spot-check. |
| Safety criticality | 2 | Read-only; low direct safety impact. |
| Integration complexity | 3 | Doc corpus indexing; modest. |
| Local model feasibility | 5 | Document Q&A is a well-solved local task. |
| Procurement barrier | 2 | Lowest barrier; read-only, non-code. |
| Expansion potential | 3 | Knowledge-layer feature; supports other workflows but not a wedge. |

Verdict: Easy to ship locally but low measurable value. Knowledge-layer feature, not wedge.

## 7. Engineering Change Management

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 4 | Change approval, impact assessment, and release governance are burdensome. |
| Task frequency | 3 | Every release and change request triggers the workflow. |
| Measurable value | 4 | Change lead time, approval cycle time, rollback rate. |
| Data availability | 3 | Change records, tickets, code, and tests span multiple systems. |
| Human review burden | 5 | Change approval is inherently human-gated; high burden. |
| Safety criticality | 4 | Wrong change approvals can reach production/OT. |
| Integration complexity | 5 | Spans ticketing, source control, CI, build, artifact stores, deployment. |
| Local model feasibility | 3 | Process reasoning is feasible but heavily customer-specific. |
| Procurement barrier | 4 | Touches governance and accreditation; high approver scrutiny. |
| Expansion potential | 4 | High enterprise value once baseline workflow is proven. |

Verdict: Process-heavy with too many stakeholders for a first wedge. Follow-on after baseline proven.

## 8. Model Lifecycle

| Dimension | Score | Rationale |
|---|---|---|
| Pain intensity | 3 | Model selection, versioning, and updates matter but are infrequent. |
| Task frequency | 2 | Model updates are episodic, not daily work. |
| Measurable value | 3 | Update success rate, rollback time, model performance on customer tasks. |
| Data availability | 2 | Model weights, configs, and eval results are vendor-specific and sparse. |
| Human review burden | 4 | Model updates need validation and sign-off. |
| Safety criticality | 3 | Bad model updates degrade agent behavior. |
| Integration complexity | 4 | Needs model registry, serving adapter, verification, rollback. |
| Local model feasibility | 3 | Local serving is feasible but hardware-dependent. |
| Procurement barrier | 4 | Model weights and export control add procurement complexity. |
| Expansion potential | 5 | Core platform layer; key to the wider air-gapped AI vision. |

Verdict: Platform layer with high expansion potential but immature data and infrequent tasks. Not a customer wedge; build after baseline.

## Recommended sequencing

1. **MVP:** Test Generation + read-only Repository Understanding context layer. Sandboxed test execution, human approval gate, audit log. Evaluable on non-production data with objective metrics.
2. **Follow-on 1:** Defect Investigation — shares sandbox/approval infra; incident-driven.
3. **Follow-on 2:** Requirements Traceability — for regulated buyers (defense/aerospace) once baseline is proven.
4. **Platform layer:** Model Lifecycle + Engineering Change Management — after workflow value is validated.

## Reference

See REPORT.md for the condensed scoring table, MVP definition, non-goals, success metrics, and open questions.
