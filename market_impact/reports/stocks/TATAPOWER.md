# TATAPOWER — Tata Power Co. Ltd.
*NIFTY_NEXT_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.7%**, **12 months +6.0%** (rank 24 / 33 of 200 for 3m / 12m); beta 1.23
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 63%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +1.0% … P90 +9.1%; plausible 12m relative-return range incl. stock-specific noise: -18.8% … +27.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.8 pp (model impact +9.7% beta-adjusted vs realised market-adjusted move -18.9%); forward event exposure +2.4% (3m +1.5%; half assumed priced); company-specific events +2.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +5.24 | +4.00 | +1.07 | +0.17 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.69 | +0.00 | -1.71 | -1.78 | -0.21 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +3.35 | +3.00 | +0.34 | +0.00 | +0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.68 | -2.50 | -0.18 | +0.00 | -0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +2.60 | +2.50 | +0.10 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.21 | +2.00 | +0.08 | +0.03 | +0.10 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +2.08 | +1.50 | +0.54 | +0.04 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.93 | +0.00 | +0.00 | -0.94 | -0.99 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -1.80 | -1.80 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.58 | -1.00 | -0.61 | +0.00 | +0.03 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.39 | +0.00 | -0.72 | -0.48 | -0.19 | +3.5% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -1.32 | +0.00 | -1.07 | -0.51 | +0.26 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.31 | +0.00 | -1.05 | -0.22 | -0.04 | +9.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +6.0% | +6.0% | +5.5 | +0.5 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.7% | -5.7% | +0.4 | -0.9 | -2.4 | -2.9 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.9% | -4.9% | -4.4 | -0.2 | -0.1 | -0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.3% | -4.3% | +0.0 | -2.0 | -2.0 | -0.3 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.0% | -4.0% | -4.0 | +0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.8% | +3.8% | +3.6 | +0.2 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.6% | +2.8% | +5.0 | +0.2 | +0.1 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -2.4 | -0.3 | -0.1 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +2.6% | +2.6% | +2.0 | +0.5 | +0.1 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -2.2 | -0.2 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | -0.0 | +0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -6.6% | -1.9% | +0.0 | -4.8 | -1.3 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATAPOWER | +5.00% | +2.50% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → TATAPOWER | +2.50% | +1.12% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATAPOWER | -2.00% | -1.00% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → TATAPOWER | +2.25% | +0.90% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → TATAPOWER | +2.10% | +0.84% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TATAPOWER | -2.99% | -0.84% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → TATAPOWER | +1.25% | +0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → TATAPOWER | -1.25% | -0.75% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TATAPOWER | -3.73% | -0.67% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TATAPOWER | -3.00% | -0.66% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → TATAPOWER | -0.86% | -0.58% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → TATAPOWER | -0.60% | -0.57% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → TATAPOWER | -2.50% | -0.55% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → TATAPOWER | +0.90% | +0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TATAPOWER | -1.92% | -0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_RENEWABLE_SUPPORT → TATAPOWER | +1.50 | events | +6.00% |
| 1 | F_GSEC_10Y_IN → TATAPOWER | +1.70 | events | -4.25% |
| 1 | F_FPI_FLOWS → TATAPOWER | -1.60 | events | -3.20% |
| 1 | F_POWER_PRICE_IN → TATAPOWER | +3.00 | events | +2.10% |
| 1 | F_POWER_DEMAND_IN → TATAPOWER | +1.20 | events | +1.80% |
| 1 | T_ENERGY_TRANSITION → TATAPOWER | +0.50 | events | +1.50% |
| 1 | F_REPO_IN → TATAPOWER | +1.00 | events | -1.00% |
| 1 | F_CREDIT_SPREADS_IN → TATAPOWER | +0.50 | events | -0.90% |
| 1 | F_COAL_INTL → TATAPOWER | +0.70 | director_override | +0.70% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → TATAPOWER | +1.50 | events | +0.48% |
| 1 | C_MIDEAST_CONFLICT → TATAPOWER | +1.50 | events | +0.45% |
| 1 | P_ANTI_DUMPING_IN → TATAPOWER | +0.40 | events | +0.40% |

## Analyst profile (agent research, sourced)
# TATAPOWER — Tata Power Co. Ltd. (as of 2026-11-05)

*Scenario/exposure analysis relative to the Nifty 200; not a validated forecast. Primary source: Q1 FY27 earnings call (28 Jul 2026, filed on BSE), screener.in (financials through Jun 2026; Q2 FY27 results were not yet published as of 5 Nov 2026) and headline searches. The Q2 results date was not confirmed in this research. "Model knowledge" marks facts from training memory.*

