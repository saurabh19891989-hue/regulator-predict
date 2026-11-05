# M&MFIN — Mahindra & Mahindra Financial Services Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +0.6%** (rank 25 / 57 of 200 for 3m / 12m); beta 1.36
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +36.4%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.7% … P90 +4.5%; plausible 12m relative-return range incl. stock-specific noise: -43.4% … +47.5%
- Decomposition (12m): 0.5 × forward event exposure +0.5% (3m +0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -4.4% (beta-adjusted) vs a realised market-adjusted move of -8.7% — gap +4.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.05 | +0.09 | +0.13 | -0.04 |
| Regulatory | -0.34 | -0.09 | -0.44 | -0.04 |
| Sector | +0.75 | +0.52 | +1.28 | +0.67 |
| Theme | +0.00 | +0.03 | +0.03 | +0.02 |
| Geopolitics | +0.00 | +0.01 | +0.01 | +0.03 |
| Company catalysts | +0.41 | +0.12 | +0.54 | +0.54 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.78 | -0.35 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.62** | **+0.71** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.41 | -6.00 | -0.42 | +0.00 | +0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.55 | +4.00 | +1.17 | +0.62 | -0.25 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.19 | +1.50 | +1.76 | +0.61 | +0.32 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +4.02 | +2.50 | +0.57 | +0.62 | +0.33 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -3.48 | -3.50 | +0.00 | +0.04 | -0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.16 | -2.50 | -0.59 | -0.07 | -0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.07 | -2.00 | -1.30 | +0.13 | +0.09 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.34 | -1.50 | -0.72 | -0.11 | -0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.33 | +0.00 | -1.62 | -0.82 | +0.11 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.17 | +0.00 | +1.68 | +0.61 | -0.12 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.00 | +0.00 | +1.20 | +0.63 | +0.17 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.80 | +0.00 | -0.32 | -0.98 | -0.50 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -1.77 | +0.00 | -1.20 | -0.26 | -0.31 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -5.1% | -5.1% | -3.1 | -0.7 | -0.8 | -0.4 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.7% | -3.7% | -3.2 | -0.5 | +0.0 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.5% | -3.5% | -3.3 | +0.0 | -0.1 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -2.2 | -1.0 | +0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +4.1% | +2.8% | +2.5 | +0.6 | +0.8 | +0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.0% | +2.0% | +3.8 | -0.0 | +0.2 | +0.1 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +2.2% | +1.9% | +1.2 | +0.4 | +0.5 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.2 | -0.4 | -0.2 | +0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +1.6% | +1.6% | +1.6 | +0.0 | -0.0 | -0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -3.7% | -1.5% | -3.2 | -0.5 | +0.0 | -0.1 |
| IMD April 2027 forecast says below-normal monsoon (<96% LPA) - second weak year risk (`EV_MONSOON27_DEFICIT_FORECAST`) | risk_scenario | 0.32 | -4.6% | -1.5% | -2.5 | -0.7 | -1.1 | -0.3 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -1.5% | -1.4% | -1.5 | -0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → M&MFIN | +3.75% | +1.88% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → M&MFIN | +2.50% | +1.70% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → M&MFIN | +1.25% | +1.06% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → M&MFIN | -2.50% | -1.05% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → M&MFIN | +1.20% | +0.84% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → M&MFIN | -0.90% | -0.81% |
| 1 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → M&MFIN | -2.50% | -0.80% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → M&MFIN | +1.30% | +0.72% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → M&MFIN | -2.50% | -0.68% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → M&MFIN | +1.20% | +0.66% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → M&MFIN | -1.05% | -0.63% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → M&MFIN | -2.20% | -0.55% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → M&MFIN | +0.80% | +0.54% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → M&MFIN | -0.60% | -0.54% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → M&MFIN | -1.05% | -0.53% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_MONSOON → M&MFIN | -1.56 | events | -3.90% |
| 1 | F_REPO_IN → M&MFIN | +1.00 | events | -2.50% |
| 1 | F_FPI_FLOWS → M&MFIN | -1.60 | events | -2.40% |
| 1 | F_CREDIT_SPREADS_IN → M&MFIN | +0.50 | events | -1.75% |
| 1 | F_AUTO_DEMAND_IN → M&MFIN | +0.50 | director_override | +1.75% |
| 1 | F_RURAL_DEMAND → M&MFIN | -0.25 | events | -1.00% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → M&MFIN | +0.50 | events | +0.96% |
| 1 | F_GOLD → M&MFIN | -1.05 | observed | -0.52% |
| 1 | F_STEEL_GLOBAL → M&MFIN | +0.50 | director_override | +0.40% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → M&MFIN | +1.00 | events | -0.24% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → M&MFIN | +1.15 | events | -0.21% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → M&MFIN | -1.56 | events | -0.19% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Dividend following 36th AGM approval on 4 Nov 2026 (record date unverified) | corporate_action | 0.90 | +0.0% | +0.00% |
| 2026-12 | Festive/rabi season collection efficiency print (Q3 business update) | guidance | 0.70 | +0.5% | +0.35% |
| 2027-01 | Q3 FY27 results (Q2 was 21 Oct 2026) | results | 0.95 | +0.5% | +0.47% |

## Analyst profile (agent research, sourced)
# M&MFIN - Mahindra & Mahindra Financial Services (midcap, vehicle/rural NBFC)

## Business
MMFS is the Mahindra Group's rural and semi-urban lender: new and pre-owned utility vehicles, tractors, passenger cars, CVs, 3W and SME finance, plus a stake in Mahindra Rural Housing. M&M owns about 52.5%. Revenue Rs 22.6k cr TTM, PAT Rs 3.6k cr TTM; Q2 FY27 PAT Rs 882-911 cr (+55% y/y). Its customers are farmers, small transporters and self-employed borrowers whose cash flows hinge on monsoon, crop prices and fuel.

## What moves the stock (ranked)
1. **Rural demand, monsoon and auto volumes** - drive disbursements (PV disbursements +28% in Q2) and collection efficiency; a +5pp rural demand shock is worth roughly +4% equity.
2. **Margin / funding cost** - the Q2 reaction (-10%, Citi/Jefferies/Nomura target cuts) shows margins are the market's focus; the repo hike to 5.50% and wider NCD spreads feed this.
3. **Asset quality** - a +50bp credit cost shock is about -6%; Stage 3 has been in the high 3s (model knowledge).
4. **Parent link and flows** - M&M UV/tractor cycle; FII 9.95%; steep recent de-rating.
5. **Regulation** - RBI norms for NBFCs.

## Transmission examples
- **Middle East escalation -> Brent up -> diesel cost for transporters and tractor users -> operator income down -> EMI delay and CV/tractor purchase deferral -> MMFS Stage 2/3 up and disbursements down; second chain: INR weaker -> CPI up -> RBI hike (done on 7 Oct) -> floating bank loans reprice within weeks while vehicle-loan yields lag -> NIM compression -> brokerages cut targets (as seen 22 Oct).**
- **Poor monsoon -> kharif output down -> food inflation -> rural demand down -> tractors and UV sales slow -> M&M volumes fall and MMFS collections worsen; RBI cannot cut because of food CPI -> funding cost stays high.**
- **Positive: GST relief and strong festive demand -> PV/tractor demand up -> MMFS disbursements +20%+ -> operating leverage lifts PAT.**

## Current situation
The stock is at a 52-week low (-25.9% in 3m, -12.1% in 1m) despite a 55% profit jump, because NII grew only 13% and brokerages see margin pressure. P/E 10.8 and 1.45x book is cheap vs Bajaj but reflects rural cyclicality. The AGM approved the dividend on 4 Nov.

## Upcoming
Q3 FY27 results (January 2027); December RBI MPC; festive-season disbursement and collection data.

## Bull / bear
Bull: pricing and funding stabilise margins, credit cost stays below 2%, tractor cycle recovers, re-rating from depressed multiple. Bear: further margin squeeze, rural stress, competition, regulatory tightening.

Uncertainty: book composition and Stage 3 numbers are model knowledge; PAT reported as Rs 882 cr (company) vs Rs 911 cr (screener consolidated).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.