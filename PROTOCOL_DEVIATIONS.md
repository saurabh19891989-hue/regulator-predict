# PROTOCOL_DEVIATIONS.md — timestamped changes to the frozen plan

`docs/PREREGISTRATION.md` stays frozen (commit 6841b87, 2026-09-25 12:03 UTC). Every methodological change
after that point is recorded here with a UTC timestamp and a statement of whether any forecast or result
existed when the change was made. Entries are append-only.

| id | UTC timestamp | forecasts existing? | results seen? |
|---|---|---|---|
| DEV-001 … DEV-007 | 2026-09-25 12:20 | 0 (no ledger) | none |

## DEV-001 — `sampling_origin` on every thread; primary results exclude backfill
Every thread carries `sampling_origin` ∈ {precursor_population, outcome_backfill, purposive}. It is set by the
executor, or derived by `rpe.build` from `sampling_method` (census/systematic/random → precursor_population, else
purposive). **Primary results use precursor_population threads only**; the others are reported separately.
Reason: director instruction; guards against outcome-selected samples.

## DEV-002 — "CLEAN" renamed "LATE"; no claim of a guaranteed-clean holdout
The stratum of threads whose resolution is on/after 2026-07-01 (or unresolved) is called **LATE**. It lies after the
forecaster model's *stated* knowledge cutoff (June 2026), but that cutoff is not independently guaranteed, so LATE
results are described as "post-stated-cutoff", never as a clean holdout. Snapshot flag renamed
`post_cutoff_snapshot`.

## DEV-003 — Entity/title-masked anti-memorisation test
New arm `MASKED_B_PLUS_C`: same evidence as B_PLUS_C, but the title is withheld, the regulator is replaced by a generic
description ("a US federal regulator"/"an Indian regulator"), document titles and source domains are withheld, and
RINs, docket ids, FR/CFR citations, URLs, quoted titles and regulator names/abbreviations are masked in the text.
Run on the GOLD sample (and informative subsets) against unmasked B_PLUS_C with the same model. A large accuracy drop
under masking indicates reliance on identity/memory rather than on evidence (caveat: masking also removes some
legitimate context, e.g. regulator-specific base rates).

## DEV-004 — Design C (calendar-forward) replaces Design K and becomes the headline live-discovery design
At fixed calendar checkpoints (1 Jan and 1 Jul of 2019–2026, plus 2026-06-26, 2026-07-26, 2026-08-25), every sampled
thread that is visible (anchor ≤ checkpoint) and unresolved is forecast for progress within 7/30/60/90/180 days.
Threads are monitored at checkpoints up to 730 days after their anchor (cap for cost; very old stalled threads are
not monitored forever). Horizons beyond the censor date (2026-09-24) are censored. Design T (outcome-anchored) is
retained for lead-time measurement only. Prereg §2's Design K is subsumed by Design C's post-cutoff checkpoints.

## DEV-005 — Primary arm and ablation scope (cost control)
Broad backtest: **B_ONLY and B_PLUS_C** (Opus 5.5) on all precursor-population threads; primary action metrics use
B_PLUS_C (= B_ONLY where no tier C exists, scored once via packet aliasing). Prereg §3 named `ALL` as primary; it is
now run only on GOLD / informative subsets together with the stakeholder, news, latest-only and masked arms.
TITLE_ONLY control on a subset. Reason: director instruction to control cost and prioritise B vs B+C.

## DEV-006 — Smoke test before scaling
10 threads (~5 progressing, ~5 stalled/no-action), B_ONLY vs B_PLUS_C at T-90 and T-30, Opus 5.5, manually inspected
for leakage and coherence before any scaled run. Smoke-test forecasts are kept in the ledger (run `SMOKE1`) but
excluded from headline metrics.

## DEV-007 — Baselines emphasised
The evaluator's comparators are regulator/process-stage historical base rates computed with thread-grouped CV
(workstream × elapsed-time bucket; workstream × visible process stage) plus the heuristic and logistic feature model.
The LLM must beat the best of these. Where available, an external US Federal Register population base-rate table
(significant NPRMs outside the test window) is added as a further comparator.

