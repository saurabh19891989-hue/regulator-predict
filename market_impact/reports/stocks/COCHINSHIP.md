# COCHINSHIP — Cochin Shipyard Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.7%**, **12 months +7.7%** (rank 25 / 23 of 200 for 3m / 12m); beta 1.67
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.9%): 3 months 60%, 12 months 62%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.0% … P90 +25.1%; plausible 12m relative-return range incl. stock-specific noise: -32.2% … +33.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.3 pp (model impact +8.7% beta-adjusted vs realised market-adjusted move -21.0%); forward event exposure +7.9% (3m +3.6%; half assumed priced); company-specific events +1.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Shipbuilding & maritime policy support (`NEW_SHIPBUILDING_POLICY`) | +1 = stronger support (financial assistance, ISRF, yard infrastructure funding) | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +3.11 | +0.00 | +1.14 | +2.14 | -0.18 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +3.05 | +0.00 | +3.12 | -0.03 | -0.04 | — |
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +2.99 | +3.00 | +0.00 | -0.01 | -0.01 | — |
| Red Sea / Suez shipping disruption (`C_RED_SEA`) | +1 = disruption | +2.75 | +0.80 | +1.95 | +0.00 | +0.00 | — |
| Global container / freight rates (`F_SHIPPING_RATES`) | +25% | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.51 | -1.50 | +0.00 | -0.01 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.43 | -1.50 | +0.06 | +0.01 | -0.01 | +3.5% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.16 | +0.00 | -1.00 | -0.13 | -0.04 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -0.92 | -1.00 | +0.07 | +0.02 | -0.01 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -0.85 | +0.00 | -0.88 | -0.06 | +0.09 | — |
| US growth (`F_US_GDP`) | +1 pp | +0.79 | +0.00 | +0.48 | +0.45 | -0.14 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.75 | +0.00 | -0.61 | -0.17 | +0.03 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | -0.75 | +0.00 | -0.74 | +0.00 | -0.01 | +20.6% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +5.8% | +5.8% | +3.3 | +3.0 | -0.3 | -0.1 |
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +3.0% | +3.0% | +3.0 | +0.0 | -0.0 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.6% | +2.4% | +3.0 | -0.2 | -0.1 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -2.9% | -1.7% | +0.0 | -1.3 | -1.6 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -5.8% | -1.6% | -6.0 | +0.2 | +0.1 | -0.2 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -7.2% | -1.3% | -7.5 | +0.3 | +0.2 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +3.0% | +1.1% | -0.5 | +1.7 | +1.9 | -0.1 |
| Red Sea shipping closed again (Houthi campaign broadens; Bab el-Mandeb largely avoided) (`EV_RED_SEA_CLOSURE`) | risk_scenario | 0.25 | +4.2% | +1.1% | +4.2 | +0.0 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.0% | +1.0% | +0.0 | +0.5 | +0.5 | -0.1 |
| Container lines broadly return to Suez/Red Sea routing; freight rates fall (`EV_RED_SEA_SUEZ_NORMALISATION`) | anticipated | 0.45 | -2.2% | -1.0% | -2.2 | +0.0 | +0.0 | +0.0 |
| Red Sea: Houthi attacks on shipping and Saudi targets resume (Jul-Oct 2026) while carriers partially return to Suez (`EV_RED_SEA_HOUTHI_ESCALATION_Q3`) | occurred | 1.00 | +1.0% | +1.0% | +1.0 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → COCHINSHIP | +3.00% | +2.70% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → COCHINSHIP | -6.00% | -1.68% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → COCHINSHIP | -7.50% | -1.35% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → C_RED_SEA → F_SHIPPING_RATES → COCHINSHIP | -1.75% | -1.02% |
| 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → C_RED_SEA → F_SHIPPING_RATES → COCHINSHIP | +2.10% | +0.75% |
| 1 | EV_RED_SEA_CLOSURE ⇒ F_SHIPPING_RATES → COCHINSHIP | +3.00% | +0.75% |
| 1 | EV_RED_SEA_SUEZ_NORMALISATION ⇒ F_SHIPPING_RATES → COCHINSHIP | -1.60% | -0.72% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → COCHINSHIP | +1.00% | +0.65% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → COCHINSHIP | -1.80% | -0.64% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → COCHINSHIP | -2.16% | -0.54% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → COCHINSHIP | +1.25% | +0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → COCHINSHIP | -0.75% | -0.44% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → COCHINSHIP | +0.75% | +0.44% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → COCHINSHIP | -2.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → COCHINSHIP | +0.60% | +0.37% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_DEFENCE_PROCUREMENT → COCHINSHIP | +1.00 | events | +3.00% |
| 1 | F_STEEL_INDIA → COCHINSHIP | +1.65 | events | -2.47% |
| 1 | C_RED_SEA → COCHINSHIP | +1.50 | events | +1.20% |
| 1 | F_REPO_IN → COCHINSHIP | +1.00 | events | -0.70% |
| 1 | P_US_TARIFF_INDIA → COCHINSHIP | -0.60 | events | +0.60% |
| 1 | F_SHIPPING_RATES → COCHINSHIP | +0.30 | events | +0.60% |
| 1 | F_USDINR → COCHINSHIP | -0.37 | observed | -0.37% |
| 1 | F_RISK_SENTIMENT → COCHINSHIP | +0.11 | observed | -0.17% |
| 1 | F_BRENT → COCHINSHIP | +0.00 | observed | +0.00% |

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