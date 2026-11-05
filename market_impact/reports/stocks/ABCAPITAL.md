# ABCAPITAL — Aditya Birla Capital Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.9%**, **12 months -7.8%** (rank 181 / 186 of 200 for 3m / 12m); beta 1.31
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.6%): 3 months 35%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -15.8% … P90 -5.5%; plausible 12m relative-return range incl. stock-specific noise: -32.5% … +12.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.0 pp (model impact -4.0% beta-adjusted vs realised market-adjusted move +7.7%); forward event exposure -9.1% (3m -3.9%; half assumed priced); company-specific events -0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.50 | -6.00 | -0.48 | -0.03 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -5.59 | +0.00 | -2.16 | -3.03 | -0.40 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.66 | -3.00 | -1.90 | +0.11 | +0.13 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -4.15 | -4.00 | -0.15 | +0.04 | -0.05 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.70 | +0.00 | -0.88 | -1.20 | -1.62 | -1.1% |
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -3.10 | -3.00 | +0.00 | -0.11 | +0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.09 | +0.00 | +0.00 | -1.29 | -1.81 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.73 | -2.00 | -0.68 | -0.04 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.60 | -1.50 | -1.02 | -0.06 | -0.02 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +2.49 | +2.50 | +0.00 | +0.00 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.17 | +2.00 | +0.03 | +0.06 | +0.07 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.15 | +0.00 | +1.28 | +1.89 | -1.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.14 | +0.00 | +0.12 | +0.73 | +1.28 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.94 | +0.00 | +0.32 | +1.12 | +0.50 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -9.4% | -9.4% | +0.0 | -1.2 | -4.8 | -3.5 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -6.7% | -6.7% | +0.0 | -2.5 | -3.6 | -0.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.8% | -4.8% | -4.4 | -0.1 | -0.2 | -0.2 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -7.5% | -4.6% | -7.2 | -0.3 | +0.1 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.3% | -3.3% | -2.5 | -0.8 | +0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.3 | -0.4 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.5% | +2.7% | +5.0 | +0.1 | +0.2 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -1.7 | -0.6 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -0.4 | -1.4 | -0.6 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.2% | -2.2% | +0.0 | -1.5 | -2.8 | -2.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.5 | -0.4 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.4% | +2.0% | +0.0 | +0.7 | +1.6 | +1.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → ABCAPITAL | -4.40% | -4.40% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ABCAPITAL | +5.00% | +2.50% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → ABCAPITAL | -1.99% | -1.99% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → ABCAPITAL | -3.00% | -1.86% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → ABCAPITAL | -3.00% | -1.86% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → ABCAPITAL | -1.50% | -1.50% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → ABCAPITAL | -1.33% | -1.33% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_CREDIT_SPREADS_IN → ABCAPITAL | -1.20% | -1.20% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → ABCAPITAL | -1.19% | -1.19% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → ABCAPITAL | -1.12% | -1.12% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_ASSET_QUALITY_IN → ABCAPITAL | -1.07% | -1.07% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → ABCAPITAL | -2.10% | -1.05% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → ABCAPITAL | +1.00% | +1.00% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → ABCAPITAL | +0.96% | +0.96% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → ABCAPITAL | -0.94% | -0.94% |

## Analyst profile (agent research, sourced)
# ABCAPITAL - Aditya Birla Capital Ltd. (Nifty 200, I_NBFC_VEHICLE_CONSUMER) - as of 2026-11-05

## Business
Aditya Birla Capital is the financial-services holding company of the Aditya Birla Group (promoters 68.8%). Lending through an NBFC and a housing-finance company is the largest business (about 58% of group value, model estimate); the rest is a life-insurance joint venture with Sun Life, asset management (ABSLAMC), health insurance and wealth/broking. Q2 FY27 consolidated profit rose 38% to Rs1,288cr as lending grew and costs were controlled. On 2026-08-19 it entered gold loans. At Rs399 it trades at 29.8x earnings and 3.1x book with ROE of 11.6%, which prices in continued strong growth.

## What moves the stock, ranked
1. **Credit cost (F_ASSET_QUALITY_IN -6.0) and unsecured stress (-2.0).** The lending book of ~Rs1.65 lakh cr (model estimate) is the main earnings engine and carries consumer and small-business credit risk.
2. **Funding cost: spreads (-4.0), repo (-1.5), G-sec (-0.8, mixed).** Borrowings ~Rs1.3 lakh cr; the 2026-10-07 hike and wider AAA spreads compress margins before assets reprice. Rising G-sec yields help the life insurer slightly.
3. **Regulation: RBI prudential (-3.0) and IRDAI (-3.0).** Revolving-credit curbs and gold-loan norms affect lending; surrender/commission rules affect insurance.
4. **Growth drivers: credit growth (+2.5), domestic financial flows (+2.5), housing (+1.5).**
5. **Flows (+2.0)** and a weak **Grasim group link (+0.05)**.

## Transmission examples
- **Oil -> rates -> NBFC margin:** Brent at 95 (107 in late Sept) -> CPI up -> RBI hikes again -> bank lending rates and AAA spreads up -> ABCAPITAL's floating liabilities reprice faster than fixed-rate retail assets -> lending NIM compresses -> group EPS growth slows and the 29.8x multiple de-rates.
- **Equity-market chain:** risk-off, VIX up -> SIP flows slow and equity markets fall -> AMC AUM and ULIP premiums fall -> fee income drops -> insurance and AMC contribution weakens (about 30% of value).
- **Regulatory chain:** RBI restricts revolving/unsecured credit -> lending growth slows in consumer segments -> operating leverage fades; but new gold-loan business may offset if gold prices recover.
- **Insurance chain:** IRDAI tightens surrender/commission norms -> distribution incentives change -> new-business margins fall -> value of in-force book re-rated lower.

## Current situation and bull/bear
Q2 profit +38%; stock up 20% in 12 months; Jefferies bullish. Bull: lending growth with improving credit cost, insurance margin gains, cost programmes. Bear: rate-driven margin squeeze, credit-cost normalisation, regulatory tightening, high multiple. Confidence is low: the segment weights and funding split are model estimates and should be refreshed from the Q2 investor presentation.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.