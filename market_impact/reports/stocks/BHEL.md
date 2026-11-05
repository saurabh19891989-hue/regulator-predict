# BHEL — Bharat Heavy Electricals Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +1.1%** (rank 37 / 44 of 200 for 3m / 12m); beta 1.51
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +33.0%): 3 months 51%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.7% … P90 +5.8%; plausible 12m relative-return range incl. stock-specific noise: -39.4% … +45.6%
- Decomposition (12m): 0.5 × forward event exposure +3.2% (3m +1.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +7.5% (beta-adjusted) vs a realised market-adjusted move of -3.3% — gap +10.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +3.18 | +3.00 | +0.18 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.16 | +3.00 | +0.02 | +0.13 | +0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.19 | +2.00 | +0.00 | +0.12 | +0.07 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -2.01 | -2.00 | +0.00 | -0.01 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.39 | -1.30 | -0.04 | +0.01 | -0.05 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.28 | +0.00 | -0.35 | -0.53 | -0.40 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -1.28 | +0.00 | -1.72 | +0.10 | +0.34 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | +1.23 | +0.00 | +0.48 | +0.80 | -0.05 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.18 | +1.00 | +0.18 | +0.00 | +0.00 | — |
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +1.16 | +1.00 | +0.14 | +0.00 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.11 | -1.00 | -0.03 | -0.05 | -0.03 | +3.5% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.04 | +0.00 | -0.96 | -0.02 | -0.06 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.99 | +0.00 | -0.85 | -0.09 | -0.05 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.3% | +3.3% | +3.0 | +0.4 | -0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.2% | +3.2% | +3.0 | +0.2 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | -0.0 | +0.0 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +4.6% | +1.9% | +4.5 | +0.3 | -0.0 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.3 | -0.1 | +0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.0 | -0.1 | -0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | -1.4% | -0.9% | +0.0 | -1.7 | +0.2 | +0.2 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.0% | +0.9% | +0.9 | +0.0 | +0.0 | +0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.8 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.3% | -0.8% | -2.5 | -0.1 | -0.6 | -0.1 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | +0.0 | -0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.4% | -0.6% | -1.3 | -0.1 | +0.0 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → BHEL | +4.50% | +1.80% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → BHEL | -1.72% | -1.17% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → BHEL | -0.86% | -0.73% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BHEL | -2.50% | -0.62% |
| 2 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → F_POWER_DEMAND_IN → BHEL | +1.72% | +0.55% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BHEL | -1.30% | -0.55% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BHEL | +0.60% | +0.54% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → BHEL | +1.00% | +0.45% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → BHEL | -0.80% | -0.44% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BHEL | -2.50% | -0.38% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BHEL | -1.30% | -0.35% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → BHEL | +0.50% | +0.30% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → BHEL | -1.00% | -0.25% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → BHEL | +0.40% | +0.25% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → BHEL | +0.99% | +0.25% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_POWER_DEMAND_IN → BHEL | +1.20 | events | +3.60% |
| 1 | F_STEEL_INDIA → BHEL | +1.35 | events | -2.70% |
| 1 | F_REPO_IN → BHEL | +1.00 | events | -1.30% |
| 1 | F_GOVT_CAPEX → BHEL | +0.20 | director_override | +0.60% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → BHEL | +0.60 | director_override | +0.29% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → BHEL | +1.20 | events | +0.22% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → BHEL | +0.50 | events | +0.20% |
| 1 | P_DEFENCE_PROCUREMENT → BHEL | +0.50 | director_override | +0.20% |
| 1 | F_USDINR → BHEL | -0.37 | observed | +0.18% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → BHEL | +0.30 | director_override | +0.18% |
| 1 | F_COPPER → BHEL | -0.24 | observed | +0.14% |
| 2 | F_CREDIT_SPREADS_IN → F_PRIVATE_CAPEX → BHEL | +0.50 | events | -0.12% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Formal contract signing/LoA conversion for Adani Power orders (up to Rs28,000 cr) and further thermal awards (NTPC, state gencos) *(review: [RT_TOP_B] order reported 4 Nov; stock +6% the same day)* | other | 0.70 | +0.5% | +0.35% |
| 2027-02 | Q3 FY27 results (Q2 reported 2026-10-14: PAT +120% YoY) | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Order inflow vs FY27 target; brokers (CLSA) argue valuation already prices order wins | guidance | 0.80 | -1.0% | -0.80% |

## Analyst profile (agent research, sourced)
# BHEL - Bharat Heavy Electricals Ltd. (Power equipment PSU)

## Business
BHEL builds boilers, turbines and generators for thermal power plants and is a major supplier of transformers and HVDC, railway propulsion, industrial equipment, and defence systems. It is government controlled, nearly all revenue is Indian, and profit depends on order book execution on fixed-price, multi-year contracts. TTM EBITDA margin has recovered to 10% (from 3-5% over FY22-FY25); Q2 FY27 PAT was Rs821 cr.

## What moves the stock, ranked
1. **Thermal ordering cycle and power demand** (F_POWER_DEMAND_IN +3.0 per +3pp): Adani Power awarded up to Rs28,000 cr (4 projects, 6,400 MW) on 2026-11-04; Financial Express expects Rs40,000 cr+ orders in the pipeline.
2. **Government and private capex** (+3.0, +2.0 per SSU).
3. **Execution margin versus commodity inflation** (steel -2.0 per +7%; copper -0.6): fixed-price contracts mean cost spikes hit the existing order book.
4. **Valuation and risk appetite** (VIX -1.0, repo -1.3): 51x P/E, beta 1.7-1.8; CLSA sees large downside (NDTV Profit 2026-10-15).
5. **Railways, transmission, reform** (+1.0, +1.5, +1.0).

## Transmission examples
- **Heat wave/power demand surge -> peak shortages -> accelerated thermal tenders -> BHEL BTG awards -> order book up -> revenue visibility 2-3 years out -> margin leverage** (1st-4th order).
- **Middle East escalation -> Brent/LNG up -> gas-based power less viable -> more coal-based capacity -> more BTG orders** (3rd order); simultaneously Brent up -> inflation up -> higher rates -> discount rate up -> multiple down.
- **China steel rally (global HRC +20.6% since June) -> domestic plate/forging cost up -> BHEL fixed-price contracts lose margin in 6-12 months.**
- **Rate hike -> private developers' project financing costlier -> slower thermal financial closure -> order conversion delays.**

## Current situation
Q2 profit +120% YoY, but the stock fell 4% the next day on valuation concerns (2026-10-15); a 5-day rally to a record preceded. The Adani win (2026-11-04) pushed the stock +6%; CLSA remains cautious. DIIs trimmed (23.9% to 21.8%), FIIs added (7.2% to 9.9%).

## Upcoming
Contract finalisation with Adani and others; Q3 results (Feb 2027); Union Budget (Feb 2027).

## Bull and bear
Bull: 6,400 MW Adani wins, multi-year thermal and nuclear cycle, margins rising from 10% toward mid-teens, lower debt. Bear: 51x P/E on 6% ROE, execution delays, working capital and commodity cost spikes on fixed-price contracts.

Uncertainties: segment mix, exact order book and tender pipeline are partly model knowledge; empirical positive steel/iron-ore sensitivities are treated as cycle proxies.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.