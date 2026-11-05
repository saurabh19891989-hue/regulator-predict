# LGEINDIA — LG Electronics India Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.9%**, **12 months +0.8%** (rank 20 / 55 of 200 for 3m / 12m); beta 0.95
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.5%): 3 months 52%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.9% … P90 +2.7%; plausible 12m relative-return range incl. stock-specific noise: -37.1% … +38.5%
- Decomposition (12m): 0.5 × forward event exposure +0.6% (3m +0.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.6% (beta-adjusted) vs a realised market-adjusted move of +13.4% — gap -10.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.12 | +3.00 | +0.12 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.08 | +3.00 | +0.00 | +0.09 | -0.01 | — |
| Consumer durables category promotional / discount intensity (`NEW_CONSUMER_DURABLES_PRICE_WAR`) | +1 pp of industry-wide margin given up (discounts, channel incentives, ad spend) in room AC and appliances | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.81 | -1.50 | -0.13 | -0.14 | -0.04 | -1.1% |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -1.80 | -1.80 | +0.00 | +0.00 | +0.00 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +1.58 | +1.50 | +0.06 | +0.01 | +0.01 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.28 | +1.20 | +0.00 | +0.04 | +0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.28 | +0.00 | -1.00 | -0.20 | -0.09 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.26 | +0.00 | +0.94 | +0.21 | +0.11 | — |
| Copper price (`F_COPPER`) | +10% copper | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | -2.4% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.98 | +0.80 | +0.17 | +0.00 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.96 | +0.00 | +0.00 | -0.60 | -0.36 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.95 | -0.90 | -0.05 | +0.00 | -0.01 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.95 | +0.00 | -0.75 | -0.13 | -0.08 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.2% | -2.2% | -1.8 | -0.4 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.1 | -0.2 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.3 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.5% | +1.3% | +2.0 | +0.5 | -0.0 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.8% | -0.9% | -4.1 | -0.5 | -0.2 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.8% | +0.8% | +0.6 | +0.3 | -0.1 | -0.0 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +1.0% | +0.8% | +0.9 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.7% | -0.7% | -0.3 | -0.4 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +0.0 | +0.7 | +0.4 | +0.1 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | -0.1 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | +0.0 | -0.2 | -0.5 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.6% | +0.6% | +0.4 | +0.2 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LGEINDIA | +2.00% | +1.00% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → LGEINDIA | +0.90% | +0.72% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → LGEINDIA | -0.72% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → LGEINDIA | -1.95% | -0.35% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → LGEINDIA | +1.30% | +0.32% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ T_CHINA_PLUS_ONE → LGEINDIA | +0.45% | +0.25% |
| 2 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → F_URBAN_DEMAND → LGEINDIA | +0.29% | +0.23% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → LGEINDIA | +0.40% | +0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → LGEINDIA | -1.20% | -0.22% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ T_CHINA_PLUS_ONE → LGEINDIA | +0.30% | +0.21% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → LGEINDIA | -0.59% | -0.21% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → LGEINDIA | -0.77% | -0.19% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → LGEINDIA | -0.77% | -0.19% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LGEINDIA | -0.75% | -0.19% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → LGEINDIA | -0.40% | -0.18% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → LGEINDIA | +1.55 | director_override | -1.40% |
| 1 | F_FPI_FLOWS → LGEINDIA | -1.60 | events | -1.28% |
| 1 | F_URBAN_DEMAND → LGEINDIA | +0.20 | events | +0.60% |
| 1 | F_USDINR → LGEINDIA | -0.37 | observed | +0.55% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → LGEINDIA | +1.00 | events | -0.25% |
| 1 | F_COPPER → LGEINDIA | -0.24 | observed | +0.24% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → LGEINDIA | -0.60 | events | +0.22% |
| 2 | P_FDI_RULES → T_CHINA_PLUS_ONE → LGEINDIA | +0.50 | events | +0.15% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → LGEINDIA | +0.50 | events | +0.14% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → LGEINDIA | -0.30 | events | +0.13% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → LGEINDIA | +1.55 | director_override | -0.07% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → LGEINDIA | +1.35 | events | -0.06% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Citi '90-day positive catalyst watch' (opened 2026-10-01) runs to ~end Dec; MOFSL target Rs2,080, BOB Capital +20%, UBS Buy | other | 0.50 | +1.5% | +0.75% |
| 2026-11-05 | Q2 FY27 results declared: profit +26% YoY, revenue beat (per headlines); board approved foray into a new business (details not read). Stock +3.5% intraday | results | 1.00 | +1.0% | +1.00% |
| 2027-02 | Q3 FY27 results (festive-quarter sell-through); then summer 2027 AC season | results | 0.95 | +0.0% | +0.00% |
| 2027-06 | Hypothetical parent stake sale (OFS) given 85% holding vs 75% SEBI MPS limit; no evidence of a plan, listed only as a tail risk (SEBI public-shareholding rule: model knowledge) | corporate_action | 0.05 | -5.5% | -0.28% |

## Analyst profile (agent research, sourced)
# LGEINDIA - LG Electronics India Ltd. (midcap, appliances and consumer electronics)

## Business
85%-owned subsidiary of LG Electronics Inc. (Korea), listed in October 2025. Sells refrigerators, washing machines, ACs, microwaves and TVs/displays, manufactured at Noida, Pune and the newer Sri City site, with a growing export book (record in Q1 FY27) and a B2B/AMC service arm. Highest margin among listed peers (EBITDA ~12.5% in Q1 FY27). Fundamentals in the data pack were empty, so valuation and balance-sheet figures here come from news and are low confidence.

## What moves the stock (ranked)
1. **Premiumisation (+3.0) and urban demand (+3.0 per +5pp):** the margin story depends on mix.
2. **Category price war (-3.0 per +1pp):** largest downside because the margin base is high.
3. **Semiconductor/memory and panel costs (-1.8):** TV and smart-appliance BOM.
4. **USD/INR (-1.5 per +3%) and copper (-1.0 per +10%).**
5. Exports/China+1 (+1.5), housing (+1.2), G-sec (-0.9), flows (+0.8), decoupling (+0.5).

## Transmission examples
- **Middle East escalation -> Brent up (1st) -> INR weaker and freight up (2nd) -> USD-linked component and royalty costs up (3rd) -> appliance price hikes of 5-8% (4th) -> festive-quarter volume elasticity and margin squeeze.**
- **AI/memory demand boom -> DRAM/NAND prices up -> TV and smart-appliance BOM up -> Home Entertainment margin (19% in Q1) compresses even as revenue is price-inflated.**
- **Copper up (AI/grid demand) -> compressor/coil costs up -> AC price hike -> Voltas/Blue Star follow; LG's thicker margin lets it hold prices or gain share.**
- **Korean parent weakness (Q3 prelim miss) -> sentiment and potential royalty/transfer-price scrutiny -> stock-specific drawdown with no change in Indian demand.**
- **US-China decoupling -> Chinese appliance rivals face friction -> LG and other non-Chinese brands gain Indian share (small).**

## Current situation
Q2 FY27 was declared on 2026-11-05: headlines say profit +26% and revenue beat estimates, and the board approved a new business (details not read; the Q2 FY26 base was revenue Rs6,174cr and PAT Rs389cr). Q1 FY27: revenue ~Rs7,233cr (+15.5%), PAT Rs653cr, margin 12.5%. Shares rose 3.5% intraday to ~Rs1,813 after hitting a record on 2026-10-05; 3m +14.9%.

## Upcoming
Digest of the Q2 call and new-business details; Citi catalyst watch (to ~end Dec); Q3 FY27 (Feb 2027); summer 2027.

## Bull / bear
Bull: mix and exports hold margin at 12%+, input costs ease, new business adds growth. Bear: rupee and memory cost spike, price war narrows the margin premium, parent-level issues, rich multiple.

Uncertainties: no screener financials; Q2 FY27 figures and new-business scope not read; cost-structure shares are estimates (confidence low).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.