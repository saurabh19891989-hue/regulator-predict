# ENRIN — Siemens Energy India Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.5%**, **12 months +2.1%** (rank 5 / 12 of 200 for 3m / 12m); beta 0.83
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +41.8%): 3 months 53%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.7% … P90 +6.0%; plausible 12m relative-return range incl. stock-specific noise: -53.8% … +58.3%
- Decomposition (12m): 0.5 × forward event exposure +2.1% (3m +1.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +3.4% (beta-adjusted) vs a realised market-adjusted move of -26.9% — gap +30.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.42 | +0.61 | +1.02 | +0.20 |
| Sector | +0.38 | -0.45 | -0.07 | +0.41 |
| Theme | +0.27 | +0.18 | +0.45 | +0.24 |
| Geopolitics | +0.00 | +0.14 | +0.14 | +0.09 |
| Company catalysts | +1.18 | +0.00 | +1.18 | +0.88 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.48 | -0.22 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+2.09** | **+1.50** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +4.15 | +3.00 | +1.14 | +0.00 | +0.01 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +4.08 | +4.00 | -0.03 | +0.06 | +0.05 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +4.04 | +0.00 | +3.48 | +0.56 | +0.00 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +3.72 | +3.00 | +0.72 | +0.00 | +0.00 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +3.66 | +3.00 | +0.60 | +0.05 | +0.01 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +3.06 | +2.50 | +0.36 | +0.18 | +0.02 | — |
| Power/T&D equipment capacity additions vs demand (pricing pressure) (`NEW_POWER_EQUIP_CAPACITY`) | +1 = peer capacity additions outpace demand enough to cut order pricing/margins ~100 bp | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -1.67 | +0.00 | -1.72 | -0.30 | +0.36 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.59 | +0.00 | -0.90 | -0.41 | -0.28 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.51 | -1.50 | +0.02 | +0.00 | -0.03 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | +1.50 | +0.00 | +0.48 | +0.88 | +0.14 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.44 | +0.00 | +1.44 | +0.00 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.30 | +0.00 | -1.28 | -0.00 | -0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.1% | +4.1% | +4.0 | +0.1 | +0.0 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +4.0% | +4.0% | +1.5 | +2.5 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.7% | +3.7% | +3.0 | +0.7 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -11.9% | -3.0% | -10.0 | -1.2 | -0.7 | -0.1 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +5.5% | +2.2% | +4.5 | +1.1 | +0.0 | -0.1 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +2.0% | +2.0% | +0.0 | +1.7 | +0.3 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | +0.0 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.1 | -0.1 | -0.1 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | -1.8% | -1.2% | +0.0 | -1.7 | -0.2 | +0.1 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +2.0% | +1.2% | +0.9 | +1.1 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.1 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.9% | +1.1% | +0.4 | +1.1 | +0.3 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN | -7.50% | -1.88% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → ENRIN | +4.50% | +1.80% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → ENRIN | -1.72% | -1.17% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → ENRIN | -0.86% | -0.73% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ENRIN | +0.80% | +0.72% |
| 2 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → ENRIN | +1.44% | +0.65% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ENRIN | -1.50% | -0.63% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ENRIN | -2.50% | -0.62% |
| 2 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → F_POWER_DEMAND_IN → ENRIN | +1.72% | +0.55% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → ENRIN | +0.90% | +0.54% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_AI_CAPEX → ENRIN | +0.75% | +0.46% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → ENRIN | +1.08% | +0.43% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → ENRIN | +0.72% | +0.43% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ F_AI_CAPEX → ENRIN | +0.50% | +0.42% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ENRIN | -1.50% | -0.41% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GAS_GLOBAL → ENRIN | +4.61 | observed | -3.69% |
| 1 | F_POWER_DEMAND_IN → ENRIN | +1.20 | events | +3.60% |
| 1 | F_REPO_IN → ENRIN | +1.00 | events | -1.50% |
| 1 | NEW_POWER_EQUIP_CAPACITY → ENRIN | +0.50 | director_override | -1.50% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ENRIN | +0.60 | director_override | +1.15% |
| 1 | T_ENERGY_TRANSITION → ENRIN | +0.30 | director_override | +0.90% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → ENRIN | +1.20 | events | +0.86% |
| 1 | F_GOVT_CAPEX → ENRIN | +0.20 | director_override | +0.80% |
| 1 | F_AI_CAPEX → ENRIN | -0.30 | events | -0.75% |
| 1 | F_STEEL_INDIA → ENRIN | +1.35 | events | -0.54% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → ENRIN | +0.30 | director_override | +0.36% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → ENRIN | +0.50 | director_override | +0.24% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | FY26 (Sep-2026) annual and Q4 results; trading window closed from 2026-09-28 (scanx) *(review: [RT_TOP_A] symmetric)* | results | 0.95 | +0.0% | +0.00% |
| 2026-11 | Siemens Energy AG FY results / outlook (global read-across) *(review: [RT_TOP_A] symmetric)* | guidance | 0.80 | +0.0% | +0.00% |
| 2027-01 | Large HVDC/transmission order awards (PGCIL packages) that could lift backlog | other | 0.35 | +5.0% | +1.75% |
| 2027-02 | Q1 FY27 (Dec-2026 quarter) results *(review: [RT_TOP_A] symmetric)* | results | 0.95 | +0.0% | +0.00% |
| 2027-06 | Transformer capacity expansion commissioning | capex | 0.30 | +2.0% | +0.60% |

## Analyst profile (agent research, sourced)
# ENRIN — Siemens Energy India Ltd. (profile as of 2026-11-05)

Sources: pack `market_impact/data/packs/ENRIN.md`; web-search summaries of the Jun-2026 quarter release (investywise, Sahi, ICICI Direct), Business Standard and Livemint headlines. Segment shares are model estimates. The company's financial year ends in September, so the June 2026 quarter is "Q3 FY26". No expected-return number is given.

## Business
Siemens Energy India (75% owned by Siemens Energy AG, demerged from Siemens Ltd in 2025) sells the equipment that moves and generates power: power and traction transformers, HVDC converters, switchgear, gas and steam turbines, compressors and long-term service. It is net cash, earns a ~68% ROCE and trades at P/E ~67. Backlog is Rs 19,331 cr (+16.4% YoY), roughly two years of sales.

## What moves the stock (ranked)
1. **Grid electrification theme (+6 per unit)** and **government capex (+4 per +10%)**: transmission build-out (HVDC corridors, 765 kV, renewable evacuation) drives orders; backlog converts to revenue over 18-30 months, so order announcements move the stock more than quarterly sales.
2. **Power demand and data centres (+3 each):** gas turbines and services follow generation capex; data-centre captive power is a new pocket.
3. **Energy transition (+3)** and **AI-capex sentiment (+2.5):** the listed power-equipment basket trades as one factor; AI-related stocks fell up to 5-6% on 2026-10-13, 10-15 and 10-30 (Moneycontrol) and the capital goods index fell ~4% on 2026-10-23 with Hitachi Energy and ABB India down 6%.
4. **Valuation channels:** repo +25 bp ≈ -1.5, VIX +5 ≈ -1.
5. **Costs:** copper -0.5, steel -0.4, USD/INR -0.5; price-variation clauses protect most of the order book, so these are small.
6. **Competition (-3 per unit):** peers (Hitachi Energy, GE Vernova T&D, CG Power) are adding capacity; pricing discipline is the main structural risk to a 21-24% OPM.

## Transmission examples
- **Grid capex (3rd order):** Government raises transmission capex (Rs 9 lakh cr grid plan headline, LinkedIn 2026-10-23) -> PGCIL and states float HVDC and 765 kV packages -> Siemens Energy India wins transformer and HVDC orders -> backlog and OPM rise -> equity re-rates; also benefits Indian steel (CRGO) and copper demand, which feeds back as a small cost headwind.
- **Middle East escalation (4th order):** Escalation -> Brent and LNG up -> gas power less competitive and INR weaker -> gas-turbine order delays and imported-content costs up -> margins down slightly; offset: energy-security push raises grid and renewables capex over 12 months. Net effect small near term, mildly positive 12-month.
- **AI sell-off (2nd order):** US AI stocks drop -> FPIs sell Indian AI-adjacent names -> power-equipment basket falls regardless of orders (observed Oct 2026) -> valuation compresses at P/E 67 although fundamentals unchanged.
- **Rates (3rd order):** US 10-year at ~4.9% -> FII selling pressure and weaker INR -> RBI cannot cut -> long-duration, high-multiple equities de-rate; customer financing for IPP capex costlier.

## Current situation
Jun-2026 quarter: sales Rs 2,486 cr (+39%), OPM 24%, PAT Rs 441 cr (+68%), shares +10% on 2026-08-07. Since then the stock fell: -13.5% in a month and -12% in three months to Rs 2,860, against a 12-month range of Rs 2,105-3,968. Motilal Oswal (2026-09-03) and Prabhudas Lilladher (target Rs 3,655, 2026-09-08) were constructive. A new execution head for grid transformers was appointed 2026-10-05. The September-quarter / FY26 results are due in November 2026 (trading window closed 2026-09-28).

## Upcoming events
FY26 annual results (Nov 2026), parent's global read-across, HVDC award decisions, Q1 FY27 results (Feb 2027), transformer capacity commissioning (2027).

## Bull case
Orders accelerate (ICICI Direct sees Rs 35,000-36,000 cr over FY27-28), OPM holds above 22%, and the capacity expansion lifts revenue growth above 30%; scarcity premium for listed grid equipment persists.

## Bear case
AI/power-capex sentiment keeps deflating, peers cut prices, HVDC awards slip, and with P/E 67 any margin slip produces 15-25% drawdowns.

## Uncertainties
Segment mix, cost shares and order inflow figures are estimates; no earnings call or annual report retrieved. Confidence: medium.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.