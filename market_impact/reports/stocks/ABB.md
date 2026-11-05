# ABB — ABB India Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months -0.2%** (rank 122 / 118 of 200 for 3m / 12m); beta 1.18
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +31.4%): 3 months 50%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.1% … P90 +4.1%; plausible 12m relative-return range incl. stock-specific noise: -39.2% … +43.0%
- Decomposition (12m): 0.5 × forward event exposure +0.4% (3m +0.5%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +5.6% (beta-adjusted) vs a realised market-adjusted move of -10.9% — gap +16.5 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.16 | +0.22 | +0.38 | +0.07 |
| Regulatory | +0.00 | -0.02 | -0.02 | -0.00 |
| Sector | -0.27 | +0.08 | -0.19 | +0.09 |
| Theme | +0.44 | +0.23 | +0.67 | +0.45 |
| Geopolitics | +0.00 | +0.02 | +0.02 | -0.04 |
| Company catalysts | -0.25 | +0.00 | -0.25 | -0.25 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.68 | -0.31 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.22** | **-0.08** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.46 | +3.50 | +0.00 | -0.09 | +0.05 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +3.32 | +3.00 | +0.30 | +0.02 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.81 | +1.50 | +0.25 | +0.07 | -0.01 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +1.68 | +1.20 | +0.36 | +0.11 | +0.01 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.45 | +0.00 | +0.80 | +0.65 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.32 | -1.20 | -0.08 | -0.01 | -0.03 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.31 | +0.00 | +1.32 | +0.00 | -0.01 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +1.17 | +1.00 | +0.17 | +0.01 | -0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.00 | -0.80 | -0.14 | -0.05 | -0.00 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.99 | +0.00 | -0.85 | -0.07 | -0.07 | — |
| Production-linked incentive schemes (`P_PLI`) | +1 = expansion/disbursement | +0.64 | +0.00 | +0.60 | +0.05 | -0.01 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.62 | +0.00 | -0.48 | -0.09 | -0.05 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +0.60 | +0.00 | +0.60 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.9% | +1.9% | +1.5 | +0.4 | +0.0 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +1.5% | +1.5% | +0.0 | +1.5 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.6% | -1.4% | -3.6 | -1.3 | -0.7 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.2 | -0.2 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.0 | -0.1 | -0.1 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.4 | +0.3 | +0.0 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +0.8% | +0.6% | +0.6 | +0.2 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +0.6% | +0.6% | +0.0 | +0.6 | +0.0 | +0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -0.6% | -0.6% | -0.4 | -0.1 | -0.1 | -0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.4% | -0.6% | -1.2 | -0.2 | +0.0 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -2.6% | -0.5% | -2.2 | -0.2 | -0.1 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -0.4% | -0.4% | -0.4 | +0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ABB | -3.60% | -0.90% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ABB | -1.20% | -0.50% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → ABB | +0.60% | +0.48% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ABB | -0.78% | -0.43% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → ABB | +0.90% | +0.36% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ABB | +1.32% | +0.33% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ABB | -1.20% | -0.32% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ABB | +0.30% | +0.27% |
| 2 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → ABB | +0.60% | +0.27% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → ABB | -1.08% | -0.27% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_AI_CAPEX → ABB | +0.36% | +0.22% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → ABB | -0.32% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → ABB | -1.20% | -0.22% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ F_AI_CAPEX → ABB | +0.24% | +0.20% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → ABB | -1.04% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REPO_IN → ABB | +1.00 | events | -1.20% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → ABB | +1.20 | events | +0.72% |
| 1 | F_STEEL_INDIA → ABB | +1.35 | events | -0.54% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ABB | +0.60 | director_override | +0.48% |
| 1 | F_AI_CAPEX → ABB | -0.30 | events | -0.36% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → ABB | +0.50 | events | +0.35% |
| 1 | F_GOVT_CAPEX → ABB | +0.20 | director_override | +0.30% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → ABB | +0.30 | director_override | +0.30% |
| 1 | F_USDINR → ABB | -0.37 | observed | +0.30% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → ABB | +0.50 | director_override | +0.24% |
| 2 | F_CREDIT_SPREADS_IN → F_PRIVATE_CAPEX → ABB | +0.50 | events | -0.21% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → ABB | -0.60 | events | +0.14% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-13 | Q3 CY26 (Sep 2026) results; analysts expect order intake ~Rs 4,400-4,600 cr (flat q/q); margin and segment mix watched | results | 0.97 | +0.0% | +0.00% |
| 2026-12 | ABB-SoftBank robotics divestment: China regulator prohibited the China leg (2026-11-05); parent restructures/negotiates | corporate_action | 0.60 | +0.0% | +0.00% |
| 2027 | Closing of ABB-Mitsubishi Electric JV and effect on ABB India export mandates | corporate_action | 0.50 | -1.0% | -0.50% |
| 2027-02 | Q4 CY26 / full-year results and dividend; ABB Ltd Q4 update in late January shapes India sentiment | results | 0.97 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# ABB - ABB India Ltd. (as of 2026-11-05)

## Business
ABB India is the 75%-owned Indian arm of the Swiss electrification and automation group. It sells low- and medium-voltage electrification products, motors and drives (motion), process automation systems and services. It reports on a calendar year: Q2 CY26 (April-June) revenue was a record Rs 3,559 cr (+21%) with EBITDA of Rs 447 cr (margin 13% vs 14%), and the order backlog was ~Rs 11,900 cr (0.85x annualised revenue). The robotics business was sold in early 2026 (hence the Rs 1,784 cr exceptional-gain quarter in March). It is debt-free with large cash, exports ~13% of revenue and trades at ~91x trailing earnings. The parent holds the maximum 75%.

## What moves the stock (ranked, % equity value per standard shock)
1. **Private capex** (F_PRIVATE_CAPEX +3.5 per +10pp growth): factories, EMS, batteries and process industries drive motion and automation orders.
2. **Data-centre and AI theme** (T_DATA_CENTRES_IN +3.0, F_AI_CAPEX +1.2): the parent launched a DC power portfolio on 2026-09-21, but on 2026-10-20 it fell on 'AI worries' despite record orders and ABB India fell 6% the next day (its worst day in five months). Part of the stock's value is sentiment about AI capex that India orders do not yet reflect: India order growth was +50% in Q2 vs +81% for the group because DC and some projects are booked by the parent.
3. **Grid electrification and government capex** (T_GRID_ELECTRIFICATION +2.5, F_GOVT_CAPEX +1.5).
4. **Discount rate** (F_REPO_IN -1.2 per +25bp): at 15x book and 91x earnings the equity is very long-duration; the RBI hiked to 5.50% on 2026-10-07 and signalled no cuts.
5. **Margin inputs and FX** (USD/INR -0.8, copper -0.4, steel -0.4): CFO said margin recovery will take time due to commodities and forex.
6. **Brent** (+0.6, empirical +1.68 with t 2.5, shrunk): oil-and-gas capex proxy.

The pack also shows a significant but implausible wheat sensitivity (+2.33, t 2.5), which is treated as spurious and not modelled. The copper sign conflict (empirical positive, structural negative) is explained under the edge.

## Worked transmission chains
- **Middle East escalation -> Brent up (1st) -> Gulf and upstream oil capex plus commodity inflation (2nd) -> demand for process automation up but copper/steel and imported component costs up (3rd) -> ABB India EBITDA margin down 50-100bp before price hikes while orders rise (4th).**
- **Brent up -> INR weaker (2nd) -> ~17% of sales net import exposure costlier (3rd) -> margin -60-120bp unless hedged (4th); CFO already cites forex volatility.**
- **Brent up -> CPI up (2nd) -> RBI hikes (3rd) -> higher discount rate on a 91x P/E stock (4th) -> de-rating of 3-5% per 50bp even if earnings are unchanged.**
- **US hyperscaler capex cut or 'AI bubble' narrative (1st) -> ABB Ltd and Schneider/Siemens fall (2nd) -> ABB India sentiment falls through the parent's listing (3rd) -> valuation compression despite domestic orders (4th).**
- **India grid and renewables build-out (government capex up) -> utilities order switchgear and drives (2nd) -> backlog grows but copper pass-through lags (3rd) -> margin flat while revenue rises (4th).**

## Current situation
ABB India's June-quarter results were solid on revenue and orders but margins slipped. On 2026-10-20 ABB Ltd posted record margins and orders but its shares fell on AI worries; the Indian stock fell more than 12% in five days and brokerages are cautious: Citi Sell, Macquarie Underperform, Axis Reduce, with 14 of 33 analysts at Sell. It also faces the ABB-Mitsubishi Electric JV, seen as an overhang for ABB India's exports to SE Asia. On 2026-11-05 ABB said China's foreign-investment review has prohibited the SoftBank acquisition of ABB Robotics in China; this is a parent-level issue since the Indian robotics business was already sold. A new CFO was appointed on 2026-10-19.

## Upcoming events
Q3 CY26 results on 2026-11-13 (consensus order intake ~Rs 4,400-4,600 cr, flat q/q), RBI MPC in December, Union Budget on 1 February 2027, the Q4 results and dividend in February 2027.

## Bull case
DC and grid orders accelerate, margins recover as commodity and FX volatility settles, large cash balance is deployed, and a stock down 17% from its high re-rates with the global electrification cycle.

## Bear case
Orders disappoint (flat q/q expected), AI-capex scepticism and rate hikes compress the 91x multiple, competition and the Mitsubishi JV erode exports, and group-booked orders keep India's reported order growth below the group's.

Confidence: medium on direction of drivers, low on magnitudes (cost shares and the DC revenue share are model estimates).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.