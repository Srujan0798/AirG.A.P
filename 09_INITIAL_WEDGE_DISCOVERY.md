# 09 — Initial Wedge Discovery: Customer Segment & Workflow Selection

**Project:** AI for the Air-Gapped Economy  
**Prepared by:** Enterprise Product Discovery Lead  
**Status:** Hypothesis baseline — zero customer interviews completed  
**Date:** 30 October 2026  
**Owner:** Product discovery  
**Related:** `01_MASTER_VISION_AND_STRATEGY.md` (product hypothesis), `README.md` (evidence & limitations)

---

## 0. Decision frame

**Question:** Which customer segment and which workflow inside that segment should be the first wedge (initial ICP + beachhead workflow)?

**Product under test (hypothesis, not validated):** A customer-controlled, offline agentic engineering workbench that lets teams understand, test, modernize and propose changes to software repositories without sending code, requirements, logs or proprietary data outside the customer's approved boundary.

**First workflow candidates (from 01):**
1. Codebase understanding (module/dependency/data-flow mapping, source-grounded Q&A)
2. Requirements traceability (requirements ↔ code ↔ tests ↔ change history)
3. Change-impact analysis (files/interfaces/tests/dependent components affected by a change)
4. Test generation (bounded issue/function → proposed tests → sandbox execution → coverage gaps)
5. Legacy modernization (migration plan + small reviewable patches, no silent subsystem replacement)
6. Defect investigation (logs + repo context → candidate root causes → reproducible test/patch proposal)

**Decision rule:** Select the segment+workflow with the highest composite score on urgency × budget ownership × access × pilot feasibility ÷ (sales cycle × repeatability risk), subject to Gate A–E in 01 (§9). All segment scores below are **unvalidated hypotheses** pending interviews. No market-size number is given anywhere in this document; none will be produced without a cited methodology.

---

## 1. Interview guide (current process first — no solution pitch)

**Rule:** The first ~20 minutes of every interview covers current process, roles, pain and constraints. Product/solution discussion only after the interviewee has described the status quo in their own words. Every question lists the evidence it gathers and the role to ask.

### A. Context & current process (ask everyone; target: engineering lead / senior engineer)

| # | Question | Evidence gathered | Ask |
|---|----------|-------------------|-----|
| A1 | Walk me through the last time your team had to understand a large or unfamiliar part of the codebase. What did you actually do, step by step? | Current workflow, manual effort, tooling, frequency trigger | User |
| A2 | How often does this kind of work come up (per week/month/quarter)? What triggers it? | Task frequency | User |
| A3 | What happens today when you need to trace a requirement to code, or a code change to tests? | Current traceability process, substitutes | User |
| A4 | When a proposed change breaks something downstream, how do you find out? How long does root-cause take? | Consequence, manual effort, defect cost | User |
| A5 | Show me the most recent patch or test you wrote for a legacy/embedded module. How was it reviewed and approved? | Approval flow, human-in-the-loop, current QC | User |
| A6 | What AI or coding-assistant tools has your team tried, rejected or banned, and why? | Existing substitutes, rejection reasons, policy constraints | User / security approver |

### B. Roles, authority & buying center (target: engineering director, security lead, procurement)

| # | Question | Evidence gathered | Ask |
|---|----------|-------------------|-----|
| B1 | Who does the day-to-day work on this task? Who is formally accountable for its outcome? | User vs. accountable owner | Engineering lead |
| B2 | If we could cut the time on this task by half, whose budget would pay for it? Is that budget already allocated or would it need a new request? | Budget ownership, budget cycle | Economic buyer |
| B3 | Who must sign off before new software runs in your engineering environment? What does that review require (documentation, SBOM, pen test, accreditation)? | Security approver, accreditation burden | Security approver |
| B4 | How do you buy specialized engineering software today? Approved vendor list? PO process? GSA/SEWP-like vehicle? Typical lead time from evaluation to signed PO? | Procurement path, sales cycle | Economic buyer / procurement |
| B5 | Who could run a 4–6 week pilot with a real (non-production) repo on isolated hardware, and what would make them say yes/no? | Pilot feasibility, access, success criteria | Champion / user |

