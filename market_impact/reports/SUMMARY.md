# Market Impact Graph — Nifty 200 second-to-fourth-order effects (analysis date 2026-11-05)

**What this is.** A causal exposure network: events → macro/commodity/policy/geopolitical drivers → companies, with 2808 weighted edges among 459 nodes (200 company profiles, 161 events of which 62 already occurred since June 2026). Effects propagate up to four hops, damped by order, with double-count controls (clamping, overlap damping, link semantics).

**How to read the numbers.** Expected returns are *scenario-implied*, beta-adjusted and relative to the Nifty 200 average: probability-weighted impacts of upcoming and risk events through the graph (half assumed already priced) plus company-specific catalysts. They are not validated forecasts; the rankings are frozen in `ledger/` and will be scored against realised returns and a momentum baseline.

**What the in-sample check showed.** We first also credited the part of June–November driver moves the graph said was not yet in prices. Across 198 stocks the graph's June–November impact correlated **−0.34** with realised market-adjusted moves (agent-estimated event shocks −0.41; market-observed drivers +0.10; within industries −0.16), and eight red-team reviewers found most large 'unpriced' items were stock-specific news the graph lacks (results misses, regulation, competition). That component is therefore excluded from the headline and kept only as a diagnostic. The graph's value is the exposure map — which drivers and events hit which company, by causal order — not a proven return forecast.

## Top 20 (12-month, beta-adjusted, relative)
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 1 | [HINDPETRO](stocks/HINDPETRO.md) | Hindustan Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +3.5 | +9.7 | 70% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → HINDPETRO |
| 2 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +3.4 | +7.0 | 72% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → IOC |
| 3 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +4.7 | +6.5 | 70% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 4 | [JINDALSTEL](stocks/JINDALSTEL.md) | Jindal Steel Ltd. | Metals & Mining | +3.4 | +5.4 | 65% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL |
| 5 | [BDL](stocks/BDL.md) | Bharat Dynamics Ltd. | Capital Goods | +1.9 | +4.7 | 48% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BDL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BDL |
| 6 | [LAURUSLABS](stocks/LAURUSLABS.md) | Laurus Labs Ltd. | Healthcare | +1.5 | +4.3 | 57% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LAURUSLABS | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → LAURUSLABS |
| 7 | [IDEA](stocks/IDEA.md) | Vodafone Idea Ltd. | Telecommunication | +0.1 | +4.1 | 60% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA |
| 8 | [NMDC](stocks/NMDC.md) | NMDC Ltd. | Metals & Mining | +2.3 | +3.8 | 50% | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_IRON_ORE → NMDC | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_IRON_ORE → NMDC |
| 9 | [SAIL](stocks/SAIL.md) | Steel Authority of India Ltd. | Metals & Mining | +2.4 | +3.7 | 70% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → SAIL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL |
| 10 | [BPCL](stocks/BPCL.md) | Bharat Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +1.8 | +3.6 | 68% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL |
| 11 | [JSWSTEEL](stocks/JSWSTEEL.md) | JSW Steel Ltd. | Metals & Mining | +1.4 | +3.5 | 52% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JSWSTEEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JSWSTEEL |
| 12 | [BEL](stocks/BEL.md) | Bharat Electronics Ltd. | Capital Goods | +2.5 | +3.2 | 78% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BEL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BEL |
| 13 | [UPL](stocks/UPL.md) | UPL Ltd. | Chemicals | +0.9 | +3.1 | 52% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → UPL | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → UPL |
| 14 | [TATASTEEL](stocks/TATASTEEL.md) | Tata Steel Ltd. | Metals & Mining | +1.4 | +3.0 | 55% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → TATASTEEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → TATASTEEL |
| 15 | [HAL](stocks/HAL.md) | Hindustan Aeronautics Ltd. | Capital Goods | +2.1 | +3.0 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → HAL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HAL |
| 16 | [RELIANCE](stocks/RELIANCE.md) | Reliance Industries Ltd. | Oil Gas & Consumable Fuels | +0.4 | +2.7 | 45% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → RELIANCE | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → RELIANCE |
| 17 | [COALINDIA](stocks/COALINDIA.md) | Coal India Ltd. | Oil Gas & Consumable Fuels | +1.8 | +2.7 | 52% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → COALINDIA | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA |
| 18 | [BHARTIARTL](stocks/BHARTIARTL.md) | Bharti Airtel Ltd. | Telecommunication | +1.3 | +2.6 | 60% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → BHARTIARTL | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BHARTIARTL |
| 19 | [M&M](stocks/M&M.md) | Mahindra & Mahindra Ltd. | Automobile and Auto Components | +1.7 | +2.6 | 45% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → M&M | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → M&M |
| 20 | [TMCV](stocks/TMCV.md) | Tata Motors Ltd. | Capital Goods | +1.3 | +2.5 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TMCV | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TMCV |

