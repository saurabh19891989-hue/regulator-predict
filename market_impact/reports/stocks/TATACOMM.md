# TATACOMM — Tata Communications Ltd.
*MIDCAP_100 · Telecommunication · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months +0.0%** (rank 130 / 98 of 200 for 3m / 12m); beta 1.05
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.8%): 3 months 50%, 12 months 47%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.4% … P90 +3.3%; plausible 12m relative-return range incl. stock-specific noise: -38.0% … +35.0%
- Decomposition (12m): 0.5 × forward event exposure -2.0% (3m -0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.3%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -6.0% (beta-adjusted) vs a realised market-adjusted move of -15.0% — gap +9.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.08 | +0.08 | -0.04 |
| Sector | -1.00 | +0.46 | -0.54 | -0.05 |
| Theme | +0.00 | +0.08 | +0.08 | +0.05 |
| Geopolitics | -0.00 | +0.01 | +0.01 | -0.00 |
| Company catalysts | +1.14 | +0.00 | +1.14 | +0.24 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.60 | -0.27 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.01** | **-0.17** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Enterprise connectivity pricing pressure (`NEW_ENTERPRISE_CONNECTIVITY_PRICING`) | +1 = 5% decline in MPLS/SD-WAN/IZO prices | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +3.11 | +2.50 | +0.42 | +0.16 | +0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.04 | +2.00 | +0.01 | -0.00 | +0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.02 | -2.00 | +0.00 | -0.01 | -0.01 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.01 | +2.00 | +0.00 | +0.00 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.51 | -1.00 | -0.45 | -0.03 | -0.02 | — |
| US/EU enterprise IT services spend (`F_US_TECH_SPEND`) | +5% growth | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.42 | +0.00 | +0.61 | +0.56 | +0.25 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.40 | +1.50 | +0.15 | -0.17 | -0.09 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.33 | +0.00 | -0.90 | -0.49 | +0.06 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.21 | +0.00 | -0.40 | -0.44 | -0.37 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.07 | +0.00 | -0.80 | -0.21 | -0.07 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.05 | -0.50 | -0.33 | -0.19 | -0.03 | +3.5% |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.97 | +0.00 | +0.96 | +0.11 | -0.10 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.5% | -4.5% | -4.4 | -0.0 | +0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -13.2% | -3.3% | -8.8 | -4.0 | -0.5 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.8 | +0.0 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.3% | +2.6% | +5.2 | -0.0 | -0.0 | +0.1 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.8% | -1.8% | -1.6 | -0.0 | -0.1 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.0 | -0.6 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -0.9 | -0.3 | -0.3 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -0.9 | -0.5 | -0.1 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.0 | -0.1 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.1% | +1.1% | +1.0 | +0.1 | -0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.2 | +0.1 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACOMM | +5.00% | +2.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → TATACOMM | -7.50% | -1.88% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → TATACOMM | -2.10% | -0.84% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATACOMM | -1.60% | -0.80% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TATACOMM | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TATACOMM | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → TATACOMM | -1.92% | -0.48% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_AI_CAPEX → TATACOMM | +0.75% | +0.46% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_TECH_SPEND → TATACOMM | -1.71% | -0.43% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ F_AI_CAPEX → TATACOMM | +0.50% | +0.42% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACOMM | -1.00% | -0.42% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → TATACOMM | -0.40% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → TATACOMM | -0.60% | -0.36% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → TATACOMM | -0.60% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → TATACOMM | -2.00% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → TATACOMM | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → TATACOMM | +1.55 | director_override | -3.10% |
| 1 | F_POWER_PRICE_IN → TATACOMM | +1.90 | director_override | -1.33% |
| 1 | F_REPO_IN → TATACOMM | +1.00 | events | -1.00% |
| 1 | F_US_TECH_SPEND → TATACOMM | -0.60 | events | -0.90% |
| 1 | F_AI_CAPEX → TATACOMM | -0.30 | events | -0.75% |
| 1 | F_GDP_IN → TATACOMM | +0.50 | events | +0.75% |
| 1 | C_RED_SEA → TATACOMM | +1.00 | events | -0.50% |
| 1 | F_USDINR → TATACOMM | -0.37 | observed | -0.30% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → TATACOMM | +0.50 | director_override | +0.16% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → TATACOMM | -0.30 | events | -0.07% |
| 1 | F_RISK_SENTIMENT → TATACOMM | +0.11 | observed | -0.06% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Dividend/AGM-related corporate actions (dividend yield 1.0%) | corporate_action | 0.30 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (digital EBITDA break-even target; double-digit EBITDA growth guided for FY27) | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | AI Super Highway construction start (Q4 FY27 subject to vendor selection / approvals) | capex | 0.60 | +0.5% | +0.30% |
| 2027-03 | Digital portfolio EBITDA break-even announcement | guidance | 0.30 | +5.0% | +1.50% |

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