# GPT_ASTRA_HANDOFF.md — Regulatory Predictive Precursor Engine (Gate 0)

Handoff from the Claude (Anthropic) Director session paused 2026-09-25 ~12:38 UTC to a GPT-6 Astra Director.
Everything needed to resume is in this repository; no chat history is required.
Repo: `https://github.com/saurabh19891989-hue/regulator-predict`, branch `claude/optimistic-planck-3efc05`.
Read next: `CLAUDE.md` (constitution; model names there refer to the old Anthropic routing — substitute your own
models), `BACKTEST_PROTOCOL.md`, `docs/PREREGISTRATION.md`, `PROTOCOL_DEVIATIONS.md`, `PROJECT_STATUS.md`,
`TASK_QUEUE.json`, `PAUSE_CHECKPOINT.md`, `DATA_MANIFEST.md`.

## 1. North Star
Determine empirically whether future regulatory actions can be predicted from information public **before** the
decisive regulatory document — and how early, how accurately, from which precursor classes (Tier B official forward
material vs Tier C official soft signals vs stakeholder responses vs news), and whether policy **content** is
predictable. Gate 0 = a point-in-time historical backtest ending in a GO/NO-GO answer to six questions:
(1) predictable detection? (2) how early? (3) which precursors carry signal? (4) does Tier C add value over Tier B?
(5) is content predictable? (6) does it survive negative controls and leakage auditing?

## 2. Out of scope (do not build)
Stock prediction, options, valuation, Neo4j exposure maps, trading logic. Reason: they are downstream transformations
of a regulatory signal and cannot create predictive information; if Gate 0 finds no signal they are worthless. The
constitution requires the GO/NO-GO gate before any of them.

## 3. Frozen methodology
- `docs/PREREGISTRATION.md` — analysis plan + numeric GO/NO-GO bands, committed 2026-09-25 12:03 UTC (commit
  6841b87) before any forecast. Never edit it; record changes in `PROTOCOL_DEVIATIONS.md` (append-only, timestamped).
- Deviations already recorded: DEV-001 sampling_origin · DEV-002 "CLEAN"→"LATE" (no clean-holdout claim) · DEV-003
  entity/title-masked arm · DEV-004 calendar-forward Design C · DEV-005 primary arm B_PLUS_C, broad run = B_ONLY vs
  B_PLUS_C, rich ablations only on GOLD/informative subsets · DEV-006 smoke test first · DEV-007 stronger base rates ·
  FINDING-001/002 (see §9).
- Unit = regulatory thread anchored on a precursor document (NPRM, consultation paper, draft direction, exposure
  draft, draft guidance). Outcome = first official adopting publication (decisive date) or withdrawal / no action.
- Designs: **T** outcome-anchored cutoffs T-365…T-7 (pseudo-anchors for no-action threads drawn from matched
  positive gaps) → lead time only. **C** calendar-forward checkpoints (1 Jan/1 Jul 2019–2026 + 2026-06-26, 07-26,
  08-25), every visible unresolved thread ≤730 days old, horizons 7/30/60/90/180 d with censoring at 2026-09-24 →
  headline live-discovery metrics.
- Evaluation: Brier, log loss, AUROC/AUPRC, ECE, calibration slope, precision/recall at 0.5/0.7/0.8, lead time at
  precision ≥0.8, content-direction multiclass Brier/top-1, thread-clustered bootstrap CIs; comparators = best of
  4 no-LLM baselines with thread-grouped CV (workstream×elapsed base rate, workstream×process-stage transition,
  fixed heuristic, logistic feature model).