## Bottom 20
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 200 | [BAJFINANCE](stocks/BAJFINANCE.md) | Bajaj Finance Ltd. | Financial Services | -4.6 | -7.6 | 28% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJFINANCE | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BAJFINANCE |
| 199 | [TATACAP](stocks/TATACAP.md) | Tata Capital Ltd. | Financial Services | -3.7 | -6.7 | 28% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACAP |
| 198 | [BAJAJFINSV](stocks/BAJAJFINSV.md) | Bajaj Finserv Ltd. | Financial Services | -3.7 | -6.2 | 35% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJFINSV | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BAJAJFINSV |
| 197 | [YESBANK](stocks/YESBANK.md) | Yes Bank Ltd. | Financial Services | -4.2 | -6.0 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → YESBANK | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → YESBANK |
| 196 | [JIOFIN](stocks/JIOFIN.md) | Jio Financial Services Ltd. | Financial Services | -3.2 | -5.6 | 32% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JIOFIN | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → JIOFIN |
| 195 | [IREDA](stocks/IREDA.md) | Indian Renewable Energy Development Agency Ltd. | Financial Services | -2.5 | -5.4 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IREDA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IREDA |
| 194 | [ETERNAL](stocks/ETERNAL.md) | Eternal Ltd. | Consumer Services | -2.7 | -4.8 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ETERNAL | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → ETERNAL |
| 193 | [PERSISTENT](stocks/PERSISTENT.md) | Persistent Systems Ltd. | Information Technology | -1.3 | -4.6 | 30% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → PERSISTENT | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PERSISTENT |
| 192 | [POLICYBZR](stocks/POLICYBZR.md) | PB Fintech Ltd. | Financial Services | -3.3 | -4.6 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POLICYBZR | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → POLICYBZR |
| 191 | [LENSKART](stocks/LENSKART.md) | Lenskart Solutions Ltd. | Consumer Services | -2.9 | -4.3 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LENSKART | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LENSKART |
| 190 | [AUBANK](stocks/AUBANK.md) | AU Small Finance Bank Ltd. | Financial Services | -2.8 | -4.0 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AUBANK | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → AUBANK |
| 189 | [GROWW](stocks/GROWW.md) | Billionbrains Garage Ventures Ltd. | Financial Services | -1.2 | -4.0 | 35% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → GROWW | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → GROWW |
| 188 | [INFY](stocks/INFY.md) | Infosys Ltd. | Information Technology | -1.9 | -3.6 | 42% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_GENAI_SERVICES → INFY | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → INFY |
| 187 | [HCLTECH](stocks/HCLTECH.md) | HCL Technologies Ltd. | Information Technology | -1.4 | -3.3 | 50% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → HCLTECH | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → HCLTECH |
| 186 | [ICICIAMC](stocks/ICICIAMC.md) | ICICI Prudential Asset Management Company Ltd. | Financial Services | -1.7 | -3.1 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ICICIAMC | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ICICIAMC |
| 185 | [IDFCFIRSTB](stocks/IDFCFIRSTB.md) | IDFC First Bank Ltd. | Financial Services | -1.0 | -3.0 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IDFCFIRSTB | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → IDFCFIRSTB |
| 184 | [MUTHOOTFIN](stocks/MUTHOOTFIN.md) | Muthoot Finance Ltd. | Financial Services | -1.6 | -3.0 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MUTHOOTFIN |
| 183 | [LTM](stocks/LTM.md) | LTM Ltd. | Information Technology | -1.1 | -3.0 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTM | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → LTM |
| 182 | [WIPRO](stocks/WIPRO.md) | Wipro Ltd. | Information Technology | -1.1 | -2.9 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → WIPRO | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → WIPRO |
| 181 | [MPHASIS](stocks/MPHASIS.md) | MphasiS Ltd. | Information Technology | -1.1 | -2.9 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MPHASIS | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MPHASIS |

