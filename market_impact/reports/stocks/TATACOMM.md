# TATACOMM — Tata Communications Ltd.
*MIDCAP_100 · Telecommunication · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.2%**, **12 months -1.6%** (rank 135 / 125 of 200 for 3m / 12m); beta 1.05
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.8%): 3 months 47%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.4% … P90 +2.6%; plausible 12m relative-return range incl. stock-specific noise: -49.3% … +24.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -7.0% beta-adjusted vs realised market-adjusted move -15.0%); forward event exposure -3.1% (3m -1.4%; half assumed priced); company-specific events +2.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Enterprise connectivity pricing pressure (`NEW_ENTERPRISE_CONNECTIVITY_PRICING`) | +1 = 5% decline in MPLS/SD-WAN/IZO prices | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +3.17 | +2.50 | +0.42 | +0.19 | +0.06 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.85 | +0.00 | -1.47 | -1.29 | -0.09 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.07 | +2.00 | +0.01 | -0.00 | +0.07 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.04 | -2.00 | +0.00 | -0.03 | -0.01 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.00 | +2.00 | +0.00 | +0.00 | -0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.60 | +0.00 | -0.40 | -0.44 | -0.76 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.59 | +0.00 | +0.00 | -0.88 | -0.71 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.51 | -1.00 | -0.45 | -0.03 | -0.02 | — |
| US/EU enterprise IT services spend (`F_US_TECH_SPEND`) | +5% growth | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.34 | +0.00 | +0.61 | +0.50 | +0.22 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.27 | +0.00 | +0.88 | +0.36 | +0.04 | +1.2% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.08 | +0.00 | -0.80 | -0.21 | -0.08 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.07 | -0.50 | -0.33 | -0.20 | -0.05 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.4% | -6.4% | -0.5 | -1.1 | -2.5 | -2.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.8% | -4.8% | -4.6 | +0.0 | +0.0 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -14.6% | -4.1% | -9.5 | -4.5 | -0.6 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -1.7 | -1.6 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.8 | +0.0 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.4% | +2.7% | +5.2 | -0.0 | -0.0 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -2.1 | +0.0 | -0.1 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.9 | +0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.8% | -1.8% | -1.6 | -0.0 | -0.1 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.1 | -0.3 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.3% | -1.5% | -0.6 | -1.2 | -1.3 | -1.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → TATACOMM | -4.40% | -4.40% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → TATACOMM | -2.80% | -2.80% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACOMM | +5.00% | +2.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → TATACOMM | -7.50% | -2.10% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_PRICE_IN → TATACOMM | -2.10% | -2.10% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → TATACOMM | -1.32% | -1.32% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → TATACOMM | +1.25% | +1.25% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → TATACOMM | -1.19% | -1.19% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → TATACOMM | -1.05% | -1.05% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → TATACOMM | +1.00% | +1.00% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → TATACOMM | -1.00% | -1.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → TATACOMM | -0.94% | -0.94% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → TATACOMM | -0.89% | -0.89% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → TATACOMM | -0.89% | -0.89% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → TATACOMM | -0.88% | -0.88% |

## Analyst profile (agent research, sourced)
# TATACOMM — Tata Communications Ltd. (Midcap 100) — profile as of 2026-11-05

## Business
Global enterprise network and digital-infrastructure provider (ex-VSNL; 58.85% Tata group). Core connectivity (MPLS, SD-WAN, internet, subsea/IZO), media and entertainment, plus a digital portfolio (cloud, CPaaS, IoT, security, collaboration) with 300 of the Fortune 500 as customers. TTM revenue ~Rs26.0k cr; Q2 FY27 (company, 2026-10-15): revenue Rs6,688 cr (+9.6%), EBITDA Rs1,422 cr (margin 21.3% vs 19.2%), PAT Rs341 cr (+86%), digital platform revenue +18.6%, data +12.2%, digital margin -3.6% (losses halved). Net debt/EBITDA ~2.2x (MOFSL note via search). Fundamentals fetched directly from screener.in because the evidence pack had no dossier.

## What moves the stock (ranked)
1. **Enterprise connectivity pricing (-5 per 5% price cut)**: core connectivity is the cash engine; Airtel Business, Jio and hyperscaler networks compress prices.
2. **AI/data-centre demand (+2.5 per AI capex +10%; +2.0 data-centre theme)**: the $450m AI Super Highway (3-5 years, targets up to 40% of AI network demand; construction from Q4 FY27 subject to approvals) is a major bet.
3. **Discount rate (-2.0 per +25bp 10y) and funding (-1.0 per +25bp repo)** with a P/E of 41.
4. **Macro demand (GDP +1.5, US tech spend +1.5)** and **rupee (+0.8)**.

## Transmission examples
- AI capex boom -> hyperscaler/data-centre builds in India (theme) -> demand for long-haul fibre and interconnect (1st) -> Tata Comm order book grows double digits (2nd) -> operating leverage lifts EBITDA margin beyond 21-22% (3rd) -> FCF funds the $450m network and lowers net debt/EBITDA below 2x (4th).
- Middle East escalation -> Brent up -> INR weaker (+0.8 for Tata Comm's net USD revenue) -> RBI holds -> G-sec yield up (-2.0) -> valuation de-rates; Red Sea cable cuts raise restoration costs but boost demand for diverse routes.
- US tech spend slowdown -> MNC enterprise IT budgets shrink -> collaboration and security digital revenue slows (growth +18.6% is the key to break-even) -> digital losses persist.
- GenAI-driven traffic and sovereign-cloud mandates may add demand but also invite hyperscaler-owned networks (substitution risk, captured in connectivity pricing).

## Current situation and upcoming
Stock ~Rs1,746 (52w Rs1,322-2,110), +10-14% from lows after Q2, -8.4% 12m; Motilal Neutral Rs1,980. FIIs 13.55%, DIIs 20.2%. Upcoming: Q3 FY27 results (Jan 2027), AI Super Highway vendor selection and construction start (Q4 FY27), digital EBITDA break-even (management: at the earliest).

## Bull and bear
Bull: AI interconnect wins, digital break-even, EBITDA growth >15% (management targets double-digit FY27), stable pricing. Bear: connectivity price erosion, cost overruns on AI capex (cash capex +60% y/y), digital losses persist, valuation (41x P/E).

## Gaps
Revenue mix, cost shares and net debt are approximate; a different aggregator showed contradictory EBITDA (Rs743 cr) and was rejected in favour of the company press release; the call transcript was not read.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.