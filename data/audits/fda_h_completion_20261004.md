# FDA historical Frame H completion audit — 2026-10-04

## Result

The 21 previously unaudited historical FDA guidance threads are now audited: **18 actions and 3 stalled controls**. Together with the 9 historical threads in `audit_us_fda_stratified_20260927.jsonl`, this covers **30/30 Frame H threads** (23 actions, 7 controls). The separate prior C-0001 audit is outside this frame. This completion pass creates audit and patch records only; derived snapshots need rebuilding by the owner.

Action/delay labels remain RAPID quality. Each retained thread has only **one distinct primary precursor** after the pre-existing synthetic comment-count drops, so **0/21 are GOLD eligible**. The prior H audit also did not certify GOLD. This is a usable binary action/control frame after patches, subject to documented timing and absence limits; it is not a 30-thread GOLD set.

## Method and decision rule

- Read each original numbered Federal Register draft notice/API abstract and Filed line. All 21 stored excerpts and extracted claims match original abstracts after whitespace/punctuation normalization. Kept the FR print date as `publication_date`; patched `first_known_date` to the earlier public-inspection Filed date. The official print page, raw text and public-inspection PDF URLs are in the per-thread JSONL records.
- For 18 actions, read the matching official final-guidance FR notice, checked title/topic and docket (PFDD Guidance 3, H-0022, uses a different final docket but explicitly names its draft), and moved `decisive_date` to the final notice public-inspection date. This is the **earliest verified official public finalization notice**, an upper bound on first availability. It does not prove no earlier FDA PDF posting. `label_confidence=medium` records this exact-day uncertainty.
- For 3 controls, bounded FR API searches by same docket and exact FDA title to `2026-09-24` returned only the draft notice. FDA’s current official guidance page still says Draft. These are censored no-action observations, with medium absence confidence because FDA could have posted an unannounced final or later revised the page.
- The pre-existing `us_fda_synthetic_counts_20260927.jsonl` drops unsupported close+14 comment counts; this patch file does not duplicate those operations. The fixed censor date is `2026-09-24`, replacing executor retrieval date `2026-09-25`.
- Broad content scoring asks whether the thread’s draft policy mechanism survived finalization. All 18 actions retain the topic/mechanism at that level. Final notices describe some additions and refinements, listed below. Notice-level reading is insufficient for exact parameter-level identity; all 18 content confidences are patched to medium. H-0016’s wider final UDI title includes prior guidance, but its thread-scoped class I GUDID mechanism survives; its former low content confidence is repaired to medium.

## Per-thread disposition