## 4. Architecture actually implemented (Python 3.11; numpy, pandas, scikit-learn, jsonschema, pytest)
| module | role |
|---|---|
| `schemas/*.schema.json` | thread, evidence (tiers B/C/S/D), outcome (sealed), forecast, audit — v1.x |
| `rpe/validate.py`, `rpe/lint.py` | schema + referential integrity + leakage lint per workstream |
| `rpe/build.py` | merges `data/raw/<ws>` → canonical stores; derives family, stratum (HIST/LATE), sampling_origin; merges US Unified-Agenda/OIRA items (OIRA receipt and conclusion split into separately dated items); applies audit patches; GOLD promotion from audits |
| `rpe/snapshots.py` | point-in-time snapshot index: designs T and C × arms (ALL, B_ONLY, C_ONLY, B_PLUS_C≡FULL_TRAJECTORY, B_C_STAKEHOLDERS, B_C_STAKEHOLDERS_PLUS_NEWS, LATEST_DOCUMENT_ONLY, TITLE_ONLY, MASKED_B_PLUS_C); labels per horizon with censoring |
| `rpe/packets.py` | renders blind packets + output stubs outside the repo; opaque ids; E1..En relabelling; hard guard against internal-id leakage; post-cutoff ISO-date scan; masked rendering; ≤1 snapshot per thread per batch; identical-packet aliasing |
| `rpe/ledger.py` | append-only, hash-chained forecast ledger; coherence repair log; `verify` detects tampering |
| `rpe/baselines.py` | cutoff-valid features + 4 pre-registered baselines (thread-grouped CV) |
| `rpe/evaluate.py` | all metrics/blocks → `reports/metrics.json`, `reports/METRICS.md` |
| `rpe/probe.py` | memorisation recall probe (no evidence) |
| `rpe/judge.py` | blinded content judge (scenario mechanism + parameter coverage; naive "as proposed" item mixed in) |
| `rpe/usage_audit.py` | Claude transcript model/usage audit (Anthropic-specific; not needed going forward) |
| `collectors/us_fr.py`, `collectors/reginfo.py` | Federal Register NPRM→final collector; Unified Agenda/OIRA collector |
| `docs/EXECUTOR_GUIDE.md`, `docs/AUDIT_GUIDE.md` | binding data-collection and leakage-audit protocols |
| `tests/` | 9 tests (fixtures synthetic) — all pass |

Folder map: `data/raw/<workstream>/` executor outputs (threads/evidence/outcomes.jsonl, sources.json, NOTES.md) ·
`data/threads|evidence|outcomes/` canonical (outcomes are SEALED — never show to forecasters) · `data/snapshots/index.jsonl`
· `data/forecasts/{ledger.jsonl, runs/, raw/, packets/}` · `data/audits/` (patches/, probe, judgements) ·
`data/derived/` (summaries, spend/usage logs, patch log) · `reports/` · `collectors/` · `rpe/` · `schemas/` · `docs/`.

## 5. Commands
```bash
pip install numpy pandas scikit-learn jsonschema pytest pdfminer.six beautifulsoup4 lxml requests
python3 -m pytest -q tests                        # 9 tests, ~5 min (bootstrap-heavy evaluator test)
python3 -m rpe.validate data/raw/<workstream>     # per-workstream validation (0 errors in all 7 today)
python3 -m rpe.build                              # canonical stores (~2 s)
python3 -m rpe.snapshots                          # snapshot index (deterministic given the canonical stores)
python3 -m rpe.packets make <RUN> --arms B_ONLY,B_PLUS_C --designs C --size 25   # packets+stubs in $RPE_FC_ROOT
python3 -m rpe.ledger ingest <RUN> --model <model-id>   # after forecaster wrote outbox JSON
python3 -m rpe.ledger verify
python3 -m rpe.probe make <RUN> --size 40 ; python3 -m rpe.probe score <RUN>
python3 -m rpe.judge make <RUN> --forecast-runs <R> --offsets T-90,T-30 ; python3 -m rpe.judge score <RUN>
python3 -m rpe.evaluate --primary-runs <R1,R2> --title-runs <R3> --masked-runs <R4> --ablation-runs <R5>
```
Set `RPE_FC_ROOT` to a scratch directory OUTSIDE the repo (default is a path in the old Claude container).
Forecaster contract: give the model the packet file text only (no tools, no browsing, no retrieval), require a
single JSON object exactly as specified in the packet header, write it to the outbox path, then ingest.

## 6. Dataset state (canonical build 2026-09-25 12:37 UTC)
| family | threads | positive | no-action | HIST | LATE | GOLD candidates | evidence B/C/S/D |
|---|---|---|---|---|---|---|---|
| IN-IRDAI | 19 | 13 | 6 | 19 | 0 | 0 | 22/0/0/4 |
| IN-RBI | 27 | 16 | 11 | 21 | 6 | 15 | 27/12/0/20 |
| IN-SEBI | 44 | 33 | 11 | 29 | 15 | 8 | 49/0/0/74 |
| IN-TRAI | 10 | 9 | 1 | 10 | 0 | 4 | 19/0/0/0 |
| US-FDA | 55 | 23 | 32 | 30 | 25 | 25 | 63/0/21/0 |
| US-FR | 179 | 111 | 68 | 119 | 60 | 60 | 1596/0/158/0 |
| **TOTAL** | **334** | **205** | **129 (39%)** | 228 | 106 | 112 | 1776/12/179/98 |
RAPID usable = 334 (1 excluded for low label confidence). GOLD audited = 0 (audit not run). sampling_origin =
precursor_population for all 334. Snapshots: design C 801, design T 2,286 (B_PLUS_C arm). Forecasts: 40 unique
(60 ledger records incl. aliases), smoke test only (run SMOKE1) — excluded from headline metrics.
Incomplete collectors: in_dgtr (0 threads written), in_trai (10 of ~28 planned), in_irdai (19 H; R frame not done),
in_sebi_h (14 of 25), in_rbi (27 of ~32), in_sebi_r (30, NOTES/sources not written), us_baserates (not produced).

