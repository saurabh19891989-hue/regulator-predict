# Scaled60 second-output audit — 2026-10-04

**Verdict: PASS for ASTRA_CORE60 b002/b003 and ASTRA_CAL60 b002/b003 only. No blocking defect found.** These four batches contain 80 distinct forecasts. This incremental output audit does not certify the remaining campaign, predictive accuracy, or absence of latent model memory.

## Scope and counts

Applied the same packet-to-output review as `scaled60_first_output_audit_20261004.md` to the four newly assigned batches. Read every rationale, missing-information list, scenario label, mechanism, parameter and citation against its matching inbox snapshot, plus manifests, receipts, original and repository event logs, and campaign records. Used the previously reviewed runner and packet rules. No outcome records were parsed, no inference was rerun, and no forecasts were edited or ingested.

| Batch | Forecasts | Scenarios | Citation references | Evidence-bearing | Title-only | Insufficient evidence | Recognition true | Empty scenario arrays |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ASTRA_CORE60_b002 | 20 | 27 | 28 | 10 | 10 | 10 | 2 | 10 |
| ASTRA_CORE60_b003 | 20 | 21 | 24 | 9 | 11 | 11 | 0 | 11 |
| ASTRA_CAL60_b002 | 20 | 16 | 16 | 7 | 13 | 13 | 2 | 13 |
| ASTRA_CAL60_b003 | 20 | 28 | 19 | 12 | 8 | 8 | 3 | 0 |
| Total | 80 | 92 | 87 | 38 | 42 | 42 | 7 | 34 |

All 80 direct snapshot IDs are distinct and exactly match the respective manifests and inbox packets. Aliases do not represent additional model forecasts. The 34 empty scenario arrays occur on title-only rows and comply with the packet's instruction to provide **up to three** scenarios; this is not a missing-field or probability defect. All 42 title-only rows disclose insufficient evidence.

## Structural and probability checks

- Exact forecast and scenario field sets, expected probability keys, and boolean recognition/insufficiency types pass for all 80 forecasts.
- All 400 cumulative horizon probabilities are finite, within [0, 1], and nondecreasing. All 80 next-step distributions and 80 content distributions sum to one within numerical tolerance.
- For every forecast, next-step `final_action` is no greater than the 180-day action probability, which is no greater than one minus `no_further_official_step`.
- All 92 scenario probabilities are within [0, 1]; each forecast has at most three scenarios and a scenario sum no greater than one. These are conditional content forecasts, not unconditional action probabilities.
- All 87 supporting/contrary evidence references resolve within the same snapshot. E2 appears only where supplied. Title-only forecasts cite no absent evidence.
- All notes satisfy the 40-word limit, all mechanisms satisfy the 25-word limit, and missing-information lists contain no more than three items.
- Raw-value assertions and `canonicalise` validate all 80 forecasts with zero coherence repairs. No canonicalized forecasts were saved.

Read-only `rpe.preflight.preflight` also returns ready for each of these four batches, with zero problems and zero pending batches **within this restricted check**. To respect the four-batch scope while later work continued, the manifest read was filtered in memory to b002/b003 for each run; no manifest file was changed and no later outputs were read. This is not a full-run preflight success. The existing repository Python environment was used with bytecode writing disabled.

## Textual leakage and recognition

**No explicit post-cutoff world-state fact, remembered later decision, finalization date, or cross-snapshot information transfer was found in the reviewed text.** Rationale claims about draft age, revisions, statutory purpose, existing programs, and procedural preparation are supported by the relevant packet or expressed as general process judgments. Specific policy mechanisms are predictions conditional on action.

Examples checked closely:

- CORE b002's IT Resilience Index forecast derives the existing working model and TAC meetings from its own E1; it does not treat the consultation as an already adopted final framework.
- CORE b002's ETF scenarios distinguish visible current bands from predicted reference-price and band alternatives. CORE b003's title-only ETF forecast does not import those numerical settings.
- CORE b003's price-data forecast treats the one-day and three-month requirements as pre-existing rules shown in E1, and forecasts alternative future harmonization choices. Its neonatal-guidance rationale correctly distinguishes a statutory requirement to issue a draft from a finalization deadline.
- CORE b003's significant-index threshold and Trading Member scenarios identify visible AUM/client-level reference values correctly; hypothetical higher thresholds or transition periods are offered as uncertain alternatives. No later adopted setting is asserted.
- CAL b003's homeopathic-guidance rationale uses its own E2 comment-extension notice. Its other title-only forecasts do not import specific draft dates, thresholds, or later dispositions from neighboring snapshots.
- Draft publication on the cutoff itself is correctly treated as a newly published draft for CAL b003's Instructions for Use forecast; the PFDD forecast likewise identifies a one-day-old draft.

Seven entries disclose recognized outcomes:

