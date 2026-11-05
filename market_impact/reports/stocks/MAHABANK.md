# MAHABANK — Bank of Maharashtra
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.1%**, **12 months -4.0%** (rank 132 / 150 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.7%): 3 months 47%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -11.0% … P90 +6.1%; plausible 12m relative-return range incl. stock-specific noise: -45.5% … +20.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +1.0% beta-adjusted vs realised market-adjusted move +3.3%); forward event exposure -5.5% (3m -1.1%; half assumed priced); company-specific events -0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.07 | -7.00 | +0.00 | -0.05 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.88 | +0.00 | +2.99 | +3.38 | -0.49 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.83 | +2.80 | +2.61 | -0.40 | -0.18 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +4.73 | +0.00 | +2.35 | +3.04 | -0.66 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -4.21 | -3.50 | -0.47 | -0.24 | -0.00 | +3.5% |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.80 | -2.00 | -1.93 | +0.10 | +0.03 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.37 | +0.00 | +0.83 | +2.19 | +0.35 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -3.32 | +0.00 | -1.40 | -1.15 | -0.77 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.13 | +1.50 | +0.50 | +1.06 | +0.07 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.07 | +0.00 | +2.48 | +0.54 | +0.05 | +1.2% |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | +2.92 | +3.50 | -0.29 | -0.37 | +0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.84 | +0.00 | -1.12 | -1.00 | -0.73 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.76 | +0.00 | +1.12 | +1.95 | -0.31 | — |
| US growth (`F_US_GDP`) | +1 pp | +2.75 | +0.00 | +1.06 | +1.90 | -0.21 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.1% | -10.1% | +0.0 | -4.8 | -2.8 | -2.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.9% | -6.9% | -6.9 | -0.1 | +0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -18.6% | -5.2% | -14.0 | -4.3 | -0.5 | +0.2 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -7.2% | -4.5% | -7.2 | +0.1 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.2% | -4.2% | +0.0 | -1.0 | -2.8 | -0.4 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -22.7% | -4.1% | -17.5 | -5.3 | -0.0 | +0.2 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.9% | +3.9% | +2.9 | +1.3 | -0.2 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.7% | +3.9% | +7.7 | +0.2 | -0.1 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +3.4% | +3.4% | +0.0 | +1.4 | +1.7 | +0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -9.1% | -3.2% | -4.2 | -2.2 | -1.5 | -1.2 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -12.1% | -3.0% | +0.0 | -11.2 | -0.2 | -0.7 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -1.1 | -0.9 | -1.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → MAHABANK | -5.50% | -5.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MAHABANK | -14.00% | -3.92% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → MAHABANK | -17.50% | -3.15% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MAHABANK | +6.25% | +3.12% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → MAHABANK | -3.50% | -2.17% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → MAHABANK | -2.10% | -2.10% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → MAHABANK | +1.99% | +1.99% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → MAHABANK | -1.68% | -1.68% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → MAHABANK | -1.66% | -1.66% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → MAHABANK | -4.20% | -1.50% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → MAHABANK | +1.50% | +1.50% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → MAHABANK | +1.50% | +1.50% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → MAHABANK | -1.49% | -1.49% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_RISK_SENTIMENT → MAHABANK | -1.40% | -1.40% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → MAHABANK | +1.40% | +1.40% |

## Analyst profile (agent research, sourced)
# MAHABANK - Bank of Maharashtra (midcap PSU bank)

## Business
Bank of Maharashtra is a Pune-based PSU bank, 73.6% government-owned, with a strong retail/MSME franchise, high CASA share and notably high profitability for a PSU lender (ROE 22.6%). Revenue Rs 31.7k cr TTM, net profit Rs 8.0k cr TTM, Q2 FY27 PAT Rs 2,310 cr (+41% y/y, reported), NII +22%, total business +25.16%. Market cap Rs 64.6k cr, P/E 8.1, P/B 1.7.

## What moves the stock (ranked)
1. **Credit growth and margins** - business +25% with NII +22%; the October repo hike (5.50%) helps EBLR-linked yields quickly (PSU banks have more repo-linked loans than private peers) while CASA keeps deposit costs sticky.
2. **Asset quality / credit cost** - a +50bp credit cost shock costs about -7%; net NPA is very low (model knowledge), so the bank's earnings quality is a premium factor.
3. **Flows and sentiment** - PSU banks are high-beta flow assets: MF buying for four straight quarters, FII rising to 6.5%, but 26-28 Sep saw a -5% PSU sell-off day.
4. **Government supply** - at 73.6% government holding, further OFS/QIP and MPS planning are supply risks.
5. **Regulation** - ECL provisioning transition and project-finance norms.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker and CPI up -> RBI hawkish (7 Oct hike) -> EBLR yields reset up within the quarter while deposits reprice over a year -> NIM up first, but G-sec yields rise too -> AFS MTM loss (-1.5%); 3rd-order: higher borrowing costs for MSMEs (core segment) -> stress; 4th-order: PSU capex loan growth slows.**
- **US 10y 4.89% -> FPI pulls from Indian banks -> Nifty PSU Bank index falls (as on 28 Sep) -> MAHABANK, with thin FII base but high retail/MF base, falls less than private banks but with higher volatility (36%).**
- **Government capex increase -> infra/PSU credit demand -> MAHABANK advances up -> fee/NII growth; fiscal strain -> OFS pressure.**

## Current situation
After +44% in 12 months and +6% on Q2 results, valuation (1.7x book) no longer carries a large PSU discount. FCNR(B) deposit inflows are a system-wide funding boost and later refinancing test.

## Upcoming
Q3 results (January 2027), Union Budget (Feb 2027), RBI December policy, potential QIP/OFS.

## Bull / bear
Bull: RoA ~1.5%+, 20%+ growth, further EBLR repricing, flows keep coming. Bear: valuation fatigue, margin peak, asset quality surprise, government stake sale.

Uncertainty: net profit shown as Rs 2,136 cr on screener (consolidated/standalone difference) vs Rs 2,310 cr in news; EBLR share, GNPA and CASA values are model knowledge (low confidence).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.