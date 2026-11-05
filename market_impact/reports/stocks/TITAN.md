# TITAN — Titan Company Ltd.
*NIFTY_50 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months +0.1%** (rank 82 / 93 of 200 for 3m / 12m); beta 1.02
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.1%): 3 months 52%, 12 months 20%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.6% … P90 +0.5%; plausible 12m relative-return range incl. stock-specific noise: -28.4% … +12.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +0.5% beta-adjusted vs realised market-adjusted move +15.5%); forward event exposure +1.4% (3m +1.3%; half assumed priced); company-specific events +0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian jewellery/gold demand volume (`F_GOLD_DEMAND_IN`) | +10% | +4.99 | +5.00 | +0.01 | -0.02 | +0.00 | — |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +3.05 | +3.00 | +0.00 | +0.04 | +0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.88 | +2.50 | +0.40 | +0.04 | -0.05 | — |
| Gold import duty (`P_GOLD_IMPORT_DUTY`) | +5 pp | -2.45 | -1.50 | -0.95 | +0.00 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.13 | +2.00 | +0.10 | +0.03 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.71 | +0.00 | +1.60 | +0.13 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.68 | +0.00 | +0.84 | +0.54 | +0.29 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.60 | -0.80 | -0.14 | -0.24 | -0.42 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.32 | +0.00 | -0.29 | -0.47 | -0.56 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.31 | -0.50 | -0.31 | -0.50 | -0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.21 | -1.20 | +0.00 | +0.00 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.18 | +1.00 | +0.02 | +0.10 | +0.06 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.13 | +0.00 | +0.72 | +0.51 | -0.10 | — |
| Labour code implementation cost (`P_LABOUR_CODES`) | +1 = implementation | +0.99 | +0.00 | +0.72 | +0.15 | +0.12 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.6% | -2.6% | -2.2 | -0.0 | -0.2 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | -0.6 | -0.4 | -0.7 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.1% | +1.5% | +2.5 | +0.0 | +0.4 | +0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.8% | +1.5% | +0.8 | +0.2 | +1.2 | +0.6 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.3% | -1.3% | -0.8 | -0.1 | -0.3 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.4% | -1.1% | -1.0 | -0.3 | -2.0 | -1.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | +0.0 | -0.6 | -0.3 |
| 57th GST Council (8 Oct 2026): no rate change; process reforms (refund automation, decriminalisation) (`EV_GST_57TH_COUNCIL_OCT26`) | occurred | 1.00 | +0.9% | +0.9% | +0.9 | +0.0 | +0.0 | +0.0 |
| Labour codes: states finalise rules (deadline 31 Oct 2026), wider operational rollout (`EV_LABOUR_CODES_RULES`) | anticipated | 0.80 | +1.1% | +0.9% | +0.0 | +0.9 | +0.2 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.7% | -0.7% | +0.0 | -1.7 | -0.8 | -0.3 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -3.8% | -0.7% | -2.3 | -1.0 | -0.5 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TITAN | +2.50% | +1.25% |
| 2 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → T_FORMALISATION → TITAN | +0.72% | +0.58% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TITAN | -0.96% | -0.48% |
| 2 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → F_GOLD_DEMAND_IN → TITAN | +1.52% | +0.46% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ F_GOLD_DEMAND_IN → TITAN | -1.50% | -0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → TITAN | +0.80% | +0.44% |
| 2 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → F_GOLD_DEMAND_IN → TITAN | -0.80% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → TITAN | -0.60% | -0.36% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → TITAN | -1.14% | -0.34% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GOLD_DEMAND_IN → TITAN | +0.48% | +0.34% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → TITAN | -0.29% | -0.27% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TITAN | -1.50% | -0.27% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → TITAN | +0.60% | +0.27% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_GOLD_DEMAND_IN → TITAN | +0.48% | +0.26% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TITAN | -0.96% | -0.24% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → TITAN | +1.55 | director_override | -1.86% |
| 1 | F_FPI_FLOWS → TITAN | -1.60 | events | -1.60% |
| 1 | T_FORMALISATION → TITAN | +0.30 | events | +0.90% |
| 2 | F_GOLD → F_GOLD_DEMAND_IN → TITAN | -1.05 | observed | +0.84% |
| 1 | C_MIDEAST_CONFLICT → TITAN | +1.00 | events | -0.80% |
| 1 | F_GOLD → TITAN | -1.05 | observed | -0.63% |
| 1 | F_CPI_IN → TITAN | +1.15 | events | -0.57% |
| 1 | F_URBAN_DEMAND → TITAN | +0.20 | events | +0.50% |
| 2 | F_RURAL_DEMAND → F_GOLD_DEMAND_IN → TITAN | -0.25 | events | -0.40% |
| 2 | F_USDINR → F_GOLD_DEMAND_IN → TITAN | -0.37 | observed | +0.15% |
| 1 | F_USDINR → TITAN | -0.37 | observed | -0.11% |
| 2 | F_URBAN_DEMAND → F_GOLD_DEMAND_IN → TITAN | +0.20 | events | +0.08% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Diwali/Dhanteras and wedding-season sell-through: some festive demand moved from Q2 into Q3 FY27 | other | 0.85 | +1.0% | +0.85% |
| 2026-11-05 | Q2 FY27 results (board meeting reported for 5 Nov; unconfirmed). Previews: profit up ~26-27% YoY on jewellery +21%; watch jewellery EBIT margin vs ~14% Q1 and studded mix | results | 0.90 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 business update (early Jan) and results (late Jan/early Feb): gold-price path and festive quarter | guidance | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# TITAN - Titan Company Ltd. (Nifty 50, jewellery and lifestyle)

