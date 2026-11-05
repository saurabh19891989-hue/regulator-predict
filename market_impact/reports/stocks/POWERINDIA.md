# POWERINDIA — Hitachi Energy India Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.6%**, **12 months +9.9%** (rank 13 / 12 of 200 for 3m / 12m); beta 1.14
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +42.7%): 3 months 59%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.7% … P90 +11.7%; plausible 12m relative-return range incl. stock-specific noise: -38.6% … +42.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +6.8 pp (model impact +13.7% beta-adjusted vs realised market-adjusted move -27.9%); forward event exposure +4.0% (3m +1.6%; half assumed priced); company-specific events +4.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +8.00 | +8.00 | +0.00 | +0.00 | +0.00 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +5.70 | +5.00 | +0.64 | +0.07 | -0.01 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +5.47 | +4.00 | +1.50 | +0.00 | -0.03 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +5.05 | +2.00 | +2.32 | +0.73 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +4.81 | +5.00 | -0.03 | -0.15 | -0.01 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +4.58 | +3.50 | +0.60 | +0.37 | +0.11 | — |
| Power/T&D equipment capacity additions vs demand (pricing pressure) (`NEW_POWER_EQUIP_CAPACITY`) | +1 = peer capacity additions outpace demand enough to cut order pricing/margins ~100 bp | -4.00 | -4.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.49 | +0.00 | -2.50 | -0.08 | +0.09 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.10 | -1.50 | -0.34 | -0.21 | -0.06 | +3.5% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.95 | -2.00 | +0.04 | +0.03 | -0.02 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.92 | +0.00 | +1.92 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.92 | +0.00 | +1.92 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.83 | -0.80 | -0.24 | -0.38 | -0.41 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.67 | +0.00 | +1.20 | +0.39 | +0.09 | +1.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +6.0% | +6.0% | +4.0 | +2.0 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -19.5% | -4.9% | -14.3 | -4.1 | -1.0 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.6% | +4.6% | +5.0 | -0.5 | +0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.7% | -3.7% | -3.3 | -0.2 | -0.1 | -0.1 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +3.9% | +3.5% | +4.0 | -0.0 | -0.1 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -2.9 | -0.1 | +0.2 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +2.5% | +2.5% | +1.0 | +1.2 | +0.4 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.8% | +2.4% | +4.3 | +0.3 | +0.1 | +0.1 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -1.6 | -0.5 | -0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.9% | +1.9% | +0.0 | +1.9 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.4% | +1.9% | +1.4 | +0.8 | +0.8 | +0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POWERINDIA | +4.00% | +3.60% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA | -10.50% | -2.63% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POWERINDIA | +3.75% | +1.88% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | +2.88% | +1.15% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → POWERINDIA | -3.75% | -0.94% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → POWERINDIA | +3.00% | +0.90% |
| 2 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → POWERINDIA | +1.92% | +0.86% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → POWERINDIA | -2.00% | -0.84% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → POWERINDIA | +1.20% | +0.72% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → POWERINDIA | +1.20% | +0.72% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | -1.03% | -0.70% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_AI_CAPEX → POWERINDIA | +1.05% | +0.65% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ F_AI_CAPEX → POWERINDIA | +0.70% | +0.60% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → POWERINDIA | -2.30% | -0.58% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → POWERINDIA | +0.96% | +0.58% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOVT_CAPEX → POWERINDIA | +1.00 | events | +5.00% |
| 1 | P_RENEWABLE_SUPPORT → POWERINDIA | +1.50 | events | +3.00% |
| 1 | F_FPI_FLOWS → POWERINDIA | -1.60 | events | -2.40% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | +1.20 | events | +2.30% |
| 1 | T_ENERGY_TRANSITION → POWERINDIA | +0.50 | events | +2.00% |
| 1 | F_REPO_IN → POWERINDIA | +1.00 | events | -2.00% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → POWERINDIA | +1.50 | events | +1.92% |
| 1 | F_AI_CAPEX → POWERINDIA | -0.30 | events | -1.05% |
| 1 | C_MIDEAST_CONFLICT → POWERINDIA | +1.00 | events | -0.80% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → POWERINDIA | +0.50 | events | +0.80% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → POWERINDIA | +1.00 | events | +0.80% |
| 1 | F_STEEL_INDIA → POWERINDIA | +1.35 | events | -0.54% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (Sep quarter); share.market headline suggests a prior-year 15% jump on Q2; test of margin and backlog | results | 0.95 | +1.0% | +0.95% |
| 2026-12 | Index rebalancing / FPI flows around AI-related stock sell-offs | other | 0.40 | -1.5% | -0.60% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | Large HVDC order awards (Barmer-type 6 GW renewable corridors) lifting backlog | other | 0.35 | +6.5% | +2.27% |
| 2027-05 | Q4 FY27 results and FY28 outlook | results | 0.95 | +0.5% | +0.47% |
| 2027-06 | Karjan (Vadodara) 20th manufacturing unit progress; capacity addition | capex | 0.50 | +1.5% | +0.75% |

