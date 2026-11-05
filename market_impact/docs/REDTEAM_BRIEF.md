# REDTEAM_BRIEF.md — adversarial review of the Market Impact Graph (Opus, high effort)

You try to BREAK the model's conclusions for your assigned scope. Repo: `/home/user/regulator-predict`.
Read `market_impact/PLAN.md`, `market_impact/docs/AGENT_SPEC.md` (units!), then your inputs:
`market_impact/results/rankings.csv`, `market_impact/reports/stocks/<T>.md` (verdict, drivers by order, event
impacts, top causal chains, agent profile), `market_impact/results/company_paths.jsonl`,
`market_impact/results/recent_state_paths.jsonl`, `market_impact/results/recent_state_vector.csv`,
`market_impact/results/edges_all.csv`, `market_impact/events/*.json`, `market_impact/results/factor_state.md`.
Today is 2026-11-05; your knowledge ends ~mid-2026 — verify recent facts with fetched primary sources
(company filings/press releases, RBI/SEBI/PIB/USTR/Federal Register, reputable outlets). Google News RSS:
`https://news.google.com/rss/search?q=<q>+when:120d&hl=en-IN&gl=IN&ceid=IN:en`; `curl -sSL -m 40 -A "Mozilla/5.0"`.

## How the numbers are built (read before judging magnitudes)
- `exp_rel_return_12m` = 0.5 × unpriced recent impact + 0.5 × (forward event exposure + company events), then
  centred on the universe. 3m uses 0.3 for the recent part and only events due by Feb 2027.
- **Beta adjustment:** model impacts are reported net of beta × universe-average impact (`beta` column, Blume-shrunk
  3-year weekly beta vs the Nifty 50), matching the beta-adjusted realised move. `*_raw` columns are before adjustment.
- **Unpriced recent impact** = model impact of Jun–Nov drivers minus the realised market-adjusted move, bounded to the
  same sign as the model impact and never larger than it (no mean-reversion bet on unexplained moves).
- **Clamping:** within an event, every node the event shocks is clamped (an event's Brent shock already includes its
  conflict effect). In the recent state, every driver with an observed/specified change is clamped.
- `OVERLAP_DAMP` 0.5: an indirect path from driver X to company c gets half credit if c also has a direct X edge.
- Director corrections live in `graph/edge_overrides.json`, `graph/event_overrides.json`, `graph/director_edges.json`,
  `graph/recent_state_overrides.json`, `graph/node_aliases.json`, `events/dedup.json` (drops, exclusive groups). Read
  them so you do not re-report fixed issues. Your `review/<ID>.json` will be merged into those files by the Director.

Hunt for:
1. **Double counting** — the same economic channel reaching a company by two paths (e.g. its own Brent edge AND
   Brent → another driver → the company where that driver is just a consequence of Brent).
2. **Sign / unit errors** — weights in the wrong direction, per +10% instead of per +1 SSU, SSU mismatch between a
   node's definition and how an edge uses it.
3. **Implausible magnitudes** — any single event or driver moving a company > ±25%, or recent-state impacts that
   ignore that the move was already priced (compare with the realised move in the stock report).
4. **Wrong facts** — events that did not happen, wrong dates, wrong policy levels, probabilities out of line with
   evidence; occurred-event shocks that are LEVELS rather than CHANGES since 2026-06-01.
5. **Missing big channels** that would flip a ranking.

Never edit agent files. Write `market_impact/review/<YOUR_ID>.json`:
```json
{"edge_scale": [{"src": "…", "dst": "…", "origin": "<file stem or null>", "factor": 0.5, "reason": "…"}],
 "event_overrides": {"EV_…": {"prob_by_3m": 0.2, "prob_by_12m": 0.4, "reason": "… source …"}},
 "event_drop": {"EV_…": "reason"},
 "recent_state_overrides": [{"node": "…", "state_ssu": 0.0, "reason": "…"}],
 "findings": [{"severity": "high|medium|low", "subject": "ticker or event", "issue": "…", "evidence": "url/date"}]}
```
`factor` multiplies an edge's weight and range (0 removes it). Be specific and evidence-based; propose only fixes
you can justify. Final reply ≤150 words: top findings and how many fixes proposed.
