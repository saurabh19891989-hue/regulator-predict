# STATUS.md — Market Impact Graph (Nifty 200, 2nd–4th-order effects)

Programme authorised by the user on 2026-11-05. It is separate from the closed regulatory programme (root `CLAUDE.md`, NO-GO 2026-10-05).
Rules: `market_impact/CLAUDE.md`. Method: `PLAN.md`, `docs/AGENT_SPEC.md`.

## Checkpoint — 2026-11-05 (first full run, frozen)

**Delivered**

- **Graph.** 459 nodes (81 agent-proposed) and 2,808 weighted edges.
  - Company exposures: 2,364
  - Backbone (macro transmission): 329
  - Company→company links: 61
  - Event-file driver edges: 48
  - Director gap-fills: 6
- **Profiles.** All 200 Nifty 200 companies, each with sourced exposures, supply chain, catalysts and an `.md` narrative. The 50 Nifty Next 50 names are covered in the most depth.
- **Events.** 161 events after deduplication (22 dropped, 14 mutually exclusive groups): 62 already occurred (since 1 Jun 2026); 99 are upcoming or risk scenarios out to May 2027.
- **Propagation.** Up to 4 hops, damped by order (1, 0.8, 0.6, 0.45). By share of absolute effect: 1st order 40%, 2nd 32%, 3rd 18%, 4th 9%.
- **Reports** (in `reports/`):
  - `SUMMARY.md` (start here) and `RANKINGS.md` (all 200 stocks)
  - `EVENTS.md` and `DRIVERS.md` (which effect hits which company)
  - `stocks/<T>.md` (200) and `events/<EV>.md` (161)
- **Ledger.** `ledger/predictions_20261105.csv` with its sha256, frozen 2026-11-05T08:51:44Z at commit f21d8f3. Entry prices are the latest Yahoo quotes on 5 Nov, intraday.
- **Dashboard.** Datasets in `results/dashboard/*.csv`; page source in `dashboard/index.html`; published privately at https://claude.ai/artifact/EoWJSKzGpqVPDB6SDwnzvm (fixed data from this run).

**Review trail.** Eight Opus red-team reviewers covered: event facts, backbone units, top 26 stocks, bottom 26 stocks, and the remaining 36 Next 50 names. A Director pass added a few more fixes. In total, 257 fixes were merged by `mi/merge_review.py` into:

| Override file | Entries |
|---|---|
| `graph/edge_overrides.json` (edge rescales) | 114 |
| `graph/event_overrides.json` | 45 |
| `graph/recent_state_overrides.json` | 20 |
| `graph/company_event_overrides.json` | 91 overrides + 8 additions |

Rejected items are in `review/rejected.json`; conflicts are in `review/merge_log.json`.

## Key decisions (with evidence)

1. **No "unpriced recent impact" in the headline.** We tested whether the graph's June–November impact explains realised beta-adjusted moves across 198 stocks. The correlation was −0.34:
   - −0.41 for driver states estimated from agent event shocks;
   - +0.10 for market-observed drivers;
   - −0.16 within industries.

   Stock reviewers also found that most large "unpriced" items were stock-specific news the graph lacks. `RECENT_CONVERGENCE` is therefore 0, and the gap is shown as a diagnostic only.
2. **Market-priced macro drift is neutralised.** The catalogue's probability-weighted drift implied S&P −7%, VIX +6 points, 10y G-sec +30 bp and repo +23 bp over 12 months, which is out of line with market pricing.
   - For traded macro drivers (`MARKET_PRICED` in `mi/graph.py`), the drift is offset; their scenarios still drive the Monte Carlo bands and the event reports.
   - Policy, sector, theme and country drivers keep their drift.
3. **Double-count controls.**
   - Within an event, every shocked node is clamped.
   - Overlap damping (0.5) applies at any upstream node with a direct company edge.
   - Driver shocks stop at companies, except for look-through to holdcos profiled ex-subsidiary (VEDL←HINDZINC; BAJAJHLDNG←BAJAJFINSV and BAJAJ-AUTO).
   - Parallel edges from one source are netted.
   - ECL and other catalogue-covered items are filtered out of company events.
4. **Beta adjustment.** Impacts are net of beta × the universe-average impact, using a Blume-shrunk 3-year weekly beta, consistent with the market-adjusted realised moves.
5. **Proxy fixes.**
   - Yahoo HO=F (refining margin) and NG=F (gas) are poor proxies, so those states come from reviewed events or overrides.
   - The MTF=F coal series is stale (last data Dec 2025); coal uses a sourced override.
   - VEDL's demerger breaks its price series, so its realised move is excluded.

