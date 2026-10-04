# Scaled60 first-output audit — 2026-10-04

**Verdict: PASS for the two b001 output batches only. No blocking output or execution-control defect found.** This is an independent packet-to-output audit, not a forecast-accuracy result, full-campaign acceptance, proof of absence of memorization, or authorization to rewrite predictions.

## Scope and counts

Reviewed the current checkpoint in `CLAUDE.md` and `PROJECT_STATUS.md`, the historical pause checkpoint, `data/audits/core60_packet_release_20261004.md`, the source-freeze receipt, both run manifests, `tools/run_forecast_packets.py`, preflight/canonicalization code, and the following two matching archived inbox/outbox/receipt/campaign-log sets. Read every forecast's rationale, missing-information list, scenario label, mechanism, parameters and citations against its own snapshot. No canonical outcome records were parsed or used. Preflight hashes canonical files, including the outcome file, as opaque bytes only.

| Batch | Distinct forecasts | Scenarios | Citation references | Evidence-bearing snapshots | Title-only snapshots | Insufficient evidence | Recognition true |
|---|---:|---:|---:|---:|---:|---:|---:|
| ASTRA_CORE60_b001 | 20 | 43 | 21 | 9 | 11 | 12 | 3 |
| ASTRA_CAL60_b001 | 20 | 46 | 30 | 12 | 8 | 8 | 3 |
| Total | 40 | 89 | 51 | 21 | 19 | 20 | 6 |

There are 40 distinct direct snapshot IDs across these outputs, with no duplicate, missing or extra IDs. Aliases are not additional model forecasts. Later batches are outside this report's output-review scope, even if produced while the report was being completed.

## Structural, citation and probability checks

All 40 entries have the exact requested fields and correct boolean disclosure types. Their ordered IDs match their batch manifests and their inbox snapshots. Both archived outputs exactly match their original dispatch outputs and the JSON in the corresponding session's sole final agent message.

- All 200 horizon probabilities are finite, in [0, 1], and nondecreasing within each forecast.
- All 40 next-step distributions and all 40 conditional-content distributions sum to one within numerical tolerance. All next-step `final_action` values are no greater than the corresponding 180-day action probability; each 180-day action probability is no greater than one minus `no_further_official_step`.
- All 89 scenario probabilities are in [0, 1]; each forecast contains two or three scenarios, with conditional scenario probability sum no greater than one. These describe policy content conditional on action, not unconditional action probabilities.
- All 51 supporting/contrary citation references resolve to local E1 labels in the same snapshot. All title-only scenarios have empty citation arrays. No cross-snapshot citation was found.
- All 40 notes satisfy the 40-word limit, all 89 mechanisms satisfy the 25-word limit, and all missing-information lists contain no more than three items.
- Independent raw-value assertions and `canonicalise` validation pass for every forecast with zero coherence repairs. No normalization, repair, ingestion, or forecast edit was performed by this audit.

## Textual leakage and recognition review

**No specific post-cutoff world-state fact, eventual decision, finalization date, or remembered outcome is asserted in the 40 rationales or 89 scenarios. No observable cross-snapshot transfer was found.** Draft ages are consistent with the dates supplied to the relevant snapshot. Title-only forecasts use the title and general procedural reasoning; all 19 correctly mark insufficient evidence. The additional insufficient-evidence flag is the CORE mpox notice, which supplies little substantive detail.

The two historical stress-testing forecasts explicitly acknowledge that replacement settings are absent; their Z-score ranges are predictions rather than claims about an adopted setting. The CAL call-auction forecast likewise treats timings as predicted ranges, and acknowledges that the actual proposed settings were omitted. CAL's drug-master-file forecast derives its six-month lead time and FY2023–2027 program period from its own E1 excerpt. The corresponding CORE title-only forecast does not import those values. Earlier-draft withdrawal in the CORE sponsor-safety-reporting evidence is contemporaneous precursor context, not withdrawal of the forecasted guidance.

Recognized outcomes are disclosed in six forecasts:

