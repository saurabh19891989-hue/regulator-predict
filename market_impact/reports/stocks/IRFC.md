# IRFC — Indian Railway Finance Corporation Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.5%**, **12 months +2.1%** (rank 86 / 68 of 200 for 3m / 12m); beta 1.40
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.9%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.6% … P90 +8.8%; plausible 12m relative-return range incl. stock-specific noise: -35.2% … +36.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.5 pp (model impact +3.0% beta-adjusted vs realised market-adjusted move -23.1%); forward event exposure +4.4% (3m +1.7%; half assumed priced); company-specific events -0.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.74 | +0.00 | -0.96 | -0.74 | -0.04 | — |
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +1.56 | +1.50 | +0.06 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.37 | -0.50 | -0.32 | -0.40 | -0.15 | -1.1% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.12 | +1.20 | +0.00 | -0.02 | -0.06 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.11 | +0.00 | -0.19 | -0.39 | -0.53 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.08 | -1.00 | -0.08 | +0.00 | +0.00 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.99 | +0.80 | +0.09 | +0.04 | +0.06 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.97 | +0.00 | -0.25 | -0.34 | -0.37 | +0.0% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.95 | -0.60 | -0.18 | -0.13 | -0.04 | +3.5% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.93 | +0.00 | +0.00 | -0.53 | -0.40 | — |
| India FX reserves (RBI intervention) (`NEW_FX_RESERVES_IN`) | +US$25bn reserves (RBI buys / net inflows) | +0.92 | +0.00 | +0.51 | +0.34 | +0.06 | — |
| US dollar index (`F_DXY`) | +3% DXY | -0.89 | +0.00 | -0.47 | -0.22 | -0.20 | +2.2% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.89 | +0.00 | -0.78 | -0.10 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.5% | -5.5% | +0.0 | -1.5 | -1.9 | -2.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.4% | -2.4% | -2.0 | -0.2 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.1 | -0.8 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.1% | +1.9% | +2.2 | +0.0 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.8% | -1.8% | -1.8 | +0.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.7% | +1.4% | +2.2 | +0.2 | +0.1 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.1 | -0.2 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.7% | -1.3% | -0.7 | -0.9 | -1.0 | -1.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.5% | -1.2% | -2.4 | -1.5 | -0.4 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.0 | -0.1 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.0% | +1.2% | +0.3 | +0.5 | +0.6 | +0.6 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -5.4% | -1.0% | -3.0 | -1.9 | -0.4 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → IRFC | +1.20% | +1.08% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IRFC | +2.00% | +1.00% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → IRFC | +0.96% | +0.86% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IRFC | -2.40% | -0.67% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → IRFC | -3.00% | -0.54% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IRFC | -0.80% | -0.40% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → IRFC | -0.60% | -0.36% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → IRFC | +0.72% | +0.32% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → IRFC | -0.50% | -0.30% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → IRFC | -1.20% | -0.26% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → IRFC | -0.72% | -0.26% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → IRFC | -0.24% | -0.23% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → IRFC | -1.00% | -0.22% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → IRFC | -0.86% | -0.22% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → IRFC | -0.77% | -0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → IRFC | +1.70 | events | -1.70% |
| 1 | F_FPI_FLOWS → IRFC | -1.60 | events | -1.28% |
| 1 | F_GOVT_CAPEX → IRFC | +1.00 | events | +1.20% |
| 1 | F_REPO_IN → IRFC | +1.00 | events | -0.40% |
| 1 | F_CREDIT_SPREADS_IN → IRFC | +0.50 | events | -0.40% |
| 1 | F_LIQUIDITY_IN → IRFC | -0.90 | events | -0.36% |
| 1 | F_USDINR → IRFC | -0.37 | observed | +0.18% |
| 1 | F_RISK_SENTIMENT → IRFC | +0.11 | observed | -0.07% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → IRFC | +0.30 | events | +0.04% |
| 4 | P_SEBI_DERIVATIVES → F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → F_DOMESTIC_FLOWS → IRFC | -0.10 | events | -0.00% |

## Analyst profile (agent research, sourced)
# Indian Railway Finance Corporation (IRFC) - Market Impact profile, as of 2026-11-05

