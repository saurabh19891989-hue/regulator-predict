# NHPC — NHPC Ltd.
*MIDCAP_100 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.0%**, **12 months +2.4%** (rank 63 / 64 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 54%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.0% … P90 +5.9%; plausible 12m relative-return range incl. stock-specific noise: -27.0% … +27.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.1 pp (model impact +2.2% beta-adjusted vs realised market-adjusted move +0.0%); forward event exposure +3.4% (3m +1.1%; half assumed priced); company-specific events +1.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.89 | +2.50 | +0.39 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.44 | +0.00 | -1.06 | -1.29 | -0.09 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.08 | -2.00 | -0.08 | +0.00 | -0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.96 | +0.00 | -0.66 | -0.76 | -0.55 | -1.1% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.66 | +1.50 | +0.08 | +0.02 | +0.06 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.30 | +0.00 | +0.00 | -0.58 | -0.72 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.26 | +0.00 | -1.12 | -0.11 | -0.03 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.06 | +0.00 | -0.56 | -0.38 | -0.12 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.05 | +0.00 | +0.00 | -0.37 | -0.68 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.04 | +0.00 | -0.66 | -0.21 | -0.17 | +2.2% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.00 | +0.00 | -0.18 | -0.40 | -0.42 | +0.0% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.99 | +0.00 | -0.82 | -0.15 | -0.02 | +9.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.5% | -5.5% | +0.0 | -0.9 | -2.3 | -2.4 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.7% | -3.7% | -3.3 | -0.2 | -0.1 | -0.2 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +3.3% | +3.3% | +3.2 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -1.2 | -1.5 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.9 | -0.2 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.2% | +2.1% | +3.8 | +0.2 | +0.1 | +0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.7 | -0.1 | -0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.4% | +1.4% | +1.2 | +0.2 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.0% | -1.4% | +0.0 | -1.1 | -1.5 | -1.4 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.0 | -0.3 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.8% | -1.3% | +0.0 | -3.7 | -0.9 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → NHPC | -3.30% | -3.30% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → NHPC | -2.80% | -2.80% |
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → NHPC | +2.50% | +2.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NHPC | +3.75% | +1.88% |
| 1 | EV_SOLAR_ALMM2_CELL_MANDATE ⇒ P_RENEWABLE_SUPPORT → NHPC | +1.25% | +1.25% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → NHPC | +2.50% | +1.12% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → NHPC | -1.05% | -1.05% |
| 1 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → NHPC | -1.01% | -1.01% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → NHPC | +1.00% | +1.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → NHPC | -0.89% | -0.89% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → NHPC | -0.88% | -0.88% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → NHPC | -1.60% | -0.80% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_GSEC_10Y_IN → NHPC | -0.78% | -0.78% |
| 1 | EV_BESS_VGF_NOV26 ⇒ T_ENERGY_TRANSITION → NHPC | +0.75% | +0.75% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → NHPC | +1.25% | +0.75% |

## Analyst profile (agent research, sourced)
_Profile not yet available._

## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.