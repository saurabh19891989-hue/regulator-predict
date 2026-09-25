# PREREGISTRATION.md — Gate 0 analysis plan and frozen GO/NO-GO bands

**Frozen:** 2026-09-25, before any forecast was generated and before any outcome was inspected by the Director.
Any later change must be appended as a dated amendment below, with reason; the original text is never edited.

## 1. Datasets and strata
- **RAPID** (quality label): threads that pass `rpe.validate` with no errors, outcome label confidence ≥ medium.
- **GOLD** (quality label): GOLD_CANDIDATE threads that additionally pass an independent Opus leakage audit
  (verdict `clean` or `minor_issue_fixed`) with all evidence dates verified from primary documents.
- **HIST** (temporal stratum): decisive action / resolution before 2026-07-01 → outcome may be memorised by the
  forecaster model (knowledge cutoff June 2026).
- **CLEAN** (temporal stratum): outcome not resolved before 2026-07-01 (decisive action/withdrawal on or after
  2026-07-01, or unresolved at censor date 2026-09-25). Outcome cannot be in the forecaster's training data.
RAPID/GOLD and HIST/CLEAN are always reported separately; any pooled number is labelled as pooled.

## 2. Snapshot designs
**Design T (outcome-anchored, protocol cutoffs; used for lead time).** Anchor date T = decisive_date for
positives. For no-action threads a pseudo-anchor T* = anchor_date + g, with g drawn (seeded, deterministic) from
the empirical distribution of (decisive_date − anchor_date) of positives of the same workstream family (pooled
across families when a family has < 5 positives), truncated so that T* ≤ min(withdrawal_date − 1, censor_date).
Cutoffs c = T − k for k ∈ {365, 270, 180, 120, 90, 60, 30, 14, 7}. k = 365 and 270 are an extension to the
protocol: they add "positive but not within 180 days" snapshots, without which a T-anchored design compares only
imminent actions against never-actions and inflates discrimination. A snapshot is valid only if c ≥ anchor_date
(the neutral title is derived from the anchor) and at least one evidence item is dated ≤ c.
**Design K (calendar, prospective; CLEAN only).** Fixed cutoffs c ∈ {2026-06-26, 2026-07-26, 2026-08-25} with
horizons to censor date 2026-09-24 of 90, 60 and 30 days. Every CLEAN thread with anchor ≤ c and unresolved at c
gets a snapshot. This mirrors live monitoring and involves no outcome-dependent cutoff placement.

**Labels.** For cutoff c and horizon h: y = 1 if decisive_date ∈ (c, c+h]; y = 0 if no decisive action in
(c, c+h] and c+h ≤ censor date; otherwise censored (excluded for that horizon).

## 3. Forecasting arms
Primary forecaster: Opus 5.5 (isolated agent: Read+Edit only; no web/search/shell; one snapshot per thread per
agent context). Arm `ALL` = every evidence class available by c (B+C+S+D).
Ablation forecaster: Sonnet 5, all arms run by the same model on the same snapshots:
`B_ONLY`, `C_ONLY`, `B_PLUS_C` (= `FULL_TRAJECTORY`: all official items), `B_C_STAKEHOLDERS`,
`B_C_STAKEHOLDERS_PLUS_NEWS`, `LATEST_DOCUMENT_ONLY` (single most recent official item), and control
`TITLE_ONLY` (neutral title + regulator + cutoff date, no documents). An arm whose added class is absent at c is
marked unavailable (identical packets are deduplicated and scored once).
Memorisation controls: (i) CLEAN stratum; (ii) `TITLE_ONLY`; (iii) a separate recall probe asking the forecaster
model whether it remembers each matter's outcome; (iv) forecaster self-report `recognised_outcome`.

## 4. Baselines (no LLM), all computed with thread-grouped cross-validation (no thread in its own training fold)
1. Workstream base rate at matched elapsed-time bucket (days since anchor).
2. Stage-transition baseline: P(y | workstream, visible process stage at c).
3. Recency/deadline heuristic (fixed rules written before results; see `rpe/baselines.py`).
4. Logistic-regression feature model on structured, cutoff-valid features (counts per tier, days since anchor /
   latest item, comment deadline passed, OIRA final-stage review received, agenda-projected final date within
   horizon, comment volume, workstream).
The **best** baseline on each metric is the comparator ("meaningful baseline").

## 5. Metrics
Action: Brier, log loss, AUROC, AUPRC, calibration (reliability bins, ECE, slope/intercept), precision/recall at
p ≥ 0.5 / 0.7 / 0.8. Timing: per-horizon Brier/ECE for 7/30/60/90/180d cumulative probabilities.
Content (positives only): multi-class Brier and top-1 accuracy of content_direction vs base-rate distribution;
scenario mechanism accuracy and parameter-range coverage by blinded LLM judge on GOLD/CLEAN positives.
Lead time: for each positive, earliest Design-T cutoff with p_180 ≥ θ (θ = 0.5, 0.7, 0.8); precision at θ over
all Design-T snapshots at k ≤ 180; lead time at the smallest θ achieving precision ≥ 0.80.
Ablation: paired ΔBrier / Δlog loss per snapshot between arms, thread-clustered bootstrap 90% CI (2,000 reps).
Uncertainty: all CIs thread-clustered bootstrap.

## 6. Frozen GO / NO-GO bands (decided before results)
**G1 Action signal.** On HIST: ALL-arm Brier skill vs best baseline ≥ +0.05, 90% CI excluding 0, AND
ALL beats TITLE_ONLY (same model) with CI excluding 0. On CLEAN: AUROC ≥ 0.70 and Brier skill vs best baseline
≥ 0 (point estimate; CI reported — CLEAN is expected to be underpowered).
**G2 Timing usefulness.** 30/90/180d buckets: ECE ≤ 0.10 and calibration slope in [0.6, 1.4] (pooled).
**G3 Content.** content_direction top-1 accuracy ≥ majority-class rate + 10 pp OR multi-class Brier skill vs
base-rate distribution ≥ 0.05; judged mechanism top-1 accuracy ≥ 60% on GOLD/CLEAN positives.
**G4 Lead time.** Median lead time ≥ 30 days at precision ≥ 0.80 ("useful"); ≥ 60 days = "strong".
**G5 Robustness.** Leakage-audit contamination ≤ 10% of audited snapshots and G1 conclusion unchanged after
excluding contaminated and self-recognised snapshots; CLEAN AUROC not more than 0.10 below HIST AUROC; signal
present (AUROC ≥ 0.65) in both the US and India families.
**Decision rule.** GO = G1 ∧ G4 ∧ G5. CONDITIONAL GO = G1 ∧ G5 with G2/G3/G4 partially failing (report which).
NO-GO = G1 or G5 fails. Sensitivity of the verdict to ±0.05 around each numeric band is reported.

## 7. Exclusions (fixed in advance)
Snapshots flagged `contaminated_exclude` by audit; threads with outcome label_confidence low (reported
separately); forecasts failing schema/coherence checks after one re-run.

## Amendments
(none)
