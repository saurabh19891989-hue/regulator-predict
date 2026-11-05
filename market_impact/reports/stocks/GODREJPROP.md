# GODREJPROP — Godrej Properties Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.5%**, **12 months -5.0%** (rank 169 / 170 of 200 for 3m / 12m); beta 1.64
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.6%): 3 months 43%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.2% … P90 -2.7%; plausible 12m relative-return range incl. stock-specific noise: -46.4% … +31.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.0 pp (model impact -6.3% beta-adjusted vs realised market-adjusted move -2.2%); forward event exposure -7.2% (3m -4.1%; half assumed priced); company-specific events +3.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -7.16 | +0.00 | -4.29 | -2.15 | -0.72 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +5.84 | +6.00 | +0.00 | -0.13 | -0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.56 | -3.50 | -0.72 | -0.28 | -0.06 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.54 | +0.00 | +0.00 | -2.36 | -1.18 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.16 | +3.00 | -0.03 | +0.10 | +0.09 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +2.43 | +1.50 | +0.96 | +0.00 | -0.03 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.36 | +0.00 | +0.82 | +1.13 | +0.42 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -2.36 | +0.00 | -0.22 | -1.37 | -0.77 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.17 | +0.00 | +0.00 | -0.64 | -1.54 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.00 | +0.00 | -1.12 | -0.66 | -0.21 | +3.5% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.88 | -1.20 | -0.65 | +0.01 | -0.03 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.86 | +0.00 | -0.27 | -1.13 | -0.47 | +0.0% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.60 | +0.00 | +0.96 | +0.49 | +0.15 | +1.2% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.55 | +1.50 | +0.05 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -8.2% | -8.2% | +0.0 | -4.9 | -2.5 | -0.8 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.0% | -7.0% | -6.6 | +0.1 | -0.2 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -4.8% | -4.8% | -3.7 | -1.1 | +0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.0% | +4.0% | +7.5 | -0.1 | +0.3 | +0.3 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -0.2 | -2.0 | -0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.2% | -2.2% | -0.2 | -1.1 | -0.6 | -0.2 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -4.8% | -2.0% | -3.7 | -1.1 | +0.0 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -10.2% | -1.8% | -7.6 | -2.6 | +0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.3% | +1.8% | +0.0 | +0.8 | +1.7 | +0.8 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -7.2% | -1.8% | +0.0 | -4.3 | -2.2 | -0.7 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | +0.0 | -1.2 | -0.6 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.7% | +1.7% | +1.5 | +0.0 | +0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GODREJPROP | +7.50% | +3.75% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GODREJPROP | -3.50% | -1.47% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → GODREJPROP | -4.03% | -1.01% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → GODREJPROP | -3.50% | -0.95% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → GODREJPROP | -1.40% | -0.84% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → GODREJPROP | -4.50% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → GODREJPROP | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → GODREJPROP | -2.88% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → GODREJPROP | -2.80% | -0.70% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → GODREJPROP | -3.50% | -0.63% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → GODREJPROP | -0.89% | -0.58% |
| 2 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → F_HOUSING_DEMAND → GODREJPROP | -1.15% | -0.58% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_REPO_IN → GODREJPROP | -0.60% | -0.54% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → GODREJPROP | +1.50% | +0.52% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → GODREJPROP | +0.60% | +0.48% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → GODREJPROP | -1.60 | events | -4.80% |
| 1 | F_REPO_IN → GODREJPROP | +1.00 | events | -3.50% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → GODREJPROP | +1.55 | director_override | -2.23% |
| 1 | F_STEEL_INDIA → GODREJPROP | +1.35 | events | -0.81% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → GODREJPROP | +0.50 | events | +0.72% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → GODREJPROP | +1.00 | events | -0.62% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → GODREJPROP | +1.00 | events | -0.48% |
| 1 | F_CREDIT_SPREADS_IN → GODREJPROP | +0.50 | events | -0.40% |
| 1 | F_DXY → GODREJPROP | +0.74 | observed | -0.37% |
| 1 | F_URBAN_DEMAND → GODREJPROP | +0.20 | events | +0.24% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → GODREJPROP | +1.35 | events | -0.16% |
| 1 | F_USDINR → GODREJPROP | -0.37 | observed | -0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11/2027-03 | H2 FY27 launches of ~Rs 32,000 cr; sell-through test for FY27 bookings target Rs 41,500 cr | capex | 0.80 | +1.5% | +1.20% |
| 2026-12/2027-03 | New land/JDA additions (company typically adds Rs 15-20k cr GDV quarterly; headline Marine Lines Rs 6,000 cr) | capex | 0.85 | +1.5% | +1.27% |
| 2027-01 | Q3 FY27 business update (bookings) and results (date model-estimated; Q2 results were 2026-10-23) | results | 0.95 | +0.5% | +0.47% |
| 2027-05 | FY27 results: bookings vs Rs 41,500 cr target, FY28 guidance | guidance | 0.90 | +0.5% | +0.45% |

