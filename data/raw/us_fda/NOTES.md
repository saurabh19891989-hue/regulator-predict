# NOTES — us_fda workstream (FDA draft guidance → final guidance threads)

process_type: `draft_guidance_to_final`. All dates/ids below verified 2026-09-25 (retrieval_date /
censor_date throughout).

## Sampling frames

### Frame H — historical, `US-FDA-H-0001`…`US-FDA-H-0030`
- Population: Federal Register API, `documents.json`, `conditions[agencies][]=food-and-drug-administration`,
  `conditions[type][]=NOTICE`, `conditions[term]="Draft Guidance" "Availability"`,
  `conditions[publication_date][gte]=2019-07-01`, `[lte]=2023-06-30`. Raw term match returned 644 documents.
- Filter (client-side, applied to all 644): title must contain "draft guidance"; excluded titles
  containing "correction" (5), "extension of comment period"/"reopening" (30), plural "Guidances"
  i.e. batch product-specific-guidance bundles (24), "withdrawal" (1), and abstracts that actually
  announce a FINAL guidance (term matched only because the final's abstract text says "...finalizes
  the draft guidance..."), plus 271 term matches whose title did not contain "draft guidance" at all
  (public meetings, ICR notices, etc. matched by the general term search). Filtered population **N=313**.
- Sample: **systematic**, step=10, start index 0, chronological (oldest-first) order → 30 threads
  (population indices 0, 10, 20, …, 290). Step recorded in each thread's `notes` field.
- Individual product-specific guidance (PSG) notices for a single product (e.g. "Product-Specific
  Guidance for Testosterone; Revised Draft Guidance for Industry; Availability") were **kept** in the
  population/sample — the task explicitly excludes only the *batch* PSG bundle notices (plural
  "Guidances", dozens of products per notice), not single-product PSG notices, which are each a
  genuine single new/revised draft guidance. One such item (Caprines anthelmintics, thread H-0023)
  was drawn by the systematic sample.

### Frame C — current/forward, `US-FDA-C-0001`…`US-FDA-C-0025`
- Population: same FR query, `publication_date` 2025-06-01..2026-04-30. Raw term match returned 92
  documents; same filter as above → **N=51**.
- Every one of the 51 population items was checked via a per-docket Federal Register search for a
  final-guidance notice. **None had a final guidance published as of 2026-09-25** (expected: FDA
  guidance finalization typically takes well over a year, and this window is the most recent ~10
  months). Consequently **Frame X (drafts already finalized before 2026-07-01) is empty — 0 threads**;
  there was nothing to route out of Frame C.
- Sample: **systematic**, step=2, start index 0, chronological order → 25 threads (population indices
  0, 2, 4, …, 48; item at index 50 excluded to keep the cap of 25).
- All 25 sampled threads are, by construction, "outcome not resolved before 2026-07-01" (no final at
  all, let alone one before that date), matching the frame's eligibility rule.
- `outcome_class`: `unresolved` if the anchor draft is <12 months old as of 2026-09-25 (15 threads),
  else `stalled_no_action` (10 threads, all ≥12 months old, drafts from 2025-06 through 2025-09).

## Outcome verification method
Decisive action = FR notice in the **same docket** whose abstract explicitly announces availability
of a **final** guidance, cross-checked for title match to the draft (all 23 Frame H positives contain
an explicit "This guidance finalizes the draft guidance ... issued on `<anchor_date>`" sentence naming
the exact anchor publication date, which is strong independent confirmation of the link). One thread
(H-0022, PFDD Guidance 3) had its final published under a *different* administrative docket than the
draft's own comment docket; found via a full-text FR title search rather than the docket search.
One thread (H-0023, VICH anthelmintics "Caprines") sits in a docket that bundles 8 different-species
anthelmintic guidances finalized the same day (2026-06-24); the Caprines-specific final was matched
by exact title, not just docket membership.

**FDA's own guidance-document search database** (`fda.gov/regulatory-information/search-fda-guidance-documents`,
named in the task brief as a supplementary check for finals not announced in the FR, and for
withdrawals) **could not be queried programmatically from this container.** Its results table is
populated client-side by a DataTables AJAX call to `/datatables-json/search-for-guidance.json`; every
attempt to fetch that endpoint (with a browser User-Agent, and again with Accept/X-Requested-With/
Referer headers matching a real AJAX request) returned an FDA WAF "FDA Internet Site Error" page
rather than data. The static page shell renders (200 OK) but the guidance table itself is empty
in server-rendered HTML. See `sources.json`. Practical effect: for the 7 Frame H negatives and all
25 Frame C threads, absence of a final/withdrawal is established via Federal Register search only
(both per-docket and broad full-text title search), not independently cross-checked against FDA's
own database. `label_confidence` on these `stalled_no_action`/`unresolved` outcome records is set to
**medium** (not high) specifically to flag this gap; `label_confidence` on the 23 positive (action)
outcomes is **high** (independently confirmed via the final notice's own cross-reference sentence).

Per the Director's schema clarification received during this run: `label_confidence` in every
`outcomes.jsonl` record now refers **only** to the action/timing label (whether and when a decisive
action or withdrawal occurred). A separate `content_label_confidence` field was added to every outcome
record for confidence in `content_direction`/`key_parameters` specifically; it is `high` where the
final's title and abstract are nearly verbatim-identical to the draft's (most positives), `medium`
where reworded but clearly the same topic, and `low` where the final's title/scope was substantially
broadened or consolidated with other pre-existing guidance content (only thread H-0016, Unique Device
Identification — the final's title folds in an existing "Compliance Dates" guidance alongside the
draft's own GUDID-database update). For all `stalled_no_action`/`unresolved`/`na`-direction outcomes,
`content_label_confidence` is `high` (trivially: "na" is certain when there was no action).

## Evidence
- E01 on every thread = the anchor draft-guidance-availability FR notice itself (tier B).
- Tier B extras added where cheaply available and genuinely pre-decisive/pre-anchor-topic-history:
  comment-period extension/reopening notices found in the same docket (H-0004 Homeopathic Drugs,
  C-0001 M13B ICH bioequivalence), and — for 6 Frame C GOLD_CANDIDATE threads whose docket carries a
  multi-year history — the immediately preceding final or draft guidance on the *same* topic in the
  *same* docket (C-0001 M13A predecessor final, C-0010 Safety Labeling Changes 2013 final, C-0012
  Expedited Programs 2019 final, C-0014 Biosimilarity 2015 final, C-0015 Medical Gases 2017 prior
  draft that was itself never finalized, C-0023 Biosimilar Q&As 2021 final). These are genuine
  historical FR documents published years before each thread's anchor date; the added evidence text
  is drawn from the original notice's own abstract only (an earlier attempt to add connective framing
  sentences referencing the 2025/2026 anchor was found by the validator's date-leakage lint to
  constitute forward-looking content inside a historical evidence item and was removed).
- Tier S stakeholder evidence: Federal Register's `regulations_dot_gov_info.comments_count` field
  (mirrors regulations.gov) was pulled for all 55 anchor notices. Where `comments_count > 0` **and**
  a `comments_close_on` date was present, one Tier S item was added with `publication_date =
  comments_close_on + 14 days` (skipped, per protocol, wherever the count was 0/absent — most Frame C
  items, since several comment periods are still open or only recently closed and regulations.gov
  had 0 recorded at the time FR last checked). 21 threads received a Tier S item this way (20 in
  Frame H, 1 in Frame C — Medical Gases CGMP, C-0015). One Frame H notice (Homeopathic Drugs, H-0004)
  drew an exceptional 50,970 public comments (a well-known high-salience rulemaking); kept as-is,
  correctly dated well before its 2022 decisive date.
- `regulations.gov`'s own v4 API (DEMO_KEY) was tried directly as a fallback/spot-check; it returned
  `OVER_RATE_LIMIT` on the first two attempts in this session and succeeded once after a delay. Not
  relied on at scale — the FR API's mirrored `regulations_dot_gov_info` field was used instead.
- CDER's annual "Guidance Agenda" (named in the task brief as a valuable Tier B
  `guidance_agenda_entry` precursor) and CDRH's A-list/B-list were **not used**. The CDER agenda
  landing page (`fda.gov/drugs/guidances-drugs/cder-guidance-agenda`) links only to the *current* PDF,
  which at time of check was itself dated "July 2026" — i.e. already a revision beyond the original
  January 2025/2026 issuance the task calls for — and `web.archive.org` is blocked from this
  container, so the original dateline could not be verified. Per task instruction ("If a guidance
  agenda's original date cannot be verified (page revised), skip it and note that"), these were
  skipped entirely rather than risk using post-hoc-revised content as if it were point-in-time.
- Evidence density: Frame H averages ~1.5 items/thread (29/30 threads have 1–2; one has 3). Frame C
  averages ~1.7 items/thread but is **uneven**: 19/25 threads have only the anchor (E01), 4 have 2
  items, and only **2/25 (C-0001, C-0015) reach the ≥3-item bar** that EXECUTOR_GUIDE's own
  `GOLD_CANDIDATE` definition calls for. This is a genuine data-availability constraint for very
  recent dockets (most are single-document dockets with comment periods still open, no extensions,
  no prior-version history, and FR-recorded comment counts of 0) rather than an under-effort gap —
  every avenue described in the task brief (extensions/reopenings, prior on-topic FR notices,
  regulations.gov comment counts, CDER/CDRH agendas, FDA's own guidance database) was attempted for
  every Frame C thread. **Flag for the Research Manager**: `quality_tier_proposed` is set to
  `GOLD_CANDIDATE` for all 25 Frame C threads per the task's explicit frame-level instruction, but only
  2 of them currently meet the full evidence-count/independent-verification bar; the other 23 should
  be treated as GOLD_CANDIDATE *in name/intended-tier* only until more evidence accrues (e.g. once
  comment periods close and regulations.gov comment counts populate) or should be down-tiered to
  RAPID for near-term backtest runs.

## Positives vs. negatives / finalization base rate
- Frame H (historical, 2019-07..2023-06 drafts, ≥3.2 years of run-out to the 2026-09-25 censor date):
  **23/30 positive (76.7%) finalized, 7/30 (23.3%) `stalled_no_action`** — no final or withdrawal
  found by exhaustive FR search. This is the closest thing this workstream has to an observed
  finalization base rate for FDA draft guidance and is noticeably higher than the ≥30% negative-control
  target in BACKTEST_PROTOCOL.md; the ratio is reported as-observed from a systematic draw of the real
  precursor population rather than forced toward 30%, per CLAUDE.md's instruction not to force quantity
  or ratio by relaxing evidence standards. The 7 negatives (H-0005, H-0007, H-0008, H-0021, H-0026,
  H-0028, H-0029) are drafts published Dec 2019 – Feb 2023, so all have had 3.5+ years to be finalized
  and have not been — genuine long-run stalls, not merely "not yet due."
- Frame C (forward, 2025-06..2026-04 drafts): **0/25 positive by design** (frame selects only
  not-yet-resolved threads) — 15 `unresolved` (<12 months old) and 10 `stalled_no_action` (≥12 months
  old, no action). These are intended as live/forward test threads plus a batch of "aging" negative
  controls, not a base-rate estimate (censoring makes the true eventual finalization rate for this
  cohort unknown until later re-labeling passes).
- Frame X: 0 threads (see above — no Frame C population item was already finalized before 2026-07-01).
- Combined dataset: 55 threads, 23 positive (`action_as_proposed` — all 23 are `as_proposed`, no
  softened/tightened/mixed/different_mechanism cases observed among Frame H finals; FDA guidance
  document text tends to carry the draft's substantive recommendations through to final with wording
  refinements rather than reversals), 32 no-action-to-date (17 `stalled_no_action` + 15 `unresolved`).

## Other problems / exclusions logged
- Batch product-specific-guidance bundle notices (plural "Guidances", e.g. "New and Revised Draft
  Product-Specific Guidances; Availability" covering dozens of drugs at once): excluded from both
  frames' populations (24 in Frame H's raw term match, 4 in Frame C's) — not a single coherent
  proposal.
- Comment-period extension/reopening notices and corrections: excluded from the population as
  candidate *anchors* (they are not a new/revised draft guidance) but several were kept as
  *evidence* items on the thread whose draft they extend/correct (see Evidence section).
- One raw-term false positive worth flagging explicitly: term search on `"draft guidance"
  "Availability"` also matches many FINAL guidance notices, because a final's own abstract routinely
  says "...finalizes the draft guidance...". All such items were excluded from both population and
  sample by inspecting each abstract, not just the title.
- Validator run: `python3 -m rpe.validate data/raw/us_fda` → **0 errors**, 7 warnings, all reviewed
  and judged benign / expected: (1) three threads/evidence items legitimately reference an
  already-public multi-year program or regulation's own dates that predate or are independent of the
  guidance's own future outcome (H-0025's GDUFA III "Fiscal Years 2023-2027" commitment letter;
  C-0013/C-0015's references to the QMSR regulation's already-fixed February 2026 effective date, a
  pre-existing regulatory fact, not this draft's own outcome); (2) one false-positive date match
  where the lint's year-regex matched the trailing digits of a docket number ("FDA-2020-D-2099") as
  if it were the year "2099" in evidence H-0014-E02.
- FDA guidance-document search database and CDER/CDRH guidance agendas: both attempted and both
  unusable from this container for the reasons above (WAF block; unverifiable original dates on a
  continuously-revised page respectively) — logged in `sources.json`, not silently skipped.
