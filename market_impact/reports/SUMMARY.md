# Market Impact Graph — Nifty 200 second-to-fourth-order effects (analysis date 2026-11-05)

**What this is.** A causal exposure network: events → macro/commodity/policy/geopolitical drivers → companies, with 2808 weighted edges among 459 nodes (200 company profiles, 161 events of which 61 already occurred since June 2026). Effects propagate up to four hops, damped by order, with double-count controls (clamping, overlap damping, link semantics).

**How to read the numbers.** Expected returns are *scenario-implied*, beta-adjusted and relative to the Nifty 200 average. They combine the still-unpriced part of June–November driver moves with probability-weighted forward events (half assumed priced) and company-specific catalysts. They are not validated forecasts; the rankings are frozen in `ledger/` and will be scored against realised returns and a momentum baseline.

## Top 20 (12-month, beta-adjusted, relative)
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 1 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +7.4 | +15.0 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 2 | [SAIL](stocks/SAIL.md) | Steel Authority of India Ltd. | Metals & Mining | +7.3 | +13.7 | 80% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → SAIL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL |
| 3 | [JINDALSTEL](stocks/JINDALSTEL.md) | Jindal Steel Ltd. | Metals & Mining | +7.9 | +13.7 | 80% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL |
| 4 | [TATASTEEL](stocks/TATASTEEL.md) | Tata Steel Ltd. | Metals & Mining | +6.7 | +12.4 | 80% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → TATASTEEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → TATASTEEL |
| 5 | [HINDPETRO](stocks/HINDPETRO.md) | Hindustan Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +5.1 | +12.1 | 60% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → HINDPETRO |
| 6 | [BDL](stocks/BDL.md) | Bharat Dynamics Ltd. | Capital Goods | +4.4 | +11.8 | 30% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BDL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BDL |
| 7 | [PREMIERENE](stocks/PREMIERENE.md) | Premier Energies Ltd. | Capital Goods | +7.5 | +11.2 | 70% | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → PREMIERENE | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → PREMIERENE |
| 8 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +5.7 | +10.6 | 60% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → IOC |
| 9 | [ENRIN](stocks/ENRIN.md) | Siemens Energy India Ltd. | Capital Goods | +6.0 | +10.2 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ENRIN | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN |
| 10 | [COALINDIA](stocks/COALINDIA.md) | Coal India Ltd. | Oil Gas & Consumable Fuels | +6.4 | +10.2 | 70% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → COALINDIA | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA |
| 11 | [WAAREEENER](stocks/WAAREEENER.md) | Waaree Energies Ltd. | Capital Goods | +6.9 | +10.2 | 70% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → WAAREEENER | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → WAAREEENER |
| 12 | [POWERINDIA](stocks/POWERINDIA.md) | Hitachi Energy India Ltd. | Capital Goods | +4.6 | +9.9 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POWERINDIA | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA |
| 13 | [BEL](stocks/BEL.md) | Bharat Electronics Ltd. | Capital Goods | +4.4 | +9.9 | 80% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BEL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BEL |
| 14 | [BPCL](stocks/BPCL.md) | Bharat Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +4.7 | +9.7 | 60% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL |
| 15 | [JSWSTEEL](stocks/JSWSTEEL.md) | JSW Steel Ltd. | Metals & Mining | +4.4 | +9.4 | 80% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JSWSTEEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JSWSTEEL |
| 16 | [BHEL](stocks/BHEL.md) | Bharat Heavy Electricals Ltd. | Capital Goods | +4.7 | +8.1 | 80% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BHEL | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → BHEL |
| 17 | [IDEA](stocks/IDEA.md) | Vodafone Idea Ltd. | Telecommunication | +3.8 | +8.1 | 50% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA |
| 18 | [SOLARINDS](stocks/SOLARINDS.md) | Solar Industries India Ltd. | Chemicals | +3.2 | +7.9 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → SOLARINDS | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SOLARINDS |
| 19 | [KEI](stocks/KEI.md) | KEI Industries Ltd. | Capital Goods | +3.7 | +7.8 | 80% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → KEI | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → KEI |
| 20 | [CGPOWER](stocks/CGPOWER.md) | CG Power and Industrial Solutions Ltd. | Capital Goods | +4.1 | +7.7 | 90% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CGPOWER | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → CGPOWER |

