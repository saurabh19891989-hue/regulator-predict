# RVNL — Rail Vikas Nigam Ltd.
*MIDCAP_100 · Construction · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months -0.0%** (rank 57 / 108 of 200 for 3m / 12m); beta 1.54
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +32.9%): 3 months 52%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.5% … P90 +3.5%; plausible 12m relative-return range incl. stock-specific noise: -33.6% … +52.1%
- Decomposition (12m): 0.5 × forward event exposure -0.0% (3m +0.8%; half assumed priced) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.7% (beta-adjusted) vs a realised market-adjusted move of -26.8% — gap +29.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +6.11 | +6.00 | +0.14 | -0.01 | -0.02 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.56 | +3.00 | -0.10 | -0.24 | -0.10 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.19 | -2.20 | +0.00 | +0.01 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.08 | -2.00 | +0.00 | -0.04 | -0.04 | +3.5% |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.51 | -1.50 | +0.00 | -0.01 | +0.00 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.41 | +0.00 | -1.41 | +0.06 | -0.06 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.34 | +0.00 | -1.27 | -0.13 | +0.06 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +1.19 | +0.00 | +1.20 | +0.00 | -0.01 | — |
| Road/highway awarding (`P_INFRA_SPENDING_ROADS`) | +10% | +1.11 | +1.00 | +0.14 | -0.01 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.06 | +0.00 | -0.71 | -0.35 | +0.01 | -1.1% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.97 | +0.00 | -0.80 | -0.27 | +0.10 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.90 | +0.00 | -0.23 | -0.36 | -0.30 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.88 | +0.00 | -0.96 | +0.03 | +0.05 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.1% | +2.1% | +3.0 | -0.8 | -0.1 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | -0.0 | +0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.7% | +1.5% | +1.8 | -0.0 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.5 | -0.2 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.2% | -1.3% | -5.0 | +0.0 | -0.1 | -0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.2% | -0.9% | -2.2 | +0.0 | +0.0 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -5.3% | -0.8% | -5.0 | +0.0 | -0.2 | -0.2 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | +0.0 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.8% | -0.7% | -2.0 | +0.0 | -0.4 | -0.4 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +0.8 | +0.0 | +0.2 | +0.2 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → RVNL | -5.00% | -1.25% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → RVNL | +1.20% | +1.08% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → RVNL | -2.20% | -0.92% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → RVNL | -5.00% | -0.75% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → RVNL | -2.20% | -0.59% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → RVNL | +0.60% | +0.54% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → RVNL | -0.88% | -0.53% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → RVNL | -2.00% | -0.50% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → RVNL | +0.80% | +0.50% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → RVNL | +0.80% | +0.44% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → RVNL | +0.80% | +0.40% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → RVNL | -2.20% | -0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → RVNL | -1.44% | -0.36% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → RVNL | -0.60% | -0.33% |
| 1 | EV_UP_UPSET_OPPOSITION_WIN ⇒ F_RISK_SENTIMENT → RVNL | -1.60% | -0.32% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REPO_IN → RVNL | +1.00 | events | -2.20% |
| 1 | F_STEEL_INDIA → RVNL | +1.35 | events | -2.03% |
| 1 | F_GOVT_CAPEX → RVNL | +0.20 | director_override | +0.60% |
| 1 | F_RISK_SENTIMENT → RVNL | +0.11 | observed | -0.22% |
| 1 | F_COPPER → RVNL | -0.24 | observed | +0.09% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → RVNL | +0.30 | events | +0.05% |
| 3 | F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → F_DOMESTIC_FLOWS → RVNL | +0.20 | events | -0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-12 | Q2 FY27 results (screener lists through Jun 2026; Q2 FY26 was mid-Nov; date estimated) | results | 0.90 | +0.0% | +0.00% |
| 2026-12 | New order wins (recent: Rs903 cr SJVN Buxar siding 7 Sep; Rs405 cr East Coast Railway 21 Sep) | other | 0.90 | +1.4% | +1.26% |
| 2027-06 | Government OFS / stake sale (govt holds ~73%, model knowledge) | corporate_action | 0.10 | -3.5% | -0.35% |

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