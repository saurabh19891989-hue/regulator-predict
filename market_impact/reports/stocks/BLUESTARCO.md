# BLUESTARCO — Blue Star Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months -0.2%** (rank 96 / 112 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.9%): 3 months 50%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.7% … P90 +2.7%; plausible 12m relative-return range incl. stock-specific noise: -47.5% … +28.6%
- Decomposition (12m): 0.5 × forward event exposure +0.0% (3m +0.3%; half assumed priced) + 0.5 × company-specific catalysts +0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +6.2% (beta-adjusted) vs a realised market-adjusted move of -3.4% — gap +9.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.11 | +3.00 | +0.00 | +0.15 | -0.04 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +3.08 | +3.00 | +0.07 | +0.00 | +0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.69 | +2.50 | +0.00 | +0.14 | +0.05 | — |
| Consumer durables category promotional / discount intensity (`NEW_CONSUMER_DURABLES_PRICE_WAR`) | +1 pp of industry-wide margin given up (discounts, channel incentives, ad spend) in room AC and appliances | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.00 | -1.80 | +0.00 | -0.13 | -0.07 | -1.1% |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.59 | +1.50 | +0.00 | +0.06 | +0.03 | — |
| Copper price (`F_COPPER`) | +10% copper | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | -2.4% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.41 | +0.00 | -1.03 | -0.25 | -0.13 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.39 | +0.00 | -1.15 | -0.15 | -0.09 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.37 | +1.00 | +0.20 | +0.15 | +0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.30 | +0.00 | +0.96 | +0.17 | +0.16 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.13 | +1.00 | +0.12 | +0.00 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.06 | +0.00 | -0.17 | -0.48 | -0.41 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.01 | +0.00 | -0.91 | -0.08 | -0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +1.6 | +0.6 | -0.2 | -0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.7% | +1.7% | +1.7 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.2 | -0.3 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.1 | -0.2 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.0% | -1.0% | -0.2 | -0.6 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.9 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.3% | -0.8% | +0.0 | -2.7 | -0.6 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.2% | -0.8% | -3.1 | -0.8 | -0.3 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +0.0 | +0.7 | +0.4 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | +0.0 | -0.3 | -0.4 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | +0.6% | +0.6% | +0.7 | -0.0 | +0.0 | +0.0 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -1.0% | -0.6% | -0.4 | -0.7 | +0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → BLUESTARCO | -2.16% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BLUESTARCO | -2.34% | -0.42% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → BLUESTARCO | +0.83% | +0.41% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BLUESTARCO | -0.64% | -0.32% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → BLUESTARCO | -0.88% | -0.31% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → BLUESTARCO | -0.60% | -0.27% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → BLUESTARCO | +0.48% | +0.27% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BLUESTARCO | -0.40% | -0.24% |
| 2 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → F_URBAN_DEMAND → BLUESTARCO | +0.29% | +0.23% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → BLUESTARCO | -0.82% | -0.20% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BLUESTARCO | +0.20% | +0.18% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → BLUESTARCO | -0.16% | -0.14% |
| 2 | EV_CPI_BREACH_6PCT ⇒ F_CPI_IN → F_URBAN_DEMAND → BLUESTARCO | -0.24% | -0.14% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → BLUESTARCO | -0.24% | -0.14% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → BLUESTARCO | -0.80% | -0.14% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_ALUMINIUM → BLUESTARCO | -1.96 | observed | +1.37% |
| 1 | F_GSEC_10Y_IN → BLUESTARCO | +1.55 | director_override | -1.24% |
| 1 | F_USDINR → BLUESTARCO | -0.37 | observed | +0.66% |
| 1 | F_URBAN_DEMAND → BLUESTARCO | +0.20 | events | +0.60% |
| 1 | F_COPPER → BLUESTARCO | -0.24 | observed | +0.36% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → BLUESTARCO | +1.00 | events | -0.31% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → BLUESTARCO | +0.50 | events | +0.25% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → BLUESTARCO | +0.50 | director_override | +0.24% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → BLUESTARCO | -0.30 | events | -0.22% |
| 1 | F_GOVT_CAPEX → BLUESTARCO | +0.20 | director_override | +0.20% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → BLUESTARCO | +0.50 | events | +0.18% |
| 2 | F_REPO_IN → F_PRIVATE_CAPEX → BLUESTARCO | +1.00 | events | -0.16% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further AC price increase after three in 2026 (latest +8% from 1 Oct) if copper/INR stay elevated | guidance | 0.30 | +1.8% | +0.53% |
| 2027-01 | Q3 FY27 results (date not announced); off-season quarter, watch EMPS margin and unitary inventory ahead of summer | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Peak summer-season AC sell-in (Feb-May 2027); temperature outcomes decide FY27 Q4 and FY28 Q1 unitary revenue | other | 0.90 | +0.0% | +0.00% |
| 2027-03 | FY27 EMPS EBIT margin guided >6.5% (aspiration 7.0-7.5%) - delivery vs guidance after Q2 6.9% | guidance | 0.60 | +0.0% | +0.00% |

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