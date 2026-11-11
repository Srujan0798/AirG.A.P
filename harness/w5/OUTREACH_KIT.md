# W5 — Outreach Kit: 15-Minute Discovery Interview

**Window:** W5 · **Task:** WAVE2-DISCOVERY · **Produced:** 2026-11-11
**Source discipline:** adapted from `09_INITIAL_WEDGE_DISCOVERY.md` §1 (guide), §2 (role matrix), §3 (evidence capture), §6 (contradiction probes). No facts asserted here require sourcing — it is a script, not a claim.
**Hard rule inherited from `09` §1:** *the first ~20 minutes covers current process, roles, pain and constraints. Product/solution discussion only after the interviewee has described the status quo in their own words.*

---

## 1. Before you send anything — 5 rules that decide whether this week works

1. **Do not mention a product, a demo, an "AI tool", or a pilot in the first message.** You are asking for 15 minutes of their time to describe their process. If they hear "AI tool", the security approver in the room switches off and the engineer gives you a rehearsed answer.
2. **Never promise air-gap compliance, certification, or accreditation.** `01` §11 and `09` §9 forbid it, and you cannot honour it before Gate C. If asked: *"That's exactly what I'd want to understand — what your process requires."*
3. **Do not claim you have customers, a product, or a company.** You are a student doing discovery. Say so plainly. Credibility here comes from precision about your ignorance, not from a pitch.
4. **Log everything the same day**, using §5. A week of 20 interviews with no log is zero evidence.
5. **One interview = one workflow.** Don't ask about all six. Pick the one the row in `TARGET_LIST.md` names and go deep.

---

## 2. The 15-minute interview guide

**Target length:** 15 minutes of *their* speaking time. Realistically 20–30 min calendar slot.
**Structure:** 0:00–0:30 framing → 0:30–9:00 current process (A + D probes) → 9:00–12:00 constraints (C) → 12:00–14:00 roles & buying (B, if the person is senior) → 14:00–15:00 close.
**Rule:** if they start describing a problem in the first 30 seconds, let them talk and let the clock run over. Do not steer back.

### 2.0 Framing (say this, near-verbatim)

> "Hi — I'm [name], I'm a final-year student at IIT Gandhinagar. I'm doing research on how software engineering actually works inside isolated and restricted networks — defence labs, space centres, power and nuclear plants — and I've found almost no good public writing about it.
>
> I'm not selling anything and I'm not pitching a tool. I have 15 minutes and I want to understand two or three things: how work actually flows today, and where it breaks. I'd like to record it only with your permission, and you can tell me to stop at any point.
>
> Can I ask you about the last time something broke?"

**If they ask "what are you building?":** *"Nothing yet. That's the point of the interviews — I'm trying to find out whether there's a problem worth building for, and if there is, whether it's worth building for *you* or for someone else entirely."*

### 2.1 Segment A — Current process (ask everyone; the core of the interview)

| # | Question | What you are gathering | Notes |
|---|---|---|---|
| A1 | "Walk me through the last time you or your team had to understand a large or unfamiliar part of a codebase — or a legacy system. What did you actually do, step by step?" | Real workflow, tools, manual effort, trigger | Let them narrate. Take notes on *tools named*, not just answers. |
| A2 | "How often does that kind of work come up — per week, per month, per quarter? What triggers it?" | Task frequency | Push for a number. "Roughly?" is fine. |
| A3 | "When you need to trace a requirement through to code, or a code change through to tests — what does that look like today?" | Traceability process and substitutes | Skip if not their domain. |
| A4 | "When a proposed change breaks something downstream, how do you find out? How long does it take to find the root cause?" | Consequence, detection latency, defect cost | **Most valuable question.** Push on the last one. |
| A5 | "Show me or describe the most recent patch or test you wrote for a legacy or embedded module. How was it reviewed and approved?" | Approval flow, human-in-the-loop, current QC | Note the number of reviewers and the gate artefacts (test evidence, review doc). |
| A6 | "Has anyone on the team tried an AI or coding-assistant tool? Adopted it, rejected it, or been told not to use it — and why?" | Existing substitutes **and rejection reasons** | **Critical.** Do not skip. If the answer is "we banned it", you have found the policy in one sentence. |

