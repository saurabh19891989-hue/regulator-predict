# Core60 gate readiness — 2026-10-04

**Scope:** Read-only analysis of the released `ASTRA_CORE60` and `ASTRA_CAL60` manifests, their selected frozen-index rows, the complete SEBI-R30/FDA-H30 cohort, canonical threads/outcomes, preregistration/deviations, evaluator/baselines, and packet-release audit. Counts below are input and label counts, **not forecast results**. This review did not inspect or alter the running inference, run tests, change data, or calculate predictive metrics.

## Answer

The released cohort has valid, matched Design-C 90-day HIST and LATE rows for the numeric G1 action comparison, along with same-model `TITLE_ONLY` rows at every selected cutoff. It also has Design-T rows needed to calculate the frozen lead-time statistic. If all released outputs pass receipt, schema, leakage and ledger checks, scoring can proceed on these frozen inputs. G1 can be **assessed numerically**, but its HIST evidence is five 90-day events in five FDA matters and its LATE evidence is nine positive snapshots in four SEBI matters. HIST/LATE comparisons are therefore entangled with regulator and calendar period.

The experiment cannot establish a complete GO or CONDITIONAL GO on this cohort: there are zero GOLD matters, zero Tier C records, no independent B/C/ALL forecasts, and no supplied blinded mechanism judgments or audited-snapshot contamination denominator. G5 requires audit/exclusion evidence beyond the evaluator's numeric slices. These missing components should remain **unassessed**, never entered as zero lift or counted as passes.

## Frozen input coverage

Both manifests bind the same canonical/index hashes and select only precursor-population RAPID matters. The release audit found all packets and aliases complete. CORE has 20 T batches, 380 distinct forecast requests plus 380 aliases (760 logical arm rows: 190 B-family and 190 TITLE_ONLY direct requests). CAL has 18 C batches, 298 distinct requests plus 298 aliases (596 logical arm rows: 149 B-family and 149 TITLE_ONLY direct requests). Both contain `TITLE_ONLY` and the identical-input B-family forecast, with `ALL`, `B_ONLY`, and `B_PLUS_C` logically aliased. CAL covers 45 of 60 matters; the other 15 have no eligible frozen calendar checkpoint, rather than an omitted packet. Across the selected matters there are 42 actions and 18 controls, all with at least medium outcome-label confidence. Of 61 retained distinct evidence records, all are Tier B.

The table counts **B_PLUS_C snapshots with an uncensored label**. “Positive/negative” describes the stated horizon at the cutoff, not the matter's final action/control status. TITLE_ONLY has the same selected cutoff and label counts.

| Design / horizon | Regulator and stratum | Selected matters | Eligible snapshots | Scored | Positive | Negative |
|---|---|---:|---:|---:|---:|---:|
| C / 90d | SEBI HIST | 0 | 0 | 0 | 0 | 0 |
| C / 90d | SEBI LATE | 15 | 45 | 23 | 9 | 14 |
| C / 90d | FDA HIST | 29 | 100 | 100 | 5 | 95 |
| C / 90d | FDA LATE | 1 | 4 | 4 | 0 | 4 |
| **C / 90d total** | **HIST 100; LATE 27** | **45** | **149** | **127** | **14** | **113** |
| T / 180d | SEBI HIST | 7 | 13 | 13 | 13 | 0 |
| T / 180d | SEBI LATE | 23 | 57 | 38 | 32 | 6 |
| T / 180d | FDA HIST | 29 | 116 | 116 | 88 | 28 |
| T / 180d | FDA LATE | 1 | 4 | 4 | 4 | 0 |
| **T / 180d total** | **HIST 129; LATE 42 scored** | **60** | **190** | **171** | **137** | **34** |

C90 HIST's five positives occur in five distinct FDA matters. C90 LATE's nine positives occur in four distinct SEBI matters. The 90-day pooled US and India blocks each retain positive and negative labels, so their AUROCs are mathematically estimable before recognition exclusions. A 90-day HIST SEBI estimate and a 90-day LATE FDA AUROC are structurally unavailable. The LATE C90 FDA rows contribute only four negative labels from one matter. Thread-clustered intervals and explicit denominators are essential; the repeated checkpoints do not create 127 independent matters.

Other C horizons have scorable positive/negative variation: 30d 6/143 over 149 rows, 60d 12/126 over 138, and 180d 23/94 over 117. Pooled C/T 30/90/180 timing labels likewise have both classes. This makes G2 calibration calculations possible, although slope can legitimately be undefined under separation or output-dependent exclusions. Later C horizons are censored at the fixed 2026-09-24 observation boundary.

## Gate-by-gate interpretation

