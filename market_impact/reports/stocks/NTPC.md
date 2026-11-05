# NTPC — NTPC Ltd.
*NIFTY_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.0%**, **12 months +2.1%** (rank 66 / 67 of 200 for 3m / 12m); beta 1.01
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.3%): 3 months 54%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.6% … P90 +4.0%; plausible 12m relative-return range incl. stock-specific noise: -25.6% … +23.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +2.1 pp (model impact +4.2% beta-adjusted vs realised market-adjusted move -20.8%); forward event exposure +1.7% (3m +1.5%; half assumed priced); company-specific events +0.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.53 | +0.00 | -1.21 | -1.25 | -0.08 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.17 | +2.00 | +0.10 | +0.01 | +0.06 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.06 | -2.00 | -0.06 | +0.00 | -0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.98 | +2.00 | -0.03 | +0.00 | +0.01 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.92 | +2.00 | -0.08 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.49 | +1.00 | +0.50 | -0.02 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.37 | +0.00 | +0.00 | -0.67 | -0.71 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.37 | +0.00 | -0.77 | -0.48 | -0.12 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -1.32 | +0.00 | -0.93 | -0.24 | -0.15 | +2.2% |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.23 | +1.00 | +0.20 | +0.03 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.17 | -0.20 | -0.37 | -0.36 | -0.24 | -1.1% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.13 | +0.00 | -0.92 | -0.19 | -0.03 | +9.4% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.12 | +0.00 | +0.64 | +0.41 | +0.08 | +1.2% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.07 | +0.00 | -0.30 | -0.40 | -0.37 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.8% | -4.8% | -4.4 | -0.2 | -0.0 | -0.2 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.0% | -4.0% | +1.5 | -1.5 | -2.0 | -2.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -1.4 | -1.4 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.5% | +2.7% | +5.0 | +0.3 | +0.0 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -2.2 | -0.2 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.2% | +2.2% | +2.2 | +0.0 | +0.0 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -2.0 | -0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -7.1% | -2.0% | +0.0 | -5.7 | -1.2 | -0.2 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.0% | +2.0% | +2.0 | -0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.2 | -0.3 | -0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -7.5% | -1.3% | +0.0 | -6.3 | -0.9 | -0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NTPC | +5.00% | +2.50% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → NTPC | +2.00% | +0.90% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NTPC | -2.99% | -0.84% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → NTPC | -1.60% | -0.80% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NTPC | -3.73% | -0.67% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → NTPC | -3.00% | -0.66% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → NTPC | +1.50% | +0.60% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → NTPC | +1.00% | +0.60% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → NTPC | -1.00% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → NTPC | -1.00% | -0.58% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → NTPC | -1.92% | -0.54% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → NTPC | +1.20% | +0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → NTPC | -1.92% | -0.48% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → NTPC | -0.48% | -0.46% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → NTPC | -2.00% | -0.44% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → NTPC | +1.70 | events | -3.40% |
| 1 | F_FPI_FLOWS → NTPC | -1.60 | events | -3.20% |
| 1 | C_MIDEAST_CONFLICT → NTPC | +1.50 | events | +1.50% |
| 1 | P_RENEWABLE_SUPPORT → NTPC | +1.50 | events | +1.50% |
| 1 | F_POWER_PRICE_IN → NTPC | +3.00 | events | +1.20% |
| 1 | F_POWER_DEMAND_IN → NTPC | +1.20 | events | +1.20% |
| 1 | T_ENERGY_TRANSITION → NTPC | +0.50 | events | +1.00% |
| 1 | F_COAL_INTL → NTPC | +0.70 | director_override | +0.63% |
| 1 | F_REPO_IN → NTPC | +1.00 | events | -0.60% |
| 1 | F_COAL_INDIA → NTPC | +1.50 | events | +0.30% |
| 1 | F_CREDIT_SPREADS_IN → NTPC | +0.50 | events | -0.30% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → NTPC | +1.00 | events | +0.16% |

## Analyst profile (agent research, sourced)
# NTPC — NTPC Ltd. (as of 2026-11-05)

