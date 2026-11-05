# IREDA — Indian Renewable Energy Development Agency Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.3%**, **12 months -5.8%** (rank 138 / 169 of 200 for 3m / 12m); beta 1.62
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.3%): 3 months 45%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -19.7% … P90 +4.0%; plausible 12m relative-return range incl. stock-specific noise: -42.6% … +23.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +6.0 pp (model impact +12.0% beta-adjusted vs realised market-adjusted move -20.9%); forward event exposure -20.6% (3m -8.4%; half assumed priced); company-specific events -0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +9.56 | +8.00 | +1.56 | +0.00 | +0.00 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -8.35 | -8.00 | -0.36 | +0.00 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -6.88 | +0.00 | -3.76 | -3.05 | -0.07 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +6.05 | +6.00 | +0.00 | +0.00 | +0.05 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -5.87 | -5.00 | -0.42 | -0.30 | -0.15 | +3.5% |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.46 | -3.00 | -1.69 | +0.06 | +0.17 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.06 | +0.00 | -1.60 | -0.81 | -1.66 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.94 | +0.00 | +0.00 | -2.17 | -1.78 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -3.90 | +0.00 | -2.00 | -1.17 | -0.73 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.78 | +0.00 | +3.04 | +0.59 | +0.15 | +1.2% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.45 | -2.50 | -1.04 | +0.06 | +0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.31 | -3.00 | -0.30 | +0.00 | -0.01 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.95 | -3.00 | +0.00 | +0.04 | +0.01 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.91 | +0.00 | +2.48 | +0.24 | +0.19 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -15.1% | -15.1% | +0.0 | -4.8 | -5.9 | -4.4 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +11.0% | +11.0% | +11.0 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -8.1% | -8.1% | +0.0 | -4.3 | -3.6 | -0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.3% | -7.3% | -6.4 | -0.4 | -0.1 | -0.3 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -25.0% | -7.0% | -20.0 | -3.6 | -1.1 | -0.3 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -30.8% | -5.5% | -25.0 | -4.5 | -0.8 | -0.5 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.0% | -5.0% | -5.1 | +0.0 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +4.8% | +4.8% | +4.0 | +0.8 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -13.4% | -4.8% | -6.0 | -1.7 | -3.2 | -2.5 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -7.1% | -4.4% | -7.0 | -0.4 | +0.2 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -4.3% | -4.3% | -4.0 | -0.3 | +0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.0% | +4.0% | +7.0 | +0.5 | +0.2 | +0.4 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → IREDA | +8.00% | +8.00% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IREDA | -20.00% | -5.60% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → IREDA | -25.00% | -4.50% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → IREDA | -4.40% | -4.40% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → IREDA | -4.20% | -4.20% |
| 1 | EV_SOLAR_ALMM2_CELL_MANDATE ⇒ P_RENEWABLE_SUPPORT → IREDA | +4.00% | +4.00% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → IREDA | -3.31% | -3.31% |
| 1 | EV_BESS_VGF_NOV26 ⇒ T_ENERGY_TRANSITION → IREDA | +3.00% | +3.00% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_DEMAND_IN → IREDA | +2.50% | +2.50% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → IREDA | -2.50% | -2.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IREDA | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → IREDA | -4.00% | -2.48% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → IREDA | -2.40% | -2.40% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → IREDA | -2.21% | -2.21% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → IREDA | -6.00% | -2.14% |

## Analyst profile (agent research, sourced)
# IREDA - Indian Renewable Energy Development Agency Ltd. (as of 2026-11-05)

## Business
IREDA is a government-owned (71.76%) non-bank lender to renewable energy developers: solar, wind, hydro, biomass, energy efficiency and storage. It is a Miniratna-category PSU under the Ministry of New and Renewable Energy and is registered with the RBI as a non-deposit NBFC. Revenue was Rs8,339cr in FY26 (+23%), and TTM profit is Rs1,968cr. The loan book is roughly Rs90k cr (derived from revenue/yield, not disclosed in the pack). Funding comes from taxable and tax-free bonds, bank loans and foreign lines, so net interest margin (about 3%) is highly sensitive to the cost of borrowing, while loan yields reset slowly.

## What moves the stock (ranked)
1. **Renewable-energy policy and transition momentum (+8.0 per support step, +6.0 theme)**: structural loan growth.
2. **Credit cost (-8.0 per +50bp)**: a project-finance lender to developers with construction and PPA risk.
3. **Funding cost: G-sec -3.0, credit spreads -3.0, repo -2.5**: liability-sensitive in a rising-rate cycle (the RBI hiked on 2026-10-07).
4. **Risk sentiment and beta (-5.0, flows +2.0)**: beta ~1.9, so market drawdowns hit hard.
5. **Prudential rules (-3.0)** on project finance and NBFCs.
6. **Power demand (+2.5)**, **power reform (+2.5)**, **INR (-0.8)**.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker -> RBI hikes again -> G-sec +30bp**: IREDA's marginal borrowing cost +10-12bp on 40% reprice -> NIM -5bp -> PAT -3%; 3rd order: AAA PSU spreads widen as the government borrows/RBI drains liquidity (-1.5 to -3); 4th order: higher funding costs raise developer hurdle rates, slowing RE tenders (loan growth -2pp) and raising stress at leveraged developers.
- **Government extends ISTS waiver/storage support -> RE auctions rise -> IREDA sanctions +20%** -> loan growth +3pp -> PAT +6% in 18 months (+4 to +8).
- **Solar module price fall -> project capex per MW down -> loan ticket per MW smaller** (volume ~ neutral), but IRRs rise and PPA signing accelerates.
- **Developer default (PPA delays, curtailment)** -> stage-3 up 1pp -> credit cost +20bp -> PAT -7%.

## Current situation
Q2 FY27 PAT Rs552cr (+0.5% YoY) is flat because borrowing costs rose faster than loan yields (interest expense up from Rs1,213cr to Rs1,377cr), although operating profit rose 17% and bad loans eased. Stock Rs109, off 28% in 12 months and well below the 52-week high Rs153. Promoters unchanged at 71.76%; FIIs 2.57%.

## Upcoming
Q3 FY27 results mid/late January 2027; Union Budget Feb 2027 (RE allocations); potential equity raise; RBI MPC December; auction pipeline and PPA signings.

## Bull case
Policy support, slower rate rises and steady asset quality - profit growth 15-20% with stable margin and re-rating toward 2.6x book (+25%).
## Bear case
Funding costs rise, credit stress emerges, equity raise dilutes: ROE slips below 13% and the stock falls another 20%.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.