## Bottom 20
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 200 | [BAJFINANCE](stocks/BAJFINANCE.md) | Bajaj Finance Ltd. | Financial Services | -9.4 | -16.5 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJFINANCE | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BAJFINANCE |
| 199 | [TATACAP](stocks/TATACAP.md) | Tata Capital Ltd. | Financial Services | -8.3 | -15.2 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACAP |
| 198 | [BAJAJFINSV](stocks/BAJAJFINSV.md) | Bajaj Finserv Ltd. | Financial Services | -6.6 | -11.8 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJFINSV | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BAJAJFINSV |
| 197 | [PERSISTENT](stocks/PERSISTENT.md) | Persistent Systems Ltd. | Information Technology | -4.2 | -9.8 | 10% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → PERSISTENT | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PERSISTENT |
| 196 | [ETERNAL](stocks/ETERNAL.md) | Eternal Ltd. | Consumer Services | -5.2 | -9.6 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ETERNAL | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → ETERNAL |
| 195 | [PRESTIGE](stocks/PRESTIGE.md) | Prestige Estates Projects Ltd. | Realty | -4.3 | -8.8 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PRESTIGE | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PRESTIGE |
| 194 | [JIOFIN](stocks/JIOFIN.md) | Jio Financial Services Ltd. | Financial Services | -4.4 | -8.8 | 0% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JIOFIN | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → JIOFIN |
| 193 | [LENSKART](stocks/LENSKART.md) | Lenskart Solutions Ltd. | Consumer Services | -4.6 | -8.1 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LENSKART | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LENSKART |
| 192 | [YESBANK](stocks/YESBANK.md) | Yes Bank Ltd. | Financial Services | -5.5 | -7.9 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → YESBANK | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → YESBANK |
| 191 | [MEESHO](stocks/MEESHO.md) | Meesho Ltd. | Consumer Services | -3.7 | -7.7 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MEESHO | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MEESHO |
| 190 | [TCS](stocks/TCS.md) | Tata Consultancy Services Ltd. | Information Technology | -4.2 | -7.6 | 30% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → TCS | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → TCS |
| 189 | [AUBANK](stocks/AUBANK.md) | AU Small Finance Bank Ltd. | Financial Services | -4.1 | -7.5 | 60% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AUBANK | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → AUBANK |
| 188 | [TECHM](stocks/TECHM.md) | Tech Mahindra Ltd. | Information Technology | -3.4 | -7.1 | 40% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → TECHM | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → TECHM |
| 187 | [TORNTPHARM](stocks/TORNTPHARM.md) | Torrent Pharmaceuticals Ltd. | Healthcare | -4.3 | -7.1 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TORNTPHARM | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TORNTPHARM |
| 186 | [FEDERALBNK](stocks/FEDERALBNK.md) | Federal Bank Ltd. | Financial Services | -3.4 | -7.1 | 10% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → FEDERALBNK | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → FEDERALBNK |
| 185 | [ABCAPITAL](stocks/ABCAPITAL.md) | Aditya Birla Capital Ltd. | Financial Services | -3.6 | -7.0 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ABCAPITAL | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → ABCAPITAL |
| 184 | [MPHASIS](stocks/MPHASIS.md) | MphasiS Ltd. | Information Technology | -3.5 | -6.9 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MPHASIS | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MPHASIS |
| 183 | [IDFCFIRSTB](stocks/IDFCFIRSTB.md) | IDFC First Bank Ltd. | Financial Services | -3.7 | -6.8 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IDFCFIRSTB | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → IDFCFIRSTB |
| 182 | [NAUKRI](stocks/NAUKRI.md) | Info Edge (India) Ltd. | Consumer Services | -3.6 | -6.6 | 70% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NAUKRI | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → NAUKRI |
| 181 | [PHOENIXLTD](stocks/PHOENIXLTD.md) | Phoenix Mills Ltd. | Realty | -4.0 | -6.6 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PHOENIXLTD | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PHOENIXLTD |

