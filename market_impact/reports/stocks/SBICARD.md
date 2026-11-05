# SBICARD — SBI Cards and Payment Services Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.1%**, **12 months -2.4%** (rank 135 / 141 of 200 for 3m / 12m); beta 0.95
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.8%): 3 months 46%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.9% … P90 +2.5%; plausible 12m relative-return range incl. stock-specific noise: -34.5% … +13.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -5.2% beta-adjusted vs realised market-adjusted move -10.1%); forward event exposure -2.9% (3m -1.1%; half assumed priced); company-specific events +0.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -6.38 | -6.00 | -0.28 | -0.10 | +0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.95 | +3.50 | +0.40 | +0.22 | -0.17 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -3.64 | -3.50 | -0.14 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.59 | +0.00 | +1.49 | +1.16 | +0.94 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.28 | +0.00 | +2.80 | +0.82 | -0.35 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.08 | +0.00 | +1.20 | +1.53 | +0.34 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.08 | +3.00 | +0.00 | +0.03 | +0.05 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.05 | -3.00 | -0.25 | +0.17 | +0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.02 | +0.00 | -0.48 | -1.18 | -1.36 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.91 | +0.00 | -0.47 | -2.06 | -0.38 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.61 | -0.80 | -1.68 | -0.29 | +0.16 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.57 | +0.00 | +1.95 | +0.45 | +0.17 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.43 | -1.50 | -0.56 | -0.32 | -0.04 | +3.5% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.34 | +0.00 | +1.68 | +0.54 | +0.12 | +1.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.8% | -6.8% | -6.6 | +0.0 | -0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.5% | -4.5% | +0.0 | -1.9 | -1.5 | -1.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.3% | +4.2% | +8.1 | +0.0 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.3% | -3.3% | -0.9 | -1.9 | -0.6 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.4% | -2.4% | -2.0 | -0.3 | +0.1 | -0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.1% | +2.1% | +0.0 | +1.6 | +1.4 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.1% | -2.0% | -3.8 | -4.3 | -0.2 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.5% | +1.9% | +0.6 | +1.2 | +1.4 | +0.3 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.3 | -0.4 | -0.2 |
| RBI tightens gold-loan / unsecured and NBFC-bank lending norms after early stress (`EV_RBI_GOLD_LOAN_TIGHTEN`) | risk_scenario | 0.30 | -5.8% | -1.7% | -4.8 | -0.8 | -0.2 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.7% | +1.7% | +1.7 | +0.3 | -0.2 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -6.7% | -1.7% | -1.5 | -2.2 | -2.5 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SBICARD | +7.50% | +3.75% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → SBICARD | -3.75% | -0.94% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → SBICARD | -3.00% | -0.90% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → SBICARD | -4.50% | -0.81% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → SBICARD | -0.90% | -0.81% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SBICARD | -1.80% | -0.76% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBICARD | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBICARD | -2.88% | -0.72% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_UNSECURED_STRESS → SBICARD | +0.96% | +0.65% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → SBICARD | -3.75% | -0.56% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → SBICARD | -2.16% | -0.54% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ F_UNSECURED_STRESS → SBICARD | -1.80% | -0.54% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → SBICARD | +1.50% | +0.52% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → SBICARD | +0.58% | +0.52% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SBICARD | -1.80% | -0.49% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → SBICARD | -1.60 | events | -4.80% |
| 1 | F_REPO_IN → SBICARD | +1.00 | events | -1.80% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → SBICARD | -1.56 | events | -1.50% |
| 1 | F_GDP_IN → SBICARD | +0.50 | events | +1.00% |
| 1 | F_CPI_IN → SBICARD | +1.15 | events | -0.92% |
| 1 | F_URBAN_DEMAND → SBICARD | +0.20 | events | +0.70% |
| 1 | F_CREDIT_SPREADS_IN → SBICARD | +0.50 | events | -0.60% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → SBICARD | +1.15 | events | -0.41% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → SBICARD | +0.50 | events | +0.28% |
| 2 | F_RURAL_DEMAND → F_UNSECURED_STRESS → SBICARD | -0.25 | events | -0.24% |
| 2 | F_GDP_IN → F_UNSECURED_STRESS → SBICARD | +0.50 | events | +0.24% |
| 1 | F_COPPER → SBICARD | -0.24 | observed | -0.24% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Festive-season spends data (Oct-Nov) and cobrand ramp (Air India, Eternal) | other | 0.80 | +0.5% | +0.40% |
| 2027 | RBI/NPCI changes to card unsecured risk weights or interchange/MDR rules | regulatory | 0.15 | -4.0% | -0.60% |
| 2027-01-22 | Q3 FY27 results (date approximate; Q2 was 2026-10-23): credit cost vs ~6% FY27 guide, receivables growth in H2 | results | 0.90 | +0.5% | +0.45% |

