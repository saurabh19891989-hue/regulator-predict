# EICHERMOT — Eicher Motors Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months -0.1%** (rank 120 / 112 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 50%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.3% … P90 +1.6%; plausible 12m relative-return range incl. stock-specific noise: -27.5% … +29.4%
- Decomposition (12m): 0.5 × forward event exposure -0.5% (3m -0.5%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.2% (beta-adjusted) vs a realised market-adjusted move of +2.9% — gap -1.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.20 | -0.01 | +0.19 | -0.07 |
| Sector | -0.05 | +0.21 | +0.16 | +0.06 |
| Theme | +0.00 | -0.02 | -0.02 | -0.02 |
| Geopolitics | +0.01 | +0.04 | +0.05 | +0.04 |
| Company catalysts | +0.30 | +0.00 | +0.30 | +0.30 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.64 | -0.29 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.10** | **-0.07** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +6.43 | +4.00 | +1.84 | +0.41 | +0.17 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +4.50 | +4.50 | +0.00 | +0.00 | +0.00 | — |
| Competitive intensity in Indian two-wheelers/EV two-wheelers (`NEW_2W_COMPETITIVE_INTENSITY`) | +1 = price/share war episode | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.29 | +0.00 | +2.16 | +0.15 | -0.02 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.09 | +2.00 | +0.00 | +0.08 | +0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.05 | +2.00 | +0.01 | +0.02 | +0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.69 | +0.00 | +1.48 | +0.25 | -0.03 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.44 | +0.00 | -1.44 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.19 | -0.60 | -0.49 | -0.04 | -0.05 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.15 | +0.00 | -0.55 | -0.31 | -0.28 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.08 | +0.00 | -0.71 | -0.36 | -0.01 | +3.5% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.04 | +0.00 | -0.53 | -0.72 | +0.21 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.99 | +0.00 | -0.64 | -0.20 | -0.15 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.5% | -4.5% | -4.4 | -0.0 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.1% | +2.6% | +5.0 | +0.0 | +0.1 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.4% | +1.4% | +0.8 | +0.6 | -0.1 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.6 | -1.0 | +0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -0.9 | -0.3 | -0.1 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.1% | +1.1% | +1.0 | +0.1 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.8% | -0.9% | +0.0 | -3.7 | -0.3 | +0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.8 | -0.1 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.8% | -0.9% | -4.2 | -0.4 | -0.1 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.9 | +0.0 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.5% | +0.8% | +0.5 | +0.5 | +0.3 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → EICHERMOT | +5.00% | +2.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → EICHERMOT | -3.00% | -0.54% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → EICHERMOT | -2.16% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → EICHERMOT | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → EICHERMOT | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → EICHERMOT | -1.87% | -0.47% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → EICHERMOT | -0.80% | -0.40% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → EICHERMOT | +1.00% | +0.35% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → EICHERMOT | +0.40% | +0.32% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → EICHERMOT | +0.44% | +0.31% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → EICHERMOT | +0.52% | +0.29% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → EICHERMOT | -1.87% | -0.28% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → EICHERMOT | -0.60% | -0.25% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → EICHERMOT | +0.44% | +0.24% |
| 1 | EV_GST_RATE_CHANGE_APR27 ⇒ P_GST_CONSUMPTION → EICHERMOT | +0.80% | +0.24% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → EICHERMOT | -1.60 | events | -3.20% |
| 1 | F_AUTO_DEMAND_IN → EICHERMOT | +0.50 | director_override | +2.25% |
| 1 | F_GSEC_10Y_IN → EICHERMOT | +1.55 | director_override | -1.55% |
| 1 | F_STEEL_INDIA → EICHERMOT | +1.35 | events | -0.94% |
| 1 | F_REPO_IN → EICHERMOT | +1.00 | events | -0.60% |
| 1 | F_ALUMINIUM → EICHERMOT | -1.96 | observed | +0.59% |
| 1 | F_GOVT_CAPEX → EICHERMOT | +0.20 | director_override | +0.16% |
| 1 | F_USDINR → EICHERMOT | -0.37 | observed | -0.11% |
| 1 | F_EU_GDP → EICHERMOT | +0.22 | events | +0.11% |
| 1 | F_BRENT → EICHERMOT | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | New model launches / EV rollout (Flying Flea C6 sales in Europe) | other | 0.60 | +1.0% | +0.60% |
| 2026-12-01 | November sales print | other | 1.00 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results (Q2 FY27 reported ~2026-10-28; numbers not retrieved) | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Eicher Motors Ltd. (EICHERMOT) — Market Impact profile, 2026-11-05

## Business
Eicher owns Royal Enfield (RE), the global leader in 250-750cc motorcycles, and 50% of VECV, its heavy-vehicle joint venture with Volvo. RE earns an operating margin of 24-25% with almost no debt, and treasury income of Rs 2,260 cr lifts profit above operations. Exports are about 12-14% of RE volumes (UK, Europe, LatAm, ASEAN, Nepal, Bangladesh). Q1 FY27 sales were Rs 6,632 cr (+31% y/y) with PAT Rs 1,463 cr. September RE sales were 133,958 (+8%) and October motorcycles +7%, while VECV sales jumped 35% in October.

## What moves the stock (ranked)
1. **Domestic mid-premium demand (+4.5 per +10% industry volumes)** and RE's own launches/pricing.
2. **Discount rate / flows**: P/E 36; FIIs hold 24% (G-sec -1.0; F_FPI_FLOWS +2.0).
3. **GST policy (+4.0 per further cut)**: the 350cc threshold under GST 2.0 is crucial; reclassification is both an upside and a risk.
4. **Cost inputs**: steel (-0.7), aluminium (-0.3), where pass-through is partial.
5. **Competition (-2.5)** from Bajaj-Triumph, Honda, Hero-Harley and TVS.
6. **VECV cycle (+0.8)** via government capex and freight.
7. **Rates (-0.6), FX (+0.3), Brent (-0.4).**

## Transmission examples
- **Rate chain (3 orders).** Inflation from Brent $95+ -> RBI hikes to 5.50% (7 Oct) -> RE buyers' EMIs rise (60-65% financed) -> ticket sizes and discretionary buying slow -> RE volumes lag; but treasury income rises on higher yields, cushioning EPS.
- **Steel chain (3 orders).** China steel exports / global HRC +20.6% -> domestic steel +4-5% -> RE frame and tank cost up -> EBITDA margin -50bp -> price rise of 1-2% in January -> volumes mildly elastic.
- **GST chain (3 orders).** Government revisits the 40% rate on >350cc -> RE's 650 range falls into 18% -> on-road price -10% on 650s -> mix shifts up; ASP and margin improve.
- **Mideast chain (4 orders).** Hormuz escalation -> Brent >$100 -> INR weaker (94.5) -> exports in INR gain slightly, but petrol prices and CPI rise -> rate cuts delayed -> urban discretionary slows.
- **VECV chain (3 orders).** Govt capex up -> trucking demand -> CV orders -> VECV profit share up (~9% of PAT).

## Current situation
RE grows steadily. Q2 FY27 results were scheduled for 28 October; their numbers were not captured, so Q1 is the latest hard data. After a ~9% drop on 1 October (September sales), the stock recovered +8.8% in a month. Brokerages (Nuvama, Elara) list it among top auto picks. FIIs trimmed from 26.8% to 24.0% across six months.

## Upcoming events
Monthly sales (Dec 1), Q3 results (early Feb), Flying Flea European roll-out, Budget (1 Feb 2027).

## Bull case
Volume growth of 10%+, ASP growth, margin >25%, VECV up-cycle and export expansion with India's UK/EU trade deals.

## Bear case
Rate/cost headwinds, GST reversal, mid-premium competition and a valuation de-rating if growth slows. Limits: Q2 numbers not captured; cost shares and VECV profit share are estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.