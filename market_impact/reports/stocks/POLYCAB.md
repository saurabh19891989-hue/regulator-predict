# POLYCAB — Polycab India Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months +0.5%** (rank 148 / 64 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.7%): 3 months 49%, 12 months 53%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.4% … P90 +3.9%; plausible 12m relative-return range incl. stock-specific noise: -37.8% … +39.5%
- Decomposition (12m): 0.5 × forward event exposure +1.8% (3m +0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.1% (beta-adjusted) vs a realised market-adjusted move of -22.4% — gap +22.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.51 | +0.38 | +0.89 | +0.17 |
| Regulatory | +0.00 | -0.02 | -0.02 | -0.00 |
| Sector | +0.00 | +0.31 | +0.31 | +0.23 |
| Theme | +0.00 | +0.34 | +0.34 | +0.20 |
| Geopolitics | +0.00 | +0.01 | +0.01 | +0.01 |
| Company catalysts | -0.21 | +0.00 | -0.21 | -0.56 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.66 | -0.30 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.52** | **-0.35** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Competitive intensity in Indian wires & cables (`NEW_WC_COMPETITIVE_INTENSITY`) | +1 = new entrants/capacity cause ~100 bp sustained W&C margin erosion | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.97 | +3.50 | +0.28 | +0.17 | +0.02 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.72 | +3.50 | +0.00 | +0.11 | +0.11 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +3.21 | +2.00 | +0.64 | +0.57 | +0.00 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +3.07 | +3.00 | +0.00 | +0.03 | +0.04 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.96 | +2.50 | +0.42 | +0.04 | +0.01 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.34 | +0.00 | +2.32 | +0.00 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.11 | -1.50 | -0.48 | -0.08 | -0.05 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.39 | +0.00 | +1.04 | +0.41 | -0.06 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.38 | +0.00 | -1.12 | -0.17 | -0.09 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.32 | +0.00 | -0.96 | -0.24 | -0.12 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.23 | +1.00 | +0.00 | +0.19 | +0.03 | — |
| Copper price (`F_COPPER`) | +10% copper | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | -2.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.4% | +4.4% | +3.7 | +0.8 | -0.0 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +3.8% | +3.8% | +2.0 | +1.8 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -1.5 | -0.6 | -0.0 | -0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.6% | +1.6% | +1.0 | +0.3 | +0.3 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.1 | -0.3 | -0.2 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | +0.0 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.0% | +1.0% | +0.0 | +1.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.2% | -0.9% | -1.5 | -0.6 | -0.0 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +0.8% | +0.7% | +0.7 | +0.1 | +0.0 | +0.0 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +1.2% | +0.7% | +0.0 | +1.2 | +0.0 | +0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -5.4% | -0.6% | -1.5 | -2.7 | -1.0 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | +0.2 | -0.3 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POLYCAB | +0.70% | +0.63% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → POLYCAB | -1.50% | -0.63% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POLYCAB | +1.44% | +0.58% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → POLYCAB | -1.80% | -0.45% |
| 2 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → POLYCAB | +0.96% | +0.43% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → POLYCAB | -1.50% | -0.41% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POLYCAB | -0.52% | -0.35% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → POLYCAB | +0.48% | +0.29% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → POLYCAB | +0.48% | +0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → POLYCAB | -1.50% | -0.27% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_GOVT_CAPEX → POLYCAB | +0.35% | +0.24% |
| 3 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POLYCAB | -0.26% | -0.22% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → POLYCAB | +0.59% | +0.21% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → POLYCAB | +0.35% | +0.19% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → POLYCAB | +0.40% | +0.18% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | NEW_WC_COMPETITIVE_INTENSITY → POLYCAB | +1.00 | director_override | -6.00% |
| 1 | F_REPO_IN → POLYCAB | +1.00 | events | -1.50% |
| 1 | P_RENEWABLE_SUPPORT → POLYCAB | +0.60 | director_override | +1.20% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POLYCAB | +1.20 | events | +1.15% |
| 1 | F_ALUMINIUM → POLYCAB | -1.96 | observed | -0.78% |
| 1 | F_GOVT_CAPEX → POLYCAB | +0.20 | director_override | +0.70% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → POLYCAB | +0.30 | director_override | +0.48% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → POLYCAB | +0.60 | director_override | +0.38% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → POLYCAB | +1.55 | director_override | -0.37% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → POLYCAB | +0.50 | events | +0.36% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → POLYCAB | +0.50 | events | +0.35% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → POLYCAB | +1.00 | events | -0.31% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Resolution of insolvency petition (NCLAT set aside proceedings 2026-10-30; further appeal possible) | litigation | 0.15 | -1.0% | -0.15% |
| 2026-12-30 | Exit from NSE F&O segment effective (announced 2026-10-13; stock fell ~5%) | corporate_action | 0.97 | -1.0% | -0.97% |
| 2027-01 | Q3 FY27 results (Dec quarter) | results | 0.95 | +0.0% | +0.00% |
| 2027-04 | EHV cable plant commissioning (FY28, possibly Apr-May 2027) | capex | 0.35 | +2.0% | +0.70% |
| 2027-05 | Q4 FY27 results and dividend | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# POLYCAB — Polycab India Ltd. (profile as of 2026-11-05)

Sources: pack `market_impact/data/packs/POLYCAB.md`; web-search summaries of Q2 FY27 coverage (CNBC TV18, NDTV Profit, Saur Energy, MOFSL/PL notes, Sahi). Cost and segment shares are model estimates. No expected-return number is given.

## Business
Polycab is India's largest wires and cables maker (house wires, LT/HT power and control cables, special cables) with a growing FMEG arm (fans, lights, switches, switchgear, pumps, inverters) and a small EPC unit. Pricing follows LME copper and aluminium with frequent list-price revisions, so revenue tracks metal prices and OPM (~14%) is the true quality signal. Q2 FY27 revenue was Rs 9,899 cr (+53%) and profit about Rs 990 cr (+43%), with volumes up only high-to-mid single digits per brokers, the rest being metal pass-through. Project Spring targets W&C EBITDA 11-13% and FMEG 8-10% by FY30, with growth around 1.5x industry; the EHV cable plant is due in FY28.

## What moves the stock (ranked)
1. **Competitive intensity (-6 per +100 bp margin erosion):** Jefferies debates "new competition" (2026-10-16). Industry capacity additions and new entrants are the main bear thesis, because OPM at 14% is above the FY30 target band of 11-13% for W&C.
2. **Infrastructure and industrial demand:** grid electrification (+4), government capex (+3.5), private capex (+3.5), housing (+3); EHV/HV cables raise mix.
3. **Copper (+1, wide range):** a rising price lifts reported revenue and creates short-lived inventory gains, but spikes cause destocking and working-capital strain; copper +28% in 12 months flatters recent growth.
4. **Valuation and funding:** repo +25 bp ≈ -1.5; interest cost has doubled in a year (Rs 51 cr -> Rs 94 cr per quarter) with working capital.
5. **Flows:** the exit from the NSE F&O segment effective 2026-12-30 cut the stock 5% on 2026-10-13; derivative-linked demand disappears.
6. **Costs:** PVC/XLPE compounds (-0.4).

## Transmission examples
- **Middle East escalation (3rd/4th order):** escalation -> Brent up -> PVC/polymer compound costs rise (2nd, -0.4 effect) and INR weakens -> RBI on hold -> housing and construction financing slow (3rd) -> house-wire volumes and FMEG demand soften (4th) -> volume growth falls below 1.5x industry. Opposite channel: higher oil lifts Gulf capex and export cables slightly.
- **China stimulus (2nd/3rd order):** China demand -> copper and aluminium up -> Polycab hikes list prices within days -> revenue up, absolute EBITDA flat, short inventory gain -> if prices spike, dealers delay purchases (3rd) -> volumes dip for a quarter -> working capital and interest rise (4th).
- **Grid capex (3rd order):** government transmission/renewables push -> HV and EHV cable tenders -> Polycab commissions its EHV plant (FY28) -> higher-margin mix -> W&C OPM above 12% target -> re-rating; also competes against KEI and imports.
- **AI/data centre build-out (3rd order):** hyperscaler campuses -> power distribution and special cable demand -> supply tightness for LT/HT cables -> pricing power, offset by new entrants chasing the same pocket.

## Current situation
Stock Rs 7,857, -15.7% in 3 months, -3.6% in 1 month, vs a 12-month range of Rs 6,660-10,129. FIIs 18.1%, promoters 61.4% (slow decline). Q2 results beat on all parameters; Prabhudas Lilladher Buy, Equitec ADD, three analysts see over Rs 11,000 (CNBC TV18). NCLAT set aside insolvency proceedings against the company on 2026-10-30 (details unknown; stock +2%). Aluminium is -19.6% since June while copper is -2.4%, so metal tailwinds to revenue are fading.

## Upcoming events
F&O exit on 2026-12-30; Q3 FY27 results (Jan 2027); Union Budget (Feb 2027) on duties; EHV plant commissioning (Apr-May 2027 possible); Q4 FY27 (May 2027).

## Bull case
Volume growth stays at 1.5x industry, W&C OPM holds near 13-14% for several years (above the guided floor), FMEG reaches 8% margin, EHV ramps, and the stock moves toward Rs 11,000.

## Bear case
Metal prices fall, reported growth slides to mid-teens, new entrants force price cuts, OPM mean-reverts to 11-12%, and the F&O exit adds supply; P/E compresses from 37 toward 28.

## Uncertainties
No call transcript read; competition thesis not verified. Confidence: medium.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.