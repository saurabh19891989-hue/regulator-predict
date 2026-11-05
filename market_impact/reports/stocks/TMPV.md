# TMPV — Tata Motors Passenger Vehicles Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.0%**, **12 months +6.8%** (rank 20 / 25 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.8%): 3 months 63%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.5% … P90 +14.5%; plausible 12m relative-return range incl. stock-specific noise: -22.6% … +35.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +5.5 pp (model impact +10.9% beta-adjusted vs realised market-adjusted move -28.9%); forward event exposure +4.5% (3m +2.6%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US tariff on UK/EU-built passenger vehicles (`NEW_US_TARIFF_UK_EU_AUTOS`) | +10pp tariff on UK/EU autos entering the US | -8.00 | -8.00 | +0.00 | +0.00 | +0.00 | — |
| Aluminium price (`F_ALUMINIUM`) | +10% aluminium | -3.40 | -3.40 | +0.00 | +0.00 | +0.00 | -19.6% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.09 | +1.50 | +1.23 | +0.29 | +0.07 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | +20.6% |
| US growth (`F_US_GDP`) | +1 pp | +2.63 | +2.50 | +0.18 | +0.01 | -0.06 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +2.30 | +2.50 | -0.07 | -0.09 | -0.03 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.99 | +2.00 | +0.00 | -0.01 | +0.00 | — |
| Copper price (`F_COPPER`) | +10% copper | -1.88 | -1.20 | -0.68 | +0.00 | +0.00 | -2.4% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.80 | +2.00 | -0.04 | -0.09 | -0.07 | -1.1% |
| US dollar index (`F_DXY`) | +3% DXY | +1.77 | +0.00 | +1.21 | +0.53 | +0.02 | +2.2% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.75 | +0.60 | -1.48 | -0.85 | -0.01 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.55 | +0.00 | -1.50 | -0.02 | -0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +7.0% | +7.0% | +7.0 | +0.0 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -6.2% | -6.2% | -6.2 | +0.0 | -0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +3.2% | +3.2% | +3.0 | +0.2 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -7.2% | -1.8% | -7.5 | -0.3 | +0.7 | -0.0 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +1.5% | +1.5% | +1.7 | -0.1 | -0.1 | -0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.4 | -0.0 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +0.8 | +0.5 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | +1.3% | +1.3% | +0.0 | +0.9 | +0.5 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.2 | -1.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.9% | -0.9% | -0.5 | -0.3 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.9 | -0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | +2.8% | +0.8% | +0.0 | +1.8 | +0.9 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → TMPV | +6.66% | +6.66% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_GLOBAL → TMPV | -6.18% | -6.18% |
| 1 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → TMPV | +3.00% | +3.00% |
| 1 | EV_CAFE3_NOTIFIED ⇒ P_EV_POLICY → TMPV | +2.00% | +2.00% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → TMPV | -7.50% | -1.88% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → TMPV | +1.56% | +1.56% |
| 2 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_COKING_COAL → F_STEEL_GLOBAL → TMPV | -1.40% | -1.40% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → TMPV | -1.22% | -1.22% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → TMPV | -0.99% | -0.99% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → TMPV | +0.81% | +0.81% |
| 1 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → TMPV | +3.00% | +0.75% |
| 1 | EV_PM_EDRIVE_EXT ⇒ P_EV_POLICY → TMPV | +0.75% | +0.75% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → TMPV | -0.74% | -0.74% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → TMPV | -0.66% | -0.66% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → TMPV | +2.16% | +0.60% |

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