| Run | Snapshot | Visible matter |
|---|---|---|
| CORE60 | S48819f1389 | Digital health technologies for remote data acquisition |
| CORE60 | S7971233e95 | Instructions for Use patient labeling |
| CORE60 | Sad08763c65 | AI/ML device predetermined change control plans |
| CAL60 | S84f524ad11 | Digital health technologies for remote data acquisition |
| CAL60 | S6236a6c68e | Drug products labeled as homeopathic |
| CAL60 | Sd5fb29532d | Covariate adjustment in randomized clinical trials |

All six retain cutoff-grounded or general-process rationales and do not reveal the remembered disposition. The other 34 declare recognition false; no contradictory explicit admission or specific future result appears in their text. Disclosure is self-report, and this review cannot establish whether latent memory influenced probabilities. Retain the flags for subsequent recognition sensitivity reporting.

## Packet, source-freeze and execution provenance

The two archived packet hashes agree with their manifest and execution receipts; their external dispatch copies match byte for byte. The frozen canonical-file hashes and snapshot-index hash pass read-only preflight and agree with the 2026-10-04 source freeze. Source-document provenance continues to rely on the completed packet-release/source audits; this audit did not reopen original PDFs or assert their historical immutability.

| Artifact | CORE60 b001 SHA-256 | CAL60 b001 SHA-256 |
|---|---|---|
| Packet | b6ac9a09ae99b1919d8f9119cb8b72e5735b476eab958573b50be7c622597ea5 | 62e17bf02a2385c9881900aef4bec0b07c759655ff28d880c44cab30e1bb00f8 |
| Output | e67e92dbd3c255589e096ec516911af615d3da22382e25e2c0ed5f296c12104d | 9c9beac09b408c4e19972fb7b1602a15f779d4ff5a2ce37a524c26b2e2131927 |
| Events | 5983d98d04e31d17d15a2d2407a0c823fd24c24aafb7f5031638a43a69058ed4 | 8b080e5c565ea17bdc6acb46f9d2d12fbea161456c3e9255f71a6c31a6a77de6 |

Both original event files match their receipt hashes. The newly preserved repository event copies, under each run's `events/<batch>.jsonl`, match those originals byte for byte. Campaign-log stdout parses to the matching execution receipt, and both campaign and runner exit codes are zero. Both stderr logs are empty. Usage values agree between completion events and receipts.

The two sessions are distinct: CORE `01a10574-dc9d-7b20-a55f-7960cb080c16` and CAL `01a10574-c973-7d03-98cf-c82d2faa105a`. Each event stream contains one thread start, one turn start, one completed agent-message item and one turn completion; zero tool items, errors or unexpected item types appear. Receipt/manifests name `gpt-6-astra`.

Reviewed runner configuration specifies high reasoning effort, fresh ephemeral sessions, isolated scratch working directories, ignored user configuration, no project-document content, disabled shell/web/plugins/apps/multi-agent/memories/shell snapshots, and read-only sandboxing. Its prompt combines only the explicit anti-leakage prefix and frozen packet text. These controls are evidenced by runner source and receipts; the event logs independently show no executed tool calls but do not independently attest every runtime flag or the served backend model.

## Read-only preflight and disposition

Called `rpe.preflight.preflight` with the repository `.venv` Python and bytecode writing disabled. At the time of this check, CORE b001 and CAL b001 were each `ready` with 20 forecasts, zero problems and three recognized IDs. CORE had 19 pending batches and CAL had 17. Both run-level `ok` values were false solely because those remaining batches were pending; this was expected and is not a defect in the audited outputs. The standalone system Python lacked `jsonschema`; using the existing repository environment resolved that audit-runtime issue without installation or repository changes.

**Disposition: preserve and accept these two outputs through the output-audit gate, with recognition flags and existing RAPID/source-timing limitations intact.** Remaining campaign outputs require their own checks before full-run acceptance and ledger ingestion. This report neither scores outcomes nor changes the fixed 2026-09-24 observation boundary, the source freeze, forecasts, code, or other project documents. Only this audit report was written.