## Nifty Next 50 — all 50 ranked
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 1 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +7.4 | +15.0 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 3 | [JINDALSTEL](stocks/JINDALSTEL.md) | Jindal Steel Ltd. | Metals & Mining | +7.9 | +13.7 | 80% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL |
| 8 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +5.7 | +10.6 | 60% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → IOC |
| 9 | [ENRIN](stocks/ENRIN.md) | Siemens Energy India Ltd. | Capital Goods | +6.0 | +10.2 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ENRIN | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN |
| 12 | [POWERINDIA](stocks/POWERINDIA.md) | Hitachi Energy India Ltd. | Capital Goods | +4.6 | +9.9 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POWERINDIA | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA |
| 14 | [BPCL](stocks/BPCL.md) | Bharat Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +4.7 | +9.7 | 60% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL |
| 17 | [IDEA](stocks/IDEA.md) | Vodafone Idea Ltd. | Telecommunication | +3.8 | +8.1 | 50% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA |
| 18 | [SOLARINDS](stocks/SOLARINDS.md) | Solar Industries India Ltd. | Chemicals | +3.2 | +7.9 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → SOLARINDS | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SOLARINDS |
| 20 | [CGPOWER](stocks/CGPOWER.md) | CG Power and Industrial Solutions Ltd. | Capital Goods | +4.1 | +7.7 | 90% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CGPOWER | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → CGPOWER |
| 22 | [POLYCAB](stocks/POLYCAB.md) | Polycab India Ltd. | Capital Goods | +2.7 | +6.9 | 50% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POLYCAB | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → POLYCAB |
| 26 | [HAL](stocks/HAL.md) | Hindustan Aeronautics Ltd. | Capital Goods | +1.4 | +5.3 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → HAL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HAL |
| 28 | [ABB](stocks/ABB.md) | ABB India Ltd. | Capital Goods | +2.8 | +5.1 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ABB | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ABB |
| 30 | [TATAPOWER](stocks/TATAPOWER.md) | Tata Power Co. Ltd. | Power | +2.8 | +4.9 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATAPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATAPOWER |
| 34 | [SIEMENS](stocks/SIEMENS.md) | Siemens Ltd. | Capital Goods | +1.9 | +4.3 | 80% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SIEMENS | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → SIEMENS |
| 38 | [ADANIGREEN](stocks/ADANIGREEN.md) | Adani Green Energy Ltd. | Power | +2.1 | +3.5 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIGREEN | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIGREEN |
| 39 | [TMCV](stocks/TMCV.md) | Tata Motors Ltd. | Capital Goods | +0.9 | +3.4 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → TMCV | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TMCV |
| 46 | [ADANIENSOL](stocks/ADANIENSOL.md) | Adani Energy Solutions Ltd. | Power | +2.4 | +3.0 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENSOL | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIENSOL |
| 50 | [GAIL](stocks/GAIL.md) | GAIL (India) Ltd. | Oil Gas & Consumable Fuels | +1.1 | +2.4 | 50% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → GAIL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GAIL |
| 55 | [AMBUJACEM](stocks/AMBUJACEM.md) | Ambuja Cements Ltd. | Construction Materials | +1.2 | +2.0 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → AMBUJACEM | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → AMBUJACEM |
| 63 | [CUMMINSIND](stocks/CUMMINSIND.md) | Cummins India Ltd. | Capital Goods | +0.7 | +1.4 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CUMMINSIND | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → CUMMINSIND |
| 65 | [ADANIPOWER](stocks/ADANIPOWER.md) | Adani Power Ltd. | Power | +0.7 | +1.4 | 50% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIPOWER | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → ADANIPOWER |
| 68 | [GODREJCP](stocks/GODREJCP.md) | Godrej Consumer Products Ltd. | Fast Moving Consumer Goods | +1.1 | +1.3 | 60% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GODREJCP | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GODREJCP |
| 72 | [IRFC](stocks/IRFC.md) | Indian Railway Finance Corporation Ltd. | Financial Services | +0.2 | +1.2 | 40% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → IRFC | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IRFC |
| 74 | [VBL](stocks/VBL.md) | Varun Beverages Ltd. | Fast Moving Consumer Goods | +0.4 | +1.1 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VBL | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → VBL |
| 77 | [HINDZINC](stocks/HINDZINC.md) | Hindustan Zinc Ltd. | Metals & Mining | +0.3 | +1.0 | 50% | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → HINDZINC | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC |
| 80 | [PNB](stocks/PNB.md) | Punjab National Bank | Financial Services | +1.4 | +0.9 | 70% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PNB | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → PNB |
| 81 | [TVSMOTOR](stocks/TVSMOTOR.md) | TVS Motor Company Ltd. | Automobile and Auto Components | +0.2 | +0.9 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TVSMOTOR | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → TVSMOTOR |
| 84 | [UNIONBANK](stocks/UNIONBANK.md) | Union Bank of India | Financial Services | +1.4 | +0.7 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → UNIONBANK | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → UNIONBANK |
| 101 | [BRITANNIA](stocks/BRITANNIA.md) | Britannia Industries Ltd. | Fast Moving Consumer Goods | -0.2 | -0.3 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BRITANNIA | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → BRITANNIA |
| 104 | [PFC](stocks/PFC.md) | Power Finance Corporation Ltd. | Financial Services | -1.1 | -0.4 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PFC | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PFC |
| 108 | [HDFCAMC](stocks/HDFCAMC.md) | HDFC Asset Management Company Ltd. | Financial Services | +0.1 | -0.5 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HDFCAMC | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → HDFCAMC |
| 109 | [VAML](stocks/VAML.md) | Vedanta Aluminium Metal Ltd. | Metals & Mining | -0.3 | -0.5 | 80% | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → VAML | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → VAML |
| 116 | [BAJAJHLDNG](stocks/BAJAJHLDNG.md) | Bajaj Holdings & Investment Ltd. | Financial Services | +0.2 | -0.7 | 70% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJHLDNG | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → BAJAJHLDNG |
| 117 | [MOTHERSON](stocks/MOTHERSON.md) | Samvardhana Motherson International Ltd. | Automobile and Auto Components | -0.1 | -0.8 | 30% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MOTHERSON | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MOTHERSON |
| 122 | [VEDL](stocks/VEDL.md) | Vedanta Ltd. | Metals & Mining | -0.4 | -1.2 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VEDL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → VEDL |
| 128 | [PIDILITIND](stocks/PIDILITIND.md) | Pidilite Industries Ltd. | Chemicals | -0.9 | -1.5 | 10% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → PIDILITIND | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PIDILITIND |
| 138 | [BANKBARODA](stocks/BANKBARODA.md) | Bank of Baroda | Financial Services | -0.2 | -2.2 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKBARODA | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → BANKBARODA |
| 139 | [DMART](stocks/DMART.md) | Avenue Supermarts Ltd. | Consumer Services | -1.5 | -2.3 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DMART | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → DMART |
| 143 | [BOSCHLTD](stocks/BOSCHLTD.md) | Bosch Ltd. | Automobile and Auto Components | -1.6 | -2.7 | 50% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BOSCHLTD |
| 145 | [DLF](stocks/DLF.md) | DLF Ltd. | Realty | -1.9 | -2.8 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DLF | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → DLF |
| 148 | [DIVISLAB](stocks/DIVISLAB.md) | Divi's Laboratories Ltd. | Healthcare | -1.7 | -3.0 | 60% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DIVISLAB | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → DIVISLAB |
| 152 | [CHOLAFIN](stocks/CHOLAFIN.md) | Cholamandalam Investment and Finance Company Ltd. | Financial Services | -2.2 | -3.3 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CHOLAFIN | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → CHOLAFIN |
| 154 | [CANBK](stocks/CANBK.md) | Canara Bank | Financial Services | -0.5 | -3.4 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CANBK | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → CANBK |
| 160 | [HYUNDAI](stocks/HYUNDAI.md) | Hyundai Motor India Ltd. | Automobile and Auto Components | -2.2 | -4.0 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HYUNDAI | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → HYUNDAI |
| 163 | [WIPRO](stocks/WIPRO.md) | Wipro Ltd. | Information Technology | -2.2 | -4.5 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → WIPRO | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → WIPRO |
| 166 | [MUTHOOTFIN](stocks/MUTHOOTFIN.md) | Muthoot Finance Ltd. | Financial Services | -2.4 | -4.7 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MUTHOOTFIN |
| 167 | [LTM](stocks/LTM.md) | LTM Ltd. | Information Technology | -2.2 | -4.8 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTM | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → LTM |
| 178 | [ZYDUSLIFE](stocks/ZYDUSLIFE.md) | Zydus Lifesciences Ltd. | Healthcare | -3.2 | -6.2 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ZYDUSLIFE | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → ZYDUSLIFE |
| 187 | [TORNTPHARM](stocks/TORNTPHARM.md) | Torrent Pharmaceuticals Ltd. | Healthcare | -4.3 | -7.1 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TORNTPHARM | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TORNTPHARM |
| 199 | [TATACAP](stocks/TATACAP.md) | Tata Capital Ltd. | Financial Services | -8.3 | -15.2 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACAP |

