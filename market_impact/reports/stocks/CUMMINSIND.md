# CUMMINSIND — Cummins India Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.4%** (rank 75 / 63 of 200 for 3m / 12m); beta 0.94
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.3%): 3 months 52%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.4% … P90 +3.1%; plausible 12m relative-return range incl. stock-specific noise: -25.4% … +22.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.1 pp (model impact +6.2% beta-adjusted vs realised market-adjusted move -31.0%); forward event exposure -0.5% (3m -0.2%; half assumed priced); company-specific events -0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Genset / engine price competition in India (`NEW_GENSET_PRICE_COMPETITION`) | +5 pp realised-price erosion in the domestic genset/engine market | -7.00 | -7.00 | +0.00 | +0.00 | +0.00 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +4.82 | +5.00 | +0.00 | -0.19 | +0.01 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +4.13 | +4.00 | +0.14 | +0.00 | -0.01 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.81 | +2.50 | +0.34 | +0.06 | -0.09 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.28 | +2.30 | +0.00 | -0.02 | +0.00 | +1.2% |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +1.91 | +0.00 | +1.60 | +0.31 | -0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.64 | +0.00 | -1.09 | -0.44 | -0.11 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.40 | +0.00 | -0.90 | -0.24 | -0.25 | — |
| US growth (`F_US_GDP`) | +1 pp | +1.35 | +0.00 | +1.66 | -0.11 | -0.19 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.27 | +0.00 | -0.87 | +0.04 | -0.44 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.24 | -1.00 | -0.17 | -0.02 | -0.05 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.08 | +0.00 | -0.80 | -0.20 | -0.09 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.02 | +0.00 | -0.98 | +0.00 | -0.04 | +3.5% |
| International thermal coal price (`F_COAL_INTL`) | +15% seaborne thermal coal | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.8% | +2.8% | +2.5 | +0.5 | -0.2 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -10.3% | -2.6% | -6.9 | -2.8 | -0.4 | -0.2 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.3% | +2.0% | +2.0 | +0.3 | +0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.3 | -0.5 | -0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.8% | +1.8% | +0.0 | +1.7 | +0.1 | -0.1 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -6.5% | -1.6% | -6.9 | +0.4 | -0.2 | +0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.0 | -0.3 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.9 | -0.4 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.1% | -1.1% | -0.8 | -0.3 | -0.0 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -0.9% | -0.9% | -0.9 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.5% | +0.8% | +0.0 | +0.7 | +0.6 | +0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.7 | -0.2 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CUMMINSIND | +2.00% | +1.80% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → CUMMINSIND | -6.90% | -1.72% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → CUMMINSIND | -6.90% | -1.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → CUMMINSIND | -2.88% | -0.72% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → CUMMINSIND | +0.92% | +0.57% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_US_EQUITIES → CUMMINSIND | -3.45% | -0.52% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → CUMMINSIND | +1.50% | +0.45% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → C_GCC → CUMMINSIND | +0.80% | +0.44% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → CUMMINSIND | -1.00% | -0.42% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → CUMMINSIND | +0.60% | +0.36% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_PRIVATE_CAPEX → CUMMINSIND | +0.32% | +0.29% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → CUMMINSIND | -1.15% | -0.29% |
| 2 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → T_DATA_CENTRES_IN → CUMMINSIND | +0.32% | +0.27% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → CUMMINSIND | -1.00% | -0.27% |
| 2 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → F_US_EQUITIES → CUMMINSIND | -0.37% | -0.26% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOVT_CAPEX → CUMMINSIND | +1.00 | events | +2.50% |
| 1 | F_STEEL_INDIA → CUMMINSIND | +1.35 | events | -1.08% |
| 1 | F_REPO_IN → CUMMINSIND | +1.00 | events | -1.00% |
| 1 | F_COAL_INTL → CUMMINSIND | +0.70 | director_override | -0.70% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → CUMMINSIND | +1.00 | events | +0.64% |
| 1 | F_ALUMINIUM → CUMMINSIND | -1.96 | observed | +0.59% |
| 1 | F_US_EQUITIES → CUMMINSIND | +0.23 | observed | +0.54% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → CUMMINSIND | +0.50 | events | +0.50% |
| 1 | P_US_TARIFF_INDIA → CUMMINSIND | -0.60 | events | +0.42% |
| 2 | F_GOVT_CAPEX → F_PRIVATE_CAPEX → CUMMINSIND | +1.00 | events | +0.40% |
| 2 | T_ENERGY_TRANSITION → F_PRIVATE_CAPEX → CUMMINSIND | +0.50 | events | +0.30% |
| 2 | F_CREDIT_SPREADS_IN → F_PRIVATE_CAPEX → CUMMINSIND | +0.50 | events | -0.30% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Management/analyst follow-up: brokerages cut estimates and targets after the Q2 miss; possible further de-rating or stabilisation | guidance | 0.80 | -1.0% | -0.80% |
| 2027-02 | Q3 FY27 results (Dec-2026 quarter): test of whether OPM recovers from 15% | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | US EPA heavy-duty emission regulation outcome affecting Cummins Inc. group sentiment (indirect) | regulatory | 0.30 | -0.5% | -0.15% |
| 2027-05 | Q4 FY27 results and final dividend declaration | results | 0.95 | +0.0% | +0.00% |
| 2027-06 | Large data-centre/commercial genset order announcements or evidence of data-centre order slowdown | other | 0.40 | +0.5% | +0.20% |

