# LUPIN — Lupin Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.4%**, **12 months +2.6%** (rank 52 / 58 of 200 for 3m / 12m); beta 0.72
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.6%): 3 months 57%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.5% … P90 +8.3%; plausible 12m relative-return range incl. stock-specific noise: -17.0% … +28.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -3.1% beta-adjusted vs realised market-adjusted move -16.1%); forward event exposure +4.2% (3m +2.1%; half assumed priced); company-specific events +3.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.76 | +3.00 | -0.17 | -0.08 | +0.00 | -1.1% |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -2.00 | -3.00 | +1.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.14 | +1.20 | +0.00 | -0.00 | -0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +0.71 | +0.00 | +0.85 | -0.05 | -0.09 | +0.0% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.71 | -0.50 | -0.17 | -0.04 | +0.00 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | +0.70 | +0.70 | +0.00 | +0.00 | +0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.58 | +0.00 | +0.35 | +0.26 | -0.03 | +2.2% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.56 | +0.00 | -0.17 | -0.31 | -0.08 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.54 | +0.80 | -0.28 | +0.01 | +0.01 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | -0.51 | +0.00 | +0.00 | -0.51 | +0.00 | — |
| Foreign portfolio flows into Indian government/corporate bonds (FAR, index-linked) (`NEW_FPI_DEBT_FLOWS`) | +US$5 bn net debt inflow per quarter | -0.51 | +0.00 | -0.60 | +0.06 | +0.03 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.47 | +0.00 | +0.34 | +0.04 | +0.09 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +0.42 | +0.00 | +0.28 | +0.20 | -0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +2.5% | +2.5% | -1.0 | +4.2 | -0.2 | -0.4 |
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -2.0% | -2.0% | -3.0 | +1.0 | +0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.0% | -1.0% | -1.1 | +0.1 | +0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.0% | -1.0% | -1.8 | +0.8 | +0.0 | -0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -7.7% | -0.9% | -7.7 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.7% | -0.7% | -0.5 | -0.2 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.2 | -0.4 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.2% | +0.6% | +2.0 | -0.8 | -0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.1 | -0.4 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | +2.1% | +0.5% | +2.2 | -0.0 | -0.1 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +1.2% | +0.4% | -0.8 | +2.2 | -0.0 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +0.4% | +0.4% | +0.0 | +0.0 | +0.4 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LUPIN | +2.00% | +1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → LUPIN | +3.90% | +0.86% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → LUPIN | +2.37% | +0.85% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → LUPIN | -1.42% | -0.83% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ F_US_GENERIC_PRICING → LUPIN | -5.00% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → LUPIN | +0.70% | +0.41% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → LUPIN | +1.44% | +0.40% |
| 2 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → F_USDINR → LUPIN | +5.69% | +0.36% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → LUPIN | -0.69% | -0.35% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LUPIN | -1.19% | -0.33% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → LUPIN | -2.70% | -0.32% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → LUPIN | +1.80% | +0.32% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → LUPIN | -0.84% | -0.30% |
| 2 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → F_USDINR → LUPIN | -0.42% | -0.27% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LUPIN | -1.49% | -0.27% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_USFDA_ENFORCEMENT → LUPIN | +1.00 | events | -3.00% |
| 1 | F_FPI_FLOWS → LUPIN | -1.60 | events | -1.28% |
| 1 | F_USDINR → LUPIN | -0.37 | observed | -1.11% |
| 1 | C_MIDEAST_CONFLICT → LUPIN | +1.50 | events | -1.05% |
| 2 | P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → LUPIN | +1.00 | events | +1.00% |
| 1 | F_REPO_IN → LUPIN | +1.00 | events | -0.50% |
| 1 | P_US_PHARMA_TARIFF → LUPIN | +0.50 | events | -0.45% |
| 2 | P_US_PHARMA_TARIFF → F_US_GENERIC_PRICING → LUPIN | +0.50 | events | +0.30% |
| 1 | F_URBAN_DEMAND → LUPIN | +0.20 | events | +0.24% |
| 2 | F_USDCNY → F_CHINA_CHEM_EXPORTS → LUPIN | -0.47 | observed | -0.08% |
| 2 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → LUPIN | +0.40 | events | -0.07% |
| 2 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → LUPIN | +0.30 | events | -0.07% |

## Analyst profile (agent research, sourced)
# LUPIN (Lupin Ltd.) — Midcap, as of 2026-11-05

## Business
Lupin is a global generics and speciality company: United States ~38%, India ~32% (branded, respiratory and cardio-metabolic), Rest of World and emerging markets ~15%, Europe, Canada and API the rest (model knowledge). Q2 FY27 results on 2026-11-03: revenue Rs 7,827 cr (+11-14% YoY), net profit Rs 1,155 cr (-22%), hit by an exceptional antitrust (US generic-pricing litigation) charge, a Rs 76.9 cr investment impairment at standalone level and margin compression on US competition. Management expects lower operating margins in FY28 (Sahi 2026-11-05). The screener pack's quarterly rows (for example Jun-26 sales Rs 7,172 cr with 52% OPM and Sep-26 sales Rs 3,567 cr with 6% OPM) are inconsistent with press-reported revenue and have been disregarded for margins; this is the main data-quality caveat.

## What moves the stock (ranked)
1. **US generic pricing and competition** (-5.0 per +5pp erosion): the explicit cause of the margin guidance cut. Jefferies cut its target 15% on US competition (2026-11-05).
2. **USD/INR** (+3.0 per +3%): large USD-linked sales; empirical +1.83 (t=1.4).
3. **USFDA enforcement** (-3.0) across Pithampur, Goa, Nagpur and US sites.
4. **US launches** (event): HIV drug launch with 180-day exclusivity eligibility (2026-11-03) and injectable/inhaler approvals are the positive offset.
5. **Tariffs** (-0.9): generics outside the 100% branded tariff (since 2026-09-29).
6. India demand (+1.2), FII flows (+0.8), Middle East (-0.7), China API cost (+0.7), rates (-0.5).

## Transmission examples
- **US buyer consolidation -> contract price cuts on tablets -> Lupin US sales -1.3% -> EBITDA -5% -> FY28 margin guide lower -> analyst cuts -> P/E re-rates** (1st to 3rd order).
- **Fed holds rates higher -> USD stronger -> rupee weaker -> Lupin USD sales translate higher -> partially offsets US price erosion** (2nd order).
- **Middle East escalation -> freight and solvent prices up -> Lupin cost +0.4% -> margins -1.5pp EBITDA; also South Africa / Gulf shipping costs** (2nd to 3rd order).
- **Antitrust settlement -> cash outflow, possible follow-on class suits for other generics -> sector-wide risk, peers' sentiment hurt** (3rd order).

## Current situation
Stock -17% in 3m and -20% in 6m before Q2; rose 2% on results day despite the profit fall. HSBC (2026-09-22) argued the market overstates one risk and understates a positive; Nomura (Rs 2,675 TP) and Kotak (Add) stay constructive while Jefferies cut. Valuation optically 16x on screener EPS, but earnings basis is uncertain.

## Upcoming events
Q3 FY27 (Feb 2027), HIV launch uptake, antitrust payout quantification, USFDA inspections.

## Bull and bear
Bull: HIV 180-day exclusivity, inhaler launches and India outperformance hold margins near 25%. Bear: FY28 margin guide proves conservative-in-reverse (below 22%), more antitrust claims, US pricing shock. Confidence low: pack data inconsistent, margins not verified from the earnings release.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.