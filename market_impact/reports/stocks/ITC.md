# ITC — ITC Ltd.
*NIFTY_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +0.3%** (rank 96 / 90 of 200 for 3m / 12m); beta 0.70
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.3%): 3 months 50%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.8% … P90 +2.0%; plausible 12m relative-return range incl. stock-specific noise: -10.9% … +11.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.2% beta-adjusted vs realised market-adjusted move -3.5%); forward event exposure +2.6% (3m +1.5%; half assumed priced); company-specific events +0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Cigarette excise / tobacco tax burden (India) (`NEW_TOBACCO_EXCISE`) | +10% rise in the tax burden per cigarette stick | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.37 | +1.40 | +0.00 | -0.00 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.14 | +0.80 | +0.25 | +0.09 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.13 | +1.20 | -0.09 | +0.01 | +0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +0.98 | +1.00 | +0.00 | -0.01 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.90 | +0.00 | -0.60 | +0.05 | -0.36 | — |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +0.81 | +0.80 | +0.00 | +0.01 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.75 | +0.00 | -0.65 | -0.08 | -0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +0.70 | +1.00 | -0.24 | -0.08 | +0.02 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.70 | -0.60 | -0.08 | -0.01 | -0.01 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.64 | +0.00 | -0.55 | -0.00 | -0.09 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.59 | -0.50 | +0.07 | -0.13 | -0.02 | +0.0% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.54 | +0.00 | +0.32 | +0.06 | +0.16 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.53 | +0.00 | +0.66 | -0.07 | -0.05 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.5% | -2.5% | -2.6 | +0.2 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.8% | +1.4% | +3.0 | -0.3 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.9 | -0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.7% | -0.7% | -0.6 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.4 | -0.1 | -0.2 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.5% | +0.5% | +0.6 | -0.1 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.0% | +0.5% | +0.7 | +0.0 | +0.2 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -1.8% | -0.5% | -1.1 | -0.2 | -0.5 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -1.8% | -0.4% | +0.0 | -2.0 | +0.2 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.4% | -0.4% | +0.0 | -0.4 | -0.0 | -0.0 |
| India 2027 wheat crop (harvest Mar-Apr 2027) below 2026's record ~120 MT (`EV_WHEAT27_CROP_BELOW`) | anticipated | 0.65 | -0.7% | -0.4% | -0.5 | +0.0 | -0.1 | -0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.4% | -0.4% | -0.4 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ITC | +3.00% | +1.50% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ITC | +0.65% | +0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ITC | -1.80% | -0.32% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → ITC | +0.42% | +0.29% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ITC | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ITC | -1.15% | -0.29% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ITC | -1.12% | -0.28% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ITC | -1.10% | -0.28% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ITC | -0.60% | -0.25% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → ITC | +1.30% | +0.23% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → ITC | +0.42% | +0.23% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → ITC | +0.32% | +0.22% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → ITC | +0.60% | +0.21% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → ITC | +0.24% | +0.19% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → ITC | +0.28% | +0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ITC | -1.60 | events | -1.92% |
| 1 | F_REPO_IN → ITC | +1.00 | events | -0.60% |
| 1 | F_USDINR → ITC | -0.37 | observed | -0.37% |
| 1 | F_RURAL_DEMAND → ITC | -0.25 | events | -0.35% |
| 1 | T_FORMALISATION → ITC | +0.30 | events | +0.24% |
| 1 | F_URBAN_DEMAND → ITC | +0.20 | events | +0.20% |
| 1 | F_EDIBLE_OIL → ITC | +0.19 | observed | -0.06% |
| 1 | F_WHEAT → ITC | -0.13 | observed | +0.05% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → ITC | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → ITC | +0.30 | events | -0.01% |
| 1 | F_BRENT → ITC | +0.00 | observed | -0.00% |
| 3 | F_BRENT → F_CHEM_FEEDSTOCK → F_PACKAGING → ITC | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further cigarette price hikes / pack-size changes after Sept 16 hike | other | 0.50 | +1.8% | +0.88% |
| 2026-12 | Residual block/overhang from large FPI sellers after GQG 8 Oct sale | other | 0.30 | -2.5% | -0.75% |
| 2027-01 | Q3 FY27 results (cigarette volume/margin recovery vs tax pass-through) | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# ITC — what moves the stock

**Business.** ITC earns most of its profit from cigarettes (about three-quarters of segment EBIT, model knowledge, approximate) and uses that cash flow to fund FMCG-others, paperboard and agri-business. It has almost no debt, pays a ~5% yield and is the heaviest consumer-staples stock in the Nifty 50. Quarter ended Sep-2026: sales Rs 20,269 cr, operating margin 28% (34% a year earlier), PAT Rs 4,229 cr (-18.5% y/y) (screener.in, 2026-11-05).

## Ranked drivers
1. **Cigarette tax regime (NEW_TOBACCO_EXCISE), about -5% equity value per +10% tax burden.** The new excise structure from early 2026 raised per-stick taxes; Reuters (2026-11-02) reports Q2 profit down ~20% as higher prices dented demand. ITC hiked prices again on 16 Sep 2026. Gross cigarette revenue rose sharply while net revenue fell, which is the tax pass-through signature.
2. **Consumer demand (rural and urban).** FMCG-others hit a 14-quarter-high growth rate in Q2; the weak 2026 monsoon is the main downside for rural volumes.
3. **Flows.** FIIs fell from 34.8% to 33.2% in two quarters; GQG's Rs 9,395 cr block on 8 Oct knocked ~4% off the stock.
4. **Rate and discount-rate effects.** A 5% yield stock behaves like a bond proxy: higher repo/G-sec yields compress the multiple.
5. **Input costs.** Wheat, edible oils, packaging, fuel; partly offset by ITC's own paperboard and agri arms.

## Worked transmission chains
- **Middle East escalation -> Brent up -> polymer/BOPP and fuel costs up -> FMCG-others margin down -> group EBITDA slightly lower (3rd order).** Brent is already +15% over three months (94.99). 4th order: ITC's paperboard arm gains from higher packaging prices, a partial hedge.
- **Brent up -> INR weaker (94.49 per USD) -> RBI holds rates -> bond yields stay high -> multiples on 5%-yield defensives compress.** The rupee move helps ITC's agri exports (~+1.0% equity per +3% USD/INR) so the second-order effect is mixed.
- **Weak monsoon -> rural income squeeze -> lower beedi-to-cigarette trading-up and slower atta/biscuit volume -> FMCG-others growth slows -> cigarette cash flow must carry more of the group.**
- **Higher tobacco tax -> price hikes -> volume loss to untaxed bidis/illicit sticks -> excise collection disappoints -> government may tighten enforcement (T_FORMALISATION) -> legal volumes recover.** This reflexive loop is the main upside option.

## Current situation
Q1 FY27 profit fell 27% (New Indian Express, 2026-07-31); Q2 fell ~20%. Citi upgraded to Buy on 5 Oct citing ~17% upside; BNP Paribas sees large upside (Business Today, 2026-09-29). The stock is -31.8% over twelve months.

## Upcoming
Q3 results (about Jan 2027), Union Budget (1 Feb 2027) for tobacco tax, further price actions and block-deal overhang. See company_events.

## Bull / bear
**Bull:** tax stability, volume stabilises, FMCG-others margin rises, 5% yield supports valuation. **Bear:** another tax step or illicit growth, continued FPI selling, margin-dilutive input inflation. Information gaps: exact segment EBIT split for FY27 and ITC's volume figures were not retrieved from primary filings; shares are approximate.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.