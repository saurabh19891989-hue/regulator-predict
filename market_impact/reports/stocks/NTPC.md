# NTPC — NTPC Ltd.
*NIFTY_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months +0.3%** (rank 120 / 83 of 200 for 3m / 12m); beta 1.01
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.3%): 3 months 50%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.6% … P90 +3.0%; plausible 12m relative-return range incl. stock-specific noise: -24.0% … +27.0%
- Decomposition (12m): 0.5 × forward event exposure +0.5% (3m +0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.0% (beta-adjusted) vs a realised market-adjusted move of -20.8% — gap +22.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.14 | +2.00 | +0.10 | +0.01 | +0.03 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.06 | -2.00 | -0.06 | +0.00 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.99 | +2.00 | -0.03 | +0.00 | +0.02 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.92 | +2.00 | -0.08 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.49 | +1.00 | +0.50 | -0.02 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.37 | +0.00 | -0.87 | -0.46 | -0.04 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.22 | +1.00 | +0.20 | +0.01 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.18 | +0.00 | -0.77 | -0.38 | -0.02 | +3.5% |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.06 | +1.00 | +0.04 | +0.01 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.01 | -0.60 | -0.44 | +0.03 | -0.01 | — |
| International thermal coal price (`F_COAL_INTL`) | +15% seaborne thermal coal | +1.00 | +0.90 | +0.09 | +0.01 | +0.00 | +0.0% |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +0.99 | +1.00 | +0.00 | +0.00 | -0.01 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -0.97 | +0.00 | -0.94 | -0.03 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.96 | +0.00 | -0.80 | -0.09 | -0.07 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.7% | -4.7% | -4.4 | -0.2 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.4% | +2.7% | +5.0 | +0.3 | +0.0 | +0.1 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.2% | +2.2% | +2.2 | +0.0 | +0.0 | +0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.0% | +2.0% | +2.0 | -0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.0 | -0.5 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.0% | -1.2% | +0.0 | -4.6 | -0.5 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.3 | -0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.0 | -0.2 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.2% | +1.2% | +1.0 | +0.2 | +0.0 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -6.1% | -1.1% | -5.9 | -0.2 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NTPC | +5.00% | +2.50% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → NTPC | +2.00% | +0.90% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → NTPC | -1.60% | -0.80% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → NTPC | +1.50% | +0.60% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → NTPC | +1.00% | +0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → NTPC | -1.00% | -0.55% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → NTPC | -3.00% | -0.54% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → NTPC | +1.20% | +0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → NTPC | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → NTPC | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NTPC | -1.87% | -0.47% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → NTPC | -0.57% | -0.39% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → NTPC | -0.40% | -0.36% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → NTPC | +0.60% | +0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → NTPC | -0.60% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → NTPC | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → NTPC | +1.55 | director_override | -3.10% |
| 1 | F_POWER_DEMAND_IN → NTPC | +1.20 | events | +1.20% |
| 1 | C_MIDEAST_CONFLICT → NTPC | +1.00 | events | +1.00% |
| 1 | F_POWER_PRICE_IN → NTPC | +1.90 | director_override | +0.76% |
| 1 | F_COAL_INTL → NTPC | +0.70 | director_override | +0.63% |
| 1 | P_RENEWABLE_SUPPORT → NTPC | +0.60 | director_override | +0.60% |
| 1 | T_ENERGY_TRANSITION → NTPC | +0.30 | director_override | +0.60% |
| 1 | F_REPO_IN → NTPC | +1.00 | events | -0.60% |
| 1 | F_COAL_INDIA → NTPC | +1.50 | events | +0.30% |
| 1 | F_CREDIT_SPREADS_IN → NTPC | +0.50 | events | -0.30% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → NTPC | +0.50 | director_override | +0.08% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Interim dividend Rs 3/share record/payment (date per exchange filing, not verified) | corporate_action | 0.95 | -0.5% | -0.47% |
| 2027-01 | Q3 FY27 results (Q2 on 30-31 Oct; estimate late Jan 2027) | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | FY27 commissioning guidance: ~4-5 GW group capacity added (2.4 GW in H1; Nabinagar, Talcher, Gadarwara etc. under construction) | capex | 0.70 | +1.5% | +1.05% |
| 2027-03 | Further government OFS or disinvestment in NTPC (51.1% held; 52-week-low PSU basket) | corporate_action | 0.10 | -3.2% | -0.33% |
| 2027-03 | NTPC Green Energy new tender wins/BESS commissioning (500 MW tender win 23 Aug 2026) | capex | 0.60 | +0.8% | +0.51% |
| 2027-06 | CERC / MoP actions on tariff regulations for 2029-34 control period (consultation) and coal pass-through changes | regulatory | 0.25 | -0.5% | -0.12% |

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