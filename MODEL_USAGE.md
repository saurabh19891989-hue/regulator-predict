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
