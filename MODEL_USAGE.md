# Model usage log

## Planned GPT smoke test, 2026-09-25 13:30 UTC

- Model: `gpt-6-astra`, high reasoning effort, fresh isolated Codex CLI session per packet; no tools or browsing requested of forecasters.
- Runs: `ASTRA_SMOKE2` (4 batches, 24 distinct outputs + 16 identical B/B+C aliases) and `ASTRA_MASK_SMOKE2_SMALL` (2 batches, 8 masked outputs).
- Approximate packet input: 23,058 + 5,762 = 28,820 tokens, before per-session instructions and model overhead. Six model calls planned.
- Output/reasoning tokens and actual Codex usage are not visible in advance. A rough API list-price equivalent for 29k input and 10k–40k output tokens is about USD 0.79–2.29 using [published Astra rates](https://developers.openai.com/api/docs/models/gpt-6-astra); this is not a billed Codex amount.
- Stop for packet or output contamination, malformed forecasts, coherence repairs, or any usage limit. Scale automatically only after the planned smoke audit passes and a separate call-count estimate is recorded.

Actual invocation count, outputs, and observed usage will be appended after the run.

## First smoke invocations, 2026-09-25 13:41 UTC

- Six fresh Astra high-effort CLI calls completed: 4 primary batches and 2 masked batches. CLI reported 52,431 total tokens across them (input, output and reasoning combined); actual account billing is unavailable.
- The primary run produced 24 distinct forecasts. Six reported `recognised_outcome=true`; these stay flagged for sensitivity analysis.
- The first masked run produced 8 forecasts but is invalid for masking comparison under FINDING-004. It is preserved without ledger ingestion. Two fresh masked calls are planned after repair, with about 5,800 packet input tokens plus overhead. No scaled forecasts have begun.

## Repaired masked smoke, 2026-09-25 13:46 UTC

- Two additional fresh Astra high-effort calls (`ASTRA_MASK_SMOKE3`) completed. CLI reported 6,647 and 10,242 tokens, respectively. Total across all eight smoke calls: **69,320 reported tokens**; actual account billing is unavailable.
- Eight new masked forecasts passed structural preflight. Two self-report outcome recognition. This run is diagnostic only under FINDING-005.
- The original six-call estimate was exceeded by two repair calls, before any scaled run. Future batch estimates should include a contingency for packet audit repairs.

## Repaired smoke plan, 2026-09-27

- ASTRA_SMOKE4: 4 calls, 24 distinct outputs + 16 aliases; 17,015 approximate packet input tokens.
- ASTRA_MASK_SMOKE4: 2 calls, 8 outputs;5,654 approximate packet input tokens. Total planned: 6 Astra high calls,
  22,669 packet input tokens plus system/model overhead. Smoke forecasts remain excluded from headline metrics.
- Fresh CLI sessions with user config/project docs, shell, web, apps/plugins, memories and delegation disabled;
  CLI events checked for any unexpected tool activity. Configuration checked against the installed CLI feature list
  and [official reference](https://learn.chatgpt.com/docs/config-file/config-reference).
- Audit workers briefly hit a usage limit; after user continuation, native usage tool reported ordinary usage allowed,
  0% of the five-hour window used and 16% of the weekly window used. No reset credit was redeemed by this task.
- Actual billing remains unavailable. Detailed per-batch usage receipts will be preserved after inference.

## Completed source-repaired smoke and masking correction, 2026-09-27

Six planned calls completed, with per-batch input/output/reasoning usage in archived receipts. All had zero
unexpected tool-item types. SMOKE4 has24 unique forecasts and14 recognition flags. MASK_SMOKE4 has8 forecasts
and4 recognition flags but is invalid for the identity-only comparison because the target endpoint changed.
Two further fresh Astra high calls are planned for MASK_SMOKE5 after restoring the process-specific endpoint;
about5,700 packet tokens plus two CLI/system overheads (roughly10k input tokens each in observed calls).
No scaled forecast run has begun. No reset credit was redeemed by this task.

## MASK_SMOKE5 completed; GPT audit routing, 2026-10-04

Two fresh Astra high calls completed with 24,992 input tokens and 3,437 output tokens reported by the CLI.
The receipts separately report 740 reasoning-output tokens; those are not added again to output usage here.
Both calls had zero unexpected tool items. Independent technical audit passed eight forecasts, now ingested;
four self-report recognition. Actual billing is unavailable.

The user withdrew the DeepSeek request and requested GPT subagents. No DeepSeek call was made. Active research
managers use Sol high; the completed independent masked-output auditor used Astra high. Source audits cover
late US actions, the complete SEBI-R frame and selected RBI records. Detailed model-call receipts are available
for blind forecasting; native research-agent billing is not visible to the Director.

## Scaled60-case forecast estimate, 2026-10-04 — before inference

- ASTRA_CORE60:20 Astra high calls,380 distinct forecasts plus380 identical-evidence aliases;122,968 packet tokens.
- ASTRA_CAL60:18 Astra high calls,298 distinct forecasts plus298 aliases;98,395 packet tokens.
- Total38 calls,678 distinct outputs,221,363 packet tokens. Observed CLI/system overhead suggests approximately
  600k input tokens in total, with roughly250k output tokens if output density follows the smoke. This is a planning
  estimate, not billed usage. Actual receipts will be archived. No reset credit or paid top-up is authorized/used.
- Primary sample is60 audited RAPID cases; zero GOLD and no added TierC in these packets. Same-model TITLE_ONLY
  is included. Any quota, source mismatch, tool activity or forecast validation failure stops the affected campaign.

## Scaled campaign first window and resume, 2026-10-04

- Four calls had completed when CAL60 b003 failed with the explicit account usage-limit error; the other active
  CORE60 b003 call finished successfully before the queue stopped. The stop left 100 distinct forecasts, with no edits/ingestion.
- Original failed CAL60 b003 receipt, events, stderr and campaign log are preserved under failed_attempts.
  The first orchestration summary hit an eager-default KeyError on skipped jobs; its status was reconstructed
  from receipts without inference and preserved as campaign_60_20261004_first_window.json.
- Following user continuation, the native account reported ordinary usage available with 0% of the new five-hour
  window used and 32% weekly used. The bounded retry of CAL60 b003 passed; no reset credit was redeemed.
- Six successful calls now report 93,296 input and 35,606 output tokens, with 2,851 reasoning-output tokens
  separately reported (not added again). There are 120 distinct forecasts. Actual billing is unavailable.
- The remaining 32 calls resumed, with two workers and a stop on any failure. Completed outputs are skipped.

## Continuing ordinary usage windows — 2026-10-05

Further quota stops preserved all successful outputs and failed receipts before retries. At10:07IST the native
account reports ordinary usage allowed,0% current five-hour window and65% weekly usage; both reset credits
remain available and unused. There are22 successful batches /440 distinct forecasts;16 batches resumed.
The long-lived native output-audit context is stopped after its quota error. Its durable reports cover the first
400 forecasts. Remaining text reviews will use fresh bounded contexts after outputs are ready, avoiding repeated
reads and waits in an ever-growing context. Same Astra high audit routing and acceptance criteria are retained.
No forecast, gate threshold, canonical source or outcome label is changed. Actual billing remains unknown.

## Completed scaled inference — 2026-10-05

All38 successful fresh Astra high calls completed:678 distinct forecasts and678 same-input aliases.
Verified successful-call receipts total570,791 input tokens (98,304 cached) and216,429 output tokens;
18,063 reasoning-output tokens are reported separately, not added again. Three failed quota attempts
are preserved separately. Audit/Director usage is not included in these inference totals; billing unknown.
The final bounded auditors hit the ordinary quota before durable reports; user continuation reopened
the window. At15:35IST ordinary usage is allowed, primary1% and weekly81%; no reset credit redeemed.
Fresh bounded Astra audits resumed for the remaining178 forecasts. All execution archives now reconcile;
the old COREb012 event archive was replaced only after matching its preserved failed-attempt bytes.
