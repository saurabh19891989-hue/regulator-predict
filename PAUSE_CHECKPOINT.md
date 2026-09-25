# PAUSE_CHECKPOINT.md

- **Paused:** 2026-09-25 12:40:42 UTC (user instruction received ~12:35 UTC; all agents stopped 12:31–12:35 UTC)
- **Reason:** Anthropic credit nearly exhausted; project moving to GPT-6 Astra / OpenAI. Resume only on explicit instruction.
- **Repository:** https://github.com/saurabh19891989-hue/regulator-predict · local `/home/user/regulator-predict`
- **Branch:** `claude/optimistic-planck-3efc05` (tracks `origin/claude/optimistic-planck-3efc05`)
- **Parent commit before checkpoint:** `bdbaf2a`
- **Checkpoint commit:** the commit that adds this file ("PAUSE CHECKPOINT: …"); its hash is recorded in the follow-up
  commit "PAUSE_CHECKPOINT: record checkpoint hash" below.
- **Working tree at checkpoint:** clean after commit (all project state committed; ignored artifacts listed in DATA_MANIFEST.md).
- **Outstanding background processes:** none. LLM agents: 0 running (verified with ListAgents after TaskStop of 8
  agents). Local shell jobs: the last pytest background job was stopped; the final test run (9 passed) ran in the foreground.
- **Uncommitted files:** none intended. Ignored (not committed, see DATA_MANIFEST.md): `data/raw/us_fr/cache/` (~95 MB),
  `data/raw/us_reginfo/agenda_entries.jsonl` (~46 MB), empty `data/raw/*/cache/` dirs, forecaster scratch in /tmp.
- **Tests:** `python3 -m pytest -q tests` → 9 passed (308 s) at pause.
- **Ledger:** `python3 -m rpe.ledger verify` → ok, 60 records (SMOKE1 only).
- **Datasets:** 334 RAPID threads (US-FR 179, US-FDA 55, IN-SEBI 44, IN-RBI 27, IN-IRDAI 19, IN-TRAI 10); GOLD 0;
  205 positive / 129 no-action; 2,065 evidence items.
- **Estimated Anthropic spend:** $76.08 at list prices (Sonnet 5 $59.74, Opus 5.5 $16.31, Haiku 4.5 $0.02).
- **Next:** `GPT_ASTRA_HANDOFF.md` §11.
