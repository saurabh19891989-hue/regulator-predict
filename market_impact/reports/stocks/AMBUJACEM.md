# AMBUJACEM — Ambuja Cements Ltd.
*NIFTY_NEXT_50 · Construction Materials · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.2%**, **12 months +2.0%** (rank 55 / 55 of 200 for 3m / 12m); beta 1.13
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.5%): 3 months 56%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.4% … P90 +5.8%; plausible 12m relative-return range incl. stock-specific noise: -17.4% … +19.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.4 pp (model impact +2.8% beta-adjusted vs realised market-adjusted move -16.7%); forward event exposure +1.1% (3m -0.4%; half assumed priced); company-specific events +2.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian cement trade price (realisation) (`NEW_CEMENT_PRICE_IN`) | +Rs10/bag (~+2.5%) | +6.50 | +6.50 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.47 | +0.00 | -1.50 | -0.68 | -0.28 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.44 | +2.50 | +0.00 | -0.06 | -0.00 | — |
| International thermal coal price (`F_COAL_INTL`) | +15% seaborne thermal coal | -2.40 | -2.40 | +0.00 | +0.00 | +0.00 | +0.0% |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +2.38 | +2.00 | +0.40 | +0.00 | -0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.33 | +0.00 | -1.20 | -0.59 | -0.53 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.07 | +2.20 | +0.00 | -0.03 | -0.10 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.66 | -1.50 | -0.07 | -0.05 | -0.04 | +2.2% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.57 | -1.20 | -0.24 | -0.12 | -0.01 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.43 | +0.00 | -1.09 | -0.17 | -0.17 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.40 | -1.00 | -0.09 | -0.21 | -0.09 | +0.0% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.19 | +0.00 | +0.00 | -0.83 | -0.37 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.02 | +0.00 | +0.64 | +0.11 | +0.26 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.01 | -0.60 | -0.10 | -0.17 | -0.15 | -1.1% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -1.7 | -0.8 | -0.3 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.7% | +1.7% | +2.2 | -0.1 | -0.2 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.2 | -0.4 | +0.0 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.7% | +1.5% | +1.8 | +0.0 | -0.0 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.3% | +1.3% | +1.3 | +0.2 | +0.6 | +0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | -0.6 | -0.2 | -0.2 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.8% | -0.9% | -2.2 | -0.9 | -0.4 | -0.3 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | +0.9% | +0.9% | +1.0 | +0.0 | +0.0 | -0.1 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.5 | +0.1 | +0.2 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.4 | -0.2 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.8 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | -0.5 | -0.0 | -0.2 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → AMBUJACEM | +1.76% | +1.58% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → AMBUJACEM | +1.30% | +0.72% |
| 1 | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → AMBUJACEM | -1.20% | -0.60% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → AMBUJACEM | -2.20% | -0.55% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → AMBUJACEM | -0.80% | -0.54% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → AMBUJACEM | -1.20% | -0.50% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → AMBUJACEM | +1.32% | +0.40% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → AMBUJACEM | -1.38% | -0.35% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → AMBUJACEM | -0.40% | -0.34% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → AMBUJACEM | -1.20% | -0.32% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_DXY → AMBUJACEM | -0.45% | -0.32% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → AMBUJACEM | +0.53% | +0.32% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → AMBUJACEM | -0.48% | -0.29% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COAL_INTL → AMBUJACEM | -0.77% | -0.27% |
| 1 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → AMBUJACEM | +0.80% | +0.26% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOVT_CAPEX → AMBUJACEM | +1.00 | events | +2.20% |
| 1 | F_COAL_INTL → AMBUJACEM | +0.70 | director_override | -1.68% |
| 1 | F_MONSOON → AMBUJACEM | -1.56 | events | +1.25% |
| 1 | F_REPO_IN → AMBUJACEM | +1.00 | events | -1.20% |
| 1 | F_DXY → AMBUJACEM | +0.74 | observed | -1.11% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → AMBUJACEM | +1.55 | director_override | -0.93% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → AMBUJACEM | +0.50 | events | +0.30% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → AMBUJACEM | +1.00 | events | -0.26% |
| 1 | F_USDINR → AMBUJACEM | -0.37 | observed | +0.22% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → AMBUJACEM | +1.00 | events | -0.20% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → AMBUJACEM | +1.35 | events | -0.14% |
| 1 | F_BRENT → AMBUJACEM | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Realisation of Rs12-15/bag price hikes in Nov-Dec (industry attempt to offset fuel) | other | 0.50 | +4.0% | +2.00% |
| 2026-11 | Stock in F&O ban list on 22 Oct (high open interest); exit normalises liquidity | other | 0.50 | +0.0% | +0.00% |
| 2026-12 | Board/regulatory clearances and groundbreaking for the 30 MTPA Rs14,500 cr expansion; environmental clearances and land are the timing risk | capex | 0.60 | +1.0% | +0.60% |
| 2027-01 | Q3 FY27 results (date not announced; estimate late Jan/Feb 2027) | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | Intra-group consolidation of ACC/Orient/Penna/Sanghi into Ambuja (status unverified, model knowledge as of mid-2026) | corporate_action | 0.30 | +1.0% | +0.30% |
| 2027-06 | Renewed US/regulatory legal escalation against Adani Group (status after June 2026 not verified) | litigation | 0.10 | -9.5% | -0.95% |

## Analyst profile (agent research, sourced)
# AMBUJACEM — Ambuja Cements Ltd. (as of 2026-11-05)

*Facts come from screener.in (via the evidence pack) and Google News headlines dated Sep-Nov 2026. Publisher article bodies returned 403, so figures quoted only in headlines are flagged as headline-reported. Items marked "model knowledge" are from memory (cutoff ~June 2026). No expected-return number is given; the Director derives that from the graph.*

