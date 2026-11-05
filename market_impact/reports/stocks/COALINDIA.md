# COALINDIA — Coal India Ltd.
*NIFTY_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +7.7%**, **12 months +12.2%** (rank 3 / 5 of 200 for 3m / 12m); beta 0.74
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.5%): 3 months 75%, 12 months 68%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +7.3% … P90 +20.3%; plausible 12m relative-return range incl. stock-specific noise: -22.7% … +39.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +8.7 pp (model impact +17.4% beta-adjusted vs realised market-adjusted move -20.1%); forward event exposure +6.7% (3m +4.5%; half assumed priced); company-specific events +2.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian domestic coal price & availability cost (`F_COAL_INDIA`) | +10% domestic coal cost (notified/e-auction) | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +3.76 | +2.80 | +0.96 | +0.00 | +0.00 | — |
| International thermal coal price (`F_COAL_INTL`) | +15% seaborne thermal coal | +2.52 | +1.80 | +0.72 | +0.00 | +0.00 | +0.0% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -2.48 | +0.00 | -1.60 | -1.09 | +0.22 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +2.09 | +0.00 | +1.20 | +0.71 | +0.18 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | +1.95 | +0.00 | +0.45 | +1.01 | +0.49 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.92 | +0.00 | +1.22 | +0.65 | +0.05 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | -1.22 | -1.20 | +0.00 | -0.04 | +0.02 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +1.17 | +1.00 | +0.19 | -0.01 | -0.01 | +0.0% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.08 | +0.00 | -0.95 | -0.12 | -0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.05 | +1.20 | -0.06 | -0.11 | +0.02 | -1.1% |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | -1.01 | -1.00 | +0.00 | +0.00 | -0.01 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | -0.87 | +0.00 | -0.64 | -0.23 | -0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | +9.0% | +9.0% | +9.0 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +6.5% | +6.5% | +5.0 | +0.9 | +0.4 | +0.2 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.8% | +3.8% | +2.8 | +1.0 | +0.0 | +0.0 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +5.7% | +2.3% | +4.2 | +1.4 | +0.1 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | -2.6% | -1.7% | +0.0 | -1.6 | -1.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | +1.3% | +1.3% | +1.3 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -2.3% | -1.3% | -1.5 | -0.4 | -0.3 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +3.6% | +1.3% | +2.5 | +1.0 | +0.2 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.1 | -0.1 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | +1.0% | +1.0% | +0.6 | +0.2 | +0.3 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +0.9% | +0.9% | +1.0 | +0.0 | -0.0 | +0.0 |
| IMD April 2027 forecast says below-normal monsoon (<96% LPA) - second weak year risk (`EV_MONSOON27_DEFICIT_FORECAST`) | risk_scenario | 0.32 | +2.4% | +0.8% | +0.0 | +1.6 | +0.8 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → COALINDIA | +4.20% | +1.68% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA | -1.60% | -1.09% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → COALINDIA | +2.50% | +0.89% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → COALINDIA | -1.50% | -0.87% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_COAL_INDIA → COALINDIA | -1.03% | -0.70% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → F_COAL_INDIA → COALINDIA | +1.44% | +0.58% |
| 2 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA | +1.60% | +0.51% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA | -0.80% | -0.46% |
| 1 | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → COALINDIA | +0.90% | +0.45% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → COALINDIA | +6.00% | +0.38% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → COALINDIA | +0.80% | +0.36% |
| 2 | EV_NEMONSOON26_DEFICIT ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA | +0.80% | +0.34% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → COALINDIA | +1.56% | +0.34% |
| 3 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_COAL_INDIA → COALINDIA | +1.03% | +0.33% |
| 3 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_COAL_INDIA → COALINDIA | -0.52% | -0.29% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_COAL_INDIA → COALINDIA | +1.50 | events | +9.00% |
| 1 | F_POWER_DEMAND_IN → COALINDIA | +1.20 | events | +3.36% |
| 1 | F_COKING_COAL → COALINDIA | +2.87 | events | +2.30% |
| 1 | F_COAL_INTL → COALINDIA | +0.70 | director_override | +1.26% |
| 1 | F_REPO_IN → COALINDIA | +1.00 | events | -0.70% |
| 1 | T_ENERGY_TRANSITION → COALINDIA | +0.50 | events | -0.50% |
| 1 | F_USDINR → COALINDIA | -0.37 | observed | -0.44% |
| 1 | F_BRENT → COALINDIA | +0.00 | observed | +0.00% |

## Analyst profile (agent research, sourced)
# Coal India (COALINDIA) — market impact profile (as of 2026-11-05)

## Business
Coal India is a near-monopoly domestic miner whose price-setting is half-political. Most coal is sold to power plants at notified prices under long-term FSAs; e-auctions sell the balance at a premium to notified prices, tied to import parity. Costs are largely fixed (wages, contractors, depreciation); royalties and levies are ad valorem. So profit is highly geared to volume and e-auction premiums and slow to respond to cost shocks.

## What moves the stock (ranked)
1. **Price realisation (F_COAL_INDIA)** — notified-price hikes and e-auction premiums; +6.0 per +10% effective.
2. **Volumes via power demand (F_POWER_DEMAND_IN)** — +2.8 per +3pp.
3. **Import parity (F_COAL_INTL, F_USDINR, F_BRENT via gas-to-coal switching)**.
4. **Costs and policy (F_WAGES_IN, P_MINING_ROYALTY)**.
5. **Discount rate (F_REPO_IN)** — a 6.75% yield makes it a bond proxy.
6. **Corporate actions** — MCL/SECL IPOs unlock value but sell down CIL's stake.

## Worked transmission examples
- Hormuz escalation -> LNG and Brent up (order 1) -> gas-based power and industrial users switch to coal/pet-coke (order 2) -> CIL e-auction premiums and offtake rise (order 3) -> EBITDA +, but the government leans on CIL to restrain prices, and imports from Indonesia/Australia become costlier in INR, supporting the premium (order 4). Meanwhile GAIL/ATGL lose volume, without any direct company link (each sits on its own factor).
- Heatwave / strong power demand -> plant coal stocks fall below 18 Mt -> Railways rake allocation and CIL despatch up -> volumes +10% -> operating leverage (fixed costs) lifts EBITDA by ~15%.
- USD/INR up -> import parity in INR up -> e-auction premium up; also thermal power tariffs for imported-coal plants rise, reducing their running and shifting to domestic coal.
- Oil-price crash (current direction) -> pack shows CIL fell with Brent (elasticity +1.78) via energy-complex sentiment, though fundamentals link is weak.

## Current situation
Q2 FY27 PAT Rs 6,547 cr (+57% y/y but -26% q/q), OPM 19%. Brokerages flagged cost pressure and weak realisations; shares fell 3-4% on 30 Oct. October output jumped 19.3% y/y. SEBI approved the Mahanadi Coalfields IPO (5 Nov) and SECL filed its DRHP (2 Nov); Bloomberg reports a $1bn MCL IPO as soon as November. Second interim dividend record date was 4 Nov.

## Upcoming events
MCL/SECL IPOs, monthly output, Q3 results (Feb 2027), price committee, dividend.

## Bull / bear
Bull: gas-to-coal switch, volume growth, subsidiary value unlock, 7x P/E and 6.75% yield. Bear: realisations stuck, wage/royalty cost increases, structural demand erosion, and IPO overhang.

*Weights are exposure estimates, not return forecasts.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.