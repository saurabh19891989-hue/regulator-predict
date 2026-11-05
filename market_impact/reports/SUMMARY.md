# Market Impact Graph — Nifty 200 second-to-fourth-order effects (analysis date 2026-11-05)

**What this is.** A causal exposure network: events → macro/commodity/policy/geopolitical drivers → companies, with 2808 weighted edges among 459 nodes (200 company profiles, 161 events of which 62 already occurred since June 2026). Effects propagate up to four hops, damped by order, with double-count controls (clamping, overlap damping, link semantics).

**How to read the numbers.** Expected returns are *scenario-implied*, beta-adjusted and relative to the Nifty 200 average: probability-weighted impacts of upcoming and risk events through the graph (half assumed already priced) plus company-specific catalysts. For market-traded macro drivers (rates, FX, commodities, equity indices, volatility, flows, growth, inflation) the market's own forward path is taken as given: the catalogue's mean drift on them is removed, and their scenarios only widen the risk bands. What remains in the expected return is policy, regulatory, sector, theme and company-specific exposure, which is where 2nd–4th-order effects are most plausibly under-priced. They are not validated forecasts; the rankings are frozen in `ledger/` and will be scored against realised returns and a momentum baseline.

**What the in-sample check showed.** We first also credited the part of June–November driver moves the graph said was not yet in prices. Across 198 stocks the graph's June–November impact correlated **−0.34** with realised market-adjusted moves (agent-estimated event shocks −0.41; market-observed drivers +0.10; within industries −0.16), and eight red-team reviewers found most large 'unpriced' items were stock-specific news the graph lacks (results misses, regulation, competition). That component is therefore excluded from the headline and kept only as a diagnostic. The graph's value is the exposure map — which drivers and events hit which company, by causal order — not a proven return forecast.

## Where the expected returns come from (all 200 stocks, 12 months)
What is left after taking market-priced macro as priced is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Share of the total absolute contribution across stocks, split by the order at which it reaches the company.
| source | share | via 1st order | via 2nd–4th order | biggest positive | biggest negative |
|---|---|---|---|---|---|
| Policy | 17% | 13% | 4% | RECLTD +1.71, PFC +1.64, HINDPETRO +1.44, ADANIENSOL +1.42 | ETERNAL -1.69, SWIGGY -1.21, AUROPHARMA -0.90, LAURUSLABS -0.73 |
| Regulatory | 7% | 6% | 1% | — | POLICYBZR -2.50, MFSL -1.62, HDFCLIFE -1.26, GROWW -1.19 |
| Sector | 36% | 17% | 19% | IDEA +7.29, HINDPETRO +4.70, IOC +2.70, BHARTIARTL +2.54 | GROWW -0.82, PERSISTENT -0.61, TATACOMM -0.54, POWERINDIA -0.53 |
| Theme | 8% | 6% | 3% | LAURUSLABS +2.61, DIXON +1.73, DIVISLAB +1.54, PIIND +1.29 | WIPRO -0.56, INFY -0.47, LTM -0.40, HCLTECH -0.39 |
| Geopolitics | 4% | 1% | 3% | HINDPETRO +0.41, BDL +0.37, BEL +0.30, BHARATFORG +0.29 | OIL -0.29, ONGC -0.22, MOTILALOFS -0.16, MCX -0.15 |
| Company catalysts | 27% | 26% | 1% | MAZDOCK +2.18, PAYTM +1.90, LAURUSLABS +1.82, LUPIN +1.71 | PIIND -2.23, HINDCOPPER -2.21, POLICYBZR -2.12, FORTIS -2.00 |
| Market-priced macro | 0% | 0% | 0% | — | — |

**Catalogue drift removed as already priced (probability-weighted, 12 months):** US equity market -1.48 × (+5% S&P 500); India 10-year G-sec yield +1.18 × (+25 bp yield); Indian banking system liquidity -1.17 × (+1 lakh crore surplus liquidity); Foreign portfolio flows into Indian equities +1.13 × (+US$5 bn net inflow per quarter); Global risk aversion (VIX) +1.12 × (+5 VIX points); RBI repo rate +0.94 × (+25 bp repo); Global natural gas / LNG price +0.90 × (+15% gas/LNG price); US growth -0.80 × (+1 pp); USD/JPY exchange rate -0.80 × (+3% USD/JPY (yen weaker)); India CPI inflation +0.76 × (+1 pp); India FX reserves (RBI intervention) -0.50 × (+US$25bn reserves (RBI buys / net inflows)); Refining margins (GRM / cracks) -0.48 × (+$2/bbl gross refining margin)