### 2.2 Segment C — Isolation, hardware, transfer (ask the security approver or infra lead; ~3 min)

| # | Question | What you are gathering |
|---|---|---|
| C1 | "Exactly what is isolated in your environment — the whole lab, only source control, the build network, runtime networks, or specific classified/sensitive data?" | **The single most important answer in the whole interview.** It decides whether the founder's "air-gapped" premise holds. |
| C2 | "How do code, packages, model weights and updates actually get into the environment today? Removable media? A diode? An allow-listed gateway? Manual review?" | Transfer path, real operational friction |
| C3 | "What hardware is already sitting in the isolated environment — servers, GPUs, air-gapped workstations? Roughly what spec and how old?" | Pilot feasibility; whether a local model can run at all |
| C4 | "If a new tool had to work there, what would it have to integrate with — source control, identity, ticketing, CI, build, artifact store — and does that integration have to work offline too?" | Integration requirements |
| C5 | "Who signs off before new software runs in your environment, and what does that review require — documentation, SBOM, penetration test, accreditation?" | Security approver, accreditation burden |

### 2.3 Segment B — Roles and buying (ask senior people only; ~2 min)

| # | Question | What you are gathering |
|---|---|---|
| B1 | "Who does the day-to-day work on this, and who is formally accountable for the outcome?" | User vs. accountable owner |
| B2 | "If this kind of work took half the time, whose budget would pay for it — and is that budget already allocated, or would it need a new request?" | Budget ownership, budget cycle |
| B3 | "How do you buy specialised engineering software today? An approved vendor list, a PO process, a rate contract? Roughly how long from evaluation to signed PO?" | Procurement path, sales-cycle reality |
| B4 | "Who could run a 4–6 week pilot on a real, non-production repository on isolated hardware? And what would make them say yes, or no?" | Pilot feasibility, access, success criteria |

### 2.4 Segment D — Contradiction probes (last, only if the interview is going well; ~2 min)

| # | Question | Why |
|---|---|---|
| D1 | "You said that's expensive and manual — but you also mentioned [their tool/process] already handles it. Help me reconcile those two." | Surfaces substitute adequacy vs. stated pain |
| D2 | "You said code can't leave the environment — but developers do sometimes paste snippets into public tools, don't they? Where exactly is the line drawn in practice?" | **Surfaces policy-vs-behaviour gap.** This is where the real product opportunity often hides. |
| D3 | "Who would block this project if it succeeded, and why would they?" | Surfaces hidden blockers and anti-champions |
| D4 | "If nobody built anything new here, what would you do instead next year?" | Surfaces the true cost of inaction |

### 2.5 Close (30 seconds)

> "That's really useful, thank you. Can I send you a one-paragraph summary of what I heard, so you can correct me if I've got it wrong?"
> "Is there anyone else on your side who sees this differently — someone who'd tell me it's not a problem?"

**Always ask the second question.** It doubles your next interview and tells you who the anti-champion is.

---

## 3. Role-specific one-liners (adapt the opening)

| Role | Opening adjustment | Questions to prioritise |
|---|---|---|
| Lead / senior software engineer | "I'd like to understand how you actually work — the tools, the steps, what you wish you didn't have to do." | A1, A2, A4, A5, A6, D2 |
| Engineering director / head of engineering | "I'm studying how engineering work happens in isolated environments, and what's actually feasible to automate." | A2, A4, B1, B2, B4 |
| Security approver / ISSO / product-security lead | "I'm not asking you to approve anything — I want to understand what your review process requires." | C1, C2, C5, A6, D3 |
| Infrastructure / IT lead | "I want to understand the transfer and update paths, since those seem like the hard part." | C2, C3, C4 |
| Procurement / purchase | "I want to understand how specialised engineering software gets bought here." | B2, B3 |
| Professor / academic supervisor | "I'm mapping the research gap between industrial isolated-network engineering and published work." | A1, A2, A6 + offer a student project/data collaboration |
| Defence PSU / labs industry-relations or SPOC | "I'm a student; I want to understand the process for a startup or university to engage with your establishment." | B3, B4, C1 + the published channel (E5) |
| Startup founder / iDEX winner | "I'm mapping how small defence teams actually build and test software under customer security constraints." | A1, A4, A6, C1, C5 |