## 7. Source availability (verified from the container 2026-09-25)
| source | status |
|---|---|
| Federal Register API, govinfo.gov PDFs | reachable; FR official dates are the strongest point-in-time anchor. federalregister.gov HTML full-text pages bot-gated → use govinfo |
| reginfo.gov (Unified Agenda XML, OIRA EO 12866 XML) | reachable; Fall-2024 agenda edition never FR-published (date confidence low) |
| regulations.gov API | DEMO_KEY only, heavily rate-limited; comment counts taken from FR API mirror (current counts, not point-in-time) |
| fda.gov | reachable with browser UA, but guidance-search DB is WAF-blocked; CDER/CDRH guidance agendas unverifiable (revised PDFs) |
| sec.gov | 403 without declared-identity User-Agent → SEC rules via FR API |
| sebi.gov.in, rbi.org.in, irdai.gov.in, trai.gov.in, dgtr.gov.in | reachable |
| news.google.com RSS (with after:/before: operators) | reachable; used for Tier D headlines+dates |
| web.archive.org | BLOCKED (tunnel reset) → no Wayback verification |
| egazette.gov.in, cbic.gov.in, nppaindia.nic.in, (cdsco.gov.in partially) | BLOCKED → CDSCO/NPPA dropped; DGTR outcomes need other sources |

## 8. Leakage controls already implemented
Precursor-population sampling (census/systematic) with `sampling_origin`; outcome store sealed and never rendered;
evidence filtered by available_date ≤ cutoff; lint errors for evidence on/after decisive or withdrawal date
(auto-dropped after audit patches); retrospective-wording and future-date lint warnings; neutral titles; opaque
snapshot ids; E1..En relabelling (no gaps revealing later items); hard guard raising if any thread/evidence id
appears in a packet; post-cutoff ISO-date scan logged per run; OIRA completion split from receipt; comment-count
items rendered without retrieval dates; one snapshot per thread per forecaster context; arm names never shown;
forecasters told not to use post-cutoff memory and to self-report `recognised_outcome`; append-only hash-chained
ledger; TITLE_ONLY arm; MASKED_B_PLUS_C arm; recall probe; LATE stratum; audit-patch mechanism with GOLD
promotion only via audit (`docs/AUDIT_GUIDE.md`).

## 9. Unresolved methodological concerns (address before scaling)
1. **FINDING-001 macro-political hindsight (smoke test):** at cutoffs before the Nov-2024 US election the forecaster
   reasoned from the Jan-2025 change of administration. Evidence was clean; the model's world knowledge leaked.
   Needed: explicit packet rule forbidding use of post-cutoff events (elections, leadership changes, court rulings,
   shutdowns); an LLM or rule-based audit of forecast rationales for post-cutoff facts; report results with flagged
   snapshots excluded. Record as DEV-008.
2. **FINDING-002 snapshot instability:** pseudo-anchors for no-action threads depend on the positive-gap pool, and
   collectors rebuilt data after SMOKE1, so 36 of 60 SMOKE1 ledger records no longer match the current index (the
   SMOKE1-era rows are preserved in `data/forecasts/runs/SMOKE1_index_rows.jsonl`). Needed: freeze and commit the
   snapshot index (and pseudo-anchor table) before any scaled run; never rebuild under a live run.
3. **Knowledge cutoff of the NEW forecaster:** the LATE stratum (resolution ≥ 2026-07-01) was defined against the
   old forecaster's stated June-2026 cutoff. GPT-6 Astra's cutoff will differ → reset `LATE_BOUNDARY` in
   `rpe/build.py` and `LATE_DATES`/`C_CHECKPOINTS` in `rpe/snapshots.py` to after the new model's documented
   cutoff (log as a deviation). If the new model's cutoff is after 2026-09, no post-cutoff stratum exists in the
   current data; memorisation must then rest on the probe, TITLE_ONLY and masking controls.
