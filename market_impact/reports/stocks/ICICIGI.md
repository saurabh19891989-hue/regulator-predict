# ICICIGI — ICICI Lombard General Insurance Company Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.1%**, **12 months -3.7%** (rank 159 / 157 of 200 for 3m / 12m); beta 0.80
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.0%): 3 months 43%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -8.9% … P90 -0.9%; plausible 12m relative-return range incl. stock-specific noise: -4.6% … +20.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -1.5% beta-adjusted vs realised market-adjusted move -10.9%); forward event exposure -4.1% (3m -1.6%; half assumed priced); company-specific events -1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -4.12 | -4.00 | -0.12 | +0.00 | +0.00 | — |
| Natural catastrophe insured losses (India floods/cyclones) (`NEW_NAT_CAT_LOSSES`) | +1 = major cat year adding ~2pp to industry combined ratio | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.47 | +0.00 | -0.48 | -1.43 | -0.56 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.14 | -1.50 | -0.37 | -0.23 | -0.04 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.12 | -1.50 | -0.22 | -0.22 | -0.18 | -1.1% |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +1.99 | +2.00 | +0.00 | +0.00 | -0.01 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.95 | +2.00 | +0.13 | -0.16 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.94 | +0.80 | +0.63 | +0.36 | +0.14 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.88 | -1.00 | -0.33 | -0.52 | -0.03 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.80 | +0.00 | -0.60 | -0.77 | -0.43 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.79 | +0.00 | +1.20 | +0.49 | +0.10 | +1.2% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.73 | +1.50 | +0.20 | -0.00 | +0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.66 | +0.00 | -0.59 | -0.49 | -0.58 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.62 | +0.00 | -1.06 | -0.29 | -0.27 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.8% | -3.8% | -3.3 | -0.4 | +0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.0% | +2.5% | +4.3 | +0.5 | -0.0 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | -1.1 | -0.4 | -0.7 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -2.1 | +0.0 | -0.1 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -0.7 | -0.8 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.1% | +1.7% | +0.6 | +1.5 | +0.5 | +0.5 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.6% | -1.7% | -3.8 | -2.4 | -0.7 | +0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.0 | -0.4 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -5.9% | -1.5% | -1.5 | -2.7 | -0.9 | -0.8 |
| IRDAI resets insurance commission/expense rules; post-GST-exemption demand (`EV_IRDAI_COMMISSION_RESET`) | anticipated | 0.50 | -2.9% | -1.4% | -2.8 | -0.1 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -5.0% | -1.2% | +0.0 | -5.2 | +0.5 | -0.3 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.2% | +1.2% | +0.0 | +0.6 | +0.4 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ICICIGI | +3.75% | +1.88% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → ICICIGI | -2.80% | -1.40% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ICICIGI | -3.75% | -0.94% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ICICIGI | -1.20% | -0.60% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ICICIGI | -3.75% | -0.56% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → ICICIGI | -2.16% | -0.54% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → ICICIGI | +0.58% | +0.52% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → ICICIGI | -0.75% | -0.45% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ICICIGI | -2.25% | -0.40% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → ICICIGI | -1.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → ICICIGI | +0.60% | +0.37% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → ICICIGI | +0.53% | +0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ICICIGI | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ICICIGI | -1.44% | -0.36% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → ICICIGI | -3.00% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ICICIGI | -1.60 | events | -2.40% |
| 1 | F_GSEC_10Y_IN → ICICIGI | +1.55 | director_override | -2.33% |
| 1 | F_CPI_IN → ICICIGI | +1.15 | events | -1.15% |
| 1 | F_GDP_IN → ICICIGI | +0.50 | events | +1.00% |
| 1 | F_USDINR → ICICIGI | -0.37 | observed | +0.55% |
| 1 | F_RISK_SENTIMENT → ICICIGI | +0.11 | observed | -0.17% |
| 1 | F_AUTO_DEMAND_IN → ICICIGI | -0.10 | events | -0.12% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → ICICIGI | +0.30 | events | +0.10% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Ex-dividend for Rs7 interim dividend (record date late Oct/Nov) | corporate_action | 0.95 | -0.4% | -0.38% |
| 2026-12 | IRDAI final commission/expense framework | regulatory | 0.55 | -1.5% | -0.83% |
| 2027-01-14 | Q3 FY27 results (estimated from Q2 on 2026-10-14): combined ratio, cat losses | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# ICICIGI - ICICI Lombard General Insurance Company Ltd. (as of 2026-11-05)

## Business
ICICI Lombard is the largest private non-life insurer in India. Motor (own damage plus third party) is roughly 38% of premiums, health and personal accident about 27%, and fire/marine/engineering/commercial lines the rest (model estimate; the pack's fundamentals table was blank and these shares need verification). ICICI Bank owns 51.3% and is a key distributor. Profit depends on the combined ratio (claims plus expenses over earned premium) and on investment income on a ~Rs32k cr float (model estimate). Q2 FY27: PAT Rs946cr (+15.5%) per BusinessLine/Financial Express vs Rs1,031cr (+27.5%) per Moneycontrol - an unresolved difference; all sources agree the combined ratio stayed elevated and investment income carried earnings.

## What moves the stock (ranked)
1. **IRDAI regulation (-4.0)**: the 2026-09-23 commission-cap/dark-pattern proposal, plus motor third-party tariff decisions.
2. **GDP and financialisation (+2.0, +2.0)**: penetration and premium growth.
3. **INR and imported-parts inflation (-1.5)**: weaker rupee raises motor repair and reinsurance costs; empirical -2.11 per SSU (t=-1.6) agrees.
4. **Rates (G-sec -1.5)** and **catastrophe losses (-3.0 in a bad cat year)**.
5. **Auto demand (+1.2)**, **CPI/medical inflation (-1.0)**, **flows and risk (+1.5, -1.5)**.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker -> imported auto parts and reinsurance dearer**: Brent +10% -> USD/INR +3% -> motor claims +0.5% (spares ~40% of own-damage claims) -> combined ratio +0.5pp -> PAT -3%; 3rd: RBI hike (already begun) lowers car sales growth -> GWP -1pp; 4th: tariff-regulated TP pricing fixed so insurer cannot reprice.
- **IRDAI commission cap -> distributors shift focus -> premium growth down but expense ratio down**: first-order GWP -2%; second-order expense ratio -1pp; third-order broker renegotiation; fourth-order market consolidation to bancassurance-led insurers like ICICI Lombard (a possible advantage).
- **Monsoon floods -> cat claims in Q2/Q3** -> combined ratio +1-2pp -> reinsurance cost up next year.
- **Higher G-sec yields** -> MTM on trading portfolio (-0.5) but better reinvestment (+0.3) -> investment income supports margins in 2027.

## Current situation
Stock -2% in 3m, -12% in 6m, -20.5% in 12m. FIIs sold from 22.3% to 18.3% while DIIs bought (23.8%). Brokers remain positive (targets Rs1,985-2,000, ~16-23% upside). The market debate: whether the combined ratio can fall below ~102% and whether IRDAI's distribution rules hurt volume.

## Upcoming
Q3 FY27 results ~mid-Jan 2027; IRDAI final framework; Union Budget Feb 2027; cat season; ex-dividend of Rs7.

## Bull case
Combined ratio improves to ~101-102%, IRDAI softens, investment income grows: EPS +15-18%, re-rating to 35x earnings (+15-20%).
## Bear case
Health/motor claims inflation, bad cat year, weaker INR and distribution caps: EPS growth <8% and de-rating (-15%).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.