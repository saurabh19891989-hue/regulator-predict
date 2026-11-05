# GROWW — Billionbrains Garage Ventures Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.8%**, **12 months -6.0%** (rank 150 / 177 of 200 for 3m / 12m); beta 1.21
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.4%): 3 months 46%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.0% … P90 +1.3%; plausible 12m relative-return range incl. stock-specific noise: -25.4% … +38.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.7 pp (model impact -3.5% beta-adjusted vs realised market-adjusted move +14.6%); forward event exposure -3.3% (3m +1.7%; half assumed priced); company-specific events -3.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| SEBI F&O / market-structure tightening (`P_SEBI_DERIVATIVES`) | +1 = tightening step | -10.56 | -8.00 | -2.79 | +0.17 | +0.05 | — |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +7.65 | +9.00 | -1.26 | -0.09 | +0.00 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -7.14 | -5.00 | -1.73 | -0.55 | +0.14 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +6.59 | +4.00 | +2.28 | +0.53 | -0.22 | — |
| Retail broking fee/pricing pressure (`NEW_BROKER_PRICING`) | +1 = broad fee cut or free-trade move by a large rival or exchange | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +3.79 | +3.00 | +1.08 | -0.28 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.71 | +2.50 | +1.54 | -0.38 | +0.05 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.67 | -2.00 | -0.69 | -0.79 | -0.19 | +3.5% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.94 | +0.00 | -0.80 | -1.09 | -1.05 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.73 | +0.00 | -0.64 | -0.75 | -1.35 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.73 | +1.00 | +0.88 | +0.69 | +0.16 | +1.2% |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.65 | +0.00 | +1.40 | +1.04 | +0.21 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.56 | +0.00 | -1.10 | -1.43 | -0.03 | +2.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.51 | -2.50 | +0.00 | +0.00 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.2% | -8.2% | -5.5 | -3.4 | +0.8 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.2% | +5.1% | +7.0 | +3.9 | -1.0 | +0.1 |
| SEBI partly reverses derivative expiry-settlement rule after closing-auction (CAS) volatility (`EV_SEBI_CAS_DERIV_REVERSAL`) | anticipated | 0.85 | +4.9% | +4.2% | +5.0 | -0.1 | -0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.5% | -3.5% | -3.5 | +0.0 | +0.0 | -0.0 |
| SEBI tightens F&O further (weekly-expiry scrapping, higher margins/lot sizes) (`EV_SEBI_FNO_CURBS_RISK`) | risk_scenario | 0.20 | -16.6% | -3.3% | -17.0 | +0.3 | +0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -12.8% | -3.2% | -8.0 | -2.4 | -3.0 | +0.6 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -1.6 | -1.4 | -0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.9% | +2.9% | +0.0 | +1.4 | +0.7 | +0.8 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.9 | -1.0 | +0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -0.6 | -1.6 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.7% | +2.0% | +0.8 | +0.7 | +1.2 | +1.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +2.0% | +2.0% | +1.2 | +0.9 | -0.2 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GROWW | +6.25% | +3.12% |
| 1 | EV_SEBI_CAS_DERIV_REVERSAL ⇒ P_SEBI_DERIVATIVES → GROWW | +3.20% | +2.72% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → GROWW | +3.60% | +1.80% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → GROWW | -9.00% | -1.80% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ P_SEBI_DERIVATIVES → GROWW | -8.00% | -1.60% |
| 1 | EV_SEBI_CAS_DERIV_REVERSAL ⇒ F_EQUITY_ACTIVITY_IN → GROWW | +1.80% | +1.53% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → GROWW | -5.00% | -1.25% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → GROWW | -2.00% | -1.00% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ P_CAPITAL_GAINS_TAX → GROWW | +2.50% | +0.88% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → GROWW | -3.00% | -0.75% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → GROWW | -3.00% | -0.75% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → GROWW | -5.00% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → GROWW | -1.25% | -0.75% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → GROWW | -3.75% | -0.67% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_EQUITY_ACTIVITY_IN → GROWW | +1.80% | +0.63% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → GROWW | -1.60 | events | -4.00% |
| 1 | F_GSEC_10Y_IN → GROWW | +1.55 | director_override | -3.88% |
| 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → GROWW | -1.60 | events | -2.30% |
| 1 | P_SEBI_DERIVATIVES → GROWW | -0.10 | events | +0.80% |
| 1 | F_REPO_IN → GROWW | +1.00 | events | +0.50% |
| 2 | P_SEBI_DERIVATIVES → F_EQUITY_ACTIVITY_IN → GROWW | -0.10 | events | +0.28% |
| 1 | F_US_EQUITIES → GROWW | +0.23 | observed | +0.23% |
| 1 | F_RISK_SENTIMENT → GROWW | +0.11 | observed | -0.22% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → GROWW | +0.30 | events | +0.19% |
| 3 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → GROWW | -1.60 | events | +0.14% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → GROWW | +0.50 | events | -0.12% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → GROWW | +0.30 | events | +0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | SEBI CAS / F&O settlement review outcome | regulatory | 0.60 | +0.5% | +0.30% |
| 2026-12 | Additional pre-IPO investor block sales (Sequoia/Peak XV, others) | corporate_action | 0.60 | -3.5% | -2.10% |
| 2027-01-20 | Q3 FY27 results (inferred; Q2 reported 2026-10-14) | results | 0.90 | +0.0% | +0.00% |
| 2027-05 | Promoter / anchor lock-in expiries (18 months from Nov 2025 listing, model knowledge) | corporate_action | 0.50 | -2.5% | -1.25% |

