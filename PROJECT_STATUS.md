# PROJECT_STATUS.md — Regulatory Predictive Precursor Engine

**Status:** READY TO START
**Last updated:** 2026-09-25
**North-star phase:** Prove or disprove predictive regulatory signal before building downstream market-impact infrastructure.

## Current Gate
GATE 0 — Infrastructure + Historical Backtest

## Current Success Criteria
A same-day RAPID backtest plus an audited GOLD subset that can answer:
- whether regulatory action is predictable before decisive publication;
- which precursor classes contain the predictive signal;
- how much lead time is achievable;
- whether Tier C adds incremental value over Tier B;
- whether stakeholder responses/news improve predictions;
- whether content/parameter prediction is possible;
- whether findings survive negative controls and leakage checks.

## Dataset Counters
- Candidate threads discovered: 0
- RAPID usable threads: 0
- GOLD audited threads: 0
- Positive/resolved actions: 0
- Stalled/withdrawn/no-action controls: 0
- Historical forecast snapshots: 0
- Ablation runs: 0

## Priority Regulators for Pilot
India: IRDAI, RBI, SEBI, TRAI, DGFT/DGTR, CDSCO/NPPA
Global: FDA, Federal Register / selected US agencies

## Model Routing
- Director: Opus 5.5 medium
- Managers: Opus 5.5 medium
- Executors: Sonnet 5 medium/high
- Blind forecasters: Opus 5.5 medium/high
- Leakage audit: Opus 5.5 high
- Exceptional adjudication only: Fable 5.1 high

## Budget
- Anthropic credit available: approximately USD 100 (user-supplied)
- Project budget cap: USD 100 unless user explicitly raises it
- Spend used: 0
- Spend remaining: 100
- Warning threshold: 75% consumed
- Hard stop / user escalation: 95% consumed

## Completed
- High-level predictive architecture defined.
- Project scope narrowed to Tier B/Tier C predictive value.
- Backtesting and ablation selected as first proof gate.

## Active
- None yet.

## Blocked
- None yet.

## Risks to Track
- historical pages silently revised;
- hindsight leakage through current webpages/search snippets;
- survivorship/selection bias from choosing only famous final regulations;
- insufficient negative/no-action controls;
- multiple articles repeating one source;
- inconsistent regulator process states;
- model overconfidence and retrospective rationalization.

## Next Actions
1. Initialize repository/database and schemas.
2. Build source registry and point-in-time evidence schema.
3. Launch candidate-event discovery in parallel by regulator.
4. Construct RAPID and GOLD timeline datasets.
5. Launch blind forecasting and evidence ablations.
6. Run leakage audit.
7. Evaluate and issue GO/NO-GO report.

## Decision Log
### 2026-09-25 — D001
Decision: Do not build stock/option/valuation layers before predictive signal is demonstrated.
Reason: They are downstream transformations and cannot create predictive information.

### 2026-09-25 — D002
Decision: Backtesting is the first scientific gate.
Reason: We need empirical evidence of predictability and incremental value of precursor classes.

### 2026-09-25 — D003
Decision: Use two datasets — RAPID and GOLD.
Reason: RAPID maximizes same-day breadth; GOLD provides stronger point-in-time validity and leakage control.