## Results (scenario-implied, beta-adjusted, relative to the Nifty 200; NOT validated forecasts)

- **Dispersion.** 12m standard deviation is 1.6 pp; 3m is 0.8 pp. The range is −6.2% to +6.6% over 12m. Model-uncertainty bands are wider: about ±5–10 pp.
- **Top 12m.** HINDPETRO +6.6, IDEA +6.1, IOC +4.1, MAZDOCK +3.5, BDL +3.4, DIXON +3.3, NMDC +2.8, SOLARINDS +2.7, ENRIN +2.5, BPCL +2.5.
  - Drivers: the retail-fuel/LPG compensation policy (OMCs), the 2027 telecom tariff hike, the defence budget, China+1/FDI easing and iron-ore stimulus.
- **Bottom 12m.** POLICYBZR −6.2, MOTILALOFS −3.7, FORTIS −3.4, GROWW −3.4, SWIGGY −3.2, MFSL −2.8, ICICIAMC −2.8, MUTHOOTFIN −2.8, BSE −2.8, 360ONE −2.7.
  - Drivers: the IRDAI commission reset, SEBI F&O curbs and capital-market activity, healthcare pricing regulation, quick-commerce competition and gold-loan rules.
- **Next 50.**
  - Best: IDEA, IOC, MAZDOCK, SOLARINDS, ENRIN, BPCL, TATAPOWER, GAIL.
  - Worst: MUTHOOTFIN, CANBK, CHOLAFIN, BANKBARODA, ZYDUSLIFE, DMART, TATACAP, WIPRO.
- **Sectors (12m).**
  - Leading: telecom +2.1, oil & gas +1.9, chemicals +1.3, capital goods +1.3, power +1.2.
  - Lagging: IT −1.5, financial services −1.3, healthcare −0.8, realty −0.8, consumer services −0.7.
- **Jindal Steel (the user's example).** +1.8% 12m, rank 18. Main channels:
  - Domestic steel price: HR anti-dumping duty and safeguard.
  - Coking coal: input cost.
  - China steel exports: through the global HRC price to the Indian HRC price.
  - Rates and FX: smaller.

  Its company catalysts were mostly duplicates of catalogue events and were removed by RT_TOP_A.

## Unresolved risks and limits

- **No out-of-sample validation.** The only test so far is the in-sample check above, and its result was negative. Rankings are exposure maps with modest tilts; treat them as hypotheses.
- **Agent-estimated magnitudes.** Edge weights rest on fundamentals rules of thumb. Coverage is 2nd–4th order, but the backbone (329 edges) is the main source of indirect effects, so errors there propagate.
- **Weak sources.** Fetching news article bodies often failed, so many facts rest on headlines, packs or screener data. These are labelled low or medium confidence in the profiles.
- **Arbitrary assumptions.** The "half priced" haircut on forward events and the damping constants are arbitrary. A sensitivity run has not been done.
- **Brent volatility.** Brent fell from $117 to $95 between 30 Oct and 5 Nov on US–Iran talks. The Iran scenarios are re-based to $95; a deal or collapse within days would change the oil, OMC and airline rows materially.
- **Spend.** Not metered in-session. About 42 subagent runs (25 Sonnet profile batches, 7 event and 2 backbone agents, 8 Opus red-teams, roughly 0.2–0.35M tokens each). Rough estimate: US$200–300.

## Next actions

1. **Score the ledger.**
   - At 3 months: `python3 -m market_impact.mi.ledger score ledger/predictions_20261105.csv 91`, around 2027-02-05.
   - At 12 months: same command with horizon 365.
   - Compare rank IC against the 12-1 momentum baseline. Do not edit frozen rows.
2. **Optional robustness check:** re-run with the priced share at 0.3 and 0.7 and DAMP ±20%, then report rank stability.
3. **Optional data fix:** replace stale or proxy series (coal, LNG, refining margin, Indian G-sec) with proper sources, then re-run the in-sample check on market-observed drivers only.
4. **Refreshing after big news:** update `events/` via overrides, re-run `mi.graph` → `mi.reports` → `mi.dashboard_data`, and freeze a new dated ledger. Never overwrite a frozen ledger.