## Analyst profile (agent research, sourced)
# GROWW - Billionbrains Garage Ventures Ltd. (midcap, digital broker) - as of 2026-11-05

## Business
Groww is an app-first investing platform: equity cash and F&O, MTF, mutual funds, bonds, IPOs, US stocks, wealth. TTM revenue Rs5,724cr, EBITDA margin 63%, PAT Rs2,693cr. Mcap Rs1.40 lakh cr, P/E 52x, promoters 27.1%, FIIs 10.9%, DIIs 12.7%. Listed November 2025, so no 3-year factor regression exists; all weights are fundamental and confidence is low.

## What moves the stock, ranked
1. **SEBI derivatives rules** - F&O is the highest-yield product. One tightening step ~ -8 (volume -10% => EBITDA -9%, persistence 0.75, plus de-rating). Management said F&O pressure is temporary; MOFSL sees 25% upside as the overhang eases (2026-10-13).
2. **Market activity and demat additions** - +20% traded value ~ +9.
3. **Investor supply** - Rs1,999cr block on 2026-09-16 (-4.5%), further sell-downs likely; short-term -1 to -6% per block.
4. **Discount rate/valuation** - 52x P/E; 10y G-sec +25bp ~ -2.5.
5. **Domestic flows and financialisation** - SIP/DII flows +3, structural theme +4.
6. **Pricing competition** (proposed NEW_BROKER_PRICING) ~ -5 per broad fee cut.
7. **Tax policy (STT)** ~ -5.

## Transmission examples
- **Middle East escalation -> VIX up -> Nifty falls 5% -> retail F&O losses and new-account additions drop -> volumes -15% -> Groww revenue -10% -> EBITDA -14% (operating leverage) -> stock -7%; 4th-order: SEBI further tightens retail F&O to protect investors -> another -8.**
- **SEBI relaxes CAS/settlement -> expiry-day volumes preserved -> Groww and BSE both rally (shared shock) -> Groww gains more through client volumes.**
- **Rate hike (RBI 5.50%) -> bond yields up -> bond products attractive (Groww bonds) but equity valuations compress -> client flows to fixed income.**

## Current situation
Q2 PAT Rs725cr (+54% y/y) but flat q/q; the stock is near its 52-week high Rs227 at Rs223 after +18% in 3 months, as institutions replaced early VC holders.

## Upcoming
Further block deals; SEBI review outcome; Union Budget (1 Feb 2027); Q3 results mid/late January; lock-in expiry (2027).

## Bull / bear
Bull: market-share gains, MTF/bonds revenue, regulatory easing, FII buying. Bear: F&O curbs, stagnation q/q, VC supply, pricing wars, premium valuation.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.