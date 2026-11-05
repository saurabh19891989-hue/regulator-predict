# NAUKRI — Info Edge (India) Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.6%**, **12 months -6.6%** (rank 182 / 182 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.8%): 3 months 40%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -14.1% … P90 -4.5%; plausible 12m relative-return range incl. stock-specific noise: -11.5% … +37.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.7 pp (model impact -5.5% beta-adjusted vs realised market-adjusted move +15.1%); forward event exposure -5.8% (3m -2.6%; half assumed priced); company-specific events +0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US growth (`F_US_GDP`) | +1 pp | +4.30 | +0.00 | +3.21 | +1.17 | -0.07 | — |
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -4.09 | -4.00 | +0.06 | -0.12 | -0.03 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -4.00 | -2.50 | -1.11 | -0.35 | -0.04 | +3.5% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.99 | +2.50 | +1.08 | +0.35 | +0.06 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -3.66 | +0.00 | -1.00 | -1.98 | -0.68 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.18 | +3.00 | +0.16 | -0.00 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.08 | +0.00 | -0.80 | -1.48 | -0.81 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.06 | +3.00 | +0.28 | -0.14 | -0.09 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.64 | +0.00 | +1.72 | +0.71 | +0.21 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.20 | +0.00 | -1.15 | -0.75 | -0.30 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.12 | +0.00 | +1.92 | +0.34 | -0.14 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.08 | +0.00 | +1.92 | +0.34 | -0.18 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.76 | +0.00 | -0.52 | -0.92 | -0.31 | +11.2% |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.76 | +1.50 | +0.24 | +0.01 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.0% | -7.0% | -6.6 | -0.4 | +0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +5.3% | +5.3% | +0.0 | +3.6 | +1.4 | +0.3 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -4.7% | -4.7% | -4.5 | -0.1 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.2% | +4.6% | +8.5 | +0.6 | -0.0 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -16.5% | -4.1% | -13.8 | -2.0 | -0.9 | +0.2 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -14.8% | -3.7% | -7.5 | -7.1 | -0.1 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -1.9 | -0.7 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -1.3 | -1.0 | -0.4 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -14.3% | -2.1% | -10.0 | -4.3 | -0.1 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.0 | -0.7 | -0.4 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -1.8 | -0.3 | -0.1 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.4% | +1.9% | +1.0 | +1.4 | +0.8 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NAUKRI | +7.50% | +3.75% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → NAUKRI | -7.50% | -1.88% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → NAUKRI | -7.50% | -1.88% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → NAUKRI | -2.00% | -1.70% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → NAUKRI | -6.25% | -1.56% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → NAUKRI | -6.25% | -0.94% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → NAUKRI | -4.50% | -0.81% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → NAUKRI | +0.86% | +0.78% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → NAUKRI | -2.50% | -0.62% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → NAUKRI | +1.00% | +0.62% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → NAUKRI | +1.00% | +0.62% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_US_EQUITIES → NAUKRI | -3.75% | -0.56% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → NAUKRI | +1.00% | +0.55% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → NAUKRI | +0.80% | +0.54% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → NAUKRI | -4.50% | -0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → NAUKRI | -1.60 | events | -4.80% |
| 1 | T_GENAI_SERVICES → NAUKRI | +1.00 | events | -4.00% |
| 1 | F_GDP_IN → NAUKRI | +0.50 | events | +1.50% |
| 1 | F_REPO_IN → NAUKRI | +1.00 | events | -1.00% |
| 1 | F_US_TECH_SPEND → NAUKRI | -0.60 | events | -0.90% |
| 1 | F_US_EQUITIES → NAUKRI | +0.23 | observed | +0.58% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → NAUKRI | +1.55 | director_override | -0.56% |
| 1 | F_RISK_SENTIMENT → NAUKRI | +0.11 | observed | -0.28% |
| 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → NAUKRI | -1.60 | events | -0.26% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → NAUKRI | +1.00 | events | -0.16% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → NAUKRI | +0.50 | events | +0.09% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → NAUKRI | +1.35 | events | -0.08% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | CEO transition: Bikhchandani resumes CEO role, Oberoi steps down - governance/strategy | other | 1.00 | +0.0% | +0.00% |
| 2027-01 | Q3 billings update | guidance | 0.90 | +0.5% | +0.45% |
| 2027-02-05 | Q3 FY27 results | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# NAUKRI — Info Edge (India) Ltd., as of 2026-11-05

*Sources: screener.in pack and Google News headlines (Sep-Oct 2026; bodies not retrieved).*

## Business
Info Edge owns Naukri (recruitment), 99acres, Jeevansathi and Shiksha, plus a large investment portfolio (startup portfolio value Rs 41,300 cr in June 2026, NiftyTrader) including stakes in Eternal and PB Fintech. Q2 FY27 revenue Rs 904 cr (+13%), operating margin 39%, billings Rs 822 cr (+12.8%). Market cap Rs 78,261 cr, so roughly half the value is investments, not the core business. Bikhchandani returns as CEO (29 Oct).

## What moves the stock (ranked)
1. Mark-to-market of listed stakes (company links to POLICYBZR and ETERNAL, ~0.10% per +1%) and US equities (+2.5 per +5%).
2. GenAI substitution (T_GENAI_SERVICES -4; Shiksha billings -27%).
3. IT hiring and US tech spend (+1.5), GDP (+3).
4. Risk sentiment (-2.5), FPI flows (+3).
5. 99acres approaching cash breakeven (housing demand +1.5).

## Transmission examples
- **IRDAI shock** to insurance distributors -> PB Fintech falls -> Info Edge stake loses Rs 1,809 cr in a day (ET, 24 Sep) -> Naukri -7%.
- **US tech selloff** -> IT hiring freezes -> Naukri billings slow; portfolio NAV falls -> double hit.
- **GenAI spreads** -> search traffic shifts to chatbots -> Shiksha billings drop; AI hiring tools reduce recruiter listings.
- **Brent up** -> INR weaker -> RBI holds -> housing demand weakens -> 99acres billings grow slower.

## Current situation
Q2: PAT reported as Rs 650 cr (incl. gains; ET quoted Rs 334 cr on another basis). Dividend Rs 3. 90% of analysts Buy after Q2 update (CNBC TV18, 9 Oct).

## Bull / bear
Bull: IT hiring revival, 99acres profitability, portfolio NAV gains. Bear: AI disruption, PB Fintech/Eternal drawdowns, CEO transition.

## Uncertainties
Stake sizes in PB Fintech and Eternal are not verified; link weights low confidence.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.