# AUDIT_GUIDE.md — Leakage red-team protocol (RP0-08)

Auditors (Opus 5.5, high effort) try to INVALIDATE threads. They may read everything, including outcomes.
They never edit `data/raw/**`. Findings go to `data/audits/audit_<batch>.jsonl` (schema `schemas/audit.schema.json`),
fixes go to `data/audits/patches/<batch>.jsonl`, which `rpe.build` applies on top of executor data.

## Per thread, check
1. **Outcome label (most important).** Independently verify from the primary source that the decisive action is the
   FIRST official adoption and that its date is right. If an EARLIER adopting publication exists (e.g. a board
   approval press release before the circular), the decisive date must move earlier — and every evidence item on or
   after the corrected date becomes post-outcome leakage (patch: `set_outcome` + `drop_evidence`). Check that
   no-action threads really had no adoption by 2026-09-24 (search regulator listings + news).
2. **Evidence dates.** Re-open each item's source; confirm the publication date from the document itself (dateline,
   FR citation, numbered press release, RSS pubDate). Flag pages showing "last updated" after the publication date,
   revised PDFs, or listings whose date differs from the document.
3. **Content leakage.** `extracted_claims` / `content_excerpt` must reflect only what the document said at its date.
   Flag retrospective wording, knowledge of later events, references to later documents, and executor paraphrase that
   adds hindsight. For Tier D, flag headlines that report or strongly imply the final decision.
4. **Title/summary leakage.** `neutral_title` and `issue_summary_neutral` must not hint at the outcome.
5. **Selection.** Was the thread in the stated sampling frame? Any sign the executor skipped outcome-inconvenient items?
6. **Duplicates / tiers.** Near-duplicate items; mis-tiered items (a decisive document mislabelled as B/C).

## Verdicts
`clean` · `minor_issue_fixed` (patch written; snapshot validity restored) · `contaminated_rebuild` (fixable with
larger patch — write it) · `contaminated_exclude` (cannot be repaired; thread excluded) · `unverifiable`
(primary sources unreachable; thread stays RAPID, never GOLD).

## Patch file format (one JSON per line)
```json
{"op": "set_evidence", "evidence_id": "…", "field": "publication_date", "value": "2023-02-10", "reason": "…"}
{"op": "drop_evidence", "evidence_id": "…", "reason": "published after corrected decisive date"}
{"op": "set_outcome", "thread_id": "…", "field": "decisive_date", "value": "2023-03-29", "reason": "…"}
{"op": "set_thread", "thread_id": "…", "field": "neutral_title", "value": "…", "reason": "…"}
{"op": "exclude_thread", "thread_id": "…", "reason": "…"}
```
Allowed fields: evidence {publication_date, first_known_date, extracted_claims, content_excerpt, tier, title,
original_or_revised, version_confidence}; outcome {decisive_date, decisive_action, outcome_class, withdrawal_date,
content_direction, content_label_confidence, label_confidence}; thread {neutral_title, issue_summary_neutral}.

## Audit record
```json
{"audit_id": "AUD-<batch>-<n>", "thread_id": "…", "scope": "thread", "verdict": "clean",
 "findings": [{"check": "outcome_label|evidence_date|content_leakage|title_leakage|selection|duplicate|tier",
               "evidence_id": null, "severity": "info|minor|major", "detail": "…", "patched": false}],
 "auditor": "opus-5.5 leakage auditor", "audit_date": "2026-09-25",
 "gold_eligible": true, "gold_reason": "all dates verified from primary documents; outcome independently confirmed"}
```
`gold_eligible` requires: verdict clean/minor_issue_fixed, every evidence date verified from a primary document,
outcome independently confirmed.
