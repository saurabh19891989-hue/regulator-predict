# PFC — Power Finance Corporation Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.8%**, **12 months -0.5%** (rank 128 / 113 of 200 for 3m / 12m); beta 1.36
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.3%): 3 months 47%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.6% … P90 +5.7%; plausible 12m relative-return range incl. stock-specific noise: -34.2% … +42.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.0 pp (model impact +2.1% beta-adjusted vs realised market-adjusted move -28.2%); forward event exposure -1.7% (3m -1.1%; half assumed priced); company-specific events +1.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Bank competition in power/infrastructure lending (`NEW_BANK_INFRA_LENDING_COMPETITION`) | +1 = banks take ~5pp of power/infra lending share or compress spreads ~25bp | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.90 | +0.00 | -3.06 | -1.90 | +0.06 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -2.93 | -2.50 | -0.51 | +0.01 | +0.08 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.82 | +2.50 | +0.17 | +0.04 | +0.11 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.76 | +0.00 | +0.00 | -1.71 | -1.05 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.64 | -2.50 | -0.15 | +0.00 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.51 | -2.00 | -0.64 | +0.09 | +0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.43 | -0.80 | -0.56 | -0.66 | -0.40 | -1.1% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.30 | +2.50 | +0.00 | +0.00 | -0.20 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.27 | +0.00 | +0.00 | -0.93 | -1.34 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -2.17 | -2.00 | -0.18 | +0.00 | +0.01 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -2.06 | +0.00 | -1.80 | -0.21 | -0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.02 | +0.00 | -0.55 | -0.85 | -0.62 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -11.0% | -11.0% | +0.0 | -2.7 | -4.7 | -3.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.3% | -6.3% | -5.5 | -0.4 | -0.1 | -0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -5.7% | -5.7% | +0.0 | -3.5 | -2.2 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.9% | -3.9% | -4.0 | +0.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.2% | +3.6% | +6.2 | +0.5 | +0.1 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -2.9 | -0.4 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | -0.0 | +0.1 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -2.6 | -0.2 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -7.7% | -2.8% | +0.0 | -2.6 | -2.9 | -2.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -8.7% | -2.4% | +0.0 | -6.5 | -1.7 | -0.5 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.2% | +2.4% | +0.0 | +1.3 | +1.6 | +1.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.7 | -0.5 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → PFC | -5.50% | -5.50% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → PFC | -3.50% | -3.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PFC | +6.25% | +3.12% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → PFC | -2.65% | -2.65% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → PFC | +2.50% | +2.50% |
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → PFC | +2.00% | +2.00% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → PFC | -2.00% | -2.00% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → PFC | -1.80% | -1.80% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → PFC | +2.00% | +1.80% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → PFC | +4.00% | +1.80% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → PFC | -1.77% | -1.77% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → PFC | -2.50% | -1.55% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_DEMAND_IN → PFC | +1.50% | +1.50% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → PFC | -1.49% | -1.49% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → PFC | -1.31% | -1.31% |

## Analyst profile (agent research, sourced)
# PFC - Power Finance Corporation Ltd. (Nifty Next 50, I_INFRA_POWER_FINANCE) - as of 2026-11-05

## Business
PFC is a government-controlled (55.99%) Maharatna infrastructure NBFC and India's largest lender to the power sector: state discoms and generation companies (the stressed legacy), central and private generators, transmission and, increasingly, renewables. It consolidates REC Ltd (~52.6% owned, model knowledge); the combined loan book is about Rs11 lakh cr, funded by roughly Rs9.8 lakh cr of mostly AAA bonds and foreign-currency loans. PFC earned Rs33,625cr in FY26 and trades at 0.73x book, 4.1x earnings and a 5.6% dividend yield, the cheapest large financial in the universe. The valuation reflects slow growth (TTM revenue +2%), bank competition and uncertainty over the REC merger structure.

## What moves the stock, ranked
1. **Funding costs and G-sec yields (w -2.5 per +25bp 10y; repo -2.0; spreads -1.5).** Liabilities are bond-financed; AAA PSU spreads follow G-secs. Loan resets lag 1-3 years so NIMs compress first. 10y is 7.19% after a 7.48% peak on 2026-10-23.
2. **Competition and growth (NEW_BANK_INFRA_LENDING_COMPETITION, w -6).** Bernstein (2026-08-25) cut targets because banks are lending to power projects; REC cut FY27 loan growth guidance to 10-11% (2026-10-29). PFC's own growth is the swing variable for the multiple.
3. **Merger mechanics (company links: RECLTD w +0.35).** RBI NOC (2026-10-16), NSE/BSE NOCs (2026-10-19), 88:100 swap ratio reported, and a possible preference-share route for the Centre to hold 51%. Direction of the ratio and value accretion are not verified here, so the model treats merger outcomes as company events, not as a fixed edge.
4. **Power-sector reform and demand (P_POWER_REFORM +4, demand +1.5, govt capex +2.5, renewables +2).** Discom privatisation and tariff true-ups are the structural catalyst for a book that is mostly state-utility credit.
5. **Asset quality, prudential rules and flows (-2.0, -2.5, +2.5).**

## Transmission examples
- **Oil/geopolitics -> yields:** Middle East escalation -> Brent up (95 now, 107 in late Sept) -> CPI up -> RBI signals more hikes -> 10y G-sec up -> AAA PSU bond yields up -> PFC's cost of fresh borrowing and cost of equity up -> NIM compresses and the already-low P/B has little room to fall but the dividend-yield bid weakens.
- **Power demand -> credit:** hot summer/industrial demand -> power demand growth up -> private/central generators expand -> disbursements and sanctions at PFC rise -> loan growth recovers from ~10% -> multiple moves from 0.73x towards 0.9x.
- **Bank competition chain:** system liquidity surplus shrinks (RBI CRR tweak, 99% daily maintenance) -> banks price deposits up -> bank power lending slows -> PFC regains share (4th-order positive); the reverse happened in Aug-Oct when excess liquidity let banks undercut spreads.
- **State finances:** state elections/fiscal slippage -> discom subsidy arrears -> utilities delay repayments -> PFC provisions rise on the legacy tail; reform success reverses it.

## Current situation
Q2 FY27 consolidated PAT Rs7,682cr (-2% y/y), H1 Rs16,679cr; expenses/provisions up to Rs1,379cr from Rs35cr last quarter. Second interim dividend declared. RBI approved the merger NOC; the Centre is weighing preference shares to retain 51%. Morgan Stanley downgraded on 2026-11-01. The stock is 21% down in three months.

## Upcoming
Merger approvals (shareholders, creditors, NCLT as applicable), Q3 results (Feb 2027), December MPC, discom reform steps.

## Bull and bear
Bull: merger clean-up, reform progress and 5.6% yield at 0.73x book; yields fall after crude eases. Bear: bank competition and slower growth persist, merger terms disappoint minorities or delay, yields rise further. Confidence medium; the swap-ratio direction and REC's exact market value need primary-document confirmation.

## Notes on evidence quality
Facts on the RBI/NSE/BSE no-objection letters, the reported 88:100 swap ratio, REC's guidance cut, the Bernstein and Morgan Stanley actions, and the Q2 headline numbers come from dated news headlines (Google News RSS URLs are listed in the JSON); consolidated balance-sheet scale (loan book, borrowings, floating share) is a model estimate derived from the screener interest line and the Rs11 lakh cr merger headline, and should be replaced with company-disclosed numbers when the Q2 investor presentation is parsed. The empirical sensitivities in the pack are weak (no |t| above 1.6), so the weights above rest on balance-sheet arithmetic rather than price co-movement.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.