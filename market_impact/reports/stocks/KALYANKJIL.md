# KALYANKJIL — Kalyan Jewellers India Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.0%**, **12 months +1.1%** (rank 63 / 81 of 200 for 3m / 12m); beta 1.38
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +47.8%): 3 months 52%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.2% … P90 +3.6%; plausible 12m relative-return range incl. stock-specific noise: -67.0% … +46.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +1.8% beta-adjusted vs realised market-adjusted move +54.0%); forward event exposure +3.2% (3m +2.2%; half assumed priced); company-specific events +1.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian jewellery/gold demand volume (`F_GOLD_DEMAND_IN`) | +10% | +6.97 | +7.00 | +0.00 | -0.03 | +0.00 | — |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +4.04 | +4.00 | +0.00 | +0.04 | +0.00 | — |
| Gold import duty (`P_GOLD_IMPORT_DUTY`) | +5 pp | -3.32 | -2.00 | -1.33 | +0.00 | +0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.26 | +0.00 | -2.00 | -0.95 | -0.31 | -1.1% |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.70 | +1.50 | +1.12 | +0.13 | -0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.31 | -1.00 | -0.33 | -0.48 | -0.49 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.11 | +1.50 | +0.56 | +0.08 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.77 | +1.50 | +0.06 | +0.13 | +0.08 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.74 | +0.00 | +0.66 | +0.70 | +0.39 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.71 | +0.00 | -0.60 | -1.20 | +0.09 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.55 | +0.00 | +0.84 | +0.78 | -0.07 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.51 | -1.50 | +0.00 | +0.00 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.40 | +0.00 | -0.52 | -0.70 | -0.18 | +3.5% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.31 | +0.00 | +0.34 | +0.66 | +0.31 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.0% | -8.0% | -1.5 | +0.2 | -4.0 | -2.8 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.0% | -4.0% | -3.3 | -0.1 | -0.4 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.1% | +2.4% | +1.0 | +0.4 | +1.8 | +0.9 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.5% | -2.3% | -1.2 | -0.7 | -3.0 | -1.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -0.8 | -1.6 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.6% | +2.3% | +3.8 | +0.1 | +0.5 | +0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -2.1 | +0.0 | -0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -6.2% | -1.7% | +0.0 | -3.5 | -2.0 | -0.7 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -0.4 | -0.8 | -0.4 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -6.7% | -1.5% | -3.8 | -2.1 | -0.9 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -7.9% | -1.4% | +0.0 | -4.4 | -2.2 | -1.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.4% | -1.4% | -0.5 | -0.3 | -0.3 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → KALYANKJIL | +3.75% | +1.88% |
| 2 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → T_FORMALISATION → KALYANKJIL | +0.96% | +0.77% |
| 2 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → F_GOLD_DEMAND_IN → KALYANKJIL | +2.13% | +0.64% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ F_GOLD_DEMAND_IN → KALYANKJIL | -2.10% | -0.63% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → KALYANKJIL | -2.24% | -0.63% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → KALYANKJIL | -1.20% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → KALYANKJIL | +1.00% | +0.58% |
| 2 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → F_GOLD_DEMAND_IN → KALYANKJIL | -1.12% | -0.50% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → KALYANKJIL | -2.80% | -0.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → KALYANKJIL | -2.25% | -0.49% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → KALYANKJIL | -0.75% | -0.45% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → KALYANKJIL | -1.20% | -0.43% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → KALYANKJIL | -1.44% | -0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → KALYANKJIL | -1.44% | -0.36% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → KALYANKJIL | -0.36% | -0.34% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → KALYANKJIL | +1.70 | events | -2.55% |
| 1 | F_FPI_FLOWS → KALYANKJIL | -1.60 | events | -2.40% |
| 1 | C_MIDEAST_CONFLICT → KALYANKJIL | +1.50 | events | -1.50% |
| 1 | T_FORMALISATION → KALYANKJIL | +0.30 | events | +1.20% |
| 2 | F_GOLD → F_GOLD_DEMAND_IN → KALYANKJIL | -1.05 | observed | +1.17% |
| 1 | F_GOLD → KALYANKJIL | -1.05 | observed | -0.52% |
| 2 | F_USDINR → F_GOLD_DEMAND_IN → KALYANKJIL | -0.37 | observed | +0.41% |
| 1 | F_RURAL_DEMAND → KALYANKJIL | -0.25 | events | -0.38% |
| 1 | F_URBAN_DEMAND → KALYANKJIL | +0.20 | events | +0.30% |
| 2 | F_RURAL_DEMAND → F_GOLD_DEMAND_IN → KALYANKJIL | -0.25 | events | -0.28% |
| 1 | F_ALUMINIUM → KALYANKJIL | -1.96 | observed | +0.20% |
| 3 | F_USDINR → P_GOLD_IMPORT_DUTY → F_GOLD_DEMAND_IN → KALYANKJIL | -0.37 | observed | +0.18% |

