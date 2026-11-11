# Harness Boss Guide — AirG.A.P

Adapted from the conventions running in the `south-0f` and `swa-erp-d8` sessions, scaled down to this project's size (4 Wave-1 research tasks, not a multi-round code audit).

## Roles
- **Boss (this Claude session):** writes the paste for each window, reviews each window's `REPORT.md` against the claim-evidence schema in `02_INDEPENDENT_RESEARCH_AGENT_PROTOCOLS.md` §6, and decides what happens next. Never edits the research/implementation output itself.
- **Owner (the founder):** copies each ACTIVE block from `harness/PASTES.md` into an idle OpenCode window, and tells the boss when a window is done.
- **Window (an OpenCode worker):** runs exactly one task from `harness/PASTES.md`, writes only inside its own `harness/<window>/` folder, and ends by printing its status line.

## Paste convention
Each paste in `harness/PASTES.md` is self-contained: "You are <WINDOW>. This text is the only task." + the task + its exact output paths. No window reads another window's folder or this guide.

## Output convention
Each window writes only to `harness/<window>/`:
- `REPORT.md` — max ~150 lines: Verdict/summary, key findings table, evidence log (source + grade per the `02` §6 schema), open questions. This is the one file the boss reads first.
- `<TOPIC>.md` — full-length backup detail if `REPORT.md` needs to stay short.
- `STATE.md` — running notes, updated as the window works (not required for a short one-shot task).

A window ends by printing: `<WINDOW> done gates=PASS|FAIL blocked=<none|list>`.

## Shared log and ledgers
Every finished task appends one line to `harness/STATUS.log`:
`YYYY-MM-DD HH:MM | WINDOW | TASK-ID short description | result`

Shared ledgers live in `harness/kb/`:
- `requests.jsonl` — one line per dispatched task (what, when, which window).
- `reviews.jsonl` — one line per boss review (verdict, what was accepted/rejected, why).
- `decisions.csv` — decisions that change strategy/architecture, with the source evidence.

## Mid-run questions
If the boss needs to answer a window that's already running, the boss writes `harness/<window>/OWNER_ANSWERS.md` and gives the owner a one-line paste telling that window to read it.

## Review pattern
The boss reads `harness/STATUS.log` for the status line, then opens the named `REPORT.md` and checks it against disk — never accepts a result on the strength of the log line alone.