## Top 20 (12-month, beta-adjusted, relative)
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | largest upside scenario chain | largest downside scenario chain |
|---|---|---|---|---|---|---|---|---|
| 1 | [IDEA](stocks/IDEA.md) | Vodafone Idea Ltd. | Telecommunication | +1.9 | +7.1 | 59% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA |
| 2 | [HINDPETRO](stocks/HINDPETRO.md) | Hindustan Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +0.9 | +5.3 | 61% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → HINDPETRO |
| 3 | [BHARTIARTL](stocks/BHARTIARTL.md) | Bharti Airtel Ltd. | Telecommunication | +1.9 | +3.4 | 56% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → BHARTIARTL | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BHARTIARTL |
| 4 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +0.6 | +3.1 | 58% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → IOC |
| 5 | [LAURUSLABS](stocks/LAURUSLABS.md) | Laurus Labs Ltd. | Healthcare | +1.4 | +3.1 | 53% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LAURUSLABS | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → LAURUSLABS |
| 6 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +1.2 | +2.9 | 56% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 7 | [DIXON](stocks/DIXON.md) | Dixon Technologies (India) Ltd. | Consumer Durables | +1.0 | +2.7 | 53% | EV_CHINA_FDI_EASING_PN3 ⇒ P_FDI_RULES → DIXON | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → DIXON |
| 8 | [JSWENERGY](stocks/JSWENERGY.md) | JSW Energy Ltd. | Power | +1.2 | +2.7 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JSWENERGY | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → JSWENERGY |
| 9 | [TATAPOWER](stocks/TATAPOWER.md) | Tata Power Co. Ltd. | Power | +1.4 | +2.4 | 56% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATAPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATAPOWER |
| 10 | [BDL](stocks/BDL.md) | Bharat Dynamics Ltd. | Capital Goods | -0.0 | +2.2 | 51% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BDL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BDL |
| 11 | [ADANIPOWER](stocks/ADANIPOWER.md) | Adani Power Ltd. | Power | +1.2 | +2.1 | 52% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIPOWER |
| 12 | [ENRIN](stocks/ENRIN.md) | Siemens Energy India Ltd. | Capital Goods | +1.5 | +2.1 | 50% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → ENRIN | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN |
| 13 | [POWERINDIA](stocks/POWERINDIA.md) | Hitachi Energy India Ltd. | Capital Goods | +0.4 | +2.1 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POWERINDIA | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA |
| 14 | [RELIANCE](stocks/RELIANCE.md) | Reliance Industries Ltd. | Oil Gas & Consumable Fuels | +0.1 | +1.9 | 56% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → RELIANCE | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → RELIANCE |
| 15 | [SOLARINDS](stocks/SOLARINDS.md) | Solar Industries India Ltd. | Chemicals | +1.0 | +1.9 | 53% | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → SOLARINDS | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SOLARINDS |
| 16 | [ADANIENSOL](stocks/ADANIENSOL.md) | Adani Energy Solutions Ltd. | Power | +1.7 | +1.8 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENSOL | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIENSOL |
| 17 | [NLCINDIA](stocks/NLCINDIA.md) | NLC India Ltd. | Power | +0.1 | +1.6 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NLCINDIA | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → NLCINDIA |
| 18 | [NHPC](stocks/NHPC.md) | NHPC Ltd. | Power | +0.9 | +1.6 | 55% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NHPC | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → NHPC |
| 19 | [TMCV](stocks/TMCV.md) | Tata Motors Ltd. | Capital Goods | +0.4 | +1.5 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TMCV | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TMCV |
| 20 | [PAYTM](stocks/PAYTM.md) | One 97 Communications Ltd. | Financial Services | +1.8 | +1.5 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PAYTM | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → PAYTM |

