# YESBANK — Yes Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -6.9%**, **12 months -10.8%** (rank 197 / 195 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +32.3%): 3 months 34%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -32.1% … P90 +1.4%; plausible 12m relative-return range incl. stock-specific noise: -63.8% … +26.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -10.7% beta-adjusted vs realised market-adjusted move -35.3%); forward event exposure -18.5% (3m -10.3%; half assumed priced); company-specific events -0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -10.25 | -10.00 | -0.18 | -0.05 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -10.09 | +0.00 | -5.32 | -4.49 | -0.28 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -5.94 | +0.00 | +0.00 | -3.26 | -2.67 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.46 | +0.00 | +4.48 | +2.68 | -1.70 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +4.88 | +0.00 | +1.39 | +2.25 | +1.25 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -4.75 | -0.50 | -1.30 | -1.88 | -1.06 | -1.1% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -4.58 | +0.00 | -1.00 | -2.07 | -1.52 | +0.0% |
| India FX reserves (RBI intervention) (`NEW_FX_RESERVES_IN`) | +US$25bn reserves (RBI buys / net inflows) | +4.51 | +0.00 | +2.37 | +1.74 | +0.40 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.42 | -3.00 | -1.40 | +0.07 | -0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.32 | +0.00 | +0.00 | -1.48 | -2.84 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.29 | +0.00 | +0.00 | +2.39 | +1.90 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.13 | +4.00 | +1.92 | -1.37 | -0.42 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.07 | -2.00 | -2.61 | +0.42 | +0.12 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +3.77 | +3.50 | +0.73 | -0.30 | -0.16 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -24.0% | -24.0% | +0.0 | -4.9 | -10.8 | -8.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -12.2% | -12.2% | +0.0 | -6.1 | -5.5 | -0.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.3% | -8.3% | -6.6 | -0.4 | -0.4 | -0.9 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -6.2% | -6.2% | -5.6 | -0.3 | -0.2 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -6.2% | -6.2% | +0.0 | -1.7 | -2.8 | -1.6 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -15.2% | -5.4% | +0.0 | -3.9 | -6.3 | -5.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -8.6% | -5.3% | -9.0 | +0.3 | +0.1 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.0% | -5.0% | -4.2 | -0.8 | +0.0 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +8.5% | +4.9% | +0.0 | +2.1 | +3.6 | +2.8 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -4.7% | -4.7% | +0.0 | -3.4 | -0.6 | -0.7 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.4% | +4.7% | +7.5 | +0.4 | +0.5 | +1.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.9% | -3.9% | +0.0 | -3.1 | -0.3 | -0.6 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → YESBANK | +7.50% | +3.75% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → YESBANK | -5.00% | -3.10% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → YESBANK | -3.00% | -1.80% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → YESBANK | -4.48% | -1.25% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → YESBANK | -2.00% | -1.24% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_CREDIT_GROWTH_IN → YESBANK | -2.00% | -1.24% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → YESBANK | -3.00% | -1.20% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → YESBANK | -2.40% | -1.20% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → YESBANK | +1.15% | +1.04% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → YESBANK | -5.60% | -1.01% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → YESBANK | -4.50% | -0.99% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → YESBANK | -1.50% | -0.90% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → YESBANK | -3.46% | -0.86% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → YESBANK | -3.00% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → YESBANK | -2.88% | -0.81% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → YESBANK | +1.70 | events | -5.10% |
| 1 | F_FPI_FLOWS → YESBANK | -1.60 | events | -4.80% |
| 1 | F_REPO_IN → YESBANK | +1.00 | events | -3.00% |
| 1 | F_GDP_IN → YESBANK | +0.50 | events | +2.00% |
| 1 | F_LIQUIDITY_IN → YESBANK | -0.90 | events | -1.80% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → YESBANK | +0.50 | events | +0.80% |
| 1 | F_CREDIT_SPREADS_IN → YESBANK | +0.50 | events | -0.75% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → YESBANK | -1.56 | events | -0.50% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → YESBANK | +1.00 | events | -0.47% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → YESBANK | -0.25 | events | -0.40% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → YESBANK | +1.00 | events | -0.40% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → YESBANK | -1.56 | events | -0.37% |