### C. Data boundaries, hardware & deployment restrictions (target: security approver / infra lead)

| # | Question | Evidence gathered | Ask |
|---|----------|-------------------|-----|
| C1 | Exactly what is isolated: the whole lab, only source control, build networks, runtime networks, or classified/sensitive data? | Data boundary, isolation model | Security approver |
| C2 | How do code, packages, model weights and updates move into the environment today? Removable media? Diode? Allowlisted gateway? | Transfer path, hardware/deployment restriction | Security / infra |
| C3 | What hardware is already available in the isolated environment (servers, GPUs, air-gapped workstations)? Age, specs, who owns it? | Hardware availability, pilot feasibility | Infra lead |
| C4 | What must any new tool integrate with (source control, identity, ticketing, CI, build, artifact store), and must that integration work offline? | Integration requirements | User / infra |
| C5 | What would constitute a failed pilot? What would a successful pilot look like in measurable terms? | Pilot exit criteria, value definition | Champion / economic buyer |

### D. Contradiction probes (ask near end; target: champion + security approver)

| # | Question | Purpose |
|---|----------|---------|
| D1 | You said X is expensive and manual — but you also said you already have [tool/process] that handles it. Help me reconcile those two statements. | Surface substitute adequacy / stated vs. revealed preference |
| D2 | You said you can't send code outside — but developers already paste snippets into public AI tools. Where is the line actually drawn? | Surface policy vs. behavior gap |
| D3 | Who would block this project if it succeeded, and why? | Surface hidden blockers / anti-champions |
| D4 | If we never built this, what would you do instead next year? | Surface true cost of inaction / urgency |

**Interview log fields (capture per interview):** date, roles, segment, workflow discussed, frequency, consequence, manual effort (hrs/week), substitutes, data boundary, hardware, buyer, security approver, procurement path, quotes, contradictions, next step, evidence quality (direct observation / self-report / second-hand).

---

## 2. Role-identification matrix (per segment)

| Segment | Typical user | Typical champion | Economic buyer | Security approver | Procurement path |
|---------|-------------|------------------|----------------|-------------------|------------------|
| Defense & aerospace suppliers | Lead/senior software engineer ( avionics, mission systems, ground software) | Engineering director / CTO of engineering | Program manager / division VP (IRAD or contract-funded) | ISSO / security engineer / accreditation authority (DCMA/CMMC-adjacent) | Prime contract flow-down, GSA/SEWP, SBIR/STTR phase II, direct PO |
| Industrial/embedded software vendors | Firmware/embedded engineer, platform team lead | VP engineering / head of product engineering | VP engineering / CTO (P&L-owned) | Product security / cert lead (IEC 61508, ISO 26262, UL) | Enterprise software PO, OEM bundling, partner/reseller |
| Critical-infrastructure engineering teams | Control-systems / OT software engineer | OT engineering manager / chief engineer | Plant/asset owner (CapEx budget) | OT security / NERC-CIP or NIST 800-82 owner | Utility/asset procurement, long-cycle capital, integrator-led |
| Financial institutions | Platform / developer-experience engineer | Head of platform engineering | CIO / CTO (budget holder) | CISO / infosec / model-risk | Vendor management, security review, enterprise agreement |
| Healthcare & research institutions | Research software engineer / bioinformatics lead | Department chair / core-facility director | Dean / hospital CIO / grant PI | IRB / infosec / HIPAA privacy officer | Grant-funded purchase, GSA, research IT procurement |
| Public-sector technology teams | Civilian software engineer / moderniza­tion team lead | CIO / digital-service director | CIO / agency procurement officer | ATO authorizing official / ISO | FedRAMP-adjacent, GSA schedules, blanket purchase agreements |

*Note: Role titles are hypotheses. Interviews must confirm the actual names and whether one person wears multiple hats (common in smaller suppliers).*

---

## 3. Evidence capture template (per segment / workflow)

Collect during or right after each interview. Rate each cell 1–5 with source noted.

