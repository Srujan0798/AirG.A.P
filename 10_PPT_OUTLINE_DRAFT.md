# 10 — Campus IDE Pitch: PPT Outline

**Status:** All four Wave 1 windows done and reviewed — see `harness/synthesis/WAVE1_SYNTHESIS.md`. Content complete; only slide-count trim left (depends on jury's actual time limit, not yet known).
**Framing:** Big vision up front, narrow validated first step as the proof, sharpened by W1 into a specific positioning claim (the control-plane layer, not another agent) rather than a generic "agentic workbench."

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
- Not "another agentic coding tool" — a **governed control plane** that sits around a replaceable local agent: deterministic policy, provenance-checked intake, immutable approval ledger, in-boundary updates, accreditation evidence.
- Offline-by-construction, human-approval-gated, fully auditable (`01` §7 architecture principles).
- Why this framing, not "agentic workbench": W1's competitor survey found every layer underneath (inference, clusters, SBOM tooling, local coding agents) already has credible occupants — none of them publish an identity model, audit ledger, or standardized offline-update path. That ungoverned gap is the product, not a better agent.

## Slide 5 — Day-1 proof point (the narrow, validated wedge)
- Per independent red-team review (W4) and workflow analysis (W3): start with **one workflow** — read-only codebase understanding + sandboxed test-generation — not the full agent swarm.
- Why: reviewable output, works on non-production data, no live-system control, objective metrics (test coverage, pass/fail), feasible on local models today.
- This is the thing we can actually demo, not just describe.

## Slide 6 — Who we go to first
- **Lead segment: Defense & Aerospace suppliers' isolated engineering labs** (`09` ICP) — legacy/safety-adjacent code, a named budget owner (IRAD/contract-funded), a natural offline boundary (classification/ITAR), and a repeatable workflow across similar suppliers.
- **Fast-follow: Industrial/embedded vendors** — an independent re-score (W2) shows this segment nearly tied with Defense/Aerospace (15 vs. 13 on `09`'s own rubric), so if defense access/clearance proves slower than expected, this is the next door, not a fallback we're hiding.
- Founder decision, 2026-11-11 — logged in `harness/kb/decisions.csv`.

## Slide 7 — Why the honesty is the pitch
- Every claim in this deck is sourced to a document in our repo (public, on GitHub) and was independently red-teamed by our own adversarial review process before this slide existed.
- We know the five strongest reasons NOT to build this (W4) and we're showing up anyway, with a narrower first step than our own ambition — that's the discipline a jury should want to fund.

## Slide 8 — Competitive landscape
- Surveyed ~38 solutions across 6 layers (inference, disconnected clusters, SBOM/supply-chain, local coding agents, RAG/knowledge, appliance vendors) — evidence-graded, sources in `harness/w1/COMPETITOR_MATRIX.md`.
- **Zero direct competitors found.** Two close-but-different: Legion Centurion (accredited national-security platform, no engineering workflow) and Element 31-style appliance chassis (displaces the software category entirely rather than competing with it).
- **The pattern:** every layer is occupied by a credible product — inference (NVIDIA NIM, vLLM, llama.cpp), clusters (OpenShift, RKE2), SBOM (Anchore, Sonatype), local coding agents (Cline, Continue — 5 surveyed, all free, zero with published governance). We don't compete on any of these layers.
- **The gap:** seven vendors each hand-rolled their own disconnected-update mechanism; nobody has standardized identity/audit/provenance for this kind of system. That's what we build.

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
1. Trim to fit whatever slide-count/time limit the jury actually gave (chat log never specified one).
2. Note (W1 review flag): don't quote an exact "N competitors surveyed" number — W1's own summary counts are internally inconsistent (27 vs. 33 vs. the actual 38 table rows). Say "~38 surveyed" or point to the matrix file rather than a precise figure.

**Resolved:** Slide 6 names Defense/Aerospace as lead segment, Industrial/embedded as fast-follow (founder decision, 2026-11-11).
