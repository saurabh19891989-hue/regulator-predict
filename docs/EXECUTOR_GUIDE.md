# EXECUTOR_GUIDE.md — How to reconstruct a regulatory thread (RAPID / GOLD)

Read this in full before collecting anything. It is binding for every executor agent.
Schemas: `schemas/*.schema.json`. Validator: `python3 -m rpe.validate data/raw/<workstream>`.

## 1. Output location (one directory per workstream; never write elsewhere)
```
data/raw/<workstream>/threads.jsonl     one thread record per line
data/raw/<workstream>/evidence.jsonl    one evidence item per line (Tier B, C, S, D only — NEVER Tier A)
data/raw/<workstream>/outcomes.jsonl    one outcome record per thread (Tier A / resolution)
data/raw/<workstream>/sources.json      source-registry entries (endpoints/listing pages + access method)
data/raw/<workstream>/NOTES.md          sampling frame, method, problems, excluded candidates and why
data/raw/<workstream>/cache/            optional downloaded copies (gitignored)
```
Do NOT run git. Do NOT edit files outside your workstream directory.

## 2. Sampling — the most important rule
Sample from the **precursor population**, never from outcomes. Pick a listing of precursors
(consultation papers, discussion papers, exposure drafts, draft directions, NPRMs, draft guidances)
over a stated date window, and take **every** item (census) or a **systematic** sample (every k-th) in
listing order. Record the frame and method in `threads.jsonl` and `NOTES.md`.
- Do not skip a precursor because nothing happened afterwards — stalled/withdrawn/no-action threads
  are REQUIRED controls (target ≥30%). Skipping is allowed only for documented reasons unrelated to
  outcome (e.g., precursor is a pure corrigendum, or it is not a policy proposal at all). Log every skip
  with the reason in NOTES.md.
- One thread = one coherent policy proposal. If one paper bundles unrelated proposals, use the primary one.

## 3. Thread record (`threads.jsonl`)
```json
{"thread_id": "IN-SEBI-0007", "workstream": "in_sebi", "regulator": "SEBI", "jurisdiction": "IN",
 "neutral_title": "SEBI proposal on <subject>",
 "issue_summary_neutral": "2–4 sentences describing ONLY what the anchor precursor proposed, written as of its date.",
 "process_type": "consultation_to_regulation",
 "anchor_evidence_id": "IN-SEBI-0007-E01", "anchor_date": "2023-01-17",
 "sampling_frame": "SEBI consultation papers listing, 2022-07-01..2023-06-30", "sampling_method": "census",
 "quality_tier_proposed": "RAPID", "created_by": "<agent>", "notes": ""}
```
- `neutral_title` / `issue_summary_neutral` MUST NOT reveal or hint at the outcome. Forbidden: "final",
  "adopted", "approved", "notified", "withdrawn", "shelved", "later", "eventually", "which led to", outcome
  dates, final-regulation names. Phrase as the proposal: "Proposal to …", "Consultation on …".
- `process_type` ∈ `nprm_to_final`, `consultation_to_regulation`, `draft_direction_to_final`,
  `exposure_draft_to_regulation`, `consultation_to_recommendation`, `draft_guidance_to_final`,
  `investigation_to_duty`, `other`.

## 4. Evidence item (`evidence.jsonl`) — Tier B / C / S / D only
```json
{"evidence_id": "IN-SEBI-0007-E03", "thread_id": "IN-SEBI-0007", "regulator": "SEBI", "jurisdiction": "IN",
 "title": "…exact document title…", "source_url": "https://…",
 "publication_date": "2023-02-10", "first_known_date": null, "retrieval_date": "2026-09-25",
 "document_type": "speech", "tier": "C",
 "original_or_revised": "original", "version_confidence": "high",
 "date_verification": "Date printed on PDF dateline and matches listing page date",
 "extracted_claims": ["Chairperson said SEBI is examining …"],
 "content_excerpt": "verbatim passage(s) from the document, ≤1200 chars, the part relevant to this thread",
 "source_hash": "sha256 of the downloaded bytes or null", "stored_copy": null}
```
Tiers (see CLAUDE.md):
- **B** official forward material: consultation/discussion papers, draft rules/directions/regulations, exposure
  drafts, NPRM/ANPRM/SNPRM, comment-period extensions/reopenings, hearings, board/committee agendas,
  regulatory agenda entries, OIRA "received for review" records, working-group reports that recommend action.
