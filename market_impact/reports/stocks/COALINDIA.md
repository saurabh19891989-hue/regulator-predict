# COALINDIA — Coal India Ltd.
*NIFTY_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.6%**, **12 months +1.9%** (rank 4 / 17 of 200 for 3m / 12m); beta 0.74
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.5%): 3 months 56%, 12 months 53%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.4% … P90 +7.2%; plausible 12m relative-return range incl. stock-specific noise: -24.5% … +30.2%
- Decomposition (12m): 0.5 × forward event exposure +2.1% (3m +1.5%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.3%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +11.7% (beta-adjusted) vs a realised market-adjusted move of -20.1% — gap +31.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +3.28 | +2.80 | +0.48 | +0.00 | +0.00 | — |
| Indian domestic coal price & availability cost (`F_COAL_INDIA`) | +10% domestic coal cost (notified/e-auction) | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| International thermal coal price (`F_COAL_INTL`) | +15% seaborne thermal coal | +2.16 | +1.80 | +0.36 | +0.00 | +0.00 | +0.0% |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -1.74 | +0.00 | -1.60 | -0.25 | +0.12 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +1.70 | +0.00 | +1.20 | +0.43 | +0.08 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.48 | +0.00 | +1.22 | +0.25 | +0.02 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | +1.36 | +0.00 | +0.45 | +0.79 | +0.11 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | -1.15 | -1.20 | +0.00 | -0.01 | +0.06 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +1.14 | +1.00 | +0.12 | +0.01 | +0.00 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.09 | +1.20 | -0.06 | -0.06 | +0.01 | -1.1% |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | +4.5% | +4.5% | +4.5 | +0.0 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.3% | +3.3% | +2.8 | +0.5 | +0.0 | +0.0 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +5.0% | +2.0% | +4.2 | +0.7 | +0.1 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | -1.8% | -1.2% | +0.0 | -1.6 | -0.2 | -0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | +1.0% | +1.0% | +1.0 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -1.9% | -1.0% | -1.3 | -0.2 | -0.3 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | +0.9% | +0.9% | +0.6 | +0.1 | +0.2 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.7 | -0.0 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | +3.0% | +0.8% | +2.2 | +0.8 | +0.1 | -0.0 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | -0.9% | -0.7% | +0.0 | -0.8 | -0.1 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | -0.0 | +0.0 |
| IMD April 2027 forecast says below-normal monsoon (<96% LPA) - second weak year risk (`EV_MONSOON27_DEFICIT_FORECAST`) | risk_scenario | 0.32 | +1.7% | +0.5% | +0.0 | +1.6 | +0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → COALINDIA | +4.20% | +1.68% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA | -1.60% | -1.09% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → COALINDIA | -1.30% | -0.72% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA | -0.80% | -0.68% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → COALINDIA | +2.20% | +0.55% |
| 2 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA | +1.60% | +0.51% |
| 1 | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → COALINDIA | +0.90% | +0.45% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → COALINDIA | +0.80% | +0.36% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → COALINDIA | -0.70% | -0.29% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → F_COAL_INDIA → COALINDIA | +0.72% | +0.29% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → COALINDIA | -0.36% | -0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → COALINDIA | +1.56% | +0.28% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → COALINDIA | -0.55% | -0.28% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → COALINDIA | +0.40% | +0.24% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → COALINDIA | +4.50% | +0.23% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_COAL_INDIA → COALINDIA | +1.50 | events | +4.50% |
| 1 | F_POWER_DEMAND_IN → COALINDIA | +1.20 | events | +3.36% |
| 1 | F_COAL_INTL → COALINDIA | +0.70 | director_override | +1.26% |
| 1 | F_COKING_COAL → COALINDIA | +1.30 | events | +1.04% |
| 1 | F_REPO_IN → COALINDIA | +1.00 | events | -0.70% |
| 1 | F_USDINR → COALINDIA | -0.37 | observed | -0.44% |
| 1 | T_ENERGY_TRANSITION → COALINDIA | +0.30 | director_override | -0.30% |
| 1 | F_BRENT → COALINDIA | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | MCL IPO launch (~$1bn, offer for sale of up to 66 cr shares; SEBI approval 5 Nov); SECL DRHP filed 2 Nov | corporate_action | 0.65 | +2.2% | +1.46% |
| 2026-12 | Monthly production/offtake releases (1st of month): Oct output +19.3% y/y; sustained >10% growth with rake supply improves FY27 volumes | other | 0.90 | +0.5% | +0.45% |
| 2027-02 | Q3 FY27 results (CIL reports around early Feb) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Notified-price revision or e-auction reform for FY28 (pricing committee) | regulatory | 0.20 | +2.0% | +0.40% |

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