# MRF — MRF Ltd.
*MIDCAP_100 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.0%** (rank 64 / 65 of 200 for 3m / 12m); beta 1.02
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +17.6%): 3 months 53%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.8% … P90 +4.1%; plausible 12m relative-return range incl. stock-specific noise: -21.8% … +29.5%
- Decomposition (12m): 0.5 × forward event exposure +2.3% (3m +1.2%; half assumed priced) + 0.5 × company-specific catalysts +0.7%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +4.3% (beta-adjusted) vs a realised market-adjusted move of -4.3% — gap +8.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Natural / synthetic rubber price (`F_RUBBER`) | +10% rubber | -3.30 | -3.30 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.51 | +0.00 | -1.53 | -0.60 | -0.37 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.86 | +0.00 | +1.23 | +0.63 | -0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.52 | +0.00 | -1.10 | -0.26 | -0.16 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.47 | -0.95 | -0.21 | -0.30 | -0.02 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.34 | -1.20 | -0.05 | -0.06 | -0.02 | -1.1% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.02 | +0.00 | +1.12 | -0.08 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.97 | +0.00 | +1.13 | -0.14 | -0.02 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.92 | +0.00 | +0.61 | +0.12 | +0.19 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +0.80 | +1.00 | -0.19 | -0.04 | +0.04 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -0.79 | +0.00 | -0.79 | +0.00 | +0.00 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.78 | +0.00 | -0.64 | -0.08 | -0.07 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.73 | -0.60 | -0.04 | -0.07 | -0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.6% | +1.4% | +1.5 | +0.4 | +0.7 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.4% | -1.1% | -2.1 | -1.1 | -1.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.7 | -0.3 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.3 | -0.2 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.7% | -0.7% | -0.6 | -0.0 | -0.1 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -0.7% | -0.7% | -0.2 | -0.4 | -0.0 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | -1.5% | -0.5% | +0.0 | -1.1 | -0.3 | -0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.5 | -0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | +0.5% | +0.5% | +0.4 | +0.0 | +0.0 | +0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.05 | -9.3% | -0.5% | -4.3 | -2.4 | -2.4 | -0.2 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.5% | +0.5% | +0.5 | -0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → MRF | +1.23% | +0.68% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MRF | -2.09% | -0.52% |
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → MRF | +0.42% | +0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → MRF | -1.56% | -0.28% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_RUBBER → MRF | -0.79% | -0.28% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → MRF | +0.55% | +0.28% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MRF | -0.60% | -0.25% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → MRF | -4.27% | -0.21% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → MRF | +0.27% | +0.18% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → F_RUBBER → MRF | +0.33% | +0.18% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → MRF | -0.72% | -0.18% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → MRF | -1.50% | -0.18% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_BRENT → MRF | +0.68% | +0.17% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MRF | -0.60% | -0.16% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → MRF | +0.20% | +0.16% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_AUTO_DEMAND_IN → MRF | +0.50 | director_override | +0.75% |
| 1 | F_STEEL_INDIA → MRF | +1.35 | events | -0.68% |
| 1 | F_REPO_IN → MRF | +1.00 | events | -0.60% |
| 1 | F_GDP_IN → MRF | +0.50 | events | +0.50% |
| 1 | F_USDINR → MRF | -0.37 | observed | +0.44% |
| 1 | F_REFINING_MARGIN → MRF | +0.60 | events | -0.24% |
| 1 | P_ANTI_DUMPING_IN → MRF | +0.40 | events | +0.24% |
| 2 | F_CHINA_GDP → F_RUBBER → MRF | +0.30 | events | -0.24% |
| 1 | F_SHIPPING_RATES → MRF | +0.30 | events | -0.09% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_RUBBER → MRF | +0.40 | events | -0.03% |
| 1 | F_BRENT → MRF | +0.00 | observed | -0.00% |
| 3 | F_BRENT → F_CHEM_FEEDSTOCK → F_RUBBER → MRF | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (trading window closed from 2026-09-29; date unconfirmed) | results | 0.97 | -0.5% | -0.48% |
| 2026-11-01 | GST on retreaded tractor tyres cut to 5% (effective); minor positive for tractor/replacement segments | regulatory | 1.00 | +0.2% | +0.25% |
| 2026-12 | Further replacement price hikes across industry (CEAT: 'plan to take prices further') | guidance | 0.70 | +2.0% | +1.40% |
| 2027-02 | Q3 FY27 results: JK expects RM +4-5% q/q in Q3 | results | 0.97 | -0.5% | -0.48% |