## Nifty Next 50 — all 50 ranked
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 2 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +3.4 | +7.0 | 72% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → IOC |
| 3 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +4.7 | +6.5 | 70% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 4 | [JINDALSTEL](stocks/JINDALSTEL.md) | Jindal Steel Ltd. | Metals & Mining | +3.4 | +5.4 | 65% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL |
| 7 | [IDEA](stocks/IDEA.md) | Vodafone Idea Ltd. | Telecommunication | +0.1 | +4.1 | 60% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA |
| 10 | [BPCL](stocks/BPCL.md) | Bharat Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +1.8 | +3.6 | 68% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL |
| 15 | [HAL](stocks/HAL.md) | Hindustan Aeronautics Ltd. | Capital Goods | +2.1 | +3.0 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → HAL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HAL |
| 20 | [TMCV](stocks/TMCV.md) | Tata Motors Ltd. | Capital Goods | +1.3 | +2.5 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TMCV | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TMCV |
| 23 | [GAIL](stocks/GAIL.md) | GAIL (India) Ltd. | Oil Gas & Consumable Fuels | +1.0 | +2.3 | 57% | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → GAIL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GAIL |
| 28 | [POWERINDIA](stocks/POWERINDIA.md) | Hitachi Energy India Ltd. | Capital Goods | +0.9 | +2.1 | 57% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POWERINDIA | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA |
| 29 | [SOLARINDS](stocks/SOLARINDS.md) | Solar Industries India Ltd. | Chemicals | +1.3 | +2.1 | 60% | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → SOLARINDS | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SOLARINDS |
| 32 | [TATAPOWER](stocks/TATAPOWER.md) | Tata Power Co. Ltd. | Power | +0.8 | +2.0 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATAPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATAPOWER |
| 33 | [ENRIN](stocks/ENRIN.md) | Siemens Energy India Ltd. | Capital Goods | +1.9 | +2.0 | 40% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → ENRIN | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN |
| 42 | [TVSMOTOR](stocks/TVSMOTOR.md) | TVS Motor Company Ltd. | Automobile and Auto Components | +0.3 | +1.5 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TVSMOTOR | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → TVSMOTOR |
| 45 | [DIVISLAB](stocks/DIVISLAB.md) | Divi's Laboratories Ltd. | Healthcare | +0.6 | +1.4 | 65% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DIVISLAB | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → DIVISLAB |
| 46 | [VBL](stocks/VBL.md) | Varun Beverages Ltd. | Fast Moving Consumer Goods | +0.7 | +1.4 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VBL | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → VBL |
| 48 | [PNB](stocks/PNB.md) | Punjab National Bank | Financial Services | +1.4 | +1.3 | 55% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PNB | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → PNB |
| 49 | [ADANIENSOL](stocks/ADANIENSOL.md) | Adani Energy Solutions Ltd. | Power | +1.1 | +1.3 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENSOL | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIENSOL |
| 52 | [UNIONBANK](stocks/UNIONBANK.md) | Union Bank of India | Financial Services | +1.4 | +1.2 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → UNIONBANK | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → UNIONBANK |
| 58 | [HINDZINC](stocks/HINDZINC.md) | Hindustan Zinc Ltd. | Metals & Mining | +0.1 | +1.2 | 42% | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → HINDZINC | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC |
| 61 | [ADANIPOWER](stocks/ADANIPOWER.md) | Adani Power Ltd. | Power | +0.3 | +1.1 | 52% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIPOWER |
| 62 | [POLYCAB](stocks/POLYCAB.md) | Polycab India Ltd. | Capital Goods | +0.1 | +1.1 | 42% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POLYCAB | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → POLYCAB |
| 64 | [GODREJCP](stocks/GODREJCP.md) | Godrej Consumer Products Ltd. | Fast Moving Consumer Goods | +0.4 | +1.0 | 57% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GODREJCP | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GODREJCP |
| 77 | [BRITANNIA](stocks/BRITANNIA.md) | Britannia Industries Ltd. | Fast Moving Consumer Goods | +0.6 | +0.8 | 57% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BRITANNIA | EV_WHEAT27_CROP_BELOW ⇒ F_WHEAT → BRITANNIA |
| 79 | [ABB](stocks/ABB.md) | ABB India Ltd. | Capital Goods | +0.5 | +0.8 | 45% | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → ABB | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ABB |
| 83 | [AMBUJACEM](stocks/AMBUJACEM.md) | Ambuja Cements Ltd. | Construction Materials | +0.7 | +0.7 | 55% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → AMBUJACEM | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → AMBUJACEM |
| 86 | [CGPOWER](stocks/CGPOWER.md) | CG Power and Industrial Solutions Ltd. | Capital Goods | +0.8 | +0.6 | 55% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → CGPOWER |
| 92 | [HDFCAMC](stocks/HDFCAMC.md) | HDFC Asset Management Company Ltd. | Financial Services | +0.4 | +0.4 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HDFCAMC | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → HDFCAMC |
| 93 | [ADANIGREEN](stocks/ADANIGREEN.md) | Adani Green Energy Ltd. | Power | -0.3 | +0.4 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIGREEN | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIGREEN |
| 105 | [VAML](stocks/VAML.md) | Vedanta Aluminium Metal Ltd. | Metals & Mining | -0.6 | +0.0 | 42% | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → VAML | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → VAML |
| 109 | [PIDILITIND](stocks/PIDILITIND.md) | Pidilite Industries Ltd. | Chemicals | -0.1 | -0.0 | 45% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → PIDILITIND | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PIDILITIND |
| 111 | [BANKBARODA](stocks/BANKBARODA.md) | Bank of Baroda | Financial Services | +0.3 | -0.2 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKBARODA | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BANKBARODA |
| 119 | [HYUNDAI](stocks/HYUNDAI.md) | Hyundai Motor India Ltd. | Automobile and Auto Components | -0.4 | -0.3 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HYUNDAI | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → HYUNDAI |
| 121 | [MOTHERSON](stocks/MOTHERSON.md) | Samvardhana Motherson International Ltd. | Automobile and Auto Components | -0.0 | -0.3 | 48% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MOTHERSON | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MOTHERSON |
| 122 | [VEDL](stocks/VEDL.md) | Vedanta Ltd. | Metals & Mining | -0.5 | -0.3 | 57% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VEDL | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC → VEDL |
| 123 | [IRFC](stocks/IRFC.md) | Indian Railway Finance Corporation Ltd. | Financial Services | -0.3 | -0.4 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IRFC | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IRFC |
| 127 | [SIEMENS](stocks/SIEMENS.md) | Siemens Ltd. | Capital Goods | +0.1 | -0.4 | 35% | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → SIEMENS | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → SIEMENS |
| 131 | [PFC](stocks/PFC.md) | Power Finance Corporation Ltd. | Financial Services | -1.0 | -0.5 | 62% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PFC | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PFC |
| 132 | [CANBK](stocks/CANBK.md) | Canara Bank | Financial Services | +0.3 | -0.5 | 60% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CANBK | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → CANBK |
| 137 | [DLF](stocks/DLF.md) | DLF Ltd. | Realty | -0.8 | -0.7 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DLF | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → DLF |
| 141 | [BOSCHLTD](stocks/BOSCHLTD.md) | Bosch Ltd. | Automobile and Auto Components | -0.8 | -0.9 | 62% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BOSCHLTD |
| 151 | [DMART](stocks/DMART.md) | Avenue Supermarts Ltd. | Consumer Services | -1.0 | -1.2 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DMART | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → DMART |
| 153 | [TORNTPHARM](stocks/TORNTPHARM.md) | Torrent Pharmaceuticals Ltd. | Healthcare | -1.1 | -1.5 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TORNTPHARM | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TORNTPHARM |
| 158 | [ZYDUSLIFE](stocks/ZYDUSLIFE.md) | Zydus Lifesciences Ltd. | Healthcare | -0.5 | -1.6 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ZYDUSLIFE | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → ZYDUSLIFE |
| 162 | [CHOLAFIN](stocks/CHOLAFIN.md) | Cholamandalam Investment and Finance Company Ltd. | Financial Services | -1.3 | -2.0 | 32% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CHOLAFIN | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → CHOLAFIN |
| 164 | [CUMMINSIND](stocks/CUMMINSIND.md) | Cummins India Ltd. | Capital Goods | -0.9 | -2.2 | 60% | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → CUMMINSIND | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → CUMMINSIND |
| 167 | [BAJAJHLDNG](stocks/BAJAJHLDNG.md) | Bajaj Holdings & Investment Ltd. | Financial Services | -1.0 | -2.2 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJHLDNG | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → BAJAJHLDNG |
| 182 | [WIPRO](stocks/WIPRO.md) | Wipro Ltd. | Information Technology | -1.1 | -2.9 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → WIPRO | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → WIPRO |
| 183 | [LTM](stocks/LTM.md) | LTM Ltd. | Information Technology | -1.1 | -3.0 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTM | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → LTM |
| 184 | [MUTHOOTFIN](stocks/MUTHOOTFIN.md) | Muthoot Finance Ltd. | Financial Services | -1.6 | -3.0 | 48% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MUTHOOTFIN |
| 199 | [TATACAP](stocks/TATACAP.md) | Tata Capital Ltd. | Financial Services | -3.7 | -6.7 | 28% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACAP |

