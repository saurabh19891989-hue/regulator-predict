# GODREJCP — Godrej Consumer Products Ltd.
*NIFTY_NEXT_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.1%**, **12 months +1.3%** (rank 59 / 68 of 200 for 3m / 12m); beta 0.92
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.5%): 3 months 54%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.6% … P90 +3.5%; plausible 12m relative-return range incl. stock-specific noise: -7.7% … +38.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.4% beta-adjusted vs realised market-adjusted move -18.2%); forward event exposure +2.8% (3m +1.5%; half assumed priced); company-specific events +2.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.52 | +2.00 | +0.40 | +0.16 | -0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.38 | +0.00 | -1.60 | -0.31 | -0.47 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.92 | +2.00 | +0.00 | -0.07 | -0.01 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -1.76 | -1.70 | +0.00 | -0.01 | -0.05 | +1.9% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.59 | +0.00 | -1.35 | -0.07 | -0.17 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.40 | +1.50 | +0.00 | -0.10 | -0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.30 | +0.00 | -1.20 | -0.04 | -0.07 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.19 | -0.90 | -0.07 | -0.19 | -0.03 | +0.0% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.04 | -0.90 | -0.11 | -0.03 | +0.00 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.87 | +0.00 | +0.58 | +0.08 | +0.22 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.76 | +0.80 | -0.07 | +0.01 | +0.02 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.72 | +0.00 | +1.00 | -0.15 | -0.12 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.71 | +0.00 | -0.12 | -0.58 | -0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.7% | -1.7% | -1.8 | +0.2 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.5 | +0.0 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.1% | +1.1% | +1.6 | +0.1 | +0.3 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -0.9 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.9% | +0.9% | +2.0 | -0.2 | +0.0 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.7% | -0.9% | -2.0 | -1.0 | -0.6 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.4 | +0.0 | -0.3 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -0.5% | -0.5% | -0.4 | +0.0 | -0.1 | -0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.1% | -0.4% | -0.9 | -0.1 | -0.0 | -0.0 |
| Windfall/export levy re-set: petrol nil, diesel Rs11.5/l, ATF ~Rs11/l (31 Oct); excise reportedly cut (3 Nov, unverified) (`EV_EXPORT_LEVY_REVISIONS`) | occurred | 1.00 | +0.4% | +0.4% | +0.0 | +0.3 | +0.0 | +0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.4% | -0.4% | -0.4 | +0.0 | +0.0 | +0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.05 | -7.9% | -0.4% | -4.1 | -2.2 | -1.4 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GODREJCP | +2.00% | +1.00% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GODREJCP | +1.17% | +0.64% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GODREJCP | -1.98% | -0.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GODREJCP | -0.90% | -0.38% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → GODREJCP | +0.45% | +0.31% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → GODREJCP | -1.04% | -0.26% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → GODREJCP | +0.45% | +0.25% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → GODREJCP | -0.90% | -0.24% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → GODREJCP | +0.34% | +0.23% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → GODREJCP | +0.42% | +0.23% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → GODREJCP | -0.36% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → GODREJCP | -1.20% | -0.22% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → GODREJCP | +0.30% | +0.20% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → GODREJCP | -4.05% | -0.20% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → GODREJCP | -0.30% | -0.20% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → GODREJCP | -1.60 | events | -1.28% |
| 1 | F_REFINING_MARGIN → GODREJCP | +1.54 | observed | -1.08% |
| 1 | F_REPO_IN → GODREJCP | +1.00 | events | -0.90% |
| 1 | F_URBAN_DEMAND → GODREJCP | +0.20 | events | +0.40% |
| 1 | F_RURAL_DEMAND → GODREJCP | -0.25 | events | -0.38% |
| 1 | F_EDIBLE_OIL → GODREJCP | +0.19 | observed | -0.32% |
| 1 | F_USDINR → GODREJCP | -0.37 | observed | -0.30% |
| 2 | F_DXY → C_AFRICA_LATAM → GODREJCP | +0.74 | observed | -0.04% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → GODREJCP | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → GODREJCP | +0.30 | events | -0.01% |
| 4 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → GODREJCP | -0.47 | observed | -0.00% |
| 4 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → GODREJCP | +0.40 | events | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-10-06 | Indonesia Kendal manufacturing plant phase 1 opened (Rs 250 cr investment); ramp-up through FY28 | capex | 1.00 | +0.8% | +0.75% |
| 2026-11 | Interim dividend Rs 5/share (declared with Q2 on 2026-10-29); record/payment date unverified | corporate_action | 0.95 | +0.3% | +0.28% |
| 2026-12 | Calibrated price increases across soaps and household insecticides to offset palm/crude inflation | guidance | 0.70 | +1.8% | +1.22% |
| 2026-12 | Further promoter-group block deals / family restructuring of stake (Godrej Industries sell-down 2026-09-24) | corporate_action | 0.25 | -1.0% | -0.25% |
| 2027-02 | Q3 FY27 results; commodity pass-through and Indonesian volume trajectory | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# GODREJCP (Godrej Consumer Products Ltd.) - company profile as of 2026-11-05