## Analyst profile (agent research, sourced)
# MRF - MRF Ltd. (as of 2026-11-05)

## Business
MRF is India's largest tyre maker with TTM sales of Rs 31,900 cr and an EBITDA margin that has slid from 17% (FY24) to 12% in Q1 FY27. Revenue is roughly 58% replacement, 30% OEM and the rest exports/other. Rubber (natural and synthetic) is about half of tyre cost; raw materials were ~67% of sales in Q1 FY27 (gross margin 32.7%). MRF is the highest-priced stock in India and trades at ~21x earnings, near a 52-week low.

## What moves the stock (ranked)
1. **Rubber** (F_RUBBER -3.3 per +10%): RSS4 is Rs 300/kg, +62% y/y (Mint, 2026-11-05). Each 10% costs MRF ~9% of EBITDA after partial price recovery.
2. **Crude derivatives** (F_BRENT -0.95; refining margin -0.4): carbon black, nylon, chemicals and freight. This matches the pack's empirical -0.92 per +10% Brent (t -2.4) and -1.04 per +$2 GRM (t -2.9), the strongest statistics in this batch.
3. **INR** (F_USDINR -1.2 per +3%): imported rubber and carbon black.
4. **Pricing power**: Anand Rathi noted MRF's replacement hikes are single-digit and below peers. CEAT said previous hikes have not offset costs and more are planned; JK Tyre raised realisation 11-12% in six months.
5. **Demand** (auto volumes +1.5, GDP +1.0): OE demand is strong (record October industry), giving room to pass costs through.
6. **Policy/rates**: anti-dumping (+0.6, conditional), RBI hike (-0.6).

## Worked chains
- **Middle East escalation -> Brent up (1st) -> synthetic rubber, carbon black and nylon up (2nd) -> tyre makers' gross margin -400-600bp before hikes (3rd) -> replacement price hikes of 4-5% slow replacement demand and shift buyers to cheaper brands, weakening MRF's premium positioning (4th).**
- **Brent up -> INR weaker (2nd) -> imported natural rubber costlier in rupees (3rd) -> domestic rubber prices follow import parity (4th) -> further margin loss.**
- **Rubber supply disruption (weather in Thailand/Indonesia + shipping delays) -> RSS4 up (2nd) -> tyre price hikes (3rd) -> CPI up marginally via transport costs (4th) -> RBI tightening.**
- **Freight volumes up (strong GDP, record vehicle sales) -> CV tyre replacement demand (2nd) -> operating leverage (3rd) -> MRF margin recovers faster than peers because of its CV mix (4th).**

## Current situation
Q1 FY27 showed the cost shock: EBITDA -8% on revenue +10%. September-quarter prints from peers were worse (CEAT PAT -40%, JK PAT -73%), and JK guides a further 4-5% rise in raw material cost in Q3. MRF's own Q2 results are due in November. The stock fell to a 52-week low on 21 October and has since stabilised with crude at ~$95 (down from a 6-month high late October).

## Upcoming
Q2 FY27 results (Nov, date unconfirmed), industry price hikes, RBI December MPC, Q3 results (Feb 2027).

## Bull and bear
Bull: rubber/crude retreat, OE strength, MRF finally matches peers' price hikes, and a de-rated valuation. Bear: rubber stays above Rs 300/kg, hikes lag, INR weakens and Chinese imports intensify.

Confidence: medium (cost shares estimated; the Q2 print is unknown).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.