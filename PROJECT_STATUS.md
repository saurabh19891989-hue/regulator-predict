# PROJECT_STATUS.md — Regulatory Predictive Precursor Engine

**Status:** GATE 0 IN PROGRESS — data collection (executors running), pipeline built
**Last updated:** 2026-09-25 (session 1)
**North-star phase:** Prove or disprove predictive regulatory signal before building downstream market-impact infrastructure.

## Current Gate
GATE 0 — Infrastructure + Historical Backtest. Analysis plan and GO/NO-GO bands are FROZEN in
`docs/PREREGISTRATION.md` (committed 2026-09-25 12:03 UTC, before any forecast or outcome review).

## How to resume (read in this order)
1. `CLAUDE.md` (constitution) → `BACKTEST_PROTOCOL.md` → `docs/PREREGISTRATION.md` (frozen plan) →
   `docs/EXECUTOR_GUIDE.md` (data rules) → this file → `TASK_QUEUE.json`.
2. Pipeline: `python3 -m rpe.validate data/raw/<ws>` → `python3 -m rpe.build` → `python3 -m rpe.snapshots` →
   `python3 -m rpe.packets make <run> ...` → run isolated forecasters (see "Forecaster isolation") →
   `python3 -m rpe.ledger ingest <run> --model <m>` → `python3 -m rpe.evaluate --primary-runs ...`.
3. Tests: `python3 -m pytest -q tests`.

## Dataset Counters
- Candidate threads discovered: 0 (9 executor workstreams running)
- RAPID usable threads: 0
- GOLD audited threads: 0
- Positive/resolved actions: 0
- Stalled/withdrawn/no-action controls: 0
- Historical forecast snapshots: 0
- Ablation runs: 0

## Workstreams (data/raw/<ws>/, executor = Sonnet 5)
| ws | scope | frame | status |
|---|---|---|---|
| us_fr | US Federal Register significant NPRM→final | H: 2019-07..2023-12 systematic 85; C: 2025-06..2026-06 census (post-model-cutoff holdout); X: recent resolved pre-July | running |
| us_reginfo | Unified Agenda editions + OIRA EO12866 reviews keyed by RIN (merged into us_fr by rpe.build) | 2018–2026 | running |
| us_fda | FDA draft guidance → final guidance | H: 2019-07..2023-06 (30); C: 2025-06..2026-04 (≤25) | running |
| in_sebi_h | SEBI consultation papers → adoption | 2022-01..2024-03 systematic 25 | running |
| in_sebi_r | SEBI consultation papers (holdout) | 2025-10..2026-06 census ≤30 | running |
| in_rbi | RBI drafts/discussion papers → final directions | H 2021-07..2024-06 (22); R 2025-10..2026-06 (≤10) | running |
| in_irdai | IRDAI exposure drafts → regulations | H 2021-07..2024-06 (20); R (≤8) | running |
| in_trai | TRAI consultations → recommendations/regulations | H 2021..2023 (20); R (≤8) | running |
| in_dgtr | DGTR final findings → MoF duty notification | 2020-07..2022-12 (22) | running |

## Model Routing (as implemented)
- Director: Opus 5.5 (this session). Executors: Sonnet 5 (`general-purpose` agents).
- Blind forecaster: Opus 5.5 via the `statusline-setup` agent type with model override — it is the only available
  agent type whose tools are exactly Read + Edit (no web, search, shell, glob). Custom `.claude/agents/*.md`
  definitions do not register mid-session (tested); `.claude/agents/blind-forecaster.md` is kept for future sessions.
- Ablation forecaster: Sonnet 5, same isolated agent type. Leakage audit: Opus 5.5. Fable 5.1: not yet used.

## Forecaster isolation (leakage controls)
- Packets rendered by `rpe.packets` to a scratch directory outside the repo; forecaster sees only its packet path and
  an output stub; no outcome fields, no internal ids (hard guard raises if a thread/evidence id appears), opaque
  snapshot ids, evidence relabelled E1..En, only evidence with available_date ≤ cutoff, one snapshot per thread per
  agent context, arm names never shown.
- Memorisation controls: CLEAN stratum (outcome after 2026-07-01 > model knowledge cutoff), TITLE_ONLY arm, recall
  probe, self-report `recognised_outcome`.

## Budget
- Budget cap: USD 100 (user-supplied). Warning 75%; hard stop / escalation 95%.
- Prices used for estimates (per M tokens, in/out): Opus 5.5 $4/$20, Sonnet 5 $2/$10, Fable 5.1 $10/$50, Haiku 4.5 $1/$5.
- Actual spend is NOT observable from inside this session; estimates come from subagent token totals × blended
  rates (Sonnet ≈ $1.0/M, Opus ≈ $2.0/M blended, assuming most agent-loop input is cache reads) plus a Director
  allowance. Log: `data/derived/spend_log.jsonl`.
