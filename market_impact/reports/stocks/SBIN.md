# SBIN — State Bank of India
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.8%**, **12 months -6.5%** (rank 170 / 174 of 200 for 3m / 12m); beta 0.96
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.9%): 3 months 39%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -17.2% … P90 -0.6%; plausible 12m relative-return range incl. stock-specific noise: -32.3% … +20.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.9 pp (model impact -5.7% beta-adjusted vs realised market-adjusted move +0.4%); forward event exposure -5.2% (3m -0.9%; half assumed priced); company-specific events +0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.03 | -6.00 | +0.00 | -0.03 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.58 | +0.00 | +2.75 | +2.53 | -0.70 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.29 | +0.00 | -0.84 | -1.96 | -1.48 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.28 | +4.00 | +0.15 | +0.04 | +0.08 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.84 | +2.50 | +1.96 | -0.54 | -0.08 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.61 | -2.50 | -1.36 | +0.22 | +0.04 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.36 | +0.00 | +0.86 | +2.04 | +0.46 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.31 | +0.00 | +1.92 | +2.16 | -0.78 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.07 | +0.00 | +2.00 | +0.85 | +0.21 | +1.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.89 | -1.50 | -0.81 | -0.49 | -0.09 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -2.78 | +0.00 | -2.00 | -0.50 | -0.28 | +2.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.76 | -1.00 | -0.87 | -0.47 | -0.42 | -1.1% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.76 | +0.00 | -0.60 | -1.26 | -0.90 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.47 | +0.00 | +0.90 | +1.61 | -0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.6% | -10.6% | -1.5 | -3.9 | -3.2 | -1.9 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -10.1% | -10.1% | -9.4 | -0.4 | -0.1 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +11.3% | +5.7% | +10.6 | +0.4 | +0.1 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.2% | -4.2% | +0.0 | -1.1 | -2.6 | -0.6 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -14.3% | -4.0% | -6.0 | -7.1 | -1.2 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -6.3% | -3.9% | -6.5 | +0.3 | +0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.9% | -3.9% | +0.0 | -3.5 | -0.2 | -0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -3.1 | -0.2 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | -1.4 | -0.1 | -1.5 | -0.2 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -17.1% | -3.1% | -7.5 | -8.8 | -0.6 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.5 | -0.1 | -0.1 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -8.0% | -2.8% | -2.5 | -2.6 | -1.8 | -1.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SBIN | +10.00% | +5.00% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → SBIN | -3.00% | -1.86% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → SBIN | -6.00% | -1.68% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → SBIN | -2.50% | -1.55% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → SBIN | -7.50% | -1.35% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → SBIN | -6.00% | -1.32% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBIN | -3.84% | -1.08% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBIN | -3.84% | -0.96% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → SBIN | -2.99% | -0.84% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → SBIN | -2.50% | -0.75% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → SBIN | -1.20% | -0.72% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → SBIN | +2.00% | +0.70% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → SBIN | -3.73% | -0.67% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → SBIN | +0.72% | +0.65% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → SBIN | -1.80% | -0.64% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → SBIN | -1.60 | events | -6.40% |
| 1 | F_GSEC_10Y_IN → SBIN | +1.70 | events | -2.55% |
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