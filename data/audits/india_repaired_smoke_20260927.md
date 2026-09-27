# India repair audit — 2026-09-27

Observation cutoff remains **2026-09-24**. This audit writes overlays only; raw executor and canonical data were not edited.

## Recommended action half of repaired smoke

| Thread | First adoption | T-90 | T-30 | Retained evidence at both cutoffs |
|---|---|---|---|---|
| IN-RBI-H-0011 | 2023-08-18 | 2023-05-20 | 2023-07-19 | E01 B, E02 C |
| IN-RBI-H-0012 | 2024-03-06 | 2023-12-07 | 2024-02-05 | E01 B |
| IN-RBI-H-0021 | 2025-05-08 | 2025-02-07 | 2025-04-08 | E01 B, E02 C |
| IN-SEBI-H-0004 | 2022-12-20 | 2022-09-21 | 2022-11-20 | E01 B, E02 B |
| IN-SEBI-H-0012 | 2023-06-28 | 2023-03-30 | 2023-05-29 | E01 B |

Dates above were computed after applying outcome/drop overlays in memory. All five have nonempty evidence at both cutoffs. Each thread has the same retained evidence at both horizons: this smoke tests leakage and plumbing, not incremental information arrival between horizons.

RBI H0011 and H0021 were false stalled controls. Their major outcome corrections require canonical/snapshot rebuilding and a post-build audit before GOLD promotion. Their audit verdict is contaminated_rebuild, gold_eligible=false. RBI H0012 and the two SEBI actions have minor_issue_fixed verdicts and primary evidence/outcome verification. All five remain RAPID because only one or two evidence items survive, below the EXECUTOR_GUIDE section 7 minimum of three; no GOLD promotion is authorized. Content confidence remains medium for incomplete parameter comparisons except the clear card-scope narrowing.

Pair these five with the independently audited FDA controls from the parallel audit. This gives regulator coverage and Tier C evidence, but action/control labels will be confounded with regulator/jurisdiction; do not interpret it as comparative forecasting performance.

## Concrete overlays

- Existing: data/audits/patches/india_gold_six_20260925.jsonl.
- Supplement: data/audits/patches/india_gold_six_20260925_supplement.jsonl.
- Verdicts: data/audits/audit_india_20260927.jsonl.

Supplement completes decisive document metadata, sealed summary/provenance, notes/key_parameters and cutoff for the false controls. It also corrects a prior SEBI rationale: February consultation paragraph32.4 already limits the change to trusts raising fresh funds; the new INR500 crore cap independently supports softened direction.

## False controls quarantined

IN-RBI-H-0001: share-capital/securities circular, March8,2022, RBI/2021-22/179, Notification Id12251.

IN-RBI-H-0004: operational-risk Master Direction, June26,2023, Notification Id12520. Deferred implementation is not no adoption.

IN-RBI-H-0005: October31,2023 PA-Cross Border circular Id12561 explicitly references the April7,2022 OEIF draft.

IN-RBI-H-0016: February21,2025 bond-forward Directions Id12784 explicitly finalise the December2023 draft. The earlier February13 enabling gazette and September22,2026 page revision need further examination before a first-date/content label.

IN-IRDAI-H-0008: IRDAI official notification list includes final Insurance Intermediaries (Amendment) Regulations2022, F.No.IRDAI/Reg/4/183/2022. Exact first publication/date and comparison remain pending.

IN-TRAI-H-0010: September18,2024 service-authorisation recommendations paragraphs2.324–2.325 expressly resolve the December2022 aircraft-ground consultation. Recommendations are the endpoint specified in this thread's process_type.

These receive exclude_thread patches rather than an invented content-direction label. Exclusion protects control scoring but does not complete their relabeling.

## Controls not certified

RBI H0017 has a primary homepage lead to 2026 final amendment directions; the stable adopting document remains unchecked. IRDAI H0001/H0003/H0006/H0013/H0014 lack a complete primary archive and substance check through the cutoff. TPA H0003 also has a February15/February16 anchor-date discrepancy. Their audit verdicts are unverifiable; none should serve as an independently confirmed no-action control.

Five India no-action controls were **not** established. A broader substantive control audit is required before scaling; same-title searches miss adoption under consolidated instruments.

## Primary sources

- RBI penal charges final: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12527
- RBI card final: https://rbi.org.in/scripts/NotificationUser.aspx?Id=12619
- RBI digital-lending final: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848&Mode=0
- SEBI December2022 Board release: https://www.sebi.gov.in/sebi_data/attachdocs/dec-2022/1671539359764.pdf
- SEBI June2023 Board release: https://www.sebi.gov.in/sebi_data/attachdocs/jun-2023/1687968454571.pdf
- SEBI green-bond consultation and extension: https://www.sebi.gov.in/sebi_data/attachdocs/aug-2022/1659672842609.pdf and https://www.sebi.gov.in/sebi_data/attachdocs/aug-2022/1661746726670.pdf
- SEBI sponsor consultation: https://www.sebi.gov.in/sebi_data/attachdocs/feb-2023/1677212827626.pdf
- SEBI REIT/InvIT Board memoranda: https://www.sebi.gov.in/sebi_data/meetingfiles/jul-2023/1688555914283_1.pdf and https://www.sebi.gov.in/sebi_data/meetingfiles/jul-2023/1688555899311_1.pdf

Some web-tool opens failed. Direct Invoke-WebRequest retrieval independently read RBI prid55506, Id12251 and Id12520 datelines and operative text. No failed fetch was treated as proof of no action.


