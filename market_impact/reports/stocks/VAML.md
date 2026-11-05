# VAML — Vedanta Aluminium Metal Ltd.
*NIFTY_NEXT_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months +0.2%** (rank 105 / 99 of 200 for 3m / 12m); beta 1.00
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.1%): 3 months 49%, 12 months 68%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.1% … P90 +12.2%; plausible 12m relative-return range incl. stock-specific noise: -12.4% … +43.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -21.9% beta-adjusted vs realised market-adjusted move —%); forward event exposure +5.9% (3m +2.9%; half assumed priced); company-specific events -3.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Aluminium price (`F_ALUMINIUM`) | +10% aluminium | +10.00 | +10.00 | +0.00 | +0.00 | +0.00 | -19.6% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +5.86 | +0.00 | +3.80 | +2.07 | -0.00 | — |
| Copper price (`F_COPPER`) | +10% copper | +4.00 | +0.00 | +4.00 | +0.00 | +0.00 | -2.4% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.66 | +3.00 | +0.00 | -0.17 | -0.17 | -1.1% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +2.49 | +0.00 | +2.14 | +0.27 | +0.08 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.31 | +1.00 | +0.86 | +0.45 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.87 | +0.00 | +0.58 | +0.84 | +0.44 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.76 | +0.00 | -0.19 | -0.99 | -0.58 | — |
| Indian domestic coal price & availability cost (`F_COAL_INDIA`) | +10% domestic coal cost (notified/e-auction) | -1.37 | -1.20 | -0.17 | +0.00 | +0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.33 | +0.00 | -0.50 | -0.78 | -0.06 | +2.2% |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | -1.17 | +0.00 | -1.07 | -0.10 | +0.00 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.10 | -1.10 | +0.00 | +0.00 | +0.00 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -19.6% | -19.6% | -19.6 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +3.6% | +3.6% | +0.0 | +4.2 | +0.5 | -1.2 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -2.8% | -2.8% | -2.4 | -0.4 | +0.0 | +0.0 |
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | -2.6% | -2.6% | -2.6 | +0.0 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +5.8% | +2.0% | +0.0 | +3.7 | +2.1 | +0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +1.6% | +1.6% | +0.0 | +1.0 | +0.6 | +0.0 |
| China Central Economic Work Conference / NPC (Dec 2026-Mar 2027): larger-than-expected fiscal or property stimulus (`EV_CHINA_CEWC_STIMULUS_DEC26`) | anticipated | 0.45 | +3.1% | +1.4% | +0.0 | +3.1 | -0.1 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | +0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +1.2% | +1.2% | +0.5 | +0.5 | +0.2 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -2.1% | -1.2% | +0.4 | -2.8 | -0.1 | +0.4 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.7 | -0.4 | -0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.2% | -1.2% | -1.1 | -0.1 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → VAML | -2.40% | -1.39% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → VAML | +3.80% | +1.33% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → VAML | +2.88% | +1.03% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → VAML | -2.40% | -0.96% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → VAML | -3.20% | -0.90% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → VAML | +3.90% | +0.86% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → VAML | +2.37% | +0.85% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → VAML | -1.42% | -0.83% |
| 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → F_ALUMINIUM → VAML | +2.20% | +0.77% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → F_ALUMINIUM → VAML | +1.60% | +0.72% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → VAML | -4.00% | -0.72% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → VAML | -1.38% | -0.69% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_CHINA_GDP → F_ALUMINIUM → VAML | +1.52% | +0.68% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → VAML | -1.87% | -0.67% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → VAML | +1.12% | +0.65% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_ALUMINIUM → VAML | -1.96 | observed | -19.61% |
| 1 | F_POWER_PRICE_IN → VAML | +3.00 | events | -2.40% |
| 1 | F_COAL_INDIA → VAML | +1.50 | events | -1.80% |
| 1 | F_GSEC_10Y_IN → VAML | +1.70 | events | -1.19% |
| 1 | F_USDINR → VAML | -0.37 | observed | -1.11% |
| 1 | T_ENERGY_TRANSITION → VAML | +0.50 | events | +0.50% |
| 1 | F_CREDIT_SPREADS_IN → VAML | +0.50 | events | -0.50% |
| 1 | P_ANTI_DUMPING_IN → VAML | +0.40 | events | +0.20% |
| 1 | F_RISK_SENTIMENT → VAML | +0.11 | observed | -0.09% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → VAML | +0.40 | events | -0.04% |
| 2 | F_BRENT → F_CHEM_FEEDSTOCK → VAML | +0.00 | observed | -0.00% |

## Analyst profile (agent research, sourced)
# VAML — Vedanta Aluminium Metal Ltd. (Nifty Next 50) — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast; no expected-return number. VAML listed on 2026-06-15, so there are only ~20 weeks of price history and no empirical sensitivities; every weight below is fundamentals-based (confidence medium at best).

