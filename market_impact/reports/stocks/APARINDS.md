# APARINDS — Apar Industries Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months +0.1%** (rank 102 / 100 of 200 for 3m / 12m); beta 1.31
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +46.0%): 3 months 50%, 12 months 62%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.0% … P90 +4.1%; plausible 12m relative-return range incl. stock-specific noise: -58.2% … +51.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +7.7% beta-adjusted vs realised market-adjusted move +17.6%); forward event exposure +3.3% (3m +1.6%; half assumed priced); company-specific events -0.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +3.29 | +0.00 | +2.32 | +0.93 | +0.04 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.96 | +2.00 | +0.95 | +0.04 | -0.03 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -2.40 | -2.50 | +0.07 | +0.06 | -0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.96 | -1.00 | -0.97 | +0.12 | -0.10 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.87 | +0.00 | -1.48 | -0.36 | -0.03 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.64 | +0.00 | -1.53 | -0.13 | +0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.55 | -1.50 | -0.04 | -0.01 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.50 | -1.50 | +0.16 | -0.09 | -0.07 | +0.0% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.43 | +1.20 | +0.29 | -0.06 | -0.00 | +1.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.39 | -1.20 | -0.20 | +0.02 | -0.01 | +3.5% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.28 | +1.50 | +0.00 | -0.16 | -0.06 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.05 | +0.00 | -0.96 | +0.02 | -0.11 | — |
| Aluminium price (`F_ALUMINIUM`) | +10% aluminium | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | -19.6% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -9.1% | -9.1% | -8.9 | +0.7 | -0.5 | -0.3 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.8% | +2.8% | +1.0 | +1.8 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -8.5% | -2.4% | -8.4 | +0.2 | -0.2 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.5% | -2.3% | -6.4 | +0.3 | -0.2 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.8% | +2.2% | +3.9 | -0.3 | +0.1 | +0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.9% | +1.9% | +1.2 | +0.7 | -0.2 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.8 | -0.2 | +0.1 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.6% | +1.6% | +0.0 | +1.2 | +0.5 | +0.0 |
| India-US interim trade agreement formally signed/announced (`EV_INDIA_US_INTERIM_DEAL_SIGNED`) | anticipated | 0.65 | +2.4% | +1.6% | +2.5 | -0.1 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | -0.0 | -0.0 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -7.3% | -1.3% | -7.8 | +0.3 | +0.3 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → APARINDS | +2.50% | +1.62% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → APARINDS | -4.80% | -1.34% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → APARINDS | -3.75% | -1.34% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → APARINDS | +2.25% | +1.31% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → APARINDS | +1.20% | +1.08% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → APARINDS | -6.00% | -1.08% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → APARINDS | -3.60% | -1.01% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → APARINDS | -6.25% | -0.94% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → APARINDS | -3.60% | -0.90% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → APARINDS | -1.50% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → APARINDS | +1.00% | +0.58% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → APARINDS | +1.44% | +0.58% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → APARINDS | -9.00% | -0.56% |
| 1 | EV_INDIA_US_TALKS_COLLAPSE ⇒ P_US_TARIFF_INDIA → APARINDS | -3.75% | -0.56% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → APARINDS | -1.44% | -0.51% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_ALUMINIUM → APARINDS | -1.96 | observed | -1.96% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → APARINDS | +1.50 | events | +1.92% |
| 1 | C_MIDEAST_CONFLICT → APARINDS | +1.50 | events | -1.50% |
| 1 | P_US_TARIFF_INDIA → APARINDS | -0.60 | events | +1.50% |
| 1 | F_REPO_IN → APARINDS | +1.00 | events | -1.50% |
| 1 | F_GOVT_CAPEX → APARINDS | +1.00 | events | +1.50% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → APARINDS | +1.20 | events | +1.15% |
| 1 | T_ENERGY_TRANSITION → APARINDS | +0.50 | events | +1.00% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → APARINDS | +0.50 | events | +0.40% |
| 1 | F_USDINR → APARINDS | -0.37 | observed | -0.37% |
| 1 | F_US_EQUITIES → APARINDS | +0.23 | observed | +0.28% |
| 1 | F_COPPER → APARINDS | -0.24 | observed | -0.14% |

## Analyst profile (agent research, sourced)
# APARINDS - Apar Industries (Capital Goods, mid-cap)

## Business
Apar sells metal-linked electrical products. Conductors (aluminium-alloy and high-temperature conductors for transmission lines), transformer and specialty oils (base-oil blends for transformers, auto and industrial uses) and power/telecom/specialty cables each contribute roughly a quarter to two-fifths of revenue (split is model knowledge; the dossier does not give it). A large share of conductor and oil sales is exported. FY26 revenue was Rs22,902 cr and TTM EBITDA margin 9.5%. Q2 FY27 (reported 2026-10-29) delivered PAT Rs447 cr (+78% YoY) and margins about 190bp higher YoY; management frames a "$2.4bn platform" with four growth cycles (Investing.com headline, 2026-10-29).

## What moves the stock, ranked
1. **Grid electrification and government capex** (T_GRID_ELECTRIFICATION +4, F_GOVT_CAPEX +1.5 per SSU): the demand base for conductors and cables.
2. **Rates and risk sentiment** (repo -1.5 per +25bp, VIX -1.2 per +5): P/E 47x, beta ~1.4, +90% in 12 months. RBI hiked to 5.50% on 2026-10-07, the first hike in about four years.
3. **Brent / base oil** (-1.5 per +10%): oils margin squeezes when crude rises faster than price resets.
4. **US tariffs and Middle East** (-2.5 per +10pp tariff; -1.0 for escalation): export exposure and the KSA unit.
5. **Metals** (aluminium +1.0, copper +0.6): mostly pass-through; inventory gains help short-term, working capital hurts.
6. **USD/INR** (+1.0 per +3%): exporter benefit on conversion margin.

## Transmission examples
- **Middle East escalation -> Brent up -> base-oil costs up -> specialty-oil spread squeezed -> Apar oils margin down** (2nd/3rd order). The same Brent rise pushes INR weaker (F_USDINR), a small positive for exports (4th-order offset), and raises India inflation -> RBI stays tight -> discount rate up -> multiple compression.
- **Govt capex up -> PGCIL/state tenders -> conductor and cable order inflow -> utilisation and per-tonne margin up** (3rd order via order book), lag 3-12 months.
- **Global growth scare -> VIX up -> FIIs reduce mid-cap capital goods -> Apar de-rates** even with intact earnings, because FII ownership just rose to 12.55%.
- **US tariff hike -> US importers shift to lower-cost sources or absorb -> Apar export price realisation falls -> EBITDA/tonne down.**

## Current situation
Q2 FY27 beat estimates (CNBC TV18, 2026-10-29). Rating upgraded to AA stable by CARE (2026-09-10). A subsidiary will buy 70% of a Chinese cable maker (2026-10-30; terms not verified). Promoters' stake fell to 55.42% in the Sep quarter. Stock was -12% over the last month after a +90% 12-month run, so near-term sentiment is cooling.

## Upcoming
Q3 FY27 results in late Jan 2027; completion of the Chinese acquisition; KSA unit ramp; any US trade action.

## Bull vs bear
Bull: margins hold >10% as specialty oils and cables scale, T&D tender flow is strong, EPS annualises near Rs 400+. Bear: P/E 47x, promoter selling, metal-price volatility and tariffs leave little margin for error; high-cost borrowing and a hiking cycle weigh on multiples.

Uncertainties: segment/export splits and net debt are model knowledge; weights for tariffs and energy-transition are low confidence.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.