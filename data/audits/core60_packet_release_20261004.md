# Core60 packet prerelease audit — 2026-10-04

**Release verdict: PASS for blind RAPID inference. No blocking packet fixes found.** This is a packet-release decision, not certification of forecast accuracy, exact outcome timing, GOLD quality, or downstream scoring. No forecasts had been produced at audit time.

## Frozen scope and counts

Read `CLAUDE.md`, `data/forecasts/cohort_60_20261004.json`, `data/snapshots/freeze_20261004.json`, both run manifests, all archived inbox packets, the canonical index/threads/evidence/outcomes, the packet renderer and snapshot selection logic, and the source audits listed below. Checks used read-only Python scripts with bytecode writing disabled when importing project modules. Only this report was written.

| Run | Design | Packets | Distinct forecasts | Aliases | Logical arm rows | Matters |
|---|---|---:|---:|---:|---:|---:|
| ASTRA_CORE60 | T, offsets 180/90/30/7 days | 20 | 380 | 380 | 760 | 60 |
| ASTRA_CAL60 | C, frozen calendar checkpoints | 18 | 298 | 298 | 596 | 45 |
| Total | | 38 | 678 | 678 | 1,356 | 60 distinct |

Manifest batch limit is 20. CORE batch sizes are eighteen of 20, one of 19 and one of 1; CAL has fourteen of 20, one of 12, one of 4 and two of 1. Each batch contains at most one snapshot per matter. CAL's 15 omitted SEBI matters have no eligible calendar checkpoint in the frozen index; this is not a missing-packet defect. Do not describe CAL as having observations on all 60 matters.

The cohort contains all 30 SEBI-R and all 30 FDA-H selected matters, all audited RAPID, zero GOLD. There are **61 retained distinct evidence records, all Tier B**, not exactly one per matter: FDA H-0004 also retains the independently audited comment-period extension E02. The other 59 matters have one retained item each.

## Exhaustive mechanical results

- All four canonical data-file SHA-256 values match the freeze and both manifests. The snapshot-index hash is `fa378d0c9c8981ce6d4a59ded4a22951ed5efd737b5a2561110ba1858be6e2a7`.
- All 38 archived packet byte hashes match their manifest hashes. All 38 external dispatch copies also exist and match those same hashes.
- Every packet's ordered snapshot IDs match its batch manifest. There are no duplicate forecast IDs, no overlap between direct IDs and alias keys, and no alias pointing outside the direct forecast set.
- All 678 aliases match their target's matter, cutoff, evidence IDs, design and offset. Different arm names do not create additional independent forecasts: ALL, B_ONLY and B_PLUS_C have identical evidence in this cohort.
- Direct IDs plus aliases exactly equal the eligible frozen-index selection for each run's cohort, arms, design and offsets: 760 T rows and 596 C rows, with no missing or extra IDs.
- Independently checked all 1,356 logical rows against retained evidence: each shown item belongs to the same matter and is available no later than the cutoff using `max(publication_date, first_known_date)`; eligible items are not silently omitted. TITLE_ONLY rows correctly contain no evidence. All cutoffs are on/after the matter anchor, on/before the fixed censor and before a recorded decisive action.
- Each packet exactly equals the reviewed common header plus the permitted rendering of its selected canonical records. This checks every rendered field and byte, not a sample of packet pages. All 61 distinct evidence records and all 60 neutral matter titles were reviewed once; repeated renderings were checked programmatically.
- Internal thread/evidence IDs, arm names, T offsets, target anchors, pseudo-anchor flags, outcome dates/classes, sampling metadata and label fields are absent from the packet text. Opaque snapshot IDs and local E1/E2 citations are the intended visible identifiers. No ISO date after a snapshot cutoff occurs in its rendered text.
- All 38 dispatch output files contain only `{"status": "PENDING_FORECAST"}`. Neither archived run has output files, and neither run appears in the forecast ledger or raw forecast store.

## Content, source linkage and scope

The neutral headers describe consultations or draft guidance and do not announce eventual adoption, delay or finalization. The common header explicitly prohibits later-known facts and specific remembered outcomes, requires recognition disclosure, and treats future plans as uncertain. The output schema's outcome categories are requested predictions, not supplied labels.

SEBI's endpoint remains the first official publication adopting the original proposal at least substantially, including an adopting board release; it is not silently delayed to implementation. FDA's endpoint remains publication of the final version of the particular guidance. Matter headers retain the original scope: for example, SEBI R-0019 identifies the historical-price stress-testing topic, and FDA H-0016 identifies its GUDID update. Original evidence may discuss adjacent components; it does not disclose their later disposition.

Reviewed mentions of existing circulars, prior guidance, withdrawn earlier drafts and already-made procedural decisions are contemporaneous precursor context. Examples include SEBI's existing intraday-borrowing framework and planned deferred applicability, FDA H-0014's withdrawal of the earlier 2015 draft concurrent with the new draft, and H-0024's proposed replacement of 2016 guidance. These do not assert the sampled proposal's future outcome. Future dates expressed as plans/deadlines remain plans, not later-known facts.

Source-audit coverage is 60/60: 11 SEBI controls in `audit_india_controls_20261004.jsonl`, 19 SEBI actions in `audit_india_late_20261004.jsonl`, 9 FDA-H matters in `audit_us_fda_stratified_20260927.jsonl`, and 21 FDA-H matters in `audit_fda_h_completion_20261004.jsonl`. Read the accompanying India controls/action and FDA completion reports. FDA's prior verified-evidence list expressly includes H-0004-E02. Retained sources are the audited official consultation PDFs/notices; unsupported news and synthetic historical comment counts are absent. This release audit relies on that completed source work and does not claim a new web reopening or cryptographic certification of original source PDFs.

## Limitations that must accompany use

1. **FDA timing is conditional and medium confidence:** dates are first verified public finalization notices, not proven first FDA PDF uploads. Some canonical FDA action records still carry high `label_confidence`; that must not override the explicit report/manifest timing limitation or be described as exact first-upload verification.
2. **SEBI controls are medium-confidence bounded absence checks.** Title-index and board-release searches cannot exclude a differently titled implementation. Unresolved does not mean permanent no action. FDA controls also remain medium confidence; the earlier audit's H-0005/H-0007/H-0008/H-0021 bounded FR reruns encountered HTTP 429, with current official draft status only corroborating absence.
3. No GOLD cases and no Tier C evidence. B_ONLY, B_PLUS_C and ALL are aliases of identical inputs, so this cohort cannot establish Tier C/news/stakeholder lift. The meaningful available input comparison is evidence versus TITLE_ONLY, with within-matter dependence respected.
4. FDA notice-level comparisons support broad mechanism direction, not exact parameter equality. SEBI R-0026's low-confidence content disposition remains unsuitable for confident detailed content scoring. Packet release does not resolve evaluator or outcome-label consistency questions.
5. T cutoffs are selected relative to actual or pseudo outcomes; C has its separate visible, unresolved checkpoint eligibility and covers 45 matters. Keep these designs distinct in reporting. Preserve censoring at 2026-09-24 and the existing exclusion of prior technical smoke outputs from headline estimates.
6. Official pages/PDFs are source audited but not proven immutable historical versions. Visible matter identities can trigger model memory; the recognition flag and prohibition are safeguards, not proof that memorization is absent. Release applies to these frozen bytes under isolated packet-only forecasting; outputs still require their own leakage audit.

**Disposition:** release both frozen runs for inference with the above limitations intact. No source, evaluator, manifest, packet, or forecast edits were made by this audit.
