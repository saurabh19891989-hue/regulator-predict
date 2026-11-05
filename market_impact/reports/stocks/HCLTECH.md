# HCLTECH — HCL Technologies Ltd.
*NIFTY_50 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.7%**, **12 months -5.2%** (rank 167 / 165 of 200 for 3m / 12m); beta 0.92
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.8%): 3 months 43%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.9% … P90 -0.5%; plausible 12m relative-return range incl. stock-specific noise: -42.2% … +34.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.1 pp (model impact -2.2% beta-adjusted vs realised market-adjusted move +15.7%); forward event exposure -5.5% (3m -2.1%; half assumed priced); company-specific events -0.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -3.94 | -4.00 | +0.06 | +0.00 | +0.00 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -3.50 | -3.50 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.34 | +2.80 | +0.56 | +0.10 | -0.11 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.75 | +1.50 | +0.35 | -0.08 | -0.02 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.39 | +0.00 | -0.96 | -0.39 | -0.04 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.38 | +1.60 | +0.00 | -0.13 | -0.09 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.21 | -1.00 | -0.23 | +0.01 | +0.02 | +3.5% |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.19 | +1.20 | +0.00 | +0.00 | -0.01 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.13 | -0.70 | -0.23 | -0.22 | +0.02 | +11.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.60 | +0.00 | +0.40 | +0.18 | +0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.53 | +0.00 | +0.10 | -0.59 | -0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.50 | +0.00 | -0.51 | -0.01 | +0.02 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.45 | +0.00 | +0.38 | +0.13 | -0.05 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.0% | +4.0% | +3.0 | +0.9 | +0.1 | -0.0 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -3.9% | -3.9% | -4.0 | +0.1 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -11.9% | -3.0% | -10.8 | -1.4 | +0.5 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -7.0% | -2.0% | -8.5 | +1.2 | +0.3 | -0.0 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -1.8% | -1.8% | -1.8 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.6% | +1.6% | +0.4 | +2.0 | -0.0 | -0.9 |
| Anthropic IPO prices and lists (proposed ticker ANT), Nov 2026-Q1 2027 (`EV_ANTHROPIC_IPO_LISTING`) | anticipated | 0.85 | -1.8% | -1.5% | -2.0 | +0.2 | +0.1 | -0.0 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -6.7% | -1.2% | -7.2 | +0.3 | +0.3 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | -0.7 | -0.5 | -0.0 | +0.0 |
| Appeals court allows $100k H-1B fee (or new rule finalised) and/or OPT fee rule finalised (`EV_H1B_FEE_REINSTATED`) | anticipated | 0.30 | -3.5% | -1.1% | -3.5 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → HCLTECH | -8.40% | -2.10% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → HCLTECH | -2.00% | -1.70% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → HCLTECH | -4.50% | -1.26% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → HCLTECH | -4.50% | -1.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → HCLTECH | -4.00% | -1.12% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → HCLTECH | -3.50% | -1.05% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → HCLTECH | -5.00% | -0.90% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → HCLTECH | +1.92% | +0.54% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → HCLTECH | +2.10% | +0.52% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → HCLTECH | +2.08% | +0.46% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → HCLTECH | +1.26% | +0.45% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → HCLTECH | -0.76% | -0.44% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → HCLTECH | -1.20% | -0.43% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → HCLTECH | -1.40% | -0.42% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → HCLTECH | -0.70% | -0.41% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | T_GENAI_SERVICES → HCLTECH | +1.00 | events | -4.00% |
| 1 | F_US_GDP → HCLTECH | +1.20 | events | +3.36% |
| 1 | P_US_VISA_OUTSOURCING → HCLTECH | +0.90 | events | -3.15% |
| 1 | F_GSEC_10Y_IN → HCLTECH | +1.70 | events | -1.53% |
| 1 | F_FED_FUNDS → HCLTECH | +1.62 | observed | -1.13% |
| 1 | F_USDINR → HCLTECH | -0.37 | observed | -0.59% |
| 1 | F_REFINING_MARGIN → HCLTECH | +1.54 | observed | +0.46% |
| 1 | F_US_EQUITIES → HCLTECH | +0.23 | observed | +0.35% |
| 1 | F_EU_GDP → HCLTECH | +0.22 | events | +0.26% |
| 1 | F_RISK_SENTIMENT → HCLTECH | +0.11 | observed | -0.11% |

## Analyst profile (agent research, sourced)
# HCL Technologies Ltd. (HCLTECH) - company profile, as of 2026-11-05

## Business
HCLTech has three engines: IT and business services (about 72% of revenue), engineering and R&D services (about 16%) and HCLSoftware (about 12%; split is approximate and based on model knowledge). Americas is about 65% of revenue and Europe about 30%. TTM sales are roughly Rs1.35 lakh cr at 21% EBITDA margin, with net cash and a 3.8% dividend yield. Q2 FY27 (reported 2026-10-12) delivered revenue of Rs35,620 cr, PAT of Rs5,132 cr (+11% QoQ), advanced AI revenue +78% YoY, HCLSoftware revenue -11%, and FY27 constant-currency growth guidance of 2.5-4% with margin guidance retained.

## What moves the stock (ranked)
1. **US demand and equity sentiment**: +1pp US growth ~ +2.8%; S&P +5% ~ +1.5% (pack +1.49, t +1.9, consistent).
2. **GenAI substitution**: -4 per unit; HCL has both a strong AI revenue ramp and a shrinking software line - a live signal of substitution.
3. **USD/INR**: +3% ~ +1.6%; pack sign negative (-2.75, t -1.8) but insignificant.
4. **US visa and outsourcing policy**: -3.5 per tightening unit.
5. **Europe growth, rates, VIX**: second-tier.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker -> margin +** (2nd order), but **-> VIX up -> FPI outflow -> premium multiple (20x) compresses** (3rd) and **-> European industrial clients cut ER&D programmes -> ER&D revenue falls** (4th).
- **Fed hawkish -> US yields up -> software budgets tight -> HCLSoftware licence renewals slip**.
- **AI coding agents -> fewer testing/maintenance hours -> infra and app maintenance revenue deflates 2-4%/year -> offsets AI growth**.
- **US outsourcing tax -> onsite cost up -> sector margin -50bp -> relative winner is the one with the lowest H-1B reliance**.

## Current situation
The stock jumped on 2026-10-13 (+4 to +8% intraday) on the Q2 beat, then drifted; it is +19% in a month, +7.4% in three months and -6.2% over twelve. Valuation (20.4x) is a premium to Infosys and Wipro.

## Upcoming
Q3 FY27 results in January 2027; dividend; US policy actions.

## Bull case
AI revenue scales, software stabilises, INR weak: re-rating continues at premium.

## Bear case
Premium multiple unwinds if growth slips under the 2.5% guidance floor, HCLSoftware keeps shrinking, or US policy hits cost.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.