## Analyst profile (agent research, sourced)
# SBICARD - SBI Cards & Payment Services (as of 2026-11-05)

## Business
SBI Cards issues credit cards (revolving credit, EMI, co-brand, corporate). Revenue is roughly 45% interest on receivables (~Rs58k cr, -2% YoY) and 50% fees/interchange on spends (Rs1.1 lakh cr per quarter). SBI owns ~69% (model knowledge). Q2 FY27 PAT Rs778cr (+75%), caused by impairments falling 37% to Rs819cr; total income only +3-4% (psuconnect, Multibagg, Business Standard, 2026-10-23). The stock at Rs580.6 is -34% over 12 months; the screener extract is empty so fundamentals come from the news summaries.

## What moves the stock (ranked, % equity value per shock)
1. **Unsecured stress (-6.0 per +1pp delinquency)** - the single biggest driver.
2. **Asset-quality/credit cost (-3.5 per +50bp).**
3. **Urban consumption (+3.5 per +5pp)** and GDP (+2.0).
4. **Regulation (-3.0)** and **funding: repo (-1.8), credit spreads (-1.2).**
5. **FPI flows (+3.0)**, VIX (-1.5), UPI substitution (-1.0), CPI (-0.8).
Pack: copper +1.76 per SSU (t 2.8) is the only significant factor; no direct mechanism, so shrunk to +1.0 as a risk/consumption proxy.

## Transmission examples
- **Repo hike (2026-10-07) -> floating borrowings reprice within a quarter -> funding cost +25bp (~Rs140cr annualised) -> management expects NIM stable only if EMI/revolver yields adjust -> card EMI mix shift (ET BFSI) cuts yield -> PAT -3%; 4th order: lower ROE re-rates the multiple (JPMorgan, Nuvama cut targets).**
- **Middle East escalation -> Brent +10% -> CPI +0.25pp and USD/INR weaker -> RBI stays 'calibrated tightening' -> consumers' disposable income down -> spends growth below 6% and revolvers' delinquencies up (F_UNSECURED_STRESS) -> credit cost back above 6% -> PAT -10 to -15%.**
- **Equity sell-off (VIX up) -> FPI outflows -> high-beta financials de-rate -> SBICARD falls with beta ~0.9 even if fundamentals are unchanged.**
- **RBI raises unsecured risk weights -> parent SBIN capital use -> SBICARD growth slows -> holding value to SBIN (4% of mcap) falls.**

## Current situation
Q2 profit beat estimates (Rs700cr est vs Rs780cr, Sahi) but revenue growth is low and the stock fell on the call (Investing.com). Management guides credit cost ~6% for FY27, NIM broadly stable, receivables growth in H2. New co-brands: Eternal (2026-10-15) and Air India (2026-10-28). Mutual funds raised holdings four quarters running (ET, 2026-11-02).

## Upcoming events
RBI December MPC, Q3 results (~2027-01-22), festive-season spend data, any RBI unsecured-lending change (prob 0.15).

## Bull and bear
**Bull:** credit cost normalisation, spend growth recovery, parent support, depressed valuation after a 34% fall.
**Bear:** yield compression from EMI shift, funding costs after hikes, one-off-driven profit growth, regulatory/UPI pressure.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.