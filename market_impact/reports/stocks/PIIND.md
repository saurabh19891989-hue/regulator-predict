# PIIND — PI Industries Ltd.
*MIDCAP_100 · Chemicals · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months -0.2%** (rank 32 / 114 of 200 for 3m / 12m); beta 0.76
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.2%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.1% … P90 +4.8%; plausible 12m relative-return range incl. stock-specific noise: -36.2% … +38.0%
- Decomposition (12m): 0.5 × forward event exposure +4.5% (3m +2.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -4.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.9% (beta-adjusted) vs a realised market-adjusted move of -35.3% — gap +37.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Global agrochemical prices and channel destocking (`NEW_AGROCHEM_PRICES_GLOBAL`) | +10% global agchem active prices / volumes | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | -3.03 | -3.00 | +0.00 | -0.03 | +0.00 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +2.92 | +3.00 | -0.08 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.01 | +2.00 | +0.00 | +0.00 | +0.01 | -1.1% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.63 | +1.50 | +0.14 | +0.03 | -0.04 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -1.38 | -1.20 | -0.22 | +0.05 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.20 | +1.20 | +0.00 | +0.02 | -0.02 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.09 | +0.00 | +0.96 | +0.09 | +0.04 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| Production-linked incentive schemes (`P_PLI`) | +1 = expansion/disbursement | +0.94 | +0.00 | +0.96 | -0.02 | +0.00 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -0.84 | +0.00 | -0.77 | -0.08 | +0.01 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -0.79 | +0.00 | -0.72 | -0.06 | -0.01 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.54 | +0.00 | -0.48 | +0.01 | -0.08 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.1% | -2.1% | -1.9 | -0.2 | -0.0 | +0.0 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +1.8% | +1.4% | +1.8 | -0.0 | +0.0 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.6% | +1.1% | +1.5 | +0.2 | -0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.8 | +0.0 | +0.0 |
| India-US interim trade agreement formally signed/announced (`EV_INDIA_US_INTERIM_DEAL_SIGNED`) | anticipated | 0.55 | +1.4% | +0.8% | +1.5 | -0.1 | -0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | +0.0 | +0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.7% | +0.7% | +0.6 | +0.1 | +0.0 | -0.0 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +0.8% | +0.7% | +0.8 | +0.1 | -0.0 | +0.0 |
| India-EU FTA signed at ceremony (planned 16 Dec 2026) (`EV_INDIA_EU_FTA_SIGNED`) | scheduled | 0.92 | +0.6% | +0.5% | +0.6 | -0.0 | +0.0 | +0.0 |
| Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil (`EV_RUSSIA_TARIFF_ENFORCED`) | risk_scenario | 0.15 | -3.6% | -0.5% | -3.0 | -0.8 | +0.2 | -0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +0.5% | +0.5% | +0.0 | +0.5 | -0.0 | +0.0 |
| IMD April 2027 forecast says below-normal monsoon (<96% LPA) - second weak year risk (`EV_MONSOON27_DEFICIT_FORECAST`) | risk_scenario | 0.32 | -1.6% | -0.5% | -1.5 | -0.2 | +0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → PIIND | +1.80% | +1.44% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → PIIND | +1.50% | +1.02% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → PIIND | +0.75% | +0.64% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ T_CHINA_PLUS_ONE → PIIND | +0.90% | +0.49% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → PIIND | +0.88% | +0.49% |
| 1 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → PIIND | -1.50% | -0.48% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → PIIND | +2.60% | +0.47% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → PIIND | -0.92% | -0.46% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → PIIND | -3.00% | -0.45% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ T_CHINA_PLUS_ONE → PIIND | +0.60% | +0.42% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → PIIND | -1.50% | -0.37% |
| 2 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → PIIND | +0.50% | +0.35% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → PIIND | +0.96% | +0.34% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → PIIND | +0.60% | +0.33% |
| 1 | EV_INDIA_US_TALKS_COLLAPSE ⇒ P_US_TARIFF_INDIA → PIIND | -1.80% | -0.32% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_MONSOON → PIIND | -1.56 | events | -2.34% |
| 1 | F_USDINR → PIIND | -0.37 | observed | -0.74% |
| 1 | P_US_TARIFF_INDIA → PIIND | -0.60 | events | +0.72% |
| 2 | F_USDCNY → F_CHINA_CHEM_EXPORTS → PIIND | -0.47 | observed | +0.34% |
| 2 | P_FDI_RULES → T_CHINA_PLUS_ONE → PIIND | +0.50 | events | +0.30% |
| 1 | F_RURAL_DEMAND → PIIND | -0.25 | events | -0.30% |
| 2 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → PIIND | +0.30 | events | +0.29% |
| 2 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → PIIND | +0.40 | events | +0.29% |
| 1 | F_EU_GDP → PIIND | +0.22 | events | +0.22% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → PIIND | -0.60 | events | +0.22% |
| 2 | C_US_CHINA_DECOUPLING → T_CHINA_PLUS_ONE → PIIND | -0.10 | events | -0.13% |
| 2 | C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → PIIND | -0.10 | events | +0.12% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Post-Q2 management commentary / analyst downgrades follow-through | guidance | 0.70 | -1.0% | -0.70% |
| 2027-02 | Q3 FY27 results (estimate) | results | 0.97 | +0.0% | +0.00% |
| 2027-06 | Stabilisation or further loss of CSM contract volumes with key customer(s) | other | 0.30 | -12.5% | -3.75% |

## Analyst profile (agent research, sourced)
# PIIND — PI Industries Ltd. (as of 2026-11-05)

*Facts from screener.in (evidence pack through Sep 2026) and Google News headlines. Article bodies could not be retrieved, so reasons for the Q2 miss and the 'Kumiai warning' are not verified. Model knowledge is labelled. No expected-return number.*

## Business
PI Industries makes active ingredients and intermediates for global crop-science innovators under multi-year custom-synthesis (CSM) contracts, with a smaller domestic branded business. Exports are about two-thirds of revenue (model estimate). Q2 FY27 sales were Rs 1,702 cr, flat y/y; EBITDA Rs 233 cr; OPM 14% versus 29% a year ago; PAT Rs 122 cr (-70%). FY26 sales fell 16%. The stock at Rs 1,844 is 52% below its high.

## What moves the stock (ranked)
1. **Innovator off-take and destocking (NEW_AGROCHEM_PRICES_GLOBAL, +6.0 per +10%).** Order timing from a few large customers sets revenue and mix.
2. **China competition (F_CHINA_CHEM_EXPORTS, -3.0 per +15%)** and **China+1 sourcing thesis (+3.0).**
3. **USD/INR (+2.0 per +3%):** a net-long-USD exporter.
4. **Domestic demand:** monsoon (+1.5) and rural demand (+1.2).
5. **Tariffs (-1.2) and feedstock (-1.0).**

## Transmission examples
- **China price cuts -> contracts at risk.** F_CHINA_CHEM_EXPORTS up -> generic active prices fall (1st) -> innovators push for price reductions or dual-source (2nd) -> PI's CSM volumes and mix weaken, OPM falls below 14% (3rd) -> operating leverage on a fixed-cost base, ROCE falls, multiple de-rates (4th).
- **Middle East escalation -> Brent -> solvents.** C_MIDEAST_CONFLICT -> Brent +10% -> aromatics/solvent costs up (1st) -> PI recovers ~70% via contracts after 1-2 quarters (2nd) -> residual ~1% EBITDA hit (3rd); INR weakens at the same time, which partly offsets (+2.0 per +3%).
- **RBI hike -> rural demand.** Repo 5.50% (7 Oct) -> farm credit costs rise slowly -> domestic agri-input demand softer in rabi (3-12m); small for PI as domestic is a third of sales.
- **Monsoon above normal -> kharif sales up -> domestic EBITDA +4%.**

## Current situation
Q2 (4 Nov): profit Rs 122 cr (-70%), margins nearly halved; shares fell 15-18% on 5 Nov to a six-year low. Morgan Stanley double-downgraded on 21 Oct (-5%). On 11 Sep the stock fell 7% on a 'Kumiai warning' (a Japanese innovator customer; detail not retrieved).

## Upcoming
Management call transcripts and brokerage revisions (Nov); Q3 results (~Feb 2027); any customer news.

## Bull case
Destocking is nearly over; Q2 is the trough; rupee at 94.5 helps; valuation is at 6-year lows.

## Bear case
CSM contract renegotiations continue, Chinese pricing pressure persists, and margins stay at 14% or lower.

## Uncertainties
Customer concentration and the cause of the miss are unverified; export share, tariff exposure and segment mix are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.