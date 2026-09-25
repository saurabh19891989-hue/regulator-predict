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
