# TECHM — Tech Mahindra Ltd.
*NIFTY_50 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.5%**, **12 months -1.2%** (rank 153 / 157 of 200 for 3m / 12m); beta 0.92
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.3%): 3 months 49%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.7% … P90 +2.3%; plausible 12m relative-return range incl. stock-specific noise: -41.5% … +35.4%
- Decomposition (12m): 0.5 × forward event exposure -2.3% (3m -1.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.9% (beta-adjusted) vs a realised market-adjusted move of +14.0% — gap -17.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -3.55 | -4.00 | +0.43 | +0.00 | +0.02 | — |
| US/EU enterprise IT services spend (`F_US_TECH_SPEND`) | +5% growth | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +2.21 | +0.00 | +2.35 | -0.08 | -0.06 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -2.19 | -2.00 | -0.19 | +0.00 | +0.00 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | -2.01 | -2.00 | +0.00 | +0.01 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.54 | +1.80 | +0.00 | -0.19 | -0.07 | -1.1% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.51 | +1.50 | +0.00 | +0.01 | +0.00 | +1.2% |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.39 | +1.20 | +0.21 | -0.02 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.08 | +0.00 | -0.80 | -0.20 | -0.08 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.01 | -0.70 | -0.12 | -0.22 | +0.02 | +11.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +0.89 | +0.00 | +0.62 | +0.28 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.85 | +0.00 | -0.52 | -0.36 | +0.02 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.77 | -0.60 | -0.22 | +0.05 | +0.00 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -4.9% | -4.9% | -5.0 | +0.2 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.9% | +2.9% | -0.3 | +3.3 | -0.1 | +0.0 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -2.1% | -2.1% | -2.0 | -0.1 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -7.3% | -1.8% | -2.4 | -5.1 | +0.4 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.7% | -1.7% | -6.0 | -0.3 | -0.4 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | -0.7 | -0.4 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.6 | -0.4 | +0.1 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -0.9% | -0.9% | -0.8 | -0.1 | +0.0 | +0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -0.8% | -0.8% | -0.7 | -0.0 | -0.0 | -0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -1.0% | -0.7% | -0.7 | -0.2 | -0.1 | +0.0 |
| Appeals court allows $100k H-1B fee (or new rule finalised) and/or OPT fee rule finalised (`EV_H1B_FEE_REINSTATED`) | anticipated | 0.30 | -2.2% | -0.7% | -2.0 | -0.2 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → TECHM | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → TECHM | -4.50% | -1.12% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_TECH_SPEND → TECHM | -3.99% | -1.00% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → TECHM | -0.80% | -0.68% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_US_TECH_SPEND → TECHM | -2.52% | -0.63% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → TECHM | -2.00% | -0.60% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → TECHM | +2.10% | +0.52% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → TECHM | -0.70% | -0.50% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → TECHM | +1.92% | +0.48% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → TECHM | -0.60% | -0.48% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → TECHM | +2.34% | +0.42% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → TECHM | -0.83% | -0.41% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TECHM | -0.80% | -0.40% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → TECHM | -1.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → TECHM | +0.60% | +0.37% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_US_TECH_SPEND → TECHM | -0.60 | events | -2.10% |
| 1 | T_GENAI_SERVICES → TECHM | +0.50 | director_override | -2.00% |
| 1 | F_GSEC_10Y_IN → TECHM | +1.55 | director_override | -1.55% |
| 1 | F_FED_FUNDS → TECHM | +1.62 | observed | -1.13% |
| 1 | P_US_VISA_OUTSOURCING → TECHM | +0.35 | director_override | -0.70% |
| 1 | F_USDINR → TECHM | -0.37 | observed | -0.66% |
| 1 | F_US_EQUITIES → TECHM | +0.23 | observed | +0.35% |
| 1 | F_EU_GDP → TECHM | +0.22 | events | +0.26% |
| 1 | F_RISK_SENTIMENT → TECHM | +0.11 | observed | -0.07% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Bonus 1:1 and Rs15 dividend record/payment dates (board recommended 15 Oct; bonus subject to shareholder approval) | corporate_action | 0.90 | +0.5% | +0.45% |
| 2027-01 | Q3 FY27 results (date unconfirmed, ~mid-Jan): margin vs FY27 target, TCV, cash conversion | results | 0.95 | +0.0% | +0.00% |
| 2027-01 | Telecom client capex/spend commentary and large-deal conversions | other | 0.50 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# TECHM — Tech Mahindra Ltd. — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast; no expected-return number.

## 1. Business
Mahindra group IT/BPS provider with the heaviest communications (telecom) exposure among large Indian IT companies, now in a margin-recovery turnaround. Q2 FY27: revenue Rs16,180 cr (+15.6%), US$1,693 mn (cc +2.4% q/q, +7.2% y/y), EBIT margin 14.8% (+270 bp y/y), PAT Rs1,586 cr (+33%), TCV US$1.02 bn (fourth straight quarter above US$1 bn), but free cash flow fell ~43% y/y. Board recommended a 1:1 bonus and a Rs15 dividend; management held its FY27 margin target. Market cap Rs1.79 lakh cr, P/E 31.3 (on recovering earnings).

## 2. What moves the stock, ranked
1. **US/EU IT spend (+3.5 per +5%)** and the telecom capex cycle.
2. **GenAI substitution (-4.0)**: BPS and engineering exposure; this is the main structural risk to margins.
3. **Wages (-2.0)**: the thin 14.8% margin magnifies cost shocks versus TCS.
4. **USD/INR (+1.8)**, **US equities (+1.5; empirical +1.78, t=2.3)**, **long rates (-1.0)**, **EU demand (+1.2)**, **visa (-2.0)**, **Fed funds (-0.7)**, **risk sentiment (-0.6)**.
Empirical flags: Brent +0.94 (t=1.7) and refining margin +1.04 (t=2.0) look like regime proxies; not modelled.

## 3. Transmission chains
**Telecom capex chain (4th order).** US telecom stocks slide (12 Oct, TechM -4%) as rates rise -> operators postpone network/IT transformation spend -> TechM's communications revenue and deal conversion slow -> utilisation and margin recovery stalls (target needs EBIT >15%) -> multiple compresses from 31x; reversal: lower yields and telecom capex improve conversion.
**Fed chain.** Fed hikes and a December hike risk (0.58) -> US/EU enterprise budgets tighten -> TCV falls below the US$1 bn run-rate -> cc growth falls from 7% y/y -> negative operating leverage on a thin margin.
**Rupee chain.** Fed/BOJ tightening -> rupee 95-96 -> ~+85 bp margin per +3% before hedges -> helps margin target, partially offset by hedging and wage costs.
**GenAI chain.** AI-led repricing of BPS contracts -> revenue deflation in run-the-business deals -> reliance on new large deals (TCV) -> deal slippage raises volatility, as the 22% four-day rally and -4% moves show.

## 4. Current situation
Strong beat and a 1:1 bonus drove the biggest one-day gain in over six years (+8%, 16 Oct), an upgrade from Jefferies and Buy reiterations (MOSL TP Rs1,950). The stock is +21% in a month and near its 52-week high (Rs1,824 vs 1,854), after Infosys cut guidance (23 Oct).

## 5. Upcoming events
Bonus/dividend record dates (Nov); Q3 FY27 results (~mid-Jan 2027); FOMC 9 Dec; Nvidia 17 Nov; telecom client commentary.

## 6. Bull and bear
**Bull:** margin target delivery, strong TCV, bonus liquidity, upgrades. **Bear:** mean reversion after a 22% four-day move, FCF decline, telecom concentration, AI deflation, wage and visa costs.

Weak spots: revenue mix by vertical/geography are estimates; the FY27 margin target number was not retrieved.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.