# TIINDIA — Tube Investments of India Ltd.
*MIDCAP_100 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +1.0%** (rank 67 / 63 of 200 for 3m / 12m); beta 1.06
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.7%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.5% … P90 +5.0%; plausible 12m relative-return range incl. stock-specific noise: -32.0% … +39.7%
- Decomposition (12m): 0.5 × forward event exposure +2.5% (3m +1.3%; half assumed priced) + 0.5 × company-specific catalysts +0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +4.8% (beta-adjusted) vs a realised market-adjusted move of -31.1% — gap +35.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +1.51 | +1.50 | +0.00 | +0.01 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.48 | +0.00 | +1.15 | +0.35 | -0.02 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -1.46 | -1.50 | +0.01 | +0.01 | +0.02 | -1.4% |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.41 | -1.40 | +0.00 | -0.01 | +0.00 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +1.40 | +1.40 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.95 | -0.80 | -0.12 | -0.01 | -0.01 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -0.69 | +0.00 | -0.69 | +0.00 | +0.00 | +20.6% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +0.60 | +0.80 | +0.00 | -0.15 | -0.04 | — |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | -0.56 | +0.00 | -0.56 | +0.00 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.56 | +0.00 | -0.60 | -0.09 | +0.13 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.52 | +0.00 | -0.40 | -0.21 | +0.09 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +0.48 | +0.00 | +0.67 | -0.13 | -0.06 | — |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -0.46 | +0.00 | -0.28 | -0.18 | +0.00 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | +0.42 | +0.00 | +0.28 | +0.14 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | -0.0 | +0.0 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.0% | -1.0% | -0.8 | -0.1 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.5 | -0.3 | +0.1 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | -0.0 | +0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +0.5% | +0.5% | +0.7 | -0.0 | -0.1 | -0.1 |
| PM E-DRIVE extended to March 2028; e2W incentive cut to Rs 5,000 (`EV_PM_EDRIVE_EXT`) | occurred | 1.00 | +0.5% | +0.5% | +0.4 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.0% | -0.4% | -0.8 | -0.1 | -0.0 | -0.0 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | -0.6% | -0.3% | -0.6 | +0.0 | -0.0 | +0.0 |
| RBI MPC Feb 2027 (~5 Feb, just after Budget): hikes 25 bp (`EV_RBI_FEB27_HIKE25`) | scheduled | 0.27 | -1.0% | -0.3% | -0.8 | -0.1 | -0.0 | -0.0 |
| Chinese steel/aluminium export surge floods Asia as China demand stays weak (`EV_CHINA_STEEL_EXPORT_FLOOD`) | risk_scenario | 0.25 | +1.0% | +0.2% | +0.0 | +1.1 | -0.1 | +0.0 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -0.4% | -0.2% | -0.3 | -0.0 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TIINDIA | -0.80% | -0.34% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → TIINDIA | -0.56% | -0.31% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → TIINDIA | -0.80% | -0.22% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → TIINDIA | -0.32% | -0.19% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → TIINDIA | +0.69% | +0.17% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TIINDIA | -0.67% | -0.17% |
| 1 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_USDCNY → TIINDIA | +0.45% | +0.16% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → TIINDIA | -0.80% | -0.14% |
| 2 | EV_US_CHINA_TRUCE_EXTENDED ⇒ C_US_CHINA_DECOUPLING → F_USDCNY → TIINDIA | +0.18% | +0.13% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ C_US_CHINA_DECOUPLING → F_USDCNY → TIINDIA | -0.48% | -0.12% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → TIINDIA | -0.46% | -0.12% |
| 1 | EV_STEEL_SAFEGUARD_EARLY_RELAXATION ⇒ F_STEEL_INDIA → TIINDIA | +0.70% | +0.10% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → TIINDIA | +0.42% | +0.10% |
| 2 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → TIINDIA | -0.21% | -0.10% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → TIINDIA | +0.14% | +0.10% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → TIINDIA | +1.35 | events | -1.89% |
| 1 | P_EV_POLICY → TIINDIA | +1.10 | events | +1.65% |
| 1 | F_REPO_IN → TIINDIA | +1.00 | events | -0.80% |
| 1 | F_AUTO_DEMAND_IN → TIINDIA | +0.50 | director_override | +0.70% |
| 1 | F_USDCNY → TIINDIA | -0.47 | observed | +0.70% |
| 1 | F_USDINR → TIINDIA | -0.37 | observed | -0.11% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → TIINDIA | +0.50 | events | +0.08% |
| 2 | F_CREDIT_SPREADS_IN → F_PRIVATE_CAPEX → TIINDIA | +0.50 | events | -0.05% |
| 2 | T_ENERGY_TRANSITION → F_PRIVATE_CAPEX → TIINDIA | +0.30 | director_override | +0.03% |
| 2 | F_GOVT_CAPEX → F_PRIVATE_CAPEX → TIINDIA | +0.20 | director_override | +0.03% |
| 2 | F_REPO_IN → F_PRIVATE_CAPEX → TIINDIA | +1.00 | events | -0.03% |
| 2 | P_FDI_RULES → F_PRIVATE_CAPEX → TIINDIA | +0.50 | events | +0.02% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (date unverified): CG Power Q2 PAT +44% already public; standalone margin recovery and EV/semiconductor losses are the watch items | results | 0.97 | +0.0% | +0.00% |
| 2026-12 | Further capital infusions into TI Clean Mobility / semiconductor ventures | capex | 0.40 | -1.0% | -0.40% |
| 2027 | Speculative value-unlocking of the holding discount to CG Power (no announcement) | corporate_action | 0.05 | +15.0% | +0.75% |
| 2027-02 | Q3 FY27 results | results | 0.97 | +0.0% | +0.00% |

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