# Codex workspace status (setup receipt, 2026-09-25)

- Repository path: `C:\Users\saura\Downloads\regulator-predict`
- Origin: `https://github.com/saurabh19891989-hue/regulator-predict.git` (fetch and push)
- Source handoff branch: `origin/claude/optimistic-planck-3efc05`
- Source handoff commit: `d93e255ec694c62cf056172734fed7c163024b9e` (includes the `93090ee` pause checkpoint)
- Current working branch: `astra/regulatory-predict`, created directly from the source handoff commit and tracking `origin/astra/regulatory-predict`
- HEAD at completed setup: `5514f16a60fd8f891394f8352ac2a9f91e76f309` (this receipt commit)
- Working tree status at completed setup: clean; `.venv/` is ignored
- Push status at completed setup: successful; this receipt commit is on origin with upstream tracking
- Runtime/environment: repository documents Python 3.11; local Python 3.12.10 is available. `.venv` uses Python 3.12 with system site packages and `jsonschema` installed locally. No dependency manifest or build script is present. Use `$env:PYTHONUTF8='1'` on Windows to avoid CP1252 encoding failures.
- Test result: `9 passed` in 452.13 s using `$env:PYTHONUTF8='1'; .\.venv\Scripts\python.exe -m pytest -q tests` (384 `datetime.utcnow` deprecation warnings). The forecast ledger separately verified: 60 records, hash chain OK.
- Authentication limitation: none for Git fetch/push through configured Git Credential Manager. GitHub CLI is not logged in, but is not needed for this workflow.
- Handoff files: `GPT_ASTRA_HANDOFF.md`, `CLAUDE.md`, `PROJECT_STATUS.md`, `BACKTEST_PROTOCOL.md`, `docs/PREREGISTRATION.md`, `PROTOCOL_DEVIATIONS.md`, `TASK_QUEUE.json`, `PAUSE_CHECKPOINT.md`, and `DATA_MANIFEST.md` are present.

Next recommended action: **Read GPT_ASTRA_HANDOFF.md and begin the autonomous Astra project directive.**
