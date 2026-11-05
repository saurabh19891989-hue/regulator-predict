# DABUR — Dabur India Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months -0.4%** (rank 150 / 128 of 200 for 3m / 12m); beta 0.92
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.5%): 3 months 48%, 12 months 47%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.6% … P90 +1.5%; plausible 12m relative-return range incl. stock-specific noise: -28.0% … +26.3%
- Decomposition (12m): 0.5 × forward event exposure -0.0% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.3% (beta-adjusted) vs a realised market-adjusted move of -12.9% — gap +12.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.03 | +0.01 | +0.04 | -0.02 |
| Sector | +0.29 | +0.25 | +0.53 | +0.22 |
| Theme | +0.00 | -0.03 | -0.03 | -0.02 |
| Geopolitics | +0.00 | -0.02 | -0.02 | -0.01 |
| Company catalysts | -0.24 | +0.00 | -0.24 | -0.24 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.53 | -0.24 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.39** | **-0.41** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.02 | +2.00 | +0.00 | -0.00 | +0.02 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.52 | +1.50 | +0.00 | -0.00 | +0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.44 | +1.00 | +0.37 | +0.09 | -0.02 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -1.40 | -1.40 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.13 | +0.00 | -0.72 | -0.16 | -0.25 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.10 | -1.00 | -0.08 | -0.02 | +0.00 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.89 | +0.00 | +0.96 | -0.07 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.88 | +0.90 | -0.05 | +0.01 | +0.01 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.87 | +0.00 | +0.53 | +0.08 | +0.26 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.85 | -0.60 | -0.07 | -0.18 | +0.00 | +0.0% |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -0.75 | -0.70 | +0.00 | -0.01 | -0.04 | +1.9% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.59 | +0.00 | -0.46 | -0.05 | -0.08 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -0.58 | +0.00 | -0.30 | -0.24 | -0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.54 | +0.00 | -0.72 | +0.18 | -0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.9% | -1.9% | -2.0 | +0.1 | -0.0 | -0.0 |
| Sugar supply shock: 2025-26 output cut to ~306 lakh t, retail sugar at record, first duty-free raw sugar imports in a decade (`EV_SUGAR_SHORTFALL26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.7 | -0.1 | -0.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.2% | +1.1% | +2.3 | -0.1 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -1.0 | +0.2 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +0.8 | +0.2 | +0.3 | +0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.3% | -0.6% | -1.3 | -0.4 | -0.5 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +0.7% | +0.5% | +0.0 | +0.6 | +0.1 | +0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.1% | -0.5% | -1.0 | -0.1 | -0.0 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.4% | +0.4% | +0.5 | -0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DABUR | +2.25% | +1.13% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → DABUR | +0.78% | +0.43% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → DABUR | +0.60% | +0.42% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → DABUR | -1.00% | -0.42% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → DABUR | +0.60% | +0.33% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → DABUR | -1.32% | -0.33% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → DABUR | +0.45% | +0.31% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → DABUR | +0.40% | +0.27% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → DABUR | -1.00% | -0.27% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → DABUR | -0.40% | -0.26% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → DABUR | -1.35% | -0.24% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → DABUR | -0.86% | -0.22% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → DABUR | -0.86% | -0.22% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → DABUR | -0.84% | -0.21% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_RURAL_DEMAND → DABUR | +0.23% | +0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → DABUR | -1.60 | events | -1.44% |
| 1 | F_SUGAR → DABUR | +2.78 | observed | -1.11% |
| 1 | F_REPO_IN → DABUR | +1.00 | events | -1.00% |
| 1 | F_RURAL_DEMAND → DABUR | -0.25 | events | -0.50% |
| 1 | F_URBAN_DEMAND → DABUR | +0.20 | events | +0.30% |
| 1 | F_USDINR → DABUR | -0.37 | observed | -0.18% |
| 1 | F_EDIBLE_OIL → DABUR | +0.19 | observed | -0.13% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → DABUR | +0.40 | events | -0.02% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → DABUR | +0.30 | events | -0.02% |
| 4 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → DABUR | -0.47 | observed | -0.00% |
| 4 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → DABUR | +0.40 | events | -0.00% |
| 4 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → DABUR | +0.30 | events | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-13 | CEO Mohit Malhotra steps down; Herjit Singh Bhalla takes over (global CEO transition) | other | 0.95 | -0.5% | -0.47% |
| 2026-12 | Sesa Care merger effective-date filings | corporate_action | 0.60 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results (Oct-Dec); winter portfolio (chyawanprash) and rural recovery | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Dabur India — what moves the stock

**Business.** Dabur sells Ayurvedic and natural products: Chyawanprash, honey, Real juices, Dabur Red toothpaste, hair oils, Odonil and Odomos. About a fifth of sales are international. Promoters own 66%. Q2 FY27: sales Rs 3,563 cr (+11.7%), operating margin 18%, PAT about Rs 500 cr (+12%) (screener.in; Moneycontrol, 2 to 4 Nov 2026). The stock is -25% in twelve months at 33.7x earnings.

## Ranked drivers
1. **Rural and urban volume growth.** The Oct 6 business update said FMCG delivered its strongest performance in recent quarters with rural ahead of urban.
2. **Packaging, edible oil, sugar and crude-linked inputs.** The industry expects margin pressure in H2 (Economic Times 2026-10-18).
3. **Management change.** Global CEO Mohit Malhotra resigns effective 13 Nov; Herjit Singh Bhalla named successor.
4. **Valuation duration and FPI flows.**
5. **Regulation and GST.**

## Worked transmission chains
- **Middle East escalation -> Brent up -> PET, paraffin and freight costs up -> home-care and oral-care margin down -> price hikes -> rural elasticity (4th order).**
- **Brent up -> INR weaker -> RBI stays on hold -> yields up -> FMCG multiples compress (33.7x to lower).** Rupee weakness helps international translation slightly.
- **Weak monsoon -> rural incomes squeezed -> health-food and Dabur Red volumes slow in rural stockists -> operating leverage turns negative.**
- **Sugar +28% since June -> Real juice cost up -> Foods margin down; offset by duty cut on edible oils.**

## Current situation
Q2 beat estimates; Nomura says Buy, Goldman Neutral (NDTV Profit 2026-10-07). NCLT approved the Sesa Care merger on 25 Sep. The CEO change was announced alongside results, which markets may read as uncertainty about the strategy. Primary filings were not read; CEO details are from headline reports.

## Upcoming
CEO transition (13 Nov), Q3 results (about Feb 2027), Sesa Care effective date, winter-portfolio sell-in.

## Bull / bear
**Bull:** volume recovery, rural strength, low valuation. **Bear:** leadership change, input costs, rural weakness. Cost shares are approximate and from model knowledge.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.