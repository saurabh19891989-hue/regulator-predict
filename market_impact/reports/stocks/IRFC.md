# IRFC — Indian Railway Finance Corporation Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.7%**, **12 months -0.7%** (rank 166 / 140 of 200 for 3m / 12m); beta 1.40
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.9%): 3 months 48%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.0% … P90 +2.2%; plausible 12m relative-return range incl. stock-specific noise: -33.4% … +32.9%
- Decomposition (12m): 0.5 × forward event exposure +0.1% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.8% (beta-adjusted) vs a realised market-adjusted move of -23.1% — gap +24.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +1.52 | +1.50 | +0.02 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.08 | -1.00 | -0.08 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.05 | -0.50 | -0.16 | -0.28 | -0.11 | -1.1% |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.98 | +0.00 | -0.73 | -0.22 | -0.03 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.94 | +0.80 | +0.09 | +0.01 | +0.04 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.91 | -0.60 | -0.18 | -0.11 | -0.02 | +3.5% |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -0.79 | -0.80 | +0.00 | +0.01 | -0.01 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +0.79 | +0.00 | +0.80 | -0.02 | +0.01 | — |
| India FX reserves (RBI intervention) (`NEW_FX_RESERVES_IN`) | +US$25bn reserves (RBI buys / net inflows) | +0.68 | +0.00 | +0.51 | +0.15 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.67 | +0.00 | -0.19 | -0.28 | -0.20 | — |
| Road/highway awarding (`P_INFRA_SPENDING_ROADS`) | +10% | +0.62 | +0.60 | +0.02 | +0.00 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.59 | +0.00 | -0.52 | -0.07 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.58 | -0.40 | -0.22 | +0.02 | +0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.1% | -2.1% | -1.8 | -0.2 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.8% | -1.8% | -1.8 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.6% | +1.3% | +2.2 | +0.2 | +0.0 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.8 | -0.2 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.9 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.9% | -0.7% | -1.5 | -1.2 | -0.2 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.1% | -0.7% | -3.9 | -0.2 | -0.0 | +0.0 |
| Banking system liquidity turns to sustained deficit by end-March 2027 (`EV_BANKING_LIQUIDITY_DEFICIT_MAR27`) | anticipated | 0.60 | -1.1% | -0.7% | -1.1 | +0.0 | +0.0 | -0.0 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -1.2% | -0.6% | -1.2 | -0.0 | -0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.5 | -0.1 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.6 | +0.0 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.5% | +0.5% | +0.4 | +0.1 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IRFC | +2.00% | +1.00% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IRFC | -0.80% | -0.40% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IRFC | -1.50% | -0.38% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → IRFC | -0.60% | -0.36% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → IRFC | +0.30% | +0.27% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → IRFC | -1.50% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → IRFC | -1.20% | -0.22% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → IRFC | -0.77% | -0.19% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → IRFC | -0.77% | -0.19% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → IRFC | -0.20% | -0.18% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → IRFC | -0.30% | -0.18% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → IRFC | -0.30% | -0.18% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → IRFC | -1.00% | -0.18% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → IRFC | -0.40% | -0.17% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → IRFC | +0.30% | +0.16% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → IRFC | +1.55 | director_override | -1.55% |
| 1 | F_FPI_FLOWS → IRFC | -1.60 | events | -1.28% |
| 1 | F_REPO_IN → IRFC | +1.00 | events | -0.40% |
| 1 | F_CREDIT_SPREADS_IN → IRFC | +0.50 | events | -0.40% |
| 1 | F_LIQUIDITY_IN → IRFC | -0.90 | events | -0.36% |
| 1 | F_USDINR → IRFC | -0.37 | observed | +0.18% |
| 1 | F_GOVT_CAPEX → IRFC | +0.20 | director_override | +0.07% |
| 1 | F_RISK_SENTIMENT → IRFC | +0.11 | observed | -0.07% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → IRFC | +0.30 | events | +0.04% |
| 3 | F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → F_DOMESTIC_FLOWS → IRFC | +0.20 | events | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11/12 | ECB / bond issuance under Rs70,000cr programme and FY27 disbursement trajectory (target Rs35,000cr) | capex | 0.80 | +0.5% | +0.40% |
| 2027 | Possible further government stake sale (OFS) given 82.9% holding vs 75% MPS norm | corporate_action | 0.30 | -4.5% | -1.35% |
| 2027-01 | Q3 FY27 results (Q2 on 2026-10-15) | results | 0.95 | +0.0% | +0.00% |

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