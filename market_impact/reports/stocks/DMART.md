# DMART — Avenue Supermarts Ltd.
*NIFTY_NEXT_50 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.5%**, **12 months -2.3%** (rank 143 / 139 of 200 for 3m / 12m); beta 0.80
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.8%): 3 months 45%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.5% … P90 -0.0%; plausible 12m relative-return range incl. stock-specific noise: -28.3% … +13.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -1.9% beta-adjusted vs realised market-adjusted move -19.8%); forward event exposure -3.7% (3m -2.8%; half assumed priced); company-specific events +1.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.97 | +4.00 | +0.00 | +0.05 | -0.08 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.92 | +3.00 | +0.56 | +0.18 | +0.18 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.24 | +0.00 | -1.88 | -1.20 | -0.16 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | -2.92 | -3.00 | +0.08 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.83 | +0.00 | -0.96 | -0.85 | -1.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.72 | +2.50 | +0.14 | +0.01 | +0.07 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.23 | -2.20 | +0.00 | +0.00 | -0.03 | — |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +2.06 | +2.00 | +0.00 | +0.07 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.77 | +0.00 | -1.01 | -0.63 | -0.14 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -1.75 | +0.00 | -1.24 | -0.34 | -0.17 | +2.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.72 | -0.60 | -0.47 | -0.43 | -0.22 | -1.1% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.59 | -0.80 | -0.24 | -0.31 | -0.24 | +0.0% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.42 | +0.00 | +0.80 | +0.52 | +0.10 | +1.2% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.33 | +0.00 | -1.07 | -0.22 | -0.04 | +9.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.0% | -6.0% | -5.5 | -0.3 | -0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.9% | +3.4% | +6.2 | +0.4 | +0.0 | +0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.2% | -3.2% | -3.1 | +0.0 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.9 | -2.2 | -1.4 | -0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.4 | -0.4 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.7 | -0.1 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.9% | +1.6% | +1.0 | +0.7 | +0.7 | +0.5 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.5% | +1.5% | +1.2 | +0.2 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -5.6% | -1.4% | -1.8 | -1.5 | -1.3 | -0.9 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.5% | -1.4% | +0.0 | -4.9 | -0.7 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.5% | -1.4% | -7.1 | -0.2 | -0.2 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.3% | +1.3% | +0.0 | +0.7 | +0.3 | +0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DMART | +6.25% | +3.12% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → DMART | -1.76% | -0.88% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → DMART | -3.75% | -0.67% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → DMART | -1.10% | -0.66% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → DMART | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → DMART | -2.40% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → DMART | -2.33% | -0.58% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → DMART | +1.04% | +0.57% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → DMART | -0.53% | -0.50% |
| 1 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → DMART | -0.60% | -0.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → DMART | -1.76% | -0.44% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → DMART | +1.25% | +0.44% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → DMART | +0.50% | +0.40% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → DMART | -0.44% | -0.40% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → DMART | -0.66% | -0.40% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → DMART | -1.60 | events | -4.00% |
| 1 | F_GSEC_10Y_IN → DMART | +1.55 | director_override | -3.41% |
| 1 | F_FOOD_INFLATION_IN → DMART | +2.00 | events | +1.60% |
| 1 | F_URBAN_DEMAND → DMART | +0.20 | events | +0.80% |
| 1 | T_FORMALISATION → DMART | +0.30 | events | +0.60% |
| 1 | F_STEEL_INDIA → DMART | +1.35 | events | -0.41% |
| 1 | F_REPO_IN → DMART | +1.00 | events | -0.40% |
| 1 | F_USDINR → DMART | -0.37 | observed | +0.22% |
| 1 | F_BRENT → DMART | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | New store additions pace: management guidance of ~ 20% area growth; new-city launches, update on DMart Ready profitability | capex | 0.60 | +0.5% | +0.30% |
| 2027-01-04 | Q3 FY27 standalone business update (revenue, store count) - DMart publishes a quarterly update in the first week after quarter end (as in Oct 2026: 4-5 Oct) | results | 0.85 | +0.5% | +0.42% |
| 2027-01-16 | Q3 FY27 results (Dec-quarter, festive/winter season); key watch: gross margin, EBITDA margin vs 8% a year ago, debt | results | 0.90 | +0.5% | +0.45% |

## Analyst profile (agent research, sourced)
# DMART — Avenue Supermarts Ltd. (as of 2026-11-05)