4. **Sampling bias:** SEBI-H has 0 no-action threads among 14 (suspicious for a systematic sample of consultation
   papers — audit the frame/skips); TRAI 1 of 10; US-FR LATE frame is 88% unresolved (few LATE positives: 7);
   FDA LATE has 0 positives. Positive/negative mix differs strongly by family → always report per family and use
   within-family baselines. Primary results must use `sampling_origin == precursor_population` only.
5. **Tier C scarcity:** only 12 tier-C items (all RBI). B-vs-B+C (question 4) is currently underpowered. Targeted
   tier-C collection (SEBI/RBI/IRDAI speeches, board-meeting statements, RBI Statements on Developmental and
   Regulatory Policies; US agency press releases/testimony for a GOLD subset) is required before answering Q4.
6. **Content labels:** US-FR content_direction is heuristic (100 of 205 positives "action_mixed");
   `content_label_confidence` separates this from the action label. Run a content-labelling pass before content
   metrics. US news (Tier D) was never collected → news ablation is India-only.
7. **Executor-authored text** (claims/summaries written by agents who knew the outcome): lint passes, but the Opus
   leakage audit (`docs/AUDIT_GUIDE.md`) has NOT been run → GOLD = 0.
8. Comment counts are current, not point-in-time; Fall-2024 agenda date low-confidence; Design C monitors a thread
   for ≤730 days (cost cap).

## 10. Why `sampling_origin` and Design C matter
- Sampling from final outcomes (backfill) selects threads that succeeded and inflates apparent predictability;
  `sampling_origin` lets primary results exclude any outcome-selected thread.
- Design T only asks "was the eventual action foreseeable before it happened" for threads with known outcomes; it
  cannot measure live discovery. Design C asks, at fixed historical dates, which currently visible open proposals will
  progress within 30/60/90/180 days — the deployment question. Headline metrics must come from Design C; Design T is
  for lead time only.
- The **entity/title-masked test** (`MASKED_B_PLUS_C` vs `B_PLUS_C`, same model, GOLD sample) is required: a large
  accuracy drop under masking indicates reliance on memorised identity rather than evidence.

## 11. Exact next execution sequence
1. Clone/check out the branch; `pip install …`; `python3 -m pytest -q tests` (expect 9 passed).
2. Decide the forecaster model and document its knowledge cutoff; apply concern 3 (reset LATE boundary) and
   concern 1 (packet rule, DEV-008); log both in `PROTOCOL_DEVIATIONS.md` with UTC timestamps.
3. `python3 -m rpe.build && python3 -m rpe.snapshots`; commit `data/snapshots/index.jsonl` as the FROZEN index
   (concern 2). Do not rebuild during forecasting; later collector additions go in a new, separately frozen index.
4. Wire the forecaster: for each batch in `data/forecasts/runs/<RUN>.json`, send the packet text as the only input
   (no tools), write the returned JSON to the batch's output path, `python3 -m rpe.ledger ingest <RUN> --model <id>`.
5. Re-run a 10-thread smoke test with the new model (5 progressing / 5 no-action; include RBI threads that have
   tier C so B vs B+C is non-trivial); inspect packets and rationales manually.
6. Recall probe on all threads (`rpe.probe`) → memorisation rate by family.
7. Broad run: B_ONLY + B_PLUS_C on all design-C snapshots (801) and design-T {T-180, T-90, T-30}.
8. TITLE_ONLY on design C; leakage audit of GOLD candidates → GOLD set; MASKED_B_PLUS_C + stakeholder/news/
   latest-only arms on GOLD/informative subsets only.
9. `python3 -m rpe.evaluate …` → `reports/METRICS.md`; content judge on positives; GO/NO-GO against the frozen bands.
10. In parallel (cheap model): finish in_dgtr, in_trai, in_irdai-R, in_sebi_h, in_rbi; targeted tier-C collection;
    external US base-rate table (spec in PROJECT_STATUS.md); content-labelling pass for US-FR.

## 12. First empirical milestone
One table (`reports/METRICS.md`) giving, on precursor-population threads: Design-C action AUROC/Brier/calibration
vs the best stage-transition/base-rate baseline (HIST, LATE-if-valid, US, India); timing calibration by horizon;
content-direction skill vs base rate; Design-T lead time at precision ≥0.8; B vs B+C lift (where tier C exists);
negative controls (no-action threads, TITLE_ONLY, masked, probe-recalled exclusion); leakage-audit findings.
