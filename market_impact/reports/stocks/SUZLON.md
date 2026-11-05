# SUZLON — Suzlon Energy Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months +0.2%** (rank 137 / 90 of 200 for 3m / 12m); beta 1.37
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.0%): 3 months 49%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.9% … P90 +4.3%; plausible 12m relative-return range incl. stock-specific noise: -44.5% … +40.8%
- Decomposition (12m): 0.5 × forward event exposure +0.4% (3m +0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +3.2% (beta-adjusted) vs a realised market-adjusted move of -35.0% — gap +38.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Wind-turbine pricing competition (`NEW_WTG_PRICING_COMPETITION`) | +1 = realised WTG price per MW -5% | -8.00 | -8.00 | +0.00 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.75 | +2.80 | +0.00 | -0.05 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.41 | -2.00 | +0.00 | -0.16 | -0.25 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.94 | -2.00 | +0.05 | +0.03 | -0.02 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.81 | -1.80 | +0.00 | -0.01 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.69 | -1.20 | -0.38 | -0.10 | -0.01 | -1.1% |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.56 | +1.50 | +0.06 | +0.00 | -0.00 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.44 | +0.00 | -0.53 | -0.53 | -0.38 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.42 | +0.00 | -1.39 | -0.04 | +0.02 | — |
| Copper price (`F_COPPER`) | +10% copper | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | -2.4% |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -0.89 | +0.00 | -0.89 | +0.00 | -0.01 | +20.6% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.78 | +0.00 | +0.00 | -0.77 | -0.02 | — |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | -0.72 | +0.00 | -0.72 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.7% | +2.7% | +2.8 | -0.1 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -2.1% | -2.1% | -2.0 | +0.0 | -0.0 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.0 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.9% | -1.9% | -2.0 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.6 | -0.1 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.8% | +1.6% | +2.0 | +0.4 | +0.4 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.0 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.4% | +1.4% | +1.4 | +0.0 | -0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.9% | -1.0% | -2.4 | -0.7 | -0.8 | -0.1 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +2.2% | +0.9% | +2.2 | +0.0 | +0.1 | -0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.9% | -0.8% | -2.0 | +0.0 | +0.0 | -0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | +0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → SUZLON | +2.00% | +1.10% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → SUZLON | +2.25% | +0.90% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SUZLON | -2.00% | -0.84% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → SUZLON | -2.40% | -0.60% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → SUZLON | -0.86% | -0.58% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SUZLON | -2.00% | -0.54% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → SUZLON | -0.72% | -0.40% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → SUZLON | -0.43% | -0.37% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → SUZLON | -2.00% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → SUZLON | -1.56% | -0.28% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → SUZLON | +0.55% | +0.28% |
| 2 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → F_POWER_DEMAND_IN → SUZLON | +0.86% | +0.27% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → SUZLON | -1.08% | -0.27% |
| 1 | EV_GST_RATE_CHANGE_APR27 ⇒ P_RENEWABLE_SUPPORT → SUZLON | +0.84% | +0.25% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ C_MIDEAST_CONFLICT → SUZLON | -5.00% | -0.25% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → SUZLON | +1.35 | events | -2.43% |
| 1 | C_MIDEAST_CONFLICT → SUZLON | +1.00 | events | -2.00% |
| 1 | F_REPO_IN → SUZLON | +1.00 | events | -2.00% |
| 1 | F_POWER_DEMAND_IN → SUZLON | +1.20 | events | +1.80% |
| 1 | P_RENEWABLE_SUPPORT → SUZLON | +0.60 | director_override | +1.68% |
| 1 | F_USDINR → SUZLON | -0.37 | observed | +0.44% |
| 1 | F_COPPER → SUZLON | -0.24 | observed | +0.21% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → SUZLON | +0.50 | director_override | +0.12% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → SUZLON | -0.30 | events | -0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Additional large order wins (1.5 GW added in H1) *(review: [RT_TOP_B] routine orders do not move the stock)* | other | 0.60 | +0.5% | +0.30% |
| 2027-02 | Q3 FY27 results (Dec quarter) - H2-loaded deliveries must offset H1 margin | results | 0.95 | +0.0% | +0.00% |
| 2027-02 | Margin trajectory: FY27 guidance ~15% +/-1% test in Q3 | guidance | 0.50 | -1.5% | -0.75% |
| 2027-03 | First S175 5 MW commercial installations and export-order milestone (BlueSky certifications) | other | 0.40 | +2.5% | +1.00% |

## Analyst profile (agent research, sourced)
# SUZLON — Suzlon Energy (as of 2026-11-05)

## Business
Suzlon is India's largest wind-turbine OEM (22+ GW installed in 17 countries) with turbine manufacturing (S144 3.15 MW; S175 5 MW and 6.3 MW launching), a Devco project-development model, O&M services (Suzlon Global Services) and forgings (SE Forge); it acquired Renom. Q2 FY27 (reported 29 Oct 2026): revenue Rs 4,869 cr (+26%), EBITDA Rs 720 cr flat y/y, margin 14.8% (18.6% a year ago), record 710 MW deliveries, comparable PAT Rs 394 cr (+1.3%; reported -69% because Q2 FY26 included an Rs 891 cr deferred-tax credit). The order book is 6 GW (18 months of cover) with 1.5 GW added in H1, net cash Rs 2,048 cr and net worth Rs 10,277 cr; Crisil upgraded to AA- stable. FY27 EBITDA margin guidance was cut to about 15% +/-1% from about 17%. WTG contribution margin fell to 21.2% from 26.9% on customer/scope mix, forex and commodities, and non-recurring costs. The stock fell about 10% to a 52-week low of Rs 33.2 on 30 Oct and recovered to Rs 38.5.

## What moves the stock, ranked
1. **Policy support for renewables** (+7 per standard policy shock). Orders depend on RE auctions, C&I wind-hybrid demand and local-content rules.
2. **WTG pricing competition** (proposed node, -8 per -5% realised price per MW). This is the core of JM Financial's downgrade (competition, margin sustainability, post-FY28 growth). UBS and MOFSL (Buy, Rs 65 target, Oct 12) disagree.
3. **Steel and copper** (-1.8 per +7% domestic steel; copper -0.9). The empirical global-steel elasticity of -2.44 (t -2.0) matches the fundamental figure.
4. **FX and West Asia** (USD/INR -1.2, Mideast conflict -2.0): management explicitly links the margin cut to commodity and FX pressure from the West Asia crisis.
5. **Rates** (-2.0) and power demand (+1.5), data centres (+1.5).

## Transmission examples
- **Commodity chain:** Middle East escalation -> Brent and steel up, INR weaker -> towers, forgings and imported gearboxes dearer while orders are fixed-price -> WTG contribution margin falls from 21% toward 18% -> FY27 margin lands at the low end of 15% +/-1% -> JM-style downgrades and stock de-rating (4th order: rating and flow impact).
- **Competition chain:** Global OEMs and Indian entrants add wind capacity -> turbine tenders priced lower -> Suzlon realised price per MW falls 5% -> EBITDA margin ~11% -> FY28 EPS cuts. Mix is the swing factor.
- **Macro chain:** Brent up -> INR weaker -> RBI holds -> IPP cost of capital up -> fewer wind projects reach financial close -> order inflow slows in H2.
- **Policy chain:** Faster RE auctions and transmission build-out (see GVT&D, POWERGRID) -> more wind-hybrid awards -> order book beyond 6 GW -> execution scale benefits.

## Current situation and upcoming events
Q2 equity reaction was -10% (intraday), the 52-week low, and the shares are -31% over six months. Events: Q3 FY27 results (Feb 2027, prob 0.95), the first S175 installations and export-order milestone (prob 0.4), new order wins (prob 0.6), and the H2-loaded delivery profile. Promoter holding is 11.7%; there is no dividend.

## Bull and bear
Bull: margins recover to the 17% range as mix normalises, S175 wins and exports start, and 18 months of cover plus net cash supports multi-year growth. Bear: competition erodes price per MW, commodity/FX squeezes continue, post-FY28 visibility fades and working capital rises. Uncertainty: customer concentration not verified; cost-share estimates are approximate.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.