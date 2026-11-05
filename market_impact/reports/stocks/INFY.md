# INFY — Infosys Ltd.
*NIFTY_50 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.5%**, **12 months -4.7%** (rank 170 / 165 of 200 for 3m / 12m); beta 0.87
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.9%): 3 months 43%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.7% … P90 -2.5%; plausible 12m relative-return range incl. stock-specific noise: -31.3% … +28.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -4.5% beta-adjusted vs realised market-adjusted move -7.4%); forward event exposure -6.6% (3m -2.5%; half assumed priced); company-specific events -0.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -4.94 | -5.00 | +0.06 | +0.00 | +0.00 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -4.00 | -4.00 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.06 | +2.50 | +0.57 | +0.10 | -0.11 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.75 | +1.50 | +0.34 | -0.07 | -0.02 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.36 | +0.00 | -0.90 | -0.41 | -0.05 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.28 | +1.50 | +0.00 | -0.13 | -0.09 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.21 | -1.00 | -0.24 | +0.01 | +0.02 | +3.5% |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.12 | -0.70 | -0.22 | -0.21 | +0.01 | +11.2% |
| Europe growth (`F_EU_GDP`) | +1 pp | +0.99 | +1.00 | +0.00 | +0.00 | -0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +0.75 | +0.00 | +0.26 | +0.47 | +0.02 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.60 | +0.00 | +0.40 | +0.19 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.54 | +0.00 | +0.08 | -0.58 | -0.04 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | -0.54 | +0.00 | -0.19 | -0.31 | -0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -4.9% | -4.9% | -5.0 | +0.1 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +3.7% | +3.7% | +2.6 | +0.9 | +0.1 | -0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -11.1% | -2.8% | -9.9 | -1.5 | +0.5 | -0.1 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.0 | +0.0 | +0.0 |
| Anthropic IPO prices and lists (proposed ticker ANT), Nov 2026-Q1 2027 (`EV_ANTHROPIC_IPO_LISTING`) | anticipated | 0.85 | -2.3% | -1.9% | -2.5 | +0.2 | +0.1 | -0.0 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.6% | -1.6% | -1.6 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.2% | -1.3% | -7.0 | +1.6 | +0.2 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | +0.0 |
| Appeals court allows $100k H-1B fee (or new rule finalised) and/or OPT fee rule finalised (`EV_H1B_FEE_REINSTATED`) | anticipated | 0.30 | -4.0% | -1.2% | -4.0 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | -0.7 | -0.5 | -0.0 | +0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -1.0% | -0.8% | -0.7 | -0.3 | -0.1 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -4.6% | -0.7% | -4.8 | +0.1 | +0.2 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → INFY | -2.50% | -2.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → INFY | -7.50% | -1.88% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → INFY | -4.00% | -1.20% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → INFY | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → INFY | -4.50% | -1.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → INFY | -2.50% | -0.62% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → INFY | +2.40% | +0.60% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → INFY | +2.10% | +0.52% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → INFY | -0.70% | -0.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → INFY | -2.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → INFY | +0.60% | +0.37% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → INFY | -0.72% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → INFY | +1.95% | +0.35% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → INFY | -0.69% | -0.35% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_US_EQUITIES → INFY | -2.25% | -0.34% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | T_GENAI_SERVICES → INFY | +1.00 | events | -5.00% |
| 1 | P_US_VISA_OUTSOURCING → INFY | +0.90 | events | -3.60% |
| 1 | F_US_GDP → INFY | +1.20 | events | +3.00% |
| 1 | F_GSEC_10Y_IN → INFY | +1.55 | director_override | -1.40% |
| 1 | F_FED_FUNDS → INFY | +1.62 | observed | -1.13% |
| 1 | F_USDINR → INFY | -0.37 | observed | -0.55% |
| 1 | F_REFINING_MARGIN → INFY | +1.54 | observed | +0.46% |
| 1 | F_US_EQUITIES → INFY | +0.23 | observed | +0.35% |
| 1 | F_EU_GDP → INFY | +0.22 | events | +0.22% |
| 1 | F_RISK_SENTIMENT → INFY | +0.11 | observed | -0.11% |
| 1 | F_BRENT → INFY | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-03 | Dividend record date (interim) - passed; Livemint 2026-11-02 | corporate_action | 1.00 | -0.6% | -0.60% |
| 2026-12 | US H-1B/outsourcing-tax action | regulatory | 0.15 | -3.5% | -0.53% |
| 2027-01 | Q3 FY27 results; test of cut guidance 1-2% and large-deal conversion | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Possible fresh buyback/special return (cash-rich, low P/E) | corporate_action | 0.20 | +2.2% | +0.45% |