## Business
Godrej Consumer Products sells soaps, household insecticides, hair colour, air and fabric care in India and has material businesses in Indonesia, Africa and Latin America. TTM sales are Rs 16,537 cr with EBITDA Rs 3,343 cr (20%) and profit Rs 1,977 cr. Sales rose 19% y/y in the September quarter (Rs 4,413 cr) and profit rose 14% to Rs 523 cr, but the operating margin fell to 19% from 20%, and the stock dropped 7% on 2026-10-30 to a four-year low of about Rs 868 (-25% in 12 months). Promoters hold 53.05%; FIIs have sold from 13.9% to 11.0% in two quarters (screener.in pack, 2026-11-05).

## What moves the stock (ranked)
1. **Palm oil and derivatives (soaps).** About 18% of costs (model estimate). A 10% rise costs about 7% of EBITDA before pass-through. This is the largest single driver and the explicit reason management gave for 'calibrated pricing actions'.
2. **Crude-linked inputs and packaging.** LAB, solvents, aerosol propellants and polymer packaging add another ~29% of costs with partial linkage to Brent. Brent is +15% in 3 months and +50% in 12 months.
3. **Pricing power and volume in India (urban 60%/rural 40%).** Household insecticide is rural-heavy and weather-sensitive; soaps are mass-market and price-sensitive.
4. **Indonesia and Africa/LatAm.** About 45% of sales; translation, local inflation and execution matter. The Kendal plant phase 1 opened 2026-10-06 (Rs 250 cr).
5. **Valuation and flows.** 41.8x P/E, FII selling (-2.95pp in two quarters), promoter-group block deals (Godrej Industries sold 0.5%, family bought 1%), rates.

## Transmission examples
- **Middle East escalation -> Brent up -> crude derivatives and packaging up -> margin down.** Brent +10% adds about 0.85% of the cost base (Rs 112 cr, 3.4% of EBITDA). Order 2: palm oil rises as biodiesel parity rises. Order 3: the company announces price hikes of 3-5% on soaps and insecticides; order 4: volumes soften 1-2% in price-sensitive rural packs and distributors destock. Net equity effect about -1.5 to -2.5%.
- **Brent up -> USD/INR up -> palm oil (USD-priced) dearer in rupees -> soap noodle cost up.** The FX leg of the palm import means Indian margins fall even if USD palm is flat. Offsetting: Indonesian and African subsidiary earnings translate into more rupees.
- **Monsoon -> rural demand -> household insecticide and soap volumes.** A strong monsoon boosts mosquito-season demand for Good Knight and HIT (+) and rural incomes (+), while also easing food inflation. The channel appears small in the weekly regression but is the base of H1 volume growth.
- **Indonesia growth/IDR -> Indonesian EBITDA -> group EBITDA.** +1pp Indonesian growth adds about +0.25 equity points; IDR weakness reduces INR-translated profit.
- **Rate cut -> discount rate down -> long-duration staples re-rate.** At 42x, a 25 bp cycle move is worth about 0.9 points.

## Empirical cross-check
Significant market-adjusted co-movements: refining margins -1.02 (t=-2.3, consistent with crude-derivative inputs), Fed funds +3.15 (t=+2.2, no clear mechanism; ignored), silver +1.16 (t=+2.1, ignored). Brent -0.68 (t=-1.4) matches the sign of the cost mechanism.

## Current situation
Management's Q2 update on 2026-10-05 flagged high-teens revenue growth with 'calibrated pricing actions' for palm oil and crude inflation (NDTV Profit). The full results on 2026-10-29 showed profit +14% to Rs 523 cr, beating revenue estimates but with margin contraction; the shares fell 7% the next day (Business Standard, Upstox). Nomura reduced its target from Rs 1,110 to Rs 950 but kept Buy (Moneycontrol 2026-11-02). On the corporate side, Godrej Industries sold 0.5% (Rs 450 cr) and four family members bought 1% (Rs 900 cr) in late September.

## Upcoming events
Price increases in December; Q3 FY27 results in February 2027; possible further promoter-group stake adjustments; Indonesian capacity ramp-up. Probabilities are in the JSON `company_events`.

## Bull case
Palm and crude ease, pricing sticks and the margin returns to 21-22% by H2 FY28 on high-teens sales growth; at 42x trailing earnings the stock has de-rated from 1,275 to 868 and DIIs are buying.

## Bear case
Input inflation persists, pricing lags and the margin falls to 17-18%; volumes in rural packs soften; Africa and Indonesia disappoint; FII selling continues. A fall to 35x on flat EPS would be -15% to -20%.

## Uncertainties
The segment revenue split, exact cost shares and net debt were not re-fetched from filings; they are model estimates (confidence medium/low). Article text for the Q2 call was not retrievable in this run (only headlines).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.