# Current empirical results

Updated 2026-10-04. The predictive GO/NO-GO gate has not been reached. The current frozen dataset has 327
threads (208 actions, 119 controls), 1,785 evidence records, 99 source-audited RAPID matters and zero GOLD.

Full source audits of the SEBI-R30/FDA-H30 cohort are complete. Packet release passed for ASTRA_CORE60
(20 T-design batches, 60 matters) and ASTRA_CAL60 (18 C-design batches, 45 eligible matters): 38 packets,
678 distinct forecasts and 678 same-input aliases. This is authorization for inference, not an empirical
result. Inference is being launched; no completed output, ingestion or score is asserted without receipts.
The retained cohort has 61 distinct evidence records, all Tier B. B_ONLY, B_PLUS_C and ALL are the same input,
so no Tier C, stakeholder or news lift is measurable in this release. Evidence versus TITLE_ONLY remains an
available comparison, subject to output audit and within-matter analysis.

No headline predictive metrics are available. Repaired SMOKE4 and MASK5 pass bounded technical audits and the
append-only ledger contains108 verified records including legacy diagnostics. Earlier invalidated runs remain
preserved. A successful JSON/coherence check does not establish valid historical labels or evidence.

The first scored technical diagnostic has18 evaluable180-day rows from nine of the ten smoke matters: model
Brier0.05587 versus0.04441 for the best thread-grouped baseline (lower is better), a skill estimate of-0.258 with
90% thread-clustered interval[-3.372,0.282]. Both model and baseline have AUROC1.0 because India/action and
FDA/control status are confounded. These figures are excluded from headline conclusions. Complete/quasi
separation makes calibration slope undefined; divergent finite slopes are not valid results.

MASK5 changes180-day probabilities by-5 to+6 percentage points across eight paired rows. All four India rows
still self-report recognition. Masking therefore has not demonstrated removal of memorisation. Detailed results
are in reports/SMOKE4_DIAGNOSTIC.md and data/audits/mask5_output_audit_20261004.md.

Earlier source audits found false no-action labels, final announcements earlier than recorded publication dates,
and undated current comment counts assigned synthetic historical dates. Those findings invalidated earlier
forecasts for empirical use and motivated the rebuilt, audited Core60 freeze. Other unaudited frames still
require source checks; these findings do not establish that regulation is either predictable or unpredictable.

Current evidence cannot support a quantified Tier-C lift, prospective discovery performance, content accuracy,
or useful lead-time claim. FDA action timing is conditional/medium-confidence first verified public notice timing,
not proven first PDF upload timing; SEBI and FDA absence controls are medium-confidence bounded checks. Visible
matter identities can induce recognition. No GOLD case is promoted. The next result requires batch receipts,
output leakage/recognition audit, valid ledger ingestion and separate T/C scoring against meaningful baselines.

See LEAKAGE_AUDIT.md for exclusions and PROJECT_STATUS.md for the active repair phase.
