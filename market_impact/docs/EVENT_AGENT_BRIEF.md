# EVENT_AGENT_BRIEF.md — executor brief for the event catalogue (binding)

You build one theme of the event catalogue for the Market Impact Graph (repo `/home/user/regulator-predict`).
Read first: `market_impact/PLAN.md`, `market_impact/docs/AGENT_SPEC.md` (§5 event format, §3 edges — binding),
`market_impact/graph/nodes_seed.json` (driver node ids + SSU definitions), `market_impact/results/factor_state.md`
(actual commodity/FX/rate moves to date — use them to quantify occurred events).

Scope: events relevant to Indian listed companies (Nifty 200), within your theme, in three groups:
1. **Occurred** 2026-06-01 → 2026-11-05 that still matter (status `occurred`, prob 1; entry shocks = the change that
   already happened, quantified from factor_state.md or sources).
2. **Scheduled / anticipated** 2026-11-06 → 2027-05-31 (policy meetings, budgets, elections, deadlines, trade-deal
   dates, OPEC meetings, results seasons, regulatory effective dates) with honest probabilities of each outcome —
   model distinct outcomes as separate events (e.g. `EV_RBI_DEC26_CUT25` and `EV_RBI_DEC26_HOLD`).
3. **Risk scenarios** (status `risk_scenario`): low-probability, high-impact possibilities with honest odds.
Aim for 15–25 events. For every event: entry shocks on driver nodes in SSU (conditional on the event), 2–4 causal
chains reaching 2nd, 3rd and 4th order (driver→driver→…; you may end a chain at a named ticker in
`most_affected_hint`), sources with dates. Add any driver→driver `edges` your chains need that are not obvious
(they will be merged with the backbone). Research via fetched sources (your knowledge ends ~mid-2026): Google News RSS
`https://news.google.com/rss/search?q=<query>+when:120d&hl=en-IN&gl=IN&ceid=IN:en`, RBI/SEBI/PIB/government sites,
reputable news. Use `curl -sSL -m 40 -A "Mozilla/5.0"`. Put dated quantitative facts in `factor_state_notes`
(e.g. "RBI repo 5.25% after Oct 2026 MPC" with source) — the Director needs current levels for non-market drivers
(repo, CPI, GDP, G-sec yield, monsoon, credit growth, FPI flows).

Write `market_impact/events/<THEME>.json`, run `python3 -m market_impact.mi.check market_impact/events/<THEME>.json`,
fix all errors. Do not run git. Final reply ≤100 words: events by status, key uncertainties.
