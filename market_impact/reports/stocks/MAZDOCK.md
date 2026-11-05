# MAZDOCK — Mazagoan Dock Shipbuilders Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +8.0%**, **12 months +16.3%** (rank 1 / 1 of 200 for 3m / 12m); beta 1.39
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +31.2%): 3 months 70%, 12 months 65%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +14.1% … P90 +23.6%; plausible 12m relative-return range incl. stock-specific noise: -17.8% … +46.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +6.4 pp (model impact +12.9% beta-adjusted vs realised market-adjusted move -30.2%); forward event exposure +13.9% (3m +3.6%; half assumed priced); company-specific events +8.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +6.27 | +6.00 | +0.28 | +0.00 | -0.01 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +6.26 | +3.00 | +3.06 | +0.22 | -0.01 | — |
| Competition among Indian shipyards for major naval programmes (`NEW_DEFENCE_SHIPYARD_COMPETITION`) | +1 = a major naval programme awarded to a competing yard | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.32 | +2.50 | -0.04 | -0.09 | -0.05 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.54 | +0.00 | -1.58 | -0.02 | +0.06 | — |
| Indian defence exports (`T_DEFENCE_EXPORTS`) | +1 | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.44 | -1.00 | -0.30 | -0.14 | +0.00 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.14 | -1.20 | +0.04 | +0.02 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.95 | +0.80 | +0.09 | +0.03 | +0.03 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.90 | +0.00 | -0.41 | -0.38 | -0.11 | +0.0% |
| US dollar index (`F_DXY`) | +3% DXY | -0.88 | +0.00 | -0.59 | -0.23 | -0.07 | +2.2% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.86 | +0.00 | +0.00 | -0.87 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.79 | +0.00 | -0.42 | -0.28 | -0.09 | +3.5% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.76 | +0.00 | -0.80 | +0.00 | +0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +8.0% | +7.2% | +8.0 | +0.1 | -0.1 | -0.0 |
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +6.3% | +6.3% | +6.0 | +0.3 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.1% | -3.1% | +1.5 | -2.0 | -2.0 | -0.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.2% | -2.2% | -1.8 | -0.3 | -0.1 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.1% | +2.1% | +2.5 | -0.3 | -0.1 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.8 | -0.0 | +0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.8 | +0.3 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.5% | +1.2% | +2.0 | +0.3 | +0.1 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -1.2 | +0.0 | +0.0 | -0.0 |
| New BrahMos/defence export contracts (Philippines follow-on, Indonesia, Vietnam or others) announced (`EV_DEFENCE_EXPORT_ORDERS`) | anticipated | 0.50 | +2.1% | +1.1% | +2.1 | +0.0 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -3.5% | -1.0% | +0.0 | -2.4 | -0.8 | -0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.7 | -0.2 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | +6.00% | +5.40% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → MAZDOCK | +2.00% | +1.80% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MAZDOCK | +2.00% | +1.00% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → MAZDOCK | +1.50% | +0.68% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | +1.20% | +0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK | -1.00% | -0.58% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MAZDOCK | -1.20% | -0.48% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → MAZDOCK | +0.90% | +0.45% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → MAZDOCK | +1.20% | +0.43% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → MAZDOCK | +0.60% | +0.36% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → MAZDOCK | -1.38% | -0.35% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MAZDOCK | -1.19% | -0.33% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MAZDOCK | -1.20% | -0.32% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → MAZDOCK | -0.48% | -0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → MAZDOCK | -1.30% | -0.29% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_DEFENCE_PROCUREMENT → MAZDOCK | +1.00 | events | +6.00% |
| 1 | F_GOVT_CAPEX → MAZDOCK | +1.00 | events | +2.50% |
| 1 | C_MIDEAST_CONFLICT → MAZDOCK | +1.50 | events | +1.50% |
| 1 | F_FPI_FLOWS → MAZDOCK | -1.60 | events | -1.28% |
| 1 | F_REPO_IN → MAZDOCK | +1.00 | events | -1.20% |
| 1 | F_STEEL_INDIA → MAZDOCK | +1.65 | events | -0.99% |
| 1 | F_USDINR → MAZDOCK | -0.37 | observed | +0.37% |
| 2 | P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → MAZDOCK | +1.00 | events | +0.18% |

## Analyst profile (agent research, sourced)
# MAZDOCK — Mazagon Dock Shipbuilders Ltd. (profile as of 2026-11-05)

