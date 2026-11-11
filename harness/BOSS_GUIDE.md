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

## Diagnosing a window that goes quiet or claims done with no file

Never accept "done" without the file on disk (see Review pattern above). When a window claims done but `harness/<window>/REPORT.md` is missing or empty, diagnose read-only before asking the owner to do anything:

```bash
sqlite3 -readonly ~/.local/share/opencode/opencode.db "PRAGMA busy_timeout=8000;" \
  "SELECT id,title,directory,time_updated FROM session WHERE parent_id IS NULL AND directory='<project path>' ORDER BY time_updated DESC;"
```

Then for the suspect session, check the finish reason on its latest assistant message:

```bash
sqlite3 -readonly ~/.local/share/opencode/opencode.db "PRAGMA busy_timeout=8000;" \
  "SELECT time_created, json_extract(data,'\$.role'), json_extract(data,'\$.finish') FROM message WHERE session_id='<id>' ORDER BY time_created DESC LIMIT 2;"
```

- `finish='length'` — the reply hit the model's output cap mid-task. The window looks finished but isn't. **Fix: the owner types "continue" in that exact window** — this is the most common cause (confirmed by south-0f and seen directly on W1, 2026-11-11).
- No session row for the project directory — the paste never reached a window there (wrong window, or wrong folder). The owner opens a window in the project and pastes again.
- `finish='stop'` but still no file — it finished normally without writing. Re-paste with "write the file first, explain after" appended.

To read message text content (for confirming which task a stuck session was given), content lives in the `part` table, not inline in `message.data`:
```bash
sqlite3 -readonly ~/.local/share/opencode/opencode.db "PRAGMA busy_timeout=8000;" \
  "SELECT json_extract(data,'\$.text') FROM part WHERE message_id IN (SELECT id FROM message WHERE session_id='<id>' AND json_extract(data,'\$.role')='user') ORDER BY time_created ASC LIMIT 1;"
```

**Prevention (per swa-erp-d8 and south-0f):** every future paste should end with "Keep every chat reply under 10 lines; write the file first, explain after" to reduce truncation risk, and should always use the full project-relative or absolute output path (never a bare filename) to avoid wrong-path writes like the one caught on W2.