## 1. Business
India's largest primary aluminium producer: smelters at Jharsuguda and BALCO (Korba) of ~2.6 Mtpa, the Lanjigarh alumina refinery, captive coal mines and captive/group power, with value-added products (billets, wire rod, rolled and foundry alloys) now about two-thirds of sales. It was demerged from Vedanta Ltd, with shares issued 1:1 to Vedanta holders, and the promoter's 56.38% is encumbered with GLAS Agency as security trustee for the promoter group's dollar financings. Q2 FY27: aluminium 649 kt (record, +5%), alumina +37%, revenue ~Rs22,100-22,300 cr (+41%), EBITDA ~Rs10,100-10,200 cr (45% margin, +83%), PAT Rs6,187 cr (about double), net debt/EBITDA 0.7x (0.9x in Q1). Market cap Rs1.49 lakh cr; EV roughly Rs1.77 lakh cr (net debt derived at ~Rs28,000 cr).

## 2. What moves the stock, ranked
1. **LME aluminium (w +10 per +10%).** About 2.6 Mt x US$320 = Rs7,900 cr of annual EBITDA per +10%, about +17% of annualised EBITDA after hedges. Aluminium is -19.6% since 1 June to ~US$3,200/t, so the next quarters will not repeat Q2's 45% margin.
2. **Coal (-1.2) and power (-0.8) cost.** Roughly 40% of costs are coal and power; captive coal covers ~60%. Coal e-auction premia hit ~94% in September-October and spot power touched Rs20/unit.
3. **Carbon, caustic and fluoride feedstock (-1.1 per +10%).** Crude-linked pet-coke and pitch.
4. **USD/INR (+3.0 per +3%).**
5. **Bauxite and royalty (-1.0).** The Odisha High Court dismissed the plea for OMC bauxite at Rs1,000/t; VAML has booked Rs3,000/t since April (market ~Rs3,800/t). CLSA estimates a one-time hit of up to US$290 mn pre-tax (US$195 mn post-tax, ~1.2% of mcap) and ~US$10/t higher cost; SAHI reports an OMC demand of Rs5,600 cr (unreconciled with CLSA's ~Rs2,500 cr before interest).
6. **Financing/pledge (-1.0), rates (-0.7), group (VEDL contagion 0.35).**

## 3. Transmission chains
**Fed/dollar/China chain (4th order).** Iran war and food inflation -> Fed hike (16 Sep) and 10y UST ~4.9% -> dollar index +2% since June -> weaker commodity demand and a heavier China export push (China Q3 GDP +4.5% on exports; processing PMI 48.9) -> LME aluminium -19.6% since June -> VAML EBITDA falls ~17% per -10% -> lower dividend capacity and a slower deleveraging -> weaker equity for a promoter-pledged stock -> forced-sale and group-credit contagion (VEDL, HZL).

**Coal-crunch chain.** Weak monsoon and El Nino -> power demand surge and critical coal stocks at 74 plants -> government prioritises grid supply, invokes emergency powers for captive plants and Coal India e-auction premia reach ~94% -> VAML's non-captive coal cost up (-1.2 per +10%) and regulatory diversion risk for captive power -> if summer 2027 repeats the shortfall (odds 0.4), potline curtailment lowers output -> smaller volumes and a higher cost per tonne at the same time; this is the main non-price tail risk.

**Rupee chain.** Record FPI outflow (Rs3 lakh cr) and RBI tightening (repo 5.50%) -> rupee at 95-96 -> USD-linked revenue exceeds USD costs by ~Rs2,300 cr a year per +3% -> +3.0 on the stock, partly offset by the higher discount rate and the 56.38% pledge channel.

**Policy chain.** India-EU FTA signing (16 Dec) with a CBAM annex for aluminium exporters -> lower CBAM leakage for exports and domestic anti-dumping probes -> a modest premium for value-added products. Union Budget (1 Feb) could change customs duty on aluminium and scrap.

## 4. Current situation
Q2 results were strong (profit doubled) but the stock has fallen 20.6% in three months and touched Rs364.7 on 29 Oct; Nifty Metal slid over 3% on 23 Oct. Brokers remain constructive: ICICI Securities Buy TP Rs490, Emkay Buy TP Rs550 (up to 53% upside), CLSA Outperform TP Rs540. Debt reduced Rs3,090 cr in the quarter. The group promoter encumbrance (16 Sep US$400m bond tap) is an overhang.

## 5. Upcoming events
Odisha HC order follow-up (appeal/SLP, OMC payments); Q3 FY27 results (~Jan 2027); India-EU FTA (16 Dec); China CEWC (Dec); Union Budget 1 Feb; summer-2027 power outlook; promoter refinancing and GLAS encumbrance changes.

## 6. Bull and bear
**Bull:** aluminium rebounds on Chinese stimulus or a Fed pause, bauxite security via Sijimali, value-added mix, net debt/EBITDA falling below 0.5x, targets of Rs490-550 imply 28-44% upside.
**Bear:** LME falls toward US$2,800, coal/power costs and curtailment, OMC dues larger than modelled, promoter pledge stress, and short trading history with index-linked flows.

Weak spots: net debt (derived from ND/EBITDA 0.7x), hedge ratio, export share, related-party power arrangements, and the revenue/EBITDA mismatch between press and screener.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.