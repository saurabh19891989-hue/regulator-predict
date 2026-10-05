# Independent final gate review — 2026-10-05

**Formal verdict: NO-GO for the frozen SEBI-R30/FDA-H30 RAPID cohort and its scored forecast approach.** The preregistered rule says NO-GO if **G1 or G5 fails**. Both fail measurable, required conditions. Missing GOLD mechanism judgments and incomplete assurance about hidden memorisation cannot turn those observed failures into an `UNASSESSED` overall verdict. This is a cohort and method verdict, not a claim that regulatory actions are inherently unpredictable.

## Gate evidence

| Gate | Frozen requirement and observed result | Adjudication |
|---|---|---|
| **G1 action** | Design-C 90-day HIST Brier skill versus the best baseline is **+0.320**, 90% thread-clustered CI **[+0.252,+0.407]**, passing that component. Matched HIST `ALL − TITLE_ONLY` Brier is **+0.000210** (positive means ALL is worse), CI **[−0.004738,+0.004780]**: evidence superiority is not established. LATE AUROC is **0.577**, below **0.70**; LATE Brier skill is **+0.043**, meeting its point-estimate condition. | **Fail** |
| **G5 robustness** | HIST minus LATE C90 AUROC gap is **0.310**, above **0.10**. US C90 AUROC is **0.864**, but India is **0.456**, below **0.65**. The output audit covers **678 distinct forecasts** across 38 batches and reports **0 observable contamination** and **64 self-recognition flags**. Excluding self-recognised forecasts leaves the HIST title Brier difference at **−0.000912**, CI **[−0.006804,+0.003981]**, so the G1 title requirement still fails. | **Fail on two numeric conditions**, irrespective of the audit's residual limits |
| **G4 lead** | At the smallest qualifying threshold, θ=0.5, precision is **0.878** on 49 flagged T snapshots, but the frozen median lead over **all 42 positive matters** is **0 days**, below **30**. Only **19/42** matters cross the threshold at an available positive offset. | **Fail** |
| **G2 timing** | Pooled C/T ECEs for 30/90/180 days are **0.184/0.192/0.188**, each above **0.10**. The 180-day slope is **1.460**, above **1.40**. | **Fail** |
| **G3 content** | Direction top-1 accuracy is **96%**, exactly the **96% snapshot majority-class rate**, with multiclass Brier skill **−1.644** versus the base-rate distribution. Blinded mechanism accuracy on GOLD/LATE positives is unavailable; the cohort has **zero GOLD** matters. | Direction conditions **fail**; full G3 **unassessed** |

The evaluator's overall `UNASSESSED` label reflects its missing-input policy. It does not implement the frozen decision rule's sufficient NO-GO condition when an assessable G1 or G5 fails. The audit's zero count concerns **observable** contamination; it does not certify absent hidden memory or replace the self-recognition sensitivity. No complete GO or CONDITIONAL GO could be supported from missing mechanism evidence, but neither is needed for this NO-GO.

## Reporting boundaries and sensitivity

- The lead-time zero is **no crossing within the available T−180/T−90/T−30/T−7 snapshots**, not a same-day warning. At θ=0.5, **23/42** positive matters have no crossing; the detected-only median is 30 days, but that is **not** the frozen all-positive statistic. T-snapshot precision is aided by a high positive share (**137/171 = 80.1%**), so 87.8% precision alone is weak evidence of useful advance warning.
- HIST C90 has **100 snapshots, 5 events, 29 matters**, all FDA; LATE C90 has **27 scored snapshots, 9 events, 15 matters**, with positive events in four SEBI matters. The US/India and HIST/LATE slices largely conflate regulator and calendar period; repeated snapshots are not independent matters. Report these limits alongside the point estimates and thread-clustered intervals.
- All selected retained evidence is Tier B; `ALL`, `B_ONLY`, and `B_PLUS_C` are aliases where packets are identical. This cohort cannot identify Tier C, stakeholder, or news lift. The 96% direction score merely matches the dominant label; it is not content value above a majority classifier. FDA action dates are first verified public finalization notices, with exact first PDF posting days unresolved, so timing claims are conditional.
- Relaxing or tightening the relevant numeric bands by **0.05** leaves NO-GO: LATE AUROC **0.577 < 0.65**, HIST–LATE gap **0.310 > 0.15**, and India AUROC **0.456 < 0.60**. The HIST title confidence interval continues to cross zero under any such band adjustment. No post-result threshold change is warranted.

Sources: `docs/PREREGISTRATION.md` §6; `PROTOCOL_DEVIATIONS.md` DEV-001–005 and DEV-014–016; `data/audits/core60_gate_readiness_20261004.md`; `data/audits/scaled60_full_acceptance_20261005.json`; `reports/metrics.json` (including recognition-excluded and sensitivity slices). This review did not alter forecasts, labels, metrics, or frozen thresholds.
