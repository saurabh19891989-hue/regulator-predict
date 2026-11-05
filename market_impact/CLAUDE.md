# market_impact/CLAUDE.md — rules for the Market Impact Graph programme

This directory is a separate programme authorised by the user on 2026-11-05. The root `CLAUDE.md` stock/valuation
out-of-scope rule applies to the regulatory programme (closed with NO-GO), not to this directory.

## Rules
- Every factual claim about a company, event or market needs a source URL and date. Model memory must be labelled as
  such. Today is the analysis date; the Opus/Sonnet knowledge cutoff is ~June 2026, so anything after that must come
  from fetched sources.
- Edges follow the unit convention in `PLAN.md` (standard shock units; company targets in % equity value).
- Events attach to factor/policy/industry/country nodes unless company-specific (layering rule).
- Label every expected return as scenario-implied and relative to the Nifty 200. Never present it as a validated
  forecast. Freeze rankings in `ledger/` with a UTC timestamp before discussing them; never edit frozen rows.
- Report uncertainty explicitly (low/high ranges, confidence, missing information).
- Agents write only to their assigned files; the Director owns merge, graph assembly and rankings.