## Analyst profile (agent research, sourced)
# Godrej Properties (GODREJPROP) - profile as of 2026-11-05

## Business
Godrej Properties is an asset-light, brand-led residential developer operating across Mumbai, NCR, Bengaluru, Pune, Hyderabad and Kolkata. It grows through joint development agreements (JDAs) and development-management deals rather than buying large land banks, so reported operating profit is lumpy (screener TTM operating profit is negative while PAT is Rs 1,334 crore because of JV and other items). Bookings are the real driver: management targets a record Rs 41,500 crore in FY27 (+22%) and plans Rs 32,000 crore of launches in H2 (Fortune India 2026-10-25; Business Standard 2026-10-23). Q2 FY27 PAT dropped 62% to about Rs 154 crore with record collections but weaker sales volumes, and shares fell 6%.

## What moves the stock
1. **Housing volumes (+6.0 per +10%)**: it is the purest market-volume play in the batch; Anarock saw only +3% y/y in Jul-Sep 2026.
2. **RBI repo and sentiment (-3.5 per +25 bp)**: repo went to 5.50% on 2026-10-07; stock beta is about 2.0 and P/E ~40.
3. **FPI flows (+3.0)**, DII flows (+1.0).
4. Premium mix (+1.5), policy (housing support +1.5, capital gains -1.2, RBI prudential -0.6), credit spreads (-0.8), construction inputs (steel -0.6, cement -0.4, wages -0.4).
Data check: the pack shows DXY +3.27 per +3% (t=2.8) and USD/INR -2.5 (t=-1.4); both are inconsistent with the mechanism-based priors so those weights are shrunk and flagged as low confidence.

## Transmission examples
- **Rates (4 orders)**: Brent at ~$95 (+15% in 3 months) -> CPI up, rupee weak -> RBI hikes again in December -> mortgage rates +25 bp, housing affordability drops, investor-buyers retreat -> bookings in H2 launches miss -> FY27 Rs 41,500 crore target at risk -> multiple derates.
- **Construction cost (3 orders)**: China steel exports fall -> Indian HRC firms (+7%) -> unsold-inventory costs rise ~0.4% of revenue -> margin on new launches shaved; developers raise launch prices which dampens volume.
- **Flows (3 orders)**: US yields (4.89%) rise -> FPIs trim EM mid-caps -> GODREJPROP (beta 2) falls more than index -> sentiment hit to launches.
- **Policy (3 orders)**: stamp-duty cut or redevelopment FSI easing in Maharashtra -> Mumbai redevelopment pipeline faster -> JDA/DM wins increase.

## Current situation
After a 62% PAT fall and a Rs 70 crore settlement shock, Nomura upgraded to Buy (TP Rs 1,900); the stock rebounded 12% in a month. Reported earnings are an unreliable guide; watch bookings and collections.

## Upcoming
H2 launches; Q3 update (~January 2027); December MPC; FY27 bookings versus target in May 2027.

## Bull / Bear
Bull: bookings reach Rs 41,500 crore, RBI pauses, FPIs return. Bear: launches under-subscribe in a hiking cycle, further one-offs, mid-cap derating. Confidence medium; leverage and NRI share are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.