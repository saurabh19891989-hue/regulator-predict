# VBL — Varun Beverages Ltd.
*NIFTY_NEXT_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.4%** (rank 56 / 46 of 200 for 3m / 12m); beta 1.08
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.3%): 3 months 52%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.2% … P90 +3.0%; plausible 12m relative-return range incl. stock-specific noise: -23.5% … +29.3%
- Decomposition (12m): 0.5 × forward event exposure +3.1% (3m +1.5%; half assumed priced) + 0.5 × company-specific catalysts +0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.4% (beta-adjusted) vs a realised market-adjusted move of -22.2% — gap +22.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.37 | +3.00 | +0.31 | +0.09 | -0.03 | — |
| Soft-drink price competition intensity (Coca-Cola, Campa, regional) (`NEW_CSD_PRICE_COMPETITION`) | +1 = materially sharper discounting/ad spend in carbonated soft drinks | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Summer temperature vs normal (`NEW_SUMMER_TEMPERATURE`) | +1 = season ~1C hotter than normal in Mar-Jun | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.48 | +1.50 | +0.00 | -0.03 | +0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.18 | +1.20 | +0.00 | -0.05 | +0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.17 | +0.00 | -0.53 | -0.49 | -0.15 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.03 | +1.00 | +0.02 | +0.01 | +0.01 | — |
| FSSAI / packaged-food regulation intensity (`NEW_FOOD_SAFETY_REG`) | +1 = materially stricter packaged-food labelling/HFSS/online-sale rules | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.82 | -0.40 | -0.33 | -0.08 | -0.01 | +0.0% |
| Sugar price (`F_SUGAR`) | +10% sugar | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | +27.8% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.77 | -0.70 | -0.05 | -0.01 | -0.01 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.67 | +0.00 | +0.77 | -0.08 | -0.02 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.61 | +0.00 | +0.43 | -0.02 | +0.20 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -0.60 | -0.60 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | -0.0 | -0.0 | -0.0 |
| Sugar supply shock: 2025-26 output cut to ~306 lakh t, retail sugar at record, first duty-free raw sugar imports in a decade (`EV_SUGAR_SHORTFALL26`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.6% | +1.3% | +2.5 | +0.1 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.7 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.5 | +0.0 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.4% | +0.7% | +0.5 | +0.6 | +0.2 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.9 | +0.2 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.5% | -0.6% | -0.9 | -1.2 | -0.4 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.5% | +0.5% | +0.5 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.0% | -0.5% | +0.0 | -2.0 | -0.0 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -2.6% | -0.5% | -2.5 | -0.1 | -0.1 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.4% | -0.4% | +0.0 | -0.4 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VBL | +2.50% | +1.25% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → VBL | -0.70% | -0.29% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → VBL | +0.52% | +0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → VBL | -1.50% | -0.27% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → VBL | +0.36% | +0.25% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → VBL | -0.96% | -0.24% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → VBL | -0.96% | -0.24% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → VBL | -0.93% | -0.23% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → VBL | -0.88% | -0.22% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → VBL | +0.36% | +0.20% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → VBL | -0.70% | -0.19% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → VBL | +0.27% | +0.18% |
| 1 | EV_GST_RATE_CHANGE_APR27 ⇒ P_GST_CONSUMPTION → VBL | +0.60% | +0.18% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → VBL | +0.50% | +0.17% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → VBL | -0.28% | -0.17% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_SUGAR → VBL | +2.78 | observed | -2.23% |
| 1 | F_FPI_FLOWS → VBL | -1.60 | events | -1.60% |
| 1 | F_REPO_IN → VBL | +1.00 | events | -0.70% |
| 1 | F_ALUMINIUM → VBL | -1.96 | observed | +0.39% |
| 1 | F_URBAN_DEMAND → VBL | +0.20 | events | +0.30% |
| 1 | F_RURAL_DEMAND → VBL | -0.25 | events | -0.30% |
| 1 | F_USDINR → VBL | -0.37 | observed | +0.07% |
| 2 | F_DXY → C_AFRICA_LATAM → VBL | +0.74 | observed | -0.07% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → VBL | +0.40 | events | -0.05% |
| 1 | F_BRENT → VBL | +0.00 | observed | -0.00% |
| 2 | F_BRENT → F_CHEM_FEEDSTOCK → VBL | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Capacity commissioning at new plants in India/Africa to support 2027 season | capex | 0.60 | +1.0% | +0.60% |
| 2027-02 | Q4 CY26 / FY (Dec-26) results; seasonally weakest quarter, key for margin outlook | results | 0.90 | +0.0% | +0.00% |
| 2027-04 | Start of peak season (Q1 CY27): volume growth and summer weather determine FY27 earnings *(review: [DIRECTOR_CE] RT_N50_A: non-event; symmetric range)* | guidance | 1.00 | +0.0% | +0.00% |
| 2027-06 | Launch/progress of planned alcohol business (The Core, 2026-09-21: VBL 'wants to build an alcohol business'); regulatory licensing required | other | 0.30 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# VBL (Varun Beverages Ltd.) - company profile as of 2026-11-05

## Business
Varun Beverages is a PepsiCo franchisee that bottles and distributes Pepsi, 7UP, Mirinda, Mountain Dew, Sting, Tropicana, Gatorade and Aquafina in India and in Nepal, Sri Lanka, Morocco, Zambia, Zimbabwe, DRC and South Africa. It reports on a calendar year, and sales are strongly seasonal: Rs 5,996 cr in the June 2026 quarter against Rs 2,135 cr in the December 2025 quarter (screener.in pack, 2026-11-05). TTM sales are Rs 16,454 cr with EBITDA Rs 4,294 cr (26%) and PAT Rs 3,032 cr. The company is almost debt free; the equity trades at 48.5x earnings and 7.8x book, with promoters at 59.43% and FIIs shrinking from 19.5% to 17.5% in two quarters.

## What moves the stock (ranked)
1. **Volume growth, driven by weather and capacity.** A hotter-than-normal Mar-Jun season is worth about +3 equity points per degree (65% of sales fall in the first half); the 2027 season starts in about four months.
2. **Sugar and PET resin.** Sugar is ~14% and PET ~20% of costs (model estimates). Sugar is +27.8% since 1 June 2026 and the September-quarter OPM fell to 24% from 26%. PET follows crude (Brent +15% in 3 months, +50% in 12).
3. **Price points and competition.** Rs 10 and Rs 20 packs give limited pass-through; Coca-Cola, Campa and regional brands compete on price.
4. **Africa and PepsiCo franchise.** About 18% of sales with higher growth; political and FX tail; PepsiCo concentrate priced in USD.
5. **Valuation, rates and flows.** At 48.5x earnings, the stock behaves like a long-duration asset.

## Transmission examples
- **Sugar price surge -> VBL input cost -> margin.** Order 1: sugar +28% since June (an Indian monsoon/ethanol story, see `P_SUGAR_ETHANOL`); order 2: Rs 170 cr per +10% = 4% of EBITDA; order 3: price cuts in promo packs are paused and pack sizes (ml) reduced; order 4: volume elasticity ~-0.4 on 3-5% effective price rise, softening growth into the 2027 peak season. Net ~-2% equity from the current run-up if not recovered.
- **Middle East escalation -> Brent up -> PX/PET up -> VBL packaging and freight cost up.** Brent +10% adds about 5% to PET; with diesel it is ~3% of EBITDA. A second route: Brent up -> USD/INR up -> concentrate and resin cost in rupees up; Africa earnings partly offset.
- **Hot summer (El Nino-type) -> volumes -> operating leverage.** A +1C season lifts volumes 3-4% on ~40% incremental margins, a ~5% EBITDA gain; sugar and PET inflation lessen but do not erase it.
- **GST rate cut on beverages -> consumer price down -> volumes.** From 40% to 18% would cut retail prices ~15%; VBL could keep part as margin. Probability low (57th Council made no rate cuts).
- **Africa FX shock (ZMW/ZWL/CDF) -> African margins -> group.** Local currency weakness translates to lower INR earnings and raises USD concentrate cost.

## Empirical cross-check
Only USD/INR is significant (+4.03/SSU, t=+2.4; beta 1.29) and it contradicts the cost mechanism. It likely reflects market-beta and flow co-movement rather than a business link. It is carried at a low-confidence -0.2 with a range up to +2. Coal (-2.45, t=-1.3) and silver (+1.12, t=+1.6) have no fundamental link.

## Current situation
Q3 CY26 (reported 2026-10-30): the screener pack shows sales Rs 3,822 cr (+25%), PAT Rs 659 cr (+14%) and OPM 24%; press headlines state revenue +33% and PAT Rs 828 cr. The difference is not reconciled here (consolidation basis or restated figures). The market reaction was -3% to -4% on margin contraction despite volume strength; BofA reiterated Buy with a Rs 550 target on 2026-11-04. On 2026-09-24 VBL signed an exclusive distribution pact with Mondelez in Zimbabwe, and its COO resigned. A report on 2026-09-21 says VBL intends to build an alcohol business.

## Upcoming events
Q4 CY26 results (February 2027), start of the 2027 summer season, capacity additions, alcohol-business steps (licences), and further leadership changes.

## Bull case
A hot 2027 summer plus sugar and aluminium relief returns EBITDA margin to 27%; Africa scales; the stock earns a premium for 15-20% earnings growth. Rs 550 (BofA) would be +26%.

## Bear case
Sugar stays high, a wet summer cuts volume, price competition erodes margin to 23-24%, and a 48x multiple compresses to 38x: -20% to -25%.

## Uncertainties
Cost shares and revenue mix are model estimates; reported-number basis for Q3 is unreconciled; no filings were fetched beyond the screener pack and headlines.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.