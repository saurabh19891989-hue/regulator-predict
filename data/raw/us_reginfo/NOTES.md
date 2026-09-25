# us_reginfo — NOTES

Workstream: `us_reginfo`. Executor collected point-in-time Tier-B precursor tables
keyed by RIN from reginfo.gov, for later merging into US Federal Register
rulemaking threads built by another agent (no coordination needed: this
collection is a census over reginfo.gov, not filtered to any particular
thread list). Retrieval date for everything in this directory: 2026-09-25.

## What was collected

1. `agenda_entries.jsonl` — 59,519 rows = every `<RIN_INFO>` element across all
   16 Unified Agenda bulk XML editions in scope (Spring 2018 through the
   terminal "2026" edition; see below). 13,208 distinct RINs. One row per
   (pub_id, RIN).
2. `agenda_editions.json` — public-date registry for those 16 editions:
   `online_release_date` (approximated from each edition's XML `RUN_DATE`
   attribute), `fr_publication_date` (verified via the Federal Register API
   against the Regulatory Information Service Center's "Introduction to the
   Unified Agenda ..." notice for that edition), and
   `conservative_public_date` = the later of the two (== `fr_publication_date`
   whenever one exists, since RUN_DATE always precedes it).
3. `oira_reviews.jsonl` — 4,873 rows from `EO_RULE_COMPLETED_2018.xml` through
   `EO_RULE_COMPLETED_2025.xml`, `EO_RULE_COMPLETED_YTD.xml` (2026 to date),
   and `EO_RULES_UNDER_REVIEW.xml` (172 rules pending review as of
   2026-09-25). 3,370 distinct RINs with at least one review record.
4. `collectors/reginfo.py` — the collector, plus two pure merge-helper
   functions (`agenda_evidence_for_rin`, `oira_evidence_for_rin`) and a
   `--selftest` that exercises both using RIN 3235-AM96 and a finalized RIN
   (0938-AT38, CMS). `python3 collectors/reginfo.py --selftest` passes.

## Method

- Editions enumerated from `https://www.reginfo.gov/public/do/eAgendaXmlReport`
  (which lists every bulk file the XMLViewFileAction endpoint currently
  serves) and cross-checked id-by-id against
  `https://www.reginfo.gov/public/do/eAgendaHistory`'s own historical-edition
  selector, which gives reginfo.gov's own season label for each pub_id.
- Each edition's bulk XML (10-20 MB) was downloaded once, stream-parsed with
  `xml.etree.ElementTree.iterparse` (elements cleared as they're consumed),
  and the source file deleted immediately after parsing — nothing from the
  raw bulk XML is retained on disk, only the extracted JSONL. Peak disk use
  during collection: one ~20 MB XML file at a time in `cache/` (now empty).
  Final directory size: **48 MB**, far under the 1.5 GB budget.
- reginfo.gov's `XMLViewFileAction` endpoint ignores HTTP Range headers
  (always returns the full body), so "streaming" here means incremental
  parsing after a full download, not partial HTTP fetches.
- Edition public dates were verified two ways and reconciled conservatively
  (see agenda_editions.json's `note` field per edition for the specific
  evidence):
  1. `online_release_date` ≈ the XML `RUN_DATE` attribute embedded in that
     edition's own bulk file (OIRA's internal "data frozen as of" date).
  2. `fr_publication_date` = the date the Federal Register published that
     edition's "Introduction to the Unified Agenda of Federal Regulatory and
     Deregulatory Actions" notice, authored by the Regulatory Information
     Service Center, found via the FR API. This notice is the one
     government-wide document per edition (as opposed to the many
     individual per-agency "Unified Agenda ..." / "Semiannual Regulatory
     Agenda" notices that all share the same publication date within an
     edition) — RISC authorship reliably identifies it across all 16
     editions in scope.
  `conservative_public_date` = later of the two. In every edition except
  201804, `fr_publication_date` > `online_release_date` (by a few weeks to,
  in one case, ~3.5 months for Fall 2020 across the Jan 2021 transition), so
  `conservative_public_date` == `fr_publication_date`. For 201804 the
  RUN_DATE (2018-09-17) is actually later than the verified FR date
  (2018-06-11) — treated as a later re-export of the dataset, not the
  original publish date, so the FR date is used.

## Two real point-in-time findings worth flagging to downstream users

1. **No "Fall 2025" or "Spring 2026" edition exists.** pub_id `202510`
   (which the file-naming convention would suggest is "Fall 2025") is
   labeled by reginfo.gov's own history page as **"2026 The Regulatory Plan
   and the Unified Agenda of Federal Regulatory and Deregulatory Actions"**
   — a single annual edition replacing both the usual Fall2025 and
   Spring2026 slots. Its FR "Introduction" notice published 2026-08-14
   (document 2026-16603). `pub_id 202604` was probed directly and does not
   exist (reginfo.gov returns its generic HTML error page, not XML). This
   is the terminal/most recent edition as of this collector's 2026-09-25
   retrieval date. Task instructions anticipated pub_ids through "202604";
   the actual last id in scope is 202510.
2. **The Fall 2024 edition (`pub_id 202410`) was never published in the
   Federal Register.** Searched the FR API for
   "Unified Agenda of Federal Regulatory and Deregulatory Actions" and,
   separately, "Semiannual Regulatory Agenda" over 2024-09-01..2025-10-01:
   zero matching documents for a Fall-2024-labeled Unified Agenda notice.
   Spot-checked a per-RIN reginfo.gov page for this edition
   (`eAgendaViewRule?pubId=202410&RIN=0503-AA80`), which explicitly shows
   "RIN Data Printed in the FR: No". Most plausible explanation: the
   Jan 2025 administration transition/regulatory freeze interrupted the
   normal online-then-FR publication sequence, and this edition was
   effectively superseded by the next edition, which appeared in the FR as
   "Spring 2025" on 2025-09-22 (a ~13-month gap since the prior FR
   publication, Spring 2024 on 2024-08-16). Because no independently
   verified public date exists for 202410 beyond its XML RUN_DATE
   (2024-12-12), `agenda_editions.json` marks it `date_confidence: "low"`
   and `agenda_evidence_for_rin` will still use RUN_DATE as
   `conservative_public_date` — **downstream forecasters using cutoffs
   between Dec 2024 and Sep 2025 should treat this edition's public date as
   uncertain** and prefer corroboration from an FR document before relying
   on it as a hard cutoff boundary.

## Derived-field decisions (agenda_entries.jsonl)

The bulk XML schema has no explicit boolean for "withdrawn"; it is inferred
as: `RIN_STATUS` contains "withdraw" (case-insensitive) OR any timetable
action for that (pub_id, RIN) contains "withdraw". `long_term` /
`completed_action` are read directly off `RULE_STAGE` (`"Long-Term Actions"`
/ `"Completed Actions"`). `projected_final_action_date_text` is the
`TTBL_DATE` of the last timetable row whose action matches
`^(\d*(st|nd|rd|th)?\s*)?final\s*(rule|action)` case-insensitively (so "2nd
Final Action" matches but "Final Rule Effective" and "Final Action
(Withdrawal)" do not, since those describe consequences of a final action
rather than the final action itself — "Final Action (Withdrawal)" is
deliberately excluded from the regex so it doesn't get mistaken for a normal
projected final rule). An extra field `printed_in_fr` (from `PRINT_PAPER`)
is included beyond the requested schema — it is a per-entry (not per-edition)
flag for whether that specific RIN's abstract was printed in the paper/FR
volume that edition (most entries are "No" in every edition, including ones
that did get an FR "Introduction" notice, since only a subset of entries get
full print — this is unrelated to the pub_id-level FR-publication-date
finding above and should not be confused with it).

## Coverage / summary counts

| pub_id | season/label | conservative_public_date | date_confidence | RIN rows |
|---|---|---|---|---|
| 201804 | Spring 2018 | 2018-06-11 | medium | 3,350 |
| 201810 | Fall 2018 | 2018-11-16 | high | 3,534 |
| 201904 | Spring 2019 | 2019-06-24 | high | 3,791 |
| 201910 | Fall 2019 | 2019-12-26 | high | 3,752 |
| 202004 | Spring 2020 | 2020-08-26 | high | 3,939 |
| 202010 | Fall 2020 | 2021-03-31 | high | 3,853 |
| 202104 | Spring 2021 | 2021-07-30 | high | 3,961 |
| 202110 | Fall 2021 | 2022-01-31 | high | 3,777 |
| 202204 | Spring 2022 | 2022-08-08 | high | 3,803 |
| 202210 | Fall 2022 | 2023-02-22 | high | 3,690 |
| 202304 | Spring 2023 | 2023-07-27 | high | 3,666 |
| 202310 | Fall 2023 | 2024-02-09 | high | 3,599 |
| 202404 | Spring 2024 | 2024-08-16 | high | 3,698 |
| 202410 | Fall 2024 | 2024-12-12 | **low** (see finding 2 above) | 3,331 |
| 202504 | Spring 2025 | 2025-09-22 | high | 3,821 |
| 202510 | 2026 (annual) | 2026-08-14 | high | 3,954 |

Row-level priority-category breakdown across all 59,519 rows: Substantive,
Nonsignificant 34,924; Other Significant 18,107; Economically Significant
3,273; Info./Admin./Other 1,459; Routine and Frequent 918; Section
3(f)(1) Significant 833; blank 5.

Distinct-RIN control balance (a RIN can be flagged across multiple editions):
2,128 distinct RINs ever flagged `withdrawn`; 9,197 ever flagged
`completed_action`; 3,181 ever flagged `long_term` (stalled/no-action-to-date
control population). This gives the downstream thread-builder a real
stalled/withdrawn control pool, not just positives.

oira_reviews.jsonl: 4,873 review rows, 3,370 distinct RINs, 1,056
economically-significant review rows. Completed-review decision breakdown:
Consistent with Change 3,976; Withdrawn 344; Consistent without Change 299;
Statutory or Judicial Deadline 75; Improperly Submitted 6; Emergency 1.
172 rows currently under review (2026-09-25 snapshot).

Only 2,622 of the 13,208 distinct agenda RINs also have an OIRA review
record. This is expected, not a collection gap: EO 12866 centralized OIRA
review applies mainly to executive-branch agencies and to
significant/economically-significant rules; independent regulatory
agencies (SEC, FCC, FTC, CFTC, FERC, etc.) and most non-significant rules
are not submitted to OIRA at all. Confirmed directly: RIN 3235-AM96 (SEC,
used in the self-test) has 9 Unified Agenda entries but 0 OIRA review
records — SEC is exactly the kind of independent agency this applies to.

## Known gaps / limitations

- `EO_RULES_UNDER_REVIEW.xml` is a **live snapshot**, not a point-in-time
  archive. It reflects what is pending as of 2026-09-25, the retrieval date.
  It should not be treated as "what was pending on every earlier date" —
  earlier-cutoff pending/received-but-not-completed status must instead be
  derived from the completed-year files' `date_received`/`date_completed`
  pair (a review with `date_received < cutoff <= date_completed` was pending
  at that cutoff), which is exactly what `oira_evidence_for_rin` does.
- The Fall 2024 edition (pub_id 202410) public-date gap described above is
  the one place in this dataset where `date_confidence` is `"low"`; every
  other edition's `conservative_public_date` is FR-API-verified
  (`date_confidence: "high"`) except Spring 2018, which is `"medium"`
  because of the RUN_DATE/FR-date ordering anomaly (documented, FR date used).
- `agenda_evidence_for_rin`/`oira_evidence_for_rin` build `source_url` from
  the standard `eAgendaViewRule?pubId=...&RIN=...` and the generic
  `eoAdvancedSearchMain` search entry point respectively; reginfo.gov has no
  stable public deep link to an individual OIRA review record (the "View EO
  12866 Meetings" link on a rule's agenda page is a *different* dataset —
  outside-party meeting logs, not review receipt/completion — so it was not
  used here).
- No RIN-level filtering to "only EO-12866-significant" was applied; this is
  a full census of both bulk sources (all RINs, all priority categories),
  per the task's preference for "all RINs" when feasible.
- Titles/abstracts sometimes change wording slightly between editions for
  the same RIN (e.g. RIN 2127-AL37 above: "Rear Seat Belt Reminder System" →
  "Seat Belt Reminder Systems" → "Rear Seat Belt Reminder System"); this is
  preserved as-is per edition (not normalized) so each evidence item quotes
  exactly what that edition printed, consistent with the no-hindsight-editing
  rule in EXECUTOR_GUIDE.md.
