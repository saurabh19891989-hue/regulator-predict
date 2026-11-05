# GVT&D — GE Vernova T&D India Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.2%**, **12 months +8.0%** (rank 19 / 21 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +43.6%): 3 months 58%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +5.8% … P90 +12.0%; plausible 12m relative-return range incl. stock-specific noise: -31.0% … +65.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.2 pp (model impact +8.3% beta-adjusted vs realised market-adjusted move -18.8%); forward event exposure +7.1% (3m +3.1%; half assumed priced); company-specific events +2.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +3.51 | +2.00 | +0.96 | +0.55 | +0.00 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.53 | +2.00 | +0.48 | +0.05 | -0.01 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.40 | +2.50 | +0.00 | -0.09 | -0.01 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.22 | +0.00 | +2.26 | +0.00 | -0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.77 | +0.00 | -1.65 | -0.17 | +0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.52 | -1.50 | -0.02 | +0.02 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.52 | +1.50 | -0.04 | +0.02 | +0.03 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.44 | +0.00 | +1.44 | +0.00 | +0.00 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.44 | +0.00 | +1.44 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.42 | +0.00 | -0.92 | -0.36 | -0.14 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.00 | -0.60 | +0.00 | -0.11 | -0.29 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +0.98 | +0.00 | +0.48 | +0.39 | +0.11 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.98 | +0.00 | +0.00 | -0.91 | -0.07 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.2% | -4.2% | -0.9 | -0.3 | -2.1 | -0.9 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +4.1% | +4.1% | +2.0 | +2.1 | +0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.3% | -3.3% | -3.3 | +0.1 | -0.0 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.2% | +2.2% | +2.5 | -0.3 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.9 | -0.2 | +0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.9% | -1.9% | -1.9 | +0.0 | -0.1 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.8% | +1.9% | +3.8 | -0.1 | +0.1 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -6.3% | -1.8% | +0.0 | -4.9 | -1.1 | -0.3 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.8% | +1.8% | +1.0 | +0.5 | +0.3 | +0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.9% | +1.7% | +2.0 | +0.0 | -0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | -0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +1.4 | +0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → GVT&D | -3.30% | -3.30% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → GVT&D | +2.50% | +2.50% |
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → GVT&D | +2.00% | +2.00% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → GVT&D | -1.99% | -1.99% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GVT&D | +3.75% | +1.88% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_GLOBAL → GVT&D | -1.85% | -1.85% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → GVT&D | -1.80% | -1.80% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → GVT&D | +2.00% | +1.80% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → GVT&D | -1.50% | -1.50% |
| 2 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → GVT&D | +1.44% | +1.44% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → GVT&D | -1.33% | -1.33% |
| 2 | EV_BESS_VGF_NOV26 ⇒ T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → GVT&D | +1.20% | +1.20% |
| 1 | EV_SOLAR_ALMM2_CELL_MANDATE ⇒ P_RENEWABLE_SUPPORT → GVT&D | +1.00% | +1.00% |
| 2 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → GVT&D | +0.96% | +0.96% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → GVT&D | -0.90% | -0.90% |

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