*Scenario/exposure analysis relative to the Nifty 200; not a validated forecast. Primary source: NTPC's Q2/H1 FY27 operational and financial snapshot (30 Sep 2026 data), screener.in and headline searches; sources in `NTPC.json`. The earnings-call recording was not transcribed.*

## Business
NTPC is India's largest power producer: 91,506 MW of group capacity (60,992 MW standalone), with 36,899 MW under construction (17.3 GW coal, 3.6 GW hydro, 16.0 GW renewables mostly through NTPC Green Energy). Coal and gas stations are CERC-regulated: fixed charges are tied to availability (coal PAF 90.3% in H1), fuel is passed through at actual cost, and the return is 15.5% on regulated equity (Rs 92.9k cr standalone; Rs 1.22 lakh cr consolidated). That makes earnings a function of regulated-equity growth, incentives/rebates and subsidiary profits rather than of power prices. Q2 FY27: consolidated PAT Rs 7,351 cr (+41%), standalone PAT Rs 5,320 cr (+14%); a first interim dividend of Rs 3 was declared. Group debt is Rs 2.76 lakh cr (debt/equity 1.29). The stock is at P/E 10.3, 2.8% dividend yield, down 21% in six months, and touched a 52-week low in October with other CPSEs.

## What moves the stock
1. **Bond-proxy valuation (G-sec -2.0, repo -0.6, spreads -0.6).** The RBI hiked 25bp on 7 Oct and the US 10y is at 4.89%; the PSU basket derated.
2. **Regulated equity and capacity additions.** Company-specific: standalone regulated equity fell year on year after coal mines moved to NTPC Mining, so growth now comes from subsidiaries.
3. **Policy and regulation (P_POWER_REFORM +2.0, renewables +1.0, energy transition +2.0)**: discom payment security, the next tariff control period, nuclear/PSP/BESS options.
4. **Fuel and demand (coal intl +0.9, domestic coal +0.2, demand +1.0)**. Demand drove coal PLF to 73.5% (66.0% LY) but fixed charges limit the earnings effect.
5. **Flows and sentiment (FPI +2.0, domestic flows +1.0, Mideast +1.0)**. LIC lifted its stake to 7.0%.
Pack: coal (+2.71, t +2.3) and Brent (+1.01, t +2.4) loadings are significant. The coal loading is partly supported (captive mines, tight market); Brent has no fundamental channel and is carried at low confidence.

## Worked transmission examples
- **Hormuz disruption -> LNG shortage and oil up (1st) -> Asia switches to coal, seaborne coal up (2nd) -> India prioritises domestic coal and nuclear for energy security, and pass-through of fuel keeps NTPC whole (3rd) -> NTPC's captive mining profit and PLF incentives rise while higher yields lower the multiple (4th).**
- **Weak monsoon -> hydro down, demand up 11% (1st) -> coal stocks at plants critical, government orders captive plants to maximise output (2nd) -> NTPC's PAF and PLF higher; incentive income rises, disincentive falls (Rs 187 cr in Q2 vs Rs 488 cr) (3rd) -> modest standalone EBITDA growth (3.8% in Q2) because revenue is capacity-based (4th).**
- **RBI hike -> higher bond yields (1st) -> NTPC's dividend yield less attractive versus bonds, CPSE basket falls to 52-week lows (2nd) -> higher cost on new borrowing for Rs 24k cr half-year capex (3rd) -> recoverable through tariffs only on normative debt; incremental funding stress at NGEL and PVUNL (4th).**

## Current situation
Consolidated H1 PAT was Rs 14,247 cr (+26%). Subsidiaries' profit was Rs 3,194 cr (Rs 1,805 cr LY) and joint ventures contributed Rs 1,253 cr. Standalone EBITDA rose 3.8% in Q2. Jefferies and Nuvama remain bullish; the stock rose 3% on 2 Nov.

## Upcoming events
Interim dividend payment, Q3 results (late January 2027, estimated), FY27 commissioning, NGEL tenders, possible tariff-regulation consultations for 2029-34, and any further government stake sale. See `company_events`.

## Bull and bear
**Bull:** capacity additions grow regulated equity, nuclear/PSP optionality, low P/E and high yield, rate relief. **Bear:** yields stay high, standalone regulated equity stagnates, discom payment or regulatory changes, fuel supply stress.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.