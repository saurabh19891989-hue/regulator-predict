# BANKBARODA — Bank of Baroda
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.9%** (rank 143 / 154 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.6%): 3 months 49%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.7% … P90 +1.6%; plausible 12m relative-return range incl. stock-specific noise: -28.6% … +26.1%
- Decomposition (12m): 0.5 × forward event exposure -1.3% (3m +0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -1.4% (beta-adjusted) vs a realised market-adjusted move of -10.5% — gap +9.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.08 | -0.04 | +0.04 | -0.08 |
| Regulatory | -0.60 | -0.05 | -0.65 | -0.06 |
| Sector | -0.43 | +0.93 | +0.50 | +0.41 |
| Theme | +0.00 | +0.08 | +0.08 | +0.05 |
| Geopolitics | +0.05 | -0.02 | +0.03 | +0.02 |
| Company catalysts | -0.09 | +0.00 | -0.09 | -0.26 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.63 | -0.29 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.86** | **-0.31** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.01 | -6.00 | +0.00 | -0.02 | +0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.51 | -3.50 | -1.23 | +0.14 | +0.08 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.63 | +0.00 | +1.06 | +1.69 | -0.11 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.43 | +0.00 | +2.67 | -0.15 | -0.09 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.08 | +2.00 | +0.06 | -0.01 | +0.03 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.54 | +0.00 | +0.19 | +1.51 | -0.17 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.49 | +0.00 | +0.10 | +0.98 | +0.41 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.42 | -1.40 | +0.00 | -0.02 | -0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.40 | -0.80 | +0.00 | -0.29 | -0.30 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.27 | +0.80 | +0.00 | +0.47 | +0.00 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -1.19 | -0.60 | -0.58 | +0.03 | -0.04 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.17 | +0.00 | -0.75 | -0.39 | -0.04 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.07 | +0.00 | -0.56 | -0.29 | -0.22 | -1.1% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.01 | +0.00 | -0.82 | -0.04 | -0.15 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.6% | -4.6% | -4.4 | -0.1 | +0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.2% | +2.6% | +5.0 | +0.1 | -0.0 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | -0.1 | +0.0 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +0.8 | +1.3 | -0.1 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.1% | -1.9% | -2.1 | +0.0 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -0.1 | -1.2 | -0.5 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.4% | +1.3% | +0.8 | +0.6 | +0.7 | +0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.3 | -0.7 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.1% | +1.1% | +1.0 | +0.1 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -4.2% | -1.0% | +0.0 | -3.8 | -0.4 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.5% | +1.0% | +0.0 | +0.1 | +1.0 | +0.4 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.0% | -1.0% | -0.8 | +0.0 | -0.2 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKBARODA | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BANKBARODA | -1.05% | -0.95% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → BANKBARODA | -0.90% | -0.81% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BANKBARODA | -1.12% | -0.56% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BANKBARODA | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → BANKBARODA | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → BANKBARODA | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → BANKBARODA | -1.87% | -0.47% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → BANKBARODA | +0.80% | +0.44% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → BANKBARODA | -1.40% | -0.42% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → BANKBARODA | -0.60% | -0.36% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → BANKBARODA | +1.00% | +0.35% |
| 2 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → BANKBARODA | -2.88% | -0.35% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → BANKBARODA | +0.48% | +0.33% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → BANKBARODA | +0.40% | +0.32% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → BANKBARODA | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → BANKBARODA | +1.55 | director_override | -2.17% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → BANKBARODA | +0.50 | events | +0.96% |
| 1 | C_MIDEAST_CONFLICT → BANKBARODA | +1.00 | events | -0.80% |
| 1 | F_REPO_IN → BANKBARODA | +1.00 | events | +0.50% |
| 1 | F_LIQUIDITY_IN → BANKBARODA | -0.90 | events | -0.36% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → BANKBARODA | +0.50 | events | -0.28% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → BANKBARODA | -0.25 | events | -0.24% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → BANKBARODA | +1.00 | events | -0.24% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → BANKBARODA | +0.50 | events | +0.20% |
| 1 | F_GOVT_CAPEX → BANKBARODA | +0.20 | director_override | +0.16% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → BANKBARODA | -1.56 | events | -0.15% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Bombay High Court proceedings in BR Shetty (NMC Healthcare) $15bn damages suit; bank says not yet served and will defend | litigation | 0.03 | -17.5% | -0.53% |
| 2027-01 | Q3 FY27 results (Q2 was 2026-10-30; typical late-Jan/early-Feb timing) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Year-end dividend/ FY27 guidance delivery (credit growth 13-15%) | guidance | 0.70 | +0.5% | +0.35% |

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