## Analyst profile (agent research, sourced)
# POWERINDIA — Hitachi Energy India Ltd. (profile as of 2026-11-05)

Sources: company Q1 FY27 press release (fetched, primary); pack `market_impact/data/packs/POWERINDIA.md` (screener fundamentals were empty, so price/market-cap context is partly estimated); Moneycontrol, Business Standard and Equitymaster headlines; Sahi/others via search. No expected-return number is given.

## Business
Hitachi Energy India (71.31% promoter) makes the hardware of the power grid: power and traction transformers, HVDC converter systems, grid-connection solutions, power quality equipment, switchgear and service. Customers are utilities (PGCIL, state companies), renewable developers, data centres, rail and industry. Financial year ends in March. Q1 FY27 (April-June 2026): revenue Rs 2,493.7 cr (+68.6%), EBITDA Rs 399.9 cr (16.0%), PAT Rs 294.2 cr (+123.5%), order intake Rs 5,096.5 cr (+26.1% ex-HVDC) and a record backlog of Rs 32,222.1 cr. Construction of a 20th plant at Karjan, Vadodara began in June 2026. Export orders were 33.6% of non-HVDC orders.

## What moves the stock (ranked)
1. **Grid electrification and government capex (+8 per theme unit, +5 per +10% capex):** HVDC corridors, 765 kV and renewable evacuation drive order intake; backlog converts over 8-10 quarters.
2. **Data centres (+5) and AI-capex sentiment (+3.5):** data centres were a "significant" contributor in Q1 orders (company). The stock fell with AI-related names on 2026-10-13, 10-15 and 10-30 and by 6% on 2026-10-23 when the capital goods index dropped ~4%.
3. **Energy transition and renewables policy (+4, +2):** first BESS order (165 MW/330 MWh), India's 900 GW non-fossil target by FY36.
4. **Valuation and flows:** repo +25 bp ≈ -2 (very long duration), VIX +5 ≈ -1.5, FPI inflows +1.5.
5. **Competition (-4):** Siemens Energy India, GE Vernova T&D, CG Power, imports; the company itself lobbies for a "level-playing-field policy".
6. **Input costs and FX (small):** copper -0.8, steel -0.4, USD/INR -1.0 (imports from the group partly hedged by export orders).

## Transmission examples
- **Government transmission plan (3rd order):** Rs 9 lakh cr grid plan headline -> PGCIL tenders HVDC and substations -> Hitachi Energy wins orders (HVDC intake lumpy; Q1 intake fell YoY to Rs 5,096 cr from Rs 11,339 cr when HVDC was included) -> backlog to Rs 40,000 cr -> multi-year revenue visibility -> higher multiple. Side effects: copper and electrical steel demand rise.
- **AI sell-off (2nd order):** US AI stocks fall -> FPI selling in Indian AI-theme names (Netweb, E2E, MTAR, Hitachi Energy) -> POWERINDIA drops 4-6% on the day regardless of orders -> then rebounds (+6% on 2026-11-04).
- **Middle East escalation (4th order):** escalation -> Brent up and global risk-off -> INR weak (94.5) and VIX up -> imported valve/component costs up (2nd) -> equity multiple compresses (3rd) -> project financing for renewable developers dearer, energy-transition projects delayed (4th); the company flags that prolonged geopolitical tension could slow the transition.
- **Rates (3rd order):** US 10y at ~4.9% -> EM discount rates up -> long-duration growth names de-rate even as earnings grow; one reason for the -19% six-month move despite +69% sales growth.

## Current situation
Stock Rs 28,130: +37.5% in 12 months, -19.3% in 6 months, -11.1% in 1 month, with a 44% annualised volatility. Chris Wood (2026-09-25) named it a core India pick; JPMorgan lists it among global power-equipment picks (Financial Express 2026-09-29). Equitymaster compared it with Siemens Energy India on 2026-11-02. Shareholders approved material related party transactions on 2026-10-12. The Q2 FY27 result (September quarter) is due in November 2026.

## Upcoming events
Q2 FY27 results (Nov 2026), HVDC awards (Barmer/6 GW-type, 2027), Karjan plant progress, Q3 and Q4 results (Feb and May 2027).

## Bull case
HVDC awards lift the backlog above Rs 40,000 cr, margins reach 16-18%, data-centre and BESS add new pockets and the multiple holds as earnings compound 40-50% a year.

## Bear case
AI-capex fears and higher yields continue to compress the multiple, HVDC order intake stays lumpy and lower, peers cut prices, and a missed quarter produces a 15-20% fall from a very high valuation.

## Uncertainties
Market cap, valuation multiples and segment shares are estimates; no call transcript read. Confidence: medium.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.