# POLICYBZR — PB Fintech Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.7%**, **12 months -5.3%** (rank 185 / 172 of 200 for 3m / 12m); beta 1.12
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +51.0%): 3 months 44%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -13.3% … P90 -3.0%; plausible 12m relative-return range incl. stock-specific noise: -87.6% … +27.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -7.1% beta-adjusted vs realised market-adjusted move -47.0%); forward event exposure -4.1% (3m -1.7%; half assumed priced); company-specific events -4.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -14.24 | -14.00 | -0.24 | +0.00 | +0.00 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +3.98 | +4.00 | +0.00 | +0.00 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.92 | +4.00 | -0.07 | -0.01 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.53 | -2.50 | -0.70 | -0.37 | +0.03 | +3.5% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.11 | +0.00 | +2.48 | +0.55 | +0.09 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.60 | +0.00 | -1.00 | -0.96 | -0.64 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -2.46 | -2.00 | +0.00 | -0.34 | -0.12 | +11.2% |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.46 | +0.00 | +1.96 | +0.26 | +0.24 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.46 | +2.00 | +0.50 | -0.04 | +0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.84 | +0.00 | +1.28 | +0.60 | -0.03 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.82 | +0.00 | +1.28 | +0.61 | -0.07 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.76 | +0.00 | -0.20 | -0.89 | -0.67 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.72 | +0.00 | -1.57 | -0.17 | +0.02 | +2.2% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.61 | +0.00 | -1.04 | -0.45 | -0.12 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.6% | -8.6% | -8.8 | +0.2 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.8% | +5.4% | +11.0 | -0.2 | -0.0 | -0.0 |
| IRDAI resets insurance commission/expense rules; post-GST-exemption demand (`EV_IRDAI_COMMISSION_RESET`) | anticipated | 0.50 | -10.0% | -5.0% | -9.8 | -0.2 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -3.4% | -3.4% | -2.0 | -1.3 | -0.1 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -10.7% | -2.7% | -6.2 | -5.1 | +0.4 | +0.2 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.2% | +2.2% | -1.0 | +0.9 | +1.8 | +0.5 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -3.0% | -2.2% | -2.0 | -0.7 | -0.2 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.9% | +1.9% | +2.0 | -0.0 | -0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -0.7 | -0.9 | -0.3 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -11.9% | -1.8% | -6.2 | -6.5 | +0.7 | +0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.7% | -1.7% | -1.6 | -0.0 | -0.0 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.5% | -1.5% | -0.9 | -0.6 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POLICYBZR | +10.00% | +5.00% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → POLICYBZR | -9.80% | -4.90% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → POLICYBZR | -6.25% | -1.56% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → POLICYBZR | +6.00% | +1.50% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → POLICYBZR | -2.00% | -1.44% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → POLICYBZR | -6.00% | -1.08% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → POLICYBZR | -3.84% | -0.96% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → POLICYBZR | -3.84% | -0.96% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → POLICYBZR | -6.25% | -0.94% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → POLICYBZR | -3.60% | -0.90% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → POLICYBZR | -2.00% | -0.80% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → POLICYBZR | +2.00% | +0.70% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → POLICYBZR | +0.80% | +0.64% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → POLICYBZR | -2.50% | -0.62% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → POLICYBZR | +1.00% | +0.62% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → POLICYBZR | -1.60 | events | -6.40% |
| 1 | F_FED_FUNDS → POLICYBZR | +1.62 | observed | -3.24% |
| 1 | F_STEEL_GLOBAL → POLICYBZR | +2.06 | observed | -1.64% |
| 1 | F_REFINING_MARGIN → POLICYBZR | +1.54 | observed | +1.23% |
| 1 | T_GENAI_SERVICES → POLICYBZR | +1.00 | events | -1.00% |
| 1 | F_GDP_IN → POLICYBZR | +0.50 | events | +1.00% |
| 1 | F_CPI_IN → POLICYBZR | +1.15 | events | -0.92% |
| 1 | F_USDINR → POLICYBZR | -0.37 | observed | -0.30% |
| 1 | F_RISK_SENTIMENT → POLICYBZR | +0.11 | observed | -0.28% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → POLICYBZR | +0.30 | events | +0.19% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | IRDAI final commission/EoM/dark-pattern rules (reported plan from January) | regulatory | 0.50 | -5.0% | -2.50% |
| 2027-01 | Insurer commission renegotiations under draft EoM (contract resets) | other | 0.50 | -3.5% | -1.75% |
| 2027-02 | Q3 FY27 results: take-rate and ad-spend trajectory | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# POLICYBZR - PB Fintech (Policybazaar) (as of 2026-11-05)

## Business
PB Fintech runs Policybazaar (insurance marketplace), Paisabazaar (loans) and newer lines. Roughly 85% of revenue is commission and marketing fees from insurers on premium sold, so it is directly exposed to how much insurers may pay distributors. Search summaries put Q2 FY27 revenue near Rs2,178cr (+35%), PAT near Rs192cr (+43%) and premium Rs9,385cr (+38%); sources differ and I could not verify them against the exchange filing. The screener extract is parent-only (Sep-26 sales Rs5cr) and is not meaningful.

## What moves the stock (ranked)
1. **IRDAI draft rules (-14, range -30 to +2).** The 2026-09-23/24 proposals (commission caps, EoM limits, dark-pattern ban) triggered a 36% one-day crash, 43% over four sessions and an estimated Rs31,000cr value loss (Fortune India, Moneycontrol). Brokerages see ~46% earnings risk; Nomura cut its target to Rs1,100, Bernstein kept Rs2,310.
2. **Global/Indian risk appetite: FPI flows (+4.0), VIX (-2.5), Fed funds (-2.0)** - beta 1.1-1.4, 58% volatility.
3. **Structural growth: financialisation (+4.0), GDP (+2.0).**
4. **AI disintermediation (-1.0), CPI (-0.8).**
Pack empirics: refining margin +2.34 (t 2.8), Brent +1.94 (t 2.1), steel -2.82 (t -2.0) have no business mechanism and are shrunk to near zero.

## Transmission examples
- **IRDAI finalises caps -> insurers' distributor payouts fall -> PB take rate down and insurers renegotiate -> revenue -15 to -25% while ad and staff costs are fixed -> EBITDA -45% -> multiple compresses; 4th order: lower profit funds fewer ad spends, slowing premium growth.**
- **Rates up (repo hiked 2026-10-07) -> FD rates up -> savings-plan demand shifts -> insurers' life APE slows -> PB's life revenue slips; separately higher discount rates hit a P/E-100 growth stock (Fed funds -2.0).**
- **Brent up -> CPI -> RBI tightening -> health/motor premium growth slows (affordability) -> PB premium growth falls below 35%.**
- **Equity sell-off -> FPI outflow -> high-beta internet names fall with beta 1.4.**

## Current situation
Stock Rs971 (-39% in 3m, 52-week low on 2026-11-02, below IPO price as of 2026-10-01). Brokers disagree strongly. IRDAI's chair said the norms are not intended to disrupt business models (Livemint, 2026-10-15); ET reported caps may roll out from January (2026-10-09).

## Upcoming events
IRDAI final rules (prob 0.5 by Dec; -25% to +15%), Q3 results (Feb 2027), contract resets with insurers.

## Bull and bear
**Bull:** 35%+ growth, profitable, dilution of draft likely, price below IPO.
**Bear:** take-rate reset, ad-spend inflation, regulatory path-dependency, disintermediation.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.