## Sector view (average of member stocks)
| industry | stocks | exp 3m | exp 12m | best | worst |
|---|---|---|---|---|---|
| Oil Gas & Consumable Fuels | 9 | +1.4 | +3.3 | HINDPETRO | ATGL |
| Metals & Mining | 12 | +1.1 | +2.0 | JINDALSTEL | VEDL |
| Chemicals | 5 | +1.0 | +1.7 | UPL | PIDILITIND |
| Telecommunication | 4 | +0.0 | +1.5 | IDEA | TATACOMM |
| Capital Goods | 24 | +0.9 | +1.4 | MAZDOCK | CUMMINSIND |
| Power | 9 | +0.1 | +1.0 | NLCINDIA | JSWENERGY |
| Automobile and Auto Components | 14 | +0.4 | +0.8 | M&M | BOSCHLTD |
| Construction Materials | 3 | +0.5 | +0.8 | ULTRACEMCO | GRASIM |
| Consumer Durables | 8 | +0.5 | +0.6 | KALYANKJIL | VOLTAS |
| Fast Moving Consumer Goods | 14 | +0.2 | +0.6 | VBL | UNITDSPR |
| Services | 4 | +0.3 | +0.3 | ADANIPORTS | GMRAIRPORT |
| Construction | 2 | +0.8 | +0.3 | LT | RVNL |
| Healthcare | 15 | -0.3 | -0.2 | LAURUSLABS | FORTIS |
| Realty | 6 | -0.8 | -0.9 | LODHA | PRESTIGE |
| Consumer Services | 12 | -0.8 | -1.1 | VMM | ETERNAL |
| Textiles | 1 | -1.2 | -1.2 | PAGEIND | PAGEIND |
| Financial Services | 48 | -0.8 | -1.8 | LICHSGFIN | BAJFINANCE |
| Information Technology | 10 | -1.3 | -3.1 | TECHM | PERSISTENT |

