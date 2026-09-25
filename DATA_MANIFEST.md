# DATA_MANIFEST.md — artifacts NOT committed to git (large, regenerable, or scratch)

Created 2026-09-25 at pause. Everything else under `data/` IS committed (largest committed file:
`data/snapshots/index.jsonl`, ~15 MB). Container paths are ephemeral: anything below that is not committed is lost
when the container is reclaimed; all of it is regenerable or non-essential.

| exact path | size | provenance | regeneration | required to resume? |
|---|---|---|---|---|
| `data/raw/us_reginfo/agenda_entries.jsonl` | 46M | Bulk Unified Agenda XML (reginfo.gov), editions 201804–202510, parsed by `collectors/reginfo.py` | `python3 collectors/reginfo.py` (see its docstring / `data/raw/us_reginfo/NOTES.md`) | **No** — `rpe.build` falls back to the committed subset `data/raw/us_reginfo/agenda_entries_sampled.jsonl` (all RINs of the current US-FR threads). Needed only if new US-FR threads with new RINs are added. |
| `data/raw/us_fr/cache/` | 95M | Cached Federal Register API responses + govinfo PDFs used by `collectors/us_fr.py` | re-run `collectors/us_fr.py` (re-fetches from the public API) | No |
| `data/raw/*/cache/` (all other workstreams) | ~0 (empty dirs) | executor download caches | n/a | No |
| `/tmp/claude-0/-home-user-regulator-predict/91e5b9f5-d683-5b72-a27c-87c3694866b1/scratchpad/fc/` | small | forecaster inbox/outbox scratch (RPE_FC_ROOT) | `python3 -m rpe.packets make …` | No — SMOKE1 packets and outputs were copied to `data/forecasts/packets/SMOKE1/` and `data/forecasts/raw/SMOKE1/` |
| `/root/.claude/projects/-home-user-regulator-predict/91e5b9f5-…/*.jsonl` | ~tens of MB | Claude Code transcripts (Director + 15 subagents) | not regenerable | No — model/usage metadata summarised in `data/derived/usage_audit.json` and `data/derived/usage_audit_table.txt`; transcripts contain conversation content and are deliberately not committed |
| `*.pdf` anywhere | varies | downloaded regulator PDFs | re-download from `source_url` fields | No |

Committed and required to resume: `data/raw/<workstream>/*.jsonl|json|md` (executor outputs), canonical
`data/threads|evidence|outcomes/`, `data/snapshots/index.jsonl` (current, NOT yet frozen — see FINDING-002),
`data/forecasts/` (ledger, runs, raw outputs, packets, SMOKE1_index_rows), `data/derived/`, `schemas/`, `rpe/`,
`collectors/`, `tests/`, `docs/`, root programme documents.
