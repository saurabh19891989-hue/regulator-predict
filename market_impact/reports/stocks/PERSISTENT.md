# PERSISTENT — Persistent Systems Ltd.
*MIDCAP_100 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.3%**, **12 months -9.6%** (rank 187 / 190 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.5%): 3 months 39%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -15.9% … P90 -3.5%; plausible 12m relative-return range incl. stock-specific noise: -41.9% … +35.7%
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

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PERSISTENT | -6.00% | -1.68% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → PERSISTENT | -6.00% | -1.50% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_TECH_SPEND → PERSISTENT | -5.70% | -1.43% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → PERSISTENT | -4.80% | -1.34% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → PERSISTENT | -1.50% | -1.27% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → PERSISTENT | -6.00% | -1.08% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_US_TECH_SPEND → PERSISTENT | -3.60% | -1.01% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → PERSISTENT | -2.50% | -0.75% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → PERSISTENT | +3.00% | +0.75% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → PERSISTENT | +2.86% | +0.63% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → PERSISTENT | +1.74% | +0.62% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → PERSISTENT | -1.04% | -0.61% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PERSISTENT | -1.20% | -0.60% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → PERSISTENT | -2.00% | -0.60% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → PERSISTENT | -1.00% | -0.58% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | T_GENAI_SERVICES → PERSISTENT | +1.00 | events | -3.00% |
| 1 | F_US_TECH_SPEND → PERSISTENT | -0.60 | events | -3.00% |
| 1 | F_GSEC_10Y_IN → PERSISTENT | +1.70 | events | -2.55% |
| 1 | P_US_VISA_OUTSOURCING → PERSISTENT | +0.90 | events | -2.25% |
| 1 | F_FED_FUNDS → PERSISTENT | +1.62 | observed | -1.62% |
| 1 | F_USDINR → PERSISTENT | -0.37 | observed | -0.81% |
| 1 | F_US_EQUITIES → PERSISTENT | +0.23 | observed | +0.47% |
| 1 | F_EU_GDP → PERSISTENT | +0.22 | events | +0.33% |
| 1 | F_RISK_SENTIMENT → PERSISTENT | +0.11 | observed | -0.13% |

## Analyst profile (agent research, sourced)
# PERSISTENT — Persistent Systems Ltd. — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast; no expected-return number.

## 1. Business
Pune-based digital and product-engineering services company serving BFSI, software/hi-tech and healthcare clients, mostly in the US. Q2 FY27: revenue US$487.6 mn (+7.8% q/q, +20% y/y; 26th straight sequential rise), Rs4,664 cr, EBIT margin 15.0% (-130 bp y/y on wage hikes, lower utilisation and deal amortisation), reported PAT Rs352 cr (-25%) after Rs185 cr of Nagarro costs, operating PAT Rs495 cr (+5%), TCV US$633.5 mn. It has secured 94.04% of Nagarro SE (Germany) and plans a squeeze-out; the acquisition was funded partly by a Rs4,265 cr QIP at a Rs5,550 floor (allotted 26 Oct). Market cap Rs1.02 lakh cr, P/E 54.5, P/B 11.4.

## 2. What moves the stock, ranked
1. **US/EU IT spend (+5.0 per +5%)**: mid-cap digital-engineering beta, roughly twice TCS.
2. **Valuation duration: long rates (-1.5), Fed funds (-1.0), risk sentiment (-1.2; empirical t=-2.3), US equities (+2.0; empirical t=2.3).**
3. **GenAI (-3.0)** and **visa (-2.5)**; **wages (-2.2)**; **USD/INR (+2.2)**; **Europe demand (+1.5)** via Nagarro.
Empirical aluminium (+3.11, t=3.0) and edible oil (+3.64, t=2.7) are spurious and not modelled.

## 3. Transmission chains
**Rates-multiple chain (4th order).** RBI hike (5.50%) and Fed hike -> 10y G-sec 7.4% and UST 4.9% -> growth multiples compress (P/E 54.5 means duration ~25 years) -> the stock falls more than the earnings change; DIIs (34%) and the QIP buyers (SBI, ICICI) provide support.
**Nagarro chain.** Deal closing -> EUR revenue and a Germany-heavy delivery base -> margin dilution and US$25-30 mn more costs over two quarters -> consolidated EBIT margin dips below the 16-17% aspiration -> if cross-sell works, upside in FY28; if European demand weakens (EU/UK growth), goodwill and leverage risk.
**AI-trade chain.** Nvidia (17 Nov) and hyperscaler capex -> enterprise AI build-outs raise demand for engineering partners (positive for Persistent more than for BPS-heavy peers) -> but an AI capex reset (odds 0.28) flips this to the downside quickly.
**Rupee chain.** Weak rupee (95-96) -> +95 bp of margin per +3%, a cushion for Nagarro and wage costs.

## 4. Current situation
Deals slipped into Q3 (ICICI Securities Hold, TP Rs5,670; Axis Capital Buy TP Rs7,210). The stock fell 5% on results (16 Oct) but is +11% in a month at Rs6,141. Promoter holding is 28.82% (-1.47 pp), DIIs 34%. No formal guidance was given.

## 5. Upcoming events
Nagarro regulatory approvals/squeeze-out (Dec); Q3 FY27 results (~mid-Jan 2027); Nvidia results 17 Nov; FOMC 9 Dec.

## 6. Bull and bear
**Bull:** continued 20% growth, margin recovery to 16-17%, Nagarro synergies, AI-engineering demand. **Bear:** high multiple under rising rates, integration and leverage, deal slippage, wage/visa costs, AI capex reset.

Weak spots: Nagarro deal value and financing mix not verified; geography and cost splits are estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.