## Upcoming and risk events that matter most (impact if the event happens, % equity, raw)
| event | status | P(12m) | biggest winners | biggest losers |
|---|---|---|---|---|
| [Hormuz effectively closed for >2 weeks (Brent > $150)](events/EV_HORMUZ_FULL_CLOSURE.md) | risk_scenario | 0.05 | OIL +39.6, ONGC +31.2, COALINDIA +7.0, MCX +5.9, HINDZINC +5.9 | INDIGO -28.2, MOTILALOFS -27.4, ICICIAMC -23.9, JIOFIN -23.3, IREDA -23.0 |
| [AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes](events/EV_AI_CAPEX_RESET_RISK.md) | risk_scenario | 0.25 | TMPV +2.2, BOSCHLTD +2.1, MARUTI +2.1, JSWSTEEL +2.1, ASTRAL +2.0 | MOTILALOFS -21.5, POWERINDIA -19.4, ICICIAMC -18.2, JIOFIN -16.9, NAUKRI -16.5 |
| [Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response)](events/EV_RUPEE_BREAK_98_RESERVE_STRESS.md) | risk_scenario | 0.18 | NATIONALUM +3.4, OIL +3.4, JSWSTEEL +3.3, ONGC +3.3, VAML +2.8 | YESBANK -15.8, MOTILALOFS -14.1, BAJFINANCE -12.3, TATACAP -11.3, ADANIGREEN -11.2 |
| [Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action](events/EV_YEN_CARRY_UNWIND_RISK.md) | risk_scenario | 0.15 | HINDZINC +2.2, JSWSTEEL +2.1, NATIONALUM +2.0, TATACONSUM +1.7, ASTRAL +1.7 | MOTILALOFS -21.5, ICICIAMC -18.4, JIOFIN -17.4, IREDA -16.4, 360ONE -15.8 |
| [Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027)](events/EV_INDIA_STAGFLATION_SCARE.md) | risk_scenario | 0.12 | VAML +0.2, NATIONALUM +0.2, UPL +0.2, OIL +0.2, TECHM +0.1 | YESBANK -17.8, INDUSINDBK -16.6, IDFCFIRSTB -15.6, AUBANK -13.8, TATACAP -13.4 |
| [FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief](events/EV_FPI_INFLOW_REBOUND.md) | anticipated | 0.50 | MOTILALOFS +19.4, ICICIAMC +14.0, PAYTM +13.4, 360ONE +12.0, INDUSINDBK +11.5 | JSWSTEEL -1.7, OIL -1.5, ONGC -1.5, NATIONALUM -1.5, SAIL -1.3 |
| [Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110](events/EV_IRAN_TALKS_FAIL_ESCALATE.md) | risk_scenario | 0.25 | OIL +18.8, ONGC +14.6, COALINDIA +3.1, MCX +3.1, HINDZINC +2.6 | INDIGO -12.9, MOTILALOFS -10.5, BPCL -10.0, HINDPETRO -9.8, GMRAIRPORT -9.5 |
| [Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil](events/EV_RUSSIA_TARIFF_ENFORCED.md) | risk_scenario | 0.15 | OIL +4.7, ONGC +3.3, JSWSTEEL +2.0, JINDALSTEL +1.7, DRREDDY +1.6 | BPCL -8.7, APARINDS -7.2, BHARATFORG -7.0, MOTILALOFS -6.6, IOC -6.4 |
| [US recession (two negative quarters or NBER-style) beginning by mid-2027](events/EV_US_RECESSION_RISK_2027.md) | risk_scenario | 0.25 | SWIGGY +5.4, BSE +4.6, UPL +3.6, ASTRAL +3.2, BPCL +3.2 | LTM -13.7, MPHASIS -12.5, NAUKRI -12.4, WIPRO -11.8, COFORGE -11.4 |
| [US-Iran ceasefire/peace framework agreed and holding](events/EV_US_IRAN_CEASEFIRE_DEAL.md) | anticipated | 0.55 | INDIGO +8.3, GMRAIRPORT +6.4, HINDPETRO +6.0, AXISBANK +5.8, BPCL +5.3 | OIL -12.5, ONGC -9.8, MCX -2.3, COCHINSHIP -2.1, VAML -1.9 |
| [India-Pakistan military crisis (terror attack, cross-border strikes) after Op Sindoor (May 2025)](events/EV_INDIA_PAK_CRISIS.md) | risk_scenario | 0.09 | MAZDOCK +5.6, HAL +5.2, BDL +5.1, SOLARINDS +4.9, BEL +4.4 | MOTILALOFS -7.6, JIOFIN -6.6, ICICIAMC -6.6, IREDA -6.3, MEESHO -5.8 |
| [RBI MPC Apr 2027 (~8 Apr): cuts 25 bp (hiking cycle reversed)](events/EV_RBI_APR27_CUT25.md) | anticipated | 0.10 | YESBANK +5.5, TATACAP +5.3, PRESTIGE +5.2, BAJFINANCE +5.2, GODREJPROP +4.6 | LICHSGFIN -1.3, PAYTM -0.5, BANKINDIA -0.1 |
| [RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75%](events/EV_RBI_DEC26_HIKE25.md) | scheduled | 0.42 | LICHSGFIN +1.2, BANKINDIA +0.6, PAYTM +0.5, MAHABANK +0.0 | BAJFINANCE -5.4, TATACAP -5.3, PRESTIGE -5.2, YESBANK -5.1, GODREJPROP -4.5 |
| [RBI MPC Feb 2027 (~5 Feb, just after Budget): hikes 25 bp](events/EV_RBI_FEB27_HIKE25.md) | scheduled | 0.27 | LICHSGFIN +1.7, BANKINDIA +0.7, PAYTM +0.6, MAHABANK +0.2, UNIONBANK +0.0 | PRESTIGE -5.0, YESBANK -4.8, TATACAP -4.7, BAJFINANCE -4.6, GODREJPROP -4.4 |
| [China property-sector credit event / sharp relapse (large developer or LGFV default)](events/EV_CHINA_PROPERTY_RELAPSE.md) | risk_scenario | 0.10 | JSWSTEEL +1.7, ASHOKLEY +1.7, JINDALSTEL +1.5, MARUTI +1.4, VOLTAS +1.3 | NMDC -11.7, JIOFIN -6.5, IREDA -6.4, MOTILALOFS -5.9, ICICIAMC -5.8 |

