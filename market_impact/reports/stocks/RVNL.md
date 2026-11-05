# RVNL — Rail Vikas Nigam Ltd.
*MIDCAP_100 · Construction · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.2%**, **12 months +4.1%** (rank 58 / 40 of 200 for 3m / 12m); beta 1.54
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +32.9%): 3 months 53%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.2% … P90 +9.3%; plausible 12m relative-return range incl. stock-specific noise: -39.3% … +47.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +2.3 pp (model impact +4.7% beta-adjusted vs realised market-adjusted move -26.8%); forward event exposure +5.0% (3m -0.2%; half assumed priced); company-specific events +0.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +6.11 | +6.00 | +0.14 | -0.01 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.59 | +0.00 | -2.53 | -0.13 | +0.08 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.53 | +3.00 | -0.10 | -0.24 | -0.13 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.19 | -2.20 | +0.00 | +0.01 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.10 | -2.00 | +0.00 | -0.04 | -0.06 | +3.5% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.67 | +0.00 | -1.41 | -0.13 | -0.13 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.53 | -1.50 | +0.00 | -0.03 | +0.00 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.41 | +0.00 | +0.00 | -1.40 | -0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.30 | +0.00 | -0.71 | -0.56 | -0.03 | -1.1% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.21 | +0.00 | -0.64 | +0.00 | -0.57 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +1.19 | +0.00 | +1.20 | +0.00 | -0.01 | — |
| Road/highway awarding (`P_INFRA_SPENDING_ROADS`) | +10% | +1.11 | +1.00 | +0.14 | -0.01 | -0.02 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.10 | +0.00 | -0.23 | -0.49 | -0.38 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +6.8% | +6.1% | +7.2 | -0.1 | -0.2 | -0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.2% | -4.2% | +0.0 | -1.0 | -2.2 | -1.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -2.9 | -0.2 | +0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -8.4% | -2.3% | -8.0 | +0.0 | -0.2 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.9% | +1.9% | +3.0 | -0.8 | -0.2 | -0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -10.6% | -1.9% | -10.0 | +0.0 | -0.3 | -0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.2% | -1.5% | -2.4 | +0.0 | -1.2 | -0.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.3% | -1.3% | -0.8 | +0.0 | -0.3 | -0.2 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -2.2 | +0.6 | +0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.1% | +1.2% | +1.0 | +0.0 | +0.7 | +0.4 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → RVNL | +4.80% | +4.32% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → RVNL | +3.00% | +3.00% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → RVNL | -2.91% | -2.91% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → RVNL | -8.00% | -2.24% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → RVNL | -2.20% | -2.20% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → RVNL | +2.40% | +2.16% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → RVNL | -2.16% | -2.16% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → RVNL | -2.10% | -2.10% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → RVNL | -1.95% | -1.95% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → RVNL | -10.00% | -1.80% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → RVNL | -0.96% | -0.96% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → RVNL | -2.20% | -0.88% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → RVNL | -2.40% | -0.86% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → RVNL | +1.80% | +0.81% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_RISK_SENTIMENT → RVNL | -0.80% | -0.80% |

## Analyst profile (agent research, sourced)
# RVNL — Rail Vikas Nigam Ltd. (as of 2026-11-05)

*Facts from screener.in (pack through Jun 2026) and Google News headlines; bodies not retrieved; order-book size not retrieved. Model knowledge labelled. No expected-return number.*

## Business
RVNL is a railway PSU that wins and sub-lets railway infrastructure projects: doubling, new lines, electrification, metro, workshops and bridges, with a small non-rail book (SJVN siding Rs 903 cr). Q1 FY27 sales Rs 4,321 cr, operating profit Rs 185 cr (4.3%), PAT Rs 160 cr. FY26 PAT fell 32% to Rs 871 cr. The share price (Rs 194) is down 40% in a year and 37% in six months.

## What moves the stock (ranked)
1. **Railway capex (P_RAILWAY_CAPEX +6.0 per +10%):** order inflow drives the story.
2. **Government capex (+3.0) and road/metro (+1.0).**
3. **Discount rate and risk appetite (F_REPO_IN -2.2, F_RISK_SENTIMENT -2.0).**
4. **Steel (-1.5 per +7%)** because margins are thin.
5. **Domestic flows (+1.5)** from retail/DII.

## Transmission examples
- **Budget railway capex -> order awards -> revenue.** P_RAILWAY_CAPEX +10% (1st) -> RVNL inflow +8% (2nd) -> revenue +8% two years later with thin margin giving ~+8% PAT (3rd) -> re-rating of 45x P/E (4th).
- **Middle East escalation -> Brent -> inflation -> RBI.** Brent $95 -> CPI up -> RBI hike (7 Oct) -> yields up -> PSU high-beta multiple falls -> RVNL -2.2 per 25bp, bigger than any cost effect.
- **Steel price spike -> EPC cost -> OPM near zero.** Steel +7% -> 0.8% of sales unrecovered -> EBITDA -20% at 4% OPM.
- **Risk-off -> FPI/retail outflow -> railway PSU theme sold.**

## Current situation
No Q2 yet; the pack shows Q1 PAT +19% on sales +11%. Orders continue (Rs 405 cr East Coast Railway, 21 Sep; Rs 903 cr SJVN, 7 Sep) but the stock keeps making lows (22 Oct), then +2.7% on 28 Oct.

## Upcoming
Q2 results (~mid-Nov, estimate); Union Budget 1 Feb 2027; order wins; RBI Dec policy.

## Bull case
Budget lifts rail capex, large awards, margin recovers to 5%+, rate cuts resume.

## Bear case
Order slippage, execution delays, margin falls below 4%, rate hikes continue.

## Uncertainties
Order book, receivables and segment mix not retrieved; revenue shares are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.