## FINDING-001 — Macro-political hindsight in forecaster rationales (smoke test SMOKE1, 2026-09-25 12:29 UTC)
Recorded after SMOKE1 results were seen. At cutoffs before the 5 Nov 2024 US election (2024-10-07, 2024-10-17) the
forecaster (Opus 5.5) reasoned that a "Jan 2025 administration change likely halts or reverses" rules. Packets were
clean; the leakage came from the model's world knowledge. Not yet remediated. Proposed DEV-008 (not implemented):
explicit packet rule forbidding post-cutoff world events + rationale audit + sensitivity excluding flagged snapshots.

## FINDING-002 — Snapshot/pseudo-anchor instability across rebuilds (2026-09-25 12:34 UTC)
Collectors rebuilt data after SMOKE1 and the positive-gap pool changed, so 36 of 60 SMOKE1 ledger records no longer
match the rebuilt index. SMOKE1-era rows preserved in `data/forecasts/runs/SMOKE1_index_rows.jsonl` (recovered from
commit bdbaf2a). Required before any scaled run: freeze and commit the snapshot index (DEV-009, not implemented).

## PAUSE — 2026-09-25 ~12:35 UTC
Programme paused on user instruction (Anthropic credit nearly exhausted; move to GPT-6 Astra). No further forecasts.