## Events since June 2026 with the widest footprint (model impact, % equity, raw)
| event | winners | losers |
|---|---|---|
| [Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October](events/EV_FPI_RECORD_OUTFLOW_26.md) | JSWSTEEL +1.3, NATIONALUM +1.2, OIL +1.2, ONGC +1.2 | MOTILALOFS -15.7, PAYTM -11.0, ICICIAMC -10.8, 360ONE -9.3 |
| [CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74%](events/EV_CPI_REACCEL_SEP26.md) | PIIND +0.3, NATIONALUM +0.3, OIL +0.3, HINDCOPPER +0.3 | YESBANK -6.1, BAJFINANCE -5.4, TATACAP -5.3, AUBANK -4.3 |
| [RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026)](events/EV_RBI_OCT26_HIKE25.md) | LICHSGFIN +1.2, BANKINDIA +0.6, PAYTM +0.5, MAHABANK +0.0 | BAJFINANCE -5.4, TATACAP -5.3, PRESTIGE -5.2, YESBANK -5.1 |
| [RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high](events/EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26.md) | HDFCLIFE +0.7, SBILIFE +0.3, MFSL +0.3, RVNL +0.1 | YESBANK -6.1, ADANIGREEN -5.7, BAJFINANCE -5.5, JIOFIN -5.3 |
| [India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus](events/EV_GDP_Q1FY27_7_8.md) | TMCV +6.2, POWERINDIA +4.6, ASHOKLEY +4.4, UNIONBANK +4.2 | PRESTIGE -1.0, JSWENERGY -1.0, SUZLON -0.8, PERSISTENT -0.8 |
| [2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015](events/EV_SWMONSOON26_DEFICIT.md) | ADANIPOWER +1.5, COALINDIA +1.1, ENRIN +0.9, WAAREEENER +0.6 | INDUSINDBK -6.7, IDFCFIRSTB -5.9, YESBANK -4.9, M&MFIN -4.8 |
| [Fed delivers first hike in years (16 Sep 2026), new chair Warsh](events/EV_FED_SEP26_HIKE.md) | LICHSGFIN +0.4, OIL +0.2, MANKIND +0.2, JSWSTEEL +0.2 | BSE -5.2, SWIGGY -3.4, POLICYBZR -2.8, MOTILALOFS -2.4 |
| [US midterms (3 Nov 2026): Democrats win House and Senate](events/EV_US_MIDTERMS_DEM_SWEEP.md) | MOTILALOFS +3.6, PAYTM +2.5, ICICIAMC +2.5, BSE +2.3 | JSWSTEEL -0.4, OIL -0.3, ONGC -0.3, NATIONALUM -0.3 |
| [Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct)](events/EV_IRAN_WAR_HORMUZ_OIL.md) | OIL +5.3, ONGC +4.5, VAML +2.1, NATIONALUM +1.8 | INDIGO -3.9, AXISBANK -3.5, GMRAIRPORT -3.2, FEDERALBNK -3.1 |
| [US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k](events/EV_US_Q3_DATA_MIXED.md) | LTM +4.5, MPHASIS +4.4, PERSISTENT +4.1, HCLTECH +3.9 | BPCL -1.2, ASTRAL -1.0, SRF -0.8, UPL -0.7 |

