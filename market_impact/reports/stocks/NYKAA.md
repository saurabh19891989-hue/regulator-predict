# NYKAA — FSN E-Commerce Ventures Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.5%**, **12 months -0.3%** (rank 158 / 123 of 200 for 3m / 12m); beta 1.02
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.9%): 3 months 48%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.2% … P90 +2.1%; plausible 12m relative-return range incl. stock-specific noise: -32.5% … +32.3%
- Decomposition (12m): 0.5 × forward event exposure -0.2% (3m -0.3%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -1.8% (beta-adjusted) vs a realised market-adjusted move of +25.3% — gap -27.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.09 | +0.01 | +0.10 | -0.05 |
| Regulatory | +0.00 | -0.02 | -0.02 | -0.01 |
| Sector | +0.00 | +0.42 | +0.42 | +0.23 |
| Theme | +0.03 | -0.01 | +0.02 | -0.01 |
| Geopolitics | +0.00 | -0.05 | -0.05 | -0.04 |
| Company catalysts | -0.08 | +0.00 | -0.08 | -0.28 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.59 | -0.26 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.33** | **-0.52** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +6.07 | +6.00 | +0.00 | +0.08 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.08 | +3.00 | +0.84 | +0.23 | +0.01 | — |
| Beauty retail competition intensity (Tira, Sephora, Purplle, quick commerce) (`NEW_BEAUTY_RETAIL_COMPETITION`) | +1 = materially sharper discounting/expansion by rival beauty retailers and q-commerce | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.63 | +2.50 | +0.09 | +0.01 | +0.03 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.25 | +2.00 | +0.24 | +0.00 | +0.01 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.77 | -1.50 | -0.25 | -0.07 | +0.05 | +9.4% |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.74 | +0.00 | +1.92 | -0.26 | +0.08 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.57 | -1.00 | -0.48 | -0.14 | +0.05 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.55 | +0.00 | -1.05 | -0.48 | -0.01 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.53 | +0.00 | +0.00 | -0.89 | -0.65 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.45 | +0.00 | -1.74 | +0.38 | -0.10 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.28 | -1.00 | -0.20 | -0.05 | -0.03 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.19 | +0.00 | +0.44 | +0.74 | +0.01 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.05 | +0.00 | +0.60 | +0.29 | +0.16 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.8% | -5.8% | -5.5 | -0.2 | -0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.6% | +3.3% | +6.2 | +0.3 | +0.0 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | -1.8 | -0.6 | -0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.1% | -2.1% | -1.2 | -0.7 | -0.2 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -2.0 | +0.4 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.6% | +1.6% | +1.6 | +0.1 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.4% | +1.4% | +1.2 | +0.2 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.0 | -0.2 | -0.1 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -6.6% | -1.2% | -6.0 | -0.2 | -0.3 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -4.7% | -1.2% | +0.0 | -5.0 | +0.1 | +0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.9% | +1.0% | +0.0 | +1.1 | +0.7 | +0.1 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.8 | -0.2 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NYKAA | +6.25% | +3.12% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → NYKAA | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → NYKAA | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → NYKAA | -2.40% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NYKAA | -2.33% | -0.58% |
| 2 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → F_URBAN_DEMAND → NYKAA | +0.58% | +0.46% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → NYKAA | +1.25% | +0.44% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → NYKAA | -1.00% | -0.42% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → NYKAA | +0.50% | +0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → F_US_10Y → NYKAA | +1.53% | +0.38% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NYKAA | -2.33% | -0.35% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_US_10Y → NYKAA | -0.45% | -0.32% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_US_10Y → NYKAA | -0.75% | -0.30% |
| 2 | EV_CPI_BREACH_6PCT ⇒ F_CPI_IN → F_URBAN_DEMAND → NYKAA | -0.48% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_10Y → NYKAA | +1.12% | +0.28% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → NYKAA | -1.60 | events | -4.00% |
| 1 | F_US_10Y → NYKAA | +1.68 | observed | -2.51% |
| 1 | F_URBAN_DEMAND → NYKAA | +0.20 | events | +1.20% |
| 1 | F_REPO_IN → NYKAA | +1.00 | events | -1.00% |
| 1 | F_USDINR → NYKAA | -0.37 | observed | +0.37% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Completion of Simply Nam 82% stake acquisition | corporate_action | 0.80 | +0.2% | +0.20% |
| 2026-12 | Block deals / promoter or PE sell-downs into strength | corporate_action | 0.30 | -2.5% | -0.75% |
| 2027-02 | Q3 FY27 results (festive quarter, highest GMV) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Index rebalancing candidate (Nifty Next 50 inclusion given Rs ~1 lakh cr market cap) | other | 0.20 | +2.0% | +0.40% |

## Analyst profile (agent research, sourced)
# NYKAA (FSN E-Commerce Ventures Ltd.) - company profile as of 2026-11-05

## Business
Nykaa is India's largest omnichannel beauty retailer with a growing fashion arm and owned brands. TTM sales are Rs 11,309 cr (+28%) with EBITDA of Rs 951 cr (8.4%, up from 4.3% in FY22). Q2 FY27 (Sep 2026) sales were Rs 3,006 cr (+28%), EBITDA Rs 263 cr and PAT Rs 101 cr, about three times last year (Economic Times, 2026-11-04). The shares (Rs 347) are +38% in 12 months at a P/E near 300 and 60x book (screener.in pack, 2026-11-05).

## What moves the stock (ranked)
1. **Execution on growth and margin.** The stock is a call on 25%+ growth and 100-200 bp annual margin expansion; each 100 bp of margin is about 11% of EBITDA.
2. **Urban discretionary demand.** Beta around 1.2 to urban consumption: +5pp urban growth is worth about +6 equity points.
3. **Discount rates.** P/E of 300 makes the stock the most rate-sensitive in this batch; the empirical US 10Y beta is -1.67 per +25 bp (t=-2.4).
4. **Competition.** Tira (Reliance), Sephora, Purplle, e-commerce giants and quick commerce.
5. **Flows and supply.** FIIs bought (12.4% -> 15.65%) while DIIs sold (25.35% -> 22.35%), so the marginal buyer is foreign.

## Transmission examples
- **Middle East escalation -> Brent up -> US 10Y and risk-off up -> growth stocks de-rate.** Order 2: US 10Y rises 25 bp (about -1.5%); order 3: FPI outflows; order 4: Nykaa's FII-heavy register amplifies. Brent also lifts India's inflation and delays RBI easing.
- **Brent up -> USD/INR up -> imported beauty brands dearer.** Imported brands and ingredients are ~10% of COGS; a 3% rupee fall costs about 2.5% of EBITDA before price actions.
- **RBI holds rates -> urban EMI burden -> discretionary spending slows.** Beauty has proven resilient but premium fashion is more cyclical.
- **Quick commerce expansion -> beauty replenishment shifts to 10-minute apps -> Nykaa's app frequency falls** (competition) but its brands also sell there.

## Current situation
Q2 revenue +28%, PAT triple; fashion profitable; Nomura and Jefferies hiked targets on 2026-11-05; board agreed to buy 82% of Simply Nam, a premium makeup brand.

## Upcoming events
Q3 FY27 festive-quarter results (February 2027), Simply Nam closing, possible block deals, potential index inclusion.

## Bull case
Growth 25% with 100 bp annual margin expansion supports 40% EPS growth for 3 years, justifying part of the multiple; owned brands raise gross margin.

## Bear case
Competition forces discounting, margins stall near 8-9% and growth slows to the teens; at P/E 300 the stock can fall 30%+.

## Uncertainties
Revenue mix and cost shares are model estimates; no company filings fetched beyond the screener pack and headlines.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.