| Evidence domain | What to capture | Scale |
|---|---|---|
| Task frequency | How often the workflow occurs per engineer/team; trigger events | 1 = rare (<monthly) … 5 = daily/continuous |
| Consequence | Cost of doing it poorly or not at all (delays, escapes, rework, safety/compliance risk) | 1 = low annoyance … 5 = mission/safety/compliance failure |
| Current manual effort | Engineer-hours per week spent on the workflow today; workaround burden | 1 = <1 hr … 5 = >10 hrs/engineer/week |
| Existing substitutes | Tools/processes already used; how well they work; why rejected/kept | 1 = fully adequate … 5 = no viable substitute |
| Data boundaries | What may not leave the environment; classification; transfer policy | 1 = open … 5 = fully air-gapped/classified |
| Hardware & deployment restrictions | Available isolated hardware, install constraints, offline-only requirement, update path | 1 = cloud-friendly … 5 = fully air-gapped, no egress |

---

## 4. Scoring rubric

Score each segment 1–5 on six dimensions. Composite = (Urgency + Budget + Access + PilotFeasibility − SalesCyclePenalty − RepeatabilityRisk) normalized; Urgency and Budget double-weighted because they drive Gate A and Gate E. Treat all scores as **unvalidated hypotheses** until confirmed by ≥3 independent interviews per segment.

| Dimension | 1 (low) | 5 (high) |
|---|---|---|
| Urgency | Task is infrequent, low consequence, well-handled today | Expensive, frequent, painful, no adequate substitute |
| Budget ownership | Budget fragmented; no named owner; new-money request required | Named budget holder with allocatable funds |
| Access | Hard to reach decision-makers; long procurement; NDA/clearance gates | Direct access to champion and buyer; short path |
| Pilot feasibility | Requires live production, classified systems, or custom hardware | Can pilot on non-production repo in isolated lab in 2–4 weeks |
| Sales cycle | 12+ months, multi-party, security accreditation required up front | <3 months, technical evaluation, PO or design-partner letter |
| Product repeatability | Workflow and environment differ wildly per customer | Same workflow, similar stack, repeatable across many customers |

Sales cycle and repeatability are **risk factors** (higher score = worse), so they subtract from the composite.

---

## 5. Ranked segments (unvalidated hypotheses)

| Rank | Segment | Lead workflow candidate | Composite (hypothetical) | Evidence quality | Key open risks |
|------|---------|------------------------|--------------------------|------------------|----------------|
| 1 | Defense & aerospace suppliers | Change-impact analysis / codebase understanding on legacy mission/ground software | High | **Unvalidated — no interviews** | Clearance/access, long procurement, multiple primes, ITAR/export-control boundaries |
| 2 | Industrial/embedded software vendors | Legacy modernization + test generation for embedded/firmware codebases | Medium-high | **Unvalidated — no interviews** | Safety certification scope, hardware diversity, long product lifecycles |
| 3 | Critical-infrastructure engineering teams | Defect investigation / impact analysis on OT/control software | Medium | **Unvalidated — no interviews** | NERC-CIP/800-82 scope, live-system caution, slow sales, few buyers |
| 4 | Financial institutions | Codebase understanding + requirements traceability in platform engineering | Medium | **Unvalidated — no interviews** | "Air gap" may be loose (private cloud, not disconnected); generic chat competition |
| 5 | Public-sector technology teams | Codebase understanding / modernization in digital-service teams | Medium-low | **Unvalidated — no interviews** | Long procurement, ATO burden, budget year cycles, lower repeatability |
| 6 | Healthcare & research institutions | Research code comprehension + test generation | Medium-low | **Unvalidated — no interviews** | Grant-funded (unstable budget), IRB/privacy scope, low willingness-to-pay for tooling |
| 7 | Other (discovered independently) | TBD | TBD | None | Not yet discovered |

**Evidence quality legend:** *Unvalidated — no interviews* = founder-visible reasoning only, drawn from `01_MASTER_VISION_AND_STRATEGY.md` and public references. Nothing here is customer-confirmed.

---

## 6. Contradictions & open risks (between founder intent and segment reality)

