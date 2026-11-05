# TMPV — Tata Motors Passenger Vehicles Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.0%**, **12 months -0.2%** (rank 97 / 115 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.8%): 3 months 50%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.0% … P90 +5.4%; plausible 12m relative-return range incl. stock-specific noise: -30.6% … +32.3%
- Decomposition (12m): 0.5 × forward event exposure -0.6% (3m -0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +14.7% (beta-adjusted) vs a realised market-adjusted move of -28.9% — gap +43.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.19 | +0.09 | +0.28 | +0.14 |
| Sector | -0.11 | +0.15 | +0.04 | -0.03 |
| Theme | +0.00 | -0.13 | -0.13 | -0.08 |
| Geopolitics | +0.00 | +0.19 | +0.19 | +0.18 |
| Company catalysts | +0.17 | +0.08 | +0.26 | +0.23 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.68 | -0.31 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.18** | **+0.04** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US tariff on UK/EU-built passenger vehicles (`NEW_US_TARIFF_UK_EU_AUTOS`) | +10pp tariff on UK/EU autos entering the US | -8.00 | -8.00 | +0.00 | +0.00 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.03 | +1.50 | +1.23 | +0.25 | +0.05 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +2.63 | +2.50 | +0.18 | +0.00 | -0.05 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +2.36 | +2.50 | -0.07 | -0.06 | +0.00 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.86 | +2.00 | -0.04 | -0.06 | -0.04 | -1.1% |
| Aluminium price (`F_ALUMINIUM`) | +10% aluminium | -1.70 | -1.70 | +0.00 | +0.00 | +0.00 | -19.6% |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.51 | +0.00 | -1.50 | -0.01 | +0.00 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | +20.6% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.36 | +0.00 | +1.44 | -0.03 | -0.05 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.28 | +0.00 | -1.15 | -0.26 | +0.13 | — |
| Copper price (`F_COPPER`) | +10% copper | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | -2.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +3.6% | +3.6% | +3.6 | +0.0 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +3.2% | +3.2% | +3.0 | +0.2 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -3.1% | -3.1% | -3.1 | +0.0 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -7.7% | -1.9% | -7.5 | -0.3 | +0.4 | -0.2 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +1.6% | +1.6% | +1.7 | -0.1 | -0.1 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.9% | -0.9% | -0.5 | -0.3 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.8 | -0.0 | +0.0 |
| PM E-DRIVE extended to March 2028; e2W incentive cut to Rs 5,000 (`EV_PM_EDRIVE_EXT`) | occurred | 1.00 | +0.7% | +0.7% | +0.8 | -0.0 | -0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | +0.0 | +0.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.5 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | +2.2% | +0.5% | +0.0 | +1.4 | +0.6 | +0.1 |
| India-EU FTA signed at ceremony (planned 16 Dec 2026) (`EV_INDIA_EU_FTA_SIGNED`) | scheduled | 0.92 | +0.6% | +0.5% | +0.6 | -0.0 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → TMPV | -7.50% | -1.88% |
| 1 | EV_INDIA_EU_FTA_SIGNED ⇒ F_EU_GDP → TMPV | +0.60% | +0.55% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → TMPV | +2.16% | +0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → TMPV | +2.60% | +0.47% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → TMPV | -0.92% | -0.46% |
| 1 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → TMPV | +1.50% | +0.38% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TMPV | -1.44% | -0.36% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ P_PLI → TMPV | +0.36% | +0.29% |
| 1 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ F_SEMICONDUCTOR_SUPPLY → TMPV | -0.90% | -0.22% |
| 1 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_STEEL_GLOBAL → TMPV | -0.45% | -0.22% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → TMPV | +0.41% | +0.22% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → TMPV | -0.48% | -0.22% |
| 1 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → TMPV | +0.60% | +0.21% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TMPV | -0.50% | -0.21% |
| 2 | EV_US_CHINA_TRUCE_EXTENDED ⇒ C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → TMPV | +0.29% | +0.21% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_ALUMINIUM → TMPV | -1.96 | observed | +3.33% |
| 1 | F_US_GDP → TMPV | +1.20 | events | +3.00% |
| 1 | P_EV_POLICY → TMPV | +1.10 | events | +2.75% |
| 1 | F_AUTO_DEMAND_IN → TMPV | +0.50 | director_override | +1.50% |
| 1 | F_STEEL_GLOBAL → TMPV | +0.50 | director_override | -0.75% |
| 1 | F_USDINR → TMPV | -0.37 | observed | -0.74% |
| 1 | F_REPO_IN → TMPV | +1.00 | events | -0.50% |
| 1 | F_EU_GDP → TMPV | +0.22 | events | +0.44% |
| 1 | F_COPPER → TMPV | -0.24 | observed | +0.28% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → TMPV | -0.30 | events | +0.22% |
| 1 | F_CHINA_GDP → TMPV | +0.30 | events | +0.18% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → TMPV | -0.10 | events | +0.10% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results and analyst call (JLR Q2 wholesales +24.5%, retail -7.5%, commodity headwind flagged in August); exact date unverified | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | Possible UK duties on Chinese EVs / EU 'Made in Europe' scheme link | regulatory | 0.40 | +1.2% | +0.50% |
| 2026-12 | US-India trade agreement or change in US tariffs on UK-built vehicles | regulatory | 0.30 | -0.5% | -0.15% |
| 2027-01 | JLR Q3 wholesale update and Jaguar Type 01 launch progress (Enterprise Missions GBP 1.7bn savings details with Q2) | guidance | 0.80 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# TMPV - Tata Motors Passenger Vehicles Ltd. (as of 2026-11-05)

## Business
TMPV is the post-demerger passenger-vehicle company of the Tata group. About two-thirds of its Rs 3.44 lakh cr revenue comes from Jaguar Land Rover (Range Rover, Range Rover Sport and Defender are 81% of wholesales), the rest from the India PV and EV business (Nexon, Punch, Harrier, Curvv, ~14.3% share in Q1 FY27, EVs 20-23% of mix). The key feature for any exposure model is the thin and volatile margin: TTM EBITDA margin is 4.9%, Q1 FY27 consolidated EBIT margin 2.4% and JLR EBIT 2.8%. A 1% change in sales-equivalent cost is therefore ~20% of EBITDA. Net debt was ~Rs 42,000 cr at Q1.

## What moves the stock (ranked, % equity value per standard shock)
1. **US tariffs on UK-built vehicles** (new node, -8 per +10pp, conditional): the single largest tail risk.
2. **Metals** (aluminium -3.4 per +10%, global steel -3.0, copper -1.2): management told investors in August that commodity pressure would persist in the September quarter; steel is +20.6% since June while aluminium is -19.6%.
3. **JLR demand by region** (US +2.5, UK/Europe +2.0, China +0.6 per +1pp growth): JLR wholesale rose 24.5% in Q2 FY27 but retail fell 7.5%; China fell 46% to 6,100 after local production ended.
4. **Indian PV volumes** (F_AUTO_DEMAND_IN +3.0 per +10%) with EBITDA margin ~4% and gearing 4.5x; share gains and the EV lead add (P_EV_POLICY +2.5, P_PLI +1.2).
5. **FX** (USD/INR +2.0 per +3%): JLR earnings translate into INR; pack empirical +2.78 (t 1.2) agrees.
6. **Brent** (input -1.2 and EV-substitution +1.0, net ~ -0.2): fuel prices push Indian buyers toward EVs where Tata leads.
7. **Rates** (-0.5) and **supply shocks** (chips/suppliers, -3.0).

## Worked chains
- **Middle East war -> Brent up (1st) -> JLR Middle East disruption and plastics/freight costs (2nd) -> JLR margin and incentives (VME 7.1% vs 4.1%) (3rd) -> group EBITDA -5-10% given 2.4% EBIT margin (4th).**
- **Brent up -> India petrol/diesel up (2nd) -> EV demand beats supply (Tata: EV demand 3x supply headline) (3rd) -> mix up to ~23-25% EV with PLI accruals (4th) -> India margin rises from ~4%.**
- **Steel and aluminium up (China exports, duties) -> body and chassis cost up (2nd) -> price hikes of up to Rs 25,000 in India but JLR slower to reprice (3rd) -> margin gap persists (4th).**
- **Tariff or US-India deal change -> JLR US volume/pricing (2nd) -> UK plants' utilisation and Stellantis/Defender US plans (3rd) -> JLR EBIT 2.8% -> negative (4th).**
- **Tata Sons leadership change (Chandrasekaran stepping down, Aug 2026) -> group risk premium (2nd) -> governance and capital-allocation concerns across TMPV/TMCV/Tata Capital (3rd).**

## Current situation
Q1 FY27: revenue Rs 95,799 cr (+9%), EBITDA -24%, PAT -80% to Rs 775 cr on weak JLR and commodities. India business grew 65% in revenue. JLR free cash flow was -GBP ~1bn in the quarter. Q2 operational update showed JLR wholesales +24.5% (82,400) but retail -7.5%. Q2 results are due in November (date unverified); the company already warned of a heavy commodity hit. The stock is ~15% below its June level and trades near book value, with fundamentals recovery priced uncertainly.

## Upcoming
Q2 FY27 results/call (Nov), UK duty decision on Chinese EVs, RBI December MPC, JLR Q3 wholesales (Jan), Jaguar Type 01 launch and Enterprise Missions savings details.

## Bull and bear
Bull: JLR volume recovery and GBP 1.7bn savings, commodity easing, EV leadership and share gains, UK protection against Chinese EVs. Bear: US tariffs, JLR retail weakness and incentives, steel inflation, execution on Jaguar relaunch, cash burn.

Confidence: low (high operating leverage amplifies every estimate error; Q2 results still pending).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.