## Bottom 20
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | largest upside scenario chain | largest downside scenario chain |
|---|---|---|---|---|---|---|---|---|
| 200 | [POLICYBZR](stocks/POLICYBZR.md) | PB Fintech Ltd. | Financial Services | -3.2 | -4.8 | 43% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POLICYBZR | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → POLICYBZR |
| 199 | [HINDCOPPER](stocks/HINDCOPPER.md) | Hindustan Copper Ltd. | Metals & Mining | -0.6 | -2.8 | 51% | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → HINDCOPPER | EV_FED_DEC26_HIKE25 ⇒ F_DXY → F_COPPER → HINDCOPPER |
| 198 | [GROWW](stocks/GROWW.md) | Billionbrains Garage Ventures Ltd. | Financial Services | -0.8 | -2.8 | 46% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → GROWW | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → GROWW |
| 197 | [FORTIS](stocks/FORTIS.md) | Fortis Healthcare Ltd. | Healthcare | -2.8 | -2.7 | 43% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → FORTIS | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → FORTIS |
| 196 | [PERSISTENT](stocks/PERSISTENT.md) | Persistent Systems Ltd. | Information Technology | -0.8 | -2.6 | 46% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → PERSISTENT | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PERSISTENT |
| 195 | [ETERNAL](stocks/ETERNAL.md) | Eternal Ltd. | Consumer Services | -1.2 | -2.5 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ETERNAL | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → ETERNAL |
| 194 | [BIOCON](stocks/BIOCON.md) | Biocon Ltd. | Healthcare | -0.5 | -2.5 | 44% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BIOCON | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → BIOCON |
| 193 | [MUTHOOTFIN](stocks/MUTHOOTFIN.md) | Muthoot Finance Ltd. | Financial Services | -0.5 | -2.3 | 47% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MUTHOOTFIN |
| 192 | [SWIGGY](stocks/SWIGGY.md) | Swiggy Ltd. | Consumer Services | -1.7 | -2.3 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SWIGGY | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → SWIGGY |
| 191 | [MPHASIS](stocks/MPHASIS.md) | MphasiS Ltd. | Information Technology | -1.0 | -2.1 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MPHASIS | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MPHASIS |
| 190 | [TCS](stocks/TCS.md) | Tata Consultancy Services Ltd. | Information Technology | -1.3 | -2.0 | 48% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → TCS | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_US_TECH_SPEND → TCS |
| 189 | [COFORGE](stocks/COFORGE.md) | Coforge Ltd. | Information Technology | -1.3 | -1.9 | 47% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → COFORGE | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → COFORGE |
| 188 | [INFY](stocks/INFY.md) | Infosys Ltd. | Information Technology | -1.4 | -1.9 | 45% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → INFY | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → INFY |
| 187 | [MFSL](stocks/MFSL.md) | Max Financial Services Ltd. | Financial Services | -0.8 | -1.9 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MFSL | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → MFSL |
| 186 | [MCX](stocks/MCX.md) | Multi Commodity Exchange of India Ltd. | Financial Services | -1.2 | -1.8 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MCX | EV_SEBI_FNO_CURBS_RISK ⇒ P_SEBI_DERIVATIVES → MCX |
| 185 | [VAML](stocks/VAML.md) | Vedanta Aluminium Metal Ltd. | Metals & Mining | -1.5 | -1.7 | 48% | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → VAML | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → VAML |
| 184 | [BSE](stocks/BSE.md) | BSE Ltd. | Financial Services | -0.3 | -1.7 | 46% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BSE | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → BSE |
| 183 | [HINDZINC](stocks/HINDZINC.md) | Hindustan Zinc Ltd. | Metals & Mining | -1.0 | -1.7 | 48% | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → HINDZINC | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC |
| 182 | [NATIONALUM](stocks/NATIONALUM.md) | National Aluminium Co. Ltd. | Metals & Mining | -0.3 | -1.6 | 49% | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → NATIONALUM | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → NATIONALUM |
| 181 | [TECHM](stocks/TECHM.md) | Tech Mahindra Ltd. | Information Technology | -0.7 | -1.6 | 48% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → TECHM | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → TECHM |

