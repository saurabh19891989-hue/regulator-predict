# ADANIPORTS — Adani Ports and Special Economic Zone Ltd.
*NIFTY_50 · Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months +1.6%** (rank 74 / 38 of 200 for 3m / 12m); beta 1.23
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.3%): 3 months 52%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.3% … P90 +4.8%; plausible 12m relative-return range incl. stock-specific noise: -23.2% … +22.9%
- Decomposition (12m): 0.5 × forward event exposure +2.6% (3m +1.2%; half assumed priced) + 0.5 × company-specific catalysts +1.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -2.6% (beta-adjusted) vs a realised market-adjusted move of +2.7% — gap -5.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.17 | +2.20 | -0.04 | +0.00 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.04 | -1.50 | -0.23 | -0.13 | -0.18 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.54 | +1.20 | +0.29 | +0.12 | -0.06 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.47 | +1.60 | +0.12 | -0.16 | -0.08 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.34 | -1.20 | -0.12 | -0.01 | -0.01 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -1.27 | -1.20 | +0.00 | -0.06 | -0.01 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +1.22 | +1.20 | -0.04 | +0.06 | +0.01 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -1.21 | -0.80 | -0.36 | -0.04 | -0.01 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | -1.08 | -1.00 | -0.12 | +0.02 | +0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.06 | +0.00 | +1.02 | +0.13 | -0.10 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.05 | +0.00 | -0.86 | -0.15 | -0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.04 | -0.60 | -0.34 | -0.09 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.04 | +0.00 | -0.70 | -0.34 | +0.01 | +3.5% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +0.95 | +0.00 | +1.02 | +0.05 | -0.12 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.8% | -4.8% | -4.8 | +0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.4% | +2.7% | +5.5 | -0.2 | -0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.0 | +0.0 | -0.0 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.9% | +1.9% | +2.0 | +0.1 | -0.1 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.2 | -0.1 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.6% | +1.5% | +1.9 | +0.5 | +0.2 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.2 | -0.0 | -0.1 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.2% | +1.2% | +1.2 | +0.1 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.5 | -0.7 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.1% | -1.0% | -2.5 | -1.1 | -0.4 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.5 | -0.3 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.9% | -1.0% | +0.0 | -3.9 | -0.2 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIPORTS | +5.50% | +2.75% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → ADANIPORTS | +1.50% | +0.83% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ADANIPORTS | -3.30% | -0.59% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → ADANIPORTS | +0.72% | +0.58% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIPORTS | -2.11% | -0.53% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIPORTS | -2.11% | -0.53% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIPORTS | -2.05% | -0.51% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIPORTS | -0.96% | -0.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → ADANIPORTS | -1.80% | -0.45% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → ADANIPORTS | +1.10% | +0.39% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → ADANIPORTS | -0.60% | -0.36% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → ADANIPORTS | +0.44% | +0.35% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIPORTS | -2.05% | -0.31% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → ADANIPORTS | -2.00% | -0.30% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → ADANIPORTS | +0.43% | +0.29% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ADANIPORTS | -1.60 | events | -3.52% |
| 1 | F_GSEC_10Y_IN → ADANIPORTS | +1.55 | director_override | -1.86% |
| 1 | C_MIDEAST_CONFLICT → ADANIPORTS | +1.00 | events | -1.50% |
| 1 | F_GDP_IN → ADANIPORTS | +0.50 | events | +0.80% |
| 1 | F_REPO_IN → ADANIPORTS | +1.00 | events | -0.60% |
| 1 | F_CREDIT_SPREADS_IN → ADANIPORTS | +0.50 | events | -0.60% |
| 1 | P_US_TARIFF_INDIA → ADANIPORTS | -0.60 | events | +0.48% |
| 1 | F_IRON_ORE → ADANIPORTS | -0.83 | observed | -0.42% |
| 1 | C_RED_SEA → ADANIPORTS | +1.00 | events | -0.40% |
| 1 | F_USDINR → ADANIPORTS | -0.37 | observed | -0.37% |
| 1 | F_GOVT_CAPEX → ADANIPORTS | +0.20 | director_override | +0.24% |
| 1 | F_COAL_INTL → ADANIPORTS | +0.70 | director_override | -0.21% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11/2027-03 | Evos Terminals US$3.3 bn bid: outcome (win would add leverage ~+0.6x ND/EBITDA; model estimate) - not yet announced as accepted | corporate_action | 0.35 | +0.0% | +0.00% |
| 2026-12 | Monthly cargo update (Nov) - October was +27% y/y | other | 0.95 | +0.2% | +0.24% |
| 2026-12/2027-06 | Group legal/regulatory: SEC civil matter and Hindenburg-era follow-ups; criminal case already dismissed 2026-08-11 | litigation | 0.15 | -3.0% | -0.45% |
| 2027-02 | Q3 FY27 results vs raised guidance bands | results | 0.95 | +0.5% | +0.47% |
| 2027-05 | FY27 results and FY28 guidance; Vizhinjam/ Paradip/ Oman ramp | guidance | 0.90 | +1.0% | +0.90% |

