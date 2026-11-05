# PERSISTENT — Persistent Systems Ltd.
*MIDCAP_100 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.8%**, **12 months -2.6%** (rank 177 / 196 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.5%): 3 months 48%, 12 months 46%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -8.3% … P90 +1.5%; plausible 12m relative-return range incl. stock-specific noise: -39.8% … +35.6%
- Decomposition (12m): 0.5 × forward event exposure -3.9% (3m -1.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -1.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -5.2% (beta-adjusted) vs a realised market-adjusted move of +8.9% — gap -14.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -0.38 | -0.05 | -0.43 | -0.16 |
| Sector | -0.26 | -0.35 | -0.61 | -0.19 |
| Theme | -0.26 | -0.05 | -0.30 | -0.23 |
| Geopolitics | +0.00 | -0.03 | -0.03 | -0.01 |
| Company catalysts | -0.50 | +0.00 | -0.50 | +0.17 |
| Market-priced macro | +0.00 | -0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.60 | -0.27 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-2.62** | **-0.77** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US/EU enterprise IT services spend (`F_US_TECH_SPEND`) | +5% growth | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.10 | +0.00 | +3.29 | -0.10 | -0.09 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -2.70 | -2.50 | -0.21 | +0.00 | +0.01 | — |
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -2.41 | -3.00 | +0.58 | +0.00 | +0.02 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | -2.23 | -2.20 | +0.00 | +0.01 | -0.04 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.03 | +2.00 | +0.00 | +0.03 | +0.00 | +1.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.84 | +2.20 | +0.00 | -0.25 | -0.11 | -1.1% |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.78 | +1.50 | +0.30 | -0.02 | +0.00 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +1.65 | +0.00 | +1.28 | +0.38 | -0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.47 | -1.20 | -0.31 | +0.06 | -0.02 | +3.5% |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.43 | -1.00 | -0.16 | -0.31 | +0.04 | +11.2% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.23 | +0.00 | -0.88 | -0.25 | -0.10 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.12 | +0.00 | -0.48 | -0.72 | +0.08 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -4.3% | -4.3% | -4.5 | +0.2 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.1% | +4.1% | -0.5 | +4.6 | -0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -11.5% | -2.9% | -9.0 | -1.8 | -0.6 | -0.1 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | -0.1 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -10.2% | -2.5% | -3.0 | -7.5 | +0.5 | -0.3 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.6% | -1.6% | -1.0 | -0.6 | +0.0 | +0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.3% | -1.3% | -1.1 | -0.2 | -0.1 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.7 | -0.6 | +0.1 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | +0.0 | +0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -1.4% | -1.0% | -1.0 | -0.3 | -0.1 | -0.0 |
| Nvidia FQ3 results (reported 17 Nov): beat-and-raise, AI demand intact (`EV_NVDA_NOV17_BEAT`) | scheduled | 0.62 | +1.5% | +0.9% | +1.3 | +0.2 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PERSISTENT | -6.00% | -1.50% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → PERSISTENT | -6.00% | -1.50% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_TECH_SPEND → PERSISTENT | -5.70% | -1.43% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_US_TECH_SPEND → PERSISTENT | -3.60% | -0.90% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → PERSISTENT | -2.50% | -0.75% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → PERSISTENT | -3.00% | -0.75% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → PERSISTENT | +3.00% | +0.75% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → PERSISTENT | -1.00% | -0.72% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PERSISTENT | -1.20% | -0.60% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → PERSISTENT | -0.66% | -0.53% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → PERSISTENT | +2.86% | +0.51% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → PERSISTENT | -0.60% | -0.51% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → PERSISTENT | -1.01% | -0.51% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → PERSISTENT | +0.80% | +0.50% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → PERSISTENT | -3.00% | -0.45% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_US_TECH_SPEND → PERSISTENT | -0.60 | events | -3.00% |
| 1 | F_GSEC_10Y_IN → PERSISTENT | +1.55 | director_override | -2.33% |
| 1 | F_FED_FUNDS → PERSISTENT | +1.62 | observed | -1.62% |
| 1 | T_GENAI_SERVICES → PERSISTENT | +0.50 | director_override | -1.50% |
| 1 | P_US_VISA_OUTSOURCING → PERSISTENT | +0.35 | director_override | -0.88% |
| 1 | F_USDINR → PERSISTENT | -0.37 | observed | -0.81% |
| 1 | F_US_EQUITIES → PERSISTENT | +0.23 | observed | +0.47% |
| 1 | F_EU_GDP → PERSISTENT | +0.22 | events | +0.33% |
| 1 | F_RISK_SENTIMENT → PERSISTENT | +0.11 | observed | -0.13% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Nagarro regulatory approvals and squeeze-out completion; consolidation begins | corporate_action | 0.70 | +0.5% | +0.35% |
| 2027-01 | Q3 FY27 results (Q2 was 2026-10-15): Nagarro costs, margin recovery, deal conversion from slipped Q2 deals | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Integration milestones; further US$25-30 mn transaction costs hit Q3-Q4 FY27 | other | 0.90 | -1.5% | -1.35% |

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