- Estimated spend so far: ≈ $3 (Director setup + 1 haiku test agent). Executors pending.

## Completed
- RP0-01 schemas (thread/evidence/outcome/forecast/audit, v1.0.0), validator + leakage lint, tests (6 passing).
- Core pipeline: build (merge + strata), snapshots (Design T + Design K + 8 arms), packets, ledger (hash chain,
  append-only), baselines (4, pre-registered), evaluator (action/timing/content/lead-time/ablation, clustered CIs).
- Pre-registration of analysis plan and GO/NO-GO bands.
- Environment reachability mapped (see docs/EXECUTOR_GUIDE.md §8).

## Active
- RP0-02/03/04/05: 9 executor workstreams collecting threads (all launched 2026-09-25 ~12:00 UTC).

## Blocked / constraints
- web.archive.org unreachable (tunnel reset) → no Wayback verification; GOLD relies on official-gazette dates
  (Federal Register), dated PDFs/press-release numbers, and independent audit.
- egazette.gov.in, cbic.gov.in, nppaindia.nic.in blocked → CDSCO/NPPA dropped from pilot; DGTR outcomes via
  dgtr.gov.in OMs / news.
- sec.gov requires a declared-identity User-Agent → SEC rules sourced via Federal Register API instead.

## Risks to Track
- Forecaster memorisation of HIST outcomes (primary threat) → CLEAN holdout + TITLE_ONLY + probe.
- Executors know outcomes when writing summaries/claims → lint + Opus leakage audit.
- T-anchored cutoffs inflate discrimination → added T-365/T-270 and Design K (prospective) — see prereg §2.
- Small CLEAN sample → wide CIs; report power honestly.
- Tier C sparse for US threads → Tier-C increment test relies mainly on India threads.
- historical pages silently revised; retrospective wording; duplicated news; inconsistent process states.

## Next Actions
1. As executors finish: validate, review NOTES.md, fix/reassign failures; merge reginfo into us_fr.
2. `rpe.build` → `rpe.snapshots`; freeze RAPID sample; select GOLD candidates.
3. Launch Opus leakage audit on GOLD candidates + risk-weighted RAPID sample (parallel with forecasting).
4. Primary Opus forecasts (ALL arm, designs T+K) + Opus TITLE_ONLY control + recall probe.
5. Sonnet ablation grid on design-T cutoffs T-180/T-90/T-30.
6. Content labelling pass where executor content labels are provisional.
7. Evaluate → GO/NO-GO report (reports/GATE0_REPORT.md).

## Decision Log
### 2026-09-25 — D001
Decision: Do not build stock/option/valuation layers before predictive signal is demonstrated.
Reason: They are downstream transformations and cannot create predictive information.
### 2026-09-25 — D002
Decision: Backtesting is the first scientific gate.
### 2026-09-25 — D003
Decision: Use two datasets — RAPID and GOLD.
### 2026-09-25 — D004
Decision: Blind forecasters run as `statusline-setup` agents (Read+Edit only) with model override; packets outside repo.
Reason: No API key in container; custom agent types don't register mid-session; this is the only agent type with no
web/search/shell tools. Verified by a test agent that reported tools = [Read, Edit, SubagentHandback].
### 2026-09-25 — D005
Decision: Add a CLEAN temporal stratum (outcome after 2026-07-01) and Design K calendar cutoffs as the primary
memorisation-free test; HIST results are reported but treated as upper bounds unless they match CLEAN.
Reason: The forecaster's training data (to June 2026) likely contains outcomes of historical threads.
### 2026-09-25 — D006
Decision: Sample from precursor populations (census/systematic over listings), never from outcomes; pseudo-anchors
for no-action threads drawn from matched positive gap distributions; extended cutoffs T-365/T-270.
Reason: protocol anti-selection rule; avoid elapsed-time tells; avoid imminent-vs-never inflated discrimination.
### 2026-09-25 — D007
Decision: FULL_TRAJECTORY ≡ B_PLUS_C (all official items); LATEST_DOCUMENT_ONLY = single latest official item;
primary forecast arm ALL = B+C+S+D. Identical packets across arms are deduplicated and scored once.
### 2026-09-25 — D008
Decision: Stakeholder evidence class S added to tier vocabulary (B/C/S/D) so the stakeholder ablation is explicit.
### 2026-09-25 — D009
Decision: Pilot regulators: US FR (multi-agency), FDA guidance, SEBI, RBI, IRDAI, TRAI, DGTR. CDSCO/NPPA dropped
(sites blocked). DGFT not sampled separately (DGTR covers trade remedies).
