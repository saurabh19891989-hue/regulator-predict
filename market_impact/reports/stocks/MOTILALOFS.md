# MOTILALOFS — Motilal Oswal Financial Services Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.7%**, **12 months -2.3%** (rank 143 / 169 of 200 for 3m / 12m); beta 1.53
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.9%): 3 months 48%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -17.3% … P90 +8.5%; plausible 12m relative-return range incl. stock-specific noise: -44.3% … +29.7%
- Decomposition (12m): 0.5 × forward event exposure -3.2% (3m -0.3%; half assumed priced) + 0.5 × company-specific catalysts -0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.8% (beta-adjusted) vs a realised market-adjusted move of +21.0% — gap -21.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +7.22 | +5.00 | +1.84 | +0.49 | -0.11 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +7.12 | +6.00 | +1.26 | -0.15 | +0.00 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -7.10 | -4.50 | -2.09 | -0.55 | +0.04 | — |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +6.33 | +7.00 | -0.51 | -0.15 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -6.22 | -3.50 | -1.54 | -1.01 | -0.16 | +3.5% |
| SEBI F&O / market-structure tightening (`P_SEBI_DERIVATIVES`) | +1 = tightening step | -3.92 | -2.00 | -2.17 | +0.16 | +0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.92 | +0.00 | -1.12 | -1.89 | -0.91 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -3.81 | +0.00 | -1.40 | -1.85 | -0.56 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +3.68 | +0.00 | +2.84 | +0.57 | +0.27 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +3.20 | +2.50 | +0.84 | -0.11 | -0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.83 | -1.50 | -0.93 | -0.34 | -0.06 | -1.1% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.83 | +1.50 | +0.96 | +0.41 | -0.05 | +1.2% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.66 | +2.00 | +0.52 | +0.26 | -0.11 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.44 | +0.00 | -1.92 | -0.50 | -0.02 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -15.7% | -15.7% | -13.2 | -2.8 | +0.3 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +19.4% | +9.7% | +16.4 | +3.3 | -0.4 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -21.5% | -5.4% | -13.3 | -5.9 | -2.7 | +0.4 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +3.6% | +3.6% | +3.0 | +0.7 | -0.1 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -21.5% | -3.2% | -11.0 | -8.8 | -2.1 | +0.4 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +3.0% | +3.0% | +0.0 | +2.3 | +0.2 | +0.5 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -1.8 | -0.8 | -0.3 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +5.0% | +2.8% | +1.4 | +2.3 | +1.1 | +0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -10.5% | -2.6% | -3.5 | -4.3 | -2.1 | -0.5 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -14.1% | -2.5% | -11.9 | -2.3 | +0.1 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -2.3 | -0.2 | +0.1 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -9.6% | -2.4% | -4.5 | -5.5 | +0.7 | -0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MOTILALOFS | +15.00% | +7.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MOTILALOFS | -8.75% | -2.19% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MOTILALOFS | -9.00% | -1.62% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → MOTILALOFS | +2.80% | +1.40% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → MOTILALOFS | -7.00% | -1.40% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → MOTILALOFS | -8.75% | -1.31% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → MOTILALOFS | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → MOTILALOFS | -4.50% | -1.12% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → MOTILALOFS | +3.00% | +1.05% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → MOTILALOFS | +1.20% | +0.96% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → MOTILALOFS | -3.50% | -0.88% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → MOTILALOFS | +1.40% | +0.87% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ P_CAPITAL_GAINS_TAX → MOTILALOFS | +2.25% | +0.79% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → MOTILALOFS | +1.40% | +0.77% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MOTILALOFS | -2.88% | -0.72% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → MOTILALOFS | -1.60 | events | -9.60% |
| 1 | F_EQUITY_ACTIVITY_IN → MOTILALOFS | +0.20 | events | +1.40% |
| 1 | F_REPO_IN → MOTILALOFS | +1.00 | events | -1.00% |
| 1 | F_GDP_IN → MOTILALOFS | +0.50 | events | +1.00% |
| 1 | P_SEBI_DERIVATIVES → MOTILALOFS | -0.50 | events | +1.00% |
| 1 | F_CREDIT_SPREADS_IN → MOTILALOFS | +0.50 | events | -0.75% |
| 1 | F_USDINR → MOTILALOFS | -0.37 | observed | +0.55% |
| 1 | F_RISK_SENTIMENT → MOTILALOFS | +0.11 | observed | -0.39% |
| 1 | F_US_EQUITIES → MOTILALOFS | +0.23 | observed | +0.35% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → MOTILALOFS | +0.30 | events | +0.24% |
| 2 | F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → MOTILALOFS | +0.20 | events | -0.05% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → MOTILALOFS | +0.30 | events | +0.04% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Leadership rejig across verticals takes effect (Vishal Tulsyan WTD) | corporate_action | 0.95 | +0.0% | +0.00% |
| 2026-11 | NCD issuance up to Rs3,000cr approved by board in Q2 | capex | 0.60 | +0.0% | +0.00% |
| 2026-12 | SEBI derivatives or broker-regulation measures | regulatory | 0.25 | -2.0% | -0.50% |
| 2027-01 | Q3 FY27 results (date approximate; Q2 on ~2026-10-28/29) | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# MOTILALOFS - Motilal Oswal Financial Services (as of 2026-11-05)

