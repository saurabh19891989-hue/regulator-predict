# GODFRYPHLP — Godfrey Phillips India Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months -0.1%** (rank 80 / 113 of 200 for 3m / 12m); beta 1.29
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +42.1%): 3 months 50%, 12 months 53%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.6% … P90 +2.4%; plausible 12m relative-return range incl. stock-specific noise: -52.8% … +55.5%
- Decomposition (12m): 0.5 × forward event exposure -0.8% (3m -0.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +3.4% (beta-adjusted) vs a realised market-adjusted move of -26.0% — gap +29.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.13 | +0.13 | +0.06 |
| Sector | +0.10 | +0.15 | +0.25 | +0.11 |
| Geopolitics | +0.00 | -0.05 | -0.05 | -0.03 |
| Company catalysts | +0.44 | +0.00 | +0.44 | +0.44 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.74 | -0.33 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.11** | **+0.15** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Cigarette excise / tobacco tax burden (India) (`NEW_TOBACCO_EXCISE`) | +10% rise in the tax burden per cigarette stick | -7.50 | -7.50 | +0.00 | +0.00 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.69 | -1.30 | -0.25 | -0.13 | -0.01 | +3.5% |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +1.51 | +1.50 | +0.00 | +0.01 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.30 | +0.00 | -0.90 | -0.22 | -0.19 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.25 | +1.20 | +0.05 | +0.01 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.24 | +1.20 | +0.00 | +0.04 | +0.00 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.96 | +0.00 | -0.52 | -0.36 | -0.08 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.90 | +0.00 | +0.81 | +0.04 | +0.04 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.80 | +0.70 | +0.00 | +0.06 | +0.04 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.75 | -0.50 | -0.23 | -0.04 | +0.02 | -1.1% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.66 | -0.40 | -0.12 | -0.13 | -0.00 | +0.0% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.59 | +0.00 | +0.45 | +0.15 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.54 | -0.50 | -0.03 | -0.01 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.50 | +0.00 | -0.58 | +0.10 | -0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.8% | -2.8% | -2.6 | -0.1 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.7% | +1.8% | +3.5 | +0.1 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.1% | -1.3% | -3.2 | -1.8 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.5% | +0.9% | +1.0 | +0.3 | +0.2 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -5.3% | -0.8% | -3.2 | -2.1 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.2% | -0.8% | -2.2 | -0.5 | -0.4 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -0.7% | -0.7% | -0.5 | -0.2 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.7 | +0.1 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.6% | +0.6% | +0.6 | +0.0 | -0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.2 | -0.1 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.5% | -0.5% | -0.5 | -0.0 | -0.0 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -3.0% | -0.5% | -2.9 | -0.0 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GODFRYPHLP | +3.00% | +1.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → GODFRYPHLP | -3.25% | -0.81% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → GODFRYPHLP | -3.25% | -0.49% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → GODFRYPHLP | -1.30% | -0.33% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → GODFRYPHLP | -1.80% | -0.32% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → GODFRYPHLP | +0.52% | +0.32% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → GODFRYPHLP | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → GODFRYPHLP | -1.15% | -0.29% |
| 2 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → T_FORMALISATION → GODFRYPHLP | +0.36% | +0.29% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GODFRYPHLP | +0.52% | +0.29% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → GODFRYPHLP | +0.52% | +0.29% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → GODFRYPHLP | +0.52% | +0.26% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → GODFRYPHLP | -0.94% | -0.23% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GODFRYPHLP | -0.88% | -0.22% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GODFRYPHLP | -0.50% | -0.21% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → GODFRYPHLP | -1.60 | events | -1.92% |
| 1 | F_REPO_IN → GODFRYPHLP | +1.00 | events | -0.50% |
| 1 | T_FORMALISATION → GODFRYPHLP | +0.30 | events | +0.45% |
| 1 | F_URBAN_DEMAND → GODFRYPHLP | +0.20 | events | +0.24% |
| 1 | F_USDINR → GODFRYPHLP | -0.37 | observed | +0.18% |
| 1 | F_RURAL_DEMAND → GODFRYPHLP | -0.25 | events | -0.17% |
| 1 | F_RISK_SENTIMENT → GODFRYPHLP | +0.11 | observed | -0.15% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → GODFRYPHLP | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → GODFRYPHLP | +0.30 | events | -0.01% |
| 1 | F_BRENT → GODFRYPHLP | +0.00 | observed | -0.00% |
| 3 | F_BRENT → F_CHEM_FEEDSTOCK → F_PACKAGING → GODFRYPHLP | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (trading window closed 28 Sep 2026; date unverified) | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | Further price hikes following ITC | other | 0.50 | +1.8% | +0.88% |

## Analyst profile (agent research, sourced)
# Godfrey Phillips India — what moves the stock

**Business.** A small cigarette maker (Four Square, Red & White, Cavanders, plus the Marlboro franchise) with a debt-free balance sheet and a large treasury book. Almost the whole profit pool is cigarettes, so the stock is a leveraged version of the tobacco-tax trade. Q1 FY27 (Jun 2026): sales Rs 1,206 cr, operating profit Rs 181 cr (15% margin versus 23%), PAT Rs 198 cr (screener.in, 2026-11-05). The stock is -40% over twelve months with 47% annualised volatility.

## Ranked drivers
1. **Cigarette tax regime (NEW_TOBACCO_EXCISE), about -7.5% per +10% tax burden.** Less price leadership than ITC; Godfrey follows ITC's hikes.
2. **Illicit trade and enforcement (T_FORMALISATION).** Weaker brands lose volume faster to untaxed sticks, so enforcement is a bigger upside here.
3. **Urban premium demand** (Marlboro/Four Square) and rural small-town demand (Red & White).
4. **Risk sentiment and FPI flows** because beta is 1.3-1.5 and float is 27%.
5. **Packaging, FX and rate effects** are second-tier.

## Worked transmission chains
- **Tax step -> price hike -> premium smokers trade down or switch to illicit -> volume down -> operating deleverage on fixed distribution costs -> margin down -> earnings down more than the tax itself (4th order).** Q1 EBITDA fell 46% on a 19% revenue drop.
- **Brent up -> INR weaker -> imported inputs dearer and CPI up -> RBI delays easing -> small-caps de-rate -> high-beta Godfrey falls more than ITC.**
- **Weak monsoon -> rural income hit -> small-town cigarette volume falls -> lower-priced Red & White brand underperforms.**
- **Global risk-off (VIX up) -> FPI selling of midcaps -> thin float magnifies the drop.**

## Current situation
After a 50% correction the company still has large reserves (Trade Brains 2026-09-23). Q2 results are due soon; the trading window closed 28 Sep 2026. No Q2 figures were found, so the Q2 numbers are an information gap.

## Upcoming
Q2 results (Nov 2026), Budget (1 Feb 2027), price hikes.

## Bull / bear
**Bull:** tax stability, illicit trade enforcement, big cash pile and buyback/dividend potential. **Bear:** tax steps, share loss to ITC, margin damage persisting, high beta. Confidence low: segment shares and Marlboro terms rely on model knowledge.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.