## Sector view (average of member stocks)
| industry | stocks | exp 3m | exp 12m | best | worst |
|---|---|---|---|---|---|
| Capital Goods | 24 | +3.1 | +6.3 | MAZDOCK | APARINDS |
| Oil Gas & Consumable Fuels | 9 | +3.3 | +6.2 | HINDPETRO | ATGL |
| Metals & Mining | 12 | +2.7 | +4.9 | SAIL | VEDL |
| Construction | 2 | +1.9 | +4.4 | LT | RVNL |
| Chemicals | 5 | +1.6 | +3.1 | SOLARINDS | PIDILITIND |
| Power | 9 | +1.2 | +2.5 | NLCINDIA | JSWENERGY |
| Telecommunication | 4 | +0.7 | +1.9 | IDEA | TATACOMM |
| Construction Materials | 3 | +0.9 | +1.7 | ULTRACEMCO | GRASIM |
| Consumer Durables | 8 | +0.8 | +1.1 | BLUESTARCO | ASIANPAINT |
| Automobile and Auto Components | 14 | +0.8 | +1.0 | TMPV | HYUNDAI |
| Fast Moving Consumer Goods | 14 | +0.1 | +0.2 | GODFRYPHLP | UNITDSPR |
| Services | 4 | -1.0 | -1.7 | CONCOR | GMRAIRPORT |
| Textiles | 1 | -1.7 | -2.1 | PAGEIND | PAGEIND |
| Healthcare | 15 | -1.5 | -2.4 | LUPIN | TORNTPHARM |
| Consumer Services | 12 | -1.8 | -3.1 | VMM | ETERNAL |
| Financial Services | 48 | -1.7 | -3.6 | LICHSGFIN | BAJFINANCE |
| Realty | 6 | -3.2 | -5.7 | DLF | PRESTIGE |
| Information Technology | 10 | -3.0 | -6.0 | OFSS | PERSISTENT |

