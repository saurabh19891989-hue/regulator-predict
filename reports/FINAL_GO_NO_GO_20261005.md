# Regulatory prediction: final Gate 0 decision

**Decision: NO-GO for the current forecasting approach.** Completed 2026-10-05.

We wanted to establish whether official early signals predict regulatory action, timing and content better
than strong process rules, with useful advance warning. The current study does not meet the frozen acceptance
criteria. Stop at this research gate; these results do not justify a trading system or production alert engine.
This is a decision about this model and audited cohort, not proof that regulation is universally unpredictable.

## What was completed

- Frozen research dataset: 327 matters, 1,785 evidence records, 99 source-audited RAPID matters; zero GOLD.
- Scaled study: all 30 SEBI-R and 30 FDA-H matters source-audited. There are 42 action and 18 control matters.
- 38 fresh, tool-disabled Astra high calls produced 678 distinct forecasts, including title-only controls.
  Identical-input arms add 678 aliases, not independent predictions. Primary ALL has 339 snapshots.
- All 678 distinct outputs independently reviewed; zero visible future-fact contamination, 64 recognition
  disclosures. Hidden model memory and historical source-version immutability remain unverifiable.
- All execution hashes reconcile; no coherence repairs. Ledger verifies 1,464 rows: 1,356 scaled logical rows
  plus 108 old diagnostic rows. Old diagnostics and the legacy recall probe are excluded from final scoring.
- Four process baselines use thread-grouped validation within the selected cohort. DEV-016 fits logistic
  preprocessing inside each training fold. Confidence intervals use 2,000 thread-clustered bootstrap draws.
- Fixed observation censor: 2026-09-24; model temporal boundary: 2026-04-30. Source and forecast hashes unchanged.

## Results that decide the gate

Brier measures probability error: lower is better. Brier skill measures improvement over the strongest baseline.
AUROC measures ranking: 0.5 is chance ranking, 1.0 is perfect. All displayed intervals are 90% intervals.

| Check | Measured result | Frozen requirement | Outcome |
|---|---|---|---|
| G1: historical calendar-forward action | Brier skill +0.320 [0.252, 0.407], 100 snapshots / 29 matters | ≥+0.05, interval above zero | This component passes |
| G1: historical evidence versus titles | ΔBrier evidence−title +0.000210 [−0.004738, +0.004780] | Evidence better, interval below zero | Fails |
| G1: newer calendar-forward action | AUROC 0.577 [0.279, 0.843]; skill +0.043 [−0.507, +0.236], 27 snapshots / 15 matters | AUROC ≥0.70 and skill ≥0 | Ranking component fails |
| G2: pooled timing | ECE 0.184 / 0.192 / 0.188 at 30 / 90 / 180 days; slopes 0.982 / 1.137 / 1.460 | Every ECE ≤0.10 and slope 0.6–1.4 | Fails |
| G3: content direction | 96% accuracy equals 96% majority baseline; multiclass skill −1.644 [−13.906, −0.513] | ≥10 percentage points over majority or skill ≥0.05 | Direction fails; mechanism unassessed |
| G4: lead time | At p≥0.5: precision 87.8%, 19/42 positive matters detected; median across all 42 = 0 days | Median ≥30 days at precision ≥80% | Fails |
| G5: temporal stability | Historical AUROC 0.887 versus newer 0.577: decline 0.310 | Decline ≤0.10 | Fails |
| G5: both regions | FDA/US AUROC 0.864; SEBI/India 0.456 | Each ≥0.65 | India fails |

The frozen decision rule says **NO-GO when G1 or G5 fails**. Both fail. Missing GOLD/mechanism work cannot turn
these observed failures into a GO. The evaluator's generic `UNASSESSED` message identifies absent external audit
inputs; this report supplies the completed audit and adjudicates the frozen rule without changing its bands.

The verdict persists with ±0.05 changes to the numeric thresholds: newer AUROC remains below even 0.65,
India below even 0.60, and the historical/newer decline above even 0.15. Evidence-versus-title uncertainty
still includes no improvement. Excluding self-recognised forecasts also leaves G1 failed: historical title
ΔBrier −0.000912 [−0.006804, +0.003981]; newer results unchanged.

## How early were warnings available?

At the selected frozen threshold p≥0.5, 49 outcome-anchored snapshots were flagged: 43 true and 6 false.
Snapshot recall was 31.4%. First warning per positive matter:

| First available warning | Positive matters |
|---|---:|
| No qualifying warning | 23 |
| 7 days | 1 |
| 30 days | 12 |
| 90 days | 4 |
| 180 days | 2 |

The 19 detected matters have a 30-day median; using only those detected would hide the 23 misses.
The gate median includes all 42, with misses represented as zero. Zero means no threshold crossing in available
snapshots, not a same-day warning. At thresholds 0.7 and 0.8, only 17 and 9 matters were detected; both gate
medians remain zero. These are retrospective, outcome-anchored measurements, not live prospective warning evidence.
The 180-day labelled T sample is 80.1% positive; precision alone is therefore an easy, inadequate success criterion.

## Answers to the research questions

