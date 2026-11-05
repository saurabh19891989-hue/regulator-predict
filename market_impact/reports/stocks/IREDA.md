# IREDA — Indian Renewable Energy Development Agency Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.5%**, **12 months -5.4%** (rank 190 / 195 of 200 for 3m / 12m); beta 1.62
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.3%): 3 months 41%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -11.7% … P90 -0.1%; plausible 12m relative-return range incl. stock-specific noise: -31.8% … +21.5%
- Decomposition (12m): 0.5 × forward event exposure -9.1% (3m -4.5%; half assumed priced) + 0.5 × company-specific catalysts -0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +4.2% (beta-adjusted) vs a realised market-adjusted move of -20.9% — gap +25.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +9.56 | +8.00 | +1.56 | +0.00 | +0.00 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -8.35 | -8.00 | -0.36 | +0.00 | +0.01 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +6.05 | +6.00 | +0.00 | +0.00 | +0.05 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -5.79 | -5.00 | -0.42 | -0.28 | -0.09 | +3.5% |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.46 | -3.00 | -1.69 | +0.06 | +0.17 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.48 | +0.00 | -2.32 | -1.20 | +0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.47 | -2.50 | -1.04 | +0.06 | +0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.30 | -3.00 | -0.30 | +0.00 | +0.00 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -3.26 | +0.00 | -2.00 | -1.01 | -0.25 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.07 | +0.00 | -1.60 | -0.58 | -0.88 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.95 | -3.00 | +0.00 | +0.04 | +0.01 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.69 | +0.00 | +2.48 | +0.10 | +0.11 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +11.0% | +11.0% | +11.0 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.1% | -5.1% | -4.4 | -0.4 | -0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.0% | -5.0% | -5.1 | +0.0 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +4.8% | +4.8% | +4.0 | +0.8 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -4.3% | -4.3% | -4.0 | -0.3 | +0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.2% | -4.2% | +0.0 | -2.7 | -1.5 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -16.1% | -4.0% | -12.5 | -3.0 | -0.6 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.8% | +3.9% | +7.0 | +0.5 | +0.2 | +0.2 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.0 | +0.0 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -16.4% | -2.5% | -12.5 | -3.5 | -0.3 | -0.2 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -4.4% | -2.2% | -4.3 | -0.1 | -0.0 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -1.8 | -0.4 | -0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IREDA | -12.50% | -3.12% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IREDA | +5.00% | +2.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → IREDA | -12.50% | -1.88% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → IREDA | +3.75% | +1.50% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → IREDA | -5.00% | -1.25% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → IREDA | +2.00% | +1.24% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IREDA | -2.40% | -1.20% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → IREDA | +2.50% | +1.12% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → IREDA | +2.00% | +1.10% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → IREDA | -1.20% | -1.08% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → IREDA | +1.80% | +1.08% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → IREDA | -2.50% | -1.05% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → IREDA | +2.00% | +1.00% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → IREDA | -1.43% | -0.97% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → IREDA | -3.60% | -0.90% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_RENEWABLE_SUPPORT → IREDA | +0.60 | director_override | +4.80% |
| 1 | F_GSEC_10Y_IN → IREDA | +1.55 | director_override | -4.65% |
| 1 | F_FPI_FLOWS → IREDA | -1.60 | events | -3.20% |
| 1 | F_POWER_DEMAND_IN → IREDA | +1.20 | events | +3.00% |
| 1 | F_REPO_IN → IREDA | +1.00 | events | -2.50% |
| 1 | T_ENERGY_TRANSITION → IREDA | +0.30 | director_override | +1.80% |
| 1 | F_CREDIT_SPREADS_IN → IREDA | +0.50 | events | -1.50% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → IREDA | +0.50 | events | +1.28% |
| 1 | F_RISK_SENTIMENT → IREDA | +0.11 | observed | -0.56% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → IREDA | -0.25 | events | -0.32% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → IREDA | +1.00 | events | -0.32% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → IREDA | -1.56 | events | -0.30% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01-19 | Q3 FY27 results (estimated from Q2 on 2026-10-19) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Equity capital raise (QIP/OFS/government infusion) to support loan growth - timing unverified | corporate_action | 0.30 | -2.5% | -0.75% |

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