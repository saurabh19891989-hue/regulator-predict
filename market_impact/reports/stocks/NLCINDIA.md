# NLCINDIA — NLC India Ltd.
*MIDCAP_100 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +2.9%**, **12 months +6.3%** (rank 33 / 30 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.7%): 3 months 58%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +2.7% … P90 +9.2%; plausible 12m relative-return range incl. stock-specific noise: -37.6% … +25.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.2 pp (model impact +8.5% beta-adjusted vs realised market-adjusted move -33.7%); forward event exposure +4.4% (3m +2.5%; half assumed priced); company-specific events +2.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +3.48 | +3.00 | +0.50 | -0.02 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.18 | +0.00 | -1.34 | -0.83 | -0.01 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.96 | +2.00 | -0.04 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.90 | +2.00 | -0.10 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.35 | +1.20 | +0.09 | +0.01 | +0.05 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.29 | +1.00 | +0.26 | +0.03 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.20 | +0.00 | +0.00 | -0.74 | -0.46 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.06 | -0.80 | -0.30 | +0.04 | +0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.00 | -0.30 | -0.26 | -0.29 | -0.15 | -1.1% |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.95 | +0.00 | +0.00 | -0.37 | -0.57 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.91 | +0.00 | -0.48 | -0.32 | -0.10 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -0.91 | +0.00 | -0.60 | -0.19 | -0.12 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.7% | -4.7% | +0.0 | -1.2 | -2.0 | -1.5 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +4.0% | +4.0% | +4.0 | -0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.0% | -3.0% | -2.6 | -0.2 | -0.0 | -0.1 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -1.5 | -1.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.7% | +1.7% | +1.5 | +0.2 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.4% | +1.7% | +3.0 | +0.2 | +0.0 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.5 | -0.2 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.4 | -0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.2% | -1.2% | -1.2 | +0.0 | +0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.4% | -1.2% | +0.0 | -1.1 | -1.3 | -1.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NLCINDIA | +3.00% | +1.50% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → NLCINDIA | +2.00% | +0.90% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → NLCINDIA | +1.50% | +0.60% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → NLCINDIA | +1.50% | +0.60% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → NLCINDIA | -1.20% | -0.60% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → NLCINDIA | +1.00% | +0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NLCINDIA | -1.79% | -0.50% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → NLCINDIA | -0.75% | -0.45% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NLCINDIA | -2.24% | -0.40% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → NLCINDIA | -1.80% | -0.40% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → NLCINDIA | -0.57% | -0.39% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → NLCINDIA | +0.60% | +0.36% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → NLCINDIA | -0.36% | -0.34% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → NLCINDIA | -1.50% | -0.33% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → NLCINDIA | -1.15% | -0.32% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_RENEWABLE_SUPPORT → NLCINDIA | +1.50 | events | +4.50% |
| 1 | F_GSEC_10Y_IN → NLCINDIA | +1.70 | events | -2.55% |
| 1 | F_FPI_FLOWS → NLCINDIA | -1.60 | events | -1.92% |
| 1 | F_POWER_PRICE_IN → NLCINDIA | +3.00 | events | +1.50% |
| 1 | F_POWER_DEMAND_IN → NLCINDIA | +1.20 | events | +1.20% |
| 1 | T_ENERGY_TRANSITION → NLCINDIA | +0.50 | events | +1.00% |
| 1 | F_REPO_IN → NLCINDIA | +1.00 | events | -0.80% |
| 1 | F_COAL_INDIA → NLCINDIA | +1.50 | events | +0.45% |
| 1 | F_USDINR → NLCINDIA | -0.37 | observed | +0.11% |

## Analyst profile (agent research, sourced)
# NLCINDIA — NLC India Ltd. (as of 2026-11-05)

*Scenario/exposure analysis relative to the Nifty 200; not a validated forecast. Sources in `NLCINDIA.json` (Q1 FY27 results filing, screener.in, 4 Nov 2026 headlines). Segment shares in the JSON are rough estimates; the Q1 filing text was OCR-degraded, so regulatory figures should be rechecked.*

## Business
NLC India mines lignite at Neyveli and Barsingsar and coal at Talabira II & III in Odisha, and converts it into power at Neyveli (TPS-I, II, Expansion), Barsingsar and Ghatampur (3x660 MW, fully commissioned in 2026). It also holds renewables through NLC India Renewables (NIRL), which the board has now cleared for an IPO with an offer for sale of up to 10 crore shares. Tariffs are set by CERC on a cost-plus basis, but several 2024-29 final orders are still pending, so billing is on interim terms (Ghatampur at 90% of claimed tariff, Neyveli mines on an interim lignite price). Q2 FY27 sales were Rs 2,691 cr (+5%) and operating profit Rs 686 cr (OPM 25%); net profit was reported at Rs 1,205-1,381 cr, well above the operating trend, suggesting non-operating or regulatory items. The government holds 69.5% (down from 72.2%). Mcap Rs 33.5k cr, P/E 10.3, dividend yield 1.5%.

## What moves the stock
1. **Regulatory settlements (P_POWER_REFORM +2.0)**: CERC final tariff orders, disputed Rs 386 cr billing, and a regulatory deferral liability of Rs 414 cr.
2. **Renewable pivot and NIRL IPO (P_RENEWABLE_SUPPORT +3.0, energy transition +2.0)**: 10 GW target by 2030, Rs 37,000 cr Odisha plan, 660 MW expansion and Rs 2,500 cr bond plan.
3. **Yields and funding (G-sec -1.5, repo -0.8)**: debt/equity above 1.2 and Rs 11k cr CWIP.
4. **Power demand and merchant prices (+1.0, +0.5)** matter only through availability incentives and Ghatampur's unscheduled sales.
5. **Mining economics (coal +0.3, royalty -1.0)**.
6. **Flows (FPI +1.2)**, with government stake sales a recurring overhang.
Pack: imported-coal loading -3.95 (t -1.8) and steel/aluminium +2.2 to +2.3 (t about 2) are not fundamental for a lignite generator and are not carried.

## Worked transmission examples
- **Middle East conflict -> seaborne coal and LNG tight (1st) -> exchange prices and power-demand pressure rise as plants run harder (2nd) -> NLC's cheap captive lignite/coal gives high dispatch merit (3rd) -> better PAF incentive and merchant sales, partly offset by higher yields compressing the multiple (4th).**
- **Weak monsoon -> demand +11% (1st) -> thermal coal stocks critical, government pushes captive output (2nd) -> NLC's Talabira coal is valuable and diverted to power (3rd) -> mining profit (Rs 289 cr PAT in Q1 for Talabira alone) rises (4th).**
- **RBI hike (7 Oct) -> MCLR up (1st) -> interest on Rs 28k cr borrowings up, recoverable only after CERC final orders (2nd) -> working-capital strain from delayed tariffs and discom receivables (3rd) -> larger bond issuance and further dependence on NIRL IPO proceeds (4th).**

## Current situation
The stock fell 21% in three months, then gained 8-9% on 4 Nov on Q2 numbers, the Rs 1.50 interim dividend and NIRL's IPO plan. Q2 earnings quality is uncertain. The CMD targets a 50:50 conventional/renewable mix by 2032.

## Upcoming events
NIRL IPO/OFS, CERC final tariff orders, interim dividend payment, bond issue, Q3 results (early Feb 2027, estimated), and possible further government OFS. See `company_events`.

## Bull and bear
**Bull:** NIRL IPO at a premium, final tariff orders release deferred income, renewables ramp lifts ROE from 7.6%. **Bear:** regulatory delay, one-off-driven Q2 profit does not repeat, OFS overhang, higher yields.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.