# TIINDIA — Tube Investments of India Ltd.
*MIDCAP_100 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.8%**, **12 months +3.2%** (rank 51 / 52 of 200 for 3m / 12m); beta 1.06
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.7%): 3 months 55%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.0% … P90 +8.1%; plausible 12m relative-return range incl. stock-specific noise: -29.5% … +45.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.8 pp (model impact +3.6% beta-adjusted vs realised market-adjusted move -31.1%); forward event exposure +4.6% (3m +2.3%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.67 | +0.00 | +1.15 | +0.47 | +0.05 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +1.51 | +1.50 | +0.00 | +0.01 | +0.00 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -1.47 | -1.50 | +0.01 | +0.01 | +0.01 | -1.4% |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.41 | -1.40 | +0.00 | -0.01 | +0.00 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +1.40 | +1.40 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.26 | +0.00 | -0.86 | -0.45 | +0.06 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.95 | -0.80 | -0.12 | -0.01 | -0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.74 | +0.00 | +0.00 | -0.51 | -0.23 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -0.70 | +0.00 | -0.69 | +0.00 | -0.01 | +20.6% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.59 | +0.00 | -0.35 | -0.29 | +0.05 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +0.58 | +0.80 | +0.00 | -0.15 | -0.06 | — |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | -0.57 | +0.00 | -0.56 | +0.00 | -0.01 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.52 | +0.00 | -0.60 | -0.09 | +0.17 | — |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -0.46 | +0.00 | -0.28 | -0.18 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.0 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.0 | -0.6 | +0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | +0.5 | -1.1 | -0.5 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.0% | -1.0% | -0.8 | -0.1 | -0.0 | -0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | -0.0 | +0.0 |
| PM E-DRIVE extended to March 2028; e2W incentive cut to Rs 5,000 (`EV_PM_EDRIVE_EXT`) | occurred | 1.00 | +0.5% | +0.5% | +0.4 | +0.0 | +0.0 | +0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +0.4% | +0.4% | +0.7 | -0.0 | -0.1 | -0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.0% | -0.4% | -0.8 | -0.1 | -0.0 | -0.0 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.4% | -0.4% | +0.0 | +0.0 | -0.3 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | +0.3% | +0.3% | +0.0 | +0.0 | +0.2 | +0.1 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -1.3% | -0.3% | +0.0 | -0.9 | -0.5 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → TIINDIA | -1.96% | -1.96% |
| 1 | EV_CAFE3_NOTIFIED ⇒ P_EV_POLICY → TIINDIA | +1.20% | +1.20% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → TIINDIA | -1.06% | -1.06% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → TIINDIA | -0.80% | -0.80% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → TIINDIA | -0.71% | -0.71% |
| 1 | EV_CHINA_Q3_GDP_AND_MINI_STIMULUS ⇒ F_USDCNY → TIINDIA | +0.68% | +0.68% |
| 1 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_STEEL_INDIA → TIINDIA | -0.56% | -0.56% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → TIINDIA | -0.49% | -0.49% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → TIINDIA | +0.47% | +0.47% |
| 1 | EV_PM_EDRIVE_EXT ⇒ P_EV_POLICY → TIINDIA | +0.45% | +0.45% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TIINDIA | -0.80% | -0.32% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → TIINDIA | -0.56% | -0.31% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → TIINDIA | +0.32% | +0.29% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_REPO_IN → TIINDIA | +0.29% | +0.29% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_USDCNY → TIINDIA | -0.26% | -0.26% |

## Analyst profile (agent research, sourced)
# TIINDIA - Tube Investments of India Ltd. (as of 2026-11-05)

## Business
Tube Investments is a Murugappa-group engineering company whose consolidated numbers are dominated by its majority holding in CG Power. In Q1 FY27 consolidated revenue was Rs 6,215 cr, of which CG Power contributed roughly Rs 3,281 cr and the standalone engineering and mobility businesses Rs 2,366 cr (tubes, chains, car door frames, strips, bicycles). It also owns Shanthi Gears, TI Clean Mobility (EV; Rs 147 cr loss in Q1), an early-stage semiconductor venture (Rs 50 cr loss) and a 76.24% stake in Orange Koi. Net profit attributable to TII shareholders (~Rs 170 cr by one source) is far lower than consolidated PAT (Rs 294 cr) because of ~Rs 124 cr of minorities, mostly in CG Power.

## What moves the stock (ranked)
1. **CG Power** (holding link 0.5 per +1%): CG Power's stake is worth ~Rs 71k cr (56% of Rs 1.27 lakh cr) versus TII's Rs 43.6k cr market cap, so TII trades at a deep discount and the rest of the business is valued below zero. The empirical beta of TII on CG, controlling for the Nifty, is only 0.31 over three years; the link weight blends this with the structural 1.0. All CG-specific drivers (grid capex, data centres, copper, CRGO) reach TII through this link and are not duplicated.
2. **Steel and standalone margins** (F_STEEL_INDIA -1.4): standalone EBITDA margin fell 194bp to 10.39% in Q1; management says it will recover inflation over coming quarters.
3. **EV and semiconductor losses** (P_EV_POLICY +1.5): Rs 250 cr was injected into TI Clean Mobility on 2026-09-29; losses are the main drag on conglomerate value.
4. **Auto and rail volumes** (+1.4, +0.4) and private capex (+0.8).
5. **Rates and China** (-0.8; USD/CNY -1.5, shrunk from an empirical -7.24, t -3.0).

## Worked chains
- **AI-capex worry (ABB's parent fell on AI concerns on 2026-10-20) -> sentiment on data-centre electrification names (1st) -> CG Power de-rates (2nd) -> TII's holding value falls by roughly half of CG's move (3rd) -> TII drops while its own engineering orders are unchanged (4th).**
- **Brent up -> India CPI up (2nd) -> RBI hikes (3rd) -> equity multiples compress on long-duration names like TII (P/E 70x) (4th).**
- **China steel exports up -> Indian steel prices fall (2nd) -> TII's tube/strip input cost falls but price pass-through falls too (3rd) -> margin improves temporarily (4th).**
- **EV policy support -> TICM volumes (2nd) -> operating loss narrows (3rd) -> less need for capital infusions from the parent (4th).**

## Current situation
The stock hit a 52-week low on 2026-11-01 (Rs 2,128) and is down 25% in 12 months despite CG Power's strong Q2 (PAT +44%, order book Rs 23.6k cr). Q2 results are pending. The market is capitalising TII at a large discount to the CG stake alone, which implies skepticism about EV/semiconductor spending and the standalone margin.

## Upcoming
Q2 FY27 results (Nov, date unconfirmed), capital calls for new ventures, Q3 results (Feb 2027). There is no announced holding-company restructuring.

## Bull and bear
Bull: CG Power compounding, standalone margin recovery, narrowing discount. Bear: CG de-rating, EV/semiconductor burn, steel inflation.

Confidence: low (TII's exact CG stake and the standalone value split are estimated).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.