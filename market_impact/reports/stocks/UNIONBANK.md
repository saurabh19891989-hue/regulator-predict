# UNIONBANK — Union Bank of India
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.9%**, **12 months -0.3%** (rank 69 / 109 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.6%): 3 months 53%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -8.1% … P90 +5.8%; plausible 12m relative-return range incl. stock-specific noise: -33.4% … +27.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +3.6% beta-adjusted vs realised market-adjusted move +9.8%); forward event exposure +3.0% (3m +2.3%; half assumed priced); company-specific events -1.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.55 | -6.50 | +0.00 | -0.03 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.13 | +0.00 | +3.09 | +2.67 | -0.63 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.84 | -3.50 | -1.59 | +0.21 | +0.05 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.42 | +3.00 | +2.05 | -0.49 | -0.14 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.82 | +0.00 | +2.32 | +2.25 | -0.75 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.38 | +2.00 | +0.54 | +0.87 | -0.03 | — |
| FDI liberalisation (`P_FDI_RULES`) | +1 = liberalisation | +3.22 | +3.00 | +0.02 | +0.09 | +0.11 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.20 | +0.00 | +0.93 | +1.90 | +0.37 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +2.62 | +2.50 | +0.40 | -0.20 | -0.08 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.36 | +0.00 | +1.20 | +1.54 | -0.38 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -2.24 | +0.00 | -1.24 | -0.38 | -0.62 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.20 | +2.00 | +0.11 | +0.01 | +0.08 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.17 | +0.00 | +0.13 | +1.31 | +0.73 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.11 | +0.00 | +0.28 | -2.33 | -0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.9% | -10.9% | +0.0 | -3.8 | -3.7 | -3.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.9% | -4.9% | -4.4 | -0.3 | -0.0 | -0.2 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -7.8% | -4.8% | -8.0 | +0.2 | +0.0 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.2% | +4.2% | +3.5 | +1.0 | -0.3 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -1.2 | -2.4 | -0.5 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.0% | -3.0% | -2.5 | -0.2 | -0.2 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -1.4 | -0.8 | -0.8 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | +0.3 | -2.9 | -0.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.6% | +2.8% | +5.0 | +0.3 | +0.0 | +0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -7.1% | -2.5% | +0.0 | -2.9 | -2.3 | -1.9 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -2.1 | -0.2 | -0.2 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.7% | +2.4% | +1.6 | +0.4 | +0.7 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → UNIONBANK | -4.40% | -4.40% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → UNIONBANK | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → UNIONBANK | -3.50% | -2.17% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → UNIONBANK | -2.10% | -2.10% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → UNIONBANK | -3.25% | -2.02% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → UNIONBANK | +2.00% | +2.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → UNIONBANK | -1.78% | -1.78% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → UNIONBANK | +1.50% | +1.50% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ P_FDI_RULES → UNIONBANK | +2.10% | +1.47% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → UNIONBANK | +1.60% | +1.44% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → UNIONBANK | -1.44% | -1.44% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → UNIONBANK | +1.32% | +1.32% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → UNIONBANK | -1.19% | -1.19% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_ASSET_QUALITY_IN → UNIONBANK | -1.16% | -1.16% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → UNIONBANK | -3.50% | -1.05% |

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