| Batch | Snapshot | Visible matter |
|---|---|---|
| CORE60 b002 | Sbc75a10375 | AI/ML device predetermined change control plans |
| CORE60 b002 | Sd1bd1b667d | Covariate adjustment in randomized clinical trials |
| CAL60 b002 | S0d747c1585 | Digital health technologies for remote data acquisition |
| CAL60 b002 | S5f9fb0e546 | Drug products labeled as homeopathic |
| CAL60 b003 | S484a64646d | Drug products labeled as homeopathic |
| CAL60 b003 | Se72fdc896d | Covariate adjustment in randomized clinical trials |
| CAL60 b003 | Sf1d0dfea34 | AI/ML device predetermined change control plans |

Their text remains grounded in the visible packet or general process reasoning and does not state the remembered outcome. The other 73 disclose recognition false and contain no contradictory explicit admission. Recognition remains a self-report; neither false flags nor this textual review demonstrate that model probabilities are free of memory influence. Preserve the flags for sensitivity analysis, including possible inconsistency across separate sessions on the same matter.

## Provenance and session controls

Each archived inbox matches its dispatch copy byte for byte, and its SHA-256 matches the batch manifest and receipt. Each archived output matches the original dispatch output byte for byte and parses to the exact JSON in its session's sole completed agent message. Both original and repository event copies match receipt hashes. All four successful receipts identify `gpt-6-astra`, exit code zero, no unexpected items, and usage matching the completion event. Successful stderr logs are empty.

| Batch | Packet SHA-256 | Output SHA-256 | Event SHA-256 |
|---|---|---|---|
| CORE60 b002 | 76ce396378ed9dd7461bb7c814b67c35cdcf0330df139484b250b331872728e0 | 097806cf7b545ce6b7854f7a9c4c87399c03e89c278dae2cadfa76b4f2c36dbf | 8bb88b56cb7a880ff5af5ba7670141cc71d8cc58839c629e119bc8cef97b86ed |
| CORE60 b003 | db68d8c0519107ce21336c2f9b32016bf646618628a388494442abbf05fe2d3a | 0e0cc6ed5afce8526a7ab0b7da63b56d5ece8ebc4112dc804b728a64fd326736 | 9586e5f29485f36f9a79908d2b92461f89d4ce524b5571719d359e8ac807d007 |
| CAL60 b002 | 9adb38cc6bc3e5289482d6d150e2ed477a935fcd30d08f241022ace16eaa7f5a | b6017f260dff7b7530abb7b8195cb6a36328f905f8ea7c71a65bea0075a65460 | 6b32903d08e8cfa08e81690798f5b7f448033540bfb9f52403451b9509a1a9a5 |
| CAL60 b003 | 89d434c69ff33b56eaa458768b08b8f84bb1166ad70fd3fc092c43ff2694b66c | 719ffcb84c8922266b04921c21ba86fc69c6a3be8f89eae6a4ae0f1a4533ceca | ebc79e1ca2a65cdea6134688a955c8ef3ce764295d97e1c533d2ed8b19afd9ea |

Successful sessions are distinct:

- CORE60 b002: `01a10578-d5c1-7802-936c-4d29048d5b1b`
- CORE60 b003: `01a1057c-3ad9-7aa1-bfdd-3f35c755107a`
- CAL60 b002: `01a10578-e2c8-7501-b887-3fa86441b7dd`
- CAL60 b003: `01a1067d-807f-7b60-b549-e39c3440b1e6`

Every successful event stream contains one thread start, one turn start, one completed agent-message item, and one turn completion. No tool items or execution errors appear. Runner source specifies high reasoning effort, ephemeral sessions, ignored user configuration, isolated scratch directories, read-only sandboxing, disabled shell/web/plugins/apps/multi-agent/memories/shell snapshots, and no project-document content. Its input is the anti-leakage prefix plus the frozen packet. Logs demonstrate no executed tools; source and receipt configuration do not independently attest the served backend model or every runtime flag.

The canonical-file byte hashes, including the snapshot index, match the 2026-10-04 source-freeze receipt and both manifests. The outcome file was only hashed as opaque bytes. Original-source provenance remains the responsibility of the completed source and packet-release audits; no source pages were reopened or source-freeze files modified.

## CAL b003 failed-attempt preservation

The current CAL b003 campaign record is explicitly `PASS_AFTER_BOUNDED_RETRY` and points to the successful receipt and `failed_attempts/ASTRA_CAL60_b003_usage_limit`. Unlike the other three campaign records, it is a retry summary rather than a stdout wrapper; its successful receipt pointer resolves correctly.

The preserved failed attempt has exit code 1, no usage, and event hash `7b3d004c87d59df481109c330ee68a9f9285d73cabc606354d25f8ec0654d350`, which matches the archived failed event bytes. Its session is `01a1057c-7901-7a83-824e-61d081398a69`; events contain thread/turn start, error and turn failure, with **no forecast agent-message item**. The subsequent successful session is different. Thus the preserved record supports a retry after failure rather than replacement of a completed forecast. This audit did not launch either attempt.

## Disposition

Accept these four outputs through the output-audit gate while retaining recognition flags and the existing RAPID/source-timing limitations. No blocker was identified for continued queued inference. Other batches and eventual full-run ingestion/scoring require their own gates. Only this report was written by this incremental audit; the first-output report remains preserved.
