# BLUESTARCO — Blue Star Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.8%**, **12 months +3.6%** (rank 47 / 45 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.9%): 3 months 55%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +2.3% … P90 +8.1%; plausible 12m relative-return range incl. stock-specific noise: -22.9% … +46.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.5 pp (model impact +7.0% beta-adjusted vs realised market-adjusted move -3.4%); forward event exposure +2.0% (3m +0.4%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.11 | +3.00 | +0.00 | +0.15 | -0.04 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +3.08 | +3.00 | +0.07 | +0.00 | +0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.69 | +2.50 | +0.00 | +0.14 | +0.05 | — |
| Consumer durables category promotional / discount intensity (`NEW_CONSUMER_DURABLES_PRICE_WAR`) | +1 pp of industry-wide margin given up (discounts, channel incentives, ad spend) in room AC and appliances | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.24 | +0.00 | -1.03 | -0.81 | -0.39 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.17 | -1.80 | +0.00 | -0.17 | -0.19 | -1.1% |
| Copper price (`F_COPPER`) | +10% copper | -1.64 | -1.50 | -0.14 | +0.00 | +0.00 | -2.4% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.62 | +0.00 | -1.15 | -0.37 | -0.11 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.59 | +1.50 | +0.00 | +0.06 | +0.03 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.47 | +0.00 | +0.96 | +0.17 | +0.33 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.37 | +1.00 | +0.20 | +0.15 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.32 | +0.00 | -0.17 | -0.70 | -0.45 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.15 | +0.00 | -0.91 | -0.20 | -0.05 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.13 | +1.00 | +0.12 | +0.00 | +0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.0% | -6.0% | +0.0 | -3.1 | -1.6 | -1.4 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.2 | -0.9 | -0.5 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +1.6 | +0.6 | -0.2 | -0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.7% | +1.7% | +1.7 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.5% | -1.5% | -1.1 | -0.3 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.6% | -1.3% | +0.0 | -1.9 | -0.9 | -0.8 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.1% | +1.2% | +0.0 | +1.1 | +0.5 | +0.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.0 | -0.1 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.0% | -1.1% | +0.0 | -3.0 | -0.9 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -0.2 | -0.7 | -0.1 | -0.1 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.1% | +1.0% | +0.8 | +0.2 | +0.1 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -4.3% | -1.0% | -3.1 | -0.9 | -0.3 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BLUESTARCO | +0.80% | +0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → BLUESTARCO | -2.16% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BLUESTARCO | -2.34% | -0.51% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → BLUESTARCO | -1.42% | -0.51% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → BLUESTARCO | +0.85% | +0.50% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → BLUESTARCO | +0.83% | +0.41% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BLUESTARCO | -0.64% | -0.32% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → BLUESTARCO | -0.88% | -0.31% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → BLUESTARCO | -0.60% | -0.27% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → BLUESTARCO | +0.60% | +0.27% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → BLUESTARCO | -0.86% | -0.24% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BLUESTARCO | -0.40% | -0.24% |
| 2 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → F_URBAN_DEMAND → BLUESTARCO | +0.29% | +0.23% |
| 2 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → F_USDINR → BLUESTARCO | -3.41% | -0.21% |
| 2 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → T_DATA_CENTRES_IN → BLUESTARCO | +0.24% | +0.20% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_ALUMINIUM → BLUESTARCO | -1.96 | observed | +1.37% |
| 1 | F_GSEC_10Y_IN → BLUESTARCO | +1.70 | events | -1.36% |
| 1 | F_GOVT_CAPEX → BLUESTARCO | +1.00 | events | +1.00% |
| 1 | F_USDINR → BLUESTARCO | -0.37 | observed | +0.66% |
| 1 | F_URBAN_DEMAND → BLUESTARCO | +0.20 | events | +0.60% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → BLUESTARCO | +1.00 | events | +0.48% |
| 1 | F_COPPER → BLUESTARCO | -0.24 | observed | +0.36% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → BLUESTARCO | +1.00 | events | -0.31% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → BLUESTARCO | +1.70 | events | -0.31% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → BLUESTARCO | +0.50 | events | +0.25% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → BLUESTARCO | -0.30 | events | -0.22% |
| 2 | F_GOVT_CAPEX → F_PRIVATE_CAPEX → BLUESTARCO | +1.00 | events | +0.20% |

## Analyst profile (agent research, sourced)
# BLUESTARCO - Blue Star Ltd. (midcap, air conditioning / MEP)

## Business
Three segments: electro-mechanical projects and commercial AC (66% of Q2 FY27 revenue, ~40% over a full year), unitary products (room ACs, coolers, purifiers; about half of annual sales and heavily concentrated in Q4/Q1), and professional/industrial equipment. EBITDA margin ~7%, P/E ~60, working-capital intensive. A MedTech unit was sold in Q2 FY27.

## What moves the stock (ranked)
1. **Category price war (-2.5 per +1pp)** and AC share shifts (Voltas, LG, Daikin).
2. **USD/INR (-1.8 per +3%)**: compressors and components are USD-priced; the rupee at 94.5 is +6.5% in 12 months.
3. **Copper (-1.5 per +10%)** and aluminium (-0.7): ~15% of costs; recovered only after 1-2 quarters through price hikes (three in 2026, latest +8% from 1 Oct).
4. **Urban demand and weather (+3.0 per +5pp)**: Q2 consumer softness was blamed on weather and GST-related deferment.
5. **Data centres (+3.0) and private capex (+2.5)**: EMPS order book Rs7,229cr.
6. Housing, premiumisation, government capex, G-sec yield.

## Transmission examples
- **Middle East escalation -> Brent and freight up (2nd) -> copper/aluminium and polymer inputs up, rupee weaker (3rd) -> compressor and coil costs up, AC list prices raised 5-8% (4th) -> weaker volumes in a festive/summer window and lower unitary margin.**
- **Brent up -> INR down -> RBI holds rates -> home loans dearer -> new-home sales and AC first-time purchase softer -> unitary volumes and residential MEP orders down.**
- **AI capex up -> Indian data-centre build-out (T_DATA_CENTRES_IN) -> precision-cooling and MEP orders -> EMPS revenue and margin upside (3rd); but also power-cable/copper demand pushes copper up (4th), a cost headwind for the unitary line.**
- **China steel/copper dumping or price cuts -> metal costs lower -> margin tailwind, but Chinese AC makers also push OEM supply and compete in exports.**

## Current situation
Q2 FY27 revenue +21% to Rs2,931cr, reported PAT +25% to Rs124cr but core profit flat once the Rs23cr MedTech gain is excluded; EMPS margin 6.9% (-190bp) on delays. Management cites H2 recovery and strong October demand. The stock is -18.4% over 12 months, near its 52-week low in early October, and UBS (Buy) and Motilal Oswal (Neutral, Rs1,510) disagree on valuation. Pack betas for copper/USDINR are positive (t=1.9/1.4) and conflict with the cost-channel sign; weights follow the mechanism and are low confidence.

## Upcoming
Q3 FY27 results ~Jan 2027; summer 2027 season sell-in from February; possible fourth price hike; EMPS margin guidance (>6.5% FY27).

## Bull / bear
Bull: metals and rupee ease, data-centre orders ramp EMPS margin toward 8%, hot summer lifts unitary share. Bear: copper/INR rebound, project delays persist, Voltas/LG discounting and a mild summer compress margin below 6%.

Uncertainties: segment margins conflict across sources (unitary margin unverified); copper share of costs is an estimate.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.