## Upcoming and risk events that matter most (impact if the event happens, % equity, raw)
| event | status | P(12m) | biggest winners | biggest losers |
|---|---|---|---|---|
| [Hormuz effectively closed for >2 weeks (Brent > $150)](events/EV_HORMUZ_FULL_CLOSURE.md) | risk_scenario | 0.05 | OIL +40.1, ONGC +31.7, JSWSTEEL +8.3, SAIL +7.8, COALINDIA +7.4 | MOTILALOFS -32.3, INDIGO -30.6, YESBANK -29.9, IREDA -29.3, JIOFIN -28.4 |
| [AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes](events/EV_AI_CAPEX_RESET_RISK.md) | risk_scenario | 0.25 | JSWSTEEL +2.6, SAIL +2.6, TMPV +2.1, ASTRAL +2.0, MOTHERSON +2.0 | MOTILALOFS -21.6, POWERINDIA -19.5, ICICIAMC -18.3, JIOFIN -17.4, NAUKRI -16.5 |
| [Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action](events/EV_YEN_CARRY_UNWIND_RISK.md) | risk_scenario | 0.15 | JSWSTEEL +2.5, SAIL +2.4, HINDZINC +2.1, NATIONALUM +2.1, TATASTEEL +1.9 | MOTILALOFS -21.5, ICICIAMC -18.3, JIOFIN -17.8, IREDA -16.5, 360ONE -16.2 |
| [Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027)](events/EV_INDIA_STAGFLATION_SCARE.md) | risk_scenario | 0.12 | UPL +0.2, NATIONALUM +0.2, OIL +0.2, VAML +0.1, TECHM +0.0 | YESBANK -19.1, INDUSINDBK -17.1, IDFCFIRSTB -16.4, AUBANK -13.5, TATACAP -13.4 |
| [Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response)](events/EV_RUPEE_BREAK_98_RESERVE_STRESS.md) | risk_scenario | 0.18 | NATIONALUM +3.4, OIL +3.4, ONGC +3.3, JSWSTEEL +3.3, VAML +2.8 | YESBANK -15.9, MOTILALOFS -14.2, BAJFINANCE -12.4, GMRAIRPORT -12.1, TATACAP -11.5 |
| [Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110](events/EV_IRAN_TALKS_FAIL_ESCALATE.md) | risk_scenario | 0.25 | OIL +19.0, ONGC +14.9, JSWSTEEL +3.6, SAIL +3.4, MCX +3.3 | INDIGO -13.9, YESBANK -13.2, MOTILALOFS -12.9, GMRAIRPORT -12.1, IDFCFIRSTB -11.7 |
| [FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief](events/EV_FPI_INFLOW_REBOUND.md) | anticipated | 0.50 | MOTILALOFS +19.4, ICICIAMC +14.0, PAYTM +13.4, 360ONE +12.1, INDUSINDBK +11.6 | JSWSTEEL -2.1, SAIL -2.0, TATASTEEL -1.5, OIL -1.4, ONGC -1.4 |
| [US recession (two negative quarters or NBER-style) beginning by mid-2027](events/EV_US_RECESSION_RISK_2027.md) | risk_scenario | 0.25 | ASTRAL +5.4, SWIGGY +4.5, BSE +4.3, UPL +3.7, SRF +3.2 | LTM -14.8, NAUKRI -14.8, MOTILALOFS -14.0, 360ONE -13.7, MPHASIS -13.1 |
| [Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil](events/EV_RUSSIA_TARIFF_ENFORCED.md) | risk_scenario | 0.15 | OIL +4.8, ONGC +3.4, JINDALSTEL +3.1, JSWSTEEL +3.0, SAIL +2.8 | YESBANK -9.1, BPCL -8.8, MOTILALOFS -8.6, IDFCFIRSTB -7.6, INDUSINDBK -7.4 |
| [Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk](events/EV_PULSES_VEG_SPIKE_WINTER.md) | risk_scenario | 0.25 | PIIND +0.2, UPL +0.1 | YESBANK -10.7, BAJFINANCE -9.8, TATACAP -9.6, GMRAIRPORT -8.2, PRESTIGE -8.0 |
| [US-Iran ceasefire/peace framework agreed and holding](events/EV_US_IRAN_CEASEFIRE_DEAL.md) | anticipated | 0.55 | INDIGO +8.9, GMRAIRPORT +7.6, YESBANK +7.3, AXISBANK +7.2, MOTILALOFS +6.4 | OIL -12.6, ONGC -9.9, COCHINSHIP -2.9, MCX -2.6, VAML -2.1 |
| [India-Pakistan military crisis (terror attack, cross-border strikes) after Op Sindoor (May 2025)](events/EV_INDIA_PAK_CRISIS.md) | risk_scenario | 0.09 | MAZDOCK +5.5, SOLARINDS +5.4, HAL +5.1, BDL +5.1, BEL +4.4 | MOTILALOFS -8.0, JIOFIN -6.9, ICICIAMC -6.7, IREDA -6.7, 360ONE -5.9 |
| [Fed cuts >=25 bp by Apr 2027 (growth scare / AI bust / lower inflation)](events/EV_FED_H1_2027_CUTS.md) | anticipated | 0.12 | BSE +8.5, MOTILALOFS +6.6, SWIGGY +5.6, POLICYBZR +5.1, YESBANK +4.8 | JSWSTEEL -0.7, SAIL -0.6, TMPV -0.5, OIL -0.5, ONGC -0.5 |
| [RBI MPC Apr 2027 (~8 Apr): cuts 25 bp (hiking cycle reversed)](events/EV_RBI_APR27_CUT25.md) | anticipated | 0.10 | YESBANK +5.4, PRESTIGE +5.4, TATACAP +5.3, BAJFINANCE +5.2, GODREJPROP +5.1 | LICHSGFIN -1.2, PAYTM -0.5, BANKINDIA -0.0 |
| [RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75%](events/EV_RBI_DEC26_HIKE25.md) | scheduled | 0.42 | LICHSGFIN +1.2, BANKINDIA +0.6, PAYTM +0.5, MAHABANK +0.0 | BAJFINANCE -5.4, TATACAP -5.3, PRESTIGE -5.3, YESBANK -5.0, GMRAIRPORT -5.0 |