---

## 4. Three outreach messages

**Rules applied to all three:** no product, no demo, no "AI assistant", no attachment in message 1, no request for a purchase or pilot, explicit permission to decline, and a **time-boxed ask of 15 minutes**. Replace `[bracketed]` fields. Keep each under ~140 words.

### 4.1 Email (cold / institutional)

**Subject:** 15 minutes — how software testing works on isolated networks (student research, no pitch)

> Dear [Role/Team],
>
> I'm [name], a final-year engineering student at IIT Gandhinagar. I'm researching how software engineering actually happens inside isolated and restricted networks — defence labs, space centres, power and nuclear plants — because I've found very little published on it.
>
> I'm not selling anything and I have no product. What I want is 15 minutes to understand how work really flows in your environment: where the time goes, what breaks, and what the rules are around code and tools. If anything I ask is sensitive, say so and I'll stop.
>
> Two things that would help most: (1) what a typical piece of work looks like end to end, and (2) what's genuinely not allowed to leave the environment.
>
> Would 15 minutes this week or next work? If it's easier, I can come to [city] — I travel to [region] regularly. If this isn't relevant to you, could you point me to the person who owns this?
>
> Best regards,
> [Name] · IIT Gandhinagar · [email] · [LinkedIn]

**Variants for institutional recipients (DRDO / ISRO / PSUs):** cite the *published channel* rather than implying personal access.
> "I'm reaching out via [the DRDO Industry Interaction Groups directory / the ISRO Industry Collaboration page] because I understand formal engagement runs through your published channels. My request is a short discovery conversation only — no proposal, no attachment."

### 4.2 LinkedIn (direct to a person)

> Hi [First name] — [one specific, checkable line about their work: "your team's work on [X]"].
>
> I'm [name], a final-year student at IIT Gandhinagar researching how software teams in isolated networks handle legacy code, testing and traceability. No product, no pitch — I'm trying to find out whether this is a real problem or whether it's already solved well.
>
> Would you be open to 15 minutes? I ask engineers and security leads, and I'm happy to work around your schedule. If it's not you, who would know best?
>
> [link]

**LinkedIn rules that matter:** no connection-request note longer than ~300 characters; do not use "AI" in the note; send the full message only after they accept (or as a comment if the note is clearly too short).

### 4.3 Warm-intro request (to an IITGN alum, faculty member, mentor, or iDEX/ARAI contact)

> Hi [Name] — hope you're well. I'm a final-year student at IIT Gandhinagar working on [topic].
>
> I'm trying to reach people who run software engineering inside isolated or restricted networks — defence labs, space centres, nuclear and power, and defence/aerospace companies — to understand how work actually happens there. I'm not building or selling anything yet; I'm doing discovery, and the point is to find out whether there's a real problem before I build anything.
>
> Would you be comfortable introducing me to one person in your network who sees this from the engineering side — ideally someone who'd be honest about whether it's a problem? A 15-minute conversation, no preparation needed, and I'll send them a short note introducing myself first so it doesn't ambush them.
>
> If it's easier, could I just pick their brain for 15 minutes instead?
>
> Thanks, [Name]

**Warm-intro rules:** always send the target a short note first so the introduction doesn't ambush them; make it easy to decline; never use the connection's name as leverage ("[Name] said this is important").

---

## 5. Interview log template (fields from `09` §1)

**Copy one block per interview. One per person. File as `harness/w5/interviews/YYYY-MM-DD-<org>-<role>.md`.**