## Drivers with the widest reach (see DRIVERS.md for the company lists)
| driver | standard shock | companies moved ≥0.5% | share via 2nd–4th order |
|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | 166.0 | 82% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | 135.0 | 13% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | 171.0 | 51% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | 183.0 | 34% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | 143.0 | 55% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | 118.0 | 79% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | 116.0 | 49% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | 156.0 | 97% |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | 109.0 | 80% |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | 38.0 | 8% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | 96.0 | 55% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | 86.0 | 48% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | 143.0 | 63% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | 103.0 | 10% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | 114.0 | 93% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | 127.0 | 100% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | 81.0 | 80% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | 124.0 | 99% |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | 40.0 | 40% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | 125.0 | 96% |

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
| PRESTIGE | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_REPO_IN → PRESTIGE | -0.64% | -0.44% |
| HYUNDAI | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.63% | +0.43% |
| JINDALSTEL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → JINDALSTEL | -0.83% | -0.41% |
| SAIL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → SAIL | -0.78% | -0.39% |
| AUBANK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → AUBANK | +0.56% | +0.38% |
| IDFCFIRSTB | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +0.56% | +0.38% |
| TATACAP | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → TATACAP | +0.56% | +0.38% |
| LICHSGFIN | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → LICHSGFIN | +0.56% | +0.38% |
| GODREJPROP | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_REPO_IN → GODREJPROP | -0.56% | -0.38% |
| YESBANK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_GDP_IN → YESBANK | +0.54% | +0.37% |
| TMCV | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_GDP_IN → TMCV | +0.54% | +0.37% |
| FEDERALBNK | 3 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.52% | +0.36% |
| GROWW | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_SEBI_DERIVATIVES → GROWW | -0.72% | -0.36% |
| BSE | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_SEBI_DERIVATIVES → BSE | -0.72% | -0.36% |
| ADANIPOWER | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_POWER_PRICE_IN → ADANIPOWER | -0.53% | -0.36% |

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
