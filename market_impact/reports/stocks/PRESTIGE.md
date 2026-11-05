# PRESTIGE — Prestige Estates Projects Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.3%**, **12 months -8.8%** (rank 192 / 195 of 200 for 3m / 12m); beta 1.56
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.6%): 3 months 36%, 12 months 20%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.7% … P90 -5.7%; plausible 12m relative-return range incl. stock-specific noise: -28.2% … +4.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.9 pp (model impact -7.8% beta-adjusted vs realised market-adjusted move +12.6%); forward event exposure -10.3% (3m -5.6%; half assumed priced); company-specific events +2.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -8.05 | +0.00 | -4.98 | -2.51 | -0.57 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -5.02 | -4.00 | -0.78 | -0.21 | -0.03 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +4.77 | +5.00 | +0.00 | -0.17 | -0.06 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -4.37 | +0.00 | -1.77 | -1.52 | -1.09 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -4.09 | +0.00 | +0.00 | -2.74 | -1.34 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -3.27 | +0.00 | -0.81 | -1.66 | -0.80 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.27 | +3.00 | +0.04 | +0.10 | +0.12 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.63 | +0.00 | -0.11 | -0.85 | -1.67 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +2.26 | +1.50 | +0.80 | +0.00 | -0.04 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.20 | +0.00 | +0.46 | +1.33 | +0.41 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.18 | +0.00 | -1.16 | -0.72 | -0.29 | +3.5% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.16 | +0.00 | -0.36 | -1.18 | -0.62 | +0.0% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.90 | -1.20 | -0.65 | -0.01 | -0.03 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.69 | +0.00 | +0.96 | +0.57 | +0.16 | +1.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -9.2% | -9.2% | +0.0 | -5.7 | -2.9 | -0.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.2% | -7.2% | -6.6 | -0.1 | -0.2 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.3% | -5.3% | -4.5 | -0.7 | +0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.3% | +4.1% | +7.5 | +0.1 | +0.3 | +0.4 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.5% | -2.5% | -1.8 | -0.8 | +0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.5% | -2.5% | -0.2 | -1.4 | -0.7 | -0.2 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -5.3% | -2.2% | -4.5 | -0.7 | +0.1 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +4.0% | +2.2% | +0.0 | +1.0 | +1.9 | +1.1 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | +0.0 | -1.4 | -0.7 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -11.2% | -2.0% | -9.5 | -1.8 | +0.1 | -0.0 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -8.0% | -2.0% | +0.0 | -5.0 | -2.5 | -0.5 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -7.7% | -1.9% | +0.0 | -6.4 | -0.9 | -0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PRESTIGE | +7.50% | +3.75% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PRESTIGE | -4.00% | -1.68% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → PRESTIGE | -4.61% | -1.15% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → PRESTIGE | -4.00% | -1.08% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → PRESTIGE | -1.60% | -0.96% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → PRESTIGE | -4.50% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → PRESTIGE | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → PRESTIGE | -2.88% | -0.72% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → PRESTIGE | -4.00% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PRESTIGE | -2.80% | -0.70% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → PRESTIGE | -1.02% | -0.66% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_REPO_IN → PRESTIGE | -0.69% | -0.62% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → PRESTIGE | +1.50% | +0.52% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → PRESTIGE | +0.93% | +0.51% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → PRESTIGE | +0.60% | +0.48% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → PRESTIGE | -1.60 | events | -4.80% |
| 1 | F_REPO_IN → PRESTIGE | +1.00 | events | -4.00% |
| 1 | F_GSEC_10Y_IN → PRESTIGE | +1.55 | director_override | -1.55% |
| 1 | F_STEEL_INDIA → PRESTIGE | +1.35 | events | -0.94% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → PRESTIGE | +1.55 | director_override | -0.93% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → PRESTIGE | +0.50 | events | +0.60% |
| 1 | F_CREDIT_SPREADS_IN → PRESTIGE | +0.50 | events | -0.60% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → PRESTIGE | +1.00 | events | -0.52% |
| 1 | F_US_TECH_SPEND → PRESTIGE | -0.60 | events | -0.48% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → PRESTIGE | +1.00 | events | -0.40% |
| 1 | F_ALUMINIUM → PRESTIGE | -1.96 | observed | +0.39% |
| 1 | F_DXY → PRESTIGE | +0.74 | observed | -0.37% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 financial results/ call follow-through (Sep column already in screener) and sell-side revisions | results | 0.70 | +0.5% | +0.35% |
| 2026-11/2027-03 | H2 launches of ~Rs 40,000 cr GDV: sell-through vs Rs 7,225 cr quarterly bookings | capex | 0.80 | +1.5% | +1.20% |
| 2026-12/2027-03 | Closing of CPP Investments' 27% hospitality stake purchase (Rs 3,000 cr) - deleveraging | corporate_action | 0.70 | +1.5% | +1.05% |
| 2027-02 | Q3 FY27 results (model-estimated) | results | 0.95 | +0.5% | +0.47% |
| 2027-06 | Mahalaxmi project litigation: further court steps after Bombay HC set aside MahaREAT order | litigation | 0.40 | -1.0% | -0.40% |