## Business
IRFC is the dedicated funding arm of Indian Railways. It borrows in rupees and foreign currency (bonds, term loans, ECBs) and leases assets (locomotives, wagons, coaches and infrastructure) to the Ministry of Railways under finance leases priced at IRFC's cost of borrowing plus a thin spread of roughly 0.40%. This cost-plus structure means earnings are predictable (zero NPA), interest-rate moves pass through, and credit risk is effectively sovereign. Q2 FY27: PAT Rs1,958cr (+10.2% y/y), revenue +23.5% on higher lease income, finance costs Rs5,917cr. Management targets Rs35,000cr of disbursements and a borrowing programme up to Rs70,000cr in FY27 (Rs24-28k cr ECB), is diversifying into non-railway loans (HURL refinancing of Rs12,800cr), and aims to cross a Rs1 lakh cr loan book. The government holds 82.9% after a Q1 FY27 OFS. Screener ratios were blank in the evidence pack, so valuation figures here are derived and flagged.

## What moves the stock, ranked
IRFC's earnings are almost insensitive to commodities; the stock trades on policy, supply and bond-proxy factors.
1. **Railway capex mix (+1.5 per +10%)** and **govt capex (+1.2)**: funding volume through IRFC; the Budget's EBR vs budgetary-support split is the key swing factor.
2. **G-sec yield (-1.0 per +25bp)**: valuation, not earnings.
3. **Domestic flows (+1.0)**, **FPI (+0.8)**, **VIX (-0.6)**, **credit spreads (-0.8)**, **infra spending (+0.6)**, **FX (-0.5)**, **repo (-0.4)**, **liquidity (+0.4)**.
Empirical check: no factor in the pack reaches |t|>=2; the strongest are gas (-0.89, t -1.4) and US equities (+1.67, t 1.3), consistent with a high-beta (1.5-1.6) PSU stock with no fundamental commodity link. We therefore deliberately do not create commodity edges.

## Transmission examples
- **Middle East escalation -> Brent up -> CPI up -> RBI hikes again -> G-sec yield up -> IRFC's new borrowing costs more -> the cost is passed through in the lease rate (earnings unchanged) -> but the stock as a bond-proxy de-rates; and the Railways' fiscal space tightens.**
- **Brent up -> INR weaker -> hedging cost on ECBs (35-40% of FY27 borrowing) up -> fully passed through in lease rate, small residual -> FPI outflows mark the PSU basket down.**
- **Budget increases extra-budgetary resource (EBR) share -> Railways borrows more through IRFC -> lease asset base and PAT grow -> the stock re-rates** (a positive 3rd-order chain; opposite for budgetary support).
- **Government OFS (promoter 82.9% vs 75% minimum public shareholding norm) -> supply overhang -> price pressure irrespective of fundamentals.**

## Current situation
Stock Rs80, near 52-week lows (30 Oct), -34% over 12m. The sell-off reflects slowing growth (~10% PAT), weaker EBR outlook, OFS supply and rising yields; Q2 was fine but could not change the narrative. Interim dividend Rs1.15 declared (record date 23 Oct).

## Upcoming
Q3 results (Jan 2027), Union Budget (1 Feb 2027, probability 0.95), borrowing/ECB issuance, RBI MPC (Dec), possible OFS (0.3).

## Bull and bear
**Bull:** sovereign-quality earnings, AAA funding, no tax, dividends, loan-book diversification, Budget could restore EBR share. **Bear:** policy-set spread, shrinking EBR role, OFS overhang, yields rising, limited earnings growth.

## Sizing notes and caveats
Why equity sensitivities are small: with a cost-plus lease, a +100bp move in borrowing cost raises both finance cost and lease income by the same amount, leaving the ~0.40% spread unchanged (about Rs1,900cr a year on an asset base near Rs4.7 lakh cr, model estimate); the bulk of PAT (~Rs7,700cr annualised) comes from the return on net-worth-funded assets, which does move with the level of rates. The edges therefore describe valuation, volume and policy rather than margin. Note that PAT growth of ~10% against revenue growth of ~23% shows the spread is being diluted by faster growth in costs, an important point to watch.

Data gaps: the screener dossier was empty (no price-to-book, dividend yield, or debt figures), the interim dividend is reported as Rs1.05 by one source and Rs1.15 by most others, and EPS differs between sources; the Director should treat valuation outputs as low-confidence. The 'fair value' downside calls from Investing.com are automated models and are not used. Overall confidence for this profile is low because earnings are policy-determined and the stock's moves have been largely supply- and sentiment-driven.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.