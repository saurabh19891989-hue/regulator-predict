# GRASIM — Grasim Industries Ltd.
*NIFTY_50 · Construction Materials · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.8%**, **12 months +1.6%** (rank 71 / 76 of 200 for 3m / 12m); beta 1.09
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.9%): 3 months 54%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.7% … P90 +5.9%; plausible 12m relative-return range incl. stock-specific noise: -20.8% … +25.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.7 pp (model impact +3.4% beta-adjusted vs realised market-adjusted move -1.6%); forward event exposure +0.4% (3m -0.1%; half assumed priced); company-specific events +1.7%

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
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.3% | -5.3% | -3.0 | -0.5 | -1.4 | -0.4 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -2.8 | -0.3 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -1.8 | -0.2 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.0% | -1.1% | -1.5 | -0.6 | -0.6 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.8% | +1.1% | +0.9 | +0.2 | +0.5 | +0.2 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -2.0% | -0.8% | -1.8 | -0.2 | -0.0 | -0.0 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | +0.0 | -0.7 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.3 | -0.2 | -0.2 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -2.8% | -0.7% | +0.0 | -2.5 | -0.3 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -3.2% | -0.7% | -2.7 | -0.4 | -0.1 | +0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.0 | +0.4 | +0.2 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.3 | +0.1 | +0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → GRASIM | -2.97% | -2.97% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → GRASIM | -2.38% | -2.38% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → GRASIM | -1.80% | -1.80% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → GRASIM | -0.80% | -0.80% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GRASIM | -1.80% | -0.72% |
| 4 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → GRASIM | -0.58% | -0.58% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → F_REPO_IN → GRASIM | -0.58% | -0.58% |
| 3 | EV_KHARIF26_OUTPUT_HIT ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → GRASIM | -0.57% | -0.57% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → GRASIM | -0.55% | -0.55% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GRASIM | -1.50% | -0.54% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GRASIM | +0.90% | +0.52% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → GRASIM | -2.07% | -0.52% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → GRASIM | -1.80% | -0.49% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → GRASIM | -0.72% | -0.43% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → GRASIM | -1.80% | -0.40% |

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