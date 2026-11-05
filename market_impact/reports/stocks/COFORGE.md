# COFORGE — Coforge Ltd.
*MIDCAP_100 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.6%**, **12 months -5.0%** (rank 166 / 163 of 200 for 3m / 12m); beta 1.23
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +39.0%): 3 months 45%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.2% … P90 -0.6%; plausible 12m relative-return range incl. stock-specific noise: -49.5% … +42.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.9 pp (model impact -3.7% beta-adjusted vs realised market-adjusted move +37.0%); forward event exposure -2.9% (3m -0.4%; half assumed priced); company-specific events -1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US growth (`F_US_GDP`) | +1 pp | +3.34 | +2.60 | +0.54 | +0.30 | -0.10 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -2.99 | -3.00 | +0.00 | +0.00 | +0.01 | — |
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -2.95 | -3.00 | +0.08 | -0.02 | -0.01 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.19 | +1.50 | +0.63 | +0.05 | +0.00 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.84 | +0.00 | -0.92 | -0.64 | -0.28 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.67 | -1.00 | -0.55 | -0.15 | +0.03 | +3.5% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.66 | +1.80 | -0.15 | +0.00 | +0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.46 | +2.00 | -0.29 | -0.14 | -0.12 | -1.1% |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.28 | -0.70 | -0.22 | -0.32 | -0.03 | +11.2% |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.27 | +0.00 | +0.83 | +0.31 | +0.13 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.01 | +1.00 | +0.00 | +0.01 | -0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.96 | -0.90 | -0.05 | +0.00 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.72 | +0.00 | +0.18 | -0.83 | -0.07 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +0.71 | +0.00 | +0.19 | +0.45 | +0.07 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.2% | -4.2% | -4.4 | +0.2 | -0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.0% | +4.0% | +2.8 | +0.9 | +0.3 | +0.1 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -12.4% | -3.1% | -10.2 | -2.2 | +0.2 | -0.2 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.1 | -0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -9.6% | -2.7% | -8.5 | -1.3 | +0.2 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.7% | +2.3% | +4.9 | -0.3 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.8% | -1.8% | -0.7 | -1.0 | -0.1 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -9.8% | -1.8% | -7.2 | -3.0 | +0.4 | -0.0 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.6 | +0.2 | +0.1 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.2% | -1.2% | -1.2 | +0.0 | +0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → COFORGE | -3.96% | -3.96% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → COFORGE | +3.13% | +3.13% |
| 1 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → COFORGE | +3.12% | +3.12% |
| 1 | EV_IT_AI_DEFLATION_Q2FY27 ⇒ T_GENAI_SERVICES → COFORGE | -3.00% | -3.00% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → COFORGE | +4.50% | +2.25% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → COFORGE | -7.80% | -1.95% |
| 1 | EV_INDIAN_IT_Q2_VISA_SHOCK ⇒ P_US_VISA_OUTSOURCING → COFORGE | -1.50% | -1.50% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → COFORGE | -1.50% | -1.27% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → COFORGE | -4.50% | -1.26% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → COFORGE | -1.26% | -1.26% |
| 1 | EV_H1B_100K_FEE_COURT ⇒ P_US_VISA_OUTSOURCING → COFORGE | -1.20% | -1.20% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → COFORGE | -4.50% | -1.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → COFORGE | -4.00% | -1.12% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → COFORGE | -1.07% | -1.07% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → COFORGE | +0.90% | +0.90% |

## Analyst profile (agent research, sourced)
# Coforge Ltd. (COFORGE) - company profile, as of 2026-11-05

## Business
Coforge is a mid-cap digital engineering services firm serving travel and transport, banking and insurance clients, roughly half from North America. Quarterly sales jumped from Rs4,450 cr (Mar 2026) to Rs5,528 cr (Jun 2026) and Rs6,171 cr (Sep 2026), consistent with a large acquisition (Encora, from model knowledge; not re-verified). Q2 FY27 results on 2026-10-23 showed PAT of Rs588 cr, order book +45% and EBIT margin guidance raised to 16%, though they missed estimates. The stock is up 62% over six months and trades at 42.5x earnings.

## What moves the stock (ranked)
1. **Valuation and flows (F_FPI_FLOWS, F_RISK_SENTIMENT)**: at a 42.5 P/E the stock behaves like a high-beta growth asset; +1.8 per +$5bn FPI inflow.
2. **US demand and sentiment**: +2.6 per +1pp US growth; pack S&P elasticity +2.93 (t +2.6) confirms a strong US-risk-on beta.
3. **Governance**: the chairman's resignation on 2026-09-09 over a board evaluation, then the NRC chair quitting (2026-09-13) cost 7-9% in a day; the new chair Akhil Gupta (2026-09-29) restored some confidence (JPMorgan overweight).
4. **GenAI substitution (-3)** and **US visa policy (-3)**.
5. **USD/INR (+2.0)** and **funding costs** of acquisition debt (interest up 41 -> 108 cr).

## Transmission examples
- **Oil spike (Middle East) -> airfares up -> airline IT budgets tightened -> Coforge travel vertical (22%) growth slows** (3rd order), while **Brent up -> INR weaker -> margin +** (2nd).
- **Fed hawkish -> US yields up -> growth multiples compress -> Coforge de-rates more than Infosys** (higher duration).
- **AI agents -> automated testing/maintenance -> lower billable hours; mitigated by digital-engineering mix**.

## Current situation
Shares recovered after the governance shock to Rs2,084, close to the 52-week high of Rs2,126. Interest expense is up and net margin hinges on integration synergies. Q2 numbers are in line with raised EBIT margin guidance but miss street estimates.

## Upcoming
Q3 FY27 results in January 2027; further board changes; US policy.

## Bull case
Order-book conversion and margin delivery justify a growth premium; FPI flows continue.

## Bear case
Governance concerns recur or integration disappoints, the 42x multiple de-rates by 25-30%.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.