# BEL — Bharat Electronics Ltd.
*NIFTY_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +1.7%** (rank 41 / 25 of 200 for 3m / 12m); beta 1.24
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.9%): 3 months 52%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.0% … P90 +5.3%; plausible 12m relative-return range incl. stock-specific noise: -24.4% … +31.6%
- Decomposition (12m): 0.5 × forward event exposure +3.1% (3m +0.5%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +5.7% (beta-adjusted) vs a realised market-adjusted move of -8.5% — gap +14.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +5.80 | +5.50 | +0.30 | +0.00 | +0.00 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +5.61 | +2.50 | +2.86 | +0.25 | +0.00 | — |
| Indian defence exports (`T_DEFENCE_EXPORTS`) | +1 | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.52 | +1.50 | +0.00 | +0.02 | -0.01 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.26 | +1.20 | +0.05 | +0.01 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.20 | -0.80 | -0.25 | -0.14 | -0.01 | +3.5% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.95 | +0.00 | -0.32 | -0.49 | -0.14 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.83 | +0.00 | -0.26 | -0.35 | -0.22 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.82 | +0.00 | -0.67 | -0.15 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.78 | -0.50 | -0.26 | -0.03 | +0.01 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.77 | -0.80 | +0.02 | +0.01 | -0.01 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.70 | +0.00 | +0.61 | +0.04 | +0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.60 | +0.00 | -0.56 | -0.04 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +5.8% | +5.8% | +5.5 | +0.3 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.8% | -2.8% | -2.6 | -0.1 | -0.0 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.1% | +1.9% | +2.0 | +0.1 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.5% | +1.7% | +3.3 | +0.1 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.1 | -0.0 | -0.0 |
| New BrahMos/defence export contracts (Philippines follow-on, Indonesia, Vietnam or others) announced (`EV_DEFENCE_EXPORT_ORDERS`) | anticipated | 0.50 | +2.3% | +1.2% | +2.3 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | +0.0 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.8% | -0.7% | -2.0 | -0.7 | -0.2 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | -0.0 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.6% | +0.6% | +0.6 | +0.0 | -0.0 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -4.1% | -0.6% | -2.0 | -2.1 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.1% | +0.6% | +0.3 | +0.4 | +0.3 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BEL | +3.00% | +1.50% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BEL | +1.65% | +1.48% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → BEL | +1.20% | +0.60% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ P_DEFENCE_PROCUREMENT → BEL | +1.10% | +0.55% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BEL | -2.00% | -0.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BEL | -0.80% | -0.34% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BEL | -1.80% | -0.32% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BEL | -2.00% | -0.30% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → BEL | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → BEL | -1.15% | -0.29% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BEL | +0.30% | +0.27% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BEL | +1.08% | +0.27% |
| 2 | EV_INDIA_PAK_CRISIS ⇒ C_INDIA_PAKISTAN → P_DEFENCE_PROCUREMENT → BEL | +2.75% | +0.25% |
| 1 | EV_INDIA_PAK_CRISIS ⇒ C_INDIA_PAKISTAN → BEL | +2.50% | +0.22% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BEL | -0.80% | -0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_DEFENCE_PROCUREMENT → BEL | +0.50 | director_override | +2.75% |
| 1 | F_FPI_FLOWS → BEL | -1.60 | events | -1.92% |
| 1 | F_REPO_IN → BEL | +1.00 | events | -0.80% |
| 1 | F_GOVT_CAPEX → BEL | +0.20 | director_override | +0.30% |
| 1 | F_USDINR → BEL | -0.37 | observed | +0.18% |
| 2 | P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → BEL | +0.50 | director_override | +0.12% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BEL | -0.30 | events | +0.11% |
| 1 | F_RISK_SENTIMENT → BEL | +0.11 | observed | -0.09% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → BEL | -0.10 | events | +0.05% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → BEL | -0.10 | events | +0.02% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Large single order(s) (e.g. air defence, EW suite) from DAC-cleared proposals; mgmt targets ~Rs55,000 cr FY27 inflow (ET Now 2026-10-30) *(review: [RT_TOP_A] guided inflow; AoN already in state)* | other | 0.50 | +1.8% | +0.88% |
| 2026-12 | FY27 revenue guidance delivery check at Q3 (Kotak raised target on guidance, NDTV Profit 2026-11-04) | guidance | 0.70 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (late Jan); Q2 reported 2026-10-30 | results | 0.90 | +0.0% | +0.00% |

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