## Analyst profile (agent research, sourced)
# KALYANKJIL - Kalyan Jewellers India Ltd. (midcap, jewellery retail)

## Business
Jewellery retailer with ~89% India (South-heavy, many franchise-owned showrooms) and ~11% Middle East, plus the Candere studded/online brand. TTM revenue ~Rs39,063cr and EBITDA ~6.7%. Gold is ~90% of costs and is largely hedged through metal loans, so the equity trades on volume, same-store growth, share gains and working-capital financing rather than on the gold price level. P/E 39x; promoter 62.9%.

## What moves the stock (ranked)
1. **Gold-jewellery demand (+7.0 per +10%)**: operating leverage is high at a 6-7% margin.
2. **Formalisation / organised share gain (+4.0)**: the main bull thesis (Jefferies).
3. **Import duty (-2.0 per +5pp), G-sec/funding (-1.5), FPI flows (+1.5), rural (+1.5), urban (+1.5).**
4. **Gulf and conflict**: GCC (+1.0), remittances (+1.2), Middle East escalation (-1.0).
5. **Gold price (+0.5, ambiguous).**

## Transmission examples
- **Middle East escalation -> Brent up (1st) -> INR weaker (2nd), gold up as haven -> domestic gold higher (3rd) -> wedding-season volumes dip and customers trade down in weight while South India's Gulf-remittance households cut purchases (4th); Gulf stores also see lower traffic.**
- **Monsoon good -> rural incomes up -> tier-3/4 wedding jewellery demand (F_RURAL_DEMAND) -> Kalyan's rural-heavy store base gains more than metro-focused Tanishq.**
- **Budget raises gold import duty -> domestic price up ~5% -> volumes down, franchise inventory gains, smuggling up -> organised players recover share over 2-3 quarters (policy-effect lag).**
- **Gold price crash -> franchise inventory valued lower and customers wait for further falls (pause) -> near-term SSSG weakens before volume rebounds.**
- **RBI cuts/holds and G-sec yields fall -> lower gold-loan and working-capital cost; discount-rate relief on a 39x P/E.**

## Current situation
Q2 FY27 business update (7 Oct): revenue +26%, India +27% with SSSG ~20% (28% in Q1), international +18%, Candere +64%. Last reported financials (Q1 FY27): revenue Rs10,589cr, OPM 6%, PAT Rs349cr. Price Rs552: 6m +34%, 3m -7.8% from a peak near Rs649, 12m +5.5%. Pack empirical betas (aluminium -3.12, gas -1.36, coal +3.91) have no business link and are ignored.

## Upcoming
Q2 FY27 results (by 14 Nov), festive quarter, Q3 update (Jan), Budget (Feb 2027).

## Bull / bear
Bull: continued organised share gains, store roll-out, Candere, stable gold. Bear: SSSG fading toward the low teens, duty/tax changes, gold price shocks, working-capital strain.

Uncertainties: Q2 results unseen; revenue split by region approximate; stock return figures are from the pack.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.