*Facts are from screener.in (via the evidence pack) and Google News headlines dated Oct 2026 (article bodies were not retrieved, so numbers quoted only in headlines are flagged). Items marked "model knowledge" are from memory. No expected-return number is given; the Director derives that from the graph.*

## Business
DMart is India's largest listed value-retail chain: EDLP pricing, mostly owned stores, ~55% foods/FMCG and ~40% general merchandise and apparel (model knowledge on mix), plus DMart Ready e-commerce. TTM sales are Rs 74,223 cr (+16%), EBITDA margin ~7.5%, PAT Rs 3,116 cr. Promoters hold 74.5%. The equity is a long-duration growth asset: P/E 71.5, P/B 8.5, ROE 12.9%.

## What moves the stock (ranked)
1. **Discount rate / multiple (F_GSEC_10Y_IN, F_FPI_FLOWS)**. At 71x earnings, +25 bp on the G-sec moves equity about -2%. FIIs (8.5%) have been trimming.
2. **Urban demand and LFL growth (F_URBAN_DEMAND, P_GST_CONSUMPTION)**. Revenue growth is ~60% area growth and ~40% LFL/ticket; sales per sq ft rose only 0.6% in Q2 (BusinessLine, 16 Oct). Each +1pp LFL is worth ~1.7% EBITDA through fixed-cost leverage.
3. **Quick-commerce substitution (T_QUICK_COMMERCE)**: Blinkit targets 3,500-5,000 stores; top-up baskets in metros are the contested pool.
4. **Margins and funding intensity**: OPM slipped to 7.1% in Q2 from 8.0% in Q1 and interest cost nearly doubled y/y (Rs 64 cr vs 35 cr).
5. **Costs**: diesel/freight, wages, labour codes (small each, 0.3-0.8% of equity per standard shock).
6. **Structural formalisation (T_FORMALISATION)** supports the long runway but is already priced.

## Transmission examples
- **Middle East escalation** (C_MIDEAST_CONFLICT) -> Brent up (F_BRENT) -> diesel and freight cost up (1st order, -0.8 per +10%) -> food inflation and CPI rise (2nd) -> RBI holds or hikes (3rd) -> G-sec yield up -> 71x multiple compresses (-2.2 per 25 bp), while household wallets tighten and urban demand softens (4th). Sign: negative at every step; the rate/multiple leg is larger than the cost leg.
- **GST cut or consumption stimulus** (P_GST_CONSUMPTION) -> lower shelf prices on staples/apparel -> volumes and trade-down footfalls rise at DMart (1st) -> LFL +1-2pp -> operating leverage lifts EBITDA ~3% (2nd) -> analysts upgrade growth, FIIs rotate back into the quality-growth cohort (3rd) -> multiple holds despite a rate backdrop (4th).
- **Weaker rupee** (F_USDINR up) -> import-linked staples (edible oil, pulses) cost more -> EDLP margin squeezed, nominal ticket rises -> FPI selling of INR assets -> DMart's 9% FII stake sold (3rd) -> relative underperformance. Sign: mildly negative.
- **Quick-commerce expansion** (T_QUICK_COMMERCE) -> metro top-up share loss -> weaker same-store sales -> operating deleverage on owned-store fixed costs -> debt-funded expansion continues so ROCE falls -> further de-rating.

## Current situation
Q2 FY27 (Oct 10): revenue +17.8%, PAT +8.5% to ~Rs 743 cr, below estimates; margin miss. Shares fell 3-4% on Oct 12, hitting a 52-week and then 3-year low (Oct 16), -28% from the April high. Jefferies and Morgan Stanley trimmed targets, Citi kept Sell, Motilal Oswal and ICICI Securities were more constructive (headlines). Debt is rising to fund 20% area growth.

## Upcoming
Q3 business update (~4 Jan 2027), Q3 results (~mid-Jan 2027), Union Budget (1 Feb 2027), store-opening cadence. No known corporate actions; no dividend.

## Bull case
Festive/GST-driven volume recovery, sales per sq ft rebounds to +5-6%, gross margin gains from private labels, multiple stabilises near 55-60x as yields ease.

## Bear case
LFL stays at low single digits, quick commerce erodes metro baskets, margins sink below 7% while debt rises, multiple de-rates toward 45-50x.

## Uncertainties
No article bodies were read; LFL and gross-margin numbers are not verified. Revenue mix and Brent/wage cost shares are estimates. Empirical iron-ore sensitivity (-3.2, t -2.0) is treated as non-causal.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.