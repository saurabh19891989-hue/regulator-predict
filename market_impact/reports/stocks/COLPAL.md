# COLPAL — Colgate Palmolive (India) Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.5%**, **12 months +1.1%** (rank 72 / 59 of 200 for 3m / 12m); beta 0.91
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.5%): 3 months 52%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.2% … P90 +2.5%; plausible 12m relative-return range incl. stock-specific noise: -18.4% … +43.3%
- Decomposition (12m): 0.5 × forward event exposure +2.3% (3m +0.8%; half assumed priced) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.3% (beta-adjusted) vs a realised market-adjusted move of -19.3% — gap +20.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Oral-care competition intensity (HUL, Dabur, Patanjali, Himalaya) (`NEW_ORAL_CARE_COMPETITION`) | +1 = materially sharper discounting/advertising by rivals in toothpaste | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.42 | +2.00 | +0.37 | +0.11 | -0.06 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.89 | +2.00 | +0.00 | -0.12 | +0.02 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.55 | +1.50 | +0.06 | +0.00 | -0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.45 | +1.50 | +0.00 | -0.08 | +0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.07 | -1.00 | -0.05 | -0.02 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.90 | +0.00 | -0.48 | -0.22 | -0.19 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.85 | +0.80 | +0.02 | +0.01 | +0.01 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.82 | +0.00 | +0.96 | -0.09 | -0.05 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.71 | +0.00 | +0.45 | -0.00 | +0.26 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.67 | +0.00 | -0.87 | +0.20 | +0.00 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -0.65 | -0.60 | +0.00 | -0.01 | -0.04 | +1.9% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.65 | -0.40 | -0.11 | -0.13 | -0.01 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.9% | -1.9% | -1.8 | -0.1 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.1% | +1.1% | +2.0 | +0.1 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -1.2 | +0.2 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.6 | +0.0 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.1% | +0.6% | +0.5 | +0.3 | +0.2 | +0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -1.9% | -0.5% | -0.9 | -0.6 | -0.4 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -2.6% | -0.5% | -2.5 | -0.1 | -0.1 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.1% | -0.5% | -1.0 | -0.1 | -0.0 | -0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -3.6% | -0.4% | -2.6 | -0.7 | -0.3 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.4% | +0.4% | +0.4 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → COLPAL | +2.00% | +1.00% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → COLPAL | +0.60% | +0.42% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → COLPAL | -1.00% | -0.42% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → COLPAL | +0.60% | +0.33% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → COLPAL | +0.45% | +0.31% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → COLPAL | +0.52% | +0.29% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → COLPAL | +0.40% | +0.27% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → COLPAL | -1.00% | -0.27% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → COLPAL | -0.40% | -0.26% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → COLPAL | -0.40% | -0.24% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → COLPAL | -0.88% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → COLPAL | -1.20% | -0.22% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_RURAL_DEMAND → COLPAL | +0.23% | +0.19% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → COLPAL | -0.77% | -0.19% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → COLPAL | -0.77% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → COLPAL | -1.60 | events | -1.28% |
| 1 | F_REPO_IN → COLPAL | +1.00 | events | -1.00% |
| 1 | F_RURAL_DEMAND → COLPAL | -0.25 | events | -0.50% |
| 1 | F_URBAN_DEMAND → COLPAL | +0.20 | events | +0.30% |
| 1 | F_EDIBLE_OIL → COLPAL | +0.19 | observed | -0.11% |
| 1 | F_USDINR → COLPAL | -0.37 | observed | +0.09% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → COLPAL | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → COLPAL | +0.30 | events | -0.01% |
| 4 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → COLPAL | -0.47 | observed | -0.00% |
| 4 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → COLPAL | +0.40 | events | -0.00% |
| 4 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → COLPAL | +0.30 | events | -0.00% |
| 4 | C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → COLPAL | -0.10 | events | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Interim dividend Rs 24/share declared 2026-10-22 (record/pay date unverified) | corporate_action | 0.95 | +0.7% | +0.66% |
| 2027-01 | Q3 FY27 results: volume growth and A&P intensity | results | 0.95 | +0.0% | +0.00% |
| 2027-06 | Parent portfolio action or open offer (low probability) | corporate_action | 0.05 | +5.0% | +0.25% |

## Analyst profile (agent research, sourced)
# COLPAL (Colgate-Palmolive (India) Ltd.) - company profile as of 2026-11-05

## Business
Colgate-Palmolive India is the leading toothpaste and toothbrush company. It is debt-free with ROCE of 108% and distributes more than 100% of earnings. TTM sales are Rs 6,391 cr (+9%) with EBITDA Rs 1,908 cr (30%). The Sep-26 quarter delivered sales of Rs 1,706 cr (+12%), operating margin of 28% (31% a year earlier) and PAT of Rs 342 cr (+4%), a narrow miss; advertising was stepped up. The stock is Rs 1,688, -23% in 12 months, near its 52-week low of Rs 1,564 (screener.in pack, 2026-11-05). The US parent holds 51%.

## What moves the stock (ranked)
1. **Category volume growth and share versus HUL, Dabur and Patanjali.** Advertising spend rose, taking 3 points off the margin; competition is the largest swing factor.
2. **Rural and urban demand.** Rural is ~40% of sales.
3. **Input costs.** Palm-derived surfactants, packaging and plastics together ~24% of costs.
4. **GST and policy.** The stock rose ~7% on 2026-10-09 after the GST Council meeting, though the Council made no broad rate cuts; the specific trigger was not verified.
5. **Valuation and rates.** A 33x P/E with 2.9% yield makes it a bond proxy.

## Transmission examples
- **Middle East escalation -> Brent up -> polymer packaging and freight up -> gross margin down; also palm oil up -> surfactant and glycerin cost up.** Brent +10% costs ~1.6% of EBITDA; with packaging and palm it can reach 4-5%. Management then raises A&P efficiency or price; volumes soften in rural towns.
- **Brent up -> USD/INR up -> imported intermediates, toothbrushes and royalty cost up** (small, -0.25).
- **Good monsoon -> rural income -> toothpaste penetration and premium trade-up** (+2).
- **Rival launches (HUL, Patanjali) -> Colgate raises A&P -> margin down** (competition).
- **US parent portfolio action -> India sale or restructuring** (low probability tail).

## Current situation
Q2 miss and the A&P step-up triggered the 52-week low on 2026-10-22. Interim dividend Rs 24. FIIs 13.7%, DIIs 15.5%, public 19.8%.

## Upcoming events
Q3 FY27 results (January 2027), dividend record date.

## Bull case
Volume growth recovers to 6-8% with margin back to 31%; yield support and defensive demand.

## Bear case
Share losses continue, A&P stays elevated, margin 26-27% and de-rating to 28x: -15%.

## Uncertainties
Cost shares, revenue mix and rural share are model estimates; filings were not fetched.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.