## Nifty Next 50 — all 50 ranked
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | largest upside scenario chain | largest downside scenario chain |
|---|---|---|---|---|---|---|---|---|
| 1 | [IDEA](stocks/IDEA.md) | Vodafone Idea Ltd. | Telecommunication | +1.9 | +7.1 | 59% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA |
| 4 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +0.6 | +3.1 | 58% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → IOC |
| 6 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +1.2 | +2.9 | 56% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 9 | [TATAPOWER](stocks/TATAPOWER.md) | Tata Power Co. Ltd. | Power | +1.4 | +2.4 | 56% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATAPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATAPOWER |
| 11 | [ADANIPOWER](stocks/ADANIPOWER.md) | Adani Power Ltd. | Power | +1.2 | +2.1 | 52% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIPOWER |
| 12 | [ENRIN](stocks/ENRIN.md) | Siemens Energy India Ltd. | Capital Goods | +1.5 | +2.1 | 50% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → ENRIN | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN |
| 13 | [POWERINDIA](stocks/POWERINDIA.md) | Hitachi Energy India Ltd. | Capital Goods | +0.4 | +2.1 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POWERINDIA | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA |
| 15 | [SOLARINDS](stocks/SOLARINDS.md) | Solar Industries India Ltd. | Chemicals | +1.0 | +1.9 | 53% | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → SOLARINDS | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SOLARINDS |
| 16 | [ADANIENSOL](stocks/ADANIENSOL.md) | Adani Energy Solutions Ltd. | Power | +1.7 | +1.8 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENSOL | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIENSOL |
| 19 | [TMCV](stocks/TMCV.md) | Tata Motors Ltd. | Capital Goods | +0.4 | +1.5 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TMCV | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TMCV |
| 21 | [ADANIGREEN](stocks/ADANIGREEN.md) | Adani Green Energy Ltd. | Power | +0.7 | +1.5 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIGREEN | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIGREEN |
| 24 | [BPCL](stocks/BPCL.md) | Bharat Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +0.5 | +1.3 | 55% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL |
| 28 | [SIEMENS](stocks/SIEMENS.md) | Siemens Ltd. | Capital Goods | +0.5 | +1.1 | 52% | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → SIEMENS | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → SIEMENS |
| 30 | [GAIL](stocks/GAIL.md) | GAIL (India) Ltd. | Oil Gas & Consumable Fuels | +0.3 | +1.1 | 52% | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → GAIL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GAIL |
| 31 | [HAL](stocks/HAL.md) | Hindustan Aeronautics Ltd. | Capital Goods | +0.4 | +1.0 | 52% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → HAL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HAL |
| 33 | [PNB](stocks/PNB.md) | Punjab National Bank | Financial Services | +0.7 | +0.9 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PNB | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → PNB |
| 34 | [DIVISLAB](stocks/DIVISLAB.md) | Divi's Laboratories Ltd. | Healthcare | +0.4 | +0.9 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DIVISLAB | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → DIVISLAB |
| 36 | [PFC](stocks/PFC.md) | Power Finance Corporation Ltd. | Financial Services | +0.1 | +0.9 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PFC | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PFC |
| 37 | [UNIONBANK](stocks/UNIONBANK.md) | Union Bank of India | Financial Services | +0.7 | +0.9 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → UNIONBANK | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → UNIONBANK |
| 43 | [CGPOWER](stocks/CGPOWER.md) | CG Power and Industrial Solutions Ltd. | Capital Goods | +0.5 | +0.8 | 52% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → CGPOWER |
| 49 | [JINDALSTEL](stocks/JINDALSTEL.md) | Jindal Steel Ltd. | Metals & Mining | +0.1 | +0.8 | 52% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL |
| 59 | [BRITANNIA](stocks/BRITANNIA.md) | Britannia Industries Ltd. | Fast Moving Consumer Goods | +0.4 | +0.6 | 54% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BRITANNIA | EV_WHEAT27_CROP_BELOW ⇒ F_WHEAT → BRITANNIA |
| 64 | [POLYCAB](stocks/POLYCAB.md) | Polycab India Ltd. | Capital Goods | -0.3 | +0.5 | 53% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POLYCAB | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → POLYCAB |
| 68 | [AMBUJACEM](stocks/AMBUJACEM.md) | Ambuja Cements Ltd. | Construction Materials | +0.6 | +0.5 | 53% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → AMBUJACEM | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → AMBUJACEM |
| 71 | [HYUNDAI](stocks/HYUNDAI.md) | Hyundai Motor India Ltd. | Automobile and Auto Components | +0.3 | +0.4 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HYUNDAI | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → HYUNDAI |
| 92 | [PIDILITIND](stocks/PIDILITIND.md) | Pidilite Industries Ltd. | Chemicals | +0.2 | +0.1 | 50% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → PIDILITIND | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PIDILITIND |
| 103 | [VBL](stocks/VBL.md) | Varun Beverages Ltd. | Fast Moving Consumer Goods | +0.0 | -0.0 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VBL | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → VBL |
| 109 | [GODREJCP](stocks/GODREJCP.md) | Godrej Consumer Products Ltd. | Fast Moving Consumer Goods | -0.1 | -0.1 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GODREJCP | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GODREJCP |
| 116 | [DMART](stocks/DMART.md) | Avenue Supermarts Ltd. | Consumer Services | -0.1 | -0.2 | 49% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DMART | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → DMART |
| 117 | [TVSMOTOR](stocks/TVSMOTOR.md) | TVS Motor Company Ltd. | Automobile and Auto Components | -0.2 | -0.2 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TVSMOTOR | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → TVSMOTOR |
| 118 | [ABB](stocks/ABB.md) | ABB India Ltd. | Capital Goods | -0.1 | -0.2 | 52% | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → ABB | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ABB |
| 119 | [TATACAP](stocks/TATACAP.md) | Tata Capital Ltd. | Financial Services | -0.1 | -0.3 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATACAP |
| 122 | [DLF](stocks/DLF.md) | DLF Ltd. | Realty | -0.1 | -0.3 | 49% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DLF | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → DLF |
| 132 | [BOSCHLTD](stocks/BOSCHLTD.md) | Bosch Ltd. | Automobile and Auto Components | -0.3 | -0.5 | 52% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BOSCHLTD |
| 137 | [CUMMINSIND](stocks/CUMMINSIND.md) | Cummins India Ltd. | Capital Goods | -0.5 | -0.6 | 48% | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → CUMMINSIND | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → CUMMINSIND |
| 141 | [BAJAJHLDNG](stocks/BAJAJHLDNG.md) | Bajaj Holdings & Investment Ltd. | Financial Services | -0.1 | -0.6 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJHLDNG | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → BAJAJHLDNG |
| 147 | [MOTHERSON](stocks/MOTHERSON.md) | Samvardhana Motherson International Ltd. | Automobile and Auto Components | -0.1 | -0.7 | 47% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MOTHERSON | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MOTHERSON |
| 148 | [HDFCAMC](stocks/HDFCAMC.md) | HDFC Asset Management Company Ltd. | Financial Services | -0.2 | -0.7 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HDFCAMC | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → HDFCAMC |
| 154 | [BANKBARODA](stocks/BANKBARODA.md) | Bank of Baroda | Financial Services | -0.3 | -0.9 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKBARODA | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BANKBARODA |
| 159 | [CHOLAFIN](stocks/CHOLAFIN.md) | Cholamandalam Investment and Finance Company Ltd. | Financial Services | -0.6 | -1.0 | 49% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CHOLAFIN | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → CHOLAFIN |
| 164 | [TORNTPHARM](stocks/TORNTPHARM.md) | Torrent Pharmaceuticals Ltd. | Healthcare | -0.5 | -1.1 | 44% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TORNTPHARM | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TORNTPHARM |
| 166 | [CANBK](stocks/CANBK.md) | Canara Bank | Financial Services | -0.2 | -1.2 | 46% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CANBK | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → CANBK |
| 171 | [WIPRO](stocks/WIPRO.md) | Wipro Ltd. | Information Technology | -0.7 | -1.3 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → WIPRO | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → WIPRO |
| 172 | [IRFC](stocks/IRFC.md) | Indian Railway Finance Corporation Ltd. | Financial Services | -1.0 | -1.3 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IRFC | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IRFC |
| 174 | [LTM](stocks/LTM.md) | LTM Ltd. | Information Technology | -0.8 | -1.5 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTM | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → LTM |
| 176 | [ZYDUSLIFE](stocks/ZYDUSLIFE.md) | Zydus Lifesciences Ltd. | Healthcare | -0.2 | -1.5 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ZYDUSLIFE | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → ZYDUSLIFE |
| 180 | [VEDL](stocks/VEDL.md) | Vedanta Ltd. | Metals & Mining | -0.7 | -1.6 | 51% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VEDL | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC → VEDL |
| 183 | [HINDZINC](stocks/HINDZINC.md) | Hindustan Zinc Ltd. | Metals & Mining | -1.0 | -1.7 | 48% | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → HINDZINC | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC |
| 185 | [VAML](stocks/VAML.md) | Vedanta Aluminium Metal Ltd. | Metals & Mining | -1.5 | -1.7 | 48% | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → VAML | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → VAML |
| 193 | [MUTHOOTFIN](stocks/MUTHOOTFIN.md) | Muthoot Finance Ltd. | Financial Services | -0.5 | -2.3 | 47% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MUTHOOTFIN |

