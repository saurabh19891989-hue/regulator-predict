# PERSISTENT — Persistent Systems Ltd.
*MIDCAP_100 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.3%**, **12 months -9.7%** (rank 187 / 190 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.5%): 3 months 38%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -16.9% … P90 -4.7%; plausible 12m relative-return range incl. stock-specific noise: -42.4% … +19.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -4.1 pp (model impact -8.2% beta-adjusted vs realised market-adjusted move +8.9%); forward event exposure -8.2% (3m -3.0%; half assumed priced); company-specific events -0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US/EU enterprise IT services spend (`F_US_TECH_SPEND`) | +5% growth | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.16 | +0.00 | +3.29 | +0.24 | -0.37 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -2.70 | -2.50 | -0.21 | +0.00 | +0.01 | — |
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -2.41 | -3.00 | +0.58 | +0.00 | +0.01 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | -2.27 | -2.20 | +0.00 | +0.01 | -0.07 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.22 | +2.00 | +0.29 | -0.03 | -0.03 | +1.2% |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +1.90 | +0.00 | +1.28 | +0.62 | +0.00 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.77 | +1.50 | +0.30 | -0.02 | -0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.73 | +2.20 | +0.00 | -0.32 | -0.15 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.61 | +0.00 | -0.62 | -0.95 | -0.04 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.58 | +0.00 | -0.88 | -0.54 | -0.16 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.49 | -1.00 | -0.16 | -0.35 | +0.03 | +11.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.49 | -1.50 | +0.00 | +0.00 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.47 | -1.20 | -0.31 | +0.07 | -0.03 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.4% | +4.4% | -0.5 | +4.6 | +0.4 | -0.1 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -4.3% | -4.3% | -4.5 | +0.2 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -13.3% | -3.7% | -10.8 | -1.6 | -0.7 | -0.1 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | -0.1 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -10.9% | -2.7% | -3.0 | -8.3 | +0.7 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -0.7 | -1.1 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.6% | -1.6% | -1.0 | -0.5 | -0.1 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -8.3% | -1.5% | -9.0 | +0.7 | +0.3 | -0.2 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.1 | -0.2 | -0.1 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.2% | +1.2% | +0.0 | +2.9 | -0.1 | -1.5 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | +0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → PERSISTENT | +3.44% | +3.44% |
| 1 | EV_IT_AI_DEFLATION_Q2FY27 ⇒ T_GENAI_SERVICES → PERSISTENT | -3.00% | -3.00% |
| 2 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_US_TECH_SPEND → PERSISTENT | +2.28% | +2.28% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → PERSISTENT | -2.10% | -2.10% |
| 2 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_US_EQUITIES → PERSISTENT | +1.73% | +1.73% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PERSISTENT | -6.00% | -1.68% |
| 1 | EV_INDIAN_IT_Q2_VISA_SHOCK ⇒ F_US_TECH_SPEND → PERSISTENT | -1.50% | -1.50% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → PERSISTENT | -6.00% | -1.50% |
| 1 | EV_IT_AI_DEFLATION_Q2FY27 ⇒ F_US_TECH_SPEND → PERSISTENT | -1.50% | -1.50% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_TECH_SPEND → PERSISTENT | -5.70% | -1.43% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → PERSISTENT | -4.80% | -1.34% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → PERSISTENT | -1.50% | -1.27% |
| 1 | EV_INDIAN_IT_Q2_VISA_SHOCK ⇒ P_US_VISA_OUTSOURCING → PERSISTENT | -1.25% | -1.25% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → PERSISTENT | -6.00% | -1.08% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_US_TECH_SPEND → PERSISTENT | -3.60% | -1.01% |

## Analyst profile (agent research, sourced)
_Profile not yet available._

## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.