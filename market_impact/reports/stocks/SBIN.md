# SBIN — State Bank of India
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months -1.8%** (rank 148 / 178 of 200 for 3m / 12m); beta 0.96
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.9%): 3 months 48%, 12 months 44%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.7% … P90 +3.8%; plausible 12m relative-return range incl. stock-specific noise: -30.3% … +24.1%
- Decomposition (12m): 0.5 × forward event exposure -3.3% (3m -0.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -5.6% (beta-adjusted) vs a realised market-adjusted move of +0.4% — gap -6.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.03 | -6.00 | +0.00 | -0.03 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.19 | +4.00 | +0.15 | -0.02 | +0.06 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.85 | +2.50 | +1.81 | -0.33 | -0.13 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.69 | +0.00 | +2.75 | +1.16 | -0.22 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.61 | -2.50 | -1.36 | +0.22 | +0.04 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.79 | -1.50 | -0.81 | -0.43 | -0.05 | +3.5% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.66 | +0.00 | +0.86 | +1.42 | +0.39 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.64 | +0.00 | +1.92 | +0.99 | -0.27 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.31 | +0.00 | -0.84 | -0.93 | -0.54 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.20 | -1.00 | -0.55 | -0.34 | -0.32 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.15 | -1.20 | -0.28 | -0.67 | +0.01 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -1.99 | -1.20 | -0.64 | -0.07 | -0.08 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.95 | +0.00 | -0.60 | -0.95 | -0.39 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.84 | +0.00 | +1.56 | +0.14 | +0.14 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -9.2% | -9.2% | -8.8 | -0.3 | +0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +11.1% | +5.6% | +10.6 | +0.4 | -0.0 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -1.1 | -1.8 | -0.5 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | -1.4 | -0.3 | -1.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.5 | -0.1 | -0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -10.2% | -2.5% | -3.8 | -5.9 | -0.6 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +2.2% | +2.2% | +2.0 | +0.2 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +1.2 | +0.9 | -0.1 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -9.9% | -1.8% | -9.2 | -0.6 | +0.0 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -1.9% | -1.7% | -1.9 | +0.1 | +0.0 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.5% | +1.7% | +0.0 | +1.0 | +1.2 | +0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.0% | +1.6% | +1.0 | +1.1 | +0.7 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SBIN | +10.00% | +5.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → SBIN | -6.00% | -1.08% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBIN | -3.84% | -0.96% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBIN | -3.84% | -0.96% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → SBIN | -3.75% | -0.94% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → SBIN | -0.90% | -0.81% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → SBIN | -1.20% | -0.72% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → SBIN | +2.00% | +0.70% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → SBIN | -0.75% | -0.68% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → SBIN | +0.80% | +0.64% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → SBIN | -1.20% | -0.60% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → SBIN | -3.75% | -0.56% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → SBIN | -1.87% | -0.47% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → SBIN | +0.67% | +0.45% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → SBIN | -3.75% | -0.45% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → SBIN | -1.60 | events | -6.40% |
| 1 | F_GSEC_10Y_IN → SBIN | +1.55 | director_override | -2.33% |
| 1 | F_CPI_IN → SBIN | +1.15 | events | -1.38% |
| 1 | F_GDP_IN → SBIN | +0.50 | events | +1.25% |
| 1 | F_REPO_IN → SBIN | +1.00 | events | +0.80% |
| 1 | F_LIQUIDITY_IN → SBIN | -0.90 | events | -0.72% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → SBIN | +0.50 | events | +0.48% |
| 1 | F_USDINR → SBIN | -0.37 | observed | +0.37% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → SBIN | -1.56 | events | -0.30% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → SBIN | -0.25 | events | -0.24% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → SBIN | +1.00 | events | -0.24% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → SBIN | +1.00 | events | -0.23% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Completion of 19.8% stake purchase in CareEdge Global IFSC | corporate_action | 0.60 | +0.1% | +0.09% |
| 2026-12 | Outcome of cybersecurity assessment / possible regulatory action after the ~3,900-record data breach (DPDP Act or RBI supervisory comment) | regulatory | 0.20 | -1.5% | -0.30% |
| 2027-02-07 | Q3 FY27 results (date approximate, SBI typically reports first/second week of Feb) | results | 0.90 | +0.5% | +0.45% |

## Analyst profile (agent research, sourced)
# SBIN - State Bank of India (as of 2026-11-05)

## Business
SBI is the system's anchor bank: roughly Rs45 lakh cr of loans (model estimate), CASA near 40%, a quarter of new credit, and subsidiaries in life insurance (SBI Life ~55%), cards (SBI Cards ~69%) and asset management. Government owns 55.45%. Q2 FY27 profit was Rs23,038cr (+14% YoY, screener). The stock trades at P/E 11.7 and P/B 1.5 with ROE 16%, and fell 5% on results day despite the beat (Investing.com, 2026-11-03) because of one-offs, margin worries and the October data breach.

## What moves the stock (ranked, % equity value per standard shock)
1. **Asset-quality cycle (-6.0 per +50bp credit cost)** - tail risk; starting GNPA 1.47%, NNPA 0.38% (Q1 FY27).
2. **FPI flows (+4.0 per +$5bn/qtr)** and **risk sentiment (-1.5 per +5 VIX)** - SBI is a heavy index weight, beta 0.9.
3. **Credit growth (+2.0)** and **GDP (+2.5)** - the 14-15% growth guidance depends on deposits keeping pace.
4. **Regulation (-2.5)** - RBI prudential tightening, plus cyber-supervision after the breach.
5. **Rates** - G-sec yield (-1.5, MTM), repo (+0.8, net of lagged deposit repricing), CPI (-1.2).
6. **Unsecured stress (-1.2)**, funding (+1.2), liquidity (+0.8).
Pack empirics: no factor has |t| >= 2; US 10y (-0.53, t -1.2) and global gas (-0.57, t -1.9) are the largest, both consistent with a rates/risk-appetite channel rather than fundamentals.

## Transmission examples
- **Middle East escalation -> Brent +10% -> USD/INR weaker and CPI +0.25pp -> RBI sustains 'calibrated tightening' (repo hiked to 5.50% on 2026-10-07) -> 10y G-sec +20bp -> SBI's AFS book loses ~Rs2.4k cr -> quarter PAT -2 to -3%; and slower credit demand -> volume growth below the 14-15% guidance.** Orders 1 to 4.
- **Repo hike -> EBLR loans (~40%) reprice immediately, term deposits lag -> NIM +4-6bp for 2-3 quarters -> PAT +2.5%; but 2nd order: bank FD rates rise -> CASA migrates to term deposits -> funding cost drifts up -> NIM gain fades within 3-4 quarters.**
- **Unsecured stress (card/personal loans) -> SBI Cards credit cost up -> SBI Cards PAT -> SBIN holding value (4% of mcap) and group sentiment; separately SBI's own personal-loan slippages.**
- **IRDAI commission caps (Sept 2026 draft) -> SBI Life volumes/margins fall -> SBILIFE price -> SBIN look-through value (10% of mcap) -> -0.1 per -1% SBILIFE.**

## Current situation
Q2 FY27 PAT Rs23,038cr (+14% YoY; +9% QoQ), revenue Rs1.32 lakh cr. Management retained credit-growth outlook near 15% (NewsDrum). Q1 FY27 domestic NIM was 3.00% with FY27 target ~3% (search summaries; Q2 deck not retrieved). Disclosed on 2026-10-21 that ~3,900 customer records were exposed and appointed a cybersecurity agency (Reuters). 2026-10-19: agreed to buy 19.8% of CareEdge Global IFSC. Brokers (Emkay Rs1,350) stay bullish.

## Upcoming events
RBI December review (~2026-12-04, prob 0.9), Union Budget (2027-02-01), Q3 results (~Feb 2027), possible regulatory outcome of the breach assessment (prob 0.2, 0 to -3%).

## Bull and bear
**Bull:** 11.7x earnings for a 16% ROE franchise with 1.5% GNPA, credit growth of 14-15%, NIM support from the hike, subsidiary value (SBI Life and SBI Cards stakes ~14% of mcap).
**Bear:** funding gap (deposits 10-11% vs credit 14-15%), rising yields hurting treasury, cyber/regulatory overhang, unsecured credit, and a stock that has lagged the Nifty (-7.8% in 3m) despite results.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.