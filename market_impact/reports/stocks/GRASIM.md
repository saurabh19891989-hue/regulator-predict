# GRASIM — Grasim Industries Ltd.
*NIFTY_50 · Construction Materials · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.5%**, **12 months +0.5%** (rank 78 / 87 of 200 for 3m / 12m); beta 1.09
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.9%): 3 months 52%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.1% … P90 +3.7%; plausible 12m relative-return range incl. stock-specific noise: -18.2% … +13.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.1 pp (model impact +2.2% beta-adjusted vs realised market-adjusted move -1.6%); forward event exposure -0.8% (3m -0.2%; half assumed priced); company-specific events +1.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.85 | +0.00 | -2.45 | -0.26 | -0.14 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.00 | -1.80 | -0.14 | -0.07 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.73 | +0.00 | -0.72 | -0.44 | -0.58 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.45 | +0.00 | +0.00 | -1.35 | -0.10 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.36 | +0.00 | -0.91 | -0.24 | -0.21 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.26 | +1.50 | +0.00 | -0.17 | -0.07 | — |
| International thermal coal price (`F_COAL_INTL`) | +15% seaborne thermal coal | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.17 | -0.70 | -0.14 | -0.26 | -0.07 | -1.1% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.01 | +0.00 | +0.50 | +0.64 | -0.13 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.00 | -0.60 | -0.11 | -0.23 | -0.06 | +0.0% |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +0.92 | +1.00 | +0.00 | -0.07 | -0.01 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | +0.90 | +0.80 | +0.10 | +0.00 | +0.00 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.79 | +0.00 | +0.38 | +0.13 | +0.28 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | -0.70 | +0.00 | +0.00 | -0.56 | -0.14 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -2.8 | -0.3 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -1.8 | -0.2 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.6% | +0.9% | +0.8 | +0.2 | +0.5 | +0.2 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.0% | -0.9% | -1.8 | -0.2 | -0.0 | -0.0 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | +0.0 | -0.7 | -0.1 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -2.8% | -0.7% | +0.0 | -2.5 | -0.3 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.7% | -0.7% | -1.3 | -0.6 | -0.5 | -0.3 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.3 | +0.1 | +0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.3 | -0.1 | -0.2 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -1.0% | -0.6% | -0.7 | -0.4 | +0.1 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -3.2% | -0.6% | -2.7 | -0.4 | -0.1 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.3 | -0.1 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GRASIM | -1.80% | -0.76% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → GRASIM | -2.07% | -0.52% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → GRASIM | -1.80% | -0.49% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → GRASIM | -0.72% | -0.43% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GRASIM | +0.78% | +0.43% |
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → GRASIM | +0.56% | +0.39% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GRASIM | -1.32% | -0.33% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → GRASIM | -1.80% | -0.32% |
| 1 | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → GRASIM | -0.60% | -0.30% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → GRASIM | -0.46% | -0.30% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_REPO_IN → GRASIM | -0.31% | -0.28% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → GRASIM | -1.80% | -0.22% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_REPO_IN → GRASIM | -0.29% | -0.20% |
| 3 | EV_NEMONSOON26_NORMAL_UP ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → GRASIM | +0.23% | +0.19% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ F_CPI_IN → F_REPO_IN → GRASIM | -0.62% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REPO_IN → GRASIM | +1.00 | events | -1.80% |
| 1 | F_COAL_INTL → GRASIM | +0.70 | director_override | -0.84% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → GRASIM | +1.55 | director_override | -0.37% |
| 1 | P_ANTI_DUMPING_IN → GRASIM | +0.40 | events | +0.32% |
| 1 | F_URBAN_DEMAND → GRASIM | +0.20 | events | +0.30% |
| 1 | F_USDINR → GRASIM | -0.37 | observed | +0.26% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → GRASIM | +0.50 | events | +0.12% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → GRASIM | +1.00 | events | -0.10% |
| 1 | F_COTTON → GRASIM | +0.19 | observed | +0.10% |
| 2 | F_USDCNY → F_CHINA_CHEM_EXPORTS → GRASIM | -0.47 | observed | +0.09% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → GRASIM | +1.00 | events | -0.08% |
| 2 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → GRASIM | +0.30 | events | +0.08% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (date not announced; Grasim reported Q1 on 12 Aug) | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | Further promoter open-market purchases (stake already raised to 45.07%) | corporate_action | 0.50 | +0.8% | +0.38% |
| 2027-03 | Birla Opus profitability milestones / pricing war outcomes | guidance | 0.50 | +0.0% | +0.00% |
| 2027-06 | Possible holding-company simplification / listing events in ABC group (unverified) | corporate_action | 0.10 | +2.0% | +0.20% |

