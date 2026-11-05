# OFSS — Oracle Financial Services Software Ltd.
*MIDCAP_100 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.2%**, **12 months -1.5%** (rank 191 / 171 of 200 for 3m / 12m); beta 0.93
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +33.7%): 3 months 47%, 12 months 46%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.5% … P90 +1.2%; plausible 12m relative-return range incl. stock-specific noise: -46.3% … +41.4%
- Decomposition (12m): 0.5 × forward event exposure -1.0% (3m -0.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -1.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.1% (beta-adjusted) vs a realised market-adjusted move of -4.2% — gap +4.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Oracle Corp credit / AI-capex stress (`NEW_ORACLE_PARENT_STRESS`) | +1 = one stress episode (force majeure, debt negotiation headlines), roughly -5% for OFSS | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +2.03 | +1.50 | +0.54 | +0.08 | -0.09 | — |
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -1.96 | -2.00 | +0.06 | -0.01 | -0.01 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.69 | +1.50 | +0.22 | -0.03 | +0.00 | +1.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.48 | -1.00 | -0.43 | -0.07 | +0.02 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.21 | +1.50 | -0.16 | -0.07 | -0.06 | -1.1% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.10 | +0.00 | -0.70 | -0.34 | -0.06 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.09 | -0.70 | -0.18 | -0.23 | +0.02 | +11.2% |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.01 | +1.00 | +0.00 | +0.01 | +0.00 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.90 | +1.00 | -0.10 | +0.00 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.80 | +0.00 | +0.64 | +0.13 | +0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.51 | +0.00 | -0.50 | +0.01 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.4% | +2.4% | +1.4 | +0.9 | +0.1 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.0% | -2.0% | -2.2 | +0.2 | +0.0 | +0.0 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.1 | -0.0 | -0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -7.8% | -2.0% | -6.9 | -1.1 | +0.4 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -7.2% | -1.8% | -7.0 | -0.4 | +0.2 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.7% | +1.4% | +2.9 | -0.2 | +0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.4% | -1.4% | -0.7 | -0.7 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -0.9% | -0.9% | -0.9 | -0.1 | +0.0 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -5.9% | -0.9% | -4.8 | -1.3 | +0.2 | -0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -1.1% | -0.8% | -0.7 | -0.4 | -0.1 | +0.0 |
| Nvidia FQ3 results (reported 17 Nov): beat-and-raise, AI demand intact (`EV_NVDA_NOV17_BEAT`) | scheduled | 0.62 | +1.1% | +0.7% | +1.0 | +0.1 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → OFSS | +2.50% | +1.25% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → OFSS | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → OFSS | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → OFSS | -4.50% | -1.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → OFSS | -2.50% | -0.62% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → OFSS | +2.10% | +0.52% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → OFSS | -0.70% | -0.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → OFSS | -2.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → OFSS | +0.60% | +0.37% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → OFSS | -0.72% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → OFSS | +1.95% | +0.35% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → OFSS | -0.40% | -0.34% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_US_EQUITIES → OFSS | -2.25% | -0.34% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → OFSS | -1.00% | -0.30% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → OFSS | -0.70% | -0.28% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_US_GDP → OFSS | +1.20 | events | +1.80% |
| 1 | F_FPI_FLOWS → OFSS | -1.60 | events | -1.60% |
| 1 | F_GSEC_10Y_IN → OFSS | +1.55 | director_override | -1.40% |
| 1 | F_FED_FUNDS → OFSS | +1.62 | observed | -1.13% |
| 1 | T_GENAI_SERVICES → OFSS | +0.50 | director_override | -1.00% |
| 1 | F_USDINR → OFSS | -0.37 | observed | -0.55% |
| 1 | P_US_VISA_OUTSOURCING → OFSS | +0.35 | director_override | -0.35% |
| 1 | F_US_EQUITIES → OFSS | +0.23 | observed | +0.35% |
| 1 | F_EU_GDP → OFSS | +0.22 | events | +0.22% |
| 1 | F_RISK_SENTIMENT → OFSS | +0.11 | observed | -0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further Oracle Corp credit/AI-capex headlines | other | 0.35 | -4.0% | -1.40% |
| 2027-01 | Q3 FY27 results; licence timing risk | results | 0.90 | +0.0% | +0.00% |
| 2027-02 | Dividend declaration (yield 3.9%) with Q3/Q4 results | corporate_action | 0.50 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Oracle Financial Services Software Ltd. (OFSS) - company profile, as of 2026-11-05

## Business
OFSS sells banking software (core banking FLEXCUBE, digital banking, financial-crime and analytics) to banks worldwide and is majority owned by Oracle Corporation (about 72-73%, model knowledge). Revenue is a mix of product licences (recognised upfront, hence lumpy), maintenance and cloud subscriptions, and services. The June 2026 quarter had a licence spike (sales Rs3,125 cr, PAT Rs1,416 cr, +121% YoY) while September 2026 (Q2 FY27, reported 2026-10-23) was Rs1,907 cr and PAT Rs702 cr (+29% YoY). EBITDA margin is 42-60%, the company is debt-free, ROE is 32.6%, and the dividend yield is 3.9%.

## What moves the stock (ranked)
1. **Oracle parent stress (NEW_ORACLE_PARENT_STRESS)**: on 2026-09-21 to 2026-09-25 the stock fell 4-6.5% a day and had its worst week in 20 months on Oracle's force-majeure notice for a New Mexico data-centre project and debt-negotiation headlines. The fundamental link is thin (royalty and sales channel) but sentiment-driven; -5 per episode.
2. **US sentiment and bank IT budgets**: pack S&P elasticity +2.96 (t +2.4); C_USA +1.5.
3. **USD/INR**: +1.5 (pack +2.65, t +1.1, agrees in sign).
4. **GenAI**: -2; the licence business is less exposed than services.
5. **Non-causal statistical links** (sugar t +2.8, USD/CNY t +2.4): token weights only.

## Transmission examples
- **AI-capex bust or Oracle credit downgrade -> parent seeks to monetise or lever against its OFSS stake (speculative) -> overhang on OFSS -> stock falls** (order 3).
- **Global bank profit squeeze (credit spreads up) -> IT budgets trimmed -> core-banking migrations delayed -> licence revenue slips** (4th order).
- **Brent up -> INR weaker -> INR-cost advantage -> margin up** (2nd order).

## Current situation
After the September Oracle-linked sell-off the stock recovered with the sector (Rs10,193; -2.7% 1m, -13% 3m). Leadership appointments were formalised alongside Q2. Licence timing makes quarterly prints noisy.

## Upcoming
Q3 FY27 results in January 2027; Oracle Corp headlines; dividend.

## Bull case
Migration cycle at large banks yields big licence quarters; dividend yield supports valuation.

## Bear case
Oracle stress continues, bank IT budgets shrink, and licence quarters disappoint.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.