## Analyst profile (agent research, sourced)
# CUMMINSIND — Cummins India Ltd. (profile as of 2026-11-05)

Sources: pack `market_impact/data/packs/CUMMINSIND.md` (screener.in, Yahoo, Google News headlines), web-search summaries of Q1 FY27 and Q2 FY26 coverage; segment and cost splits are model estimates and labelled low confidence. No expected-return number is given here; the Director computes it from the graph.

## Business
Cummins India is the 51%-owned Indian subsidiary of Cummins Inc. It makes diesel and alternative-fuel engines and gensets (up to 3 MW), alternators, filtration and components, and earns a large aftermarket stream. Power Generation is the biggest segment and includes the data-centre backup boom; Industrial serves rail, mining and construction; Distribution is parts and service. It is debt-free, pays ~70% of profits out and earns a ~30% ROE, which is why the stock carries a P/E near 50.

## What moves the stock (ranked)
1. **Genset price/mix competition and cost recovery (w about -7 per +5 pp price erosion).** The Sep-2026 quarter shows sales +4% YoY but OPM at 15% against 22% a year earlier and 18% in the June quarter. Whatever the exact split between price, mix (low-margin large data-centre sets), warranty and lagged pass-through of metals, this is the single largest driver and currently trending the wrong way. The earnings call was not retrieved, so the cause is unverified.
2. **Private capex (+5 per +10% growth)** and **data-centre build-out (+4 per theme unit)**: both lift volumes, but data-centre orders are lumpy and priced aggressively.
3. **Government capex (+2.5)**, **GCC/export demand (+1)**.
4. **Metal costs:** steel (-0.8), copper (-0.8), aluminium (-0.3). Pass-through exists but lags one to two quarters, so spikes hurt in the quarter they occur.
5. **Rates and risk sentiment:** repo +25 bp ≈ -1 (valuation duration); US equities/AI sentiment +2.3 (empirical t=+3.1); this is how the stock co-moves with global AI-capex mood, and it was hit on the 2026-10-13/15/30 AI sell-off days along with other power-equipment names.

## Transmission examples
- **Middle East escalation (4th order):** Escalation -> Brent up (even though Brent is -5.6% over a month, it is +15% over 3 months) -> diesel and freight up and INR weaker -> input and imported-component costs up while Indian industrial customers delay capex (private capex down) -> genset and industrial-engine volumes soften and discounting rises -> margin falls further from an already depressed 15%. A countervailing channel: GCC infrastructure spending rises with oil prices -> export gensets up.
- **Data-centre boom (3rd order):** AI capex up -> hyperscaler Indian data-centre commitments -> colocation operators order large backup gensets -> Cummins volume and order book up, but buyers are sophisticated, price competition from Caterpillar/Rolls-Royce/Kirloskar rises, and large-kVA sets are lower margin -> revenue up with margin flat/down. The pack's +2.5 beta to the S&P is the same channel seen from the market side.
- **Rates path (3rd order):** US 10-year yield stays near 4.9% -> FPI outflow pressure and weaker INR -> RBI holds repo -> private capex financing stays costly -> industrial order intake slows -> valuation multiple compresses at P/E 50.
- **Metals (2nd order):** China stimulus lifts copper/aluminium -> alternator and casting costs up -> Cummins raises price lists after a lag -> temporary EBITDA squeeze, and customers pre-buy before price hikes (small short-term volume pull-forward).

## Current situation
Q2 FY27 results (2026-11-04/05): net profit about Rs 507 cr (-18% YoY, one outlet reports Rs 467 cr), stock down 10-15% on the day and about 23% over three months, far below the 12-month high of Rs 6,143. FIIs trimmed to 19.5% from 21.2%. UBS cut its target on 2026-09-30 citing EPA regulation concerns at the parent. HDFC Sky (2026-10-01) still called it a capex-revival winner, which shows the debate: strong demand but compressing profitability. Conflicting figures between outlets (Rs 3,247 cr vs Rs 3,301 cr sales; Rs 467 cr vs Rs 507 cr profit) reflect consolidated vs standalone or exceptional items and were not reconciled.

## Upcoming events
Q3 FY27 results around February 2027 (key test of margin recovery); Q4 results and dividend in May 2027; ongoing broker estimate cuts in November-December 2026; data-centre order flow; US EPA rule developments for the parent.

## Bull case
The Q2 margin hit is mix- and timing-related; Q3-Q4 OPM returns to 18-20%; data-centre and infrastructure backlog converts; aluminium and copper deflation helps costs; the 15% drop resets valuation to a more reasonable P/E of ~40 and it re-rates on delivery.

## Bear case
Genset pricing has structurally reset (new capacity and competition), OPM settles at 15-17%, growth drifts to single digits, and a P/E of 50 compresses toward 30-35 as earnings estimates fall another 10-15%. Parent-level EPA/regulatory pressure and an AI-capex slowdown add downside; data-centre revenue stops contributing at the previous scale.

## Uncertainties
Earnings call commentary, order book and segment disclosures were not retrieved. Overall confidence: low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.