| # | Contradiction / risk | Why it matters | Resolution path |
|---|---------------------|----------------|-----------------|
| C1 | Founder intent assumes buyers reject cloud AI for data-boundary reasons; financial institutions often use private cloud (not air-gapped) and may not see a gap. | Segment #4 may have weak urgency for "offline" specifically. | Confirm actual isolation mode in interviews (question C1) before scoring. |
| C2 | Defense/aerospace offers urgency and budget but longest sales/clearance cycles; may consume all discovery time with one pilot. | High reward, high access risk; could stall Gate E. | Pair one defense interview set with one industrial interview set in parallel. |
| C3 | "No internet" ≠ no risk; security approvers may still require SBOM, provenance, signed updates, TUF-style artifact verification — adding scope beyond the MVP wedge. | Could expand MVP beyond the bounded workbench. | Scope MVP to evidence production for the pilot boundary only (01 §5). |
| C4 | Founder's self-described 30-skill plugin collection is developer-facing, not customer-facing; treating plugins as product risks repeating "plugin dependence" failure mode the founder rejects. | Product could become brittle/insecure. | Re-engineer only capabilities with a real customer gap (01 §2.5); plugins are accelerators, not runtime deps. |
| C5 | Legacy modernization (workflow 5) is tempting but risks silent subsystem replacement and safety-critical scope — an explicit non-goal. | Could violate MVP boundary and Gate C. | Start with read-only analysis (workflows 1–3); patch proposals require human approval (01 §5). |

---

## 7. Recommended initial customer profile (ICP)

**One ICP — pending interview validation:**

> **A defense or aerospace supplier's isolated engineering lab** (typically a subcontractor or tier-2 supplier to a prime, working on mission, ground or avionics software) where:
> - A **lead/senior software engineer** spends a measurable fraction of each week manually mapping dependencies, tracing requirements to code, and assessing change impact on legacy codebases they cannot upload to public AI services.
> - An **engineering director** is the champion, allocates IRAD or contract-funded budget, and can authorize a 4–6 week pilot on a non-production repository in an isolated lab.
> - The **economic buyer** is a program manager or division VP with allocatable funds and a defined procurement vehicle (SEWP/GSA/prime flow-down or direct PO).
> - The **security approver** (ISSO/security engineer) requires offline operation, artifact provenance/SDLC evidence, human approval for repository writes, and no hidden egress — all within the MVP boundary.
> - **Hardware:** an existing isolated server/workstation in the lab capable of local model serving.
> - **Workflow:** change-impact analysis and codebase understanding (read-only by default, sandboxed patch proposals, human approval before export).

**Why this segment first:** It combines the highest hypothesized urgency (legacy, safety-adjacent code where mistakes are costly), a named budget owner, a natural offline boundary (classification/ITAR), a repeatable workflow across similar suppliers, and a pilot that can run on non-production hardware — directly matching Gate A–E in `01 §9`. Industrial/embedded vendors are the fast-follow if defense access proves slower than expected.

---

## 8. Next steps (first 2 weeks, per `01 §10`)

1. Recruit and interview 15–25 engineers, security leads, engineering directors and integrators across the top 3 segments (target ≥3 per segment).
2. Log every interview with the template in §3; flag contradictions using §6 probes.
3. Confirm or revise the role matrix and segment scores; re-rank only after evidence.
4. Map 3–5 concrete workflows; select one to build the vertical slice around.
5. Build competitor/open-source feature matrices; identify one pilot repository and one target hardware profile.
6. Establish the baseline task set and security requirements.
7. **Do not** freeze architecture, claim compliance, or produce a market-size number without a cited methodology.

---

## 9. Methodology caveat

- No market-size, TAM/SAM/SOM, or willingness-to-pay figure appears in this document, and none will be produced unless a citation for the sizing method (e.g., top-down from a named public source, bottom-up from named customer contracts, or jobs-to-be-done effort estimation) is included alongside the number.
- All segment rankings, role assignments, and scores are unvalidated hypotheses until confirmed by direct customer interviews.
- The recommended ICP is a starting point for discovery, not a commitment.
