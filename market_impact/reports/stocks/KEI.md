# KEI — KEI Industries Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.2%**, **12 months +9.5%** (rank 18 / 15 of 200 for 3m / 12m); beta 1.42
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +33.6%): 3 months 60%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +6.5% … P90 +16.5%; plausible 12m relative-return range incl. stock-specific noise: -23.0% … +55.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +6.0 pp (model impact +12.0% beta-adjusted vs realised market-adjusted move -27.9%); forward event exposure +9.1% (3m +3.7%; half assumed priced); company-specific events +0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| New-entrant pricing pressure in wires & cables (`NEW_CABLE_NEW_ENTRANT_PRICING`) | +1 = incumbent W&C gross margin -100 bp industry-wide | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.14 | +3.00 | +0.20 | +0.00 | -0.06 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.41 | +2.00 | +0.39 | +0.04 | -0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.38 | +2.50 | +0.00 | -0.14 | +0.02 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.30 | +0.00 | +1.28 | +1.02 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.07 | +0.00 | -1.26 | -0.60 | -0.21 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.06 | +0.00 | +2.09 | +0.00 | -0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.53 | -1.20 | -0.23 | -0.07 | -0.03 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.21 | +0.00 | -0.96 | -0.21 | -0.04 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.19 | +1.20 | +0.00 | -0.02 | +0.01 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +1.04 | +0.00 | +0.76 | +0.28 | -0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.02 | +0.00 | +0.00 | -0.70 | -0.33 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +0.96 | +0.00 | +0.96 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.0% | +3.0% | +3.0 | +0.2 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -1.5 | -0.7 | -0.2 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.3% | +2.3% | +0.0 | +2.3 | +0.0 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.5% | +2.3% | +2.4 | +0.2 | +0.0 | -0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -2.2 | -0.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.2 | -0.4 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | +0.9 | -1.4 | -1.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -5.0% | -1.4% | -3.0 | -1.2 | -0.6 | -0.3 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.1% | +1.1% | +0.0 | +0.6 | +0.5 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.0% | +1.0% | +0.0 | +1.0 | +0.0 | +0.0 |
| Domestic LPG under-recoveries >Rs59,000 cr (to July); government compensation boosts IOC Q2 (`EV_LPG_UNDERRECOVERY`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.7 | -0.0 | +0.0 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +1.1% | +0.7% | +0.0 | +1.1 | +0.0 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → KEI | +3.00% | +3.00% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → KEI | +2.40% | +2.16% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → KEI | -2.16% | -2.16% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → KEI | -1.59% | -1.59% |
| 2 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → KEI | +1.28% | +1.28% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → KEI | -1.20% | -1.20% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → KEI | -1.06% | -1.06% |
| 2 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → KEI | +0.96% | +0.96% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → KEI | +0.94% | +0.94% |
| 2 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_US_EQUITIES → KEI | +0.86% | +0.86% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → KEI | -3.00% | -0.84% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → KEI | +1.80% | +0.81% |
| 2 | EV_BESS_VGF_NOV26 ⇒ T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → KEI | +0.80% | +0.80% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → KEI | -3.00% | -0.75% |
| 2 | EV_LPG_UNDERRECOVERY ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → KEI | -0.72% | -0.72% |

## Analyst profile (agent research, sourced)
# KEI — KEI Industries (as of 2026-11-05)

## Business
KEI manufactures EHV (up to 400 kV), HT and LT power cables, house wires, control cables and stainless-steel wire, with a small EPC arm. Q2 FY27 (reported 21 Oct 2026): revenue Rs 3,776 cr (+38.5%), domestic wire and cable sales +46%, EBITDA margin 9.97% (9.88% a year earlier), PAT Rs 262 cr (+29%). The wire and cable order book is Rs 4,927 cr, including Rs 991 cr exports (about half US). Cash is Rs 698 cr and the company is almost debt free. Guidance: 25%+ revenue growth in FY27, 20% CAGR for 3-4 years and EBITDA margin rising to 11-12% as the Sanand EHV Phase 2 (about Rs 1,500-1,700 cr revenue potential) commissions in March 2027. The stock is down 27% in three months, hit by the Q2 EBITDA miss (-8% to -11% on 22 Oct) and the 3 Sep launch of UltraTech's Ultravolt cables business (Rs 1,800 cr initial investment).

## What moves the stock, ranked
1. **New-entrant pricing pressure** (proposed node NEW_CABLE_NEW_ENTRANT_PRICING, -5 per -100 bp industry margin). Nuvama warned of aggressive pricing and channel investment; incumbents' stocks fell up to 16% in a week.
2. **Grid, government and private capex** (+4, +3, +2.5). EHV/HT cables for transmission, metros, renewables and data centres.
3. **Copper** (+0.8). Mostly passed through; inventory valuation swings show up as quarterly gross margin noise (cited as the cause of Q2's weaker gross margin).
4. **Data centres** (+2), **housing** (+1.2), **repo** (-1.2), **US tariff** (-0.8), **USD/INR** (+0.6).
5. **US equities beta** (+1.0 after shrinking the empirical +2.25, t +2.1; this is beta, not a causal link).

## Transmission examples
- **Competition chain:** UltraTech funds a distribution push -> dealers get higher trade margins -> house-wire and LT cable prices soften -> KEI's gross margin slips about 100 bp -> EBITDA margin stays near 10% instead of rising to 11-12% -> guided earnings growth is trimmed and the P/E derates from 37x (4th order).
- **Commodity chain:** Middle East escalation -> Brent up -> INR weaker and risk-off -> copper falls with global growth fears -> KEI books inventory losses at the same time as dealers destock -> a margin miss in the following quarter (the reverse of a copper rally, which gives inventory gains).
- **Policy chain:** Higher government capex on transmission and renewables -> Power Grid / state utility tenders -> EHV cable orders -> Sanand Phase 2 fully used -> operating leverage lifts margin to 11-12%.
- **US chain:** US tariff increase on Indian goods -> half of the Rs 991 cr export book at risk -> exports pivot to the Middle East/Europe at lower price.

## Current situation and upcoming events
Q2 revenue beat in growth but missed on margin; Jefferies still sees about 45% upside; PL Capital stays bullish. Events: Q3 results (Jan 2027), Sanand Phase 2 (Mar 2027, prob 0.6), Ultravolt launch / pricing response (Dec 2026, prob 0.45, -6% to 0%).

## Bull and bear
Bull: Ultravolt stays a niche, KEI hits 11-12% margins with EHV mix and 25% growth, justifying a rebound toward Rs 5,000+. Bear: pricing war in LT/house wire plus copper volatility holds margins at 10% and the multiple compresses to 28-30x. Uncertainty: revenue-mix and copper-cost shares are my estimates (model knowledge), not company-disclosed.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.