## Business
Tata Power is a diversified utility with five engines. (1) Generation: the 4 GW Mundra imported-coal UMPP (now on a supplementary PPA that reimburses actual coal cost and normative fixed cost but pays no ROE), Jojobera and Maithon thermal, and hydro. (2) Renewables: 6.7 GW operating, 2.5-2.7 GW to be added in FY27 to pass 9 GW. (3) Transmission and distribution: Mumbai licence, Delhi, three Odisha DISCOMs, Ajmer, plus TBCB lines (Mumbai transmission alone has about Rs 10,000 cr regulated investment over five years). (4) Manufacturing and rooftop: TP Solar (cells and modules, 1 GW of modules and 0.9 GW of cells in Q2 FY27) and rooftop solar (revenue about doubled last year). (5) Coal mining and shipping in Indonesia, EV charging, pumped storage (first unit CY2029) and Bhutan hydro. Q1 FY27 PAT Rs 1,401 cr (+11%) and underlying EBITDA Rs 4,249 cr (+8%); net debt/underlying EBITDA 3.41x and net debt/equity 1.25x; capex Rs 6,000-6,500 cr in a quarter.

## What moves the stock
1. **Rates and spreads (G-sec -2.5, spreads -1.8, repo -1.0).** EV/MCap is about 1.5 with capex outstripping cash flow. The RBI hiked 25bp on 7 Oct 2026 and the US 10y is 4.89%. Regulated T&D partially recovers interest; renewables with fixed tariffs do not. The pack's US-10y beta is -0.99 per 25bp (t -1.7), consistent with the model.
2. **Policy for renewables and manufacturing (P_RENEWABLE_SUPPORT +4, anti-dumping +1.0).** ALMM-II continues; the "rollback" covers only about 10% of DCR demand.
3. **Distribution quality (P_POWER_REFORM +2.5, grid +2.0).** Odisha collections and Delhi/Mumbai tariff orders matter more than wholesale prices.
4. **Coal (F_COAL_INTL +1.0).** Indonesian mine earnings benefit from high seaborne coal while Mundra is a pass-through.
5. **Idiosyncratic legal and governance risks.** The Kleros US$490 mn arbitration award (about Rs 4,600 cr, about 4% of market cap) survived a Singapore court challenge on 26-27 Aug and is under appeal. The Tata Sons listing dispute (Trusts rejected listing on 18 Sep) took about Rs 40,000 cr off Tata stocks, and Tata Steel group contagion (0.12) is carried as a company link.
6. **Demand, power price and flows.** Demand +1.5, spot price +0.7, FPI +2.0, rupee +0.2.
Pack: iron ore (t +3.4) and steel (t +2.0) loadings are group/Tata-complex co-movement, not raw-material links.

## Worked transmission examples
- **Middle East conflict -> Hormuz LNG disruption and higher coal prices (1st) -> Indonesian coal earnings up, Mundra neutral because actual coal cost is reimbursed (2nd) -> but Brent/inflation up, RBI tightens (3rd) -> higher debt servicing on a 3.4x levered capex programme, valuation multiple compresses (4th).** Net small positive in earnings, negative in multiple.
- **Weak monsoon -> demand growth 8-11% (1st) -> Mundra scheduled at full capacity under Section 11 / SPPA, distribution volumes up (2nd) -> better fixed-cost absorption and Odisha/Delhi sales growth, but only partially because tariffs are regulated (3rd) -> faster PSP and RE financing at lower leverage ratios (4th).**
- **Tata Sons governance dispute -> Trusts reject listing, headlines about rift (1st) -> Tata group stocks fall together (2nd) -> higher cost of capital for group companies through weaker credit sentiment; S&P says little rating impact (3rd) -> any Tata Sons capital event (stake sale, dividend) could re-rate Tata Power (4th).**
- **Chinese cell/wafer anti-dumping duties (P_ANTI_DUMPING_IN) -> imported cell costs rise (1st) -> TP Solar's integrated cells become competitive and module prices firm up (2nd) -> rooftop and EPC margins pressured unless DCR cells are used (3rd) -> TP Solar utilisation and Tata Power's capex mix shift (4th).**

## Current situation
27 consecutive quarters of profit growth (management). Stock Rs 364, -17% over six months, 22% annualised volatility, close to the bottom of its Rs 333-465 range. Management expects Q1 to be 4.5-5x annualised (seasonally low). Renewable additions in Q2 (419 MW at Tata Power Renewable) doubled year on year; 500 MW had slipped from end-June due to transmission delays. Odisha DISCOM growth was muted in Q1 by three issues, including collections and state dues.

## Upcoming events
Q2 FY27 results (November; date unconfirmed), remaining state approvals for the Mundra SPPA, Singapore appeal on the Kleros award, Shirwata 1,800 MW PSP approval, Tata Sons listing decision, and Q3 results (late January 2027). See `company_events`.

## Bull and bear
**Bull:** renewables reach 9 GW, rooftop and manufacturing scale, Mundra secured to 2038, Kleros award reduced on appeal, Tata Sons event unlocks value. **Bear:** a higher-for-longer rate path squeezes returns on 3.4x leverage, Odisha collections or Delhi tariffs disappoint, adverse Kleros outcome, solar manufacturing margins compress.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.