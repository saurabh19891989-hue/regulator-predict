# NESTLEIND — Nestle India Ltd.
*NIFTY_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months -0.1%** (rank 114 / 106 of 200 for 3m / 12m); beta 0.85
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.8%): 3 months 48%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.8% … P90 +4.0%; plausible 12m relative-return range incl. stock-specific noise: -24.8% … +24.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.7 pp (model impact +1.3% beta-adjusted vs realised market-adjusted move -13.7%); forward event exposure +1.4% (3m +0.5%; half assumed priced); company-specific events -0.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.02 | +2.20 | +0.00 | -0.16 | -0.03 | — |
| FSSAI / packaged-food regulation intensity (`NEW_FOOD_SAFETY_REG`) | +1 = materially stricter packaged-food labelling/HFSS/online-sale rules | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.92 | +0.00 | -1.93 | +0.07 | -0.06 | — |
| Milk / dairy input cost (`F_DAIRY`) | +8% milk procurement price | -1.77 | -1.60 | +0.00 | -0.01 | -0.16 | — |
| Cocoa, coffee, tea prices (`F_COCOA_COFFEE_TEA`) | +15% beverage commodities | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.41 | -1.30 | -0.07 | -0.03 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.08 | +0.00 | +0.76 | +0.51 | -0.19 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.05 | +0.00 | -0.07 | -1.05 | +0.08 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.82 | +0.00 | -0.83 | +0.12 | -0.10 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.80 | +0.00 | -0.56 | -0.08 | -0.16 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.76 | +0.00 | +0.00 | -0.27 | -0.49 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -0.74 | +0.00 | -0.59 | -0.23 | +0.08 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.5% | -3.5% | +0.0 | -1.1 | -2.0 | -0.4 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -2.3 | +0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.3 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.7 | +0.2 | -0.4 |
| Sugar supply shock: 2025-26 output cut to ~306 lakh t, retail sugar at record, first duty-free raw sugar imports in a decade (`EV_SUGAR_SHORTFALL26`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | +0.0 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -2.0% | -0.7% | +0.0 | -0.6 | -1.0 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.2% | +0.7% | +0.0 | +0.4 | +0.6 | +0.2 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.4% | -0.6% | -1.3 | -0.1 | -0.0 | -0.0 |
| India 2027 wheat crop (harvest Mar-Apr 2027) below 2026's record ~120 MT (`EV_WHEAT27_CROP_BELOW`) | anticipated | 0.65 | -0.8% | -0.6% | -0.5 | +0.0 | -0.4 | +0.0 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.0 | -0.5 | +0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | +0.5% | +0.5% | +0.0 | +0.0 | +0.3 | +0.2 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -2.0% | -0.5% | +0.0 | -2.0 | +0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → NESTLEIND | -1.30% | -0.52% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → NESTLEIND | -1.50% | -0.37% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → NESTLEIND | -1.30% | -0.35% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → NESTLEIND | -0.52% | -0.31% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → NESTLEIND | -1.30% | -0.29% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → NESTLEIND | -0.33% | -0.21% |
| 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → NESTLEIND | -0.58% | -0.21% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → NESTLEIND | +0.35% | +0.20% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_REPO_IN → NESTLEIND | -0.22% | -0.20% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ F_CPI_IN → F_REPO_IN → NESTLEIND | -0.45% | -0.20% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_WHEAT → NESTLEIND | -0.30% | -0.20% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → NESTLEIND | +0.27% | +0.19% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_DAIRY → NESTLEIND | +0.26% | +0.17% |
| 2 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → F_URBAN_DEMAND → NESTLEIND | +0.21% | +0.17% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → NESTLEIND | -1.30% | -0.16% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REPO_IN → NESTLEIND | +1.00 | events | -1.30% |
| 1 | F_SUGAR → NESTLEIND | +2.78 | observed | -0.83% |
| 1 | F_URBAN_DEMAND → NESTLEIND | +0.20 | events | +0.44% |
| 2 | F_MONSOON → F_DAIRY → NESTLEIND | -1.56 | events | -0.40% |
| 1 | F_RURAL_DEMAND → NESTLEIND | -0.25 | events | -0.23% |
| 1 | F_USDINR → NESTLEIND | -0.37 | observed | +0.15% |
| 1 | F_EDIBLE_OIL → NESTLEIND | +0.19 | observed | -0.10% |
| 1 | F_WHEAT → NESTLEIND | -0.13 | observed | +0.08% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → NESTLEIND | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → NESTLEIND | +0.30 | events | -0.01% |
| 4 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → NESTLEIND | -0.47 | observed | -0.00% |
| 4 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → NESTLEIND | +0.40 | events | -0.00% |

## Analyst profile (agent research, sourced)
# Nestle India — what moves the stock

**Business.** Maggi noodles, Nescafe, KitKat, dairy and infant nutrition, sold mostly in urban India with a rapidly growing quick-commerce share. Q2 FY27: sales Rs 6,788 cr (+20%), operating margin 24%, PAT Rs 1,010 cr (+36%) while advertising spend rose 46% (screener.in; Adgully, 2026-10-15). At 60.9x earnings the stock needs near-perfect execution and fell ~9% on 15 Oct on management's inflation comment, then to a six-month low after FSSAI notices (Moneycontrol, 2026-10-22).

## Ranked drivers
1. **Milk, coffee and cocoa costs.** Together ~38% of costs; none have been cheap in 2026. Each is worth roughly -1.5% equity value per standard shock.
2. **Urban demand and quick commerce.** The main growth engine; +5pp urban growth is worth about +2% equity value.
3. **Valuation duration.** P/E of 61 means rate moves hit the multiple harder than operations.
4. **Regulation (FSSAI).** Notices on baby-food claims and an unsafe sample reported on 3 Oct add tail risk to a high-margin segment.
5. **Packaging, wheat, edible oil, sugar, USD/INR.** Smaller cost lines.

## Worked transmission chains
- **Middle East escalation -> Brent up (94.99) -> packaging film and freight costs up -> Nestle packaging cost +10% -> EBITDA -1% after pricing offsets (3rd order).** Brent up -> INR weaker -> imported coffee/cocoa dearer -> price hike needed -> volume elasticity in Maggi (4th order).
- **Weak 2026 monsoon -> forage and fodder costs up -> milk procurement prices up -> milk products cost +8% -> gross margin -1.5pp -> management signals price hikes.**
- **Food inflation 5.5% (Oct headline) -> RBI stays on hold -> high valuation multiples de-rate -> stock falls even without earnings change.**
- **FSSAI claim enforcement -> label changes on Lactogen/Cerelac -> infant-nutrition volume disruption -> the high-margin portfolio shrinks -> EBITDA margin down.**

## Current situation
Sales growth has been above 19% for three straight quarters. Management accepted that inflation is a reality (ET 2026-10-15); HSBC still sees 16% upside (Moneycontrol 2026-10-16). Details of the FSSAI show-cause were taken from headlines only; the notice text itself was not retrieved.

## Upcoming
Q3 FY27 results (about Feb 2027), FSSAI response, price actions and festive-season quick-commerce data.

## Bull / bear
**Bull:** volume-led growth, commodity easing, pricing power. **Bear:** milk/cocoa inflation, a regulatory event on infant nutrition, de-rating from 61x. Cost shares are model-knowledge approximations.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.