## Analyst profile (agent research, sourced)
# YESBANK - Yes Bank Ltd. (Midcap 100, private banks)

## Business
Yes Bank is a mid-sized private bank rebuilt since the March 2020 reconstruction, now anchored by SMBC. Sep-2026 balance sheet: deposits Rs 3.54 lakh crore, borrowings Rs 78,410 cr, investments Rs 99,968 cr, net worth about Rs 53,400 cr. Funding cost is high (interest expense is 67% of Q2 revenue), so the bank's economics depend on deposit mix, repo-linked loan repricing and credit costs. TTM net profit is Rs 4,195 cr, ROE only 7%, and the stock trades at 0.94x book.

## What moves the stock, ranked
1. **AT1 litigation outcome (company-specific).** The Supreme Court on 2026-10-15 set aside the 2020 write-off of Rs 8,415 cr AT1 bonds; the stock fell 17% in two days. Estimates of the earnings hit are Rs 5,217-5,400 cr (ET, CNBC TV18 headlines), unbooked pending a further appeal (Reuters 2026-10-17). That is about 10% of net worth and of market cap.
2. **Asset quality / credit cost (-10 per +50bp).** Low provisions are what lifts profits today; a small reversal of that tailwind has outsized effect on a Rs 4.2k cr profit base.
3. **Funding cost and NIM (repo -3.0, deposit growth +3.5, liquidity +2.0).**
4. **Treasury MTM and discount rate (G-sec -3.0).**
5. **Growth and macro (credit growth +4, GDP +4).**
6. **Foreign flows (+3.0)** with FIIs at 47.8%.

## Transmission examples
- **Oil shock -> inflation -> RBI hikes more:** Brent +10% (1st) -> CPI +0.3pp (2nd) -> RBI second hike after 2026-10-07 (3rd) -> repo-linked assets reprice before deposits, NIM -6bp, bond MTM loss on AFS (4th) -> EPS -4%, valuation -3%.
- **Unsecured stress at fintech/NBFC peers -> RBI prudential tightening -> risk-weights up -> CET1 down at a bank already absorbing an AT1 charge.**
- **SMBC channel:** Japanese bank balance-sheet and yen funding costs -> SMBC appetite for further capital in India -> Yes Bank capital cushion. Positive if SMBC adds equity (Reuters lists large cross-border financial deals in 2026).
- **FPI flows:** US midterm result (2026-11-04/05) -> risk-on -> FPI inflows -> high-beta, high-FII bank outperforms; but the foreign limit caps buying.

## Current situation
Q2 FY27: net profit Rs 1,084 cr (+63-65% YoY), NII +23%, asset quality stable, but AT1 charge excluded. Nomura cut its target to Rs 18; ten brokers had Sell/Underperform calls on 2026-10-21. Stock Rs 16, 52-week range 15.1-25.8. DIIs and FIIs increased holdings in Sep 2026; public fell to 29.1%.

## Upcoming events
Decision on further legal remedies and provisioning (Dec 2026-Jan 2027), Q3 results (Jan 2027), RBI MPC (Dec), possible SMBC stake raise.

## Bull and bear
**Bull:** the market already prices the full AT1 charge (~10% of cap) and the stock is at 0.94x book with improving core earnings; review petition or negotiated settlement is a call option; SMBC support. **Bear:** the full charge cuts CET1 and capital-raising options, ROE stays single-digit, repo hikes pressure NIM, and the AT1 episode keeps tier-1 market access shut. Confidence medium: figures come from headlines and screener; no primary filing or earnings-call text was retrievable.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.