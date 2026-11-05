# BANKBARODA — Bank of Baroda
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months -2.9%** (rank 114 / 141 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.6%): 3 months 49%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.6% … P90 +1.4%; plausible 12m relative-return range incl. stock-specific noise: -35.7% … +23.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -2.0% beta-adjusted vs realised market-adjusted move -10.5%); forward event exposure -0.6% (3m +1.2%; half assumed priced); company-specific events -2.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.01 | -6.00 | +0.00 | -0.02 | +0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.51 | -3.50 | -1.23 | +0.14 | +0.08 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.31 | +0.00 | +1.06 | +1.89 | -0.64 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.13 | +0.00 | -0.88 | -0.63 | -0.62 | -1.1% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.13 | +2.00 | +0.06 | +0.02 | +0.05 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.66 | +0.00 | +2.86 | -0.99 | -0.21 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.59 | +0.00 | +0.01 | -1.79 | +0.19 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.51 | -0.80 | +0.00 | -0.29 | -0.41 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.45 | -1.40 | +0.00 | -0.03 | -0.03 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.38 | +0.00 | +0.10 | +1.11 | +0.17 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.33 | +0.00 | -0.75 | -0.47 | -0.12 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -1.30 | +0.00 | -0.88 | -0.24 | -0.18 | +2.2% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.24 | +0.80 | +0.00 | +0.50 | -0.06 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -1.21 | -0.60 | -0.58 | +0.03 | -0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -7.5% | -7.5% | -1.2 | -1.2 | -3.0 | -2.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.7% | -4.7% | -4.4 | -0.1 | -0.1 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -6.9% | -4.3% | -7.1 | +0.1 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.4% | +2.7% | +5.0 | +0.1 | +0.1 | +0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | -0.1 | +0.0 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -1.9 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | +0.0 | -2.1 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.7% | -2.0% | -1.0 | -1.5 | -2.0 | -1.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.3% | +1.9% | +0.8 | +0.7 | +1.1 | +0.7 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.8 | -0.1 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -0.1 | -1.4 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -6.2% | -1.7% | +0.0 | -4.9 | -0.9 | -0.4 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → BANKBARODA | -4.40% | -4.40% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKBARODA | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BANKBARODA | -3.50% | -2.17% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → BANKBARODA | -1.96% | -1.96% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → BANKBARODA | -3.00% | -1.86% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → BANKBARODA | -1.20% | -1.20% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → BANKBARODA | -1.19% | -1.19% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_ASSET_QUALITY_IN → BANKBARODA | -1.07% | -1.07% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → BANKBARODA | -3.50% | -1.05% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → BANKBARODA | +1.00% | +1.00% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → BANKBARODA | +0.96% | +0.96% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → BANKBARODA | -0.94% | -0.94% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → BANKBARODA | -2.99% | -0.84% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → BANKBARODA | +0.80% | +0.80% |
| 1 | EV_ECL_DEFERRED ⇒ P_RBI_PRUDENTIAL → BANKBARODA | +2.10% | +0.80% |

## Analyst profile (agent research, sourced)
# Bank of Baroda (BANKBARODA) - Market Impact profile, as of 2026-11-05

## Business
Bank of Baroda (BoB) is a government-controlled (63.97%) universal bank with roughly Rs12 lakh crore of advances (model estimate; implied by NII Rs13,026cr x4 / NIM 2.74% = ~Rs19 lakh cr average earning assets), a sizeable international franchise (UAE, UK, Africa, Asia - about 15% of advances), a strong retail/MSME/agri mix and a treasury arm. Q2 FY27 (quarter to 30 Sep 2026) delivered record net profit Rs6,532cr (+35.8% y/y) but only after a weak Q1 (one-off charge ~Rs5,670cr tied to a legacy NMC-related settlement, per press summaries) and helped by one-offs such as NSE stake-sale gains. NII grew a modest 9% and global NIM slipped to 2.74% from 2.96%; global cost of deposits is 4.71% against a yield on advances of 7.41%. GNPA improved to 1.78% (NNPA 0.37%). Management raised FY27 credit growth guidance to 13-15% and deposit growth to 11-13%, relying on FCNR(B) deposits in H2.

## What moves the stock, ranked
1. **Credit cost / asset quality (-6.0 per +50bp)** - the largest single lever: 50bp on Rs12 lakh cr is ~17% of annualised profit.
2. **ECL / prudential regulation (-3.5)** - RBI's expected-credit-loss transition. Peer Canara disclosed Rs12-15k cr; BoB has not (verified), so this is an assumption of comparable scale.
3. **G-sec yield (-1.4 per +25bp)** - AFS/FVTPL MTM plus a higher cost of equity for a 0.74x P/B stock. Yields hit 7.4-7.5% in October.
4. **FPI flows (+2.0)** and **credit growth (+1.2)**, **deposit growth (+0.9)**.
5. **Repo (+0.5, wide range)** - EBLR assets reprice faster than deposits, but the cycle raises credit costs.
6. Smaller: unsecured stress (-0.6), Gulf remittances (+0.4), Gulf conflict (-0.8), govt capex (+0.8).
Empirical check: only iron ore reaches |t|>=2 (+2.92, t +2.1); we treat that as cyclical beta (BoB's market beta is 1.17) and carry only +0.4. Brent (-0.77, t -1.5) is deliberately not a direct edge because the backbone carries Brent -> CPI -> repo/yields.

## Transmission examples
- **Middle East escalation -> Brent -> inflation -> yields -> BoB.** Escalation lifts Brent (already $95) -> CPI (5.54% in Sep, food 7.74%) -> RBI hikes again (5.75-6% seen in H2) -> 10y G-sec up -> MTM losses on AFS book and lower bank equity multiples. Simultaneously, escalation hits BoB's UAE/Gulf book directly and NRI deposit inflows.
- **Brent up -> INR weaker -> FPI outflow -> PSU bank de-rating.** Brent -> USD/INR -> FPI outflows (FIIs hold 10.3%) -> PSU banks have a high beta of 1.17 to the market; credit growth slows as funding costs rise -> NII growth falls short of the 13-15% guide.
- **Rate hike -> EBLR loans reprice -> NIM up briefly -> hike cycle deepens -> MSME slippages -> credit cost up.** The first order is positive (+0.5), fourth order negative (-6 per +50bp credit cost).
- **Steel price up -> large borrowers' cash flows up -> slippages fall -> credit cost down** (the benign mirror of the iron ore co-movement).

## Current situation
Stock Rs250 (+7.4% 1m, -13.2% 12m) after a 5% jump on 2 Nov following the Q2 beat (JM upgraded to Buy; Nomura constructive). Shetty's $15bn suit (13-14 Oct) knocked 3% off the stock; the bank says it has not been served and will defend. Canara's ECL warning on 15 Oct is the main sector overhang.

## Upcoming
Q3 results (late Jan 2027), RBI Dec MPC (45% chance of another hike), ECL disclosures/implementation, Bombay High Court proceedings, FY27 dividend.

## Bull and bear
**Bull:** growth guidance raised, GNPA falling, record profit, 0.74x book with 3.4% yield, FCNR(B) funding, a mild ECL outcome. **Bear:** NIM compression, heavy one-offs in profit, ECL capital hit, yield-driven MTM, legal tail and a hawkish RBI.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.