# COCHINSHIP — Cochin Shipyard Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months +0.6%** (rank 123 / 60 of 200 for 3m / 12m); beta 1.67
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.9%): 3 months 50%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.8% … P90 +9.2%; plausible 12m relative-return range incl. stock-specific noise: -37.7% … +42.2%
- Decomposition (12m): 0.5 × forward event exposure +1.3% (3m +0.0%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +6.9% (beta-adjusted) vs a realised market-adjusted move of -21.0% — gap +27.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Shipbuilding & maritime policy support (`NEW_SHIPBUILDING_POLICY`) | +1 = stronger support (financial assistance, ISRF, yard infrastructure funding) | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +3.11 | +0.00 | +3.12 | +0.00 | -0.01 | — |
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +2.99 | +3.00 | +0.00 | -0.01 | +0.00 | — |
| Red Sea / Suez shipping disruption (`C_RED_SEA`) | +1 = disruption | +2.75 | +0.80 | +1.95 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +2.11 | +0.00 | +1.14 | +1.01 | -0.04 | — |
| Global container / freight rates (`F_SHIPPING_RATES`) | +25% | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.43 | -1.50 | +0.06 | +0.01 | +0.00 | +3.5% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.15 | +0.00 | -1.00 | -0.18 | +0.02 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -0.93 | -1.00 | +0.07 | +0.00 | -0.01 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -0.74 | +0.00 | -0.74 | +0.00 | +0.00 | +20.6% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.73 | -0.70 | -0.04 | +0.01 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +0.72 | +1.00 | -0.24 | -0.04 | +0.00 | -1.1% |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -0.69 | +0.00 | -0.74 | +0.02 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +3.0% | +3.0% | +3.0 | +0.0 | -0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.6% | +1.6% | +0.4 | +1.1 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -2.0% | -1.1% | -0.0 | -1.2 | -0.8 | +0.0 |
| Red Sea shipping closed again (Houthi campaign broadens; Bab el-Mandeb largely avoided) (`EV_RED_SEA_CLOSURE`) | risk_scenario | 0.25 | +4.2% | +1.1% | +4.2 | +0.0 | +0.0 | +0.0 |
| Container lines broadly return to Suez/Red Sea routing; freight rates fall (`EV_RED_SEA_SUEZ_NORMALISATION`) | anticipated | 0.45 | -2.2% | -1.0% | -2.2 | +0.0 | +0.0 | +0.0 |
| Red Sea: Houthi attacks on shipping and Saudi targets resume (Jul-Oct 2026) while carriers partially return to Suez (`EV_RED_SEA_HOUTHI_ESCALATION_Q3`) | occurred | 1.00 | +1.0% | +1.0% | +1.0 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.6% | -0.9% | -3.8 | +0.1 | +0.1 | -0.1 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +0.8% | +0.8% | +0.9 | -0.0 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | -0.0 | +0.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +0.6% | +0.6% | +0.0 | +0.5 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → COCHINSHIP | -3.75% | -0.94% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → COCHINSHIP | +0.90% | +0.81% |
| 1 | EV_RED_SEA_CLOSURE ⇒ F_SHIPPING_RATES → COCHINSHIP | +3.00% | +0.75% |
| 1 | EV_RED_SEA_SUEZ_NORMALISATION ⇒ F_SHIPPING_RATES → COCHINSHIP | -1.60% | -0.72% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → COCHINSHIP | -3.75% | -0.56% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → C_RED_SEA → F_SHIPPING_RATES → COCHINSHIP | -0.88% | -0.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → COCHINSHIP | -1.50% | -0.38% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → COCHINSHIP | -2.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → COCHINSHIP | +0.60% | +0.37% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → COCHINSHIP | -0.65% | -0.36% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_SHIPPING_RATES → COCHINSHIP | -0.64% | -0.35% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → COCHINSHIP | +0.60% | +0.33% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → COCHINSHIP | -0.60% | -0.33% |
| 1 | EV_RED_SEA_CLOSURE ⇒ C_RED_SEA → COCHINSHIP | +1.20% | +0.30% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ P_DEFENCE_PROCUREMENT → COCHINSHIP | +0.60% | +0.30% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → COCHINSHIP | +1.35 | events | -2.03% |
| 1 | P_DEFENCE_PROCUREMENT → COCHINSHIP | +0.50 | director_override | +1.50% |
| 1 | C_RED_SEA → COCHINSHIP | +1.00 | events | +0.80% |
| 1 | F_REPO_IN → COCHINSHIP | +1.00 | events | -0.70% |
| 1 | P_US_TARIFF_INDIA → COCHINSHIP | -0.60 | events | +0.60% |
| 1 | F_SHIPPING_RATES → COCHINSHIP | +0.30 | events | +0.60% |
| 1 | F_USDINR → COCHINSHIP | -0.37 | observed | -0.37% |
| 1 | F_RISK_SENTIMENT → COCHINSHIP | +0.11 | observed | -0.17% |
| 1 | F_BRENT → COCHINSHIP | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-10 | Q2 FY27 results (screener upcoming-date field) | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | EGM / shareholder approval for Rs1,800 cr ISRF transfer and related capex | corporate_action | 0.85 | +0.5% | +0.42% |
| 2027-02 | Q3 FY27 results; test of FY27 14% EBITDA margin guidance | results | 0.90 | -0.5% | -0.45% |
| 2027-03 | Binding contracts converting from the 40-ship order announcement (2026-10-09) and further defence awards *(review: [RT_TOP_B] announcement priced 9 Oct (+5%))* | other | 0.50 | +1.0% | +0.50% |

## Analyst profile (agent research, sourced)
# COCHINSHIP - Cochin Shipyard Ltd. (Shipbuilding PSU)

## Business
Cochin Shipyard is India's biggest shipyard and the builder of INS Vikrant. Revenue comes from shipbuilding (defence and commercial exports) and ship repair. Order book is about Rs21,900 cr, roughly four times TTM sales of Rs5,047 cr, so earnings follow delivery milestones. The company also earns Rs423 cr of treasury income and is expanding capacity (Rs6,000 cr projects at Vallarpadam and Thoothukudi), funded partly by borrowings that rose to Rs1,672 cr.

## What moves the stock, ranked
1. **Order wins and margin guidance**: FY27 EBITDA margin guided at ~14% (down from 15%), which triggered a 9-12% drop on 2026-09-11. The Oct 9 headline of 40 ships from US and other countries lifted the stock 5%.
2. **Shipbuilding and defence policy** (NEW_SHIPBUILDING_POLICY +4.0, P_DEFENCE_PROCUREMENT +3.0 per SSU).
3. **Shipping cycle** (F_SHIPPING_RATES +2.0 per +25%).
4. **Risk appetite**: beta ~2 makes market direction the largest short-run factor (VIX -1.5 per +5). FII share is only 3%.
5. **Steel cost and rupee** (steel -1.5 per +7%, USD/INR +1.0).

## Transmission examples
- **Red Sea disruption -> longer voyages, tighter shipping capacity -> freight rates up -> owners order newbuilds -> Cochin commercial order intake**: 1st-3rd order. Parallel: war-risk insurance and Gulf delays slow deliveries (offset).
- **Govt shipbuilding financial assistance expanded -> ISRF funding -> capacity expansion -> higher order-book ceiling in FY28-FY30** (3rd-4th order).
- **Global steel rally (HRC +20.6% since June) -> plate cost up -> fixed-price contract margin erodes; escalation clauses recover about half**.
- **RBI hike -> discount-rate up -> P/E 48x compresses**, plus slightly higher borrowing cost for capex.

## Current situation
After the Sep 2026 margin-guidance shock (and a government stake reduction from 67.91% to 63.33% in the Sep quarter, cause not verified), the stock sits near its low. Positive news arrived in October: a 40-ship order, a cruise-vessel order via a subsidiary, a plan for new yards. Q2 results are due on 2026-11-10 and are the next hard test of delivery pace.

## Upcoming
Q2 results (2026-11-10); EGM for ISRF transfer; contract conversion; Q3 in Feb.

## Bull and bear
Bull: record order pipeline, export-led growth, policy tailwinds, correction from Rs1,844. Bear: lumpy results, lower margin guide, stake sale overhang, high capex, 48x P/E.

Uncertainties: confidence low overall; revenue split, export share and policy details are model knowledge; 40-ship order terms and firmness are not verified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.