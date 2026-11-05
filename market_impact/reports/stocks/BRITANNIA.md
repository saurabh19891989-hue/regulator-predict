# BRITANNIA — Britannia Industries Ltd.
*NIFTY_NEXT_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months -0.3%** (rank 110 / 101 of 200 for 3m / 12m); beta 0.73
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +14.0%): 3 months 49%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.3% … P90 +1.2%; plausible 12m relative-return range incl. stock-specific noise: -18.0% … +21.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -2.6% beta-adjusted vs realised market-adjusted move -6.7%); forward event exposure +1.3% (3m +0.8%; half assumed priced); company-specific events +0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.64 | +2.00 | +0.49 | +0.18 | -0.04 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.46 | +2.50 | +0.00 | -0.05 | +0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.76 | +1.80 | +0.00 | -0.09 | +0.04 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.75 | +0.00 | -1.33 | -0.23 | -0.20 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.56 | +0.00 | -0.40 | -0.57 | -0.60 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.38 | +0.00 | -1.40 | +0.09 | -0.07 | — |
| Wheat price (`F_WHEAT`) | +10% wheat | -1.27 | -1.20 | +0.00 | -0.01 | -0.05 | -1.3% |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -1.10 | -1.10 | +0.00 | +0.00 | +0.00 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -1.08 | -1.00 | +0.00 | -0.01 | -0.07 | +1.9% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.06 | -0.60 | -0.22 | -0.22 | -0.03 | +0.0% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.02 | +0.00 | +0.68 | -0.02 | +0.36 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.00 | +0.00 | -0.83 | -0.12 | -0.05 | +2.2% |
| FSSAI / packaged-food regulation intensity (`NEW_FOOD_SAFETY_REG`) | +1 = materially stricter packaged-food labelling/HFSS/online-sale rules | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Gold price (`F_GOLD`) | +8% gold (USD) | +0.96 | +1.00 | +0.00 | -0.04 | +0.00 | -8.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Sugar supply shock: 2025-26 output cut to ~306 lakh t, retail sugar at record, first duty-free raw sugar imports in a decade (`EV_SUGAR_SHORTFALL26`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.9% | -1.9% | -1.8 | -0.1 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.8 | +0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.9 | +0.0 | -0.5 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.2% | +1.1% | +2.0 | +0.1 | +0.0 | +0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.0% | -1.0% | -1.1 | +0.0 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.9% | -0.9% | -0.8 | -0.1 | -0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.7 | -0.1 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.4 | +0.2 | +0.2 |
| India 2027 wheat crop (harvest Mar-Apr 2027) below 2026's record ~120 MT (`EV_WHEAT27_CROP_BELOW`) | anticipated | 0.65 | -1.3% | -0.8% | -1.0 | +0.0 | -0.3 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.8 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +0.8 | +0.1 | +0.4 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BRITANNIA | +2.00% | +1.00% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → BRITANNIA | -1.90% | -0.57% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → BRITANNIA | +1.00% | +0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → BRITANNIA | +0.78% | +0.43% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_WHEAT → BRITANNIA | -0.60% | -0.39% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → BRITANNIA | +0.54% | +0.38% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BRITANNIA | -0.80% | -0.34% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BRITANNIA | -1.32% | -0.33% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → BRITANNIA | +0.54% | +0.30% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → BRITANNIA | +0.41% | +0.28% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → BRITANNIA | +0.36% | +0.24% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → BRITANNIA | -0.36% | -0.23% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → BRITANNIA | -0.92% | -0.23% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BRITANNIA | -0.80% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BRITANNIA | -1.20% | -0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_SUGAR → BRITANNIA | +2.78 | observed | -2.23% |
| 1 | F_FPI_FLOWS → BRITANNIA | -1.60 | events | -1.28% |
| 1 | F_GOLD → BRITANNIA | -1.05 | observed | -1.05% |
| 1 | F_REPO_IN → BRITANNIA | +1.00 | events | -0.80% |
| 1 | F_URBAN_DEMAND → BRITANNIA | +0.20 | events | +0.50% |
| 1 | F_RURAL_DEMAND → BRITANNIA | -0.25 | events | -0.45% |
| 1 | F_EDIBLE_OIL → BRITANNIA | +0.19 | observed | -0.19% |
| 2 | F_MONSOON → F_DAIRY → BRITANNIA | -1.56 | events | -0.17% |
| 1 | F_WHEAT → BRITANNIA | -0.13 | observed | +0.16% |
| 1 | F_USDINR → BRITANNIA | -0.37 | observed | +0.15% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → BRITANNIA | +0.40 | events | -0.02% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → BRITANNIA | +0.30 | events | -0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-09-30 | Top management rejig: N. Venkataraman moves to Deputy MD, R. Jayaraman to be CFO (already occurred; execution risk during transition) | other | 1.00 | +0.0% | +0.00% |
| 2026-11 | Interim dividend declaration with Q2 (Britannia typically pays an interim dividend; payout ~84% per screener) | corporate_action | 0.50 | +0.5% | +0.25% |
| 2026-11-06 | Q2 FY27 results (exact date not confirmed from filings; Trade Brains previewed Q2 expectations on 2026-11-04 so release is imminent) | results | 0.90 | -1.0% | -0.90% |
| 2026-12 | Price-increase / grammage action on core biscuit SKUs if wheat/palm/sugar remain elevated | guidance | 0.45 | +1.8% | +0.79% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# BRITANNIA (Britannia Industries Ltd.) - company profile as of 2026-11-05

## Business
Britannia is India's leading listed biscuit maker (Good Day, Tiger, Marie Gold, Milk Bikis, NutriChoice) with bread, cake, rusk and a growing dairy line. TTM sales are Rs 19,529 cr with Rs 3,600 cr EBITDA (18.4%) and Rs 2,610 cr profit; ROCE is 56% and leverage is negligible, so the equity is essentially a long-duration, high-payout (84%) compounding claim valued at 46x earnings (screener.in pack, 2026-11-05). Sales grew only 7% in FY26 and TTM, and the five-year CAGR is 7.8% (screener flags this as "poor"). Promoters (Wadia group) hold 50.55%; FIIs trimmed from 15.6% to 12.9% in two quarters while DIIs (LIC >5%) absorbed the supply. The stock closed at Rs 4,984, -15% over 12 months and at 52-week lows through late October.

## What moves the stock (ranked)
1. **Staples input basket: wheat, palm oil, sugar, dairy, packaging.** These five lines are about 49% of costs (model estimate; Britannia does not disclose exact shares in the sources fetched). The Rs 15,929 cr cost base means every 1% on the whole basket is about Rs 78 cr, or 2.2% of EBITDA. Sugar is +27.8% since June, Brent +15% in three months and edible oils +4%, while wheat is -14.7% in a month. Net, Q2/Q3 gross margin is under pressure from sugar, palm and packaging, with wheat the relief valve.
2. **Pricing power versus volume.** Biscuit price points (Rs 5-10) are sticky, so cost relief shows up as grammage cuts first and list-price moves later. Q1 FY27 operating margin 17% and the Q1 "margin miss" show the squeeze.
3. **Domestic demand (urban 60% / rural 40%).** +5pp urban demand growth is about +2.5 equity-value points; rural about +1.8.
4. **Rate/discount-rate and flows.** A 46x multiple makes the stock sensitive to bond yields and FPI flows; FIIs are net sellers for two quarters.
5. **Regulation.** GST (already at the low slab since the 2025 rationalisation, model knowledge; the 2026-10-08 Council made no rate changes), FSSAI packaged-food rules.

## Transmission examples
- **Middle East escalation (C_MIDEAST_CONFLICT) -> Brent up -> crude-linked laminates, freight and palm oil up -> Britannia gross margin down.** Order 1: Brent +10%; order 2: packaging +4%, palm oil +4% (biodiesel parity), diesel freight up; order 3: ~Rs 150-200 cr annualised cost, ~5% of EBITDA; order 4: company takes a 2-3% price/grammage action with a 2-3 quarter lag, volumes dip 1-2% in price-sensitive rural packs. Net equity effect about -1.5 to -2.5% over 6 months.
- **Brent up -> USD/INR up -> RBI holds rates -> rural real incomes squeezed (fuel and food inflation) -> mass biscuit volumes slow.** Order 2 in particular is visible in a Brent +50% 12-month move together with USD/INR +6.5%.
- **Monsoon/kharif outcome -> wheat and rural demand.** A good monsoon lowers food inflation and raises rural demand (+) while cutting wheat/sugar prices (+); a deficient monsoon flips both. The two channels have the same sign, so monsoon is a bigger lever than either node alone.
- **GST Council relief -> consumer wallet -> volumes.** A broad GST cut on packaged food would pull forward volume, but biscuits already benefit from the low slab, so upside here is limited versus household durables.
- **Global risk-off -> FPI outflows -> large-cap quality de-rating.** Higher US 10Y (4.89%, +9% since June) raises discount rates; FIIs already sold 2.7pp of the company in two quarters.

## Empirical cross-check
Pack betas (weekly, 3y, market-adjusted): gold +1.92 (t=3.1), DXY -1.99 (t=-2.6), wheat +1.29 (t=2.2). Only DXY has an obvious fundamental route (dollar strength = FPI outflows + dearer imports). The wheat sign contradicts the cost mechanism and is treated as a defensive-rotation artefact; gold is carried at half weight as a rural-wealth proxy.

## Current situation
Q1 FY27 (reported 2026-08-07): sales Rs 5,000 cr (+8%), operating profit Rs 838 cr (17%), net profit Rs 593 cr (+14%). The June-quarter operating margin was 17% versus 20% in the Dec-25 quarter. Management announced a rejig on 2026-09-30: N. Venkataraman moves to Deputy MD and R. Jayaraman becomes CFO. LIC crossed 5% on 2026-09-18. Promoter-group structure is under media scrutiny (Financial Express 2026-10-08). The Q2 FY27 print is imminent and the market is looking for margin guidance.

## Upcoming events
Q2 FY27 results (early November; date unverified), possible interim dividend, a price/grammage action if inputs persist, Q3 results in February 2027. See `company_events` in the JSON for probabilities and ranges.

## Bull case
Wheat deflation (-14.7% in a month) and any easing in sugar/palm restore 200-300 bp of margin by H2; rural recovery lifts volumes; the stock trades below its 10-year average P/E with ROCE of 56% and DIIs buying. A 10% re-rating from 46x to 50x on 20% EPS growth is plausible.

## Bear case
Sugar, palm and crude-linked packaging stay high, pricing lags, volumes weaken in rural packs and quick-commerce channel mix dilutes margin; FII selling continues; HFSS-style labelling rules hit high-sugar SKUs. A de-rating to 38-40x on flat EPS would be -15% to -20%.

## Uncertainties
No exact raw-material cost split or international share could be fetched in this run (annual-report disclosure not read); weights use model estimates and are labelled so. Q2 FY27 numbers were not available at write time.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.