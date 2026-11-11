# Wave 2 Synthesis (2026-11-11)

All four windows done and reviewed (harness/kb/reviews.jsonl). Reports: harness/w5..w8/REPORT.md.

## Position after Wave 2
The defensible claim narrowed. "AI governance inside the wall is unclaimed" is false: Tabnine, Codeium, GitLab Duo Self-Hosted and Cline Enterprise sell air-gapped assistants with their own SSO, RBAC and audit logs, and Palantir Security Forge runs governed, model-agnostic agents for cyber review (stack-locked, US government only). What survives: **a vendor-neutral layer that governs competing agents across the non-security engineering workflow (requirements -> code -> tests -> change impact), with signed offline intake and an accreditation evidence pack.** Deck slides 3 and 5 now say this.

Implication: interoperate with GitLab Duo or Tabnine where a lab already runs them; do not try to be another assistant.

## Customers (W5)
Hard isolation in India is documented for nuclear, power-grid OT (CEA) and defence/space labs (DRDO CAIR, ISRO). Industrial/embedded R&D is mostly connected (grade D). Best near targets: ISRO SAC Ahmedabad, DRDO CAIR, BEL Software SBU, HAL, GSAS (DO-178C evidence, small, reachable). Outreach kit ready. Correction pending: "IITG-TIC" is IIT Guwahati, not IIT Gandhinagar.

## India incumbent to watch (W7)
Innefu Labs, Sarvagata AI: "air-gapped sovereign agentic AI in a box", government-empanelled, Series B 2026-06. Today: intelligence workflows, not software engineering. Local-content rules may favour domestic vendors; AirG.A.P is domestic.

## Feasibility (W6)
One-shot test generation with a general 7B model on this Mac: 10 pass / 16 fail / 4 errors, about 40 tok/s, CPU only. Verdict marginal, and the human-approval gate is essential. Round 2 (coder model, repo context, repair loop) requested; it is the real test of our design.

## Money (W8)
SSIP 2.0 PoC grant up to Rs 2.5 lakh -> iDEX SPARK up to Rs 1.5 crore -> first paid pilot in months 4-6. Unit economics are assumptions only; hardware may be cheaper than assumed (W6 ran CPU-only).

## Bottleneck
Customer interviews. Everything above stays a hypothesis until 15-25 lab engineers and security leads answer the W5 guide. That is founder work; the boss and windows support it.