## Analyst profile (agent research, sourced)
# GRASIM — Grasim Industries Ltd. (as of 2026-11-05)

*Facts from screener.in (evidence pack, consolidated through Jun 2026) and Google News headlines; bodies not retrieved. "Model knowledge" items are from memory. No expected-return number.*

## Business
Grasim is a holding-plus-operating company. Its market value (Rs 2.18 lakh cr) is dominated by stakes in UltraTech (about 56%, worth roughly Rs 2.0 lakh cr) and Aditya Birla Capital (about 52%, roughly Rs 0.57 lakh cr), both model knowledge for the stake percentages. Standalone it runs VSF and fashion yarn, caustic soda and chlorine derivatives, epichlorohydrin (ECH), the Birla Opus paint business (still loss-making), B2B e-commerce and renewables. Q1 FY27 consolidated sales Rs 48,716 cr, EBITDA Rs 11,152 cr, PAT Rs 3,846 cr. Q2 results are not yet out.

## What moves the stock (ranked)
1. **UltraTech (holding link, 0.6 per 1% move):** cement price, kiln fuel and housing flow through here. See ULTRACEMCO for the cement driver weights.
2. **ABCAPITAL (0.2 per 1%):** NBFC credit cycle, rates, asset quality.
3. **Rates and leverage (F_REPO_IN -1.8 per 25 bp):** consolidated interest Rs 4,298 cr per quarter and rising with paint, chemical and renewables capex.
4. **Paint war and urban demand (+1.5 per +5pp):** Opus is a drag today but an option on a mature market.
5. **Seaborne coal for captive power (-1.2 per +15%),** FX (-0.7), Brent (-0.6), China chemical exports (-0.8), cotton (+0.5), anti-dumping (+0.8).

## Transmission examples
- **Middle East escalation -> Brent up -> UltraTech cost up -> Grasim down.** C_MIDEAST_CONFLICT -> Brent/petcoke (1st) -> UltraTech margins fall (2nd) -> UltraTech equity -3% -> Grasim -1.8% through the 0.6 look-through (3rd) -> the ECH/chemical and paint costs also rise, deepening Opus losses (4th).
- **RBI hike -> NBFC and holdco.** Repo +25bp (done 7 Oct) -> ABCAPITAL funding cost and loan growth hit (1st) -> ABCAP equity -2% -> Grasim -0.4% via 0.2 weight; separately Grasim's own Rs 60-70k cr debt costs +Rs 150 cr (2nd); housing demand slower -> UltraTech volume (3rd).
- **China export surge.** F_CHINA_CHEM_EXPORTS +15% -> caustic/ECH/VSF prices down (1st) -> chemicals EBITDA -10% (2nd) -> group EBITDA -1% (3rd) -> reduced cash for Opus capex, higher net debt (4th).
- **Paint price war (Asian Paints reacts to Opus).** Competitor cuts prices -> Opus loss widens -> group profit lower -> holdco discount widens.

## Current situation
Latest hard numbers are Q1 FY27: PAT +39% y/y to Rs 3,846 cr. UltraTech's Q2 (19 Oct): PAT +21%, OPM 16%, stock +13.9% in a month; Ambuja's Q2 showed sector margin stress. Promoters raised their stake to 45.07% via open-market buys (28 Sep). 21 Oct ECH commercial production began; 4 Nov Suzlon tie-up for recyclable blades lifted Grasim up to 5%. 12m +11%, 1m +8%.

## Upcoming
Q2 FY27 results (mid-Nov, date not announced); UltraTech Q3 (Jan); Opus break-even guidance; further promoter purchases; RBI Dec policy.

## Bull case
UltraTech earnings recover with price hikes, Opus nears breakeven, promoter buying narrows the holdco discount.

## Bear case
Paint war drags, debt costs rise, ABCAPITAL credit cost rises, and cement margins stay squeezed.

## Uncertainties
Segment shares, stakes and standalone debt are model estimates; Q2 numbers missing.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.