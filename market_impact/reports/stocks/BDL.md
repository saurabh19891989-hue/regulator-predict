# BDL — Bharat Dynamics Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.0%**, **12 months +2.2%** (rank 106 / 10 of 200 for 3m / 12m); beta 1.40
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +40.7%): 3 months 50%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.9% … P90 +7.6%; plausible 12m relative-return range incl. stock-specific noise: -48.9% … +53.0%
- Decomposition (12m): 0.5 × forward event exposure +2.2% (3m +0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +7.0% (beta-adjusted) vs a realised market-adjusted move of -17.5% — gap +24.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +1.08 | -0.01 | +1.07 | +0.09 |
| Sector | -0.02 | -0.00 | -0.02 | -0.03 |
| Theme | +0.45 | +0.02 | +0.47 | +0.24 |
| Geopolitics | +0.23 | +0.14 | +0.37 | +0.13 |
| Company catalysts | +1.24 | +0.00 | +1.24 | +0.00 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.80 | -0.36 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+2.18** | **-0.03** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +6.19 | +3.00 | +2.81 | +0.38 | +0.00 | — |
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +5.42 | +5.00 | +0.42 | +0.00 | +0.00 | — |
| Indian defence exports (`T_DEFENCE_EXPORTS`) | +1 | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.46 | +1.50 | +0.00 | -0.03 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.09 | -1.00 | -0.05 | -0.03 | -0.01 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.88 | -0.80 | -0.05 | -0.04 | +0.01 | -1.1% |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -0.83 | -0.80 | +0.00 | -0.02 | -0.01 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.69 | +0.00 | -0.40 | -0.26 | -0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.57 | +0.00 | -0.25 | -0.20 | -0.12 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.56 | -0.60 | +0.03 | +0.01 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -0.50 | -0.50 | +0.00 | +0.00 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.49 | +0.00 | -0.48 | -0.02 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.49 | +0.00 | -0.51 | +0.01 | +0.01 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.48 | +0.00 | -0.40 | -0.10 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +5.4% | +5.4% | +5.0 | +0.4 | +0.0 | +0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.9% | +1.7% | +1.8 | +0.1 | -0.0 | -0.0 |
| New BrahMos/defence export contracts (Philippines follow-on, Indonesia, Vietnam or others) announced (`EV_DEFENCE_EXPORT_ORDERS`) | anticipated | 0.50 | +2.8% | +1.4% | +2.8 | +0.0 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.4% | +1.4% | +1.5 | -0.1 | -0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | -0.7% | -0.7% | -0.8 | +0.1 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.4% | -0.6% | -2.5 | +0.2 | -0.2 | +0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.6 | +0.0 | +0.0 |
| India-Pakistan military crisis (terror attack, cross-border strikes) after Op Sindoor (May 2025) (`EV_INDIA_PAK_CRISIS`) | risk_scenario | 0.09 | +5.1% | +0.5% | +2.0 | +2.8 | +0.3 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -2.8% | -0.4% | -2.5 | -0.1 | -0.2 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +0.7% | +0.4% | +0.4 | +0.2 | +0.1 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BDL | +1.50% | +1.35% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → BDL | +1.80% | +0.90% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BDL | -2.50% | -0.62% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ P_DEFENCE_PROCUREMENT → BDL | +1.00% | +0.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BDL | -2.50% | -0.38% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BDL | +0.30% | +0.27% |
| 1 | EV_INDIA_PAK_CRISIS ⇒ C_INDIA_PAKISTAN → BDL | +3.00% | +0.27% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BDL | -0.60% | -0.25% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → BDL | -1.00% | -0.25% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → BDL | +0.40% | +0.25% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → BDL | +0.80% | +0.24% |
| 2 | EV_INDIA_PAK_CRISIS ⇒ C_INDIA_PAKISTAN → P_DEFENCE_PROCUREMENT → BDL | +2.50% | +0.22% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → BDL | +0.40% | +0.22% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → BDL | +0.40% | +0.20% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BDL | -1.04% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_DEFENCE_PROCUREMENT → BDL | +0.50 | director_override | +2.50% |
| 1 | C_RUSSIA → BDL | +1.00 | events | -0.80% |
| 1 | F_REPO_IN → BDL | +1.00 | events | -0.60% |
| 1 | F_ALUMINIUM → BDL | -1.96 | observed | -0.59% |
| 1 | F_GOVT_CAPEX → BDL | +0.20 | director_override | +0.30% |
| 1 | F_USDINR → BDL | -0.37 | observed | +0.30% |
| 2 | P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → BDL | +0.50 | director_override | +0.18% |
| 1 | F_RISK_SENTIMENT → BDL | +0.11 | observed | -0.11% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BDL | -0.30 | events | +0.04% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → BDL | -0.10 | events | +0.02% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → BDL | -0.10 | events | +0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-12 | Q2 FY27 results (screener upcoming-date field) | results | 0.95 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results; execution of Rs26,176 cr order book (conversion pace is the key variable) | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Large missile order(s) from DAC-cleared Rs2.12 lakh cr proposals (Akash-NG, Astra, Invar etc. share unknown) *(review: [RT_TOP_A] contract stage of the AoN already in P_DEFENCE_PROCUREMENT state)* | other | 0.40 | +3.8% | +1.50% |
| 2027-03 | Export contract announcement | other | 0.15 | +6.5% | +0.97% |

## Analyst profile (agent research, sourced)
# BDL - Bharat Dynamics Ltd. (Defence PSU, missiles)

## Business
Bharat Dynamics makes guided missiles and underwater weapons, principally for the Indian MoD, under DRDO designs (Akash, Astra) and foreign licences (Invar). The business is long-cycle: order book Rs26,176 cr is roughly nine times TTM sales, but delivery milestones are lumpy (FY26 sales -19%, Q1 FY27 +131%). Treasury income (Rs440 cr TTM) exceeds operating profit (Rs352 cr), so reported PAT and P/E (75x) are distorted. The stock fell 27% in 12 months to a 52-week low on 2026-10-28.

## What moves the stock, ranked
1. **Defence procurement flow** (P_DEFENCE_PROCUREMENT +5.0 per +10% orders): DAC approvals (Rs2.12 lakh cr on 2026-10-26/27) and actual order placement.
2. **Execution cadence**: quarterly revenue and margin surprises (results 2026-11-12).
3. **Geopolitical escalation** (India-Pakistan +3.0) and export wins (+3.0).
4. **Market risk appetite and rates** (high beta 1.6-1.7; repo 5.50% after the 2026-10-07 hike affects both treasury income and the multiple).
5. **Supply chain**: Russian licence content, imported electronics, rupee.

## Transmission examples
- **India-Pakistan border escalation -> emergency procurement and replenishment of missile stocks -> accelerated Akash/Astra/Invar orders -> BDL revenue visibility up** (2nd-3rd order); simultaneously it lifts Brent slightly and FPI outflows (4th order) which hit the stock's beta.
- **Higher repo -> bank deposit rates up -> BDL treasury yield up (+) but 75x P/E discounted at a higher rate (-)**; the net is negative in the model.
- **Russia sanctions/payment issues -> Invar kits delayed -> milestone billing slips -> quarterly revenue misses** (3rd order).
- **Semiconductor tightening -> seeker electronics delayed -> deliveries slip to next quarter.**

## Current situation
Orders: Rs811 cr anti-airfield weapons (2026-09-23), Rs1,307 cr Navy order (2026-10-15). Brokers see Akash and Astra ramp-ups driving growth (2026-10-08). Despite the 2026-10-27 DAC news the stock remained near lows, signalling market doubt about conversion. Promoters 74.93%, FIIs 1.8%.

## Upcoming
Q2 FY27 results on 2026-11-12 (screener); possible big missile orders from DAC-cleared proposals; Q3 results Feb 2027.

## Bull and bear
Bull: order book visibility, converting Akash-NG/Astra into higher deliveries, margin recovery from 15% toward 20-25%. Bear: execution slippage, single customer, treasury income masking low operating margin, valuation.

Uncertainties: import content, deposit size, DAC allocation to BDL are assumptions or unverified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.