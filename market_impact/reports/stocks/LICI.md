# LICI — Life Insurance Corporation of India
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.2%**, **12 months -1.1%** (rank 91 / 147 of 200 for 3m / 12m); beta 1.12
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.7%): 3 months 51%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.5% … P90 +2.9%; plausible 12m relative-return range incl. stock-specific noise: -30.2% … +26.5%
- Decomposition (12m): 0.5 × forward event exposure -1.5% (3m +0.4%; half assumed priced) + 0.5 × company-specific catalysts +0.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.4% (beta-adjusted) vs a realised market-adjusted move of -4.3% — gap +6.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.93 | -3.50 | -0.31 | -0.13 | +0.01 | +3.5% |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +3.45 | +2.50 | +1.00 | -0.02 | -0.03 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +2.47 | +2.50 | +0.00 | -0.02 | -0.01 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.29 | +0.00 | -1.40 | -0.77 | -0.11 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.06 | +0.00 | -1.38 | -0.50 | -0.19 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -2.05 | -1.50 | -0.55 | -0.01 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.90 | +0.00 | +1.76 | +0.10 | +0.04 | — |
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -1.76 | -1.50 | -0.15 | -0.11 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.56 | +1.50 | +0.14 | -0.06 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.47 | +1.50 | +0.02 | -0.04 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.23 | +1.00 | +0.00 | +0.18 | +0.05 | — |
| US growth (`F_US_GDP`) | +1 pp | +1.23 | +0.00 | +0.96 | +0.26 | +0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.05 | +0.00 | +1.01 | +0.08 | -0.04 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.01 | +0.00 | +0.96 | +0.07 | -0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.2% | -3.2% | -3.3 | -0.0 | +0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -11.0% | -2.8% | -8.8 | -2.2 | -0.2 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.1% | +2.5% | +5.2 | +0.1 | -0.1 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -11.3% | -1.7% | -8.8 | -2.6 | -0.0 | +0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.6% | +1.6% | +0.0 | +1.1 | +0.3 | +0.2 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.5% | -1.5% | -1.2 | -0.3 | -0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.4 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.5% | +1.4% | +1.4 | +0.8 | +0.2 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -5.4% | -1.4% | -3.5 | -1.4 | -0.4 | -0.1 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -4.6% | -1.1% | +0.0 | -4.2 | +0.4 | -0.8 |
| Nvidia FQ3 results (reported 17 Nov): beat-and-raise, AI demand intact (`EV_NVDA_NOV17_BEAT`) | scheduled | 0.62 | +1.7% | +1.1% | +1.4 | +0.3 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.6 | -0.3 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LICI | -8.75% | -2.19% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LICI | +3.75% | +1.88% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → LICI | -8.75% | -1.31% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → LICI | -3.50% | -0.88% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → LICI | +1.40% | +0.87% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → LICI | +1.40% | +0.77% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → LICI | +1.40% | +0.70% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → LICI | -2.52% | -0.63% |
| 1 | EV_UP_UPSET_OPPOSITION_WIN ⇒ F_RISK_SENTIMENT → LICI | -2.80% | -0.56% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_RISK_SENTIMENT → LICI | -10.50% | -0.53% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → LICI | -1.05% | -0.52% |
| 1 | EV_US_CHINA_TRUCE_EXTENDED ⇒ F_RISK_SENTIMENT → LICI | +0.70% | +0.50% |
| 1 | EV_BOJ_DEC26_HIKE_150 ⇒ F_RISK_SENTIMENT → LICI | -0.70% | -0.49% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RISK_SENTIMENT → LICI | +0.70% | +0.48% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → LICI | +1.52% | +0.46% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → LICI | -1.60 | events | -2.40% |
| 1 | F_GOLD → LICI | -1.05 | observed | +0.84% |
| 1 | F_GSEC_10Y_IN → LICI | +1.55 | director_override | -0.78% |
| 1 | F_GDP_IN → LICI | +0.50 | events | +0.75% |
| 1 | F_RISK_SENTIMENT → LICI | +0.11 | observed | -0.39% |
| 1 | F_REPO_IN → LICI | +1.00 | events | -0.30% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → LICI | +0.30 | events | +0.12% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → LICI | -1.56 | events | -0.07% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → LICI | +0.30 | events | +0.04% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → LICI | +1.15 | events | -0.04% |
| 2 | F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → LICI | +0.20 | events | -0.04% |
| 2 | F_RURAL_DEMAND → F_UNSECURED_STRESS → LICI | -0.25 | events | -0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (week of 2 Nov per Upstox; exact date unverified) | results | 0.97 | +0.5% | +0.48% |
| 2027-03 | Further government OFS (CEO said no fresh sale soon) | corporate_action | 0.12 | -4.0% | -0.48% |
| 2027-03 | Health-insurance or fintech acquisition announcement | corporate_action | 0.20 | +0.5% | +0.10% |