## Business
Jewellery is ~85% of revenue (Tanishq, Mia, Zoya, CaratLane), then watches, eyecare, fragrances and Taneira, plus Damas in the Gulf (consolidated since Jan 2026). 3,758 stores after 78 net adds in Q2 FY27. TTM revenue Rs92,417cr, EBITDA ~10%, P/E 73x. Gold is financed through gold-metal loans/lease and hedged, so per-gram margin is stable while volumes, ticket size, working capital and interest cost move with the gold price.

## What moves the stock (ranked)
1. **Gold-jewellery demand and wedding/festive volumes (+5.0 per +10%)**: Q2 jewellery +21% against 19.3% consensus (CLSA) but below JPMorgan's 25%, enough for a -4% to -5% reaction.
2. **Formalisation (+3.0), urban demand (+2.5), premiumisation/studded mix (+2.0).**
3. **Discount rate (-1.2 per +25bp) and FPI flows (+1.0)** for a 73x P/E large cap.
4. **Gold price (+0.6, ambiguous)** and **gold import duty (-1.5 per +5pp).**
5. GCC/Damas (+0.6), Middle East conflict (-0.8), CPI (-0.5), USD/INR (+0.3).

## Transmission examples
- **Middle East escalation -> gold up as haven (1st) and Brent up (1st) -> INR weaker, domestic gold higher still (2nd) -> jewellery volumes down 3-5% and customers trade to lighter/studded pieces (3rd) -> Titan's revenue per customer up but footfalls soft; Damas Gulf stores also see disruption (4th).**
- **Gold falls (-8.4% since June) -> lower ticket prices revive volume demand (+) while hedging keeps EBITDA margin near 10%; net mildly positive on volume, mixed on inventory-gain optics.**
- **Government raises gold import duty (Budget) -> domestic gold +5% -> demand dips and grey market grows -> organised players with hedges recover share in 2-3 quarters (4th).**
- **Brent up -> INR down -> RBI holds -> G-sec yield up -> discount-rate hit on a 73x P/E; FPI outflows compound it.**

## Current situation
Q1 FY27: revenue Rs21,356cr (+29%), OPM 14%, PAT Rs1,777cr. Q2 FY27 update: jewellery ~+21% (studded low-30%, plain ~20%), watches ~+30%, eyecare ~+28%, consumer businesses +25%; some festive demand shifted to Q3. Stock Rs4,837, 12m +26.8%. Results were reported as scheduled for 5 Nov (single source; previews saw profit +26-27%).

## Upcoming
Q2 results and call (5 Nov), Q3 update (early Jan), Budget (Feb 2027), gold-price path.

## Bull / bear
Bull: stable gold, strong weddings, studded mix, organised share gains, Damas ramp. Bear: gold spike/duty, jewellery growth in the high teens, margin normalisation from 14%, and de-rating.

Uncertainties: financials in the pack end at Jun 2026; Q2 results not read; revenue split and import-duty level are approximate.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.