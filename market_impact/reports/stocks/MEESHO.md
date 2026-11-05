# MEESHO — Meesho Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +0.8%** (rank 34 / 39 of 200 for 3m / 12m); beta 0.91
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +51.0%): 3 months 51%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.2% … P90 +6.2%; plausible 12m relative-return range incl. stock-specific noise: -63.2% … +64.5%
- Decomposition (12m): 0.5 × forward event exposure -0.1% (3m -0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -4.7% (beta-adjusted) vs a realised market-adjusted move of +26.7% — gap -31.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -0.51 | -0.05 | -0.56 | -0.46 |
| Sector | +0.57 | +0.53 | +1.10 | +0.44 |
| Theme | +0.00 | +0.03 | +0.03 | +0.02 |
| Geopolitics | +0.00 | -0.09 | -0.09 | -0.07 |
| Company catalysts | +1.03 | +0.00 | +1.03 | +1.03 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.52 | -0.24 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.84** | **+0.62** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.16 | +4.00 | +0.00 | +0.16 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.75 | +3.00 | +0.53 | +0.17 | +0.05 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.54 | +3.50 | +0.00 | +0.02 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.02 | -2.00 | -0.65 | -0.35 | -0.02 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.69 | +0.00 | -1.84 | -0.43 | -0.42 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.87 | -1.80 | -0.06 | +0.02 | -0.03 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.84 | +0.00 | +1.64 | +0.10 | +0.10 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.81 | +0.00 | +1.00 | +0.33 | +0.47 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.77 | +0.00 | -0.80 | -0.71 | -0.26 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.64 | +1.50 | +0.00 | +0.10 | +0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.48 | -1.00 | -0.21 | -0.26 | -0.01 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.47 | +0.00 | -1.41 | -0.17 | +0.11 | -1.1% |
| Labour code implementation cost (`P_LABOUR_CODES`) | +1 = implementation | -1.36 | -1.50 | +0.00 | +0.15 | -0.01 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.34 | +0.00 | +1.44 | -0.12 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.8% | -7.8% | -7.7 | +0.0 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.7% | +4.8% | +9.6 | +0.0 | +0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -10.0% | -2.5% | -5.0 | -5.0 | -0.1 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.3 | -0.4 | -0.6 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.9% | -1.9% | -1.8 | -0.1 | +0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.2% | +1.7% | +2.1 | +0.5 | +0.5 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.7% | +1.7% | +1.8 | +0.0 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.8 | +0.1 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -10.6% | -1.6% | -5.0 | -5.8 | +0.2 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -6.3% | -1.6% | -4.2 | -1.1 | -0.9 | -0.1 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -0.7 | -0.6 | -0.0 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.0% | -1.3% | -7.1 | -0.1 | -0.1 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MEESHO | +8.75% | +4.38% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MEESHO | -5.00% | -1.25% |
| 1 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → MEESHO | -1.50% | -1.20% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MEESHO | -5.25% | -0.95% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MEESHO | -3.36% | -0.84% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → MEESHO | -3.36% | -0.84% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → MEESHO | +1.20% | +0.84% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MEESHO | -1.80% | -0.76% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → MEESHO | -5.00% | -0.75% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → MEESHO | +1.30% | +0.72% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → MEESHO | +1.20% | +0.66% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → MEESHO | +0.91% | +0.62% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → MEESHO | +1.75% | +0.61% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → MEESHO | +0.70% | +0.56% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MEESHO | -2.20% | -0.55% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → MEESHO | -1.60 | events | -5.60% |
| 1 | F_REPO_IN → MEESHO | +1.00 | events | -1.80% |
| 1 | F_RURAL_DEMAND → MEESHO | -0.25 | events | -1.00% |
| 1 | F_URBAN_DEMAND → MEESHO | +0.20 | events | +0.30% |
| 1 | F_RISK_SENTIMENT → MEESHO | +0.11 | observed | -0.22% |
| 1 | F_COTTON → MEESHO | +0.19 | observed | -0.08% |
| 1 | F_BRENT → MEESHO | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | MSCI index review / inclusion decision *(review: [RT_BOT_A] Inclusion is now the base case (Livemint 29 Oct; Business Standard/JM 23 Oct), and the stock already rose 6% on inclusion hopes on 6 Oct. Higher probability, smaller residual impact.)* | corporate_action | 0.80 | +1.5% | +1.20% |
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