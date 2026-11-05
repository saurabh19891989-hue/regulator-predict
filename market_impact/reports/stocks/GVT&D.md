# GVT&D — GE Vernova T&D India Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +1.4%** (rank 36 / 22 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +43.6%): 3 months 51%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.9% … P90 +3.9%; plausible 12m relative-return range incl. stock-specific noise: -50.3% … +59.0%
- Decomposition (12m): 0.5 × forward event exposure +1.1% (3m +0.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +3.9% (beta-adjusted) vs a realised market-adjusted move of -18.8% — gap +22.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.25 | +0.52 | +0.77 | +0.18 |
| Sector | +0.00 | +0.13 | +0.13 | +0.17 |
| Theme | +0.00 | +0.24 | +0.24 | +0.13 |
| Geopolitics | +0.04 | -0.01 | +0.03 | -0.00 |
| Company catalysts | +1.04 | +0.00 | +1.04 | +0.52 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.64 | -0.29 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+1.43** | **+0.62** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.54 | +2.50 | +0.00 | +0.01 | +0.03 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.53 | +2.00 | +0.48 | +0.05 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.51 | +1.00 | +0.96 | +0.55 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.26 | +0.00 | +2.26 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.52 | -1.50 | -0.02 | +0.02 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.50 | +1.50 | -0.04 | +0.02 | +0.01 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.44 | +0.00 | +1.44 | +0.00 | +0.00 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.44 | +0.00 | +1.44 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.22 | +0.00 | -0.76 | -0.38 | -0.08 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.93 | -0.60 | +0.00 | -0.13 | -0.19 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | +20.6% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.85 | +0.00 | -0.78 | -0.08 | +0.01 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +0.81 | +0.00 | +0.48 | +0.28 | +0.05 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.3% | -3.3% | -3.3 | +0.1 | -0.0 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +3.1% | +3.1% | +1.0 | +2.1 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.6% | +2.6% | +2.5 | +0.0 | +0.1 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.9% | -1.9% | -1.9 | +0.0 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.7% | +1.9% | +3.8 | -0.1 | +0.1 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | -0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +1.4 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.3% | +1.3% | +0.5 | +0.5 | +0.3 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -4.7% | -1.2% | +0.0 | -4.2 | -0.6 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.9 | -0.1 | +0.0 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +1.4% | +0.8% | +0.0 | +1.4 | +0.0 | +0.0 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +2.1% | +0.8% | +0.0 | +2.2 | -0.0 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GVT&D | +3.75% | +1.88% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → GVT&D | +2.16% | +0.86% |
| 2 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → GVT&D | +1.44% | +0.65% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GVT&D | -1.50% | -0.63% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → GVT&D | -0.77% | -0.53% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → GVT&D | +0.50% | +0.45% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → GVT&D | +0.72% | +0.43% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → GVT&D | +0.72% | +0.43% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → GVT&D | -1.50% | -0.41% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → GVT&D | -2.25% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → GVT&D | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → GVT&D | -1.44% | -0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → GVT&D | -1.44% | -0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → GVT&D | -1.40% | -0.35% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → GVT&D | +0.60% | +0.33% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → GVT&D | -1.60 | events | -2.40% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → GVT&D | +1.20 | events | +1.73% |
| 1 | F_REPO_IN → GVT&D | +1.00 | events | -1.50% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → GVT&D | +0.30 | director_override | +0.72% |
| 1 | C_MIDEAST_CONFLICT → GVT&D | +1.00 | events | -0.60% |
| 1 | P_RENEWABLE_SUPPORT → GVT&D | +0.60 | director_override | +0.60% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → GVT&D | +0.60 | director_override | +0.58% |
| 1 | F_GOVT_CAPEX → GVT&D | +0.20 | director_override | +0.50% |
| 1 | F_STEEL_GLOBAL → GVT&D | +0.50 | director_override | -0.45% |
| 1 | P_US_TARIFF_INDIA → GVT&D | -0.60 | events | +0.18% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → GVT&D | +0.50 | director_override | +0.16% |
| 1 | F_USDINR → GVT&D | -0.37 | observed | -0.15% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Barmer II-South Kalamb HVDC definitive agreement signed and order booked (management expects booking in Q3 FY27) *(review: [RT_TOP_B] L1 announced 7 Sep, stock +9%)* | guidance | 0.85 | +0.3% | +0.26% |
| 2027-01 | Q3 FY27 results (Dec quarter), management reiterated FY27 EBITDA margin 'mid-20s' and base order inflow Rs 7,200-8,000 cr | results | 0.95 | +0.0% | +0.00% |
| 2027-02 | Conclusion of ~US$151 mn US related-party export order | guidance | 0.45 | +1.8% | +0.79% |
| 2027-03 | Revival of two on-hold related-party export orders (Middle East, France) | guidance | 0.30 | +1.1% | +0.34% |
| 2027-03 | STATCOM / data-centre order pick-up (from Q4 FY27) | guidance | 0.50 | +1.4% | +0.70% |

## Analyst profile (agent research, sourced)
# GVT&D — GE Vernova T&D India (as of 2026-11-05)

## Business
GE Vernova T&D India (parent GE Vernova Inc., 51%) supplies EHV transformers, reactors, GIS/AIS switchgear, HVDC and STATCOM terminals and substations to Power Grid, state utilities, renewable developers and group companies abroad. Q2 FY27 (reported 30 Oct 2026): revenue Rs 2,027 cr (+32%), EBITDA Rs 550 cr (27.1% margin, top of the mid-20s guidance), PAT Rs 431 cr (+44%, 11.7% above the CNBC-TV18 poll). Orders Rs 2,440 cr (+52% y/y), backlog Rs 21,440 cr (more than three years of revenue), net cash about Rs 3,250 cr, exports about 32% of revenue. Management targets more than 30% annual execution growth for 3-4 years, FY27 base order inflow of Rs 7,200-8,000 cr and Rs 1,000 cr of capacity capex (about 20% spent). The stock (Rs 4,107, market cap about Rs 1.05 lakh cr) trades at roughly 60-70x annualised earnings (derived from H1 PAT of Rs 794 cr); the pack's P/E of 563 is a scraping artefact from Screener.

## What moves the stock, ranked
1. **Grid build-out and HVDC awards** (T_GRID_ELECTRIFICATION +6, government capex +2.5). Power Grid's formal letter of award for the 6,000 MW Barmer II-South Kalamb HVDC terminal came on 3-4 Nov 2026 (value undisclosed; headline project size cited at about Rs 13,000 cr); management expects booking in Q3.
2. **Valuation / flows** (FPI flows +1.5, repo -1.5). Foreign holding moved 20.4% -> 22.9% -> 19.2% over three quarters.
3. **Commodity cost on fixed-price contracts** (steel -0.9, copper -0.6). The empirical steel elasticity of -3.14 (t -2.0) is higher than the fundamental estimate, likely a cyclical-beta proxy.
4. **Export programme and parent orders** (Middle East and France orders on hold; US$151 mn US order pending; USD/INR +0.4).
5. **Data centres and STATCOM** (+2), starting Q4 FY27.

## Transmission examples
- **Policy chain:** Government announces larger RE and transmission targets (P_RENEWABLE_SUPPORT) -> Power Grid tenders HVDC/GIS packages -> GVT&D wins as one of two or three qualified HVDC bidders -> backlog and margin visibility extend beyond FY30 -> the market capitalises higher long-run earnings in a 65x stock (4th order: multiple expansion).
- **Cost chain:** Middle East escalation -> Brent up -> global steel and copper prices up with freight and insurance -> fixed-price export and HVDC bills of material cost more -> margin dips below mid-20s in the quarters where unhedged content is invoiced -> stock reacts to guidance risk.
- **Macro chain:** Brent up -> INR weaker -> RBI delays easing -> state utilities' financing tighter and long-duration equities de-rate -> GVT&D multiple compresses even without any order change.
- **Competitor chain:** Domestic transformer pricing pressure (Hitachi Energy India, Siemens Energy India, CG Power) shows up first in regular transformer orders; HVDC competition is limited to a few players.

## Current situation and upcoming events
Q2 beat on revenue, margin and PAT and the stock gained 5% on 2 Nov; on 4 Nov it rose 4% intraday to Rs 4,224 on the LoA, about 25% below the 23 June high of Rs 5,650. Events: HVDC booking and definitive agreement (Dec 2026, prob 0.85, impact up to +2.5% since the award is known), Q3 results (Jan-Feb 2027), US related-party order closure (prob 0.45), revival of on-hold Middle East/France orders (prob 0.3), STATCOM/data-centre wins (prob 0.5).

## Bull and bear
Bull: HVDC bookings, higher exports and more than 30% execution growth hold margins at 26-28%, and EPS compounds at about 30%. Bear: orders lumpy, pricing pressure in standard transformers, related-party orders stay frozen and at 65x any slippage causes a 20-30% de-rating (as in Aug 2026, when the stock fell about 28% from its high). Uncertainty: HVDC order value undisclosed; revenue mix and cost shares are estimates; Screener data for this ticker were unusable so fundamentals come from news and call summaries.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.