## Sector view (average of member stocks)
| industry | stocks | exp 3m | exp 12m | best | worst |
|---|---|---|---|---|---|
| Telecommunication | 4 | +0.9 | +2.8 | IDEA | TATACOMM |
| Power | 9 | +0.8 | +1.7 | JSWENERGY | NTPC |
| Oil Gas & Consumable Fuels | 9 | +0.3 | +1.2 | HINDPETRO | ONGC |
| Capital Goods | 24 | +0.1 | +0.6 | MAZDOCK | ASTRAL |
| Consumer Durables | 8 | +0.4 | +0.5 | DIXON | VOLTAS |
| Chemicals | 5 | +0.4 | +0.5 | SOLARINDS | PIIND |
| Construction Materials | 3 | +0.5 | +0.5 | ULTRACEMCO | GRASIM |
| Services | 4 | +0.2 | +0.1 | ADANIPORTS | CONCOR |
| Automobile and Auto Components | 14 | +0.1 | +0.0 | HEROMOTOCO | BAJAJ-AUTO |
| Construction | 2 | +0.2 | -0.1 | LT | RVNL |
| Realty | 6 | +0.2 | -0.1 | GODREJPROP | LODHA |
| Fast Moving Consumer Goods | 14 | -0.1 | -0.2 | BRITANNIA | UNITDSPR |
| Consumer Services | 12 | -0.2 | -0.3 | VMM | ETERNAL |
| Textiles | 1 | -0.6 | -0.3 | PAGEIND | PAGEIND |
| Financial Services | 48 | -0.1 | -0.4 | PAYTM | POLICYBZR |
| Healthcare | 15 | -0.2 | -0.6 | LAURUSLABS | FORTIS |
| Metals & Mining | 12 | -0.4 | -0.6 | JSWSTEEL | HINDCOPPER |
| Information Technology | 10 | -1.0 | -1.8 | WIPRO | PERSISTENT |