## Events since June 2026 with the widest footprint (model impact, % equity, raw)
| event | winners | losers |
|---|---|---|
| [Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October](events/EV_FPI_RECORD_OUTFLOW_26.md) | JSWSTEEL +1.6, SAIL +1.6, JINDALSTEL +1.4, TATASTEEL +1.2 | MOTILALOFS -15.7, PAYTM -11.0, ICICIAMC -10.9, SBIN -9.4 |
| [CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74%](events/EV_CPI_REACCEL_SEP26.md) | PIIND +0.2, UPL +0.1 | YESBANK -12.2, BAJFINANCE -11.2, TATACAP -10.9, GMRAIRPORT -9.4 |
| [RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026)](events/EV_RBI_OCT26_HIKE25.md) | LICHSGFIN +1.2, BANKINDIA +0.6, PAYTM +0.5, MAHABANK +0.0 | BAJFINANCE -5.4, TATACAP -5.3, PRESTIGE -5.3, YESBANK -5.0 |
| [RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high](events/EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26.md) | HDFCLIFE +0.6, SBILIFE +0.3, MFSL +0.3, RVNL +0.1 | YESBANK -6.2, ADANIGREEN -5.7, BAJFINANCE -5.7, TATACAP -5.4 |
| [Fed delivers first hike in years (16 Sep 2026), new chair Warsh](events/EV_FED_SEP26_HIKE.md) | JSWSTEEL +0.5, SAIL +0.4, OIL +0.4, TMPV +0.4 | BSE -5.9, MOTILALOFS -4.6, SWIGGY -3.8, POLICYBZR -3.4 |
| [2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015](events/EV_SWMONSOON26_DEFICIT.md) | ADANIPOWER +3.4, COALINDIA +1.0, AMBUJACEM +0.9, ENRIN +0.6 | INDUSINDBK -8.7, IDFCFIRSTB -7.5, YESBANK -6.2, BANKINDIA -5.0 |
| [India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus](events/EV_GDP_Q1FY27_7_8.md) | TMCV +6.2, POWERINDIA +4.6, ASHOKLEY +4.4, UNIONBANK +4.2 | PRESTIGE -1.7, JSWENERGY -1.3, LODHA -1.2, GODREJPROP -1.1 |
| [US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k](events/EV_US_Q3_DATA_MIXED.md) | MOTILALOFS +5.7, NAUKRI +5.3, ICICIAMC +4.9, LTM +4.8 | ASTRAL -1.6, BPCL -1.0, SRF -1.0, SHRIRAMFIN -1.0 |
| [US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004](events/EV_UST_SELLOFF_SEP26.md) | TMPV +0.6, JSWSTEEL +0.6, SAIL +0.6, ONGC +0.4 | MOTILALOFS -3.2, BSE -3.0, YESBANK -2.8, MUTHOOTFIN -2.7 |
| [Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct)](events/EV_IRAN_WAR_HORMUZ_OIL.md) | OIL +5.2, ONGC +4.5, VAML +2.2, NATIONALUM +1.8 | FEDERALBNK -5.1, INDIGO -3.9, AXISBANK -3.5, GMRAIRPORT -3.4 |

