# ONGC — Oil & Natural Gas Corporation Ltd.
*NIFTY_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.0%**, **12 months +7.3%** (rank 21 / 24 of 200 for 3m / 12m); beta 0.83
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.7%): 3 months 63%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.7% … P90 +25.9%; plausible 12m relative-return range incl. stock-specific noise: -23.5% … +31.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.9 pp (model impact +9.8% beta-adjusted vs realised market-adjusted move -17.0%); forward event exposure +7.3% (3m +4.2%; half assumed priced); company-specific events -0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +7.14 | +3.50 | +2.73 | +0.82 | +0.09 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +4.11 | +3.50 | +0.61 | +0.03 | -0.03 | +0.0% |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | -3.04 | +0.00 | -2.24 | -0.73 | -0.07 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.89 | +3.00 | -0.03 | -0.08 | -0.01 | -1.1% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | +2.89 | +0.00 | +2.09 | +0.70 | +0.09 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.67 | +0.00 | +1.24 | +0.41 | +0.02 | — |
| Windfall (SAED) tax on domestic crude (`NEW_CRUDE_WINDFALL_TAX_IN`) | +1 = SAED reimposed at ~Rs10,000/tonne | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +1.20 | +1.20 | +0.00 | +0.00 | +0.00 | +15.4% |
| Government compensation to OMCs for fuel/LPG under-recoveries (`NEW_OMC_COMPENSATION`) | +1 = Rs25,000 cr compensation to oil marketing companies | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.97 | +0.00 | +0.70 | +0.28 | -0.02 | +2.2% |
| US growth (`F_US_GDP`) | +1 pp | +0.78 | +0.00 | +0.86 | +0.12 | -0.21 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.76 | -0.60 | -0.12 | -0.04 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | +0.64 | +0.00 | +0.36 | +0.24 | +0.04 | +3.5% |
| Windfall / export taxes on commodities (`P_WINDFALL_EXPORT_TAX`) | +1 = imposition | -0.57 | +0.00 | -0.58 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +27.5% | +27.5% | +24.4 | +2.9 | +0.2 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -11.0% | -6.4% | -9.7 | -1.2 | -0.2 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +16.2% | +5.8% | +13.4 | +2.3 | +0.5 | +0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.06 | +37.8% | +2.4% | +31.2 | +5.4 | +1.1 | +0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.3% | +1.3% | +0.0 | +1.4 | -0.0 | -0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.0% | +1.0% | +0.0 | +1.0 | +0.2 | -0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.5 | +0.4 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.5 | +0.4 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.6 | -0.1 | -0.0 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | +3.3% | +0.7% | +3.3 | +0.0 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | -1.4% | -0.7% | +0.0 | -1.5 | +0.0 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → ONGC | +17.32% | +17.32% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → ONGC | +5.25% | +5.25% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ONGC | +8.75% | +3.12% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ONGC | -5.25% | -3.05% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → ONGC | +2.35% | +2.35% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → ONGC | -3.50% | -2.03% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_REFINING_MARGIN → ONGC | +1.80% | +1.80% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → ONGC | +4.20% | +1.50% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → ONGC | +21.00% | +1.31% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → ONGC | +1.21% | +1.21% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → ONGC | -1.11% | -1.11% |
| 2 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_BRENT → ONGC | +1.01% | +1.01% |
| 1 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → ONGC | +1.00% | +1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → ONGC | +3.90% | +0.86% |
| 2 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → F_BRENT → ONGC | -0.84% | -0.84% |

## Analyst profile (agent research, sourced)
# ONGC — market impact profile (as of 2026-11-05)

## Business
ONGC is India's biggest upstream producer and, through HPCL and MRPL, also a downstream owner. Standalone, it is a Brent-linked royalty-paying explorer: roughly +10% Brent adds ~15% to standalone EBITDA. Consolidated, HPCL (54.9%) offsets part of the gain when crude spikes with retail prices frozen. That is why the stock has fallen 19% in six months at $95-110 crude.

## What moves the stock (ranked)
1. **Brent (+3.5)** and **Mid-East conflict (+3.5)**.
2. **USD/INR (+3.0).**
3. **Subsidy sharing / windfall tax (NEW_CRUDE_WINDFALL_TAX_IN -1.5, NEW_OMC_COMPENSATION -1.0)** — the policy overhang.
4. **HPCL via holding link (0.12 per 1%)**.
5. **Russia asset access (+1.0)** and **MRPL refining margins (+1.2)**.

## Worked transmission examples
- Escalation -> Brent +12% -> ONGC realisation up (standalone EBITDA +Rs 7k cr/yr) -> OMC under-recoveries widen (HPCL -> consolidated drag, HPCL booked a Rs 12.3k cr loss in Q1, ~15% of its market cap) -> government debates windfall tax/sharing (third-order) -> ONGC's net gain shrinks; the stock lags crude.
- Brent -9% (4 Nov) -> ONGC realisation down but HPCL margin up -> consolidated EBITDA less volatile; the share has risen 2.4% in a month.
- INR depreciation -> USD realisation upside; at the same time OVL/HPCL USD debt is marked-to-market.
- Gas: APM price formula capped, so higher spot LNG yields little for ONGC while GAIL/ATGL lose.

## Current situation
Q2 FY27 not yet reported; previews expect ~14% lower profit y/y. Interim dividend record date 12 Nov. Stock is near yearly lows (Oct), P/E 6.6x, P/B 0.8x, yield 5.8%. The Mahanadi deepwater gas discovery (21 Sep) is positive but not yet reserve-booked.

## Upcoming events
Q2 results (Nov), dividend, Q3 (Feb), policy package for OMCs.

## Bull / bear
Bull: Brent stable ~$90, no tax, HPCL recovers, production growth. Bear: windfall tax/sharing, Brent <$80, HPCL losses, production slip.

*Weights are exposure estimates, not return forecasts. Latest quarter not in dossier; refresh after Q2.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.