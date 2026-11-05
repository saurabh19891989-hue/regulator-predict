# POLYCAB — Polycab India Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.0%**, **12 months +8.0%** (rank 31 / 22 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.7%): 3 months 58%, 12 months 65%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +4.0% … P90 +13.3%; plausible 12m relative-return range incl. stock-specific noise: -24.1% … +30.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +5.5 pp (model impact +11.1% beta-adjusted vs realised market-adjusted move -22.4%); forward event exposure +7.6% (3m +1.9%; half assumed priced); company-specific events -0.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Competitive intensity in Indian wires & cables (`NEW_WC_COMPETITIVE_INTENSITY`) | +1 = new entrants/capacity cause ~100 bp sustained W&C margin erosion | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.77 | +3.50 | +0.28 | +0.07 | -0.08 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.47 | +0.00 | -1.83 | -1.14 | -0.50 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.43 | +3.50 | +0.00 | -0.06 | -0.01 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +3.22 | +2.00 | +0.64 | +0.57 | +0.01 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +3.01 | +3.00 | +0.00 | -0.01 | +0.02 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.95 | +2.50 | +0.42 | +0.04 | -0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.34 | +0.00 | +2.32 | +0.04 | -0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.20 | -1.50 | -0.48 | -0.18 | -0.05 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.66 | +0.00 | -1.12 | -0.43 | -0.11 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.65 | +0.00 | +0.00 | -1.01 | -0.65 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.15 | +0.00 | +0.52 | +0.31 | +0.32 | — |
| Copper price (`F_COPPER`) | +10% copper | +1.08 | +1.00 | +0.08 | +0.00 | +0.00 | -2.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.3% | -4.3% | +0.0 | -0.7 | -2.0 | -1.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -2.1 | -1.3 | -0.6 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +3.8% | +3.8% | +2.0 | +1.8 | +0.0 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.7% | +3.7% | +3.7 | +0.5 | -0.3 | -0.2 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +3.0% | +2.7% | +2.8 | +0.2 | +0.1 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -2.5 | -0.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.4% | -2.4% | -1.5 | -0.8 | -0.0 | -0.1 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.6% | +1.6% | +1.0 | +0.3 | +0.3 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.1 | -0.0 | +0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | +0.0 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.0% | +1.0% | +0.0 | +1.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -2.4% | -0.9% | -1.5 | -0.8 | -0.0 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → POLYCAB | +3.50% | +3.50% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POLYCAB | +2.80% | +2.52% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → POLYCAB | -2.52% | -2.52% |
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → POLYCAB | +2.00% | +2.00% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → POLYCAB | -1.99% | -1.99% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → POLYCAB | -1.50% | -1.50% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → POLYCAB | -1.35% | -1.35% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → POLYCAB | -1.33% | -1.33% |
| 2 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → F_HOUSING_DEMAND → POLYCAB | -1.01% | -1.01% |
| 1 | EV_SOLAR_ALMM2_CELL_MANDATE ⇒ P_RENEWABLE_SUPPORT → POLYCAB | +1.00% | +1.00% |
| 2 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POLYCAB | +0.96% | +0.96% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → POLYCAB | +2.10% | +0.95% |
| 2 | EV_LPG_UNDERRECOVERY ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → POLYCAB | -0.84% | -0.84% |
| 2 | EV_BESS_VGF_NOV26 ⇒ T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → POLYCAB | +0.80% | +0.80% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → POLYCAB | -0.78% | -0.78% |

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