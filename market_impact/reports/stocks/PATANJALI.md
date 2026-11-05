# PATANJALI — Patanjali Foods Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months +0.3%** (rank 101 / 93 of 200 for 3m / 12m); beta 0.87
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +31.1%): 3 months 50%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.9% … P90 +3.1%; plausible 12m relative-return range incl. stock-specific noise: -50.6% … +34.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.7 pp (model impact +1.5% beta-adjusted vs realised market-adjusted move -15.5%); forward event exposure +2.9% (3m +1.8%; half assumed priced); company-specific events -1.3%

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
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.3% | -3.3% | +0.0 | -1.1 | -1.9 | -0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.9% | -2.9% | -2.6 | -0.2 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.3% | +1.6% | +3.0 | +0.2 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.3 | +0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.1% | -1.1% | +0.0 | -3.3 | -0.7 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.9 | -0.1 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.9 | -0.1 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -2.6% | -0.9% | +0.0 | -1.2 | -1.2 | -0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -4.8% | -0.9% | +0.0 | -4.2 | -0.6 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.4 | -0.1 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.3% | +0.8% | +0.0 | +0.6 | +0.7 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -3.5% | -0.8% | -3.4 | -0.0 | -0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → PATANJALI | -2.64% | -2.64% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PATANJALI | +3.00% | +1.50% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → PATANJALI | -1.25% | -1.25% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_EDIBLE_OIL → PATANJALI | +0.89% | +0.89% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → PATANJALI | -0.79% | -0.79% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → PATANJALI | -0.71% | -0.71% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → PATANJALI | +0.60% | +0.60% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → PATANJALI | -0.60% | -0.60% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → PATANJALI | -0.56% | -0.56% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → PATANJALI | -0.53% | -0.53% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PATANJALI | -1.79% | -0.50% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → PATANJALI | -0.45% | -0.45% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_RURAL_DEMAND → PATANJALI | -0.43% | -0.43% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → PATANJALI | -0.41% | -0.41% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PATANJALI | -2.24% | -0.40% |

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