## Analyst profile (agent research, sourced)
# Prestige Estates Projects (PRESTIGE) - profile as of 2026-11-05

## Business
Prestige is a Bengaluru-rooted, diversified developer with large residential pipelines (Bengaluru, Mumbai, NCR, Hyderabad, Chennai, Kochi) and an annuity/hospitality portfolio. It is the most leveraged name in this batch: TTM interest is Rs 1,617 crore against operating profit of Rs 3,630 crore. Q2 FY27 bookings rose 20% to Rs 7,225 crore (Business Standard, 2026-10-13) and management plans Rs 40,000 crore of launches in H2 (2026-10-20). On 2026-09-30 CPP Investments agreed to buy 27% of the hospitality arm for Rs 3,000 crore, a deleveraging step that followed the cancellation of hospitality IPO plans (2026-09-28). On 2026-11-04 Prestige acquired Gloind Vintage Infra at Rs 519 crore EV, and on 2026-10-01 the Bombay High Court set aside a MahaREAT order in the Mahalaxmi project case.

## What moves the stock
1. **Housing volumes (+5.0)** and **repo (-4.0 per +25 bp)**: higher leverage plus beta ~2 makes this the most rate-sensitive realty stock; the RBI hiked to 5.50% on 2026-10-07.
2. **FPI flows (+3.0)**, credit spreads (-1.2), G-sec (-1.0), RBI prudential norms (-0.8).
3. Bengaluru tech employment (US tech spend +0.8), premium mix (+1.5), policy (housing +1.5, capital gains -1.2), travel (+0.5), NRI (+0.4), costs (steel -0.7, cement -0.4, wages -0.4, aluminium -0.2).
Data check: DXY (+3.48 per +3%, t=2.7) and aluminium (-2.48 per +10%, t=-2.2) are significant in the pack but not mechanism-consistent in size; shrunk and flagged low.

## Transmission examples
- **Rates (4 orders)**: Middle East flare-up -> Brent up -> CPI and rupee pressure -> RBI hikes again in December -> Prestige's floating-rate debt cost rises and Bengaluru mortgage EMI up -> bookings slow while interest expense bites -> earnings and multiple (P/E 62) compress.
- **Tech cycle (4 orders)**: US tech/AI spending slows -> Bengaluru IT/GCC hiring slows -> housing demand in Whitefield/North Bengaluru softens and office leasing weakens -> pre-sales growth fades.
- **Deleveraging (3 orders)**: CPPIB closes Rs 3,000 crore hospitality deal -> net debt falls -> interest burden eases -> lower rate sensitivity.
- **Costs (3 orders)**: steel/cement up -> unsold inventory cost up -> margin cut on new launches.

## Current situation
Bookings strong, earnings volatile, debt high. The stock rose 11% in a month and trades at P/E 62; Motilal (TP Rs 1,830) sees 29% upside, but that is a sell-side view.

## Upcoming
H2 launches, CPPIB closing, Q3 results (~February 2027), Mahalaxmi litigation, December MPC.

## Bull / Bear
Bull: launches sell, hospitality proceeds cut debt, RBI pauses. Bear: more tightening hits the most levered stock; launches under-absorb; legal setbacks. Confidence medium; debt split and geographic mix are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.