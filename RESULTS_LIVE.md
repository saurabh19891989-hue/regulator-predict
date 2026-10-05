# Current empirical results

## Final decision — 2026-10-05

**NO-GO for the current Astra / SEBI-R30-FDA-H30 approach.** Frozen G1 and G5 fail; independent
review agrees. HIST C90 baseline skill +0.320 is promising, but evidence-versus-title CI crosses zero,
LATE C90 AUROC0.577 misses0.70, India AUROC0.456 misses0.65 and HIST-LATE gap0.310 exceeds0.10.
At p>=0.5,19/42 positive matters get a warning; all-matter median lead is zero (23 misses), so G4 fails.
Timing calibration fails; content accuracy96% merely matches the majority baseline. No TierC lift,
trajectory ablation, parameter coverage, full masking or GOLD survival is established.
All38 calls /678 distinct forecasts independently audited and1,356 logical rows ingested; ledger1,464
records verified. Zero visible contamination;64 recognition disclosures. Exclusion preserves NO-GO.
Stop at the gate; no production or trading architecture is justified. Full results:
reports/FINAL_GO_NO_GO_20261005.md, reports/FINAL_DECISION_20261005.json,
reports/FINAL_GATE_REVIEW_20261005.md and reports/metrics.json.
Market-data capture closed successfullyOctober5 15:31IST with24,167,141updates; automatic Drive upload
started15:50IST; completed verification is pending. Latest verified completed copy remainsOctober2.
No daily regulatory collection/upload automation found. See docs/COLLECTION_STATUS_20261004.md.

## Earlier checkpoints (historical; superseded by final decision above)

## Current checkpoint — 2026-10-05, scaled scoring

All38 fresh Astra calls completed:678 distinct forecasts plus678 same-input aliases. Full independent
text/citation review and execution preflight PASS. Zero visible contamination;64 self-recognition disclosures.
Unsupported conditional parameter guesses are documented, not certified as accurate. All1,356 scaled logical
rows ingested without problems; hash-chain verification passes1,464 records, including108 excluded diagnostics.
Final evaluation is running with ALL primary arm and same-model TITLE_ONLY; no legacy probe mixed in.
Freeze remains327 threads /1,785 evidence /99 source-audited RAPID /zero GOLD, censor2026-09-24.
Today market capture closed successfully15:31IST with24,167,141updates; Drive upload due15:50IST.
No automated daily regulatory collection/upload was found. Predictive GO/NO-GO is pending scored metrics.

## Earlier checkpoints (historical; superseded by the checkpoint above)


## Live continuation — 2026-10-05

The ordinary account window reopened after the user continued. Fifteen successful batches / 300 distinct
forecasts were preserved from October4; the failed CAL60 b008 attempt was archived before retry. The remaining
23 batches resumed with two workers. By the latest audit message, eighteen batches / 360 distinct forecasts
were complete and independently reviewed without unresolved defects. No scaled output has been ingested or
scored yet. Source freeze and observation cutoff remain unchanged. Eleven focused evaluation tests passed
after DEV-016 fold-local preprocessing repair. Daily market collector timers were rechecked; today's09:05IST
capture was not yet due. No daily regulatory collector/upload exists in this workspace.

Updated 2026-10-04. The predictive GO/NO-GO gate has not been reached. The current frozen dataset has 327
threads (208 actions, 119 controls), 1,785 evidence records, 99 source-audited RAPID matters and zero GOLD.

Full source audits of the SEBI-R30/FDA-H30 cohort are complete. Packet release passed for ASTRA_CORE60
(20 T-design batches, 60 matters) and ASTRA_CAL60 (18 C-design batches, 45 eligible matters): 38 packets,
678 distinct forecasts and 678 same-input aliases. This is authorization for inference, not an empirical
result. Six batches / 120 distinct forecasts have completed with receipts and pass structural preflight. Independent
review passed the first 40; the next 80 are under review. The remaining 32 batches resumed after an ordinary
usage-window interruption. No scaled output has been ingested or scored yet.
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
