# 07 — Next-Steps Dispatch Protocol (Orchestrator Handoff)

**Prepared by:** Claude, acting as orchestrator/strategist on the founder's instruction.
**Date:** 11 November 2026.
**Purpose:** Turn deliverables 01-06 into an immediate, sequenced action list. This file is the protocol — hand it to the execution agent as-is; it should not need to re-derive strategy from scratch.

---

## 0. Reality check before anything else

- YC Winter 2027's on-time application deadline was **2 November 2026, 8pm Pacific Time** (see `01` §11, `06` §11). Today is 11 November 2026. **That window is closed.** Do not plan this sprint around hitting it. If a later/rolling YC batch exists, verify it independently on ycombinator.com/apply — do not assume one.
- The separate campus "IDE" incubator program (acronym collision — this is the pitch/mentorship program, not an Integrated Development Environment) has no new deadline yet: PPT submissions closed EOD 11 Nov 2026; mentor results are expected "by Monday" (~16 Nov 2026), already delayed once.
- **Time available:** no hard external deadline exists right now except the ~16 Nov mentor-results checkpoint. Treat now -> 16 Nov as the research/build window. Re-plan once results or a next-round requirement are known.

## 1. Day-1 repository setup (per `03` §2-3, §9)

Give this to the execution agent verbatim:

1. `git init` this directory (or branch into a fresh `airgap-ai-platform/` if the founder wants the original handoff docs kept untouched and separate from the working repo — founder's call, not assumed here).
2. Create `AGENTS.md` at the root using the template in `03_IDE_AGENT_AND_STARTUP_INITIALIZATION.md` §3 verbatim, adapting only the project-name line.
3. Create the `docs/`, `agents/`, `prompts/`, `research-data/`, `evals/`, `supply-chain/` directory skeletons from `03` §2.
4. **Do not create `src/` yet.** No vertical slice has been validated — building code modules now would be exactly the "uncontrolled vibe coding" deliverable 01 says the founder rejects.
5. Start `DECISION_LOG.md` (ADR index) and `CLAIM_LEDGER.md` (using the YAML schema in `02` §6) at the repo root — both empty until the first research or decision lands in them.
6. Commit: "Initialize repo scaffold from founder handoff package."

## 2. Research dispatch order (per `02` §3)

Deliverable `02` already contains all 12 ready-to-run specialist prompts — use them verbatim, do not rewrite them. Dispatch in this priority order; the near-term need is a jury-facing PPT, not the full YC-grade research program:

**Wave 1 — run in parallel now (needed for any pitch):**
- Agent 6 — Competitor and substitute analyst
- Agent 7 — Customer discovery and vertical selection
- Agent 8 — Workflow and product-wedge analyst
- Agent 12 — Adversarial investment committee (stress-test the pitch before anything is built)

**Wave 2 — after Wave 1 synthesis (needed before committing to a technical story):**
- Agent 2 — Local models, inference and hardware architect
- Agent 4 — Security and adversarial red team
- Agent 5 — Air-gap lifecycle and supply-chain specialist

**Wave 3 — deeper technical/academic grounding, lower urgency for the pitch:**
- Agents 1, 3, 9, 10, 11

Each agent must return the outputs required in `02` §1 and file claims into `research-data/claims/` using the evidence-grade schema in `02` §6. No agent may use a plugin/skill as the default answer (per `02` §1 independence requirements).

## 3. Synthesis target

Once Wave 1 returns, run the final synthesis prompt from `02` §8 to produce one decision memo. That memo, plus `01` (vision/strategy) and `06` (hybrid methodology), are the three documents the campus PPT gets written from — not a fresh rewrite of the idea from memory.

## 4. Open items — nothing blocking right now

- No founder input needed to proceed with Wave 1.
- Flag back to the orchestrator when Wave-1 synthesis is done (for a PPT-outline pass) or when the ~16 Nov mentor results define whether there's a new hard deadline.
