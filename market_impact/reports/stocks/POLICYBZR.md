# POLICYBZR — PB Fintech Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.7%**, **12 months -6.5%** (rank 179 / 173 of 200 for 3m / 12m); beta 1.12
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +51.0%): 3 months 44%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -13.5% … P90 +1.8%; plausible 12m relative-return range incl. stock-specific noise: -59.8% … +62.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -6.7% beta-adjusted vs realised market-adjusted move -47.0%); forward event exposure -6.3% (3m -1.6%; half assumed priced); company-specific events -4.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -14.24 | -14.00 | -0.24 | +0.00 | +0.00 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +3.98 | +4.00 | +0.00 | +0.00 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.92 | +4.00 | -0.07 | -0.01 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.53 | -2.50 | -0.70 | -0.37 | +0.03 | +3.5% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.11 | +0.00 | +2.48 | +0.55 | +0.09 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.60 | +0.00 | -1.00 | -0.96 | -0.64 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -2.46 | -2.00 | +0.00 | -0.34 | -0.12 | +11.2% |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.46 | +0.00 | +1.96 | +0.26 | +0.24 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.46 | +2.00 | +0.50 | -0.04 | +0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.84 | +0.00 | +1.28 | +0.60 | -0.03 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.82 | +0.00 | +1.28 | +0.61 | -0.07 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.76 | +0.00 | -0.20 | -0.89 | -0.67 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.72 | +0.00 | -1.57 | -0.17 | +0.02 | +2.2% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.61 | +0.00 | -1.04 | -0.45 | -0.12 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -9.6% | -9.6% | -9.8 | +0.2 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.1% | -6.1% | +1.2 | -4.2 | -2.7 | -0.5 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.8% | +5.4% | +11.0 | -0.2 | -0.0 | -0.0 |
| IRDAI resets insurance commission/expense rules; post-GST-exemption demand (`EV_IRDAI_COMMISSION_RESET`) | anticipated | 0.50 | -10.0% | -5.0% | -9.8 | -0.2 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -15.7% | -4.4% | -10.0 | -6.2 | +0.3 | +0.2 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -20.2% | -3.6% | -12.5 | -8.3 | +0.5 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -3.4% | -3.4% | -2.0 | -1.3 | -0.1 | -0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.2% | +2.2% | -1.0 | +0.9 | +1.8 | +0.5 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -2.5 | +0.3 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.8% | -2.1% | -3.0 | -1.4 | -1.4 | -0.0 |
| Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027 (`EV_FED_H1_2027_FURTHER_HIKES`) | anticipated | 0.30 | -6.6% | -2.0% | -4.0 | -2.1 | -0.3 | -0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -2.2 | +0.2 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → POLICYBZR | -8.80% | -8.80% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POLICYBZR | +10.00% | +5.00% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → POLICYBZR | -9.80% | -4.90% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → POLICYBZR | -10.00% | -2.80% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → POLICYBZR | -2.38% | -2.38% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → POLICYBZR | -12.50% | -2.25% |
| 1 | EV_FED_SEP26_HIKE ⇒ F_FED_FUNDS → POLICYBZR | -2.00% | -2.00% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → POLICYBZR | +2.00% | +2.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → POLICYBZR | -1.88% | -1.88% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_GLOBAL → POLICYBZR | -1.65% | -1.65% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → POLICYBZR | +6.00% | +1.50% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → POLICYBZR | -1.36% | -1.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → POLICYBZR | -6.00% | -1.32% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_FPI_FLOWS → POLICYBZR | -1.28% | -1.28% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → POLICYBZR | +1.25% | +1.25% |

## Analyst profile (agent research, sourced)
# POLICYBZR - PB Fintech (Policybazaar) (as of 2026-11-05)

## Business
PB Fintech runs Policybazaar (insurance marketplace), Paisabazaar (loans) and newer lines. Roughly 85% of revenue is commission and marketing fees from insurers on premium sold, so it is directly exposed to how much insurers may pay distributors. Search summaries put Q2 FY27 revenue near Rs2,178cr (+35%), PAT near Rs192cr (+43%) and premium Rs9,385cr (+38%); sources differ and I could not verify them against the exchange filing. The screener extract is parent-only (Sep-26 sales Rs5cr) and is not meaningful.

## What moves the stock (ranked)
1. **IRDAI draft rules (-14, range -30 to +2).** The 2026-09-23/24 proposals (commission caps, EoM limits, dark-pattern ban) triggered a 36% one-day crash, 43% over four sessions and an estimated Rs31,000cr value loss (Fortune India, Moneycontrol). Brokerages see ~46% earnings risk; Nomura cut its target to Rs1,100, Bernstein kept Rs2,310.
2. **Global/Indian risk appetite: FPI flows (+4.0), VIX (-2.5), Fed funds (-2.0)** - beta 1.1-1.4, 58% volatility.
3. **Structural growth: financialisation (+4.0), GDP (+2.0).**
4. **AI disintermediation (-1.0), CPI (-0.8).**
Pack empirics: refining margin +2.34 (t 2.8), Brent +1.94 (t 2.1), steel -2.82 (t -2.0) have no business mechanism and are shrunk to near zero.

## Transmission examples
- **IRDAI finalises caps -> insurers' distributor payouts fall -> PB take rate down and insurers renegotiate -> revenue -15 to -25% while ad and staff costs are fixed -> EBITDA -45% -> multiple compresses; 4th order: lower profit funds fewer ad spends, slowing premium growth.**
- **Rates up (repo hiked 2026-10-07) -> FD rates up -> savings-plan demand shifts -> insurers' life APE slows -> PB's life revenue slips; separately higher discount rates hit a P/E-100 growth stock (Fed funds -2.0).**
- **Brent up -> CPI -> RBI tightening -> health/motor premium growth slows (affordability) -> PB premium growth falls below 35%.**
- **Equity sell-off -> FPI outflow -> high-beta internet names fall with beta 1.4.**

## Current situation
Stock Rs971 (-39% in 3m, 52-week low on 2026-11-02, below IPO price as of 2026-10-01). Brokers disagree strongly. IRDAI's chair said the norms are not intended to disrupt business models (Livemint, 2026-10-15); ET reported caps may roll out from January (2026-10-09).

## Upcoming events
IRDAI final rules (prob 0.5 by Dec; -25% to +15%), Q3 results (Feb 2027), contract resets with insurers.

## Bull and bear
**Bull:** 35%+ growth, profitable, dilution of draft likely, price below IPO.
**Bear:** take-rate reset, ad-spend inflation, regulatory path-dependency, disintermediation.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.