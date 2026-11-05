# TCS — Tata Consultancy Services Ltd.
*NIFTY_50 · Information Technology · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.3%**, **12 months -2.0%** (rank 195 / 190 of 200 for 3m / 12m); beta 0.94
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.8%): 3 months 46%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.6% … P90 +1.2%; plausible 12m relative-return range incl. stock-specific noise: -33.8% … +28.7%
- Decomposition (12m): 0.5 × forward event exposure -3.7% (3m -1.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -4.3% (beta-adjusted) vs a realised market-adjusted move of +4.1% — gap -8.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -0.45 | -0.04 | -0.49 | -0.19 |
| Sector | -0.22 | -0.22 | -0.44 | -0.15 |
| Theme | -0.34 | -0.03 | -0.37 | -0.28 |
| Geopolitics | +0.00 | -0.01 | -0.01 | -0.00 |
| Company catalysts | -0.05 | +0.00 | -0.05 | -0.39 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.54 | -0.24 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-2.04** | **-1.34** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US/EU enterprise IT services spend (`F_US_TECH_SPEND`) | +5% growth | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| GenAI substitution of IT/BPO labour (higher = more substitution) (`T_GENAI_SERVICES`) | +1 | -3.53 | -4.00 | +0.45 | +0.00 | +0.02 | — |
| US H-1B / outsourcing restrictions (`P_US_VISA_OUTSOURCING`) | +1 = material tightening | -3.17 | -3.00 | -0.17 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +2.14 | +0.00 | +2.26 | -0.06 | -0.05 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | -1.81 | -1.80 | +0.00 | +0.01 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.27 | +1.50 | +0.00 | -0.17 | -0.06 | -1.1% |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.22 | +1.00 | +0.24 | -0.02 | +0.00 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.22 | +1.20 | +0.00 | +0.02 | +0.00 | +1.2% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.97 | +0.00 | -0.72 | -0.18 | -0.07 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -0.97 | -0.70 | -0.10 | -0.19 | +0.02 | +11.2% |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +0.94 | +0.00 | +0.66 | +0.27 | +0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.90 | -0.90 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.79 | +0.00 | -0.49 | -0.31 | +0.02 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.63 | -0.50 | -0.17 | +0.04 | -0.00 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -5.1% | -5.1% | -5.2 | +0.1 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.8% | +2.8% | -0.3 | +3.2 | -0.1 | +0.0 |
| Indian IT: weakest Q2 in 3 years, Infosys guidance cut, US green card freeze (`EV_INDIAN_IT_Q2_VISA_SHOCK`) | occurred | 1.00 | -2.8% | -2.8% | -2.7 | -0.1 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -6.8% | -1.7% | -1.5 | -5.5 | +0.3 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.1% | -1.5% | -4.8 | -0.7 | -0.5 | -0.0 |
| US $100,000 H-1B fee (new ~$103k proposal Aug 2026) blocked by court; administration appeals; DHS proposes $70k/$30k OPT fees (`EV_H1B_100K_FEE_COURT`) | occurred | 1.00 | -1.3% | -1.3% | -1.2 | -0.1 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.2% | -1.2% | -1.3 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | -0.7 | -0.3 | -0.0 | +0.0 |
| Appeals court allows $100k H-1B fee (or new rule finalised) and/or OPT fee rule finalised (`EV_H1B_FEE_REINSTATED`) | anticipated | 0.30 | -3.2% | -1.0% | -3.0 | -0.2 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.6 | -0.4 | +0.1 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -0.7% | -0.7% | -0.6 | -0.1 | -0.0 | -0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -0.9% | -0.7% | -0.7 | -0.2 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_TECH_SPEND → TCS | -4.56% | -1.14% |
| 1 | EV_H1B_FEE_REINSTATED ⇒ P_US_VISA_OUTSOURCING → TCS | -3.00% | -0.90% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → TCS | -3.60% | -0.90% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → TCS | -3.60% | -0.90% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_US_TECH_SPEND → TCS | -2.88% | -0.72% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → TCS | -0.80% | -0.68% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → TCS | +2.10% | +0.52% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → TCS | -0.70% | -0.50% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → TCS | +1.92% | +0.48% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → TCS | -0.54% | -0.43% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TCS | -0.72% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → TCS | +1.95% | +0.35% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → TCS | -0.69% | -0.35% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → TCS | -1.25% | -0.31% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → TCS | +0.48% | +0.30% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_US_TECH_SPEND → TCS | -0.60 | events | -2.40% |
| 1 | T_GENAI_SERVICES → TCS | +0.50 | director_override | -2.00% |
| 1 | F_GSEC_10Y_IN → TCS | +1.55 | director_override | -1.40% |
| 1 | F_FED_FUNDS → TCS | +1.62 | observed | -1.13% |
| 1 | P_US_VISA_OUTSOURCING → TCS | +0.35 | director_override | -1.05% |
| 1 | F_USDINR → TCS | -0.37 | observed | -0.55% |
| 1 | F_US_EQUITIES → TCS | +0.23 | observed | +0.28% |
| 1 | F_EU_GDP → TCS | +0.22 | events | +0.22% |
| 1 | F_RISK_SENTIMENT → TCS | +0.11 | observed | -0.06% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Company wage-hike cycle announcement (Q3-Q4 FY27) | guidance | 0.50 | -0.8% | -0.38% |
| 2027-01-09 | Q3 FY27 results (TCS reports ~9-12 Jan; date unconfirmed): cc growth, AI revenue, margin, variable pay | results | 0.95 | +0.0% | +0.00% |
| 2027-02 | H-1B $100,000 fee appeal / green-card freeze litigation outcomes | regulatory | 0.40 | -1.0% | -0.40% |
| 2027-03-31 | India-US interim trade deal concluded (services/visa side-letter odds uncertain) | regulatory | 0.45 | +1.5% | +0.68% |

## Analyst profile (agent research, sourced)
# TCS — Tata Consultancy Services Ltd. — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast; no expected-return number.

## 1. Business
India's largest IT services company (Tata Sons 71.77%). Revenue is ~95% foreign currency, roughly half from North America and ~30% from the UK and Continental Europe, with BFSI the largest vertical. Debt-free; dividend yield 2.6%; P/E 16.5; market cap Rs9.02 lakh cr. Q2 FY27: revenue Rs73,188 cr (+11.2% in rupees but only +2.8% cc y/y, the weakest September quarter in three years per Reuters), US$7,642 mn, operating margin 24.0%, PAT Rs13,884 cr, TCV US$9.6 bn, annualised AI revenue US$3.1 bn (>10% of revenue). India revenue fell 10.3% q/q.

## 2. What moves the stock, ranked
1. **US/EU enterprise IT spend (+4.0 per +5%)**, the demand engine; links to US GDP, Fed policy and BFSI budgets.
2. **GenAI substitution (-4.0)**: productivity pass-through reprices the services base; offset by AI revenue. The October 'reverse-AI' rally (+18.6% in a month) shows how violently sentiment swings.
3. **US visa/outsourcing policy (-3.0)**: green-card freeze (9 Oct), H-1B fee litigation.
4. **Wages (-1.8)**, **USD/INR (+1.5)**, **US equities (+1.2)**, **long rates (-0.9)**, **Fed funds (-0.7)**, **EU/UK demand (+1.0)**, **risk sentiment (-0.5)**.
The pack shows significant but non-fundamental correlations (Brent +0.96 t=2.2, refining margin +0.88 t=2.1, steel -1.70 t=-2.5) that look like macro-regime proxies; they are not modelled as edges.

## 3. Transmission chains
**Fed chain (4th order).** Oil shock and 3.7% US CPI -> Fed hikes (16 Sep) and December hike odds 0.58 -> US BFSI and consumer clients trim discretionary projects and renegotiate rates -> TCS cc growth stays ~2-3% and TCV conversion slows -> margin leverage lost (24.0% flat) -> equity de-rates; separately, higher US yields strengthen the dollar and the rupee weakens to ~95, which adds ~+1.5% via margin, a partial offset.
**Visa chain.** US freezes green cards for TCS and peers -> more local hiring and subcontracting at higher onsite cost (+1.3-1.5 pp of revenue) -> margin -50 bp unless priced -> clients push back on rates -> competitors with lower H-1B reliance gain share (Wipro, local firms).
**AI chain.** Hyperscaler capex pause/AI sell-off (22 Oct) -> 'anti-AI' rotation into incumbents (stock +5.5% on results) but if capex resets (odds 0.28), enterprise AI project demand falls while productivity pass-through continues -> deflation without volume offset -> negative.
**Rupee/rate chain.** RBI hike (5.50%) and record FPI outflow -> rupee 95-96 -> margin tailwind but a 10y G-sec 7.4% discount-rate headwind for a stock priced on a ~2.6% yield.

## 4. Current situation
Q2: in-line revenue, flat margin, AI at 10% of sales; senior staff miss variable pay (Reuters 9 Oct). Infosys then cut FY27 guidance to 1-2% (23 Oct); IT fell 2-5% on 27-28 Oct after a 16% month. Price Rs2,492 (-16.7% over 12 months).

## 5. Upcoming events
Q3 FY27 results (~9-12 Jan 2027); Nvidia results 17 Nov; FOMC 9 Dec; H-1B appeal; wage-hike cycle; India-US trade deal (odds 0.45 by Mar 2027).

## 6. Bull and bear
**Bull:** Fed pause, AI revenue scaling, large-deal conversion, rupee weakness, 16.5x P/E near the low end of history (not verified). **Bear:** AI deflation, visa tightening, BFSI budget cuts, margin pressure from wages and bench, post-rally mean reversion.

Weak spots: segment mix figures are model estimates; the net profit differs between sources (Rs13,884 vs 13,934 cr).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.