| Question | Evidence-based answer |
|---|---|
| 1. Can action be predicted above strong process baselines? | Partially in this historical sample. Pooled C90 skill +0.191 [0.039, 0.289], but the required title-control and newer-sample tests fail. No validated deployable signal. |
| 2. How early? | 19/42 positive matters detected at p≥0.5; detected-only median 30 days, all-matter median zero. Lead gate fails. |
| 3. Which precursors carry value? | Official Tier B evidence is the only supplied class. Calendar evidence-versus-title improvement is not established; individual class attribution is unmeasured. |
| 4. How much does Tier C add? | Unmeasured: no retained Tier C in this cohort. B, B+C and ALL have identical inputs; an alias difference is not an estimate of Tier C value. |
| 5. Full trajectory versus latest document? | Unmeasured: no informative independent trajectory/latest-document comparison. |
| 6. Can policy content be predicted? | Direction accuracy matches the majority baseline and probability scores are worse. Mechanism accuracy has no blinded GOLD/LATE judgment. No demonstrated incremental content value. |
| 7. Useful parameter ranges? | Unassessed. Bounded audits found unsupported conditional numerical guesses; these are preserved, not presented as grounded predictions or validated range coverage. |
| 8. Which regulators work best? | FDA historical calendar ranking looks stronger than SEBI's newer sample, but regulator and temporal strata are confounded. No reliable regulator league table or general claim. |
| 9. Does it survive stalled/no-action controls? | Controls are included in action scoring: 18 matters, with horizon censoring. No-action searches are medium-confidence bounded absence evidence. Their inclusion does not produce an overall passing gate. |
| 10. Leakage, memory and masking? | Visible-output audit passes 678/678; excluding recognition preserves failure. Hidden memory cannot be excluded. Earlier eight-output masking smoke is diagnostic and excluded; full scaled masking/recall robustness unassessed. |
| 11. GOLD survival? | Unmeasured: zero GOLD. Source audits of RAPID are not GOLD certification. |
| 12. Prospective discovery? | Calendar-forward historical simulation exists, not live prospective validation. Newer C90 AUROC 0.577 fails the band; after-cutoff C30 AUROC 0.608 with skill −0.005 is inconclusive. No demonstrated live discovery capability. |

## Limits on interpretation

The historical C90 block has only five positive snapshots; newer C90 has nine positive snapshots across only
four positive SEBI matters. Its intervals are wide. Historical C90 is FDA; newer C90 is predominantly SEBI,
so a temporal decline cannot be uniquely attributed to memory, geography or process. FDA dates represent
verified public finalization notices and are not established as the earliest FDA PDF upload. Source pages and
PDFs are not proven immutable historical versions. Sampling-origin tags do not prove population completeness.
The study supports the declared operational NO-GO, with limited generality.

Outcome-anchored T180 probability error was also worse than its strongest baseline: Brier 0.292 versus 0.217,
skill −0.349 [−0.657, −0.095]. Stronger ranking on that retrospective design did not establish calibrated warnings.
Pooled metrics must not be presented as uncontaminated live performance.

## What should be built next?

No production prediction, stock-selection or trading architecture is justified by this result. Preserve this
completed experiment and stop at the gate. If a separate research programme is later authorised, the most
informative next output would be a genuinely prospective, timestamped Tier B/C forecast ledger with both
regulators represented in the same temporal period, strong baselines and fixed calibration. That is a proposal,
not work started after this NO-GO.

## Daily data collection

The running daily collector belongs to the separate NNML **market-data** programme. On October5 its capture
closed successfully at15:31IST with24,167,141 updates. At15:36IST, upload was scheduled15:50IST and pending;
the most recent previously verified completed Drive copy wasOctober2 (3,826 objects,344.4MiB).
Follow-up at15:50IST confirms the automatic post-close upload started on schedule; a completed October5
Drive receipt is not yet present. October2 remains the latest verified completed copy. Today's local
CAPTURE_RESULT also confirms zero slot/decode errors. See `docs/COLLECTION_STATUS_20261004.md` for evidence. No daily regulatory collection or regulatory
Drive-upload automation was found; the frozen regulatory dataset is saved locally and in Git.

## Reproducible evidence

- `reports/metrics.json`, `reports/METRICS.md`: full unedited evaluator output.
- `reports/FINAL_DECISION_20261005.json`: adjudication, metric hash and lead distributions.
- `reports/FINAL_GATE_REVIEW_20261005.md`: independent decision review when completed.
- `data/audits/scaled60_full_acceptance_20261005.json`: exact audit scope and report hashes.
- `data/audits/scaled60_execution_preflight_20261005.json`: all batch and execution hashes and receipt usage.
- `data/snapshots/freeze_20261004.json`: canonical data freeze.
- `docs/PREREGISTRATION.md`, `PROTOCOL_DEVIATIONS.md`: original bands and declared method repairs.

Scoring: `python -m rpe.evaluate --primary-runs ASTRA_CORE60,ASTRA_CAL60 --title-runs ASTRA_CORE60,ASTRA_CAL60 --primary-arm ALL --probe [empty]`.
The evaluator implementation is commit79f98d1, including DEV-016. No result-driven threshold tuning was performed.