## Analyst profile (agent research, sourced)
# Adani Ports and SEZ (ADANIPORTS) - profile as of 2026-11-05

## Business
APSEZ is India's largest private port operator, with domestic ports (Mundra, Krishnapatnam, Dhamra, Kandla, Vizhinjam, Paradip berths), a growing logistics arm (rail, warehousing), marine services and international terminals (Haifa, Colombo, Tanzania, Australia; an Oman subsidiary was set up on 2026-10-23). Margins are very high (operating margin about 60%). Q2 FY27: revenue +24%, EBITDA +23%, PAT Rs 3,682 crore (+18%), and the FY27 revenue and EBITDA guidance bands were each raised by Rs 1,000 crore (company release, 2026-10-28). October cargo rose 27% (marketscreener, 2026-11-02). On 2026-10-30 it placed a US$3.3 billion bid for Evos Terminals, and on 2026-08-11 a US court dismissed the criminal case against Gautam Adani. The stock sits at its 52-week high (Rs 1,934) after +34% in 12 months.

## What moves the stock
1. **India growth and trade volumes** (GDP +1.6 per +1pp; China+1 +1.2; US tariffs -0.8; government infrastructure capex +1.2).
2. **Group/governance and financing** (credit spreads -1.2; group contagion from ADANIENT 0.15; the case dismissal removed a major tail risk).
3. **Geopolitics** (Middle East escalation -1.5 because of Haifa and Gulf routes; India-Pakistan -1.0; Red Sea ambiguous).
4. **Rates and flows** (G-sec -1.2, repo -0.6, FPI +2.2) after the RBI's hike to 5.50% on 2026-10-07.
5. **USD/INR (+1.0, shrunk)**: the pack shows +2.91 per +3% (t=2.0); mechanism is plausible (USD-linked tariffs and overseas earnings) but USD debt offsets.

## Transmission examples
- **Geopolitical chain (4 orders)**: Israel-Iran or wider Gulf escalation -> Brent up (already $95) and war-risk premia -> Haifa volumes fall and Gulf-route shipping reroutes -> APSEZ international EBITDA and Mundra Gulf feeder volumes dip -> group risk-off hits financing spreads and valuation.
- **Trade chain (4 orders)**: higher US tariff on Indian goods -> export volumes fall -> container throughput at Mundra/Vizhinjam slows -> logistics (rail, warehousing) utilisation falls -> operating leverage cuts EBITDA by roughly 1 to 2 times the volume drop.
- **Rate chain (3 orders)**: Brent -> CPI -> RBI tightening -> higher INR bond yields -> group refinancing costs and discount rate up -> multiple compression; larger because of the Evos acquisition debt.
- **China+1 (3 orders)**: manufacturing relocation -> electronics and apparel exports -> Mundra/Vizhinjam box volumes -> port and logistics EBITDA growth.

## Current situation
Strong operations and guidance raise; the market is cheering volumes (+27% October) but has to digest a large acquisition and a stock at its highs. Governance tail risk is lower after the US criminal case was dismissed, though the civil matter and group financing remain watch items (our sources did not retrieve their current status).

## Upcoming
Monthly cargo updates, Evos bid outcome (prob ~0.35 of agreement within six months), Q3 results (~February 2027), December MPC, Vizhinjam/Oman ramp.

## Bull / Bear
Bull: sustained 20%+ cargo growth, accretive Evos deal, group risk premium falls. Bear: Middle East escalation hits Haifa/Gulf trade, leverage and rates rise, governance headlines return. Confidence medium; segment shares, debt split, Haifa share and USD debt are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.