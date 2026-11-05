# ONGC — Oil & Natural Gas Corporation Ltd.
*NIFTY_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.4%** (rank 141 / 123 of 200 for 3m / 12m); beta 0.83
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.7%): 3 months 49%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.5% … P90 +12.5%; plausible 12m relative-return range incl. stock-specific noise: -33.8% … +34.2%
- Decomposition (12m): 0.5 × forward event exposure +0.1% (3m +0.3%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +7.5% (beta-adjusted) vs a realised market-adjusted move of -17.0% — gap +24.5 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +6.97 | +3.50 | +2.73 | +0.64 | +0.11 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +3.97 | +3.50 | +0.44 | +0.05 | -0.02 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.93 | +3.00 | -0.03 | -0.04 | +0.00 | -1.1% |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | -2.57 | +0.00 | -2.24 | -0.27 | -0.06 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | +2.27 | +0.00 | +2.09 | +0.18 | +0.00 | — |
| Windfall (SAED) tax on domestic crude (`NEW_CRUDE_WINDFALL_TAX_IN`) | +1 = SAED reimposed at ~Rs10,000/tonne | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.44 | +0.00 | +1.24 | +0.18 | +0.02 | — |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +1.20 | +1.20 | +0.00 | +0.00 | +0.00 | +15.4% |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | +1.02 | +1.00 | -0.05 | +0.03 | +0.03 | — |
| Government compensation to OMCs for fuel/LPG under-recoveries (`NEW_OMC_COMPENSATION`) | +1 = Rs25,000 cr compensation to oil marketing companies | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.76 | -0.60 | -0.12 | -0.04 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +0.72 | +0.00 | +0.86 | -0.03 | -0.12 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.70 | +0.00 | +0.48 | +0.20 | +0.02 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | +0.64 | +0.00 | +0.36 | +0.22 | +0.05 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -9.8% | -5.4% | -8.8 | -0.8 | -0.2 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +4.5% | +4.5% | +4.2 | +0.2 | +0.1 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | +14.6% | +3.6% | +12.4 | +1.7 | +0.4 | +0.1 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.05 | +31.1% | +1.6% | +26.0 | +3.8 | +1.1 | +0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.2% | +1.2% | +0.0 | +1.2 | -0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +0.9% | +0.9% | +0.0 | +1.0 | +0.0 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.6 | -0.1 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | -1.5% | -0.8% | +0.0 | -1.5 | +0.0 | +0.0 |
| Cabinet approves further LPG under-recovery compensation to OMCs (`EV_LPG_COMPENSATION_CABINET`) | anticipated | 0.55 | -1.2% | -0.7% | -1.2 | +0.0 | +0.0 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | +3.3% | +0.6% | +3.3 | +0.0 | -0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.6% | +0.6% | +1.0 | -0.2 | -0.2 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ONGC | -4.55% | -2.50% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → ONGC | -3.50% | -1.93% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ONGC | +7.70% | +1.93% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → ONGC | +4.20% | +1.05% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → ONGC | +15.75% | +0.79% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → ONGC | +3.90% | +0.70% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → ONGC | -1.38% | -0.69% |
| 1 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_COMPENSATION → ONGC | -1.20% | -0.66% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_BRENT → ONGC | -2.52% | -0.63% |
| 1 | EV_OPEC_NOV29_RAISE ⇒ F_BRENT → ONGC | -2.45% | -0.49% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ C_MIDEAST_CONFLICT → ONGC | +8.75% | +0.44% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ F_BRENT → ONGC | +2.80% | +0.42% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → ONGC | -0.72% | -0.40% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_BRENT → ONGC | +1.12% | +0.39% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → ONGC | -1.00% | -0.30% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | C_MIDEAST_CONFLICT → ONGC | +1.00 | events | +3.50% |
| 1 | F_USDINR → ONGC | -0.37 | observed | -1.11% |
| 1 | C_RUSSIA → ONGC | +1.00 | events | +1.00% |
| 1 | F_REFINING_MARGIN → ONGC | +0.60 | events | +0.72% |
| 1 | F_REPO_IN → ONGC | +1.00 | events | -0.60% |
| 1 | F_GAS_GLOBAL → ONGC | +1.00 | director_override | +0.50% |
| 1 | F_GDP_IN → ONGC | +0.50 | events | +0.15% |
| 1 | F_BRENT → ONGC | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (pending as of 5 Nov; previews expect profit ~Rs 15.5-16.4k cr, down ~14% y/y on lower realisations/ HPCL; exact date not verified) | results | 0.95 | -0.5% | -0.47% |
| 2026-11-12 | Interim dividend record date (PSU Connect; amount per share not verified) | corporate_action | 0.90 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Subsidy-sharing / windfall-tax decision in OMC compensation package | regulatory | 0.15 | -4.0% | -0.60% |
| 2027-06 | KG-98/2 deepwater gas ramp-up and Mahanadi deepwater gas discovery (21 Sep 2026) appraisal | capex | 0.50 | +1.5% | +0.75% |

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