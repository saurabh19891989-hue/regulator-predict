# TRENT — Trent Ltd.
*NIFTY_50 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +1.1%** (rank 64 / 29 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +51.3%): 3 months 50%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.5% … P90 +2.8%; plausible 12m relative-return range incl. stock-specific noise: -64.0% … +63.5%
- Decomposition (12m): 0.5 × forward event exposure +0.2% (3m -0.0%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.6% (beta-adjusted) vs a realised market-adjusted move of +4.7% — gap -3.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.03 | +0.07 | +0.10 | -0.02 |
| Regulatory | +0.00 | -0.01 | -0.01 | -0.00 |
| Sector | +0.39 | +0.34 | +0.74 | +0.36 |
| Theme | +0.00 | -0.02 | -0.02 | -0.02 |
| Geopolitics | +0.00 | -0.03 | -0.03 | -0.02 |
| Company catalysts | +1.10 | +0.00 | +1.10 | +0.42 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.67 | -0.30 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+1.07** | **+0.31** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +5.14 | +5.00 | +0.00 | +0.12 | +0.02 | — |
| Value-fashion and mass-retail competition intensity (`NEW_VALUE_FASHION_COMPETITION`) | +1 = materially sharper expansion/discounting by Reliance Trends/Yousta, Max, Style Union, Myntra, V-Mart | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.35 | +1.50 | +0.98 | -0.12 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.02 | +1.00 | +0.82 | +0.17 | +0.03 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.88 | +1.50 | +0.00 | +0.19 | +0.19 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.80 | -1.50 | -0.18 | -0.06 | -0.05 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.58 | +1.50 | +0.05 | +0.02 | +0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.27 | +0.00 | -1.28 | +0.11 | -0.09 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.15 | +0.00 | +0.46 | +0.23 | +0.46 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.06 | +0.00 | +0.64 | +0.42 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.00 | +0.00 | +0.00 | -0.50 | -0.49 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.94 | +0.00 | -0.62 | -0.29 | -0.03 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.90 | -0.50 | -0.36 | -0.10 | +0.06 | -1.1% |
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -0.89 | +0.00 | -0.76 | -0.10 | -0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.5% | -3.5% | -3.3 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.0% | +2.0% | +3.8 | +0.1 | +0.1 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.8% | -1.8% | -1.5 | -0.2 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.6 | +0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -0.6 | -0.3 | -0.6 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.3% | +1.3% | +1.0 | +0.3 | +0.0 | -0.0 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.8 | -0.1 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.8% | -0.9% | -4.4 | -0.2 | -0.2 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.8% | +0.8% | +0.8 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.8% | -0.8% | -1.5 | -0.2 | -0.1 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.9% | -0.7% | +0.0 | -3.0 | +0.1 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TRENT | +3.75% | +1.88% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TRENT | -1.50% | -0.63% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → TRENT | -1.50% | -0.41% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TRENT | -2.25% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TRENT | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → TRENT | -1.44% | -0.36% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → TRENT | +0.45% | +0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TRENT | -1.40% | -0.35% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → TRENT | +0.45% | +0.31% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → TRENT | -1.50% | -0.27% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → TRENT | +0.75% | +0.26% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → TRENT | +0.45% | +0.25% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → TRENT | +0.30% | +0.24% |
| 2 | EV_CPI_BREACH_6PCT ⇒ F_CPI_IN → F_URBAN_DEMAND → TRENT | -0.40% | -0.24% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → TRENT | +0.34% | +0.23% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → TRENT | -1.60 | events | -2.40% |
| 1 | F_REPO_IN → TRENT | +1.00 | events | -1.50% |
| 1 | F_URBAN_DEMAND → TRENT | +0.20 | events | +1.00% |
| 1 | F_RURAL_DEMAND → TRENT | -0.25 | events | -0.38% |
| 1 | F_USDINR → TRENT | -0.37 | observed | +0.18% |
| 1 | F_COTTON → TRENT | +0.19 | observed | -0.10% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Q3 business update (Trent publishes quarterly revenue updates early in the following month; Q2 update was 2026-10-06) | guidance | 0.85 | +1.0% | +0.85% |
| 2027-02 | Q3 FY27 results (festive quarter with Diwali on 2026-11-08, model knowledge); like-for-like growth and EBIT margin | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Zudio / Westside store additions toward FY27 target; Star Bazaar rollout | capex | 0.90 | +1.5% | +1.35% |
| 2027-04 | Index changes / FII reallocation after Q4 | other | 0.15 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# TRENT (Trent Ltd.) - company profile as of 2026-11-05

## Business
Trent, part of the Tata Group (promoters 37.01%), runs Zudio (value fashion, 1,000+ stores), Westside (premium fashion) and Star Bazaar, plus emerging categories (beauty, footwear and others) now 21% of revenue. TTM sales are Rs 22,001 cr (+18%) with EBITDA Rs 4,169 cr (19%). September 2026 quarter: sales Rs 5,873 cr (+22%), OPM 18%. The market cap is Rs 1.63 lakh cr at Rs 3,058, P/E 85, yet the shares are -34.5% over twelve months (Yahoo/screener, 2026-11-05).

## What moves the stock (ranked)
1. **Like-for-like growth and new store productivity.** Sales growth slowed to 15-19% in FY26, then re-accelerated to 22%. The market prices persistence of 20%+.
2. **Urban discretionary demand.** Beta 1.3; +5pp urban growth is worth about +5 equity points.
3. **Competition in value fashion** (Reliance, Max, online).
4. **Discount rate and flows.** FIIs fell from 25.9% to 15.3% since Dec 2023; the empirical US 10Y beta is -1.49 (t=-1.5).
5. **Input and FX costs.** Cotton and imports are small relative to the demand channel.

## Transmission examples
- **Middle East escalation -> Brent up -> fuel and food inflation -> real incomes squeezed -> discretionary apparel slows -> LFL growth down.** Order 2: inflation; order 3: RBI holds rates; order 4: urban EMI burden. For an 85x stock, a 3pp LFL miss can cost 8-10%.
- **Brent up -> USD/INR up -> imported garments/cosmetics dearer** (small, -0.5).
- **US 10Y up -> global growth de-rating -> FII selling -> Trent (holders 15.3%) falls**, as in the empirical beta.
- **Monsoon/good harvest -> rural wallet -> Zudio small-town stores**.
- **Wage growth -> aspirational spending -> Zudio price-point volumes.**

## Current situation
The Q2 business update on 2026-10-06 (revenue +23%) lifted the stock 10-13% to a two-year high; Q2 results on 2026-10-29 beat estimates with margin expansion and Zudio crossing 1,000 stores (+5-7%). Brokerages differ on outlook (BusinessLine 2026-10-30).

## Upcoming events
Q3 business update (January) and results (February 2027), store additions, festive-shift effects (Diwali 2026-11-08, model knowledge).

## Bull case
20%+ growth for three more years with margin at 19-20% justifies 70-80x forward earnings; emerging categories add margin.

## Bear case
LFL slips to low single digit, competition increases, multiple compresses from 85x to 55x: -35%.

## Uncertainties
Segment shares, cost splits and Inditex JV details are model estimates; press and screener PAT differ (Rs 468 cr vs Rs 490 cr).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.