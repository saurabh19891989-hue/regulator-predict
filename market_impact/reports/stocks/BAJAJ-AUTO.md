# BAJAJ-AUTO — Bajaj Auto Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +1.9%** (rank 82 / 71 of 200 for 3m / 12m); beta 1.12
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.0%): 3 months 53%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.6% … P90 +7.6%; plausible 12m relative-return range incl. stock-specific noise: -34.1% … +29.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.7 pp (model impact +1.4% beta-adjusted vs realised market-adjusted move -1.9%); forward event exposure +4.7% (3m +2.0%; half assumed priced); company-specific events +0.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.32 | +0.00 | +3.28 | +0.60 | +0.44 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -2.06 | -1.50 | -0.56 | +0.00 | +0.00 | — |
| Competitive intensity in Indian two-wheelers/EV two-wheelers (`NEW_2W_COMPETITIVE_INTENSITY`) | +1 = price/share war episode | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.69 | +0.00 | +1.92 | +0.02 | -0.24 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.57 | +1.50 | +0.00 | +0.07 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.50 | +2.00 | -0.08 | -0.21 | -0.21 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.48 | +0.00 | +0.11 | -1.62 | +0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.31 | +0.00 | -1.15 | -0.14 | -0.02 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.07 | +0.00 | -0.72 | -0.44 | +0.09 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +0.99 | +1.00 | +0.00 | -0.01 | +0.00 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -0.98 | +0.00 | -0.90 | -0.12 | +0.03 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +0.96 | +0.80 | +0.32 | -0.00 | -0.16 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +3.2% | +3.2% | +2.5 | +1.5 | +0.0 | -0.8 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | +0.1 | -2.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.2% | -1.2% | -0.4 | -0.6 | -0.2 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | +0.0 | +0.0 | -0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +0.8% | +0.8% | +0.8 | +0.0 | +0.0 | +0.0 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -3.0% | -0.7% | -2.2 | -0.8 | +0.0 | +0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | -0.0 | +0.1 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +1.5% | +0.5% | +0.8 | +1.0 | +0.1 | -0.5 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.2% | -0.5% | -0.4 | -0.6 | -0.2 | -0.1 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -0.8% | -0.5% | -0.6 | -0.1 | -0.2 | +0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.5% | +0.5% | +0.0 | +0.7 | -0.1 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → BAJAJ-AUTO | +3.96% | +3.96% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → BAJAJ-AUTO | -1.68% | -1.68% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → BAJAJ-AUTO | +1.56% | +1.56% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → BAJAJ-AUTO | -1.50% | -1.50% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → BAJAJ-AUTO | -0.98% | -0.98% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → BAJAJ-AUTO | +0.81% | +0.81% |
| 1 | EV_CAFE3_NOTIFIED ⇒ P_EV_POLICY → BAJAJ-AUTO | +0.80% | +0.80% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → BAJAJ-AUTO | +0.78% | +0.78% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → BAJAJ-AUTO | -0.74% | -0.74% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BAJAJ-AUTO | +2.00% | +0.71% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → BAJAJ-AUTO | -1.20% | -0.70% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → BAJAJ-AUTO | -0.63% | -0.63% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_AUTO_DEMAND_IN → BAJAJ-AUTO | -0.60% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → BAJAJ-AUTO | +1.00% | +0.58% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BAJAJ-AUTO | +2.60% | +0.57% |

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