| Thread | Draft first verified / print | Final first verified / print | Binary and timing after patch | Content after patch | Thread-scoped qualification |
|---|---|---|---|---|---|
| H-0002 | 2019-07-31 / 2019-08-01 | 2022-07-26 / 2022-07-27 | Action; PI-date bound, medium | Broad direction only, medium | Final notice adds immunogenicity, administered-volume and microsampling detail. |
| H-0006 | 2020-01-10 / 2020-01-13 | 2023-04-13 / 2023-04-14 | Action; PI-date bound, medium | Broad direction only, medium | Final notice reports added nonclinical test detail and alignment with consensus standards. |
| H-0009 | 2020-07-14 / 2020-07-15 | 2021-10-05 / 2021-10-06 | Action; PI-date bound, medium | Broad direction only, medium | Final notice reports clarifying/editorial revisions while retaining biomarker and surrogate-endpoint scope. |
| H-0010 | 2020-08-28 / 2020-08-31 | 2022-01-25 / 2022-01-26 | Action; PI-date bound, medium | Broad direction only, medium | Final notice retains fit-for-purpose PRO principles, clarifies instrument scores and expands examples across the product life cycle. |
| H-0011 | 2020-10-07 / 2020-10-08 | 2021-06-23 / 2021-06-24 | Action; PI-date bound, medium | Broad direction only, medium | Final notice adds diversity, patient-experience and clinical-effects recommendations. |
| H-0012 | 2020-11-30 / 2020-12-01 | 2023-03-10 / 2023-03-13 | Action; PI-date bound, medium | Broad direction only, medium | Final notice updates pH-DDI framework, references and proton-pump-inhibitor examples. |
| H-0013 | 2021-05-20 / 2021-05-21 | 2023-05-25 / 2023-05-26 | Action; PI-date bound, medium | Broad direction only, medium | Final notice clarifies standard errors, stratification, estimands, interactions and other methods. |
| H-0014 | 2021-06-25 / 2021-06-28 | 2025-12-15 / 2025-12-16 | Action; PI-date bound, medium | Broad direction only, medium | Final notice changes aggregate-analysis approaches and adds small-program, rare-disease and electronic-reporting detail. |
| H-0015 | 2021-09-22 / 2021-09-23 | 2022-10-19 / 2022-10-20 | Action; PI-date bound, medium | Broad direction only, medium | Final notice retains donor-screening and testing scope; detailed draft-versus-final recommendations were not fully compared. |
| H-0016 | 2021-10-13 / 2021-10-14 | 2022-07-22 / 2022-07-25 | Action; PI-date bound, medium | Broad direction only, medium | Final notice confirms the class I GUDID policy, clarifies consumer-health-product scope and consolidates the prior UDI compliance guidance; score this thread on its GUDID mechanism. |
| H-0017 | 2021-12-09 / 2021-12-10 | 2023-06-29 / 2023-06-30 | Action; PI-date bound, medium | Broad direction only, medium | Final notice adds efficacy-assessment considerations within the same CRSwNP trial-design scope. |
| H-0018 | 2021-12-22 / 2021-12-23 | 2023-12-21 / 2023-12-22 | Action; PI-date bound, medium | Broad direction only, medium | Final notice clarifies DHT functions, device regulatory considerations and participant-owned technologies. |
| H-0019 | 2022-03-09 / 2022-03-10 | 2023-12-06 / 2023-12-07 | Action; PI-date bound, medium | Broad direction only, medium | Final notice clarifies saleable-return transaction information and verification details. |
| H-0020 | 2022-04-19 / 2022-04-20 | 2023-03-15 / 2023-03-16 | Action; PI-date bound, medium | Broad direction only, medium | Final notice retains literature, review and meta-analysis scope for animal drug approvals; detailed changes were not fully compared. |
| H-0022 | 2022-06-29 / 2022-06-30 | 2025-11-17 / 2025-11-18 | Action; PI-date bound, medium | Broad direction only, medium | Final notice reformulates the COA conceptual framework as a COA-based endpoint approach and clarifies qualitative patient input. |
| H-0024 | 2022-08-22 / 2022-08-23 | 2024-02-14 / 2024-02-15 | Action; PI-date bound, medium | Broad direction only, medium | Final notice adds informed-consent charging information and an intermediate-size expanded-access definition. |
| H-0025 | 2022-10-05 / 2022-10-06 | 2024-10-17 / 2024-10-18 | Action; PI-date bound, medium | Broad direction only, medium | Final notice adds a footnote on unsolicited DMF amendments after prior assessment. |
| H-0026 | 2022-10-31 / 2022-11-01 | none through censor | Censored control; medium | N/A | Control; draft status corroborated by current FDA page. |
| H-0027 | 2022-12-08 / 2022-12-09 | 2024-08-28 / 2024-08-29 | Action; PI-date bound, medium | Broad direction only, medium | Final notice clarifies VMSR product-code eligibility and summary-reporting conditions. |
| H-0028 | 2023-01-19 / 2023-01-20 | none through censor | Censored control; medium | N/A | Control; draft status corroborated by current FDA page. |
| H-0029 | 2023-02-24 / 2023-02-27 | none through censor | Censored control; medium | N/A | Control; draft status corroborated by current FDA page. |

## Eligibility and remaining limits

**Binary action/control:** Eligible for a RAPID comparison after patch application: 18 verified final notices and 3 bounded no-action controls. The complete historical frame has 23 action and 7 control labels. Controls are not permanent negatives; they mean no verified final/withdrawal by the fixed censor.

**Timing:** Action dates are verified public-inspection notice dates, not proven first FDA file-release dates. Exact first-event timing is conditional/medium. Censored controls support time-to-event treatment through 2026-09-24. Published FR issue dates were 1–3 calendar days later than the inspection dates in this completion pass.

**Content:** The final notices support broad `as_proposed` thread-scoped direction. They do not establish exact parameter-level equality or quantitative content accuracy. The FDA final PDFs and original draft PDFs would be needed for that finer claim. No content score applies to the 3 controls.

**GOLD:** None of these 21 threads meets the ≥3 distinct retained primary-item requirement. Synthetic comment counts are already dropped and must not be counted. The frame is informative for RAPID action/control comparison but thin for precursor-class ablations.

**Selection:** The executor describes a systematic step-10 sample from N=313 FDA draft-guidance notices. We checked each drawn anchor’s topic and sample-index metadata; we did not independently rebuild the full 313-item population in this pass. The 23/30 historical finalization frequency is descriptive of this sampled frame, not a general FDA base-rate estimate.

## Artifacts

- `data/audits/audit_fda_h_completion_20261004.jsonl`: 21 audit records with official URLs, dates, findings, and separate eligibility decisions.
- `data/audits/patches/fda_h_completion_20261004.jsonl`: source-backed first-known, outcome-date/provenance, confidence, content and censor repairs.
- The original raw files, canonical build outputs, forecasts and ledgers were not changed.
