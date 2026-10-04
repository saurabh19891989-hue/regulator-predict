# Late India control source audit — 2026-10-04

Fixed outcome censor: **2026-09-24**. Scope: the four `IN-RBI-R` and eleven specified `IN-SEBI-R` draft/consultation threads. This audit did not rebuild canonical data or snapshots. The accompanying patch file is `patches/india_controls_20261004.jsonl`.

## Result

| Measure | Count |
|---|---:|
| Audited threads | 15 |
| False unresolved controls corrected to official action | 3 |
| Provisionally unresolved at cutoff | 12 |
| Official B/C precursors retained | 16 (15 B, 1 C) |
| Unstable Tier D items dropped | 35 |
| GOLD eligible now | 0 |

The three RBI false controls have dated primary releases that expressly identify the sampled draft and announce final issuance. Adoption is the issuance date, not the later effective date:

| Thread | First official final adoption | Primary source | Scope of repair |
|---|---|---|---|
| `IN-RBI-R-0001` | 2026-01-05 | [RBI related-party-lending final release](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61972) | Eight regulated-entity credit-risk amendments plus disclosure amendments; release explicitly cites the 2025-10-03 draft. |
| `IN-RBI-R-0002` | 2026-01-16 | [RBI Integrated Ombudsman Scheme, 2026 release](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62052) | Release explicitly cites the 2025-10-07 draft. The scheme came into force 2026-07-01, after adoption. |
| `IN-RBI-R-0004` | 2026-06-24 | [RBI Net Open Position final release](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=63007) | Eight amendment directions; release explicitly cites the 2026-01-14 draft. Effective date is 2027-04-01. |

The broad mechanisms were adopted. The exact changes to thresholds, exceptions and operational parameters were not independently compared clause by clause; the patched `as_proposed` content direction is **provisional medium confidence**. Action existence and first release date are high confidence. All three require downstream snapshot rebuild and post-build leakage validation.

## Precursor checks

The four RBI anchor drafts were reopened at their numbered official press releases: [related-party lending](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61365) (2025-10-03), [Ombudsman](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61374) (2025-10-07), [forex transaction costs](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61782) (2025-12-09), and [Net Open Position](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62041) (2026-01-14). Their datelines and draft/consultation framing agree with raw B items. The extra R-0001 C item is [RBI's 2023-12-08 policy statement](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=56889): its connected-lending section explicitly promises a unified framework and a later public-comment draft.

Each of the eleven SEBI B items was reopened at its official consultation landing page and attached PDF. The landing-page date matched the raw date; every PDF explicitly prints an “Issued on” date agreeing with the listing. The attached PDFs contain the proposals rather than final circulars. No retained official precursor is on or after a verified decisive date. The eleven official source URLs are the `E01` records in the audit JSONL; their titles and mechanisms were checked against the PDFs. Minor wording/format differences do not change the proposed mechanism.

Every Tier D item in this batch pointed either to a dynamic Google News RSS query or to a news-domain homepage, not to a stable dated article. Those 35 items are dropped. The draft PDFs' annexed **draft circulars** were treated as part of the Tier B proposal, not as enacted circulars.

## Bounded negative-outcome coverage

For SEBI, the [official News Listing search](https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListingAll=yes) was queried on 2026-10-04 using each topic's proposal terms (the exact query URLs are patched into each `outcome_sources`). This covered circular, regulation, report and press-release *titles* through the fixed cutoff. I also read the official [2025-12-17](https://www.sebi.gov.in/media-and-notifications/press-releases/dec-2025/sebi-board-meeting_98433.html), [2026-03-23](https://www.sebi.gov.in/media-and-notifications/press-releases/mar-2026/key-decisions-taken-in-the-sebi-board-meeting-dated-23rd-march-2026_100515.html), [2026-06-19](https://www.sebi.gov.in/media-and-notifications/press-releases/jun-2026/key-decisions-taken-in-the-sebi-board-meeting-dated-19th-june-2026_102250.html), and [2026-09-24](https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2026/key-decisions-taken-in-the-sebi-board-meeting-dated-24th-september-2026_104725.html) board-decision PDFs. No item adopting one of these eleven sampled mechanisms was located. The title index is not a full-text corpus; a differently titled implementation cannot be ruled out. All eleven therefore remain `unresolved` with **medium** label confidence, not proven no-action.

Two plausible title matches were checked for scope: the [2026-06-15 base-price/call-auction circular](https://www.sebi.gov.in/legal/circulars/jun-2026/norms-for-base-price-price-bands-call-auction-in-pre-open-session-and-close-out-procedure-for-exchange-traded-funds-etfs-_102121.html) is ETF-specific, not the multi-exchange equity-scrip or IPO/re-listed-scrip proposal (`R-0003`, `R-0005`). The [2026-09-09 position-limit circular](https://www.sebi.gov.in/legal/circulars/sep-2026/review-of-position-limits-for-clients-and-penalty-provisions-for-violation-breach-of-position-limits-for-commodity-derivatives-segment_104387.html) concerns **clients in commodity derivatives**, not trading-member FutEq limits in equity derivatives (`R-0023`). The September board's AIF action concerns a distinct AIF proposal, not the June 30 investor-consent/conflicted-transaction paper (`R-0001`).

For `IN-RBI-R-0003`, bounded searches of [RBI Notifications](https://www.rbi.org.in/Scripts/NotificationUser.aspx), press releases and exact proposal terms did not locate a final retail forex cash/tom/spot transaction-cost disclosure circular by 2026-09-24. It remains `unresolved`, medium confidence. The RBI raw censor date of 2026-09-25 was corrected to the study's fixed 2026-09-24 for all four RBI threads. An unindexed or differently titled instrument remains possible.

## Cohort disposition after patches

All fifteen may remain in the **RAPID precursor sampling frame** after the patches are applied and snapshots are rebuilt. The three corrected action threads are `IN-RBI-R-0001`, `IN-RBI-R-0002`, `IN-RBI-R-0004`. The twelve **provisionally unresolved controls** are `IN-RBI-R-0003`, `IN-SEBI-R-0001`, `IN-SEBI-R-0002`, `IN-SEBI-R-0003`, `IN-SEBI-R-0005`, `IN-SEBI-R-0006`, `IN-SEBI-R-0007`, `IN-SEBI-R-0009`, `IN-SEBI-R-0013`, `IN-SEBI-R-0023`, `IN-SEBI-R-0029`, `IN-SEBI-R-0030`. Do not treat `unresolved` as demonstrated long-run no-action.

No thread qualifies for GOLD: after Tier D removal, each has only one distinct official B item except RBI R-0001, which has one B plus one C. The required minimum is three retained distinct items, and the negative labels are bounded-search results. No thread was excluded solely because it became a positive action; retaining those cases preserves the original precursor sample.
