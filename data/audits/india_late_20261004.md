# India action-thread audit — 2026-10-04

Scope: 15 originally assigned LATE RBI/SEBI threads, extended at parent request to 7 HIST SEBI-R actions (R0017, R0018, R0021, R0024, R0025, R0027, R0028), for **22 actions total**. Observation cutoff remains **2026-09-24**. Official regulator pages and linked PDFs were fetched; dated claims and content were compared to raw records. The patch file is `data/audits/patches/india_late_20261004.jsonl`. No canonical build, snapshot, forecast, ledger, or raw record was changed.

## Findings

- **H0007:** exact-title RBI IT-governance Master Direction was issued **2023-11-07**, not 2026-07-31. The 2026 cyber framework is a separate, later instrument. Source: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12562&Mode=0
- **H0009:** RBI market-risk final is dated **2026-09-21** and sets effect on **2027-04-01**, compared with the draft's proposed **2024-04-01**. Source: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13705&Mode=0
- **H0015:** April 30 is the instrument's signature date; RBI explicitly identifies **2026-05-06** as its Gazette publication date. Source: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13445&Mode=0 and https://egazette.gov.in/WriteReadData/2026/272222.pdf
- **R0019:** February paper also proposed an SGF coverage change, but this sampled thread explicitly covers only the Z-score mechanism. August 12 circular adopts its scoped Z-score change (10→5), so as-proposed remains valid. Source: https://www.sebi.gov.in/legal/circulars/aug-2026/review-of-inclusion-of-historical-scenarios-in-stress-testing-for-commodity-derivatives-segment_103521.html
- **R0017:** February 9 consultation included Social Impact Fund investment and two NPO requirements. March 23 board item adopts only the investment reduction to Rs 1,000; patched to partial/mixed content. Source: https://www.sebi.gov.in/media-and-notifications/press-releases/mar-2026/key-decisions-taken-in-the-sebi-board-meeting-dated-23rd-march-2026_100515.html
- **R0022:** HTML circular landing page returned 404; official SEBI PDF remains live and dated May 8. Its 30-day uniform lag is sourced directly, and content direction is corrected to as proposed. Source: https://www.sebi.gov.in/sebi_data/attachdocs/may-2026/1778242522289.pdf
- **R0026:** September 24 board release adopts CAPSM changes, but its summary does not establish all four proposal themes; content confidence lowered to low. Source: https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2026/key-decisions-taken-in-the-sebi-board-meeting-dated-24th-september-2026_104725.html
- All Tier D records in this batch used dynamic Google News queries or publisher homepages, so dated originals cannot be reconstructed; all are dropped. Two RBI Tier C claims containing retrospective anchor timing were corrected.

## Per-thread empirical eligibility after patches

| Thread | First decisive date | Binary/timing | Content label | Retained official precursors | GOLD |
|---|---|---|---|---:|---|
| IN-RBI-H-0007 | 2023-11-07 | Yes (high) | Yes (medium) | 2 | No |
| IN-RBI-H-0009 | 2026-09-21 | Yes (high) | No (low) | 1 | No |
| IN-RBI-H-0015 | 2026-05-06 | Yes (high) | Yes (medium) | 2 | No |
| IN-SEBI-R-0004 | 2026-08-14 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0008 | 2026-06-19 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0010 | 2026-06-19 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0011 | 2026-06-19 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0012 | 2026-06-19 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0014 | 2026-08-24 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0015 | 2026-05-29 | Yes (high) | Yes (medium) | 1 | No |
| IN-SEBI-R-0016 | 2026-06-15 | Yes (high) | Yes (medium) | 1 | No |
| IN-SEBI-R-0017 | 2026-03-23 | Yes (high) | Yes (medium) | 1 | No |
| IN-SEBI-R-0018 | 2026-03-23 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0019 | 2026-08-12 | Yes (high) | Yes (medium) | 1 | No |
| IN-SEBI-R-0020 | 2026-05-05 | Yes (high) | Yes (medium) | 1 | No |
| IN-SEBI-R-0021 | 2026-03-23 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0022 | 2026-05-08 | Yes (high) | Yes (medium) | 1 | No |
| IN-SEBI-R-0024 | 2025-12-24 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0025 | 2025-12-17 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0026 | 2026-09-24 | Yes (medium) | No (low) | 1 | No |
| IN-SEBI-R-0027 | 2025-12-17 | Yes (high) | Yes (high) | 1 | No |
| IN-SEBI-R-0028 | 2025-12-17 | Yes (high) | Yes (high) | 1 | No |

All 22 labels have an official dated adopting source after the listed repairs. H0009 and R0026 should be excluded from policy-content scoring because their full proposal-to-final disposition is not verified. No thread meets the three-distinct-evidence GOLD floor. These are **post-patch eligibility recommendations**; the parent task must rebuild and validate canonical records and snapshots before empirical use.

## Source limits

Official report/press pages directly show publication dates, and the linked attachments match their proposal text. A current regulator page and PDF do not by themselves prove an immutable historical version; no historical archive was available in this audit. The R0026 board summary lacks a fully notified amendment comparison. The R0017 board item does not adopt the additional NPO components; this audit does not prove no later separate action before cutoff. R0019's separate SGF coverage proposal is outside its sampled thread's explicit scope.
