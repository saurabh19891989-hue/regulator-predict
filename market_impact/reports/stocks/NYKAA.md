# NYKAA — FSN E-Commerce Ventures Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.1%**, **12 months -1.5%** (rank 134 / 124 of 200 for 3m / 12m); beta 1.02
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.9%): 3 months 47%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.3% … P90 +2.6%; plausible 12m relative-return range incl. stock-specific noise: -33.4% … +24.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.8 pp (model impact -1.7% beta-adjusted vs realised market-adjusted move +25.3%); forward event exposure +1.1% (3m +0.8%; half assumed priced); company-specific events -0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +5.99 | +6.00 | +0.00 | +0.01 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.15 | +3.00 | +0.84 | +0.30 | +0.01 | — |
| Beauty retail competition intensity (Tira, Sephora, Purplle, quick commerce) (`NEW_BEAUTY_RETAIL_COMPETITION`) | +1 = materially sharper discounting/expansion by rival beauty retailers and q-commerce | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.65 | +2.50 | +0.09 | +0.01 | +0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.55 | +0.00 | -2.31 | -0.04 | -0.20 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.24 | +2.00 | +0.24 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.99 | +0.00 | +0.00 | -1.01 | -0.98 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.87 | -1.50 | -0.25 | -0.11 | -0.01 | +9.4% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.74 | +0.00 | -1.05 | -0.60 | -0.08 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -1.73 | +0.00 | -1.33 | -0.31 | -0.08 | +2.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.70 | -1.00 | -0.48 | -0.21 | -0.02 | -1.1% |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.52 | +0.00 | +1.92 | -0.35 | -0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.43 | +0.00 | -0.62 | -0.67 | -0.15 | +0.0% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.37 | +0.00 | +0.80 | +0.48 | +0.09 | +1.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -7.9% | -7.9% | +0.0 | -3.0 | -3.8 | -1.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.9% | -5.9% | -5.5 | -0.3 | -0.0 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -4.1% | -4.1% | -2.5 | -1.4 | -0.2 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.7% | -3.7% | -2.2 | -1.3 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.7% | +3.3% | +6.2 | +0.3 | +0.0 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -2.7 | -0.0 | -0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.5% | -2.5% | -1.2 | -0.9 | -0.3 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.7% | -2.0% | +0.0 | -2.8 | -2.4 | -0.5 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -7.1% | -2.0% | +0.0 | -6.6 | -0.6 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.1% | +1.8% | +0.0 | +1.5 | +1.3 | +0.3 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -9.4% | -1.7% | +0.0 | -8.3 | -0.9 | -0.2 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.6% | +1.6% | +1.6 | +0.1 | +0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → NYKAA | -5.50% | -5.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NYKAA | +6.25% | +3.12% |
| 1 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → NYKAA | -2.55% | -2.55% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → NYKAA | -2.25% | -2.25% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → NYKAA | -1.56% | -1.56% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → NYKAA | -1.49% | -1.49% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → NYKAA | -1.32% | -1.32% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → NYKAA | +1.25% | +1.25% |
| 1 | EV_FED_SEP26_HIKE ⇒ F_US_10Y → NYKAA | -1.20% | -1.20% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → NYKAA | +1.20% | +1.20% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → NYKAA | -1.17% | -1.17% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_URBAN_DEMAND → NYKAA | -1.10% | -1.10% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → NYKAA | -3.73% | -1.05% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → NYKAA | -1.00% | -1.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → NYKAA | -0.89% | -0.89% |

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