## Business
Ambuja is the Adani Group's cement flagship. With ACC, Orient Cement, Penna and Sanghi consolidated it is India's second-largest cement group (structure per model knowledge; the pack's "31 Mt" description is stale). Q2 FY27 sales volume was 16.5 Mt (NDTV Profit headline), revenue Rs 9,197 cr, EBITDA Rs 1,271 cr, which is about Rs 770/t. Promoters hold 67.3%, FIIs 5.7%, DIIs 19.4%, and the balance sheet is almost debt-free, so the equity trades as a cash-generating, long-duration asset (P/E 31.6 on depressed TTM EPS, P/B 1.6). The stock is Rs 385, down 32% in 12 months and 15% over 6 months.

## What moves the stock (ranked by absolute weight x current shock)
1. **Cement price (NEW_CEMENT_PRICE_IN, +6.5 per Rs10/bag).** Prices decide margins more than anything: a Rs 10/bag move is about 18% of EBITDA. Nomura (12 Oct) says Rs 12-15/bag hikes are needed merely to offset fuel costs; ET EnergyWorld (30 Sep) reported hikes of up to Rs 15/bag in October. Whether they stick is the single biggest swing.
2. **Kiln fuel: petcoke and imported coal (F_COAL_INTL, -2.4 per +15%).** Fuel and power are roughly 27% of costs. Seaborne coal is flat over six months in the factor table (+0.0%), but petcoke delivered to India has risen with freight (ChemAnalyst 22 Oct), which is why Q2 OPM fell to 14% from 19%.
3. **Group contagion (ADANIENT, +0.25 per 1%) and the F_DXY/flow channel.** Ambuja moves with Adani Enterprises on legal and financing news; it rose 5% on 2 Nov in a group rally. The strongest empirical beta is DXY (-2.4 per +3%, t -2.8), a flows proxy.
4. **Housing and government capex (+2.5 and +2.2 per SSU).** Together about 90% of demand. The RBI hike of 7 Oct (repo 5.50%, "calibrated tightening") is a 3-12 month headwind for housing.
5. **Discount rate (F_REPO_IN, -1.2 per 25 bp).** Net cash means little cost effect; it works through the multiple.
6. **Brent and freight (F_BRENT, -1.0 per +10%).** Diesel-linked road freight; empirical -0.81, t -1.8.
7. **FX, royalty, monsoon, housing policy:** each below 1% of equity per SSU in size.

## Transmission examples
- **Middle East escalation -> fuel -> margins (4 steps).** C_MIDEAST_CONFLICT up -> Brent and seaborne freight up (1st) -> petcoke landed cost and diesel up (2nd) -> kiln-fuel and freight costs rise ~Rs 150-250/t unless prices rise (3rd) -> EBITDA/t falls, the industry tries Rs 10-15/bag hikes, volumes soften as dealers resist (4th). Net sign: negative, partially offset when price discipline holds.
- **Brent up -> rupee weaker -> RBI stays tight -> housing demand weaker -> cement volumes weaker.** Brent at $95 widens the import bill, USD/INR (94.5) weakens, RBI has already hiked (7 Oct) and signals no cuts near term, mortgage rates stay high, housing sales slow, and the ~65% of cement demand tied to housing grows slower (2.5 per 10% sales move). Sign: negative, lag 3-12 months.
- **Adani-group stress -> Ambuja.** A negative legal or funding headline for ADANIENT -> group-wide sell-off -> Ambuja falls ~0.25x despite unchanged cement fundamentals; reversed in rallies like 2 Nov.
- **Government capex up -> roads and railways -> clinker demand -> operating leverage.** +10% central+state capex -> +1.4% volume -> ~5% EBITDA at current 14% OPM -> equity +2.2%.
- **Cement price hikes -> inflation -> RBI.** Each Rs 10/bag adds ~0.02pp to CPI; minor, so no feedback modelled.

## Current situation
Q2 FY27 (29 Oct): revenue Rs 9,197 cr (flat y/y), EBITDA down 28%, OPM 14% vs 19% a year ago. Headline net profit Rs 236 cr (-90%) reflects a Sep-2025 base lifted by one-offs; ET reports Rs 114 cr on a tax reversal, so definitions differ. Management targets 8% trade volume growth and Rs 4,250/t cost in FY27 (scanx headline). On 2 Nov it announced a Rs 14,500 cr, 30 MTPA expansion towards 155 MTPA by FY30; Nomura kept Buy but cut the target. The stock was in the F&O ban list on 22 Oct and has rebounded 6.5% in a month. Peers: UltraTech's Q2 (19 Oct) showed 21% profit growth on volume and efficiency with OPM 16%; Nuvama stays neutral on rising costs.

## Upcoming
Price-hike realisation (Nov-Dec); Q3 FY27 results (~late Jan/Feb 2027, date not announced); expansion approvals; Union Budget 1 Feb 2027 (infra/housing); possible intra-group mergers (status unverified); RBI December policy.

## Bull case
Hikes stick, petcoke eases, cost/t falls toward Rs 4,250, EBITDA/t rebuilds above Rs 1,000, group sentiment recovers and FIIs return; the stock re-rates from 31x depressed earnings to a 15x EV/EBITDA on higher EBITDA.

## Bear case
Fuel inflation persists, UltraTech's capacity push triggers a price war, the 30 MTPA capex (15% of market cap) earns below cost of capital, and an Adani-group legal escalation hits the stock regardless of fundamentals.

## Uncertainties
Article bodies were not read; segment/cost shares and demand splits are model estimates; net cash level and consolidated structure not verified from filings; the Q2 net-profit figures conflict across publishers. The empirical DXY sensitivity is treated as a flows proxy.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.