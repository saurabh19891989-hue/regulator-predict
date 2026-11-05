# LTM — LTM Ltd.
*NIFTY_NEXT_50 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.8%**, **12 months -1.2%** (rank 172 / 160 of 200 for 3m / 12m); beta 1.16
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.3%): 3 months 48%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.1% … P90 +3.1%; plausible 12m relative-return range incl. stock-specific noise: -33.7% … +31.8%
- Decomposition (12m): 0.5 × forward event exposure -1.9% (3m -1.3%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.4% (beta-adjusted) vs a realised market-adjusted move of -1.9% — gap +3.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -3.93 | -4.00 | +0.09 | -0.01 | -0.01 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.76 | +3.00 | +0.74 | +0.11 | -0.10 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -3.49 | -3.50 | +0.00 | +0.00 | +0.01 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.02 | +1.80 | +0.26 | -0.05 | +0.00 | +1.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.92 | +2.20 | -0.14 | -0.07 | -0.06 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.86 | -1.40 | -0.43 | -0.06 | +0.03 | +3.5% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.58 | +0.00 | -1.16 | -0.37 | -0.05 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.12 | -0.70 | -0.20 | -0.25 | +0.03 | +11.2% |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.01 | +1.00 | +0.00 | +0.01 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.95 | +0.00 | +0.78 | +0.14 | +0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.73 | +0.90 | -0.17 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.58 | +0.00 | -0.56 | -0.01 | -0.01 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.41 | +0.00 | -0.34 | -0.04 | -0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.5% | +4.5% | +3.2 | +1.1 | +0.1 | +0.0 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -3.9% | -3.9% | -4.0 | +0.1 | -0.0 | -0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -13.7% | -3.4% | -12.3 | -1.6 | +0.4 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.4% | -2.1% | -8.9 | +0.2 | +0.3 | +0.0 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -1.7% | -1.7% | -1.8 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.6% | -1.6% | -2.0 | +0.4 | +0.0 | +0.0 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.5% | +1.3% | +2.8 | -0.3 | +0.0 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -7.1% | -1.1% | -6.2 | -1.1 | +0.3 | -0.0 |
| Appeals court allows $100k H-1B fee (or new rule finalised) and/or OPT fee rule finalised (`EV_H1B_FEE_REINSTATED`) | anticipated | 0.30 | -3.5% | -1.0% | -3.5 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → LTM | -9.00% | -2.25% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → LTM | -5.40% | -1.35% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → LTM | -5.40% | -1.35% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTM | +2.25% | +1.13% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → LTM | -3.50% | -1.05% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LTM | -3.50% | -0.88% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → LTM | -0.80% | -0.68% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → LTM | -3.50% | -0.53% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → LTM | +2.10% | +0.52% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → LTM | +2.86% | +0.51% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → LTM | -0.70% | -0.50% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → LTM | +1.92% | +0.48% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → LTM | +0.72% | +0.45% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_US_EQUITIES → LTM | -2.70% | -0.41% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → LTM | -0.72% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_US_GDP → LTM | +1.20 | events | +3.60% |
| 1 | T_GENAI_SERVICES → LTM | +0.50 | director_override | -2.00% |
| 1 | F_FPI_FLOWS → LTM | -1.60 | events | -1.44% |
| 1 | F_GSEC_10Y_IN → LTM | +1.55 | director_override | -1.40% |
| 1 | P_US_VISA_OUTSOURCING → LTM | +0.35 | director_override | -1.23% |
| 1 | F_FED_FUNDS → LTM | +1.62 | observed | -1.13% |
| 1 | F_USDINR → LTM | -0.37 | observed | -0.81% |
| 1 | F_US_10Y → LTM | +1.68 | observed | +0.67% |
| 1 | F_US_EQUITIES → LTM | +0.23 | observed | +0.42% |
| 1 | F_EU_GDP → LTM | +0.22 | events | +0.22% |
| 1 | F_RISK_SENTIMENT → LTM | +0.11 | observed | -0.16% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Q3 FY27 results (mid-Jan, after TCS/Infosys); guidance on AI revenue, margin, large deals | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Possible inorganic AI/engineering acquisition (management has signalled M&A optionality) | corporate_action | 0.10 | +0.5% | +0.05% |

## Analyst profile (agent research, sourced)
# LTM Ltd. (LTM) - company profile, as of 2026-11-05

## Business
LTM (formerly LTIMindtree, the 2022 merger of L&T Infotech and Mindtree; 69% owned by Larsen & Toubro) sells application, cloud, data/AI, ERP and digital-engineering services. About 70% of revenue is from North America (model knowledge), BFSI is roughly a third, and the rest is manufacturing, hi-tech/CPG and health. TTM sales are Rs43,359 cr with ~18% EBITDA margin; it is debt-free with ROE ~24%. The Sep-2026 quarter (Q2 FY27, reported 2026-10-16) showed revenue of Rs11,276 cr on screener (+13% YoY), a flat margin, PAT of ~Rs1,350-1,400 cr (sources differ), a Rs25 per share dividend and AI-linked revenue +47% YoY. The stock is down 22.8% over 12 months and ~28% year to date but still trades at 24.6x earnings, a premium to Infosys/Wipro at ~15x.

## What moves the stock (ranked)
1. **US demand and US equities (C_USA, F_US_EQUITIES)**: the cleanest statistical link (S&P elasticity +2.15 per 5%, t +2.8). A +1pp US growth shock is worth about +3% of equity value, because it lifts revenue ~1%, EBITDA ~1.7% and the multiple.
2. **GenAI substitution (T_GENAI_SERVICES)**: the biggest left-tail. Deflation of 3% of the revenue base at 60% flow-through cuts EBITDA ~10%; with AI revenue growing 47% the net central estimate is -4% per unit, range -10 to +3.
3. **USD/INR**: +3% adds ~+2.2% (revenue in USD, ~52% of cost in INR), but only for ~4-6 quarters. The pack's empirical sign is negative (not significant) - flagged.
4. **US visa/outsourcing policy**: -3.5 per unit of tightening; tail only, recent events (PERM suspension, $100k fee struck down) were mild.
5. **Risk sentiment and FPI flows**: premium multiple on an under-owned (FII 6.15%) stock.
6. **Rates**: Indian 10y has a small duration effect; Fed/US 10y effects are ambiguous (demand vs valuation).

## Transmission examples
- **Middle East escalation -> Brent up -> global risk-off**: C_MIDEAST_CONFLICT -> F_BRENT (+) -> F_RISK_SENTIMENT (VIX up) -> FPI outflows -> LTM de-rates (order 3-4); separately Brent up -> INR weaker (India imports ~85% of crude) -> LTM margin +; the net is negative in the first month, mildly positive over 6-12 months if no US recession.
- **Fed hawkish surprise -> F_US_10Y up -> US equities down -> BFSI/tech client budgets cut -> LTM deal conversion slows (order 4)**; simultaneously higher US yields strengthen USD -> INR weaker -> margin tailwind partly offsets.
- **US HIRE-style tax on outsourcing -> P_US_VISA_OUTSOURCING -> onsite cost up, clients pull work offshore or delay -> sector-wide de-rating including LTM**.
- **Group channel**: L&T share-price moves transmit weakly into LTM (w 0.10) while LTM moves feed L&T value (w 0.12) - used only for index/sentiment spillover.

## Current situation
Q2 FY27 on 2026-10-16: AI revenue +47%, margins steady, but sequential profit fell and the sell-off in IT (Infosys and Wipro at six-year lows on 2026-09-29) weighed on the whole group. The stock rose 9.3% in the last month on the sector bounce and the PERM-related relief. Newsflow: a deal with a US engineering & construction firm (2026-10-15), Google Cloud Gemini Enterprise expansion (2026-10-07), BlueVerse AgenTraceIQ with Rubrik (2026-10-05).

## Upcoming
Q3 FY27 results mid-January 2027 (peers TCS/HCL/Infosys report earlier and set the tone); possible U.S. policy actions on H-1B; dividend payout mechanics; AI revenue trajectory.

## Bull case
AI deals become larger and longer, margins climb with the pyramid, INR stays weak at ~94-95, US spending recovers: premium multiple holds and earnings grow mid-teens.

## Bear case
GenAI reprices application maintenance faster than AI revenue scales, the premium multiple compresses toward 18x, and US policy adds cost. Data inconsistencies in the headline numbers also lower confidence in the margin trajectory.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.