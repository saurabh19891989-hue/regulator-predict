# ASHOKLEY — Ashok Leyland Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months -0.2%** (rank 167 / 114 of 200 for 3m / 12m); beta 1.35
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.6%): 3 months 48%, 12 months 53%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.3% … P90 +4.4%; plausible 12m relative-return range incl. stock-specific noise: -31.3% … +35.4%
- Decomposition (12m): 0.5 × forward event exposure +0.8% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +5.7% (beta-adjusted) vs a realised market-adjusted move of +8.0% — gap -2.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.31 | -0.01 | +0.31 | -0.08 |
| Regulatory | +0.00 | -0.02 | -0.02 | -0.01 |
| Sector | -0.18 | +0.98 | +0.79 | +0.35 |
| Theme | +0.00 | +0.06 | +0.06 | +0.04 |
| Geopolitics | +0.05 | +0.01 | +0.06 | +0.02 |
| Company catalysts | -0.45 | +0.00 | -0.45 | -0.45 |
| Market-priced macro | -0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.78 | -0.35 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.18** | **-0.58** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.64 | +3.00 | +0.50 | +0.16 | -0.03 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.49 | +3.50 | -0.03 | +0.05 | -0.03 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.42 | +0.00 | +2.37 | +0.01 | +0.04 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.29 | +0.00 | +2.24 | -0.02 | +0.06 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.15 | -0.80 | -1.01 | -0.20 | -0.15 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.86 | -1.50 | -0.18 | -0.13 | -0.05 | +0.0% |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.82 | -1.80 | +0.00 | -0.02 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.79 | +0.00 | -0.99 | -0.49 | -0.32 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.71 | +0.00 | +0.93 | +0.52 | +0.26 | — |
| Road/highway awarding (`P_INFRA_SPENDING_ROADS`) | +10% | +1.70 | +1.50 | +0.14 | +0.05 | +0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.45 | -1.20 | -0.04 | -0.17 | -0.03 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.41 | +0.00 | +1.40 | -0.01 | +0.02 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.17 | +0.00 | -0.96 | -0.14 | -0.06 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.14 | +0.00 | +0.96 | +0.11 | +0.08 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.6% | +4.6% | +4.8 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.2 | -0.7 | -0.3 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.3% | +1.8% | +2.8 | +0.3 | +0.2 | +0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.8% | +1.8% | +1.8 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.2 | -0.0 | -0.2 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -5.2% | -1.3% | -4.3 | -0.5 | -0.3 | -0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.6% | +1.1% | +0.0 | +0.9 | +0.6 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.7 | -0.5 | +0.2 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -0.9% | -0.9% | -0.8 | -0.1 | +0.0 | -0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -6.9% | -0.8% | -6.5 | -0.3 | -0.2 | +0.0 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +0.9% | +0.8% | +0.0 | +0.5 | +0.4 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ASHOKLEY | +1.95% | +1.07% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ASHOKLEY | -3.30% | -0.83% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → ASHOKLEY | +0.93% | +0.63% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → ASHOKLEY | -5.25% | -0.63% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → ASHOKLEY | +0.70% | +0.56% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ASHOKLEY | +0.60% | +0.54% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ASHOKLEY | -1.20% | -0.50% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → ASHOKLEY | +0.67% | +0.47% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → ASHOKLEY | +0.80% | +0.44% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_GDP_IN → ASHOKLEY | +0.47% | +0.40% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → ASHOKLEY | -0.72% | -0.40% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_GDP_IN → ASHOKLEY | +0.67% | +0.37% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → ASHOKLEY | -6.75% | -0.34% |
| 1 | EV_Q2_FY27_GDP_SOFT ⇒ F_GDP_IN → ASHOKLEY | -2.80% | -0.34% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ASHOKLEY | -1.20% | -0.32% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → ASHOKLEY | +1.35 | events | -2.43% |
| 1 | F_ALUMINIUM → ASHOKLEY | -1.96 | observed | +1.77% |
| 1 | F_GDP_IN → ASHOKLEY | +0.50 | events | +1.75% |
| 1 | F_REPO_IN → ASHOKLEY | +1.00 | events | -1.20% |
| 1 | C_MIDEAST_CONFLICT → ASHOKLEY | +1.00 | events | -0.80% |
| 1 | P_EV_POLICY → ASHOKLEY | +1.10 | events | +0.66% |
| 1 | F_GOVT_CAPEX → ASHOKLEY | +0.20 | director_override | +0.60% |
| 1 | F_USDINR → ASHOKLEY | -0.37 | observed | -0.11% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → ASHOKLEY | +0.50 | events | +0.06% |
| 2 | F_CHINA_GDP → F_RUBBER → ASHOKLEY | +0.30 | events | -0.05% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → ASHOKLEY | -0.25 | events | -0.03% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → ASHOKLEY | +1.00 | events | -0.03% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (Sep quarter; expected mid-Nov) | results | 0.95 | +0.0% | +0.00% |
| 2026-12-01 | November 2026 sales release (strong-volume trend; Oct +23%, Sep +28%) | other | 0.98 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results; commentary on FY27 peak-cycle ('output to peak in FY2027 before two-year dip', Automotive World 2026-09-30) | results | 0.90 | -1.0% | -0.90% |

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