## Upcoming and risk events that matter most (impact if the event happens, % equity, raw)
| event | status | P(12m) | biggest winners | biggest losers |
|---|---|---|---|---|
| [Hormuz effectively closed for >2 weeks (Brent > $150)](events/EV_HORMUZ_FULL_CLOSURE.md) | risk_scenario | 0.05 | OIL +39.5, ONGC +31.1, COALINDIA +6.8, MCX +5.9, HINDZINC +5.8 | INDIGO -28.3, MOTILALOFS -27.4, ICICIAMC -24.0, IREDA -23.7, INDUSINDBK -21.9 |
| [AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes](events/EV_AI_CAPEX_RESET_RISK.md) | risk_scenario | 0.25 | TMPV +2.2, BOSCHLTD +2.1, MARUTI +2.1, JSWSTEEL +2.1, ASTRAL +2.0 | MOTILALOFS -21.5, POWERINDIA -19.4, ICICIAMC -18.2, NAUKRI -16.5, IREDA -16.2 |
| [Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027)](events/EV_INDIA_STAGFLATION_SCARE.md) | risk_scenario | 0.12 | VAML +0.2, NATIONALUM +0.2, UPL +0.2, OIL +0.2, TECHM +0.1 | INDUSINDBK -16.6, IDFCFIRSTB -15.6, YESBANK -15.5, AUBANK -12.8, SHRIRAMFIN -11.6 |
| [Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response)](events/EV_RUPEE_BREAK_98_RESERVE_STRESS.md) | risk_scenario | 0.18 | NATIONALUM +3.4, OIL +3.4, JSWSTEEL +3.3, ONGC +3.3, VAML +2.8 | MOTILALOFS -14.1, YESBANK -12.8, ADANIGREEN -11.2, IDEA -10.7, IREDA -10.6 |
| [Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action](events/EV_YEN_CARRY_UNWIND_RISK.md) | risk_scenario | 0.15 | HINDZINC +2.2, JSWSTEEL +2.1, NATIONALUM +2.0, ASTRAL +1.7, TATACONSUM +1.7 | MOTILALOFS -21.5, ICICIAMC -18.4, IREDA -16.4, 360ONE -15.8, INDUSINDBK -15.1 |
| [FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief](events/EV_FPI_INFLOW_REBOUND.md) | anticipated | 0.50 | MOTILALOFS +19.3, ICICIAMC +14.0, PAYTM +13.4, 360ONE +12.0, INDUSINDBK +11.5 | JSWSTEEL -1.7, OIL -1.5, ONGC -1.5, NATIONALUM -1.5, SAIL -1.3 |
| [Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110](events/EV_IRAN_TALKS_FAIL_ESCALATE.md) | risk_scenario | 0.25 | OIL +18.8, ONGC +14.6, MCX +3.1, COALINDIA +3.0, HINDZINC +2.6 | INDIGO -12.9, MOTILALOFS -10.5, BPCL -10.0, GMRAIRPORT -9.6, AXISBANK -9.2 |
| [Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil](events/EV_RUSSIA_TARIFF_ENFORCED.md) | risk_scenario | 0.15 | OIL +4.6, ONGC +3.2, JSWSTEEL +1.9, DRREDDY +1.5, PERSISTENT +1.5 | BPCL -8.8, APARINDS -7.2, BHARATFORG -7.1, MOTILALOFS -6.6, IOC -6.5 |
| [US recession (two negative quarters or NBER-style) beginning by mid-2027](events/EV_US_RECESSION_RISK_2027.md) | risk_scenario | 0.25 | SWIGGY +5.3, BSE +4.5, UPL +3.6, BPCL +3.2, ASTRAL +3.1 | LTM -13.7, MPHASIS -12.5, NAUKRI -12.4, WIPRO -11.8, COFORGE -11.5 |
| [US-Iran ceasefire/peace framework agreed and holding](events/EV_US_IRAN_CEASEFIRE_DEAL.md) | anticipated | 0.55 | INDIGO +8.4, GMRAIRPORT +6.4, AXISBANK +5.9, BPCL +5.3, HDFCBANK +5.1 | OIL -12.4, ONGC -9.8, MCX -2.3, COCHINSHIP -2.0, VAML -1.9 |
| [India-Pakistan military crisis (terror attack, cross-border strikes) after Op Sindoor (May 2025)](events/EV_INDIA_PAK_CRISIS.md) | risk_scenario | 0.09 | MAZDOCK +5.6, HAL +5.2, BDL +5.1, SOLARINDS +4.9, BEL +4.4 | MOTILALOFS -7.6, ICICIAMC -6.6, IREDA -6.3, 360ONE -5.6, INDUSINDBK -5.2 |
| [RBI MPC Apr 2027 (~8 Apr): cuts 25 bp (hiking cycle reversed)](events/EV_RBI_APR27_CUT25.md) | anticipated | 0.10 | GODREJPROP +4.6, IREDA +4.5, JSWENERGY +4.4, OBEROIRLTY +3.7, PRESTIGE +3.6 | LICHSGFIN -1.3, PAYTM -0.5, BANKINDIA -0.1 |
| [RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75%](events/EV_RBI_DEC26_HIKE25.md) | scheduled | 0.42 | LICHSGFIN +1.2, BANKINDIA +0.6, PAYTM +0.5, MAHABANK +0.0 | GODREJPROP -4.5, IREDA -4.3, JSWENERGY -4.2, M&MFIN -3.7, PRESTIGE -3.6 |
| [RBI MPC Feb 2027 (~5 Feb, just after Budget): hikes 25 bp](events/EV_RBI_FEB27_HIKE25.md) | scheduled | 0.27 | LICHSGFIN +1.7, BANKINDIA +0.7, PAYTM +0.6, MAHABANK +0.2, UNIONBANK +0.0 | GODREJPROP -4.4, JSWENERGY -3.8, IREDA -3.8, OBEROIRLTY -3.4, PRESTIGE -3.4 |
| [China property-sector credit event / sharp relapse (large developer or LGFV default)](events/EV_CHINA_PROPERTY_RELAPSE.md) | risk_scenario | 0.10 | JSWSTEEL +1.7, ASHOKLEY +1.7, MARUTI +1.5, VOLTAS +1.3, TMPV +1.2 | NMDC -11.7, IREDA -6.3, MOTILALOFS -5.9, ICICIAMC -5.7, 360ONE -5.0 |