## Analyst profile (agent research, sourced)
# Infosys Ltd. (INFY) - company profile, as of 2026-11-05

## Business
Infosys is the second-largest Indian IT services company, with digital, cloud, data/AI, application and BPM services plus the Finacle banking platform. North America is about 57% of revenue and Europe about 28% (model knowledge). TTM sales are roughly Rs1.9 lakh cr at a 24% EBITDA margin; it is debt-free with 32% ROE and a 4.2% dividend yield. On 2026-10-23 it posted Q2 FY27 revenue of Rs49,244 cr (+10.7% YoY, constant-currency +1.5% QoQ), profit Rs7,838 cr, and cut FY27 constant-currency revenue growth guidance to 1-2%, even though it won $5.2bn of large deals and AI is now ~10.5% of revenue.

## What moves the stock (ranked)
1. **GenAI substitution/repricing**: central -5% per unit (range -12 to +2). The company is simultaneously the beneficiary (AI revenue) and the victim (legacy run-and-maintain).
2. **US demand and sentiment**: +1pp US growth ~ +2.5%; S&P +5% ~ +1.5%. The guidance cut shows US discretionary spend is still soft.
3. **US visa and outsourcing policy**: -4 per tightening unit; the PERM suspension of 2026-10-08 was shrugged off.
4. **USD/INR**: +3% ~ +1.5% (30bp margin per 1% INR per company disclosures, model knowledge); the pack's negative empirical sign (-1.48, t -1.0) is not significant.
5. **Risk sentiment, G-sec yields, Fed funds**: small.
6. **Significant but non-causal pack links** (refining margin t +2.4, Brent t +1.8): treated as risk-on proxies with token weights.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker (India imports crude)**: margin tailwind for Infosys (2nd order, +) but **-> VIX up -> FPI outflow from IT (3rd)** and **-> US/EU consumer slowdown -> retail and manufacturing clients freeze programmes (4th)** dominate.
- **US inflation surprise -> Fed hikes -> US banks cut tech budgets -> Infosys financial-services vertical (28%) slows -> guidance cut again**.
- **AI agent release -> T_GENAI_SERVICES -> clients demand productivity pass-through in renewals -> revenue deflation of 1-3% -> EBIT margin held only by pyramid and automation**.
- **US HIRE-type tax -> onsite costs up -> margin -> peers equally hit; relative effect higher for visa-heavy firms**.

## Current situation
Shares fell to six-year lows on 2026-09-29, rebounded ~15% in a month (PERM relief, TCS and HCL results), then dipped after the guidance cut on 2026-10-26. A record date for the interim dividend was 2026-11-03. Brokerages note valuation (14.9x) is cheap but sentiment negative.

## Upcoming
Q3 FY27 results in mid-January 2027; large-deal conversion; policy risk in the US; possible buyback.

## Bull case
Large deals convert, AI revenue scales beyond 15% of sales, INR stays weak, and the stock rerates from 15x towards 18-20x.

## Bear case
Guidance is cut again, AI pricing compresses legacy revenue faster than AI wins, and the sector remains a funding source for FPIs.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.