# SUZLON — Suzlon Energy Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.6%**, **12 months +6.3%** (rank 26 / 28 of 200 for 3m / 12m); beta 1.37
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.0%): 3 months 58%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +2.2% … P90 +12.3%; plausible 12m relative-return range incl. stock-specific noise: -28.9% … +48.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +5.4 pp (model impact +10.9% beta-adjusted vs realised market-adjusted move -35.0%); forward event exposure +2.4% (3m +1.4%; half assumed priced); company-specific events +1.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Wind-turbine pricing competition (`NEW_WTG_PRICING_COMPETITION`) | +1 = realised WTG price per MW -5% | -8.00 | -8.00 | +0.00 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +6.95 | +7.00 | +0.00 | -0.05 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.59 | -2.00 | +0.00 | -0.23 | -0.36 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.49 | +0.00 | -2.54 | -0.04 | +0.09 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.94 | -2.00 | +0.05 | +0.03 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.84 | -1.20 | -0.38 | -0.24 | -0.02 | -1.1% |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.83 | -1.80 | +0.00 | -0.03 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.70 | +0.00 | -0.53 | -0.72 | -0.45 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.55 | +1.50 | +0.06 | +0.00 | -0.01 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.38 | +0.00 | +0.00 | -1.40 | +0.02 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.28 | +0.00 | -0.92 | -0.27 | -0.10 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.01 | +0.00 | -0.38 | -0.54 | -0.09 | +0.0% |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -0.91 | +0.00 | -0.89 | +0.00 | -0.02 | +20.6% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.1% | -8.1% | -3.0 | -1.9 | -2.7 | -0.5 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +6.9% | +6.9% | +7.0 | -0.1 | +0.0 | -0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +3.5% | +3.5% | +3.5 | +0.0 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -2.9 | -0.0 | +0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.6% | -2.6% | -2.5 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.8% | +2.2% | +2.0 | +0.6 | +0.9 | +0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.5% | -2.0% | -2.4 | -1.1 | -1.5 | -0.5 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.5 | -0.3 | -0.2 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +2.2% | +0.9% | +2.2 | +0.0 | +0.2 | -0.2 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.7 | -0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → SUZLON | +2.00% | +1.16% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → SUZLON | +2.25% | +0.90% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → SUZLON | -2.40% | -0.86% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SUZLON | -2.00% | -0.80% |
| 1 | EV_GST_RATE_CHANGE_APR27 ⇒ P_RENEWABLE_SUPPORT → SUZLON | +2.10% | +0.63% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → SUZLON | -0.86% | -0.58% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → SUZLON | -2.30% | -0.58% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SUZLON | -2.00% | -0.54% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → SUZLON | -0.80% | -0.48% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → SUZLON | -2.00% | -0.44% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → SUZLON | -0.72% | -0.40% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → SUZLON | -1.56% | -0.34% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → SUZLON | -0.95% | -0.34% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → SUZLON | +0.57% | +0.33% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → SUZLON | -0.51% | -0.33% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_RENEWABLE_SUPPORT → SUZLON | +1.50 | events | +10.50% |
| 1 | C_MIDEAST_CONFLICT → SUZLON | +1.50 | events | -3.00% |
| 1 | F_STEEL_INDIA → SUZLON | +1.65 | events | -2.97% |
| 1 | F_REPO_IN → SUZLON | +1.00 | events | -2.00% |
| 1 | F_POWER_DEMAND_IN → SUZLON | +1.20 | events | +1.80% |
| 1 | F_USDINR → SUZLON | -0.37 | observed | +0.44% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → SUZLON | +1.00 | events | +0.24% |
| 1 | F_COPPER → SUZLON | -0.24 | observed | +0.21% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → SUZLON | -0.30 | events | -0.11% |

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