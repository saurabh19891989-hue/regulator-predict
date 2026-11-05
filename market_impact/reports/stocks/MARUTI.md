# MARUTI — Maruti Suzuki India Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.9%**, **12 months +0.3%** (rank 70 / 89 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.4%): 3 months 54%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.3% … P90 +2.5%; plausible 12m relative-return range incl. stock-specific noise: -15.6% … +9.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.6% beta-adjusted vs realised market-adjusted move -7.5%); forward event exposure +1.2% (3m +1.1%; half assumed priced); company-specific events +1.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +7.08 | +4.00 | +2.36 | +0.63 | +0.10 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +5.50 | +5.50 | +0.00 | +0.00 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -2.61 | +0.00 | -2.61 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.28 | +0.00 | +2.64 | -0.22 | -0.14 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -2.09 | +0.00 | -0.87 | -0.80 | -0.43 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.05 | +0.00 | -1.10 | -1.12 | +0.17 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -2.02 | -2.00 | +0.00 | -0.01 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.86 | +1.30 | +0.90 | -0.17 | -0.17 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.66 | -0.60 | -0.78 | -0.06 | -0.22 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.53 | -1.20 | -0.05 | -0.18 | -0.10 | +0.0% |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.49 | +0.00 | -0.96 | -0.83 | +0.30 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.44 | +0.00 | -0.10 | -0.74 | -0.59 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.34 | -0.90 | -0.32 | -0.08 | -0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.4 | -1.4 | +0.2 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.7% | +1.5% | +2.2 | +0.1 | +0.3 | +0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -0.9 | -0.3 | -0.1 | -0.0 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | -1.2% | -1.2% | -1.2 | +0.0 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.4% | -1.1% | -3.4 | -0.2 | -0.5 | -0.3 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | +0.0 | +0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.4 | -0.4 | -0.2 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.6 | +0.1 | +0.2 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | +0.0 | -0.0 | -0.0 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -3.2% | -0.8% | -0.9 | -2.8 | +0.3 | +0.2 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | -2.1% | -0.7% | +0.0 | -0.9 | -0.8 | -0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → MARUTI | +1.56% | +0.86% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → MARUTI | -2.64% | -0.66% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MARUTI | -2.64% | -0.66% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MARUTI | +2.16% | +0.54% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → MARUTI | -0.80% | -0.44% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MARUTI | -0.90% | -0.38% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MARUTI | +0.60% | +0.33% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → MARUTI | +0.39% | +0.27% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → MARUTI | -5.40% | -0.27% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → MARUTI | +0.38% | +0.26% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → MARUTI | -1.04% | -0.26% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → MARUTI | +0.99% | +0.25% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MARUTI | -0.90% | -0.24% |
| 1 | EV_GST_RATE_CHANGE_APR27 ⇒ P_GST_CONSUMPTION → MARUTI | +0.80% | +0.24% |
| 1 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ F_SEMICONDUCTOR_SUPPLY → MARUTI | -0.90% | -0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → MARUTI | +1.35 | events | -2.70% |
| 1 | F_ALUMINIUM → MARUTI | -1.96 | observed | +0.98% |
| 1 | F_REPO_IN → MARUTI | +1.00 | events | -0.90% |
| 1 | P_EV_POLICY → MARUTI | +1.10 | events | -0.88% |
| 1 | C_MIDEAST_CONFLICT → MARUTI | +1.00 | events | -0.60% |
| 1 | F_AUTO_DEMAND_IN → MARUTI | -0.10 | events | -0.55% |
| 1 | F_RURAL_DEMAND → MARUTI | -0.25 | events | -0.33% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MARUTI | -0.30 | events | +0.22% |
| 1 | F_USDINR → MARUTI | -0.37 | observed | +0.11% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → MARUTI | -0.10 | events | +0.10% |
| 1 | F_COPPER → MARUTI | -0.24 | observed | +0.07% |
| 2 | F_CHINA_GDP → F_RUBBER → MARUTI | +0.30 | events | -0.04% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-08 | Diwali festive peak (retail conversion of 2.45 lakh pending orders) | other | 0.95 | +1.0% | +0.95% |
| 2026-12-01 | November sales print (festive month, first full month of Diwali retail) | guidance | 0.99 | +0.5% | +0.49% |
| 2027-01 | CNG production capacity expansion starts (company) | capex | 0.80 | +0.8% | +0.60% |
| 2027-01 | Q3 FY27 results (margin trajectory; commodity pass-through via price hikes) | results | 0.97 | +0.0% | +0.00% |
| 2027-06 | EPR / End-of-Life Vehicles certificate pricing framework (company says obligation not yet reliably estimable) | regulatory | 0.30 | -1.5% | -0.45% |