## Events since June 2026 with the widest footprint (model impact, % equity, raw)
| event | winners | losers |
|---|---|---|
| [Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October](events/EV_FPI_RECORD_OUTFLOW_26.md) | JSWSTEEL +1.4, NATIONALUM +1.2, OIL +1.2, ONGC +1.2 | MOTILALOFS -15.6, PAYTM -11.0, ICICIAMC -10.8, 360ONE -9.3 |
| [CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74%](events/EV_CPI_REACCEL_SEP26.md) | PIIND +0.3, NATIONALUM +0.3, OIL +0.3, HINDCOPPER +0.2 | YESBANK -4.4, IREDA -4.3, TATACAP -3.9, BAJFINANCE -3.9 |
| [RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026)](events/EV_RBI_OCT26_HIKE25.md) | LICHSGFIN +1.2, BANKINDIA +0.6, PAYTM +0.5, MAHABANK +0.0 | GODREJPROP -4.5, IREDA -4.3, JSWENERGY -4.2, M&MFIN -3.7 |
| [RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high](events/EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26.md) | HDFCLIFE +0.7, MFSL +0.3, SBILIFE +0.3, RVNL +0.0 | ADANIGREEN -5.7, JIOFIN -5.3, IREDA -5.1, BANKINDIA -4.7 |
| [India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus](events/EV_GDP_Q1FY27_7_8.md) | TMCV +6.4, POWERINDIA +5.0, ASHOKLEY +4.6, POLYCAB +4.4 | PERSISTENT -0.6, TECHM -0.5, TCS -0.5, SUZLON -0.4 |
| [2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015](events/EV_SWMONSOON26_DEFICIT.md) | ADANIPOWER +1.4, COALINDIA +0.9, ENRIN +0.6, ULTRACEMCO +0.4 | INDUSINDBK -6.9, IDFCFIRSTB -6.1, YESBANK -5.1, M&MFIN -5.1 |
| [Fed delivers first hike in years (16 Sep 2026), new chair Warsh](events/EV_FED_SEP26_HIKE.md) | LICHSGFIN +0.4, OIL +0.2, MANKIND +0.2, JSWSTEEL +0.2 | BSE -5.2, SWIGGY -3.4, POLICYBZR -2.8, MOTILALOFS -2.4 |
| [US midterms (3 Nov 2026): Democrats win House and Senate](events/EV_US_MIDTERMS_DEM_SWEEP.md) | MOTILALOFS +3.6, PAYTM +2.5, ICICIAMC +2.5, BSE +2.3 | JSWSTEEL -0.4, OIL -0.3, ONGC -0.3, NATIONALUM -0.3 |
| [Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct)](events/EV_IRAN_WAR_HORMUZ_OIL.md) | OIL +5.3, ONGC +4.5, VAML +2.1, HINDPETRO +1.8 | INDIGO -3.9, AXISBANK -3.5, GMRAIRPORT -3.2, FEDERALBNK -3.1 |
| [US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k](events/EV_US_Q3_DATA_MIXED.md) | LTM +4.5, MPHASIS +4.4, PERSISTENT +4.1, HCLTECH +3.9 | BPCL -1.2, ASTRAL -0.9, SRF -0.8, UPL -0.7 |

## Drivers with the widest reach (see DRIVERS.md for the company lists)
| driver | standard shock | companies moved ≥0.5% | share via 2nd–4th order |
|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | 167.0 | 84% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | 135.0 | 13% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | 169.0 | 49% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | 118.0 | 50% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | 124.0 | 79% |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | 117.0 | 80% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | 183.0 | 36% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | 143.0 | 58% |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | 38.0 | 7% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | 157.0 | 97% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | 108.0 | 55% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | 92.0 | 50% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | 120.0 | 93% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | 144.0 | 64% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | 88.0 | 81% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | 103.0 | 9% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | 127.0 | 100% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | 123.0 | 99% |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | 40.0 | 40% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | 131.0 | 96% |

