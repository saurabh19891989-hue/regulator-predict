# WIPRO — Wipro Ltd.
*NIFTY_NEXT_50 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.2%**, **12 months -4.5%** (rank 156 / 155 of 200 for 3m / 12m); beta 0.93
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.2%): 3 months 43%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -8.9% … P90 -0.8%; plausible 12m relative-return range incl. stock-specific noise: -45.4% … +24.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -6.1% beta-adjusted vs realised market-adjusted move -8.4%); forward event exposure -6.4% (3m -2.7%; half assumed priced); company-specific events -0.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -5.95 | -6.00 | +0.07 | -0.01 | -0.01 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.35 | +2.50 | +0.73 | +0.23 | -0.11 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.19 | +1.70 | +0.50 | +0.00 | -0.01 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.75 | +0.00 | -0.90 | -0.68 | -0.18 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.60 | +1.60 | +0.00 | +0.01 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.51 | -1.00 | -0.45 | -0.08 | +0.03 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.41 | +1.80 | -0.16 | -0.13 | -0.09 | -1.1% |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.19 | -0.70 | -0.19 | -0.29 | -0.01 | +11.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.00 | +0.00 | +0.64 | +0.28 | +0.08 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.89 | +1.00 | -0.13 | +0.00 | +0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.63 | +0.00 | +0.12 | -0.72 | -0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.55 | +0.00 | -0.57 | +0.01 | -0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -5.9% | -5.9% | -6.0 | +0.1 | -0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.0% | +4.0% | +2.6 | +1.1 | +0.2 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -12.7% | -3.2% | -10.5 | -2.4 | +0.4 | -0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.5% | -2.5% | -2.6 | +0.2 | -0.0 | -0.0 |
| Anthropic IPO prices and lists (proposed ticker ANT), Nov 2026-Q1 2027 (`EV_ANTHROPIC_IPO_LISTING`) | anticipated | 0.85 | -2.7% | -2.3% | -3.0 | +0.2 | +0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -7.9% | -2.2% | -9.1 | +1.1 | +0.2 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -8.7% | -1.6% | -7.6 | -1.5 | +0.4 | -0.0 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.8% | +1.4% | +2.9 | -0.2 | +0.0 | +0.0 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.2% | -1.2% | -1.2 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | -0.5 | -0.5 | -0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → WIPRO | -3.00% | -2.55% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → WIPRO | -7.50% | -1.88% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → WIPRO | -5.10% | -1.43% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → WIPRO | -5.10% | -1.28% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → WIPRO | +2.50% | +1.25% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → WIPRO | -4.00% | -1.12% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → WIPRO | -3.00% | -0.90% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → WIPRO | -5.00% | -0.90% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → WIPRO | +2.88% | +0.81% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → WIPRO | +2.10% | +0.52% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → WIPRO | +2.34% | +0.51% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → WIPRO | +1.42% | +0.51% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → WIPRO | -0.85% | -0.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_US_EQUITIES → WIPRO | -2.55% | -0.46% |
| 1 | EV_INDIA_EU_FTA_SIGNED ⇒ F_EU_GDP → WIPRO | +0.48% | +0.44% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | T_GENAI_SERVICES → WIPRO | +1.00 | events | -6.00% |
| 1 | F_US_GDP → WIPRO | +1.20 | events | +3.00% |
| 1 | P_US_VISA_OUTSOURCING → WIPRO | +0.90 | events | -2.70% |
| 1 | F_GSEC_10Y_IN → WIPRO | +1.70 | events | -1.70% |
| 1 | F_FPI_FLOWS → WIPRO | -1.60 | events | -1.60% |
| 1 | F_FED_FUNDS → WIPRO | +1.62 | observed | -1.13% |
| 1 | F_USDINR → WIPRO | -0.37 | observed | -0.66% |
| 1 | F_US_10Y → WIPRO | +1.68 | observed | +0.50% |
| 1 | F_US_EQUITIES → WIPRO | +0.23 | observed | +0.40% |
| 1 | F_EU_GDP → WIPRO | +0.22 | events | +0.35% |
| 1 | F_COAL_INTL → WIPRO | +0.70 | director_override | -0.35% |
| 1 | F_RISK_SENTIMENT → WIPRO | +0.11 | observed | -0.11% |

## Analyst profile (agent research, sourced)
# Wipro Ltd. (WIPRO) - company profile, as of 2026-11-05

