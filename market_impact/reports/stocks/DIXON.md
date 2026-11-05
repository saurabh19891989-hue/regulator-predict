# DIXON — Dixon Technologies (India) Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.3%**, **12 months +2.1%** (rank 55 / 67 of 200 for 3m / 12m); beta 1.30
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.5%): 3 months 53%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.2% … P90 +5.7%; plausible 12m relative-return range incl. stock-specific noise: -33.3% … +32.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.4 pp (model impact +6.2% beta-adjusted vs realised market-adjusted move +3.4%); forward event exposure +2.4% (3m +3.3%; half assumed priced); company-specific events +1.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Production-linked incentive schemes (`P_PLI`) | +1 = expansion/disbursement | +4.65 | +4.00 | +0.64 | +0.01 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -4.50 | -4.50 | +0.00 | +0.00 | +0.00 | — |
| FDI liberalisation (`P_FDI_RULES`) | +1 = liberalisation | +4.42 | +4.00 | +0.42 | +0.00 | +0.00 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +4.02 | +4.00 | +0.02 | +0.00 | +0.00 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | +2.47 | +2.50 | -0.02 | +0.00 | -0.01 | -1.4% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.45 | +2.50 | +0.00 | +0.00 | -0.05 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.42 | +2.00 | +0.36 | +0.06 | +0.00 | +1.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.00 | -1.50 | -0.47 | -0.01 | -0.02 | +3.5% |
| US growth (`F_US_GDP`) | +1 pp | +1.86 | +0.00 | +1.80 | +0.20 | -0.14 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +1.72 | +1.50 | +0.48 | -0.27 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.47 | +0.00 | -0.79 | -0.54 | -0.14 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.21 | -1.20 | +0.00 | +0.00 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.18 | +0.00 | -0.48 | -0.46 | -0.24 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -1.13 | +0.00 | -1.03 | -0.04 | -0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -1.5 | -1.1 | -1.3 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +3.6% | +2.9% | +3.6 | +0.0 | +0.0 | +0.0 |
| India further eases Press Note 3 rules for China/border-country FDI (approval timelines, minority stakes) (`EV_CHINA_FDI_EASING_PN3`) | anticipated | 0.70 | +3.6% | +2.5% | +3.6 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -8.8% | -2.5% | -12.0 | +3.1 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.4% | +2.4% | +0.0 | +2.0 | +0.3 | +0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -11.1% | -2.0% | -10.5 | -0.1 | -0.4 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -7.8% | -1.9% | -6.0 | -2.2 | +0.9 | -0.5 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -0.9 | -0.6 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.9% | -1.4% | -1.8 | -1.0 | -0.4 | -0.8 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.4% | -1.4% | -0.6 | -0.6 | +0.0 | -0.2 |
| India-China thaw: Xi visit around BRICS summit in India (mid-Sep 2026), flights resume, Chinese-investment curbs eased (`EV_INDIA_CHINA_THAW_SEP26`) | occurred | 1.00 | +1.2% | +1.2% | +1.0 | +0.1 | +0.0 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ P_FDI_RULES → DIXON | +2.80% | +1.96% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → DIXON | +2.40% | +1.92% |
| 2 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_US_EQUITIES → DIXON | +1.73% | +1.73% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → DIXON | -6.00% | -1.68% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → DIXON | -6.00% | -1.68% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → DIXON | -1.68% | -1.68% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → DIXON | -6.00% | -1.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → DIXON | -7.50% | -1.35% |
| 1 | EV_INDIA_CHINA_THAW_SEP26 ⇒ P_FDI_RULES → DIXON | +1.20% | +1.20% |
| 1 | EV_CHINA_Q3_GDP_AND_MINI_STIMULUS ⇒ F_USDCNY → DIXON | -1.12% | -1.12% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ P_PLI → DIXON | +1.20% | +0.96% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → DIXON | +3.24% | +0.91% |
| 1 | EV_ECOM_FDI_EXPORT_INVENTORY ⇒ P_FDI_RULES → DIXON | +0.80% | +0.80% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → DIXON | -0.78% | -0.78% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ T_CHINA_PLUS_ONE → DIXON | +1.20% | +0.78% |

## Analyst profile (agent research, sourced)
# DIXON - Dixon Technologies (India) Ltd. (midcap, EMS)

## Business
India's largest listed EMS company: about three-quarters of revenue is smartphone contract manufacturing, plus TVs, appliances, lighting, security and IT hardware, with a push into camera and display modules through JVs with Chinese technology partners (Vivo India 51%, HKC, Longcheer, Chongqing Yuhai, Q Tech). EBITDA margin was 2.7% in Q2 FY27 on Rs21,794cr revenue; reported profit also includes sizeable other income. The equity trades at 49x earnings.

## What moves the stock (ranked)
1. **Semiconductor/memory pricing (-4.5 per +1 tightening)**: raised revenue (price pass-through) while compressing margin and cutting market volumes (-16% YoY).
2. **Industrial policy: PLI/ECMS (+4.0), FDI/Press Note 3 relaxations (+4.0), China+1 (+4.0)**: the stock is a policy and sourcing-shift vehicle.
3. **Demand (+2.5 per +5pp), risk sentiment (-1.5 per +5 VIX), US equities (+2.0), G-sec (-1.2).**
4. **FX**: USD/CNY (+2.5 per +3%) with pack t=2.4; USD/INR (-0.5), weakly identified.

## Transmission examples
- **AI server and phone demand pull on DRAM/NAND -> memory price spike (1st) -> phone BOM up and brand price hikes (2nd) -> market units -16% but Dixon share up (3rd) -> pass-through lag compresses margin to 2.7% and working capital rises (4th).**
- **US-China tariff escalation -> brand customers shift assembly to India (T_CHINA_PLUS_ONE) -> more orders for Dixon, but Press Note 3 limits Chinese JV partners' access -> approvals become the gating factor for upside.**
- **Mobile PLI sunsets -> margin down ~110bp (already visible) -> only recouped by backward integration (displays, cameras) or ECMS approvals; a policy announcement can reprice the stock by 5-8%.**
- **Brent up -> INR weaker and freight dearer -> imported-component and logistics cost up; cost-plus contracts defend margin but working-capital financing costlier.**

## Current situation
Q2 FY27 revenue +47% and profit down 45% (prior-year base inflated by other income); shares jumped 8-13% on 2 Nov as brokerages cited the Vivo JV (start now Q4 FY27) and smartphone share gains, after falling 29% from the high by 23 Sep. FY27 phone volumes ex-Vivo guided at about 32-33m. Promoter holding 28.5% (-5.3pp in 3 yrs).

## Upcoming
Q3 FY27 results (Jan 2027), Vivo JV commencement (Q4 FY27), ECMS/scheme approvals, memory-price trend.

## Bull / bear
Bull: JV and component ramp, margin to 3-4%, policy support, China+1 wins. Bear: memory inflation, no PLI, Chinese JV approval or geopolitical shock, margin stuck below 3%, and valuation compression.

Uncertainties: segment split is approximate; JV approval status not verified; reported profits include large other income; empirical USD/CNY and US equity betas have weak mechanisms.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.