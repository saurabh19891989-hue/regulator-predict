# Scaled60 remaining-output audit — progress through 2026-10-05

**PARTIAL: reviewed batches PASS; full remaining-output audit is not complete.**

Scope: CORE60 b004–b020 and CAL60 b004–b018, 32 batches requesting 558 distinct forecasts. The first six campaign batches (120 forecasts) are covered by the preserved first and second output-audit reports.

Reviewed so far: 12 batches, 240 forecasts. Each received complete packet-to-output text review, raw probability/field/citation checks, and original session/event/output hash checks. No observed contamination or unresolved blocking defect in accepted batches. Recognition is self-report and does not establish absence of latent memory.

| Batch | Forecasts | Recognition flags | Result |
|---|---:|---:|---|
| ASTRA_CORE60_b004 | 20 | 2 | PASS |
| ASTRA_CAL60_b004 | 20 | 2 | PASS |
| ASTRA_CORE60_b005 | 20 | 2 | PASS |
| ASTRA_CAL60_b005 | 20 | 2 | PASS |
| ASTRA_CORE60_b006 | 20 | 1 | PASS |
| ASTRA_CAL60_b006 | 20 | 1 | PASS |
| ASTRA_CORE60_b007 | 20 | 1 | PASS |
| ASTRA_CAL60_b007 | 20 | 2 | PASS |
| ASTRA_CORE60_b008 | 20 | 1 | PASS |
| ASTRA_CORE60_b009 | 20 | 1 | PASS |
| ASTRA_CAL60_b008 | 20 | 1 | PASS |
| ASTRA_CAL60_b009 | 20 | 2 | PASS |

The durable JSON companion records individual hashes, session IDs, recognition IDs, counts, and review status. Original receipt event paths were checked; final reconciliation of all repository event copies remains pending. No outcome records were parsed. Frozen canonical files were hashed only as opaque bytes. The observation boundary remains 2026-09-24.

CAL b008 initially had the prior quota-failed event in its active archived event path. The parent reconciled that file to the successful receipt; the auditor verified matching successful bytes/hash and separately preserved failed-attempt receipt. This resolved archival defect did not involve changing a forecast.

New successful batches will be reviewed as they arrive. This report is not full-campaign acceptance or permission to alter predictions. No forecasts, sources, code, or other project documents were changed; no inference or ingestion was performed by this audit.