## Business
Wipro is India's fourth-largest listed IT services group, 72.6% held by the Premji family and trusts. IT services are ~99% of revenue: Americas about 58%, Europe about 30%, APMEA about 12% (model knowledge, not re-verified), spread across BFSI (~30%), consumer, health, and technology/communications. TTM sales are Rs97,023 cr at ~19% EBITDA margin and Rs13,200 cr of profit; the balance sheet holds net cash, which supports a 5.6% dividend yield and the M&A appetite reported by NDTV Profit on 2026-10-16. The stock trades at 14.9x earnings, close to six-year lows hit on 2026-09-29, but has rebounded 22% in a month.

## What moves the stock (ranked)
1. **GenAI repricing and deal momentum (T_GENAI_SERVICES)**. Large-deal bookings in Q2 FY27 were the weakest in 19 quarters (-76% YoY) and Q3 is guided at -1.5% to +0.5% constant currency. Each unit of repricing costs about -6% of equity value; range -13 to +2 because the same fear can reverse (the 'anti-AI trade' lifted Wipro ADRs 5% on 2026-10-15).
2. **US demand (C_USA, F_US_EQUITIES)**: +1pp US growth ~ +2.5%; S&P +5% ~ +1.7% (empirical +1.69, t +2.2, matches).
3. **Europe (C_EU_UK)**: highest European mix among peers, so +1.6 per +1pp.
4. **USD/INR**: +3% => ~+1.8% (net cash, 45% INR costs). The pack elasticity is negative (-2.52, t -1.7) and we flag the sign conflict: IT sells off when INR weakens in risk-off episodes.
5. **Flows and rates**: FPI inflow (+1.0), 10y G-sec up (-1.0), VIX up (-1.0). The 5.6% yield makes the stock a bond proxy.
6. **US visa/outsourcing policy**: -3 per tightening unit, low realised damage in 2026.

## Transmission examples
- **Middle East escalation -> F_BRENT up -> India CAD widens -> INR weaker (order 2)** helps Wipro's margin directly (+), but **-> VIX up -> FPI outflows -> IT de-rates (order 3)** dominates in the first month; **-> global growth slows -> US banks/consumer clients cut discretionary programmes -> Wipro deal conversion falls (order 4)** is the persistent harm.
- **US 10y up on strong data -> S&P up -> US client budgets firmer -> deals convert**; but **US 10y up on inflation -> mortgages/credit slow -> BFSI programmes deferred (Capco, BFS)**.
- **Anthropic/OpenAI-style agent releases -> T_GENAI_SERVICES -> price renegotiation of infra and BPS renewals -> Wipro revenue guide cut**; offset if clients redeploy savings into transformation deals.
- **Nifty 50 reshuffle -> index selling by DIIs (DII stake 7.86% -> 5.14%) -> temporary price pressure, followed by FII buying (8.32% -> 9.46%)**.

## Current situation
On 2026-10-15 Wipro reported revenue +1.1% QoQ, profit -4.5% QoQ, margin improved to 16.5% in IT services, and a muted Q3 guide. The stock still rose (+2% to +6.5%) as the revenue beat offset weak bookings; brokerages remain split (Nomura Buy, +15% upside; others bearish). Interest expense is up sharply (Rs545 cr in the quarter vs Rs361 cr a year earlier), consistent with acquisition or lease funding (reason not verified).

## Upcoming
Q3 FY27 results in mid-January 2027, preceded by TCS, HCL and Infosys; potential acquisition announcement; dividend/buyback; US policy risk.

## Bull case
The deal rebound the CEO expects arrives, valuation (14.9x, 5.6% yield) attracts FPIs, acquisitions add AI capability and INR weakness lifts margin.

## Bear case
Bookings stay weak, Q4 guide slips to negative growth, GenAI deflation hits infra/BPS, and acquisitions dilute margin further.

## Uncertainties and data caveats
The revenue-mix percentages and the cost split above come from model knowledge and the 2025 annual report structure, not from a document fetched on 2026-11-05; confidence is medium. The FPI/DII shareholding shift is consistent with a Nifty 50 index change, but the exact effective date and size were not verified. Screener 'OPM' (20%) differs from the company's IT-services segment margin (16.5%) because screener includes other operating items. The pack's coal and aluminium elasticities carry no causal channel for an IT firm, so they were reduced to a token weight rather than adopted.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.