# PATANJALI — Patanjali Foods Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.0%** (rank 111 / 96 of 200 for 3m / 12m); beta 0.87
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +31.1%): 3 months 49%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.9% … P90 +2.1%; plausible 12m relative-return range incl. stock-specific noise: -16.4% … +61.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.6 pp (model impact +1.1% beta-adjusted vs realised market-adjusted move -15.5%); forward event exposure +2.3% (3m +1.6%; half assumed priced); company-specific events -1.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India effective import duty on crude edible oils (`NEW_EDIBLE_OIL_IMPORT_DUTY`) | +5 pp effective import duty on crude palm/soy/sunflower oil | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | — |
| FSSAI / packaged-food regulation intensity (`NEW_FOOD_SAFETY_REG`) | +1 = materially stricter packaged-food labelling/HFSS/online-sale rules | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.49 | +1.50 | +0.00 | -0.02 | +0.01 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | +1.44 | +1.50 | +0.00 | -0.01 | -0.05 | +1.9% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.29 | +1.20 | +0.07 | +0.01 | +0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.14 | +0.80 | +0.23 | +0.13 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.10 | -0.80 | -0.24 | -0.07 | +0.01 | -1.1% |
| US dollar index (`F_DXY`) | +3% DXY | -0.93 | +0.00 | -0.72 | -0.18 | -0.03 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.90 | +0.00 | -0.54 | -0.32 | -0.04 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.90 | +0.00 | +0.00 | -0.41 | -0.50 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.88 | +0.00 | -0.98 | +0.07 | +0.02 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +0.82 | +0.80 | +0.00 | -0.01 | +0.03 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +0.74 | +0.00 | +0.38 | +0.29 | +0.07 | +1.2% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.68 | +0.00 | +0.34 | +0.06 | +0.27 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.8% | -2.8% | -2.6 | -0.2 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.3% | +1.6% | +3.0 | +0.2 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.3 | +0.1 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.4 | -0.1 | -0.3 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.0% | -0.7% | +0.0 | -2.5 | -0.5 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | -0.1 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.7% | +0.7% | +0.6 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.1% | +0.6% | +0.0 | +0.5 | +0.6 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -3.5% | -0.6% | -3.4 | -0.0 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.5 | -0.1 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.2% | -0.6% | +0.0 | -1.0 | -1.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PATANJALI | +3.00% | +1.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → PATANJALI | -1.80% | -0.32% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → PATANJALI | +0.45% | +0.31% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → PATANJALI | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → PATANJALI | -1.15% | -0.29% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PATANJALI | -1.12% | -0.28% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PATANJALI | -0.60% | -0.25% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → PATANJALI | +0.45% | +0.25% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → PATANJALI | +0.34% | +0.23% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → PATANJALI | +0.60% | +0.21% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → PATANJALI | +0.30% | +0.20% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → PATANJALI | -0.30% | -0.20% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → PATANJALI | +0.24% | +0.19% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → PATANJALI | -1.04% | -0.19% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → PATANJALI | +0.33% | +0.18% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → PATANJALI | -1.60 | events | -1.92% |
| 1 | F_REPO_IN → PATANJALI | +1.00 | events | -0.60% |
| 1 | F_RURAL_DEMAND → PATANJALI | -0.25 | events | -0.38% |
| 1 | F_USDINR → PATANJALI | -0.37 | observed | +0.30% |
| 1 | F_EDIBLE_OIL → PATANJALI | +0.19 | observed | +0.28% |
| 1 | F_URBAN_DEMAND → PATANJALI | +0.20 | events | +0.16% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → PATANJALI | +0.40 | events | -0.00% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → PATANJALI | +0.30 | events | -0.00% |
| 3 | F_BRENT → F_CHEM_FEEDSTOCK → F_PACKAGING → PATANJALI | +0.00 | observed | -0.00% |
| 4 | F_BRENT → F_CHEM_FEEDSTOCK → F_PETROCHEM_SPREADS → F_PACKAGING → PATANJALI | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (mid-Nov; date unverified) | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | FDA test results on cow ghee batch | regulatory | 0.60 | -2.2% | -1.35% |
| 2027-02 | Q3 FY27 results; Budget (1 Feb) edible-oil duty review | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Patanjali Foods — what moves the stock

**Business.** Patanjali Foods is India's large edible-oil refiner and marketer (ex Ruchi Soya) with a growing food and FMCG business. About two-thirds of revenue is oil (approximate, model knowledge), sold on a margin of just 4-5%. Q1 FY27: sales Rs 11,337 cr (+29%), operating margin 4.8%, PAT Rs 336 cr (screener.in, 2026-11-05). Q2 results are due in mid-November.

## Ranked drivers
1. **India's edible-oil import duty (NEW_EDIBLE_OIL_IMPORT_DUTY).** A duty cut devalues inventory and narrows the protection for refiners; shares fell after the 24 Sep 2026 cut.
2. **Global vegetable-oil prices and the refining spread.** Direction is mixed: rising prices give inventory gains but hurt working capital.
3. **Food safety regulation.** Ghee batch recall (MP FDA, 24 Oct) and the Maharashtra FDA action.
4. **USD/INR.** Crude oil is imported in dollars.
5. **Rural/urban consumption and the FMCG mix shift.**

## Worked transmission chains
- **Palm oil rally on biodiesel demand (Brent up) -> global oil prices up -> Patanjali inventory gains in the first quarter, then lower volume and tighter working capital -> government cuts duty to cool inflation -> inventory losses (4th order).** This sequence is visible in 2026: Brent +15% in 3 months, duty cut on 24 Sep.
- **Brent up -> INR weaker (94.49) -> imported oil dearer in rupees -> higher shelf prices -> RBI holds -> consumers trade down.**
- **Weak monsoon -> lower domestic oilseed crop -> higher import dependence -> duty cuts to protect consumers -> compresses refiner margin.**
- **Regulatory test of ghee -> recall -> brand damage on Food & FMCG, the growth leg.**

## Current situation
The stock rallied about 16% in four sessions in September on FY27 growth targets (Upstox 2026-09-22), then gave back some on the duty cut. SBI lost a Rs 1,759 cr insolvency case against a guarantor of Patanjali Foods (Moneycontrol 2026-09-23); the details of the guarantee were not retrieved. Segment mix and cost shares are approximate.

## Upcoming
Q2 FY27 results (mid-Nov 2026), FDA test results on ghee, Budget (Feb 2027) duty review.

## Bull / bear
**Bull:** food mix rising, margin recovery, duty restoration. **Bear:** repeated duty cuts, recalls, thin margin amplifying any cost error, related-party risk. Confidence low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.