# TRENT — Trent Ltd.
*NIFTY_50 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.2%**, **12 months +1.1%** (rank 92 / 82 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +51.3%): 3 months 50%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.6% … P90 +3.7%; plausible 12m relative-return range incl. stock-specific noise: -77.6% … +65.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +1.7% beta-adjusted vs realised market-adjusted move +4.7%); forward event exposure +2.4% (3m +1.1%; half assumed priced); company-specific events +2.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +5.01 | +5.00 | +0.00 | +0.01 | -0.00 | — |
| Value-fashion and mass-retail competition intensity (`NEW_VALUE_FASHION_COMPETITION`) | +1 = materially sharper expansion/discounting by Reliance Trends/Yousta, Max, Style Union, Myntra, V-Mart | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.29 | +0.00 | -2.15 | +0.04 | -0.18 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.20 | +1.50 | +0.98 | -0.18 | -0.10 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.09 | +1.00 | +0.82 | +0.28 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.80 | -1.50 | -0.18 | -0.06 | -0.05 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.63 | +1.50 | +0.00 | +0.02 | +0.12 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.60 | +1.50 | +0.05 | +0.02 | +0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.35 | +0.00 | +0.00 | -0.57 | -0.79 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.28 | +0.00 | -0.12 | -1.18 | +0.02 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.19 | +0.00 | +0.46 | +0.09 | +0.64 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.08 | +0.00 | -0.62 | -0.37 | -0.09 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.06 | -0.50 | -0.36 | -0.20 | -0.00 | -1.1% |
| US dollar index (`F_DXY`) | +3% DXY | -1.05 | +0.00 | -0.78 | -0.21 | -0.07 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.6% | -5.6% | +0.0 | -1.7 | -3.1 | -0.8 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.6% | -3.6% | -3.3 | -0.1 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -2.6 | +0.1 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.1% | +2.0% | +3.8 | +0.1 | +0.1 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.9% | -1.9% | -1.5 | -0.2 | -0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -0.6 | -0.1 | -0.8 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.9% | -1.4% | +0.0 | -1.6 | -1.9 | -0.5 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.5% | -1.3% | +0.0 | -3.9 | -0.4 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.1% | +1.2% | +0.0 | +0.8 | +1.0 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.1 | -0.1 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -4.8% | -1.1% | -4.4 | -0.2 | -0.2 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -5.8% | -1.0% | +0.0 | -4.9 | -0.6 | -0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TRENT | +3.75% | +1.88% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TRENT | -2.24% | -0.63% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TRENT | -1.50% | -0.60% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TRENT | -2.80% | -0.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TRENT | -2.25% | -0.49% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → TRENT | -1.73% | -0.43% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → TRENT | -1.50% | -0.41% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TRENT | -1.44% | -0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → TRENT | -1.44% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → TRENT | -0.60% | -0.36% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → TRENT | +0.45% | +0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → TRENT | -1.50% | -0.33% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → TRENT | +0.45% | +0.31% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → TRENT | +0.75% | +0.26% |
| 2 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → F_URBAN_DEMAND → TRENT | -0.30% | -0.26% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → TRENT | -1.60 | events | -2.40% |
| 1 | F_REPO_IN → TRENT | +1.00 | events | -1.50% |
| 1 | F_URBAN_DEMAND → TRENT | +0.20 | events | +1.00% |
| 1 | F_RURAL_DEMAND → TRENT | -0.25 | events | -0.38% |
| 1 | F_USDINR → TRENT | -0.37 | observed | +0.18% |
| 1 | F_COTTON → TRENT | +0.19 | observed | -0.10% |

## Analyst profile (agent research, sourced)
# TRENT (Trent Ltd.) - company profile as of 2026-11-05

## Business
Trent, part of the Tata Group (promoters 37.01%), runs Zudio (value fashion, 1,000+ stores), Westside (premium fashion) and Star Bazaar, plus emerging categories (beauty, footwear and others) now 21% of revenue. TTM sales are Rs 22,001 cr (+18%) with EBITDA Rs 4,169 cr (19%). September 2026 quarter: sales Rs 5,873 cr (+22%), OPM 18%. The market cap is Rs 1.63 lakh cr at Rs 3,058, P/E 85, yet the shares are -34.5% over twelve months (Yahoo/screener, 2026-11-05).

## What moves the stock (ranked)
1. **Like-for-like growth and new store productivity.** Sales growth slowed to 15-19% in FY26, then re-accelerated to 22%. The market prices persistence of 20%+.
2. **Urban discretionary demand.** Beta 1.3; +5pp urban growth is worth about +5 equity points.
3. **Competition in value fashion** (Reliance, Max, online).
4. **Discount rate and flows.** FIIs fell from 25.9% to 15.3% since Dec 2023; the empirical US 10Y beta is -1.49 (t=-1.5).
5. **Input and FX costs.** Cotton and imports are small relative to the demand channel.

## Transmission examples
- **Middle East escalation -> Brent up -> fuel and food inflation -> real incomes squeezed -> discretionary apparel slows -> LFL growth down.** Order 2: inflation; order 3: RBI holds rates; order 4: urban EMI burden. For an 85x stock, a 3pp LFL miss can cost 8-10%.
- **Brent up -> USD/INR up -> imported garments/cosmetics dearer** (small, -0.5).
- **US 10Y up -> global growth de-rating -> FII selling -> Trent (holders 15.3%) falls**, as in the empirical beta.
- **Monsoon/good harvest -> rural wallet -> Zudio small-town stores**.
- **Wage growth -> aspirational spending -> Zudio price-point volumes.**

## Current situation
The Q2 business update on 2026-10-06 (revenue +23%) lifted the stock 10-13% to a two-year high; Q2 results on 2026-10-29 beat estimates with margin expansion and Zudio crossing 1,000 stores (+5-7%). Brokerages differ on outlook (BusinessLine 2026-10-30).

## Upcoming events
Q3 business update (January) and results (February 2027), store additions, festive-shift effects (Diwali 2026-11-08, model knowledge).

## Bull case
20%+ growth for three more years with margin at 19-20% justifies 70-80x forward earnings; emerging categories add margin.

## Bear case
LFL slips to low single digit, competition increases, multiple compresses from 85x to 55x: -35%.

## Uncertainties
Segment shares, cost splits and Inditex JV details are model estimates; press and screener PAT differ (Rs 468 cr vs Rs 490 cr).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.