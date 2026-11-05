# ASHOKLEY — Ashok Leyland Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.0%**, **12 months +2.8%** (rank 99 / 57 of 200 for 3m / 12m); beta 1.35
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.6%): 3 months 50%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.2% … P90 +8.7%; plausible 12m relative-return range incl. stock-specific noise: -34.5% … +45.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +7.2% beta-adjusted vs realised market-adjusted move +8.0%); forward event exposure +8.8% (3m +2.4%; half assumed priced); company-specific events -0.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.51 | +3.00 | +0.50 | +0.08 | -0.07 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.18 | +3.50 | -0.26 | -0.02 | -0.04 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -2.26 | +0.00 | -0.99 | -0.88 | -0.39 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.18 | -0.80 | -1.01 | -0.18 | -0.20 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.06 | +0.00 | +2.37 | -0.28 | -0.02 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.93 | +0.00 | +2.24 | -0.31 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.91 | -1.50 | -0.16 | -0.17 | -0.08 | +0.0% |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.83 | -1.80 | +0.00 | -0.03 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.81 | +0.00 | -1.32 | -0.37 | -0.12 | — |
| Road/highway awarding (`P_INFRA_SPENDING_ROADS`) | +10% | +1.69 | +1.50 | +0.14 | +0.05 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.65 | +0.00 | +0.93 | +0.39 | +0.33 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.47 | -1.20 | -0.04 | -0.17 | -0.05 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.36 | +0.00 | -0.96 | -0.30 | -0.11 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.35 | +0.00 | +0.96 | +0.20 | +0.20 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.8% | -10.8% | -8.6 | -1.0 | -0.8 | -0.4 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.4% | +4.4% | +4.8 | -0.3 | -0.1 | -0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -2.2 | -0.4 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.6% | -2.6% | -2.5 | +0.0 | -0.0 | +0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.8% | +2.5% | +2.4 | +0.4 | +0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.5 | -0.6 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.8% | +2.2% | +3.0 | +0.3 | +0.3 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.9% | -2.1% | -4.7 | -0.5 | -0.4 | -0.3 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.2 | -0.5 | -0.4 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.8% | +1.8% | +1.8 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.2 | -0.0 | -0.3 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.2% | +1.2% | +0.0 | +0.9 | +0.1 | +0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → ASHOKLEY | -7.43% | -7.43% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → ASHOKLEY | +3.00% | +3.00% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → ASHOKLEY | -2.52% | -2.52% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ASHOKLEY | +2.40% | +2.16% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → ASHOKLEY | -2.16% | -2.16% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → ASHOKLEY | +1.76% | +1.76% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → ASHOKLEY | +1.75% | +1.75% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → ASHOKLEY | -1.59% | -1.59% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ASHOKLEY | -3.75% | -1.34% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ASHOKLEY | +2.25% | +1.31% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → ASHOKLEY | -1.20% | -1.20% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → ASHOKLEY | -1.20% | -1.20% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_GDP_IN → ASHOKLEY | -1.18% | -1.18% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → ASHOKLEY | -1.04% | -1.04% |
| 3 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → F_GDP_IN → ASHOKLEY | -0.85% | -0.85% |

## Analyst profile (agent research, sourced)
# ASHOKLEY - Ashok Leyland (Capital Goods / commercial vehicles)

## Business
Ashok Leyland is India's second-largest M&HCV maker with LCVs, buses, defence vehicles, engines and spares, an EV arm (Switch Mobility) and a captive finance associate. It is almost debt-free; earnings depend on industry volumes and the gap between steel/aluminium/rubber costs and its price hikes. TTM EBITDA margin was 12.8% (Rs5,732 cr), and the Q2 FY27 result is due in November.

## What moves the stock, ranked
1. **Crude / diesel** (F_BRENT -1.5 per +10%, empirical -1.52 with t=-2.8): the strongest statistical driver; fleet profitability and used-CV values follow diesel prices.
2. **GDP, government and roads capex** (+3.5 per pp GDP, +3.0 and +1.5 per capex SSU): freight and construction cycle.
3. **Steel and other input costs** (steel -1.8 per +7%): Q1 FY27 margin fell about a point on materials.
4. **Rates and CV-financing stress** (repo -1.2 per +25bp, credit cost -0.8): RBI hiked to 5.50% on 2026-10-07.
5. **Cycle timing**: industry output seen peaking in FY27 before a two-year dip (Automotive World, 2026-09-30).

## Transmission examples
- **Middle East escalation -> Brent up -> diesel up -> fleet operator margins squeezed -> deferred truck purchases -> Ashok Leyland volumes down** (2nd-3rd order); simultaneously Brent up -> INR weaker -> imported inflation -> RBI tightens again -> CV loan EMIs up -> volumes down (4th order).
- **Crude falls (as on 2026-11-05) -> diesel and inflation expectations ease -> rate-hike pressure fades -> operator profitability improves -> replacement demand and financing appetite revive.**
- **China-driven steel rally (HRC +20.6% since June) -> domestic steel up -> Ashok Leyland cost +1% to +2% -> price hikes -> some pre-buying then softer demand.**
- **Infrastructure push -> road/mining projects -> tipper demand -> operating leverage on 10-13% margins.**

## Current situation
Domestic volumes are very strong: Q1 record 48,763 units; Sep +28%, Oct +23% YoY. The stock rose ~19% in four sessions to 2026-11-05 (headlines tie it to falling crude and strong sales; I did not read the articles in full), after a 3-month dip following the rate hike. Foreign holders have been trimming (FII 24.6% to 19.9% since Mar).

## Upcoming
Q2 FY27 results (Nov); Dec 1 monthly sales; next RBI MPC (Dec); Q3 results in Feb; commodity pass-through.

## Bull and bear
Bull: multi-year freight upcycle, strong cash returns (56% payout), lower crude. Bear: peak-cycle volumes, steel/aluminium cost pass-through lags, higher rates and CV-loan stress, 40% promoter pledge.

Uncertainties: segment mix and export share unverified; the rally cause on 5 Nov is from headlines only.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.