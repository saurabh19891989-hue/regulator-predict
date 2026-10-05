# Leakage and label audit

## Run disposition

| Run | Disposition | Reason |
|---|---|---|
| SMOKE1 | Diagnostic only | Expressed future political knowledge; index drift documented in FINDING-001/002 |
| ASTRA_SMOKE2 | Invalidated for empirical smoke gate | RBI H0021 false no-action label/pseudo-anchor; US/FDA first-public dates under repair |
| ASTRA_MASK_SMOKE2_SMALL | Invalidated | Exact identities/titles remained in masked packet |
| ASTRA_MASK_SMOKE3 | Invalidated for empirical smoke gate | Same RBI false-control issue; residual recognition and loss of topic information |
| ASTRA_SMOKE4 | Technical pass; headline excluded | Repaired source freeze;14/24 recognised; regulator/action confounding |
| ASTRA_MASK_SMOKE4 | Invalidated masking comparison | Masked action endpoint changed; preserved without ingestion |
| ASTRA_MASK_SMOKE5 | Technical pass; headline excluded | Endpoint repaired;4/8 recognised; masking information loss remains |

All raw forecasts remain preserved. SMOKE2/MASK2/MASK3 were invalidated before ledger ingestion and headline evaluation.
The first GPT primary run had 24 distinct outputs plus 16 aliases; six distinct outputs self-reported recognition.
The repaired masked diagnostic had eight outputs, two recognised. Independent rationale review found no expressed
post-cutoff political facts or invalid citations, but that does not cure source/label failures.

## Source findings being repaired

- US-FR: 158 comment-count items were assigned comment-close +14 days although the count was observed later.
  Drop patches preserve raw data. Such Tier-S items did not enter the B/B+C smoke packets.
- US-FR: print dates are later than public-inspection dates; agency releases can be earlier still. NARA explains
  [public inspection](https://www.archives.gov/federal-register/public-inspection/about.html). PI dates prove the
  document was public by that date, not that no earlier agency announcement existed. Use earliest verified official
  adoption for the target; retain print and PI dates as provenance/sensitivity metadata.
- India: the first review found RBI H0011/H0021 falsely stalled; further control screening is finding more adopted
  proposals. Correct labels and sealed source metadata, and rebuild pseudo-anchors before new forecasts.
- FDA: 21 count items have the same provenance problem; sampled final-guidance notices precede recorded FR print dates.

No source audit finding is interpreted as a predictive result. Pending or contaminated-rebuild verdicts are never GOLD.
The fixed censor boundary remains 2026-09-24 despite the resumed audit date of 2026-09-27.

## Scaled60 acceptance — 2026-10-05

All678 distinct outputs across38 fresh Astra sessions received independent text/citation review.
Zero observable contamination findings;64 self-recognition disclosures (9.44%). Hidden memory remains
unverifiable. Unsupported conditional numeric guesses in the bounded reviews are retained unchanged;
parameter coverage is unassessed. See data/audits/scaled60_full_acceptance_20261005.json for exact coverage.
Execution preflight passed all source/packet/event/output hashes, unique sessions, disabled-tool logs and
canonical schema/coherence checks; no coherence repairs needed. All1,356 scaled logical rows were ingested
serially. Ledger verification passes1,464 records including108 old diagnostics, excluded from scoring.
Zero GOLD; a clean visible-output audit does not establish immutable historical source versions.
