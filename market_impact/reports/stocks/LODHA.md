# LODHA — Lodha Developers Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.0%**, **12 months -0.6%** (rank 109 / 136 of 200 for 3m / 12m); beta 1.75
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +36.6%): 3 months 50%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.2% … P90 +1.5%; plausible 12m relative-return range incl. stock-specific noise: -48.4% … +45.6%
- Decomposition (12m): 0.5 × forward event exposure -1.7% (3m -0.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -2.5% (beta-adjusted) vs a realised market-adjusted move of +23.0% — gap -25.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.10 | -0.00 | +0.10 | +0.04 |
| Regulatory | -0.10 | -0.03 | -0.14 | -0.01 |
| Sector | -0.04 | +0.27 | +0.22 | +0.11 |
| Theme | +0.00 | +0.01 | +0.01 | +0.00 |
| Geopolitics | +0.00 | -0.03 | -0.03 | -0.03 |
| Company catalysts | +0.40 | +0.00 | +0.40 | +0.40 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -1.00 | -0.45 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.58** | **-0.05** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +5.99 | +6.00 | +0.00 | +0.00 | -0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.29 | -2.45 | -0.70 | -0.07 | -0.08 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.02 | +3.00 | -0.06 | +0.05 | +0.03 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +2.46 | +1.50 | +0.96 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.16 | +0.00 | -1.29 | -0.71 | -0.16 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.02 | +2.00 | +0.00 | +0.00 | +0.02 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.85 | -1.20 | -0.65 | +0.02 | -0.02 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.61 | +0.00 | -1.09 | -0.49 | -0.03 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.48 | +0.00 | -0.05 | -0.74 | -0.70 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.27 | +0.00 | +0.48 | +0.34 | +0.45 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.17 | +0.00 | +0.00 | -0.71 | -0.46 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.16 | +0.00 | +0.64 | +0.34 | +0.18 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.15 | +0.00 | -0.68 | -0.22 | -0.26 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.06 | +0.00 | +1.66 | -0.41 | -0.18 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.6% | -6.6% | -6.6 | +0.1 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.6% | +3.8% | +7.5 | -0.2 | +0.1 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.5% | -3.5% | -2.6 | -0.8 | +0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.5 | -0.8 | -0.3 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.6% | +1.6% | +1.5 | -0.0 | +0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.1% | -1.5% | +0.0 | -6.0 | -0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -3.5% | -1.5% | -2.6 | -0.8 | +0.1 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.4% | -1.4% | -0.2 | -0.9 | -0.3 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.7% | -1.4% | -6.2 | -1.6 | +0.1 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | +0.0 | -0.5 | -0.5 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.9% | +1.0% | +0.0 | +0.8 | +0.9 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | -0.2 | -0.8 | -0.1 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LODHA | +7.50% | +3.75% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → LODHA | -2.45% | -1.03% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → LODHA | -4.50% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → LODHA | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → LODHA | -2.88% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LODHA | -2.80% | -0.70% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → LODHA | -2.45% | -0.66% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → LODHA | +1.50% | +0.52% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → LODHA | +0.60% | +0.48% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → LODHA | -2.45% | -0.44% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LODHA | -2.80% | -0.42% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ NEW_USDJPY → F_FPI_FLOWS → LODHA | -2.16% | -0.32% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → LODHA | -2.45% | -0.29% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LODHA | -1.12% | -0.28% |
| 2 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LODHA | +0.45% | +0.28% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → LODHA | -1.60 | events | -4.80% |
| 1 | F_REPO_IN → LODHA | +1.00 | events | -2.45% |
| 1 | F_STEEL_INDIA → LODHA | +1.35 | events | -0.81% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → LODHA | +1.55 | director_override | -0.74% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → LODHA | +0.50 | events | +0.72% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → LODHA | +1.00 | events | -0.62% |
| 1 | F_CREDIT_SPREADS_IN → LODHA | +0.50 | events | -0.40% |
| 1 | F_ALUMINIUM → LODHA | -1.96 | observed | +0.39% |
| 1 | F_DXY → LODHA | +0.74 | observed | -0.37% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → LODHA | +0.50 | director_override | -0.24% |
| 1 | F_USDINR → LODHA | -0.37 | observed | -0.22% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → LODHA | +1.35 | events | -0.16% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11/2027-03 | H2 launches incl. NCR office/residential and MMR; test of Nomura's +25% H2 pre-sales call | capex | 0.80 | +1.0% | +0.80% |
| 2027-02 | Q3 FY27 results/pre-sales (model-estimated; Q2 reported 2026-10-30) *(review: [RT_BOT_B] )* | results | 0.95 | +0.0% | +0.00% |
| 2027-05 | FY27 results: PAT versus guidance (company flags it will exceed); FY28 pre-sales guidance *(review: [RT_BOT_B] )* | guidance | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Lodha Developers (LODHA) - profile as of 2026-11-05

## Business
Lodha is India's largest developer by Mumbai-region residential pre-sales, with extra projects in Pune, Bengaluru, a new NCR entry (Rs 1,700 crore office project, 2026-10-31) and London, plus industrial/logistics and digital parks around Palava. Q2 FY27: pre-sales Rs 5,037 crore (+10%), PAT Rs 1,013 crore (+28%); H1 PAT Rs 2,386 crore (+63%) and management expects to beat FY27 profit guidance (Economic Times / Business Standard, 2026-10-30). Nomura (2026-11-03) expects H2 pre-sales +25% to Rs 143 billion. TTM operating margin is about 33% and ROCE 16.4%, the highest in this batch except Oberoi.

## What moves the stock (ranked)
1. **Housing volumes (+6.0 per +10%)**, concentrated in MMR where redevelopment and premium demand dominate.
2. **Repo / rate sentiment (-3.5 per +25 bp)**: the RBI hiked to 5.50% on 2026-10-07; yet Lodha rose 4% on 2026-09-18 on "rate hike bets" (Livemint), showing the market sometimes reads hikes as a sign of strong growth. Treat as ambiguous.
3. **FPI flows (+3.0)** with beta 2.2-2.3: the highest-beta name in the batch.
4. Premium mix (+2.0), NRI/Gulf remittances (+0.6), weak rupee (+0.6, low confidence), policy (housing +1.5, capital gains -1.2), credit spreads (-0.8), costs (steel -0.6, cement -0.4, aluminium -0.2).
Empirical oddities: DXY +4.48 per +3% (t=3.1) and aluminium -3.11 per +10% (t=-2.5) are not mechanism-consistent in size, so they are shrunk.

## Transmission examples
- **Rates (4 orders)**: Brent ~$95 and weak rupee -> CPI -> RBI hikes again in December -> MMR mortgage rates +25 bp -> investor and mid-segment buyers delay -> H2 launches sell slower than Nomura's +25% -> pre-sales miss -> beta-2.2 stock derates.
- **Wealth (3 orders)**: Nifty rally and bonuses -> NRI/HNI demand -> Lodha Bellevue-type premium launches sell out -> realisations up -> margin above 33%.
- **Industrial parks (4 orders)**: AI/data-centre and China+1 capex -> demand for logistics and digital parks around Palava -> land monetisation and leasing income -> lower dependence on residential cycle.
- **Costs (3 orders)**: steel +7% -> unsold stock cost +0.4% of revenue -> small margin hit.

## Current situation
Profits are strong but the Q2 call "missed estimates" (Investing.com, 2026-11-02) on pre-sales growth of only 10%; brokers (Motilal Rs 1,375, Emkay Rs 1,400) remain positive. The stock is +21% in six months yet -4% in 12 months.

## Upcoming
Investor meets mid-November; H2 launches; Q3 results (~early February 2027); December MPC; FY27 profit-guidance beat.

## Bull / Bear
Bull: launch momentum returns, profit guidance beaten, RBI pauses. Bear: rate hikes and FPI outflow hit a 40%-vol stock; pre-sales growth stays near 10%. Confidence medium; debt, NRI share and regional mix are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.