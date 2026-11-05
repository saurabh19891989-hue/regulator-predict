# BAJAJ-AUTO — Bajaj Auto Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.5%**, **12 months -0.8%** (rank 153 / 153 of 200 for 3m / 12m); beta 1.12
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.0%): 3 months 48%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.6% … P90 +3.7%; plausible 12m relative-return range incl. stock-specific noise: -25.1% … +25.3%
- Decomposition (12m): 0.5 × forward event exposure -1.4% (3m -0.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +4.5% (beta-adjusted) vs a realised market-adjusted move of -1.9% — gap +6.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -0.15 | +0.12 | -0.02 | -0.11 |
| Sector | -0.33 | +0.19 | -0.14 | -0.07 |
| Theme | +0.00 | -0.08 | -0.08 | -0.06 |
| Geopolitics | +0.07 | +0.14 | +0.22 | +0.16 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.64 | -0.29 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.82** | **-0.47** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.15 | +0.00 | +3.28 | +0.60 | +0.27 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -2.06 | -1.50 | -0.56 | +0.00 | +0.00 | — |
| Competitive intensity in Indian two-wheelers/EV two-wheelers (`NEW_2W_COMPETITIVE_INTENSITY`) | +1 = price/share war episode | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.85 | +0.00 | +1.92 | +0.02 | -0.09 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.62 | +2.00 | -0.08 | -0.15 | -0.14 | -1.1% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.57 | +1.50 | +0.00 | +0.07 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.33 | +0.00 | -1.15 | -0.15 | -0.04 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.21 | +0.00 | +1.31 | +0.04 | -0.14 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +0.99 | +1.00 | +0.00 | -0.01 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +0.92 | +0.80 | +0.21 | +0.01 | -0.10 | +0.0% |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.83 | +0.00 | -0.72 | -0.19 | +0.08 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.2% | -1.2% | -0.4 | -0.6 | -0.2 | -0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | -0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | +0.1 | -1.2 | +0.2 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +0.8% | +0.8% | +0.8 | +0.0 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | +0.0 | +0.0 | +0.0 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -3.0% | -0.7% | -2.2 | -0.8 | +0.0 | +0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | -0.0 | +0.1 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.5% | +0.5% | +0.0 | +0.6 | -0.0 | -0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.2% | -0.5% | -0.4 | -0.6 | -0.2 | -0.1 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -0.9% | -0.4% | -1.0 | +0.0 | +0.0 | -0.0 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +0.4% | +0.4% | +0.4 | +0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → BAJAJ-AUTO | -1.04% | -0.57% |
| 1 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → BAJAJ-AUTO | -2.25% | -0.56% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → BAJAJ-AUTO | +1.00% | +0.55% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BAJAJ-AUTO | -0.96% | -0.48% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BAJAJ-AUTO | +2.60% | +0.47% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → BAJAJ-AUTO | -0.92% | -0.46% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BAJAJ-AUTO | +1.76% | +0.44% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → BAJAJ-AUTO | -1.20% | -0.30% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → BAJAJ-AUTO | -2.00% | -0.30% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → BAJAJ-AUTO | +0.39% | +0.28% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → BAJAJ-AUTO | -0.96% | -0.24% |
| 1 | EV_INDIA_EU_FTA_SIGNED ⇒ F_EU_GDP → BAJAJ-AUTO | +0.24% | +0.22% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → BAJAJ-AUTO | +0.40% | +0.22% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → BAJAJ-AUTO | +0.39% | +0.22% |
| 1 | EV_INDIA_US_TALKS_COLLAPSE ⇒ P_US_TARIFF_INDIA → BAJAJ-AUTO | -1.20% | -0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_AUTO_DEMAND_IN → BAJAJ-AUTO | +0.50 | director_override | +2.00% |
| 1 | F_GSEC_10Y_IN → BAJAJ-AUTO | +1.55 | director_override | -1.86% |
| 1 | P_EV_POLICY → BAJAJ-AUTO | +1.10 | events | +1.10% |
| 1 | C_MIDEAST_CONFLICT → BAJAJ-AUTO | +1.00 | events | -1.00% |
| 1 | F_STEEL_INDIA → BAJAJ-AUTO | +1.35 | events | -0.94% |
| 1 | F_ALUMINIUM → BAJAJ-AUTO | -1.96 | observed | +0.78% |
| 1 | F_USDINR → BAJAJ-AUTO | -0.37 | observed | -0.74% |
| 1 | P_US_TARIFF_INDIA → BAJAJ-AUTO | -0.60 | events | +0.48% |
| 1 | F_EU_GDP → BAJAJ-AUTO | +0.22 | events | +0.18% |
| 2 | F_DXY → C_AFRICA_LATAM → BAJAJ-AUTO | +0.74 | observed | -0.11% |
| 2 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → BAJAJ-AUTO | -0.10 | events | +0.07% |
| 1 | F_BRENT → BAJAJ-AUTO | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12-01 | November sales print (exports and domestic) | other | 1.00 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | India-US trade deal or further tariff changes affecting KTM/Triumph exports | regulatory | 0.30 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Bajaj Auto Ltd. (BAJAJ-AUTO) — Market Impact profile, 2026-11-05

## Business
Bajaj Auto makes Pulsar, Platina, Dominar and Chetak motorcycles/scooters and three-wheelers, and controls KTM/Husqvarna (through Pierer Bajaj AG, BMAG) while co-producing Triumph. Roughly half of standalone revenue is exports to Africa, Latin America, ASEAN, the Middle East and Europe, which makes it the group most exposed to emerging-market FX and commodity-exporter incomes. In Q2 FY27 (Sep 2026) standalone revenue was Rs 20,003 cr (+34%) and profit Rs 3,354 cr (+35%); consolidated sales were Rs 25,126 cr with a 19% operating margin. The company holds a large investment book, so net debt is not an issue at the standalone level; interest cost has risen with KTM debt.

## What moves the stock (ranked)
1. **Exports (C_AFRICA_LATAM +0.6, F_BRENT +0.8, F_USDINR +2.0).** The pack shows significant positive Brent (t=2.2): oil-exporter incomes buy Bajaj vehicles.
2. **Domestic 2W/3W demand (+4.0 per +10%).** September domestic sales -12% triggered a 6.5-9% one-day crash on 1 Oct 2026; October rebounded.
3. **Discount rate (G-sec -1.2) and rate hikes.** Bajaj Auto was among top losers on 7 Oct after RBI's hike.
4. **Cost overhang (steel -0.7, aluminium -0.4, rare earths -1.5)** and competition (-2.0).
5. **KTM/Europe (+0.8)** and **US tariffs (-0.8).**

## Transmission examples
- **Oil to exports (3 orders).** Brent rallies on Iran/Hormuz risk -> oil-exporting economies (Nigeria, Angola, Colombia) gain FX and income -> import demand for three-wheelers and motorcycles rises -> Bajaj export volumes and USD revenue up. Counter-chain: Brent up -> India petrol/CPI up -> RBI hikes (done 7 Oct) -> domestic 2W demand slows.
- **Rupee chain (3 orders).** USD/INR at 94.5 (+6.5% in 12 months) -> export realisations in INR up -> hedges roll at better rates -> EBITDA margin +50-70bp, partly offset by imported KTM parts.
- **US tariff chain (3-4 orders).** India-US talks stall -> tariff on India-made Triumph/KTM 400s -> US landed price up, dealers cut orders -> Pune/Chakan export mix shifts to other regions -> margin dilution.
- **Rare-earth chain (4 orders).** China restricts magnets -> Chetak motor supply cut -> EV output down -> lost PLI/EV incentives and market share to Ather/Ola -> premium multiple compresses.
- **Group chain.** Bajaj Auto stock moves feed Bajaj Holdings (NAV share ~17%).

## Current situation
Strong Q2: exports surged, revenue crossed Rs 20,000 cr (standalone), JPMorgan upgraded to Overweight and CLSA sees ~29% upside. After the 1 October crash (-18% in a month), the stock has recovered 7% in the last month but is -7.8% over three months. Promoter holding rose to 55.95%. Cost overhang is the near-term worry (steel +20.6% since June).

## Upcoming events
Monthly sales (Dec 1); Q3 results (January); US tariff developments; Budget (1 Feb 2027).

## Bull case
Exports hold above 2.5 lakh/month, INR stays weak, domestic recovers, BMAG turns profitable and Chetak scales. Cheapest valuation (P/E 22) among 2W peers.

## Bear case
Domestic share erosion, African currency shocks, US tariffs, higher steel/rare-earth costs, and RBI tightening. Limits: cost shares and export mix are estimates; KTM debt details not retrieved.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.