## Business
Motilal Oswal combines an asset manager (now the largest profit pool), capital-markets businesses (broking, institutional equities, IB), wealth/PMS and a housing-finance/lending balance sheet. Screener's Sep-26 quarter shows sales Rs1,748cr and OPM 57%; TTM PAT Rs1,427cr; mcap Rs65,803cr, P/E 46, P/B ~7. Reported Q2 profit is noisy: operating PAT Rs718cr (+29%) vs a headline Rs1,081cr including treasury gains (Moneycontrol, TaxGuru/Investywise via search). The March-26 quarter showed a Rs-49cr loss, a reminder of market sensitivity.

## What moves the stock (ranked)
1. **Equity activity/volumes (+7.0 per +20%)** and **FPI flows (+6.0)**; market beta 1.6-1.8 (pack).
2. **Tax policy (P_CAPITAL_GAINS_TAX -4.5 for a tightening step):** FM said she is open to views (reported 2026-10-13; shares +7% on 2026-11-03).
3. **Risk sentiment (-3.5)** and **domestic SIP flows (+2.5).**
4. **Structural financialisation (+5.0)** and GDP (+2.0).
5. **Funding: repo (-1.0), credit spreads (-1.5);** F&O regulation (-2.0, small).
Pack: US equities +3.10 (t 1.1) and USD/INR -7.96 (t -1.5) are noisy; shrunk.

## Transmission examples
- **Global risk-off (VIX +5) -> FPI outflow -> Nifty down 2% -> cash turnover down -> broking and IB fees down, treasury MTM loss -> PAT -15% (March-26-type swing) -> stock -3.5 per shock with beta 1.7.**
- **FM cuts LTCG/STT in Budget -> retail turnover up 8-10% -> broking/distribution revenue up -> SIP flows to MO AMC up -> AMC fee growth -> EBITDA +10% -> +5 to +12%.**
- **Middle East escalation -> Brent up -> CPI up -> RBI 'calibrated tightening' (2026-10-07) -> bond yields up -> NCD funding costs up for MO's balance-sheet book -> NIM squeeze, and equity multiples compress -> P/E 46 de-rates.**
- **IPO boom (Jio Platforms listing, Oct 2026) -> IB/ECM pipeline -> fee income, and wealth distribution of IPOs.**

## Current situation
Momentum high (+25% in 3m). Leadership rejig on 2026-11-03 (Vishal Tulsyan WTD, Ajay Menon exits). Board cleared up to Rs3,000cr NCDs (Multibagg).

## Upcoming events
Budget 2027-02-01 (equity tax, prob 0.35 of a cut), Q3 results (~Jan 2027), SEBI measures (prob 0.25).

## Bull and bear
**Bull:** AMC compounding, tax relief option, market uptrend, 20-22% PAT growth target (scanx).
**Bear:** earnings volatility, P/E 46, market drawdown, funding costs.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.