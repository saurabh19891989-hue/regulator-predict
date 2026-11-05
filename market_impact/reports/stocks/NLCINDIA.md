# NLCINDIA — NLC India Ltd.
*MIDCAP_100 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +2.2%** (rank 89 / 26 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.7%): 3 months 51%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.3% … P90 +4.1%; plausible 12m relative-return range incl. stock-specific noise: -45.9% … +35.2%
- Decomposition (12m): 0.5 × forward event exposure +3.3% (3m +1.4%; half assumed priced) + 0.5 × company-specific catalysts +2.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +5.1% (beta-adjusted) vs a realised market-adjusted move of -33.7% — gap +38.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +3.48 | +3.00 | +0.50 | -0.02 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.96 | +2.00 | -0.04 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.90 | +2.00 | -0.10 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.33 | +1.20 | +0.09 | +0.01 | +0.03 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.28 | +1.00 | +0.26 | +0.02 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.17 | +0.00 | -0.88 | -0.29 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.06 | -0.80 | -0.30 | +0.04 | +0.01 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.85 | -0.30 | -0.26 | -0.18 | -0.12 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.75 | +0.00 | -0.48 | -0.24 | -0.02 | +3.5% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -0.69 | +0.00 | -0.72 | -0.12 | +0.16 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.66 | +0.00 | -0.60 | -0.05 | -0.01 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.65 | +0.00 | -0.63 | -0.06 | +0.04 | +9.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +4.0% | +4.0% | +4.0 | -0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.9% | -2.9% | -2.6 | -0.2 | -0.0 | -0.1 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | -0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.7% | +1.7% | +1.5 | +0.2 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.3% | +1.7% | +3.0 | +0.2 | +0.0 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.0 | -0.3 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.2% | -1.2% | -1.2 | +0.0 | +0.0 | -0.0 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +3.0% | +1.2% | +3.0 | +0.1 | +0.0 | -0.1 |
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | +0.9% | +0.9% | +0.9 | +0.0 | +0.0 | +0.0 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +1.5% | +0.9% | +1.6 | -0.1 | +0.0 | +0.0 |
| Electricity (Amendment) Bill / distribution parallel licensing and DISCOM privatisation steps (`EV_POWER_DISTRIB_REFORM`) | anticipated | 0.45 | +1.9% | +0.9% | +2.0 | -0.1 | +0.0 | +0.0 |

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
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → NLCINDIA | -0.75% | -0.45% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → NLCINDIA | -0.57% | -0.39% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → NLCINDIA | +0.60% | +0.36% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → NLCINDIA | -0.80% | -0.34% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → NLCINDIA | -1.80% | -0.32% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → NLCINDIA | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → NLCINDIA | -1.15% | -0.29% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NLCINDIA | -1.12% | -0.28% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → NLCINDIA | -0.30% | -0.27% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → NLCINDIA | +1.55 | director_override | -2.33% |
| 1 | F_FPI_FLOWS → NLCINDIA | -1.60 | events | -1.92% |
| 1 | P_RENEWABLE_SUPPORT → NLCINDIA | +0.60 | director_override | +1.80% |
| 1 | F_POWER_DEMAND_IN → NLCINDIA | +1.20 | events | +1.20% |
| 1 | F_POWER_PRICE_IN → NLCINDIA | +1.90 | director_override | +0.95% |
| 1 | F_REPO_IN → NLCINDIA | +1.00 | events | -0.80% |
| 1 | T_ENERGY_TRANSITION → NLCINDIA | +0.30 | director_override | +0.60% |
| 1 | F_COAL_INDIA → NLCINDIA | +1.50 | events | +0.45% |
| 1 | F_USDINR → NLCINDIA | -0.37 | observed | +0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Ex-date/payment of Rs 1.50 interim dividend (record date per exchange filing, not verified) | corporate_action | 0.95 | -0.3% | -0.33% |
| 2027-02 | Q3 FY27 results (Q2 declared 4 Nov after reschedule; estimate early Feb 2027) | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | NIRL IPO/OFS listing (FY27 per company; up to 10 crore shares by NLC) | corporate_action | 0.60 | +3.5% | +2.10% |
| 2027-03 | CERC final tariff orders for 2024-29 / Ghatampur final tariff (replacing 90% interim billing) | regulatory | 0.40 | +2.2% | +0.90% |
| 2027-03 | Rs 2,500 cr bond issue and Rs 37,000 cr Odisha power & minerals investment announcements progress | capex | 0.70 | +0.5% | +0.35% |
| 2027-03 | Further government OFS in NLC India (promoter 72.2% -> 69.5% in Q1 FY27) | corporate_action | 0.20 | -4.5% | -0.90% |

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