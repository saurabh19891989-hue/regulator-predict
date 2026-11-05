# MEESHO — Meesho Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.0%**, **12 months -2.2%** (rank 161 / 166 of 200 for 3m / 12m); beta 0.91
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +51.0%): 3 months 48%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.4% … P90 +4.1%; plausible 12m relative-return range incl. stock-specific noise: -60.2% … +56.5%
- Decomposition (12m): 0.5 × forward event exposure -6.4% (3m -4.3%; half assumed priced) + 0.5 × company-specific catalysts +2.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -6.0% (beta-adjusted) vs a realised market-adjusted move of +26.7% — gap -32.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -5.05 | -4.00 | -0.65 | -0.36 | -0.04 | +3.5% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.69 | +3.00 | +0.53 | +0.26 | -0.10 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.67 | +4.00 | +0.00 | -0.28 | -0.04 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.58 | +3.50 | +0.00 | +0.04 | +0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.34 | +0.00 | -2.48 | -0.43 | -0.42 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.07 | -3.00 | -0.06 | +0.02 | -0.03 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.76 | +0.00 | -1.60 | -0.98 | -0.18 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.65 | +0.00 | +2.44 | +0.10 | +0.11 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.94 | +0.00 | -1.60 | -0.43 | +0.09 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.89 | +0.00 | -1.97 | +0.05 | +0.03 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.50 | -1.00 | -0.21 | -0.25 | -0.03 | +0.0% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.47 | +0.00 | +1.00 | -0.03 | +0.50 | — |
| Labour code implementation cost (`P_LABOUR_CODES`) | +1 = implementation | -1.37 | -1.50 | +0.00 | +0.15 | -0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.36 | +0.00 | -0.32 | -1.08 | +0.05 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.9% | -7.9% | -7.7 | +0.0 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.6% | +5.3% | +10.4 | +0.0 | +0.1 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -14.9% | -3.7% | -10.0 | -5.0 | -0.1 | +0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.1% | -3.1% | -3.0 | -0.1 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -2.6 | +0.1 | +0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -15.7% | -2.4% | -10.0 | -5.8 | +0.2 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +4.0% | +2.2% | +2.9 | +0.5 | +0.5 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -8.4% | -2.1% | -6.2 | -1.1 | -0.9 | -0.2 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -2.0% | -2.0% | -1.4 | -0.6 | -0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.3 | +0.0 | -0.6 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.7% | +1.7% | +1.8 | +0.0 | -0.1 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.3 | -0.2 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MEESHO | +8.75% | +4.38% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MEESHO | -10.00% | -2.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → MEESHO | -10.00% | -1.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MEESHO | -3.00% | -1.26% |
| 1 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → MEESHO | -1.50% | -1.20% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → MEESHO | -4.00% | -1.00% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → MEESHO | +1.60% | +0.99% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MEESHO | -5.25% | -0.95% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → MEESHO | +1.60% | +0.88% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MEESHO | -3.36% | -0.84% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → MEESHO | -3.36% | -0.84% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → MEESHO | +1.20% | +0.84% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MEESHO | -3.00% | -0.81% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → MEESHO | +1.60% | +0.80% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → MEESHO | -1.20% | -0.72% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → MEESHO | -1.60 | events | -5.60% |
| 1 | F_REPO_IN → MEESHO | +1.00 | events | -3.00% |
| 1 | F_RURAL_DEMAND → MEESHO | -0.25 | events | -1.00% |
| 1 | F_RISK_SENTIMENT → MEESHO | +0.11 | observed | -0.45% |
| 1 | F_URBAN_DEMAND → MEESHO | +0.20 | events | +0.30% |
| 1 | F_COTTON → MEESHO | +0.19 | observed | -0.08% |
| 1 | F_BRENT → MEESHO | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | MSCI index review / inclusion decision | corporate_action | 0.40 | +5.0% | +2.00% |
| 2026-11 | Kirana Club acquisition tranche update (Reg 30 filing 3 Nov) | corporate_action | 0.70 | +0.0% | +0.00% |
| 2027-01-28 | Q3 FY27 results (festive quarter) - first full festive period post-IPO | results | 0.85 | +1.0% | +0.85% |

## Analyst profile (agent research, sourced)
# MEESHO — Meesho Ltd., as of 2026-11-05

*Screener unavailable; facts from Google News headlines (Jun-Nov 2026; bodies not retrieved) and model knowledge where labelled.*

## Business
Zero-commission e-commerce marketplace for value-seeking tier-2+ India with in-house logistics (Valmo), advertising monetisation and a content-commerce push. Q2 FY27: loss narrowed ~68%, marketplace revenue +34% to Rs 4,120 cr, content-commerce NMV +152% (Upstox, Storyboard18, Exchange4Media). It bought Kirana Club for Rs 202 cr (June 2026). Price Rs 235.7, +26.6% in 3m, 1y vol 54%.

## What moves the stock (ranked)
1. Execution on growth and contribution margin (ad take rate, logistics cost).
2. Discount rate/risk appetite (F_REPO_IN -3, F_RISK_SENTIMENT -4).
3. Flows: FPI, MSCI inclusion and block deals (+3.5).
4. Rural/value demand and GST (+4, +3).
5. Logistics fuel and labour codes (-1, -1.5).

## Transmission examples
- **Brent up** -> fuel cost for delivery partners -> logistics cost up -> contribution margin down; CPI up squeezes rural purchasing power -> orders slow.
- **GST cut on apparel** -> lower consumer prices -> more first-time online shoppers -> volume and ad revenue up.
- **MSCI inclusion** -> passive inflows -> price up 2-8%; **block deals** -> supply.
- **Rate cut** -> long-duration platform multiple expands.

## Current situation
Analysts split: Nomura Reduce TP Rs 167 (27% downside), Jefferies/Motilal up to +25% (29 Oct). Festive Day-1 orders +75% y/y. Management said 6% margin gains will partly fund lower prices (4 Nov).

## Bull / bear
Bull: ads and content commerce lift take rate, profit inflection. Bear: price war with Flipkart/Amazon, valuation, supply overhang.

## Uncertainties
No audited numbers retrieved; market cap and cost shares are estimates; all confidence low.

## Additional notes
Upcoming events: Q3 FY27 results (~late Jan 2027, first full festive quarter after listing), possible MSCI inclusion in the November review, and further Kirana Club acquisition tranches (Regulation 30 filing, 3 Nov). Competition from Flipkart/Shopsy and Amazon is the main structural risk; pricing investment could offset the margin gains highlighted on 4 Nov.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.