```yaml
# --- Identity ---
interview_id: INT-###
date: "YYYY-MM-DD"
time_start: "HH:MM"
duration_min: 
segment: "defence_lab | defence_psu | space | private_defence_startup | critical_infra | industrial_embedded | global_prime | ot_vendor | academic | other"
org: 
org_unit: 
city: 
role_of_interviewee: "user | champion | economic_buyer | security_approver | infra_lead | procurement | influencer"
was_warm_path: "yes | no"
warm_path_type: "iitgn_alumni | iitgn_faculty | ide_mentor | gujarat_defence_network | drdo_iig_channel | isro_channel | idex_network | arai_network | other | none"
referral_from: 
# --- Workflow evidence ---
workflow_discussed: "codebase_understanding | change_impact | requirements_traceability | test_generation | legacy_modernization | defect_investigation | other"
frequency_answer: 
trigger: 
consequence: 
manual_effort_hrs_per_week: 
current_tools_named: 
approval_flow: 
ai_tools_tried_rejected: 
rejection_reason: 
# --- Isolation & hardware (C) ---
c1_exactly_what_is_isolated: 
c2_transfer_path: 
c3_hardware_available: 
c4_integration_requirements: 
c5_security_approver_and_requirements: 
# --- Roles & buying (B) ---
b1_user_vs_accountable: 
b2_budget_owner: 
b3_procurement_path_and_lead_time: 
b4_pilot_possible_and_criteria: 
# --- Contradictions ---
d1_substitute_reconciliation: 
d2_policy_vs_behaviour: 
d3_who_would_block: 
d4_cost_of_inaction: 
# --- Quotes ---
verbatim_quotes:
  - "..."
# --- Capture ---
next_step: 
evidence_quality: "direct_observation | self_report | second_hand"
recording_consent: "yes_audio | yes_notes_only | no"
follow_up_date: 
# --- Scoring (09 §3, rate 1-5 after the interview) ---
freq_score: 
consequence_score: 
effort_score: 
substitutes_score: 
data_boundary_score: 
hardware_score: 
```

**Interviewee quote discipline:** capture verbatim quotes with quotation marks in `verbatim_quotes` — never paraphrase inside quotes, never invent a quote. If they said it in a dialect or were unclear, write `[unclear]`. Mark any second-hand claim (e.g. "the security team said...") as `second_hand` in `evidence_quality`.

---

## 6. Scoring & what to do with it

Rate the six domains in `09` §3 on 1–5 after each interview (scale definitions are in `09` §3). Do **not** compute the `09` §4 composite until you have ≥3 interviews per segment — `09` §4 says scores stay hypotheses until confirmed by ≥3 independent interviews per segment.

**Two numbers to report every evening:**
1. **Isolation score (C1)**: how many interviewees described an environment where *code itself* cannot reach a public service. This is the founder's core premise. If it is 0 or 1 out of 12, the premise is wrong and the pitch must change before more interviews happen.
2. **Contradiction count (D2)**: how many said "we can't send code out" *and* described pasting snippets into public tools anyway. Each one is a candidate policy-vs-behaviour wedge.

**Do not compute or report any market size, TAM, or budget figure.** `09` §9 forbids it without a cited methodology, and none of these interviews produce one.

---

## 7. One-week schedule that fits 15–25 interviews

| Day | Activity | Target |
|---|---|---|
| Day 1 | Send 25 messages: 8 email, 8 LinkedIn, 9 warm-intro requests. Log every send in `TARGET_LIST.md` order. | 0 interviews |
| Day 2 | Follow up once on non-responses (one line only). Start 2–3 calls that replied. | 2–3 |
| Day 3 | 3 calls. **Ask each for a referral.** | 3 |
| Day 4 | 3 calls + 8 new messages (2nd wave: industrial/embedded block, rows 50–60) | 3 |
| Day 5 | 3 calls + 2 site visits if in Gujarat (SAC row 21, PRL row 28, an Adani/Torrent/Ahmedabad utility row 46, Tata Sanand row 53, Cummins Ahmedabad row 51) | 3 + 2 |
| Day 6 | 2–3 calls; log and score everything; cluster the C1 answers | 2–3 |
| Day 7 | Write the interview synthesis. **Decide segment. Do not build.** | 0 |

**Realistic yield:** 25 messages → ~8–12 replies → ~6–9 completed interviews. **To reach 15–25, send 60+ messages.** Plan for 60 sends, not 25. A 40% reply rate to a cold student request from a defence lab is already optimistic.

**If access stalls (likely):** industrial/embedded rows (50–60) and the ARAI council (row 56) are the highest-yield fallbacks — lower clearance, faster response, and a direct test of the W2 segment question. Critical-infrastructure rows (39–49) are the lowest-yield and should be attempted through an institutional channel only, never cold.
