# PROJECT_STATUS.md — Regulatory Predictive Precursor Engine

**Status:** ⏸ PAUSED (user instruction, 2026-09-25 ~12:35 UTC) — Anthropic credit nearly exhausted; project moving to
GPT-6 Astra / OpenAI models. No LLM jobs running. Resume only on explicit instruction. Handoff: `GPT_ASTRA_HANDOFF.md`.
**Last updated:** 2026-09-25 12:40 UTC
**Gate:** GATE 0 — historical point-in-time backtest (not yet evaluated; no GO/NO-GO answer exists yet)
**Repository:** https://github.com/saurabh19891989-hue/regulator-predict · branch `claude/optimistic-planck-3efc05`
· local path `/home/user/regulator-predict` · latest commit: see `PAUSE_CHECKPOINT.md`

## Exact current state
- Infrastructure: complete and frozen (schemas, validator/lint, build, snapshots designs T+C, 9 arms, packets,
  ledger, baselines, evaluator, probe, content judge, audit-patch mechanism). Tests: **9/9 passing** (308 s).
- Data: 334 RAPID threads from 6 regulator families, 2,065 evidence items; all workstreams validate with 0 errors.
- Forecasts: smoke test only (SMOKE1, Opus 5.5, 10 threads, 40 unique forecasts / 60 ledger records incl. aliases);
  excluded from headline metrics. Ledger hash chain verified.
- Audit: not run (GOLD = 0). Evaluation: not run. GO/NO-GO: not reached.

## Dataset counts by regulator (canonical build 12:37 UTC)
| family | threads | positive | no-action | HIST | LATE | GOLD candidates | evidence B/C/S/D |
|---|---|---|---|---|---|---|---|
| IN-IRDAI | 19 | 13 | 6 | 19 | 0 | 0 | 22/0/0/4 |
| IN-RBI | 27 | 16 | 11 | 21 | 6 | 15 | 27/12/0/20 |
| IN-SEBI | 44 | 33 | 11 | 29 | 15 | 8 | 49/0/0/74 |
| IN-TRAI | 10 | 9 | 1 | 10 | 0 | 4 | 19/0/0/0 |
| US-FDA | 55 | 23 | 32 | 30 | 25 | 25 | 63/0/21/0 |
| US-FR | 179 | 111 | 68 | 119 | 60 | 60 | 1596/0/158/0 |
| **TOTAL** | **334** | **205** | **129 (39%)** | 228 | 106 | 112 | 1776/12/179/98 |
- Candidate threads discovered: 335 (1 excluded: low action-label confidence). RAPID usable: 334. GOLD audited: 0.
- sampling_origin: precursor_population 334 / backfill 0 / purposive 0.
- Snapshots (B_PLUS_C arm): design C 801 · design T 2,286. Forecast snapshots completed: 40 unique (smoke).
- Ablation runs: 0. Outcome classes: action_mixed 100, action_as_proposed 74, action_softened 23,
  action_tightened 8, stalled_no_action 42, unresolved 83, withdrawn 4.
- US Unified Agenda/OIRA: 16 editions (Spring 2018–"2026"), 59,519 (edition, RIN) rows, 4,873 OIRA reviews;
  1,333 agenda/OIRA evidence items merged into US-FR threads.

