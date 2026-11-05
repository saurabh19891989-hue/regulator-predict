# UNIONBANK — Union Bank of India
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months +0.3%** (rank 56 / 87 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.6%): 3 months 51%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.4% … P90 +3.2%; plausible 12m relative-return range incl. stock-specific noise: -34.2% … +34.4%
- Decomposition (12m): 0.5 × forward event exposure -0.8% (3m +0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.8% (beta-adjusted) vs a realised market-adjusted move of +9.8% — gap -9.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.55 | -6.50 | +0.00 | -0.03 | -0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.84 | -3.50 | -1.59 | +0.21 | +0.05 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.41 | +3.00 | +1.86 | -0.27 | -0.18 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.13 | +0.00 | +3.09 | +1.22 | -0.17 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.37 | +2.00 | +0.54 | +0.80 | +0.03 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.09 | +0.00 | +2.32 | +1.01 | -0.23 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +2.62 | +2.50 | +0.40 | -0.20 | -0.08 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.51 | +0.00 | +0.93 | +1.23 | +0.35 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.11 | +2.00 | +0.11 | -0.04 | +0.05 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.79 | +0.00 | +1.20 | +0.70 | -0.10 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.73 | +0.00 | -1.24 | -0.22 | -0.26 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -1.67 | -0.80 | -0.72 | -0.07 | -0.08 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.61 | +0.00 | +0.13 | +1.12 | +0.37 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.58 | -1.50 | +0.00 | -0.06 | -0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.7% | -4.7% | -4.4 | -0.2 | +0.1 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.2% | +4.2% | +3.5 | +0.9 | -0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -1.2 | -1.5 | -0.4 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.5 | -0.2 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.3% | +2.7% | +5.0 | +0.3 | -0.1 | +0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.3% | -2.1% | -2.4 | +0.1 | +0.0 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.5% | +1.7% | +0.0 | +0.9 | +1.3 | +0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -0.3 | -1.1 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.9 | -0.4 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.2% | +1.2% | +1.0 | +0.2 | -0.0 | +0.0 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +1.4% | +1.2% | +0.0 | +0.5 | +0.7 | +0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.0% | +1.1% | +0.0 | +1.2 | +0.5 | +0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → UNIONBANK | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → UNIONBANK | -1.05% | -0.95% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → UNIONBANK | -0.97% | -0.88% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → UNIONBANK | -1.20% | -0.72% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → UNIONBANK | -1.20% | -0.60% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → UNIONBANK | +0.80% | +0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → UNIONBANK | -3.00% | -0.54% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → UNIONBANK | -4.50% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → UNIONBANK | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → UNIONBANK | -1.92% | -0.48% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → UNIONBANK | +0.60% | +0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → UNIONBANK | -1.87% | -0.47% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_DEPOSIT_GROWTH_IN → UNIONBANK | +0.75% | +0.45% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → UNIONBANK | -1.40% | -0.42% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → UNIONBANK | +1.00% | +0.42% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → UNIONBANK | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → UNIONBANK | +1.55 | director_override | -2.33% |
| 1 | F_GDP_IN → UNIONBANK | +0.50 | events | +1.50% |
| 1 | F_REPO_IN → UNIONBANK | +1.00 | events | +1.00% |
| 1 | F_LIQUIDITY_IN → UNIONBANK | -0.90 | events | -0.72% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → UNIONBANK | +0.50 | events | +0.52% |
| 1 | F_GOVT_CAPEX → UNIONBANK | +0.20 | director_override | +0.40% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → UNIONBANK | +1.00 | events | -0.29% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → UNIONBANK | -0.25 | events | -0.26% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → UNIONBANK | +1.00 | events | -0.26% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → UNIONBANK | +0.50 | events | +0.21% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → UNIONBANK | -1.56 | events | -0.20% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Government PSU consolidation/stake-sale announcements (Oct 2026 reports) | corporate_action | 0.30 | +2.0% | +0.60% |
| 2027-01 | Q3 FY27 results (inferred; Q2 on 2026-10-19): NIM expansion test from the repo hike, GNPA trend | results | 0.92 | +0.5% | +0.46% |
| 2027-03 | Cabinet raises FDI cap in PSU banks from 20% to 49% (draft cabinet note with RBI backing; reports 21 Oct 2026) *(review: [DIRECTOR_CE] RT_N50_A: replaces conflated P_FDI_RULES edge)* | regulatory | 0.50 | +1.5% | +0.75% |

## Analyst profile (agent research, sourced)
# UNIONBANK - Union Bank of India (Nifty Next 50, I_PSU_BANKS) - as of 2026-11-05

## Business
Union Bank of India is a government-owned (74.76%, at the 75% ceiling) bank with roughly Rs11 lakh cr of advances, growing 18.5% y/y, one of the fastest large public-sector lenders. NIM is a thin 2.95%, ROE 15.7%, P/B about 1.0x and P/E 6.5x. Roughly half the loan book is linked to the repo rate (model estimate), so the October hike raises yields quickly while deposit costs lag. Subsidiaries and associates (Star Union Dai-ichi Life, Union AMC, ASREC) are non-core. The stock has risen 23.6% in 12 months and 11% in the last month after a strong Q2.

## What moves the stock, ranked
1. **Credit cost / asset quality (w -6.5 per +50bp).** Q2 profit grew 30% mainly on lower provisions; GNPA is 2.42%, still above private peers, so there is less cushion.
2. **ECL transition (P_RBI_PRUDENTIAL -3.5).** Union estimates a Rs5,500cr hit from April 2027 (about 3.8% of market value), against SBI's Rs19,500cr. RBI is meeting bank CEOs on readiness (2026-11-03).
3. **Repo and NIM (+1.0), G-sec (-1.5).** Asset-sensitivity helps; treasury MTM and higher yields hurt. Net modest positive with wide range.
4. **Growth and funding (credit +2.5, deposits +2.5, GDP +3.0, capex +2.0).** Advances are outpacing deposits, which is why Union returned to the dollar market ($600m, August 2026). Deposit growth is the real swing variable.
5. **Policy and flows (FDI/consolidation +3, FPI +2).**

## Transmission examples
- **Oil -> repo -> NIM:** Middle East escalation -> Brent up (95 now, 107 in late Sept) -> CPI up -> RBI hikes again -> EBLR-linked loans (half the book) reprice in one month -> NIM expands from 2.95% -> EPS up; the 10y G-sec also rises -> AFS book loses value -> net +1.
- **Funding chain:** loan growth at 18.5% vs slower deposits -> CD ratio rises -> bank issues dollar bonds or CDs at higher cost -> hedging costs climb (Reuters 2026-10-27: lenders defer dollar sales) -> cost of funds up -> NIM slips; a liquidity drain by RBI worsens it.
- **ECL chain:** ECL rules -> Rs5,500cr transition provisions -> CET1 falls ~40-60bp -> bank needs capital -> government at 74.76% cannot sell down; it must inject or allow OFS/QIP via a carve-out -> dilution risk.
- **Capex chain:** government capex up -> steel/power/infra borrowers' cash flows improve -> corporate slippages fall -> credit cost falls -> EPS beats.

## Current situation
Q2 FY27 PAT Rs5,537cr (+30%), NII +20%, GNPA 2.42%, NIM 2.95%. Brokerages see upside (Anand Rathi Rs221). A group of four PSU banks is slated for stake cuts to 75% (not Union). Consolidation remains a policy theme after the IDBI sale (2026-10-14).

## Upcoming
Q3 results (Jan 2027), December MPC, ECL (April 2027), capital-raise decision.

## Bull and bear
Bull: strong growth and falling credit cost, NIM expansion, ROE 15.7% at 1.0x book. Bear: ECL and growth need capital, deposit shortage raises funding cost, asset-quality cycle turns. Confidence medium; loan-book split, EBLR share and AFS size are model estimates and should be replaced by investor-presentation figures.

## Notes on evidence quality
Headline results (PAT Rs5,537cr standalone, Rs5,781cr consolidated, NIM 2.95%, GNPA 2.42%, advances +18.53%, ECL estimate Rs5,500cr, $600m dollar bond) come from dated news headlines whose URLs are in the JSON; the two profit figures differ by perimeter (standalone versus consolidated) and are reported separately. Balance-sheet scale, the EBLR share and the AFS book are model estimates. Empirical sensitivities in the pack are weak (no |t| above 1.8) and none contradicts the fundamental weights; the US 10-year elasticity (-1.29, t -1.8) agrees in sign with the G-sec edge. In the second half of FY27 the most informative disclosures to watch are the Q3 NIM, the credit-deposit ratio and the final ECL transition number.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.