## Analyst profile (agent research, sourced)
# LICI - Life Insurance Corporation of India (midcap, life insurance)

## Business
LIC is the dominant Indian life insurer: about 66% of new business premium, roughly Rs 55 lakh cr of assets and 14 lakh agents. Par (participating) policies still dominate the mix; management wants a higher non-par share and VNB margins in the mid-20s. Reported net profit (Rs 57.4k cr FY26, Rs 13.5k cr Q1 FY27) swings with realised equity gains because LIC holds one-third of assets in equity. The government owned 96.5% until the August 2026 OFS of Rs 31,552 cr; promoter share is now 90.0% and public float 10%.

## What moves the stock (ranked)
1. **Equity-market level and flows** - the portfolio makes both P&L and embedded value market-sensitive. A VIX spike of +5 points is worth about -3.5% for the stock.
2. **Government stake-sale supply** - the OFS raised DII ownership from 1% to 6.2%. Management said no fresh sale soon, but the 12-month probability of another tranche is about 12%; each costs 2-6%.
3. **VNB growth and margins** - Q1 VNB +61%; GST relief on individual premia and ITC on group cover (8 Oct) are tailwinds; commission/distribution reform and margin caps are risks.
4. **Rates** - mostly neutral: 75% of assets are debt with reinvestment benefit offsetting EV discount-rate effects.
5. **Tax policy** - LTCG revisit talk (ET, 3 Nov) matters for realised-gain profits.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker and FPI selling -> Nifty falls -> LIC's equity book marks down -> reported profit and solvency buffer drop -> shares fall (and LIC may act as a market stabiliser, buying dips, reducing further fall).**
- **RBI hike (7 Oct) -> bank FD rates up -> household substitution into FDs and gold; but higher yields lift annuity and non-par pricing -> VNB margin up with a lag (3rd order).**
- **PSU divestment push (Hindustan Copper, Cochin Shipyard OFS in Aug) -> LIC as anchor buyer absorbs supply -> its equity-gain book changes (4th-order: LIC's own stake sale reduces domestic institutional appetite for other PSU OFS).**
- **Higher gold price -> more jewellery/gold ETF buying -> less savings into endowment policies -> lower NBP.**

## Current situation
Stock fell 7.3% in October before Q2; 12m -9.8% but 3m +5.4%. Q1 showed VNB +61% and profit +23%. Q2 results are due this week (date unconfirmed). Valuation P/E 8.6 with ROE 38% looks cheap versus private peers but reflects government control and low growth (sales CAGR 7.5% over 5 years).

## Upcoming
Q2 FY27 results; Union Budget (Feb 2027); IRDAI distribution reforms; potential further OFS; NSE stake increase.

## Bull / bear
Bull: VNB margin expansion, non-par shift, large float increase and index flows, strong equity market. Bear: equity correction, government supply, regulatory caps, political demands to share surplus with policyholders.

Uncertainty: AUM mix and equity share are model knowledge; screener series for Sep 2026 quarter was not yet available; low confidence overall.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.