- **C** official soft signals: speeches, minutes, annual reports/workplans, FAQs, staff papers, supervisory
  letters, official interviews, official statements of intent (e.g., RBI "Statement on Developmental and
  Regulatory Policies"), testimony, press releases that are not the decisive action.
- **S** stakeholder responses: published comment letters, industry-association submissions, comment counts.
- **D** reputable contemporaneous news (Economic Times, Mint, Business Standard, Moneycontrol, Reuters,
  Bloomberg, Hindu BusinessLine, FT, WSJ, trade press). Use headline + date + short snippet only.
- **Tier A** (the decisive final action, a withdrawal notice, or anything published on/after the decisive date that
  describes the outcome) goes ONLY into `outcomes.jsonl`, never into evidence.

Point-in-time rules (NO HINDSIGHT LEAKAGE):
1. `publication_date` is the date the item was first public. Verify it (PDF dateline, listing date, press
   release number, FR official date). Explain in `date_verification`. If you cannot verify, set
   `version_confidence: "low"` and say why.
2. `extracted_claims` and `content_excerpt` must contain ONLY what the document itself said at that date. Quote
   or closely paraphrase. Never add context you know from later ("this was later adopted", "the final rule…").
   Never mention any date later than `publication_date`.
3. Current web pages may have been revised. If a page shows "last updated" after the publication date, or
   contains links/sidebars to later material, excerpt only the original dated content and set
   `original_or_revised: "unknown"` unless you can show it is original.
4. For news (Tier D) prefer Google News RSS with date operators, which gives the index date and headline:
   `https://news.google.com/rss/search?q=<terms>+after:YYYY-MM-DD+before:YYYY-MM-DD&hl=en-IN&gl=IN&ceid=IN:en`
   (use `hl=en-US&gl=US&ceid=US:en` for US). Use the RSS `<title>`, `<pubDate>` and `<source>`; do NOT excerpt
   the live article body (it may have been updated). Discard any headline that reports the final outcome.
5. The anchor precursor itself is evidence item E01 of the thread (tier B).
6. Do not include items that are near-duplicates of each other (e.g., five outlets repeating one PTI story):
   keep one and note the duplicates in NOTES.md.

## 5. Outcome record (`outcomes.jsonl`) — the sealed label
```json
{"thread_id": "IN-SEBI-0007",
 "outcome_class": "action_softened",
 "decisive_action": true, "decisive_date": "2023-06-28",
 "decisive_document_title": "…", "decisive_document_url": "https://…", "decisive_document_type": "board_meeting_press_release",
 "withdrawal_date": null, "censor_date": "2026-09-25",
 "content_direction": "softened",
 "content_summary": "What the decisive action actually did: mechanism, scope, key numbers, compliance dates.",
 "key_parameters": [{"name": "threshold", "proposed": "INR 100 crore", "final": "INR 250 crore"}],
 "outcome_sources": ["https://…"], "label_confidence": "high", "labeled_by": "<agent>", "notes": ""}
```
- **Decisive action** = the FIRST official publication that adopts the proposal (at least in substantial part):
  final rule / regulation notification / circular / master direction / board-meeting press release approving it /
  TRAI recommendations released / final guidance / customs duty notification. `decisive_date` = its date.
- `outcome_class` ∈ `action_as_proposed`, `action_softened`, `action_tightened`, `action_mixed`,
  `withdrawn` (formally withdrawn/abandoned), `stalled_no_action` (no decisive action by censor date),
  `unresolved` (proposal still formally live and recent — treated as no-action to date).
- `content_direction` (relative to the anchor proposal) ∈ `as_proposed`, `softened`, `tightened`, `mixed`,
  `different_mechanism`, `na` (use `na` when there is no action).
- `censor_date` = the date you verified the outcome (today: 2026-09-25).
- `label_confidence` refers ONLY to the action label (whether/when the decisive action or withdrawal happened).
  Put confidence in content_direction/key_parameters in a separate field `content_label_confidence`
  (high|medium|low). Never lower `label_confidence` because content is uncertain.
- If you cannot determine the action outcome with at least medium confidence, keep the thread but set
  `label_confidence: "low"` and explain in `notes` — do not guess (low-confidence threads are excluded).

## 6. Source registry (`sources.json`)
```json
[{"regulator": "SEBI", "endpoint": "https://www.sebi.gov.in/…", "content": "consultation papers listing",
  "tier": "B", "access_method": "HTML listing, paginated POST", "date_field": "listing date",
  "reliability_notes": "…", "checked": "2026-09-25"}]
```

## 7. Quality tiers
- `RAPID`: anchor + outcome verified; dates reasonably verified; ≥1 evidence item (the anchor).
  Add Tier C / D / S items when cheaply findable (aim for 2–6 items total per thread).
- `GOLD_CANDIDATE`: all evidence dates independently verified from the primary document itself (dateline,
  gazette/FR citation, numbered press release), original versions, ≥3 evidence items with at least one item
  besides the anchor published before the decisive date, outcome label confidence high.

## 8. Access notes (verified 2026-09-25 from this container)
Reachable: sebi.gov.in, rbi.org.in, irdai.gov.in, trai.gov.in, dgtr.gov.in, federalregister.gov API,
reginfo.gov, regulations.gov (DEMO_KEY, rate-limited), fda.gov (send a browser User-Agent), news.google.com RSS.
Blocked: web.archive.org (connection reset), egazette.gov.in, cbic.gov.in, nppaindia.nic.in. Do not retry
blocked hosts more than twice. Use `curl -sSL -m 40 -A "Mozilla/5.0"`; PDFs → `python3 -c` with pdfminer.six.

## 9. Before you finish
Run `python3 -m rpe.validate data/raw/<workstream>` and fix every error. Write NOTES.md with: frame, window,
method, count of candidates seen, included, skipped (+reasons), positives vs negatives, known weaknesses.
