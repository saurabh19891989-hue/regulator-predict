# US–FR public availability date repair — scope and limits

Audit basis: preserved `data/raw/us_fr` rows (179 threads, 421 evidence rows, 111 action outcomes, 4 withdrawals), with the outcome censor date held at **2026-09-24**. No raw row or canonical store was edited; no index was rebuilt. The reproducible collector is `tools/us_fr_pi_provenance.py`. Its outputs are `us_fr_pi_provenance_2026-09-27.jsonl`, `patches/us_fr_public_availability_2026-09-27.jsonl`, and the per-thread `us_fr_date_scope_2026-09-27.jsonl`.

## Coverage and patch semantics

- 374 unique Federal Register document numbers appeared in evidence source URLs or outcome URLs. The official `/api/v1/public-inspection-documents/{document_number}.json` endpoint returned `filed_at` for 371. The provenance JSONL records the endpoint, Eastern-time timestamp, print `publication_date`, filing type, linked IDs, retrieval time, and response SHA-256. All 371 successful PI dates precede print publication by 1–13 calendar days.
- Three related evidence documents have no PI API record (404): `2010-13877` and `2010-17966` in `US-FR-H-0027`, and `2011-17995` in `US-FR-H-0054`. Their existing dates were left in place and those two threads are flagged as mixed PI/print-date sensitivity.
- The patch has **627** schema-allowed operations: `publication_date` and `first_known_date` for each of 256 FR evidence rows (512 operations), `decisive_date` for 111 actions, and `withdrawal_date` for 4 withdrawals. It leaves 158 synthetic comment-count rows to the separate `us_fr_synthetic_comment_counts_2026-09-25.jsonl` drop patch. It does not change censor dates. `rpe.build` derives each thread's `anchor_date` from its patched anchor evidence row when a future, separately versioned rebuild is authorized.
- A PI `filed_at` date is an **upper bound on earliest official public availability**, not proof that it was the first agency publication. For PI-only outcomes the patched `decisive_date` is the latest documented first-public-adoption date pending an agency release search. The same limit applies to evidence. The patch uses `publication_date` as the project packet's effective availability date, so the original print publication date remains recoverable from the provenance file. Existing raw `date_verification` prose still describes print dates and should not be read as validating the patched date.

## Earlier agency releases confirmed

| Thread / item | Earlier documented public date | Basis | PI / print |
|---|---:|---|---|
| `US-FR-H-0002-E01` EPA proposal | 2019-06-25 | [Dated EPA announcement](https://www.epa.gov/newsreleases/reducing-regulatory-burdens-epas-proposal-levels-playing-field-sources-reduce) | PI 2019-07-25 / print 2019-07-26 |
| `US-FR-H-0002` EPA final action | 2020-10-01 | [Dated EPA finalization announcement](https://www.epa.gov/newsreleases/epa-encourages-innovation-levels-playing-field-sources-are-reducing-hazardous-air) | PI 2020-11-10 / print 2020-11-19 |
| `US-FR-C-0018-E01` EPA WOTUS proposal | 2025-11-17 | [Dated EPA proposal announcement](https://www.epa.gov/newsreleases/epa-army-corps-unveil-clear-durable-wotus-proposal) | PI 2025-11-19 / print 2025-11-20 |
| `US-FR-C-0018-E02` EPA WOTUS supplement | 2026-09-04 | [Dated EPA supplement announcement](https://www.epa.gov/newsreleases/epa-and-army-seek-additional-input-proposed-waters-us-definition-while-advancing), with [prepublication text linked by EPA](https://www.epa.gov/wotus/updated-definition-waters-united-states) | PI 2026-09-08 / print 2026-09-09 |

For `US-FR-H-0002`, the earlier EPA press release is strong evidence of public action on October 1, but the date correction alone does not verify that every claim extracted from the later FR proposal was available in the June 25 release. Recheck the packet text against contemporaneous material before treating that smoke-test thread as clean. The 2018 EPA guidance on the same policy is a separate precursor and also warrants a content/selection audit; it is not treated as adoption of this final rule.

`US-FR-H-0010` is a **withdrawal**, not a positive adoption: [SSA's regulation listing](https://www.ssa.gov/regulations/recentregulatory.html) labels the withdrawal July 28, 2021; FR PI filed it July 27 at 08:45 ET. The patch moves `withdrawal_date` to July 27. No earlier public SSA withdrawal announcement was established in this targeted check.

## Six sampled C threads

| Thread | Anchor availability patched to | Other documented correction | Earlier agency-date review |
|---|---:|---|---|
| `US-FR-C-0004` | 2025-06-30 PI | Extension 2025-07-21 PI | MSHA listing checked in prior audit; no earlier dated release established. |
| `US-FR-C-0005` | 2025-06-30 PI | Extension 2025-09-02 PI; final 2026-08-20 PI | Targeted DOL/OFCCP check found no earlier dated finalization release. |
| `US-FR-C-0014` | 2025-08-27 PI | Final 2026-07-16 PI | Targeted DHS search found no earlier dated release. |
| `US-FR-C-0018` | 2025-11-17 EPA | Supplement 2026-09-04 EPA | Both dated EPA releases confirmed above. |
| `US-FR-C-0044` | 2026-04-13 PI | Final 2026-08-13 PI | Targeted OPM search found no earlier dated release. The separate audit's content-direction correction is outside this date patch. |
| `US-FR-C-0047` | 2026-04-29 PI | Extension 2026-05-27 PI | [AbilityOne news listing](https://www.abilityone.gov/media_room/news_events.html) dates its announcements April 30 and May 28; no earlier dated release established. |

The targeted searches are **not exhaustive negative evidence**. In particular, an earlier agency posting could predate PI for any of the other five sampled threads.

## Permissible analysis scope

`us_fr_date_scope_2026-09-27.jsonl` flags 177 threads with complete PI coverage as usable for a **PI-bound date sensitivity only after a new versioned build and snapshot index**. The two threads with 404 related documents need a mixed PI/print stratum or exclusion from that sensitivity. All 179 retain `needs_full_earliest_agency_date_audit=true`; none becomes GOLD through this repair. Positive event-time claims need an earliest-agency-release audit for all 111 actions (with `US-FR-H-0002` already showing a 40-day gap from PI), and outcome/source linkage and content-direction issues remain separate audit gates. The 4 withdrawals likewise need a first-public-withdrawal check for definitive timing.

The existing frozen index and any completed forecasts refer to the prior date version. Applying these patches would move anchor/outcome dates and change eligible cutoffs, so use a new indexed sensitivity run with explicit provenance. Do not silently reinterpret the old run or relax the **2026-09-24** censor date.
