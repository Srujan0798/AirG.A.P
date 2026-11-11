# 10 — Campus IDE Pitch: PPT Outline (Draft)

**Status:** Draft from `01`, `06`, `09`, and Wave-1 windows W2/W3/W4 (W1 pending — will add one competitor-landscape slide/stat once it lands).
**Framing:** Big vision up front, narrow validated first step as the proof — this resolves the W4 "full workbench vs. narrow pivot" tension without picking a side prematurely: ambition stays, but what we claim to have *proven* stays honest.

---

## Slide 1 — Title
AirG.A.P — AI for the Air-Gapped Economy
One line: Bringing frontier AI inside the walls that can never connect to the internet.

## Slide 2 — The opportunity
- YC Winter 2027 RFS #10: "AI for the Air-Gapped Economy" — named opportunity, not yet solved.
- Who needs this: defense/aerospace, industrial/embedded, critical infrastructure, financial, healthcare, public sector — orgs that legally/contractually cannot send code or data to cloud AI.
- Market framing from `01` §3: air-gapped is a spectrum (cloud → private → restricted → disconnected → fully air-gapped), and most "AI for air-gapped" offerings today only solve the infrastructure layer, not the full lifecycle.

## Slide 3 — The problem, concretely
- Engineering teams in isolated labs still do code comprehension, test writing, and change-impact analysis by hand — slow, error-prone, un-auditable.
- They can't use Copilot/ChatGPT/Claude because the code can't leave the boundary.
- **Caveat we say out loud:** zero customer interviews completed yet (per `09`) — this is a validated-opportunity pitch, not a validated-demand pitch. (Credibility move, not a weakness — see Slide 7.)

## Slide 4 — What we're building (the vision)
- A secure, offline, agentic engineering workbench: understand, test, modernize, and propose changes to code — without the code ever leaving the customer's boundary.
- Offline-by-construction, human-approval-gated, fully auditable (`01` §7 architecture principles).

## Slide 5 — Day-1 proof point (the narrow, validated wedge)
- Per independent red-team review (W4) and workflow analysis (W3): start with **one workflow** — read-only codebase understanding + sandboxed test-generation — not the full agent swarm.
- Why: reviewable output, works on non-production data, no live-system control, objective metrics (test coverage, pass/fail), feasible on local models today.
- This is the thing we can actually demo, not just describe.

## Slide 6 — Who we go to first
- Segment hypothesis: Defense/Aerospace suppliers' isolated engineering labs (`09` ICP) — OR Industrial/embedded vendors, which an independent re-score (W2) shows as a near-tie, not a clear #1.
- **We say this honestly in the pitch:** two strong candidate segments, interviews will decide — this is the single most important thing we learn next.

## Slide 7 — Why the honesty is the pitch
- Every claim in this deck is sourced to a document in our repo (public, on GitHub) and was independently red-teamed by our own adversarial review process before this slide existed.
- We know the five strongest reasons NOT to build this (W4) and we're showing up anyway, with a narrower first step than our own ambition — that's the discipline a jury should want to fund.

## Slide 8 — Competitive landscape
*[PENDING W1 — will list: who already covers infrastructure/model-serving (NVIDIA NIM, vLLM, llama.cpp), who covers local coding assistants, and the specific gap none of them close: the full offline lifecycle + audit/approval layer, not just local inference.]*

## Slide 9 — What we need next (the ask)
- A mentor/design-partner introduction into one of the two candidate segments.
- 15-25 structured interviews (guide already written, `09` §1) to settle the segment + workflow question before we build further.
- Not asking for build-it-now money — asking for validated access.

## Slide 10 — Roadmap (honest, gated)
- Weeks 1-2: interviews, settle segment/workflow (per `01` §10 execution sequence).
- Weeks 3-4: feasibility slice on one non-production repo, offline, egress-blocked.
- Gate-based, not date-based: we only move to the next stage when the evidence says so (`01` §9 Gates A-E).

---

**Open items before this is final:**
1. W1 competitor stats for Slide 8.
2. Founder call: does Slide 6 name one segment, or keep both candidates honestly open as written above?
3. Trim to fit whatever slide-count/time limit the jury actually gave (chat log never specified one).
