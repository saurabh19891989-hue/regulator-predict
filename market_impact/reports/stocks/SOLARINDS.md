# SOLARINDS — Solar Industries India Ltd.
*NIFTY_NEXT_50 · Chemicals · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.0%**, **12 months +1.9%** (rank 12 / 15 of 200 for 3m / 12m); beta 0.89
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +37.3%): 3 months 52%, 12 months 53%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.6% … P90 +6.6%; plausible 12m relative-return range incl. stock-specific noise: -46.0% … +49.0%
- Decomposition (12m): 0.5 × forward event exposure +2.3% (3m +0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +5.9% (beta-adjusted) vs a realised market-adjusted move of -2.0% — gap +7.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.71 | +0.04 | +0.75 | +0.05 |
| Sector | +0.35 | -0.32 | +0.02 | +0.07 |
| Theme | +0.75 | -0.01 | +0.74 | +0.37 |
| Geopolitics | -0.12 | +0.25 | +0.13 | +0.02 |
| Company catalysts | +0.93 | +0.00 | +0.93 | +0.83 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.51 | -0.23 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+1.92** | **+1.01** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian defence exports (`T_DEFENCE_EXPORTS`) | +1 | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +4.86 | +0.00 | +4.26 | +0.61 | -0.01 | — |
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +3.65 | +3.00 | +0.66 | +0.00 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.02 | -2.00 | -0.02 | +0.00 | +0.00 | — |
| Africa & Latin America demand (`C_AFRICA_LATAM`) | +1 pp growth | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +1.51 | +1.50 | +0.18 | -0.01 | -0.16 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.41 | +1.50 | +0.00 | -0.05 | -0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.08 | +0.00 | -1.05 | -0.04 | +0.02 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.59 | +0.00 | +0.00 | -0.58 | -0.01 | — |
| Ammonia / urea / phosphate input prices (`F_FERTILISER_INPUTS`) | +15% fertiliser inputs | -0.51 | -0.50 | +0.00 | +0.00 | -0.01 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | +0.48 | +0.50 | -0.05 | +0.01 | +0.02 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.46 | +0.00 | -0.48 | +0.01 | +0.01 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -0.46 | +0.00 | -0.57 | -0.07 | +0.18 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +3.7% | +3.7% | +3.0 | +0.7 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | -0.0 | +0.0 | -0.0 |
| New BrahMos/defence export contracts (Philippines follow-on, Indonesia, Vietnam or others) announced (`EV_DEFENCE_EXPORT_ORDERS`) | anticipated | 0.50 | +3.6% | +1.8% | +3.6 | +0.0 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.3% | +1.3% | +1.5 | -0.1 | -0.1 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.2% | +1.2% | +1.5 | -0.1 | -0.1 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.4% | +1.2% | +1.2 | +0.2 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.2 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -1.8% | -1.0% | -2.1 | +0.0 | +0.2 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.0% | +1.0% | +1.0 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.0% | -0.8% | -2.0 | -0.0 | +0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | +2.4% | +0.6% | +2.9 | -0.2 | -0.2 | -0.1 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +1.5% | +0.6% | +1.5 | +0.0 | +0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → SOLARINDS | +3.00% | +1.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SOLARINDS | -2.00% | -0.84% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → SOLARINDS | -1.50% | -0.83% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → SOLARINDS | +0.90% | +0.81% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → SOLARINDS | +1.50% | +0.60% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SOLARINDS | -2.00% | -0.54% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → SOLARINDS | +1.80% | +0.45% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → SOLARINDS | -0.57% | -0.39% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → SOLARINDS | -2.00% | -0.36% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → SOLARINDS | -0.65% | -0.36% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ P_DEFENCE_PROCUREMENT → SOLARINDS | +0.60% | +0.30% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → SOLARINDS | +1.10% | +0.28% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SOLARINDS | +0.30% | +0.27% |
| 2 | EV_INDIA_PAK_CRISIS ⇒ C_INDIA_PAKISTAN → P_DEFENCE_PROCUREMENT → SOLARINDS | +3.00% | +0.27% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → SOLARINDS | -0.29% | -0.24% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REPO_IN → SOLARINDS | +1.00 | events | -2.00% |
| 1 | C_MIDEAST_CONFLICT → SOLARINDS | +1.00 | events | +1.50% |
| 1 | P_DEFENCE_PROCUREMENT → SOLARINDS | +0.50 | director_override | +1.50% |
| 1 | F_POWER_DEMAND_IN → SOLARINDS | +1.20 | events | +1.20% |
| 1 | F_FERTILISER_INPUTS → SOLARINDS | +1.00 | events | -0.50% |
| 1 | C_RUSSIA → SOLARINDS | +1.00 | events | +0.50% |
| 2 | F_DXY → C_AFRICA_LATAM → SOLARINDS | +0.74 | observed | -0.35% |
| 1 | F_GOVT_CAPEX → SOLARINDS | +0.20 | director_override | +0.30% |
| 2 | P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → SOLARINDS | +0.50 | director_override | +0.30% |
| 1 | F_USDINR → SOLARINDS | -0.37 | observed | -0.18% |
| 1 | F_BRENT → SOLARINDS | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-02 | Q3 FY27 results (Dec quarter): defence delivery ramp toward >Rs 4,500 cr FY27 target | results | 0.95 | +0.0% | +0.00% |
| 2027-02 | Upgrade of FY27 revenue guidance above Rs 14,000 cr | guidance | 0.55 | +3.0% | +1.65% |
| 2027-03 | Omnia Holdings acquisition: shareholder / regulatory (South Africa competition) approvals and funding details | corporate_action | 0.60 | +0.0% | +0.00% |
| 2027-03 | Large defence export or domestic order announcement (>Rs 1,000 cr) *(review: [RT_TOP_B] export-order channel already in EV_DEFENCE_EXPORT_ORDERS)* | other | 0.45 | +1.8% | +0.79% |
| 2027-06 | Plant accident / PESO regulatory action (explosives sector tail risk) | regulatory | 0.06 | -9.5% | -0.57% |

## Analyst profile (agent research, sourced)
# SOLARINDS — Solar Industries India (Nifty Next 50, as of 2026-11-05)

## Business
Solar Industries is India's largest commercial-explosives group (about 26% volume share in FY25, 20-23% wallet share at Coal India) and a fast-growing defence supplier of rockets, warheads, ammunition filling and pyro products. Q2 FY27 (reported 3 Nov 2026) revenue was Rs 3,519 cr (+69% vs ~50% expected), EBITDA Rs 1,006 cr (28.6%, +200 bp) and PAT Rs 617-650 cr (+79%). The mix was international explosives 43%, defence 29% (24% a year ago) and domestic explosives 27%. The order book is Rs 20,178 cr, of which defence is Rs 17,568 cr. H1 revenue Rs 7,187 cr against FY27 guidance of Rs 14,000 cr, which management expects to exceed; defence revenue target for FY27 is above Rs 4,500 cr versus only about Rs 1,002 cr in Q2, so delivery is steeply H2-weighted. On 14 Sep 2026 the company agreed to buy South Africa's Omnia Holdings for US$1.355 bn (Rs 12,951 cr, all cash), targeting FY28 combined revenue above Rs 30,000 cr and EBITDA of Rs 6,800-7,000 cr. The stock fell 8-9% on the deal, then recovered on results.

## What moves the stock, ranked
1. **Defence orders and execution** (procurement +3 per +10% domestic orders; defence exports +5 per standard shock). This is where the multiple (74x trailing) comes from.
2. **The Omnia financing and integration.** Not yet quantified: the fetched article did not disclose the funding mix. At ~70% debt and ~8% cost, interest could add about Rs 700 cr a year against TTM EBITDA of Rs 3,555 cr; rates (-2 per +25 bp) and USD/INR matter more than before.
3. **Domestic mining/infrastructure volumes** (government capex +1.5, power demand +1.0) tied to Coal India and tunnelling/roads.
4. **International mining cycle** (Africa/LatAm +2) which Omnia will enlarge.
5. **Input costs.** Ammonium nitrate, linked to ammonia and gas, is about 18% of sales but price-variation clauses recover about 80% in a quarter (-0.5 per +15% fertiliser inputs).
6. **Geopolitics** (Middle East +1.5 with wide range; Russia AN supply +0.5).

## Empirical cross-check
Edible oil +4.70 (t +2.8), DXY -3.17 (t -2.1) are the significant betas. Edible oil has no causal link to explosives and I treat it as a commodity-reflation / risk-on proxy and do not adopt it. DXY is consistent with a high-multiple EM stock reacting to dollar strength; it is partly captured by the rate and FX edges. Aluminium +2.39 (t +1.8) has the opposite sign from a pure cost channel (aluminium powder is a small input); I read it as the mining-cycle co-movement and left aluminium out as an edge.

## Transmission examples
- **Defence chain (3rd/4th order):** Middle East or Eastern Europe escalation -> global ammunition and rocket demand up -> Solar's export and domestic defence orders rise (order book already Rs 17,568 cr) -> utilisation of ammunition-filling capacity rises and defence mix lifts group EBITDA margin (defence is higher margin) -> the market capitalises FY28 revenue above Rs 30,000 cr and the stock re-rates.
- **Cost chain:** Brent up -> gas and ammonia up -> AN price up -> bulk explosives cost up -> Coal India contracts adjust with a quarter's lag -> small margin squeeze, offset by volume. Same Brent shock also lifts the rupee cost of imports and weakens INR, which raises the INR value of Omnia debt service.
- **Macro chain:** Rate hike or higher Brent-driven inflation -> RBI holds -> infrastructure and mining capex slows -> domestic explosives volumes grow slower; meanwhile higher funding cost lands on an Rs 12,951 cr acquisition loan.
- **Commodity-cycle chain:** China growth -> copper/gold/coal prices up -> African miners expand -> international explosives volumes and Omnia earnings rise.

## Current situation and upcoming events
Q2 beat but the shares faded: Yahoo close on 5 Nov was Rs 18,580, versus a post-result intraday high of Rs 20,880 on 3 Nov and Rs 19,877 at 3 pm; I did not find a dated reason. Key events: Omnia approvals and funding (prob 0.6 by Mar 2027), Q3 FY27 results (Feb 2027), a possible guidance upgrade (0.55), large defence orders (0.45), Union Budget 1 Feb 2027, and a low-probability explosives-safety/PESO incident (0.06, -4% to -15%).

## Bull and bear
Bull: defence ramps to the Rs 4,500 cr FY27 target and beyond, Omnia synergies are credible, margin sustains 28-30% and earnings compound at 35-45%. Bear: defence deliveries slip into FY28, the Omnia purchase is financed at stretched leverage, order timing disappoints, and a 50-75x multiple derates 20-30%. Confidence is medium: segment profit splits and Omnia funding were not disclosed in the sources I could read.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.