## Drivers with the widest reach (see DRIVERS.md for the company lists)
| driver | standard shock | companies moved ≥0.5% | share via 2nd–4th order |
|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | 189.0 | 98% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | 169.0 | 86% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | 176.0 | 62% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | 139.0 | 83% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | 139.0 | 15% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | 170.0 | 98% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | 181.0 | 34% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | 149.0 | 59% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | 114.0 | 50% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | 165.0 | 74% |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | 106.0 | 80% |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | 38.0 | 7% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | 135.0 | 85% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | 119.0 | 64% |
| US dollar index (`F_DXY`) | +3% DXY | 134.0 | 97% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | 131.0 | 100% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | 143.0 | 100% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | 124.0 | 93% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | 88.0 | 49% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | 108.0 | 15% |

## Strongest 3rd- and 4th-order chains from upcoming/risk events (expected 12m = probability × impact)
| company | order | chain | impact if event | expected 12m |
|---|---|---|---|---|
| INDUSINDBK | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +1.38% | +1.24% |
| IDFCFIRSTB | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +1.21% | +1.09% |
| COCHINSHIP | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → C_RED_SEA → F_SHIPPING_RATES → COCHINSHIP | -1.75% | -0.96% |
| INDUSINDBK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +1.28% | +0.87% |
| JINDALSTEL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → JINDALSTEL | -1.66% | -0.83% |
| JINDALSTEL | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → JINDALSTEL | -1.48% | -0.81% |
| YESBANK | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → YESBANK | +0.86% | +0.78% |
| JINDALSTEL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL | +2.22% | +0.78% |
| SAIL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → SAIL | -1.55% | -0.78% |
| VAML | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → F_ALUMINIUM → VAML | +2.20% | +0.77% |
| SAIL | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → SAIL | -1.39% | -0.76% |
| IDFCFIRSTB | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +1.12% | +0.76% |
| SAIL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL | +2.08% | +0.73% |
| COALINDIA | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_COAL_INDIA → COALINDIA | -1.03% | -0.70% |
| POWERINDIA | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | -1.03% | -0.70% |
| FEDERALBNK | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.78% | +0.70% |
| AXISBANK | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → AXISBANK | +0.73% | +0.66% |
| PRESTIGE | 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → PRESTIGE | -1.02% | -0.66% |
| INDUSINDBK | 3 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +0.92% | +0.65% |
| JINDALSTEL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → JINDALSTEL | +1.80% | +0.63% |
| JINDALSTEL | 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → JINDALSTEL | +2.50% | +0.63% |
| IREDA | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → IREDA | +0.69% | +0.62% |
| PRESTIGE | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_REPO_IN → PRESTIGE | -0.69% | -0.62% |
| SAIL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → SAIL | +1.69% | +0.59% |
| SAIL | 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → SAIL | +2.35% | +0.59% |