**G1 — action signal.** `rpe/evaluate.py` uses C90 HIST Brier skill versus the best selected-cohort, thread-grouped baseline, its 90% CI excluding zero, a matched same-model HIST B_PLUS_C-minus-TITLE_ONLY Brier CI excluding zero in the favorable direction, and C90 LATE AUROC ≥0.70 plus nonnegative Brier skill versus its best baseline. All required labels and matched input rows exist. The `TITLE_ONLY` forecast is distinct from the evidence packet; it is not an alias of B_PLUS_C. At evaluation, include both run names in `--primary-runs` **and** `--title-runs`, because the title comparison is produced only when `--title-runs` is provided. No score can be asserted until outputs are validated and ingested. HIST is FDA-only in C90 and LATE positives are SEBI-only, so even a passing G1 supports a narrow, mixed-period RAPID conclusion, not a regulator-balanced replication or memory-free result. The 90-day LATE positive count is four matters; AUROC and CI may be unstable.

**G2 — timing.** The evaluator can calculate pooled C/T 30/90/180 ECE and calibration slope against the frozen limits. Report pooled design mix and any undefined slope. FDA action dates are the first verified public finalization notices, not proven first FDA PDF postings, so FDA timing and derived lead claims remain conditional.

**G3 — content.** Among 42 action matters, three content-direction labels are low confidence and excluded by the evaluator. Of the other 39, 37 are `as_proposed`, one `mixed`, and one `tightened`; the matter-level majority rate is 37/39 = 94.9%. Thus the frozen “majority +10 percentage points” top-1 route is mathematically impossible on this label set, while multiclass Brier skill is still assessable. Blinded mechanism top-1 accuracy on GOLD/LATE positives is not assessable from the supplied data: no GOLD matters or judge output exists. No exact FDA parameter claim should be inferred from notice-level sources; SEBI R-0026's low-confidence content disposition requires care.

**G4 — lead time.** Forty-two positive matters have a scored T180 row; ten of eighteen controls have any scored T180 row, with the other eight losing their relevant horizon to censoring. Among positive matters, the earliest *available* selected T offset is 180 days for 25, 90 for four, 30 for twelve, and 7 for one. The frozen statistic evaluates θ ∈ {0.5, 0.7, 0.8}, precision only over selected T rows with k≤180 and a valid 180-day label, and median first crossing among positives at the smallest θ with precision ≥0.80 (and at least five flagged rows in the implementation). It is computable after outputs arrive. The T precision denominator is already 137/171 = **80.12% positive**. A constant forecast above θ for every T row would clear 0.80 precision without discrimination, and because 25/42 positives have T−180, would yield a 180-day median first crossing. Therefore a numeric G4 pass in this cohort alone is weak evidence of useful advance warning; state the T base rate and compare with calendar-forward results. This does not change the frozen scoring rule.

**G5 — robustness.** The evaluator emits US/India C90 AUROCs, HIST–LATE AUROC gap, and self-recognition-excluded C/T slices. The required audited-snapshot contamination numerator/denominator and full “conclusion unchanged after excluding contaminated and self-recognised” analysis are not supplied by the index or manifests. Canonical build excludes contaminated threads, which is not a measured contamination rate for these forecast snapshots. No clean GOLD sample exists. Output rationale audit and recognition flags remain necessary before drawing a robustness conclusion. B_ONLY/B_PLUS_C/ALL aliases cannot measure Tier C, stakeholder or news incremental value; absence of those classes is missing identification, not zero measured lift.

## Decision boundary after inference

- If all G1 inputs are valid and the frozen G1 conjunction **fails**, report **NO-GO under the preregistered decision rule** for this audited RAPID cohort, identifying which condition failed and its CI/denominator. Do not call a sparse-CI failure proof that no regulatory signal exists in any population. A G1 failure is sufficient for the formal NO-GO regardless of G5's missing inputs; it is not a reason to change cutoffs, thresholds, sources, or architecture after seeing results.
- If a required G1 input is **missing or undefined** (for example failed forecast validation, no matched title forecasts, or no class variation after required exclusions), mark G1 and the overall gate **UNASSESSED**. Missing is not a failed numeric band and cannot yield GO, CONDITIONAL GO, or an empirical NO-GO.
- If G1 passes, report the numeric pass and the available G2/G4 results, but keep the overall gate **UNASSESSED** while G5's required audit inputs remain missing. G3 and evidence-class lift also remain unassessed. Do not use the evaluator's available numeric checks as a complete decision verdict.

The next decision-relevant operation is bounded output receipt, schema/coherence and rationale audit, ledger ingestion, then the frozen evaluator invocation with title comparisons and explicit missing-gate reporting. This review identifies no need for further infrastructure or changes to the released packets or source freeze.