## Analyst profile (agent research, sourced)
# MARUTI - Maruti Suzuki India Ltd. (as of 2026-11-05)

## Business
Maruti Suzuki is India's largest carmaker, selling about 2.1 lakh domestic passenger vehicles and ~50,000 exports a month (October 2026: 2.76 lakh units, +25% y/y, a record). About 40% of sales are CNG, small cars grew 38% y/y and SUVs hit a record 73,058 units (New Indian Express, 2026-11-01). Suzuki Motor holds ~58.7% (screener promoter holding). Revenue is ~80% domestic PV, ~15% exports and the rest spares/services. A large treasury portfolio adds ~Rs 4k cr a year of other income, which softens the equity impact of operating shocks but now creates mark-to-market noise.

## What moves the stock (ranked, model-implied, % equity value per standard shock)
1. **Industry demand** (F_AUTO_DEMAND_IN, +5.5 per +10% volumes): operating gearing of ~2.5x makes volume the largest lever. Record October sales, 12 days of dealer stock and a 2.45 lakh pending-order book support H2, but the GST 2.0 boost fades from Q3 as the base normalises.
2. **Steel and basic metals** (F_STEEL_INDIA -2.0, aluminium -0.5, copper -0.3): raw materials were 79.9% of sales in Q2 FY27 vs 75.7% a year earlier. Global HRC is +20.6% since June; aluminium is -19.6%, a partial offset.
3. **Policy: GST** (P_GST_CONSUMPTION +4.0, conditional): the Sept-2025 cut is the reason for the 26-27% volume growth; reversal risk is low, a further cut unlikely.
4. **Rates** (F_REPO_IN -0.9 per +25bp): RBI hiked to 5.50% on 2026-10-07 and signalled no cuts.
5. **Brent** (-1.2 per +10%, empirical -0.99, t -2.5): direct plastics/paint/fuel-cost channel.
6. **Competition and mix**: Tata Motors PV and Mahindra are taking SUV/EV share (Maruti only reclaimed 40% share in H1 FY27, Moneycontrol 2026-10-16); EV policy push is a modest negative (-0.8).

## Worked transmission chains
- **West Asia escalation -> Brent up (1st) -> pet-based inputs (plastics, paint, synthetic rubber) up (2nd) -> parts and variable cost up, Maruti margin -50-100bp (3rd) -> price hikes of 1-2% needed, which dent entry-level affordability and festive conversion (4th).**
- **Brent up -> INR weaker (2nd) -> yen/dollar-linked imports and treasury MTM losses (3rd, both cited in Q2) -> reported EBITDA margin down -> brokerages cut FY27/28 EPS (4th).**
- **Brent up -> India CPI up (2nd) -> RBI hike to 5.50% and 'calibrated tightening' (3rd) -> car-loan EMIs +1% and weaker equity multiples for rate-sensitive consumer discretionary (4th) -> volumes -0.5% per 25bp and de-rating.**
- **Steel up (China export surge or duty) -> auto input costs up (2nd) -> price hikes (3rd) -> small-car demand elastic, Maruti's core segment (4th).**

## Current situation
Q2 FY27 (reported 2026-10-27): revenue Rs 53,356 cr (+26%), EBITDA Rs 4,764 cr (-6% y/y), margin ~9%, PAT Rs 2,466 cr (-26%). Management cited commodity prices (West Asia), adverse FX, higher depreciation from new facility and dies, and MTM losses on treasury. The stock fell ~33% in CY2026 to an 18-month low in October and has bounced ~8% in a month; Nifty Auto jumped 2.9% on 2026-11-05 as crude eased and US tariff hopes rose after the midterms. Company said it cannot yet estimate obligations under the End-of-Life Vehicles EPR rules.

## Upcoming
November dispatches (1 Dec), a possible second RBI step in December, CNG capacity addition from January, Q3 results (~late Jan 2027), EPR pricing framework (timing unknown).

## Bull case
Crude and metals keep easing on Iran-US talks, price hikes stick, exports and CNG capacity keep growing, and margins recover toward 11-12%: EPS upgrades on a de-rated stock.
## Bear case
Metals and rubber stay high while rate hikes and fuel costs cool post-festive demand; share loss to Tata/Mahindra continues; treasury MTM and EPR liabilities hit earnings.

Confidence: medium. Estimates of cost shares and pass-through are model assumptions flagged in each edge. Screener dossier in the pack was empty; figures above come from a direct screener.in fetch on 2026-11-05 and the cited news.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.