## Strongest 2nd–4th-order chains from what already moved since 1 June 2026 (raw model impact)
| company | order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|---|
| ENRIN | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ENRIN | +1.50 | events | +2.88% |
| BSE | 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → BSE | -1.60 | events | -2.30% |
| GROWW | 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → GROWW | -1.60 | events | -2.30% |
| POWERINDIA | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | +1.20 | events | +2.30% |
| LODHA | 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → LODHA | +1.55 | director_override | -2.23% |
| GODREJPROP | 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → GODREJPROP | +1.55 | director_override | -2.23% |
| APARINDS | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → APARINDS | +1.50 | events | +1.92% |
| KEI | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → KEI | +1.50 | events | +1.92% |
| POWERINDIA | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → POWERINDIA | +1.50 | events | +1.92% |
| MOTILALOFS | 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → MOTILALOFS | -1.60 | events | -1.79% |
| GVT&D | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → GVT&D | +1.20 | events | +1.73% |
| SBICARD | 2 | F_MONSOON → F_UNSECURED_STRESS → SBICARD | -1.56 | events | -1.50% |
| INDUSINDBK | 2 | F_MONSOON → F_UNSECURED_STRESS → INDUSINDBK | -1.56 | events | -1.50% |
| GVT&D | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → GVT&D | +1.50 | events | +1.44% |
| FEDERALBNK | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.50 | events | +1.44% |
| CGPOWER | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | +1.20 | events | +1.44% |
| CHOLAFIN | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → CHOLAFIN | +0.50 | events | +1.28% |
| INDUSINDBK | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +0.50 | events | +1.28% |
| 360ONE | 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → 360ONE | -1.60 | events | -1.28% |
| IREDA | 2 | F_GDP_IN → F_ASSET_QUALITY_IN → IREDA | +0.50 | events | +1.28% |
| IDFCFIRSTB | 2 | F_MONSOON → F_UNSECURED_STRESS → IDFCFIRSTB | -1.56 | events | -1.25% |
| ABB | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ABB | +1.50 | events | +1.20% |
| CGPOWER | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → CGPOWER | +1.50 | events | +1.20% |
| GVT&D | 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → GVT&D | +0.50 | events | +1.20% |
| ADANIENSOL | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ADANIENSOL | +1.50 | events | +1.20% |

## Files
- `RANKINGS.md` — all 200 stocks; `stocks/<TICKER>.md` — per-stock deep dive (drivers by order, events, chains, analyst profile); `events/<EVENT>.md` — per-event winners/losers by order; `EVENTS.md`; `DRIVERS.md`.
- Data: `results/rankings.csv`, `results/sensitivity_by_order.csv`, `results/event_impacts.csv`, `results/edges_all.csv`.
- Method: `PLAN.md`, `docs/AGENT_SPEC.md`; review trail: `review/`, `graph/*overrides*.json`.
