# BEL — Bharat Electronics Ltd.
*NIFTY_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.8%**, **12 months +10.6%** (rank 13 / 11 of 200 for 3m / 12m); beta 1.24
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.9%): 3 months 67%, 12 months 62%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +7.5% … P90 +16.5%; plausible 12m relative-return range incl. stock-specific noise: -29.5% … +32.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +5.0 pp (model impact +10.0% beta-adjusted vs realised market-adjusted move -8.5%); forward event exposure +11.7% (3m +3.3%; half assumed priced); company-specific events +1.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +5.79 | +5.50 | +0.30 | +0.00 | -0.01 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +5.60 | +2.50 | +2.86 | +0.25 | -0.01 | — |
| Indian defence exports (`T_DEFENCE_EXPORTS`) | +1 | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.44 | +1.50 | +0.00 | -0.03 | -0.03 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.27 | +1.20 | +0.05 | +0.01 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.21 | -0.80 | -0.25 | -0.14 | -0.01 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.19 | +0.00 | -0.26 | -0.49 | -0.44 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.18 | +0.00 | -0.32 | -0.59 | -0.28 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.10 | +0.00 | +0.77 | +0.27 | +0.06 | +1.2% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.03 | +0.00 | -1.02 | -0.05 | +0.05 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.91 | +0.00 | -0.67 | -0.21 | -0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.84 | -0.50 | -0.26 | -0.09 | -0.00 | -1.1% |
| US dollar index (`F_DXY`) | +3% DXY | -0.84 | +0.00 | -0.65 | -0.16 | -0.03 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +7.1% | +6.4% | +6.9 | +0.2 | -0.0 | -0.0 |
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +5.8% | +5.8% | +5.5 | +0.3 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.1% | -4.1% | +0.0 | -1.9 | -1.7 | -0.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.1% | -3.1% | -3.0 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.5% | +1.8% | +3.3 | +0.1 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.3% | +1.3% | +1.5 | -0.1 | -0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.6% | -1.3% | -3.2 | -1.1 | -0.3 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -6.8% | -1.2% | -4.0 | -2.7 | -0.1 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.2 | -0.1 | +0.1 |
| New BrahMos/defence export contracts (Philippines follow-on, Indonesia, Vietnam or others) announced (`EV_DEFENCE_EXPORT_ORDERS`) | anticipated | 0.50 | +2.3% | +1.2% | +2.3 | +0.0 | +0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.1% | -1.1% | -1.0 | -1.1 | -0.9 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.6% | +0.9% | +0.4 | +0.6 | +0.5 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BEL | +5.50% | +4.95% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BEL | +3.00% | +1.50% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BEL | +1.20% | +1.08% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BEL | -3.20% | -0.90% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BEL | -4.00% | -0.72% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → BEL | +1.20% | +0.60% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ P_DEFENCE_PROCUREMENT → BEL | +1.10% | +0.55% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → BEL | +0.90% | +0.40% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BEL | -1.80% | -0.40% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → BEL | -0.96% | -0.34% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → BEL | -1.15% | -0.32% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BEL | -0.80% | -0.32% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BEL | +1.08% | +0.30% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → BEL | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → BEL | -1.15% | -0.29% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_DEFENCE_PROCUREMENT → BEL | +1.00 | events | +5.50% |
| 1 | F_FPI_FLOWS → BEL | -1.60 | events | -1.92% |
| 1 | F_GOVT_CAPEX → BEL | +1.00 | events | +1.50% |
| 1 | F_REPO_IN → BEL | +1.00 | events | -0.80% |
| 2 | P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → BEL | +1.00 | events | +0.24% |
| 1 | F_USDINR → BEL | -0.37 | observed | +0.18% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BEL | -0.30 | events | +0.11% |
| 1 | F_RISK_SENTIMENT → BEL | +0.11 | observed | -0.09% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → BEL | -0.10 | events | +0.05% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → BEL | -0.10 | events | +0.02% |

## Analyst profile (agent research, sourced)
# BEL - Bharat Electronics Ltd. (Defence electronics PSU, Nifty 50)

## Business
BEL designs and builds military electronics: radars, communications, electronic warfare, naval combat systems, missile electronics, electro-optics, air-defence and homeland-security systems, plus a small civil business. MoD and the services are the dominant customers; the company runs a net-cash balance sheet with 28% EBITDA margin but 170 debtor days. Order book of Rs68,717 cr (2026-09-30) is 2.3x TTM sales.

## What moves the stock, ranked
1. **Defence procurement and order inflow** (P_DEFENCE_PROCUREMENT +5.5 per +10%): the DAC cleared Rs2.12 lakh cr on 2026-10-26/27; brokers expect about Rs55,000 cr FY27 order inflow.
2. **Execution and margin**: Q2 PAT +20% beat estimates but margin contracted from 29% to 28%; guidance for FY27 revenue was positively received (Kotak, 2026-11-04).
3. **Geopolitics** (India-Pakistan +2.5; exports +2.0).
4. **Valuation drivers**: FPI flows, VIX and the 5.50% repo (discount-rate -0.8 / -0.8).
5. **Component supply and rupee**: semiconductors -1.5, USD/INR -0.5.

## Transmission examples
- **India-Pakistan escalation -> emergency procurement and air-defence urgency -> BEL radar/EW orders accelerated -> order book up** (2nd-3rd order). 4th order: higher oil and risk-off FPI selling temper the equity move.
- **Chip supply tightening (Taiwan/China) -> component lead times and prices up -> BEL material cost up on fixed-price contracts -> margin squeeze** (3rd order, 3-12 months).
- **Government capex push -> higher defence capital budget (Feb 2027) -> more DAC acceptances of necessity -> RFP and contract timeline -> order inflow in FY28.**
- **RBI hike -> bond yields up -> discount rate up -> 45x P/E compresses; but deposit income rises slightly.**

## Current situation
Q2 FY27 PAT Rs1,541 cr, sales Rs7,328 cr. Recent orders include Rs770 cr radar (2026-10-22), Rs533 cr (2026-10-13) and Rs648 cr (2026-09-17). The stock touched Rs355-ish 52-week low zone on 2026-10-23, then rebounded on DAC news and brokerage upgrades (Motilal, Elara). Empirical sensitivities show aluminium (+3.34, t=3.6) and wheat (+2.10, t=2.5) as strongest co-movers, but these have no clear fundamental channel and are treated as sector/PSU-cycle proxies, not edges.

## Upcoming
Q3 results late Jan 2027; large orders; Union Budget (Feb 2027); FY27 inflow vs target.

## Bull and bear
Bull: structural indigenisation tailwind, Rs68,717 cr order book, strong cash returns, guidance upgrades. Bear: 45x P/E, working capital stretch, margin pressure, order timing slippage and FII selling.

Uncertainties: export share, import content and customer concentration figures are model knowledge.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.