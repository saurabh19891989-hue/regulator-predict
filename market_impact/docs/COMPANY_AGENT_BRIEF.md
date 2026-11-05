# COMPANY_AGENT_BRIEF.md — executor brief for company profiling (binding)

You profile a batch of ~8 Nifty 200 companies for the Market Impact Graph (repo `/home/user/regulator-predict`).
Read first: `market_impact/PLAN.md`, `market_impact/docs/AGENT_SPEC.md` (output format — binding),
`market_impact/graph/nodes_seed.json` (driver node ids + SSU definitions), `market_impact/results/factor_state.md`
(current commodity/FX/rate levels and recent moves).

For EACH ticker in your batch, in order:
1. Read `market_impact/data/packs/<TICKER>.md` (screener.in fundamentals through the latest quarter, price performance,
   empirical sensitivities, recent headlines).
2. Targeted research, at most ~6 fetches per company: the latest quarterly results commentary / investor presentation /
   earnings-call highlights (company website, BSE/NSE filings mirrors, reputable news), segment and geography mix,
   key raw materials and their cost share, key customers/suppliers, debt and FX exposure, capacity/capex plans,
   regulatory exposure, and dated developments Aug–Nov 2026. Google News RSS:
   `https://news.google.com/rss/search?q=<query>+when:90d&hl=en-IN&gl=IN&ceid=IN:en`. Use `curl -sSL -m 40 -A "Mozilla/5.0"`.
   Prefer primary sources. Do not read whole annual reports; target the needed numbers.
3. Write `market_impact/companies/<TICKER>.json` and `market_impact/companies/<TICKER>.md` exactly per AGENT_SPEC §4,
   then run `python3 -m market_impact.mi.check market_impact/companies/<TICKER>.json` and fix errors before moving on.
   Write each company as soon as it is done (work must survive interruption).

Quality bar for `exposures` (the core of the model):
- Cover every material channel: input costs, output prices, demand drivers, FX (exports/imports/foreign debt),
  funding cost and discount rate (rates), policy/regulation, geopolitics/trade, competition/substitution, themes.
  Banks/NBFCs: credit growth, deposit growth/funding, repo/G-sec (NIM and treasury), asset quality, unsecured stress,
  regulation. IT: US tech spend, USD/INR, GenAI substitution, visas. Pharma: US generic pricing, USFDA, tariffs, USD/INR.
- Weights must be numerically reasoned with the §2 rule of thumb; put the arithmetic in `mechanism`
  (e.g. "coking coal 35% of costs; +15% → costs +5.3% → EBITDA −24% at 22% margin; EV/MCap 1.2; persistence 0.3 → −8.6").
- Compare with the pack's empirical sensitivities; mention agreement/disagreement in `mechanism` where |t| ≥ 2.
- Ranges must be honest (wide when uncertain). Confidence `high` only with company-disclosed numbers.
- Use `company_links` only for holding_stake / group_contagion / dominant_customer between universe tickers.
- `company_events`: next results date, AGMs/corporate actions, capex commissioning, regulatory decisions,
  litigation, index changes — with probability and impact range (% equity value, conditional on the event).
- The `.md` narrative must include concrete 2nd/3rd/4th-order transmission examples for THIS company (e.g. for a
  cement maker: Middle East escalation → Brent ↑ → pet-coke & diesel ↑ → cement cost ↑ → margins ↓; and
  Brent ↑ → INR ↓ → RBI holds rates → housing demand ↓ → cement volumes ↓).

Do not run git. Write only your batch's files. Final reply ≤100 words: tickers done, any failures, main uncertainties.