Sources: pack `market_impact/data/packs/MAZDOCK.md` (no headlines were available in the pack); web-search summaries of Kotak Neo, Univest, Arthneeti, Business Today, Maritime Gateway and Sahi. Several Q2 FY27 data points conflict between outlets and are flagged. Cost shares are estimates. No expected-return number is given.

## Business
Mazagon Dock (81.2% government-owned) is India's leading warship and submarine builder: Kolkata-class destroyers, Nilgiri-class (P17A) frigates, Scorpene/Kalvari submarines, refits and some offshore work. Almost all revenue comes from the Indian Navy under long, milestone-based contracts, so revenue is lumpy and depends on the order book and stage-of-completion accounting. FY26: sales Rs 13,006 cr, OPM 17%, profit Rs 2,578 cr.

## What moves the stock (ranked)
1. **Mega-order conversion (P75I, +6 per +10% orders):** the ~Rs 90,000 cr P75I submarine programme with a German partner and three further Kalvari-class boats are the whole growth story; management targets a Rs 1 lakh cr order book in FY27 and 15-17% revenue growth. Brokerages after Q1 said finalisation was imminent (Business Today, 2026-08-02), but no signing was found in retrieved sources, and Sahi lists administrative delay as a risk. A signing would be a company event worth +8% to +25%.
2. **Execution and provisions:** the Sep-2026 quarter showed sales -16.5% YoY, OP of Rs 199 cr (8% margin vs 24% a year earlier) and PAT -54% on "higher provisions" (Kotak Neo). Contingent liabilities are Rs 28,181 cr. Stage-of-completion timing and cost overrun provisions make quarterly numbers noisy.
3. **Competition (-5 per major program lost):** Cochin Shipyard, GRSE, L&T and private yards.
4. **Geopolitics (+3 India-Pakistan, +1 Middle East):** headline-driven.
5. **Macro:** repo -1.2, USD/INR -1.0 (imported systems), steel -0.6, govt capex +2.5.

## Transmission examples
- **Indo-Pacific tension (4th order):** China naval activity in the Indian Ocean -> Navy accelerates submarine and frigate procurement (2nd) -> MoD signs P75I/Kalvari follow-ons (3rd) -> MDL's order book jumps from ~Rs 16-27k cr to >Rs 1 lakh cr -> revenue visibility to FY35, equity re-rates; offsets: partner-technology dependence and cash-flow timing.
- **Steel up (3rd order):** China steel export cuts and Indian HRC +20% since June (global HRC +20.6%) -> plate and structural costs up -> fixed-price portions of Navy contracts absorb the hit -> provisions rise (as in Q2) -> OPM falls; price-variation clauses recover part with a 2-4 quarter lag.
- **Weaker rupee (2nd/3rd order):** INR slides (USD/INR 94.5, +6.5% in 12 months) -> imported equipment and partner payments cost more -> margin squeeze on fixed-rupee contracts -> but defence budgets are rupee-denominated, so recovery depends on escalation clauses.
- **Rate path (3rd order):** US yields up -> FPIs sell (FII holding just 1.7%, so limited) -> PSU defence flows are domestic-led -> small effect; main channel is valuation duration at P/E 30.

## Current situation
Stock Rs 1,846 (-31% in 12 months, -27% in 3 months, near the Rs 1,688 low). Q1 FY27 PAT Rs 550 cr (+22%) triggered brokerage upgrades up to 37% upside; Q2 reversed that, with the stock reportedly down 10% on the day. Promoter holding unchanged at 81.22%. One aggregator shows EBITDA margin 18.4% and an order book of Rs 16,443 cr at 30-Sep-2026, which contradicts the screener's 8% OPM (Rs 199 cr on Rs 2,446 cr) and the DSIJ headline of Rs 27,415 cr; treat the order book as unresolved.

## Upcoming events
Possible P75I and Kalvari signings (prob. ~25-30% within 3-4 months); interim dividend (Rs 5); Q3 FY27 results (Feb 2027); Q4 results and FY28 guidance (May 2027); government OFS risk (low).

## Bull case
P75I and Kalvari orders are signed within FY27, order book above Rs 1 lakh cr, H2 sales rebound, provisions reverse, and the stock recovers toward Rs 2,500.

## Bear case
P75I slips into FY28 or is renegotiated, order book stays at ~1.5x sales, more provisions on legacy contracts, growth turns negative and P/E (30) compresses toward 20-22.

## Uncertainties
Order book, margin and the cause of provisions are not reconciled. Confidence: low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.