## DEV-008 — GPT-6 Astra cutoff and post-cutoff world-knowledge guard (2026-09-25 13:21 UTC)
Recorded after the 60 SMOKE1 ledger records and FINDING-001/002 were known, before any GPT forecast or new result.
[Official OpenAI documentation](https://developers.openai.com/api/docs/models/gpt-6-astra) states GPT-6 Astra's
knowledge cutoff is 2026-04-30. For this forecaster, LATE thread outcomes begin 2026-05-01, and the stricter
`post_cutoff_snapshot` flag requires the **forecast cutoff** itself to be after 2026-04-30. LATE is a
post-**stated**-cutoff stratum, not a guaranteed contamination-free holdout. Model identity and cutoff must be
reconsidered if a different forecaster model is used. The packet now explicitly forbids post-cutoff world facts
from model memory, including later election results and decisions; plans dated after the cutoff may be used only
when they were already stated in cutoff-valid evidence and remain uncertain. Forecast rationales must be audited
for assertions about later world state. This responds to FINDING-001. The frozen preregistration is unchanged.

## DEV-009 — Masked packet identity and independent runs (2026-09-25 13:21 UTC)
Recorded after SMOKE1, before any GPT forecast or new result. A masked packet has a different rendering from an
unmasked packet even when its evidence IDs match, so runtime packet deduplication now keeps it distinct. Short
regulator names such as RBI and FDA are masked as well. Masked and unmasked forecasts will use separate isolated
contexts. This implements the entity/title comparison already specified in DEV-003; it does not change outcome
labels or the original preregistration.

## DEV-010 — Frozen GPT-6 Astra snapshot index (2026-09-25 13:25 UTC)
Recorded after SMOKE1 and before any GPT forecast or new result. The canonical stores were rebuilt from the
preserved raw workstreams after DEV-008. Counts stayed at 334 threads (205 actions, 129 controls), 2,065 evidence
items, and 0 GOLD. The new stated-cutoff split is 206 HIST / 128 LATE. The index contains 801 available Design-C
and 2,286 available Design-T `B_PLUS_C` snapshots. `data/snapshots/index.jsonl` SHA-256 is
`eca775c8e0de4eaaf0d8c4fb95de331f9a647d597d3568ec06b41299bdffc7eb`. Commit this index before any
new forecast. Future data or method changes require a new index version and explicit run-to-index provenance; do
not rebuild the index under a live forecast run. This responds to FINDING-002.

## FINDING-003 — Pre-release packet audit and source-claim repair (2026-09-25 13:29 UTC)
Recorded before any GPT forecast or new result. The pre-release smoke packet audit found two Tier-C `extracted_claims`
that appended retrospective comparisons to later thread anchor drafts (`IN-RBI-H-0010-E02` and
`IN-RBI-H-0021-E02`). The source excerpts themselves were contemporaneous. The claims are patched through
`data/audits/patches/astra_smoke_preflight.jsonl`, preserving the raw executor data. The audit also found full
regulator names in masked FDA/RBI packets; the masking alias table and generic masked action description were
expanded. Packet files were written with Windows CRLF while their manifest hashes covered LF text; the writer now
uses UTF-8/LF bytes. All packets must be regenerated and byte hashes checked before forecasting. These repairs
do not alter evidence IDs/dates, outcomes, or index membership; they do not constitute a full GOLD audit.

## FINDING-004 — Masked smoke run requires repair (2026-09-25 13:41 UTC)
Recorded after the first GPT smoke forecasts, before headline evaluation. Independent review found that the eight
forecasts in `ASTRA_MASK_SMOKE2_SMALL` used packets which, despite masking agency names and header titles, retained
an official's name and exact policy/document titles in claims and excerpts. The run is preserved for audit but is
**invalid for the masked-versus-unmasked comparison** and will not be ingested into the headline ledger. The masking
rules now redact those names and title phrases while keeping the policy mechanism where possible; a new run with
fresh model contexts is required. Masking can still remove legitimate content (notably the FDA draft guidance
topic), so any measured accuracy change must be interpreted with that limitation.

## DEV-011 — Bind each forecast run to the frozen index (2026-09-25 13:46 UTC)
Recorded after the GPT smoke forecasts but before ingestion or evaluation. Run manifests now include SHA-256 of
their source snapshot index; preflight and ledger ingestion reject a changed index. The hash was retrofitted to
`ASTRA_SMOKE2` and `ASTRA_MASK_SMOKE3` after confirming both used the unchanged index recorded in DEV-010.
The invalidated first masked run remains preserved and cannot be ingested. This protects future scaled runs against
the index drift described in FINDING-002; it does not alter forecasts or labels.

## FINDING-005 — Repaired masked smoke remains a diagnostic (2026-09-25 13:46 UTC)
Independent review of `ASTRA_MASK_SMOKE3` found no expressed future facts, invalid citations, or incoherent
probabilities. Two of eight forecasts self-report outcome recognition. Two FDA guidance forecasts lose most
substantive topic information when the title is withheld. An RBI excerpt retained an exact draft title despite
agency-name redaction; a further generic title pattern was added for **future** masked packets, without modifying
or relabelling the existing SMOKE3 packets. SMOKE3 is a partial-masking sensitivity only, not evidence of anonymity
or freedom from memorisation. A representative GOLD masking test remains required.

## FINDING-006 — Source audit invalidates the GPT smoke gate (2026-09-27)
Recorded after smoke forecasts, before headline evaluation. RBI H0021 was labeled stalled but official Directions
adopted the matter on 2025-05-08. The pseudo-anchor used in both ASTRA_SMOKE2 and ASTRA_MASK_SMOKE3 was therefore
invalid. Further reviews found earlier US/FDA first-public action dates and additional India false controls.
Both runs are now invalidated; source index rows and forecasts remain archived, and neither run was ingested.
The actual primary smoke includes US-FR H0002 and H0010 only. An earlier agent message incorrectly described six
US-FR smoke threads. Canonical synthetic comment counts were Tier S and did not enter B_ONLY/B_PLUS_C packets.
The 158 US-FR counts are being dropped; FDA has 21 similar items. These flaws invalidate affected experiments,
not the research question. Fresh smoke forecasts are required after repair and a new committed dataset freeze.

## DEV-012 — Full source binding and audited provenance corrections (2026-09-27)
Recorded after diagnostic forecasts, before any headline evaluation. New run manifests bind SHA-256 of canonical
threads, evidence, outcomes, and index. Preflight, ledger ingestion, and evaluation reject a changed canonical
source set; the evaluator validates only the requested runs and rejects invalidated runs. Earlier GPT diagnostics
have been bound to their unchanged source files at checkpoint b53ca1b for archival provenance.
Auditor patch fields now include decisive-document/source metadata and evidence source/date-verification fields,
so a false-control correction replaces its evidence trail as well as its boolean/date. Original raw files stay intact.
The US-FR collector no longer backdates current comment counts to comment-close +14 days; a count is available
only on its actual observation date, and observations after the fixed censor window cannot enter this backtest.
The target remains first verified official public adoption. PI availability and print publication are distinct;
PI alone is not proof that no earlier agency posting existed. Such uncertainty must remain explicit for RAPID,
and cannot be called GOLD. The observation boundary stays 2026-09-24.

## DEV-013 — Source-repair freeze and preserved masking semantics (2026-09-27)
Before any new forecast after FINDING-006, the canonical data was rebuilt with 961 applied patches. It now holds
328 threads (207 actions, 121 controls), 1,869 evidence items and zero GOLD. Six false controls are quarantined;
179 unsupported comment counts are removed. Three OIRA conclusion items on/after corrected action dates were
automatically dropped. All retained anchors exist and canonical schemas validate. The 60-record legacy ledger
chain remains intact. Full suite 17 passed; later guard/masking edits passed 16 focused tests.
The new index has 777 Design-C and 2,240 Design-T B_PLUS_C snapshots. Exact canonical file hashes are recorded in
data/snapshots/freeze_20260927.json. Index SHA-256: `77413c7de115c76fccb308c94a3003d6c0d55a3b183b358f4f8db6dbd1198f90`.
Every run must be frozen/committed before inference; corrections after this freeze require a new version.
A repaired technical smoke uses five verified India actions and five medium-confidence FDA controls. This
regulator/action confounding and incomplete FDA absence verification forbid predictive conclusions from the smoke.
Four masked anchor-topic paraphrases preserve FDA substantive information while removing exact titles. These are
source-derived, audited before inference, and contain no outcome facts. A GOLD masking experiment is still pending.
The GOLD guard now enforces the existing >=3 retained evidence/high action-label confidence requirements and
ignores evidence-item verdicts when selecting a whole-thread audit. No threshold in the preregistration changed.

## FINDING-007 — Masked action endpoint mismatch (2026-09-27)
After the completed SMOKE4 calls, independent output audit found masked rendering replaced the process-specific
final-guidance/final-directions event with a generic adoption event. ASTRA_MASK_SMOKE4 is invalidated for the
identity-only comparison; original outputs/receipts remain preserved and will not be ingested. The renderer now
preserves the original process-specific endpoint, with only the central-bank name generalized to regulator.
A regression test verifies this invariant. Fresh ASTRA_MASK_SMOKE5 packets are generated on the unchanged
source freeze; two further Astra high calls are planned. This corrects the target definition, not the outcomes.
Core SMOKE4 structural checks pass:24 unique forecasts,14 recognition flags; MASK4 had8 outputs,4 recognised.
Recognition is not proof of expressed leakage, but excludes these rows from an uncontaminated sensitivity.

## DEV-014 — Evaluation cohort and comparison guards (2026-10-04)

Before scaled inference, baseline feature/training rows are restricted to threads in the selected primary runs.
Previously an audited subset could be scored against a comparator fitted on unrelated, unaudited canonical labels.
Thread-grouped cross-validation and the fixed baseline rules are unchanged. Exact baseline cohort IDs are reported.
Paired ablations now require matching model, design, matter and cutoff, and reject competing replicate runs rather
than silently overwriting one. The masking-report caption no longer equates a small difference with proof against
memorisation. Calibration slopes are undefined for complete/quasi separation or failed convergence; a divergent
Newton iteration must not produce a spurious finite slope. Original gate thresholds remain unchanged.

The next cohort plan is docs/SCALING_PLAN_20261004.md. Complete precursor frames take priority over an
outcome-conditioned collection of late actions; selected partial audit sets remain explicitly exploratory.
