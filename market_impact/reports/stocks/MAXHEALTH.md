# MAXHEALTH — Max Healthcare Institute Ltd.
*NIFTY_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.3%**, **12 months -1.1%** (rank 194 / 163 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.6%): 3 months 46%, 12 months 47%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.4% … P90 +1.1%; plausible 12m relative-return range incl. stock-specific noise: -33.8% … +31.1%
- Decomposition (12m): 0.5 × forward event exposure -0.8% (3m -0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -1.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -2.2% (beta-adjusted) vs a realised market-adjusted move of -6.2% — gap +4.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | -0.03 | -0.03 | -0.10 |
| Regulatory | +0.00 | -0.01 | -0.01 | -0.00 |
| Sector | -0.12 | +0.41 | +0.29 | +0.11 |
| Theme | +0.00 | +0.01 | +0.01 | +0.01 |
| Geopolitics | +0.00 | -0.04 | -0.04 | -0.04 |
| Company catalysts | -0.52 | +0.00 | -0.52 | -0.90 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.64 | -0.29 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-1.08** | **-1.31** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India NPPA/NLEM drug price control and trade-margin regulation (`NEW_NPPA_DRUG_PRICE_CONTROL`) | +1 = one tightening step (NLEM expansion or trade-margin cap) | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.44 | +3.50 | -0.09 | +0.01 | +0.02 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.48 | +2.20 | +0.32 | +0.01 | -0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.24 | -2.00 | -0.13 | -0.08 | -0.03 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.91 | +1.80 | +0.09 | +0.02 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.75 | +0.00 | -1.62 | -0.13 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.73 | +0.00 | -1.19 | -0.53 | -0.01 | +3.5% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.61 | +1.60 | +0.03 | +0.01 | -0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.42 | +0.00 | +0.00 | -0.81 | -0.60 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.40 | +0.00 | +0.84 | +0.36 | +0.20 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.32 | +0.00 | +0.62 | +0.68 | +0.02 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.23 | +0.00 | -1.26 | +0.03 | -0.00 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.11 | +0.00 | +1.02 | +0.07 | +0.01 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.10 | +0.00 | +1.12 | -0.02 | +0.00 | +1.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.6% | -7.6% | -7.7 | +0.2 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.6% | +4.3% | +8.8 | -0.3 | +0.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.3% | -2.3% | -2.0 | -0.1 | -0.1 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.9 | -0.2 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.7% | +1.7% | +1.8 | -0.0 | -0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.3% | -1.6% | +0.0 | -6.3 | -0.1 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -0.5 | -0.3 | -0.5 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.2% | +1.2% | +1.2 | +0.0 | -0.1 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -6.2% | -1.1% | -6.0 | +0.0 | -0.3 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.0 | -0.1 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -7.1% | -1.1% | +0.0 | -7.2 | +0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.8% | +1.0% | +0.0 | +1.0 | +0.7 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MAXHEALTH | +8.75% | +4.38% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MAXHEALTH | -5.25% | -0.95% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MAXHEALTH | -3.36% | -0.84% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → MAXHEALTH | -3.36% | -0.84% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MAXHEALTH | -2.00% | -0.84% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MAXHEALTH | -3.27% | -0.82% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → MAXHEALTH | +1.75% | +0.61% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → MAXHEALTH | +0.70% | +0.56% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MAXHEALTH | -2.00% | -0.54% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MAXHEALTH | -3.27% | -0.49% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ NEW_USDJPY → F_FPI_FLOWS → MAXHEALTH | -2.52% | -0.38% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → MAXHEALTH | -2.00% | -0.36% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MAXHEALTH | -1.31% | -0.33% |
| 2 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MAXHEALTH | +0.52% | +0.32% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_FPI_FLOWS → MAXHEALTH | +0.55% | +0.30% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → MAXHEALTH | -1.60 | events | -5.60% |
| 1 | F_REPO_IN → MAXHEALTH | +1.00 | events | -2.00% |
| 1 | F_GDP_IN → MAXHEALTH | +0.50 | events | +0.80% |
| 1 | F_URBAN_DEMAND → MAXHEALTH | +0.20 | events | +0.44% |
| 1 | F_USDINR → MAXHEALTH | -0.37 | observed | -0.37% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Supreme Court/NPPA follow-ups on medicine MRP and trade-margin caps | regulatory | 0.60 | -3.0% | -1.80% |
| 2027-02 | Q3 FY27 results: ARPOB, occupancy, new-bed ramp | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Commissioning of new hospital capacity (bed expansion per CLSA/management) | capex | 0.50 | +1.5% | +0.75% |
| 2027-04 | Possible index/MSCI rebalance given FII reduction (low confidence) | other | 0.20 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# MAXHEALTH (Max Healthcare Institute) — Nifty 50, as of 2026-11-05

## Business
Max Healthcare is the premium North-Indian multi-speciality hospital operator (Delhi NCR, Mohali, Dehradun, Lucknow, Mumbai, Nagpur and expanding). It has among the highest ARPOB and an EBITDA margin around 27%. Q2 FY27 (2026-10-30): consolidated revenue +20% YoY, consolidated PAT Rs 414 cr (-15%), network PAT Rs 448 cr (+10%). The screener pack shows narrower sales (Rs 2,569 cr, EBITDA Rs 711 cr, 28%) than the company's network figures (Q1 network sales Rs 2,982 cr), so growth rates are more reliable than absolute levels.

## What moves the stock (ranked)
1. **Drug price/MRP regulation** (-6.0 per tightening step): the stock slid ~20% in three weeks to a 2-year low after the Supreme Court (2026-09-30) questioned steep cancer-drug markups and floated a 16% MRP cap; the Centre cut cancer-drug prices ~30% in October. Oncology is a core Max speciality.
2. **FPI flows and sentiment** (+3.5): 40.5% FII holding and beta ~1.25; FIIs have trimmed from 45.4%.
3. **Discount rate** (-2.0 per +25bp): 64x P/E.
4. **Urban demand/GDP** (+2.2, +1.6) and **premiumisation** (+1.8).
5. **Wages** (-1.0).
6. **DXY/USD-INR**: empirical DXY +3.26 (t=2.5) contradicts the prior; flagged and shrunk.

## Transmission examples
- **SC order on MRP caps -> pharmacy/oncology margin cut -> EBITDA -7% -> P/E derating at 64x** (1st to 3rd order), partly offset by procedure re-pricing.
- **Fed hawkish -> DXY and US yields up -> FPI outflow -> FIIs trim a 40%-FII-owned stock -> liquidity-driven selloff -> cost of equity up for expansion** (3rd order).
- **Wage inflation (labour codes, doctor retention) -> costs up -> tariff hikes needed -> insurers resist -> occupancy mix shifts** (3rd order).
- **Monsoon/rural income strong -> urban/semi-urban affluence -> elective surgeries and health insurance take-up up -> occupancy up** (3rd order).

## Current situation
Post-slump recovery: +2.9% 1m, -13% 3m, -18% 12m. Brokers: ICICI Securities Buy Rs 1,300; PL Buy Rs 1,080; CLSA positive (2026-11-04). Competitors (Rainbow, Artemis, Yatharth) report 12-14% ARPOB growth with capacity adds.

## Upcoming events
SC/NPPA follow-ups (Dec), Q3 results (Feb 2027), new bed commissioning.

## Bull and bear
Bull: regulatory clarity and capacity ramp support 20% earnings CAGR, price Rs 1,200+. Bear: MRP caps extended to consumables, FII selling, wage squeeze; derates to 45x. Confidence medium; call details only via headlines.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.