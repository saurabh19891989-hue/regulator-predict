# SBICARD — SBI Cards and Payment Services Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months -1.2%** (rank 139 / 148 of 200 for 3m / 12m); beta 0.95
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.8%): 3 months 48%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.4% … P90 +3.0%; plausible 12m relative-return range incl. stock-specific noise: -26.7% … +21.0%
- Decomposition (12m): 0.5 × forward event exposure -1.8% (3m -0.8%; half assumed priced) + 0.5 × company-specific catalysts +0.3%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -4.7% (beta-adjusted) vs a realised market-adjusted move of -10.1% — gap +5.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -6.38 | -6.00 | -0.28 | -0.10 | +0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.98 | +3.50 | +0.40 | +0.22 | -0.14 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -3.64 | -3.50 | -0.14 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.07 | +0.00 | +2.80 | +0.41 | -0.15 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.05 | -3.00 | -0.25 | +0.17 | +0.03 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.05 | +3.00 | +0.00 | +0.03 | +0.03 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.89 | +0.00 | +1.49 | +0.97 | +0.42 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.68 | +0.00 | +1.95 | +0.62 | +0.11 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.42 | +2.00 | +0.58 | -0.19 | +0.04 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.39 | -1.50 | -0.56 | -0.31 | -0.02 | +3.5% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.15 | +0.00 | +1.20 | +0.85 | +0.09 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.14 | -1.80 | -0.32 | +0.06 | -0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.11 | +0.00 | -0.48 | -1.01 | -0.62 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.92 | -0.80 | -1.16 | -0.12 | +0.16 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.7% | -6.7% | -6.6 | +0.0 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.2% | +4.1% | +8.1 | +0.0 | +0.1 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.6% | -3.6% | +0.0 | -1.9 | -1.2 | -0.5 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | -0.9 | -1.3 | -0.4 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.3% | -2.3% | -2.0 | -0.3 | +0.1 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.0% | -2.0% | -3.8 | -4.3 | -0.2 | +0.2 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.8% | +1.8% | +1.7 | +0.3 | -0.2 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.6% | +1.8% | +0.0 | +1.6 | +1.0 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.5% | +1.4% | +0.6 | +1.2 | +0.7 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -8.5% | -1.3% | -3.8 | -5.0 | +0.2 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.1 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SBICARD | +7.50% | +3.75% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → SBICARD | -3.75% | -0.94% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → SBICARD | -4.50% | -0.81% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → SBICARD | -0.90% | -0.81% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SBICARD | -1.80% | -0.76% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBICARD | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBICARD | -2.88% | -0.72% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_UNSECURED_STRESS → SBICARD | +0.96% | +0.65% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → SBICARD | -3.75% | -0.56% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ F_UNSECURED_STRESS → SBICARD | -1.80% | -0.54% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → SBICARD | +1.50% | +0.52% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SBICARD | -1.80% | -0.49% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → SBICARD | +0.60% | +0.48% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → SBICARD | -0.53% | -0.47% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → SBICARD | -0.72% | -0.43% |

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