# AGENT_SPEC.md — binding output formats for Market Impact Graph agents

Read `market_impact/PLAN.md` and `market_impact/CLAUDE.md` first. Node vocabulary: `market_impact/graph/nodes_seed.json`
(ids, names and the **standard shock unit (SSU)** of every non-company node). Today = 2026-11-05. Your training
knowledge ends ~mid-2026: everything after that MUST come from fetched sources (screener.in, company filings,
exchange announcements, news via Google News RSS `https://news.google.com/rss/search?q=<q>+when:90d&hl=en-IN&gl=IN&ceid=IN:en`,
RBI/SEBI/government sites). Label facts from memory as `"source": "model knowledge"`. Never invent numbers.

## 1. Graph layers (prevents double counting)
- **Layer 0 – EVENT** (from the event catalogue).
- **Layer 1 – DRIVERS**: `FACTOR`, `POLICY`, `COUNTRY`, `THEME` nodes. Events connect only to drivers (or, for
  company-specific events, to one company). Drivers connect to drivers (macro transmission, e.g. Brent → USD/INR).
- **Layer 2 – COMPANY**: drivers → company edges. Company → company edges ONLY for `holding_stake`
  (listed parent/subsidiary or large stake), `group_contagion` (same promoter group), `dominant_customer`
  (counterparty >25% of revenue/volume). Do not create company→company edges for price channels already covered by a
  shared driver (e.g. do not link COALINDIA → NTPC; both attach to `F_COAL_INDIA`).
- **company_links unit:** `w` = % change in the TARGET company's equity value per **+1%** change in the SOURCE
  company's equity value (e.g. parent holding 30% of a subsidiary worth 40% of the parent's value → w ≈ 0.4).
- `INDUSTRY` nodes are labels only (company classification), never edge endpoints.
- If a needed driver does not exist, propose it in `new_nodes_proposed` with id `NEW_<NAME>`, type, name and SSU,
  and use that id in your edges.

## 2. Edge weights — unit convention
`w` = change in the target per **+1 SSU** of the source. Target driver → measured in the target's SSU. Target company →
**% change in equity value**. Give `w` (central), `w_low`, `w_high`, sign included (negative = hurts).
Company rule of thumb: `Δequity% ≈ ΔEBITDA% × (EV / market cap) × persistence`, persistence 0.25 (shock fades within
~6 months), 0.5 (lasts 1–2 years), 1.0 (structural). Example — JSPL vs `F_STEEL_INDIA` (+7% domestic steel price):
steel ≈95% of revenue, EBITDA margin ≈16% ⇒ ΔEBITDA ≈ +6.65/16 ≈ +40%; EV/MCap ≈1.3; persistence 0.3 ⇒ w ≈ +16 (%
equity value per SSU), range +9…+24. Cross-check with the empirical market-adjusted sensitivity in the company pack
(`elasticity_per_ssu`, with t-stat); explain large disagreements.

## 3. Edge object (used everywhere)
```json
{"src": "F_BRENT", "dst": "HINDPETRO", "relation": "input_cost", "w": -9.0, "w_low": -14.0, "w_high": -4.0,
 "lag": "0-3m", "mechanism": "crude is ~80% of costs; retail prices regulated so marketing margins compress",
 "confidence": "medium", "evidence": [{"source": "https://…", "date": "2026-10-28", "note": "Q2 FY27 GRM $6.1"}]}
```
`relation` ∈ input_cost, output_price, demand_driver, competition, funding_cost, discount_rate, fx_translation,
policy_effect, macro_transmission, geopolitical_exposure, regulatory_risk, holding_stake, group_contagion,
dominant_customer, substitution. `lag` ∈ "0-3m", "3-12m", ">12m". `confidence` ∈ high, medium, low.

## 4. Company profile — `market_impact/companies/<TICKER>.json` (+ `<TICKER>.md`)
```json
{"ticker": "JINDALSTEL", "name": "…", "as_of": "2026-11-05", "industry": "I_STEEL", "tier": "NIFTY_NEXT_50",
 "business_summary": "<=120 words",
 "revenue_mix": [{"segment": "steel", "share_pct": 92, "geography": "India 88% / export 12%"}],
 "cost_structure": [{"input": "F_COKING_COAL", "share_of_costs_pct": 35}, {"input": "F_IRON_ORE", "share_of_costs_pct": 15}],
 "exposures": [ <edge objects with dst = ticker, at least 8 for NIFTY_NEXT_50 and 6 for others, covering commodities,
                FX, rates/funding, demand, policy, geopolitics, competition> ],
 "company_links": [ <company→company edge objects, only the allowed relations> ],
 "supply_chain": [{"counterparty": "…", "ticker": "X or null", "role": "supplier|customer|competitor|parent|subsidiary",
                   "importance": "high|medium|low", "note": "…"}],
 "company_events": [{"date": "YYYY-MM-DD or YYYY-MM", "event": "…", "type": "results|capex|regulatory|litigation|corporate_action|guidance|other",
                     "prob": 0.0, "impact_pct_low": 0.0, "impact_pct_high": 0.0, "source": "…"}],
 "current_state": {"latest_quarter": "…", "trend": "…", "valuation": "P/E, EV/EBITDA vs history if known",
                   "recent_developments": ["dated items from Aug–Nov 2026"]},
 "key_risks": ["…"], "upside_triggers": ["…"],
 "new_nodes_proposed": [],
 "confidence_overall": "high|medium|low",
 "sources": [{"url": "…", "date": "…", "what": "…"}]}
```
`<TICKER>.md` (Next 50: ≥600 words; others ≥300): business; ranked list of what moves the stock and why; worked
1st→2nd→3rd→4th-order transmission examples relevant to this company; current situation (latest results, recent
news); upcoming events; bull and bear cases. No expected-return number (the Director computes it from the graph).

## 5. Event — `market_impact/events/<THEME>.json`: `{"events": [...], "edges": [...], "new_nodes_proposed": [...],
"factor_state_notes": [...]}`
```json
{"event_id": "EV_<SHORT_NAME>", "title": "…", "category": "india_macro|global_macro|energy|metals_china|geopolitics_trade|sector_policy|agri_rural",
 "status": "occurred|scheduled|anticipated|risk_scenario", "date": "YYYY-MM-DD", "window_end": "YYYY-MM-DD or null",
 "prob_by_3m": 0.0, "prob_by_12m": 0.0,
 "description": "…", "what_already_moved": "for occurred events: dated, numeric market moves",
 "entry_shocks": [{"node": "F_BRENT", "ssu": 1.5, "low": 0.8, "high": 2.5, "note": "conditional on the event"}],
 "chains": [{"order": 3, "path": ["EV_X", "F_BRENT", "F_USDINR", "F_CPI_IN"], "explanation": "…"}],
 "most_affected_hint": [{"ticker": "…", "direction": "+|-", "why": "…"}],
 "sources": [{"url": "…", "date": "…", "title": "…"}], "confidence": "high|medium|low"}
```
`edges` = any driver→driver transmission edges your chains need (edge objects, §3). Occurred events: prob = 1 and
`entry_shocks` describe the change that already happened (from its start to today). Cover recent (2026-06-01 →
today) and upcoming (→ 2027-05-31) events; include low-probability, high-impact risk scenarios with honest odds.

## 6. Validation before you finish
Run `python3 -m market_impact.mi.check <file>` on every file you wrote and fix all errors. Reply in ≤100 words:
files written, counts, main uncertainties.