## Strongest 3rd- and 4th-order chains from upcoming/risk events (expected 12m = probability × impact)
| company | order | chain | impact if event | expected 12m |
|---|---|---|---|---|
| POWERINDIA | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | -1.03% | -0.70% |
| SAIL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → SAIL | +1.69% | +0.59% |
| GVT&D | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → GVT&D | -0.77% | -0.53% |
| FEDERALBNK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.72% | +0.49% |
| COCHINSHIP | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → C_RED_SEA → F_SHIPPING_RATES → COCHINSHIP | -0.88% | -0.48% |
| SAIL | 4 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL | +1.33% | +0.46% |
| HINDZINC | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_GOLD → F_SILVER → HINDZINC | -0.84% | -0.46% |
| CGPOWER | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | -0.64% | -0.44% |
| POWERINDIA | 3 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | -0.52% | -0.44% |
| INDUSINDBK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +0.64% | +0.44% |
| HYUNDAI | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.63% | +0.43% |
| SAIL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → SAIL | -0.78% | -0.39% |
| AUBANK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → AUBANK | +0.56% | +0.38% |
| IDFCFIRSTB | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +0.56% | +0.38% |
| TATACAP | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → TATACAP | +0.56% | +0.38% |
| LICHSGFIN | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → LICHSGFIN | +0.56% | +0.38% |
| YESBANK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_GDP_IN → YESBANK | +0.54% | +0.37% |
| TMCV | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_GDP_IN → TMCV | +0.54% | +0.37% |
| FEDERALBNK | 3 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.52% | +0.36% |
| JINDALSTEL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → JINDALSTEL | -0.72% | -0.36% |
| GROWW | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_SEBI_DERIVATIVES → GROWW | -0.72% | -0.36% |
| BSE | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_SEBI_DERIVATIVES → BSE | -0.72% | -0.36% |
| ADANIPOWER | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_POWER_PRICE_IN → ADANIPOWER | -0.53% | -0.36% |
| JSWSTEEL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → JSWSTEEL | +1.01% | +0.35% |
| KEI | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → KEI | -0.52% | -0.35% |

## Strongest 2nd–4th-order chains from what already moved since 1 June 2026 (raw model impact)
| company | order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|---|
| VEDL | 2 | F_SILVER → HINDZINC → VEDL | -2.50 | observed | -5.24% |
| POWERINDIA | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | +1.20 | events | +2.30% |
| GVT&D | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → GVT&D | +1.20 | events | +1.73% |
| SBICARD | 2 | F_MONSOON → F_UNSECURED_STRESS → SBICARD | -1.56 | events | -1.50% |
| INDUSINDBK | 2 | F_MONSOON → F_UNSECURED_STRESS → INDUSINDBK | -1.56 | events | -1.50% |
| FEDERALBNK | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.50 | events | +1.44% |
| CGPOWER | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | +1.20 | events | +1.44% |
| CHOLAFIN | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → CHOLAFIN | +0.50 | events | +1.28% |
| INDUSINDBK | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +0.50 | events | +1.28% |
| IREDA | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → IREDA | +0.50 | events | +1.28% |
| IDFCFIRSTB | 2 | F_MONSOON → F_UNSECURED_STRESS → IDFCFIRSTB | -1.56 | events | -1.25% |
| KALYANKJIL | 2 | F_GOLD → F_GOLD_DEMAND_IN → KALYANKJIL | -1.05 | observed | +1.17% |
| ENRIN | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ENRIN | +0.60 | director_override | +1.15% |
| APARINDS | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → APARINDS | +1.20 | events | +1.15% |
| POLYCAB | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POLYCAB | +1.20 | events | +1.15% |
| KEI | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → KEI | +1.20 | events | +1.15% |
| CANBK | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → CANBK | +0.50 | events | +1.12% |
| IDFCFIRSTB | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +0.50 | events | +1.12% |
| LICHSGFIN | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → LICHSGFIN | +0.50 | events | +1.12% |
| AUBANK | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → AUBANK | +0.50 | events | +1.12% |
| TATACAP | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → TATACAP | +0.50 | events | +1.12% |
| M&MFIN | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → M&MFIN | +0.50 | events | +0.96% |
| ABCAPITAL | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → ABCAPITAL | +0.50 | events | +0.96% |
| BANKBARODA | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → BANKBARODA | +0.50 | events | +0.96% |
| LTF | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → LTF | +0.50 | events | +0.88% |

## Files
- `RANKINGS.md` — all 200 stocks; `stocks/<TICKER>.md` — per-stock deep dive (drivers by order, events, chains, analyst profile); `events/<EVENT>.md` — per-event winners/losers by order; `EVENTS.md`; `DRIVERS.md`.
- Data: `results/rankings.csv`, `results/sensitivity_by_order.csv`, `results/event_impacts.csv`, `results/edges_all.csv`.
- Method: `PLAN.md`, `docs/AGENT_SPEC.md`; review trail: `review/`, `graph/*overrides*.json`.
