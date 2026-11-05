# VBL — Varun Beverages Ltd.
*NIFTY_NEXT_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.5%**, **12 months +1.7%** (rank 85 / 74 of 200 for 3m / 12m); beta 1.08
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.3%): 3 months 52%, 12 months 68%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.5% … P90 +4.6%; plausible 12m relative-return range incl. stock-specific noise: -19.9% … +36.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.2 pp (model impact +0.3% beta-adjusted vs realised market-adjusted move -22.2%); forward event exposure +4.3% (3m +2.3%; half assumed priced); company-specific events +1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.43 | +3.00 | +0.31 | +0.14 | -0.02 | — |
| Soft-drink price competition intensity (Coca-Cola, Campa, regional) (`NEW_CSD_PRICE_COMPETITION`) | +1 = materially sharper discounting/ad spend in carbonated soft drinks | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Summer temperature vs normal (`NEW_SUMMER_TEMPERATURE`) | +1 = season ~1C hotter than normal in Mar-Jun | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.80 | +0.00 | -0.53 | -0.89 | -0.39 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.47 | +1.50 | +0.00 | -0.03 | -0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.16 | +1.20 | +0.00 | -0.05 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.09 | +0.00 | -1.09 | +0.02 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.04 | +1.00 | +0.02 | +0.01 | +0.01 | — |
| FSSAI / packaged-food regulation intensity (`NEW_FOOD_SAFETY_REG`) | +1 = materially stricter packaged-food labelling/HFSS/online-sale rules | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.90 | -0.40 | -0.34 | -0.14 | -0.03 | +0.0% |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.83 | +0.00 | +0.26 | +0.41 | +0.16 | — |
| Sugar price (`F_SUGAR`) | +10% sugar | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | +27.8% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.77 | -0.70 | -0.05 | -0.01 | -0.01 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.72 | +0.00 | -0.40 | -0.26 | -0.07 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.8% | -4.8% | -2.0 | -1.8 | -0.9 | -0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | -0.1 | -0.0 | -0.0 |
| Sugar supply shock: 2025-26 output cut to ~306 lakh t, retail sugar at record, first duty-free raw sugar imports in a decade (`EV_SUGAR_SHORTFALL26`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.4 | +0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.6% | +1.3% | +2.5 | +0.1 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.1% | -1.1% | -1.0 | -1.4 | -0.6 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.8% | +1.0% | +0.6 | +0.8 | +0.3 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.5 | +0.0 | -0.3 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -2.9% | -0.8% | +0.0 | -2.5 | -0.3 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.7 | -0.1 | -0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.3 | +0.3 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.7 | -0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_SUGAR_SHORTFALL26 ⇒ F_SUGAR → VBL | -2.24% | -2.24% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → VBL | -2.20% | -2.20% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → VBL | -1.98% | -1.98% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VBL | +2.50% | +1.25% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → VBL | -1.01% | -1.01% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → VBL | -0.93% | -0.93% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → VBL | -0.70% | -0.70% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → VBL | +0.50% | +0.50% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → VBL | -1.49% | -0.42% |
| 1 | EV_ETHANOL_ESY27_TENDER ⇒ F_SUGAR → VBL | +0.40% | +0.40% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → VBL | +0.39% | +0.39% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → VBL | -0.36% | -0.36% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → VBL | -1.00% | -0.36% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → VBL | +0.60% | +0.35% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_RURAL_DEMAND → VBL | -0.34% | -0.34% |

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