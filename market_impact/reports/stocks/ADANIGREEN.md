# ADANIGREEN — Adani Green Energy Ltd.
*NIFTY_NEXT_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +0.4%** (rank 67 / 71 of 200 for 3m / 12m); beta 1.62
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +36.6%): 3 months 51%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.2% … P90 +4.3%; plausible 12m relative-return range incl. stock-specific noise: -50.0% … +49.2%
- Decomposition (12m): 0.5 × forward event exposure -0.3% (3m +0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.7%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.5% (beta-adjusted) vs a realised market-adjusted move of -9.7% — gap +11.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +6.98 | +6.00 | +1.01 | -0.03 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +3.97 | +4.00 | -0.06 | +0.00 | +0.03 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.75 | -3.50 | -0.25 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.32 | +3.00 | +0.23 | +0.03 | +0.06 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.88 | +2.80 | +0.05 | +0.02 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.65 | +0.00 | -1.62 | -0.92 | -0.11 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.52 | -2.50 | +0.00 | +0.00 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.37 | -1.00 | -0.56 | -0.35 | -0.45 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.93 | +0.00 | -1.24 | -0.62 | -0.08 | +3.5% |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.86 | +2.00 | -0.14 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.74 | -1.00 | -0.80 | +0.02 | +0.04 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.73 | +0.00 | -1.40 | -0.23 | -0.11 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.64 | +0.00 | -1.51 | -0.22 | +0.09 | +9.4% |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.52 | +1.20 | +0.30 | +0.02 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +8.0% | +8.0% | +8.0 | -0.1 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.3% | -7.3% | -6.6 | -0.5 | -0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.7% | -5.7% | -5.7 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.4% | +4.2% | +7.5 | +0.6 | +0.1 | +0.2 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +3.5% | +3.5% | +3.0 | +0.5 | -0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.3% | +3.3% | +3.3 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -1.9 | -1.1 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.5% | -2.5% | -2.5 | +0.0 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.9% | -2.2% | +0.0 | -8.0 | -1.0 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -2.1 | -0.1 | +0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.7 | -0.3 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -11.2% | -2.0% | -10.3 | -1.0 | +0.0 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIGREEN | +7.50% | +3.75% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIGREEN | -2.80% | -1.40% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → ADANIGREEN | +2.00% | +0.90% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIGREEN | +2.10% | +0.84% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ADANIGREEN | -4.50% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIGREEN | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIGREEN | -2.88% | -0.72% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → ADANIGREEN | +1.80% | +0.72% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → ADANIGREEN | +1.20% | +0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIGREEN | -2.80% | -0.70% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → ADANIGREEN | -0.70% | -0.63% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → ADANIGREEN | -1.05% | -0.63% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → ADANIGREEN | -1.05% | -0.63% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → ADANIGREEN | -3.50% | -0.63% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → ADANIGREEN | +1.00% | +0.60% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → ADANIGREEN | +1.55 | director_override | -5.43% |
| 1 | F_FPI_FLOWS → ADANIGREEN | -1.60 | events | -4.80% |
| 1 | P_RENEWABLE_SUPPORT → ADANIGREEN | +0.60 | director_override | +3.60% |
| 1 | F_POWER_DEMAND_IN → ADANIGREEN | +1.20 | events | +1.44% |
| 1 | F_POWER_PRICE_IN → ADANIGREEN | +1.90 | director_override | +1.33% |
| 1 | F_CREDIT_SPREADS_IN → ADANIGREEN | +0.50 | events | -1.25% |
| 1 | T_ENERGY_TRANSITION → ADANIGREEN | +0.30 | director_override | +1.20% |
| 1 | F_REPO_IN → ADANIGREEN | +1.00 | events | -1.00% |
| 1 | C_MIDEAST_CONFLICT → ADANIGREEN | +1.00 | events | -0.40% |
| 1 | F_USDINR → ADANIGREEN | -0.37 | observed | +0.37% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → ADANIGREEN | +0.50 | director_override | +0.22% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → ADANIGREEN | -0.30 | events | -0.20% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Chitravathi 500 MW pumped-storage project commissioning by year-end and BESS >10 GWh by FY27 end | capex | 0.60 | +1.8% | +1.05% |
| 2027-01 | Q3 FY27 results (date not announced; Q2 was 22 Oct, estimate late Jan/early Feb 2027) | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | Phase-3 Khavda evacuation commissioned by end of Q4 FY27, enabling 4.5-5 GW of FY27 commissioning (mgmt says currently expects Q4) | capex | 0.55 | +4.5% | +2.48% |
| 2027-03 | FY27 commissioning target of 4.5-5 GW missed (grid readiness slips again) | guidance | 0.40 | -5.0% | -2.00% |
| 2027-03 | Conversion of ~974 MW merchant capacity to 25-yr fixed PPAs and new C&I/hyperscaler PPAs | other | 0.60 | +1.5% | +0.90% |
| 2027-03 | Renewed US/foreign legal-regulatory action vs Adani Group (criminal case dismissed 10 Aug 2026; SEC civil status not verified) | litigation | 0.06 | -16.5% | -0.99% |

## Analyst profile (agent research, sourced)
# ADANIGREEN — Adani Green Energy Ltd. (as of 2026-11-05)

*Scenario/exposure analysis relative to the Nifty 200; not a validated forecast. Sources are listed in `ADANIGREEN.json` (AGEL Q2 FY27 earnings presentation and call transcript, screener.in, Google-News headline searches). "Model knowledge" marks facts from training memory.*

## Business
AGEL develops, owns and operates utility-scale solar, wind and hybrid plants plus a fast-growing storage book. At 30 Sep 2026 it had 20,763 MW operational (14,550 MW solar, 3,266 MW hybrid, 2,947 MW wind; +24% YoY) and 6.6 GWh of battery storage, mostly at Khavda in Gujarat, the largest single-location renewable site in the world. The 2030 target is 50 GW, supported by a Rs 2.4 lakh cr capex programme. Revenue is contracted: nearly all capacity sits under 25-year fixed-tariff PPAs with SECI, NTPC, state discoms and private offtakers, and the PPAs are take-or-pay, with curtailment ordered by the grid paid for. EBITDA margin on power supply is about 92%, so the equity story is entirely about growth in operating MW, the cost of capital, and avoiding curtailment and counterparty slippage. Q2 FY27: revenue from power supply Rs 4,019 cr (+45%), EBITDA Rs 3,835 cr (+51%), but PAT only Rs 747 cr because interest (Rs 2,119 cr) and depreciation (Rs 1,084 cr) absorb most of EBITDA. Net debt Rs 102,973 cr (5.6x run-rate EBITDA), average cost 8.9% with 72% fixed, and 100% of foreign-currency debt principal hedged.

## What moves the stock
1. **Long-duration discount rate (G-sec -3.5, repo -1.0, spreads -2.5).** P/E is 119 and EV/MCap about 1.44. The RBI hiked 25bp on 7 Oct 2026 and the US 10y is 4.89%. Management argues rate risk is limited because 72-73% of project loans are fixed for three to five years and operating SPVs re-rate to AA/AAA (one SPV, about 15% of EBITDA, is now AAA at 8.4%). The valuation effect still dominates the earnings effect.
2. **Transmission readiness at Khavda (P_RENEWABLE_SUPPORT +6).** H1 EBITDA was Rs 8,276 cr versus about Rs 9,000 cr without curtailment. Management now says Phase-3 evacuation will arrive in Q4 FY27 rather than by December, but it still expects 4.5-5 GW of FY27 commissioning if the corridor is ready, and has accelerated BESS to soak up curtailed energy.
3. **Policy and theme support** (PM-DHARA corridor scheme, energy-transition and data-centre themes: +4.0 and +2.8) which broaden the PPA pipeline and underpin the valuation premium.
4. **Foreign flows and group sentiment** (FPI +3.0, group contagion 0.35 from Adani Enterprises). The US criminal case was dismissed on 10 Aug 2026; FII ownership is 11.3% and DIIs have risen from 2.4% to 5.3% in 18 months.
5. **Rupee and battery costs** (-1.0 and -0.5): hedged debt but imported cells.
6. **Merchant exposure** (power price +0.7, demand +1.2) is small.
The pack's strongest empirical co-movements are negative loadings on gold (t -3.3) and silver (t -2.7). They have no fundamental link and are carried as a low-confidence proxy for risk-on / real-yield sensitivity.

## Worked transmission examples
- **Hormuz disruption -> LNG shortage and Brent up (1st) -> Indian inflation and yields up, RBI turns hawkish (2nd) -> corporate spreads and the 10-year G-sec rise (3rd) -> AGEL's valuation falls because 80% of its value is terminal and its net debt/EBITDA is 5.6x (4th).** At the same time, energy-security policy strengthens the demand for domestic RE plus storage (opposite sign, smaller).
- **Slow grid build at Khavda (ROW delays at Power Grid/AESL) -> solar curtailment during peak hours (1st) -> lower billed units; take-or-pay protects PPAs with counterparties but not units curtailed by the grid on non-PPA capacity (2nd) -> EBITDA short by Rs 700 cr per half (3rd) -> 5.6x leverage persists longer and rating upgrades are delayed (4th).** Accelerated BESS is the mitigation.
- **Weak monsoon (-13% in Q2) -> record demand (270 GW) and thermal dispatch (1st) -> spot power prices rise and coal stocks run critical (2nd) -> states tender more firm/storage-backed power, which AGEL's 6.6 GWh BESS and hybrid portfolio can bid for (3rd) -> better pricing in FDRE/C&I tenders, higher ROE (13-14% target) (4th).**
- **Lower battery-cell prices (F_BATTERY_MATERIALS down) -> cheaper BESS capex (1st) -> competitive tariffs in storage tenders (2nd) -> higher win rates but lower tariff per MWh (3rd) -> faster rollout but unchanged IRR (4th).**

## Current situation
H1 FY27 energy sold was 25.7 bn units (+32%); cash profit was Rs 4,176 cr (+35%). Net debt rose Rs 11.7k cr in the half. Jefferies (12 and 23 Oct) rates it a Buy with about 35% upside, and the stock fell 4% on results day, then recovered; it is 13% below its 52-week high of Rs 1,632. The call confirmed the ROE framework of 13-14% and a preference for AA+ counterparties.

## Upcoming events
Phase-3 Khavda evacuation (Q4 FY27), the 4.5-5 GW FY27 commissioning outcome, 500 MW Chitravathi pumped storage and >10 GWh BESS by year-end, conversion of 974 MW of merchant capacity to fixed PPAs, Q3 FY27 results (late Jan 2027, estimated), and the tail risk of renewed US legal action. Probabilities are in `company_events`.

## Bull and bear
**Bull:** curtailment ends in H2, commissioning reaches 4.5-5 GW, upgrades cut funding cost to below 8.5%, hyperscaler/C&I contracts lift tariffs. **Bear:** evacuation slips again, yields rise further, group legal risk returns, and a 119x P/E offers little cushion if growth in operating EBITDA disappoints.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.