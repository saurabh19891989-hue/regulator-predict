# MPHASIS — MphasiS Ltd.
*MIDCAP_100 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.5%**, **12 months -6.9%** (rank 181 / 184 of 200 for 3m / 12m); beta 1.26
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.7%): 3 months 39%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.8% … P90 -6.1%; plausible 12m relative-return range incl. stock-specific noise: -39.6% … +13.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.1 pp (model impact -6.1% beta-adjusted vs realised market-adjusted move +3.4%); forward event exposure -4.4% (3m -1.4%; half assumed priced); company-specific events -1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -4.94 | -5.00 | +0.08 | -0.01 | -0.01 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.68 | +3.30 | +0.34 | +0.15 | -0.11 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -3.49 | -3.50 | +0.00 | +0.00 | +0.01 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.04 | +1.50 | +0.56 | -0.01 | -0.01 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.76 | +0.00 | -1.06 | -0.52 | -0.18 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.60 | +2.00 | -0.19 | -0.11 | -0.09 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.50 | -1.00 | -0.43 | -0.11 | +0.04 | +3.5% |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.38 | -0.70 | -0.39 | -0.27 | -0.02 | +11.2% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.08 | -0.80 | -0.36 | +0.04 | +0.04 | +9.4% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.06 | +1.20 | -0.15 | +0.00 | +0.01 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.03 | +0.00 | +0.69 | +0.24 | +0.10 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.91 | -0.90 | +0.00 | +0.00 | -0.01 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +0.80 | +0.80 | +0.00 | +0.01 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.55 | +0.00 | +0.18 | -0.70 | -0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -4.9% | -4.9% | -5.0 | +0.1 | -0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.5% | +4.5% | +3.6 | +0.5 | +0.3 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -13.1% | -3.3% | -12.3 | -1.0 | +0.3 | -0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.6 | +0.3 | +0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.1% | -2.1% | -1.3 | -0.6 | -0.1 | -0.0 |
| Anthropic IPO prices and lists (proposed ticker ANT), Nov 2026-Q1 2027 (`EV_ANTHROPIC_IPO_LISTING`) | anticipated | 0.85 | -2.2% | -1.9% | -2.5 | +0.2 | +0.1 | +0.0 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -1.7% | -1.7% | -1.8 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.3% | -1.6% | -7.0 | +0.2 | +0.4 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.1% | +1.6% | +3.4 | -0.3 | +0.0 | +0.0 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | -1.0 | -0.5 | +0.1 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MPHASIS | -9.90% | -2.47% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → MPHASIS | -2.50% | -2.12% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MPHASIS | +3.00% | +1.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → MPHASIS | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → MPHASIS | -4.50% | -1.12% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → MPHASIS | -3.50% | -1.05% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MPHASIS | -2.50% | -0.62% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → MPHASIS | +2.40% | +0.60% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → MPHASIS | +2.10% | +0.52% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → MPHASIS | -0.70% | -0.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → MPHASIS | +2.60% | +0.47% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → MPHASIS | -0.82% | -0.45% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → MPHASIS | -2.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → MPHASIS | +0.60% | +0.37% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → MPHASIS | -0.72% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | T_GENAI_SERVICES → MPHASIS | +1.00 | events | -5.00% |
| 1 | F_US_GDP → MPHASIS | +1.20 | events | +3.96% |
| 1 | P_US_VISA_OUTSOURCING → MPHASIS | +0.90 | events | -3.15% |
| 1 | F_FPI_FLOWS → MPHASIS | -1.60 | events | -1.92% |
| 1 | F_GSEC_10Y_IN → MPHASIS | +1.55 | director_override | -1.40% |
| 1 | F_US_10Y → MPHASIS | +1.68 | observed | -1.34% |
| 1 | F_FED_FUNDS → MPHASIS | +1.62 | observed | -1.13% |
| 1 | F_USDINR → MPHASIS | -0.37 | observed | -0.74% |
| 1 | F_ALUMINIUM → MPHASIS | -1.96 | observed | -0.59% |
| 1 | F_US_EQUITIES → MPHASIS | +0.23 | observed | +0.35% |
| 1 | F_EU_GDP → MPHASIS | +0.22 | events | +0.18% |
| 1 | F_RISK_SENTIMENT → MPHASIS | +0.11 | observed | -0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (date not captured; pack shows only Jun-26 quarter) | results | 0.60 | +0.0% | +0.00% |
| 2026-12 | US H-1B/outsourcing action | regulatory | 0.15 | -2.8% | -0.41% |
| 2027-01 | Q3 FY27 results | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Blackstone block deal/stake sale (overhang) | corporate_action | 0.15 | -4.5% | -0.67% |

## Analyst profile (agent research, sourced)
# Mphasis Ltd. (MPHASIS) - company profile, as of 2026-11-05

## Business
Mphasis is a Blackstone-controlled mid-cap IT services firm with a heavy BFSI tilt (about 58%, mortgage and banking) and roughly 80% of revenue from North America (model knowledge). The latest quarter in the data pack is June 2026 (sales Rs4,384 cr, +17.5% YoY, EBITDA margin 18%, PAT Rs490 cr); the September quarter had not been captured by 2026-11-05, which lowers confidence. The stock is at Rs2,524, -8.8% over twelve months, at 24.9x earnings with a 2.5% yield.

## What moves the stock (ranked)
1. **US demand and mortgage/BFSI cycle**: the highest US beta among the batch (+3.3 per +1pp US growth). Pack S&P elasticity +1.89 (t +2.3) agrees; higher US yields slow mortgage-related spend (-0.8 per +25bp).
2. **GenAI substitution (-5)**: large legacy BFSI application maintenance.
3. **Controlling-shareholder behaviour**: Blackstone's dividend take (about Rs3,270 cr, Moneycontrol 2026-11-02) outpaces profit and cash growth; a block sale is an overhang risk.
4. **US visa policy (-3.5)** and **USD/INR (+2.0)**.
5. **Statistically significant but non-causal**: aluminium (t +2.1), a cyclical-risk proxy with a token weight.

## Transmission examples
- **Fed pause/cut -> US mortgage rates down -> refinancing and origination volumes up -> bank/mortgage IT spend up -> Mphasis BFSI revenue** (4th order, +).
- **Middle East escalation -> Brent up -> global risk-off -> VIX up -> FPI outflow from mid-cap IT**; also **Brent -> INR weaker -> margin +**.
- **AI agents -> application maintenance deflation -> renewals reprice -> revenue growth falls**.

## Current situation
Recent wins include a GBP35.4m Social Security Scotland contract (2026-10-06). Mid-cap IT rallied in early October on peer results. Missing: Q2 FY27 figures, which should be treated as an unobserved event of +/-7%.

## Upcoming
Q2 FY27 results (if not yet released) and Q3 in January 2027; Blackstone liquidity actions; US policy.

## Bull case
Deal wins plus lower US yields revive mortgage tech demand; margin expands.

## Bear case
AI repricing of legacy BFSI work plus a Blackstone sell-down compress the multiple.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.