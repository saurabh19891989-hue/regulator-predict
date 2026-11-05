# NHPC — NHPC Ltd.
*MIDCAP_100 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.5%** (rank 58 / 40 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 53%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.2% … P90 +3.3%; plausible 12m relative-return range incl. stock-specific noise: -17.3% … +34.8%
- Decomposition (12m): 0.5 × forward event exposure +2.4% (3m +0.8%; half assumed priced) + 0.5 × company-specific catalysts +1.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.7% (beta-adjusted) vs a realised market-adjusted move of +0.0% — gap -0.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.89 | +2.50 | +0.39 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.08 | -2.00 | -0.08 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.63 | +1.50 | +0.08 | +0.02 | +0.03 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.34 | +0.00 | -0.77 | -0.53 | -0.04 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.33 | +0.00 | -0.66 | -0.32 | -0.36 | -1.1% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.23 | +0.00 | -1.12 | -0.08 | -0.02 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +0.95 | +1.00 | -0.03 | +0.04 | -0.06 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.94 | +0.00 | -0.56 | -0.33 | -0.05 | +3.5% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.93 | -0.50 | -0.45 | +0.02 | +0.00 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.85 | +0.00 | -0.82 | -0.08 | +0.04 | +9.4% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.80 | +0.00 | +0.00 | -0.37 | -0.43 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.6% | -3.6% | -3.3 | -0.2 | -0.0 | -0.1 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +3.3% | +3.3% | +3.2 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.1% | +2.0% | +3.8 | +0.2 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -0.9 | -0.6 | -0.1 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.4% | +1.4% | +1.2 | +0.2 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | -0.0 |
| Electricity (Amendment) Bill / distribution parallel licensing and DISCOM privatisation steps (`EV_POWER_DISTRIB_REFORM`) | anticipated | 0.45 | +2.5% | +1.1% | +2.5 | +0.0 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.1 | -0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.9 | -0.2 | +0.0 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +1.7% | +1.0% | +1.7 | +0.0 | +0.0 | +0.0 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -2.0% | -1.0% | -1.8 | -0.1 | -0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NHPC | +3.75% | +1.88% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → NHPC | +2.50% | +1.12% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → NHPC | -1.60% | -0.80% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → NHPC | +1.25% | +0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → NHPC | -1.00% | -0.60% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → NHPC | +0.80% | +0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → NHPC | -2.25% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → NHPC | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → NHPC | -1.44% | -0.36% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → NHPC | -0.40% | -0.36% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → NHPC | +0.90% | +0.36% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → NHPC | -0.60% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → NHPC | -2.00% | -0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NHPC | -1.40% | -0.35% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → NHPC | +0.40% | +0.34% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → NHPC | +1.55 | director_override | -3.10% |
| 1 | F_FPI_FLOWS → NHPC | -1.60 | events | -2.40% |
| 1 | P_RENEWABLE_SUPPORT → NHPC | +0.60 | director_override | +1.50% |
| 1 | F_MONSOON → NHPC | -1.56 | events | -1.25% |
| 1 | F_POWER_DEMAND_IN → NHPC | +1.20 | events | +0.72% |
| 1 | F_STEEL_INDIA → NHPC | +1.35 | events | -0.54% |
| 1 | F_REPO_IN → NHPC | +1.00 | events | -0.50% |
| 1 | T_ENERGY_TRANSITION → NHPC | +0.30 | director_override | +0.45% |
| 1 | F_CREDIT_SPREADS_IN → NHPC | +0.50 | events | -0.40% |
| 1 | F_GOVT_CAPEX → NHPC | +0.20 | director_override | +0.20% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further Subansiri Lower units commissioned (Unit 5 on 21 Oct 2026; 4 units were remaining at Jun-26 per presentation) lifting regulated equity | capex | 0.80 | +1.5% | +1.20% |
| 2027-01 | Q3 FY27 results (Q2 declared 4 Nov; estimate late Jan/early Feb 2027) | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | Kiru (624 MW), Pakal Dul (1,000 MW) and Rangit-IV commissioning scheduled Q3-Q4 FY27 (slippage typical) | capex | 0.40 | +2.5% | +1.00% |
| 2027-03 | Kamala (1,720 MW) forest clearance and Sawalkot (1,856 MW) construction start | regulatory | 0.50 | +1.5% | +0.75% |
| 2027-03 | Further government OFS in NHPC (promoter 61.4% after Q1 FY27 sale; government remains seller of PSU stakes) | corporate_action | 0.25 | -3.8% | -0.94% |
| 2027-06 | Additional provisions or cost overruns on Teesta-IV or arbitration outcomes | litigation | 0.30 | -1.8% | -0.53% |

## Analyst profile (agent research, sourced)
# NHPC — NHPC Ltd. (as of 2026-11-05)

*Scenario/exposure analysis relative to the Nifty 200; not a validated forecast. Primary source: NHPC investor presentation for Q1 FY27 (June 2026), screener.in and headline searches (Q2 FY27 results of 4 Nov 2026 were read only via headlines). Sources are in `NHPC.json`.*

## Business
NHPC is India's largest hydropower company: 9,333 MW operating (8,771 MW hydro, about 17% of national hydro capacity, plus 562 MW of solar and wind), 9,204 MW under construction and about 10 GW awaiting clearances, including Subansiri Lower (2,000 MW, being commissioned unit by unit), Parbati-II, Teesta-VI, Kiru, Kwar, Ratle and Pakal Dul. Revenue is regulated: CERC tariffs give cost recovery on normative debt and a 15.5% RoE on regulated equity, tied to plant availability rather than volume. Profit therefore grows as new capacity enters the regulated equity base, not with commodity or power prices. Q2 FY27 revenue was Rs 4,483 cr (+33%), profit Rs 1,658 cr (+36%) after a Rs 231 cr Teesta IV provision. The government holds 61.4% after a stake sale in Q1 FY27. P/E 18.8; dividend yield 2.0%.

## What moves the stock
1. **Yields and bond-proxy status (G-sec -2.0, repo -0.5, spreads -0.8).** The valuation behaves like a long-duration government-backed annuity. RBI hiked on 7 Oct; 10-year G-sec yields moved with it.
2. **Project delivery and costs.** The key company-specific driver: timely commissioning adds regulated equity; geological problems and cost overruns (Teesta IV provision; Rs 5,737 cr overrun on four J&K projects) delay it. Edges: steel -0.4 (cost), government capex +1.0, renewable policy +2.5.
3. **Discom payment (P_POWER_REFORM +2.5).** Receivables were Rs 4,354 cr at June 2026 versus Rs 2,629 cr at March.
4. **Hydrology (F_MONSOON +0.8)** is small and two-sided because tariffs are availability-based.
5. **Government stake sales and flows (FPI +1.5).** Promoter ownership dropped from 67.4% to 61.4%, and the Centre continues OFS programmes (LIC OFS on 4 Aug 2026 shows the pace).
6. **Geopolitics (C_INDIA_PAKISTAN +0.5).** Indus Waters Treaty abeyance speeds up Chenab projects but raises security risk.
The pack's empirical iron-ore (+3.48) and gold (-2.03) loadings are PSU/risk-cycle co-movements and are not carried.

## Worked transmission examples
- **Middle East conflict -> Brent and inflation up, RBI "calibrated tightening" (1st-2nd) -> G-sec yields up (3rd) -> NHPC's 2% dividend yield looks less attractive versus bonds, bond-proxy PSU derates despite fixed regulated returns (4th).**
- **Weak monsoon (13% below normal in Q2) -> lower inflows to run-of-river plants (1st) -> less secondary energy but unchanged fixed charges (2nd) -> thermal plants run harder and power prices rise, making hydro's peaking capacity more valuable in a tight market (3rd) -> support for more hydro/PSP approvals and VGF (4th).**
- **Indus Waters Treaty in abeyance -> India fast-tracks storage and run-of-river projects on the Chenab (1st) -> NHPC's Sawalkot (1,856 MW), Kiru, Kwar, Ratle start or accelerate (2nd) -> capex and borrowings rise before regulated returns start (interest during construction) (3rd) -> higher near-term leverage; long-run rate base growth (4th); escalation risk with Pakistan adds attack and availability risk on J&K assets.**

## Current situation
Q2 profit growth was strong on new capacity but interest costs doubled as projects were capitalised; borrowings reached Rs 57.4k cr. The stock rose 11% in a month to Rs 81, close to its 52-week high of Rs 86.9. Unit 5 of Subansiri Lower was commissioned on 21 Oct; Kamala is awaiting forest clearance.

## Upcoming events
More Subansiri units and Kiru/Pakal Dul/Rangit-IV commissioning (FY27 Q3-Q4), approvals for Kamala and Sawalkot work, possible further OFS, Q3 FY27 results (late Jan 2027, estimated). See `company_events`.

## Bull and bear
**Bull:** commissioning ahead of schedule, regulated equity grows 15%+, strategic fast-tracking of Chenab projects, high dividends. **Bear:** more provisions and overruns, further government OFS, higher yields, discom delays.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.