## Agents/jobs active at pause (all stopped by the Director; 0 LLM jobs remain)
| job | model | state at pause | output preserved |
|---|---|---|---|
| executor in_sebi_h | Sonnet 5 | stopped mid-work (14 of 25 threads; writing #14) | threads/evidence/outcomes/sources.json |
| executor in_sebi_r | Sonnet 5 | stopped while writing NOTES/sources (30 threads done) | threads/evidence/outcomes |
| executor in_rbi | Sonnet 5 | stopped (27 threads; R6–R10 batch not written) | threads/evidence/outcomes |
| executor in_irdai | Sonnet 5 | stopped (19 H threads; R frame not started) | threads/evidence/outcomes |
| executor in_trai | Sonnet 5 | stopped (10 threads) | threads/evidence/outcomes |
| executor in_dgtr | Sonnet 5 | stopped before writing any thread | nothing (empty cache dir) |
| executor us_baserates | Sonnet 5 | stopped early | nothing (empty cache dir) |
| executor us_fr | Sonnet 5 | completed (179 threads) just before pause | full + NOTES.md + collector |
Completed earlier: us_reginfo (Sonnet 5), us_fda (Sonnet 5), 4 SMOKE1 forecasters (Opus 5.5), 1 isolation test (Haiku 4.5).

## Model routing audit (from transcript metadata; `python3 -m rpe.usage_audit`, `data/derived/usage_audit.json`)
- Executors: 100% `claude-sonnet-5` (NOT Opus — verified per request). Forecasters + Director: `claude-opus-5-5`.
  Isolation test: `claude-haiku-4-5`. Fable 5.1: never used. Routing matched the intended hierarchy.
- Deviation: every subagent inherited the session effort **xhigh** (intended medium) → higher cost per call.
- Estimated spend at list prices up to 12:40 UTC: **$76.08** (Sonnet 5 $59.74 · Opus 5.5 $16.31 · Haiku $0.02);
  final commit steps add < $1. Largest items: us_fr executor $13.80, Director $12.47 (to
  12:30), in_sebi_h $11.91. Cache reads dominate (~286 M tokens). Actual billed spend is not visible from inside
  the session.

## Tickets
| id | title | status |
|---|---|---|
| RP0-00 | Pre-registration | COMPLETE |
| RP0-01 | Schemas, ledger, validator, tests | COMPLETE |
| RP0-02 | Source registry | PARTIAL (sources.json for us_fr, us_fda, us_reginfo, in_sebi_h; reachability table in docs/EXECUTOR_GUIDE.md §8; India ws mostly missing sources.json) |
| RP0-03 | Discover candidate threads | PARTIAL (335 discovered; DGTR 0) |
| RP0-04 | Reconstruct RAPID timelines | PARTIAL (334 usable; several India frames incomplete) |
| RP0-05 | GOLD threads | NOT_STARTED (112 candidates; audit not run) |
| RP0-06 | Blind cutoff forecasts | PAUSED (smoke test only) |
| RP0-07 | Evidence ablations | NOT_STARTED |
| RP0-08 | Leakage red-team | NOT_STARTED (protocol ready: docs/AUDIT_GUIDE.md) |
| RP0-09 | Evaluation metrics | NOT_STARTED (code ready, tested on synthetic data) |
| RP0-10 | Fable adjudication | NOT_STARTED (optional) |
| RP0-11 | GO/NO-GO report | NOT_STARTED |
| RP0-12 | Content-label pass | NOT_STARTED |
| RP0-13 | US news enrichment | NOT_STARTED |
| RP0-14 | External US base-rate table | PAUSED (agent stopped; no output) |
| RP0-15 | Smoke test SMOKE1 | COMPLETE (valid pipeline; FINDING-001/002) |

## What remains unfinished
Collectors (DGTR entirely; TRAI, IRDAI-R, SEBI-H, RBI-R partial; India NOTES.md/sources.json), tier-C enrichment,
US news, content labels, external base rates, GOLD audit, recall probe, broad forecasts, ablations, masked test,
content judge, evaluation, GO/NO-GO report. See `GPT_ASTRA_HANDOFF.md` §11 for the sequence.

## Known methodological issues
FINDING-001 macro-political hindsight in forecaster rationales · FINDING-002 snapshot/pseudo-anchor instability
across rebuilds (freeze index before forecasting) · LATE stratum tied to the old model's stated cutoff (must be
re-derived for a new model) · sampling imbalance (SEBI-H 0 negatives, TRAI 1, FDA-LATE 0 positives) · tier C nearly
absent (12 items) → B-vs-B+C underpowered · heuristic US content labels · US news absent · executor-authored text
not yet audited · comment counts not point-in-time · Fall-2024 agenda date low-confidence · Design C 730-day cap ·
Design T inflates discrimination (mitigated by T-365/T-270 and Design C).

## Known source-access limitations
web.archive.org, egazette.gov.in, cbic.gov.in, nppaindia.nic.in blocked (CDSCO/NPPA dropped); FDA guidance DB
WAF-blocked; federalregister.gov HTML bot-gated (govinfo used); sec.gov needs declared UA; regulations.gov DEMO_KEY
rate-limited. Details: `GPT_ASTRA_HANDOFF.md` §7.

## Decision Log
- D001 No stock/option/valuation layers before signal is shown. D002 Backtest first. D003 RAPID + GOLD.
- D004 Forecasters isolated via `statusline-setup` agent type (Read+Edit only; custom agent types don't register
  mid-session). D005 post-cutoff stratum (now "LATE", DEV-002). D006 precursor-population sampling, matched
  pseudo-anchors, T-365/T-270. D007 FULL_TRAJECTORY ≡ B_PLUS_C. D008 stakeholder tier S. D009 pilot regulators
  (CDSCO/NPPA dropped). D010 infrastructure freeze + DEV-001..007 (12:20 UTC). D011 OIRA split (prereg amendment A1).
- D012 (12:35 UTC) Programme paused on user instruction; all agents stopped; handoff to GPT-6 Astra.
