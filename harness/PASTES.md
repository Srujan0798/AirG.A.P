# Harness Paste Board — Wave 1

One ACTIVE block per window. Copy the whole block (including the "You are W#" line) into one idle OpenCode window. See `harness/BOSS_GUIDE.md` for the convention.

---

## DONE — W1

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

## DONE — W2

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

## DONE — W3

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

## DONE — W4

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

---

# Wave 2 — attack the red-team's risks (dispatched 2026-11-11)

Each window targets one risk from harness/w4/REPORT.md. Shared rules live in harness/COMMON.md.

## ACTIVE — W5 (risk: pain not validated)

```text
Read /Users/srujansai/Desktop/AirG.A.P/harness/COMMON.md first and obey it. You are W5. This text is the only task.

GOAL: Give the founder (an IIT Gandhinagar student) everything needed to start 15–25 customer interviews this week. This attacks the biggest risk: the pain is not yet validated.

READ FIRST: 09_INITIAL_WEDGE_DISCOVERY.md (sections 1, 2, 7), harness/w2/REPORT.md, harness/synthesis/WAVE1_SYNTHESIS.md.

DO:
1. harness/w5/TARGET_LIST.md — 40–60 real organisations, India first, then global, whose engineering runs on isolated or air-gapped networks: DRDO labs, defence PSUs, ISRO centres, private defence & aerospace firms, iDEX-backed startups, industrial/embedded R&D centres in India, critical-infrastructure operators. Per row: segment, why its engineering is isolated (source URL + grade), likely first workflow, the role to approach, and a warm path (IITGN alumni, faculty, IDE mentors, Gujarat defence network) or "cold".
2. harness/w5/OUTREACH_KIT.md — a 15-minute interview guide adapted from 09 section 1 (current process first, no pitching), three outreach messages (email, LinkedIn, warm-intro request), and an interview log template with the fields from 09 section 1.
3. harness/w5/REPORT.md — top 10 targets ranked by access × urgency, the 3 warmest paths, open questions.

TASK-ID: WAVE2-DISCOVERY
```

## ACTIVE — W6 (risk: local models not good enough)

```text
Read /Users/srujansai/Desktop/AirG.A.P/harness/COMMON.md first and obey it. You are W6. This text is the only task.

GOAL: Prove or disprove, with measured numbers, that a local open-weight model on this Mac can do our Day-1 workflow (test generation) with no network. This attacks the risk that local models are not good enough.

SAFETY: Before any download run `df -h /`. If less than 12 GB is free, write harness/w6/REPORT.md saying so and print "W6 blocked: disk". Download at most one model file of 5 GB or less. Generation and test runs must use only local files.

READ FIRST: 04_TRADITIONAL_SYSTEMS_ENGINEERING_BLUEPRINT.md sections 5 and 12, harness/w3/REPORT.md.

DO:
1. Pick the strongest open-weight coding model whose quantised file is 5 GB or less and whose licence allows commercial use. Record exact name, revision or hash, quantisation and licence URL. Run it with llama.cpp or Ollama.
2. Clone a small, permissively licensed Python repo with an existing test suite into harness/w6/sandbox/. Choose 10 functions with weak or no tests.
3. For each function: ask the local model for unit tests, run them with pytest in a fresh venv, and record pass/fail, coverage before and after (coverage.py), tokens per second, peak memory and wall time. Save raw output to harness/w6/logs/.
4. harness/w6/FEASIBILITY.md — table of all 10 runs plus every command used.
5. harness/w6/REPORT.md — verdict (useful / marginal / not useful), the numbers, failure modes, and what hardware a lab would need.

TASK-ID: WAVE2-FEASIBILITY
```

## ACTIVE — W7 (risks: incumbents already do this; thin moat)

```text
Read /Users/srujansai/Desktop/AirG.A.P/harness/COMMON.md first and obey it. You are W7. This text is the only task.

GOAL: Stress-test our pitch claim "a vendor-neutral layer that governs AI coding inside the wall is still unclaimed" before a mentor does. This attacks the risks that incumbents already do this and that our moat is thin.

READ FIRST: harness/w1/REPORT.md, harness/w1/COMPETITOR_MATRIX.md, harness/w4/REPORT.md.

DO:
1. Check the enterprise self-hosted coding assistants W1 missed, from official docs where possible: Tabnine (air-gapped tier), Sourcegraph Cody Enterprise, Windsurf/Codeium self-hosted, Refact.ai, GitLab Duo Self-Hosted, JetBrains AI Enterprise, and any others you find. For each: fully air-gapped (yes/no + source), SSO/RBAC, audit logs, admin policy, agent capabilities, which models it can run, offline update path, pricing signal.
2. Re-check Legion Centurion, NVIDIA NIM / AI Enterprise and Red Hat OpenShift AI for any public move toward governed coding agents.
3. Inspect the source and docs of Cline, Continue, LocalPilot and Sovereign Agent for identity, audit and update features (W1 open question 1).
4. harness/w7/MOAT.md — which parts of our control plane are unclaimed, partly claimed (by whom), or taken, and the 3 most defensible features to build first.
5. harness/w7/REPORT.md — verdict on the claim (holds / holds with caveat / fails) and the exact wording a pitch should use.

TASK-ID: WAVE2-MOAT
```

## ACTIVE — W8 (risk: costs outrun revenue)

```text
Read /Users/srujansai/Desktop/AirG.A.P/harness/COMMON.md first and obey it. You are W8. This text is the only task.

GOAL: Find the fastest credible path from an IIT Gandhinagar student startup to a first paid pilot in India, and check whether the unit economics work. This attacks the risk that deployment and support costs outrun revenue.

READ FIRST: 01_MASTER_VISION_AND_STRATEGY.md section 8, 06_CUSTOM_HYBRID_ENGINEERING_METHODOLOGY.md section 10, harness/w4/REPORT.md.

DO:
1. harness/w8/PATHS.md — funding and procurement routes for a defence/aerospace software startup in India: iDEX challenges and grants, DRDO Technology Development Fund, defence PSU startup programmes, GeM procurement, Startup India and Gujarat state schemes, incubator grants. Per route: eligibility, ticket size, timeline, official source URL, fit for us. Note any security-clearance or export-control limits a student team would hit.
2. harness/w8/ECONOMICS.md — cost of one single-node offline deployment in India (GPU workstation or server options with INR price sources), install and support effort, and three pricing models (per-site licence, paid pilot, appliance bundle) with break-even at 1, 5 and 20 customers. State every assumption.
3. harness/w8/REPORT.md — the recommended first-revenue path with dates, and the 3 numbers the next pitch should use.

TASK-ID: WAVE2-GTM
```
