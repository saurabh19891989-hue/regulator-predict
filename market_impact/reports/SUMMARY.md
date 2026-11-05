# Market Impact Graph — Nifty 200 second-to-fourth-order effects (analysis date 2026-11-05)

**What this is.** A causal exposure network: events → macro/commodity/policy/geopolitical drivers → companies, with 2808 weighted edges among 459 nodes (200 company profiles, 161 events of which 61 already occurred since June 2026). Effects propagate up to four hops, damped by order, with double-count controls (clamping, overlap damping, link semantics).

**How to read the numbers.** Expected returns are *scenario-implied*, beta-adjusted and relative to the Nifty 200 average. They combine the still-unpriced part of June–November driver moves with probability-weighted forward events (half assumed priced) and company-specific catalysts. They are not validated forecasts; the rankings are frozen in `ledger/` and will be scored against realised returns and a momentum baseline.

## Top 20 (12-month, beta-adjusted, relative)
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 1 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +8.0 | +16.3 | 65% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 2 | [HINDPETRO](stocks/HINDPETRO.md) | Hindustan Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +5.5 | +13.5 | 72% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HINDPETRO |
| 3 | [BDL](stocks/BDL.md) | Bharat Dynamics Ltd. | Capital Goods | +4.6 | +12.7 | 55% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BDL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BDL |
| 4 | [TATASTEEL](stocks/TATASTEEL.md) | Tata Steel Ltd. | Metals & Mining | +6.1 | +12.2 | 72% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → TATASTEEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → TATASTEEL |
| 5 | [COALINDIA](stocks/COALINDIA.md) | Coal India Ltd. | Oil Gas & Consumable Fuels | +7.7 | +12.2 | 68% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → COALINDIA | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → COALINDIA |
| 6 | [PREMIERENE](stocks/PREMIERENE.md) | Premier Energies Ltd. | Capital Goods | +7.7 | +11.9 | 68% | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → PREMIERENE | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → PREMIERENE |
| 7 | [SAIL](stocks/SAIL.md) | Steel Authority of India Ltd. | Metals & Mining | +5.5 | +11.8 | 70% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → SAIL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL |
| 8 | [WAAREEENER](stocks/WAAREEENER.md) | Waaree Energies Ltd. | Capital Goods | +7.6 | +11.5 | 62% | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → WAAREEENER | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → WAAREEENER |
| 9 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +5.6 | +11.2 | 70% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → IOC |
| 10 | [JINDALSTEL](stocks/JINDALSTEL.md) | Jindal Steel Ltd. | Metals & Mining | +5.6 | +10.7 | 75% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL |
| 11 | [BEL](stocks/BEL.md) | Bharat Electronics Ltd. | Capital Goods | +4.8 | +10.6 | 62% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BEL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BEL |
| 12 | [ENRIN](stocks/ENRIN.md) | Siemens Energy India Ltd. | Capital Goods | +6.3 | +10.5 | 68% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ENRIN | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN |
| 13 | [BPCL](stocks/BPCL.md) | Bharat Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +4.5 | +10.4 | 65% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL |
| 14 | [POWERINDIA](stocks/POWERINDIA.md) | Hitachi Energy India Ltd. | Capital Goods | +4.6 | +9.6 | 57% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POWERINDIA | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA |
| 15 | [KEI](stocks/KEI.md) | KEI Industries Ltd. | Capital Goods | +4.3 | +9.5 | 65% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → KEI | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → KEI |
| 16 | [SOLARINDS](stocks/SOLARINDS.md) | Solar Industries India Ltd. | Chemicals | +4.0 | +9.4 | 57% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → SOLARINDS | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → SOLARINDS |
| 17 | [BHEL](stocks/BHEL.md) | Bharat Heavy Electricals Ltd. | Capital Goods | +5.1 | +9.0 | 70% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BHEL | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → BHEL |
| 18 | [CGPOWER](stocks/CGPOWER.md) | CG Power and Industrial Solutions Ltd. | Capital Goods | +4.4 | +8.6 | 78% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CGPOWER | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → CGPOWER |
| 19 | [OIL](stocks/OIL.md) | Oil India Ltd. | Oil Gas & Consumable Fuels | +5.3 | +8.3 | 57% | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → OIL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → OIL |
| 20 | [JSWSTEEL](stocks/JSWSTEEL.md) | JSW Steel Ltd. | Metals & Mining | +3.1 | +8.1 | 72% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JSWSTEEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JSWSTEEL |

## Bottom 20
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 200 | [BAJFINANCE](stocks/BAJFINANCE.md) | Bajaj Finance Ltd. | Financial Services | -10.4 | -18.8 | 15% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJFINANCE | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BAJFINANCE |
| 199 | [TATACAP](stocks/TATACAP.md) | Tata Capital Ltd. | Financial Services | -9.1 | -17.0 | 18% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → TATACAP |
| 198 | [BAJAJFINSV](stocks/BAJAJFINSV.md) | Bajaj Finserv Ltd. | Financial Services | -7.4 | -13.4 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJFINSV | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BAJAJFINSV |
| 197 | [JIOFIN](stocks/JIOFIN.md) | Jio Financial Services Ltd. | Financial Services | -5.4 | -11.8 | 12% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JIOFIN | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → JIOFIN |
| 196 | [ETERNAL](stocks/ETERNAL.md) | Eternal Ltd. | Consumer Services | -5.2 | -10.9 | 32% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ETERNAL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ETERNAL |
| 195 | [YESBANK](stocks/YESBANK.md) | Yes Bank Ltd. | Financial Services | -6.9 | -10.8 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → YESBANK | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → YESBANK |
| 194 | [IDFCFIRSTB](stocks/IDFCFIRSTB.md) | IDFC First Bank Ltd. | Financial Services | -5.5 | -10.6 | 35% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IDFCFIRSTB | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → IDFCFIRSTB |
| 193 | [MEESHO](stocks/MEESHO.md) | Meesho Ltd. | Consumer Services | -4.3 | -10.2 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MEESHO | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MEESHO |
| 192 | [LENSKART](stocks/LENSKART.md) | Lenskart Solutions Ltd. | Consumer Services | -5.0 | -9.9 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LENSKART | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LENSKART |
| 191 | [FEDERALBNK](stocks/FEDERALBNK.md) | Federal Bank Ltd. | Financial Services | -4.3 | -9.9 | 25% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → FEDERALBNK | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → FEDERALBNK |
| 190 | [PERSISTENT](stocks/PERSISTENT.md) | Persistent Systems Ltd. | Information Technology | -4.3 | -9.6 | 30% | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → PERSISTENT | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PERSISTENT |
| 189 | [AUBANK](stocks/AUBANK.md) | AU Small Finance Bank Ltd. | Financial Services | -4.8 | -9.5 | 22% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AUBANK | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → AUBANK |
| 188 | [PRESTIGE](stocks/PRESTIGE.md) | Prestige Estates Projects Ltd. | Realty | -4.3 | -9.0 | 32% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PRESTIGE | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PRESTIGE |
| 187 | [INDUSINDBK](stocks/INDUSINDBK.md) | IndusInd Bank Ltd. | Financial Services | -4.2 | -8.0 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → INDUSINDBK | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → INDUSINDBK |
| 186 | [ABCAPITAL](stocks/ABCAPITAL.md) | Aditya Birla Capital Ltd. | Financial Services | -3.9 | -7.8 | 20% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ABCAPITAL | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → ABCAPITAL |
| 185 | [NAUKRI](stocks/NAUKRI.md) | Info Edge (India) Ltd. | Consumer Services | -3.8 | -7.8 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → NAUKRI | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → NAUKRI |
| 184 | [GMRAIRPORT](stocks/GMRAIRPORT.md) | GMR Airports Ltd. | Services | -4.3 | -7.7 | 40% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GMRAIRPORT | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GMRAIRPORT |
| 183 | [AXISBANK](stocks/AXISBANK.md) | Axis Bank Ltd. | Financial Services | -3.6 | -7.6 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AXISBANK | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → AXISBANK |
| 182 | [TORNTPHARM](stocks/TORNTPHARM.md) | Torrent Pharmaceuticals Ltd. | Healthcare | -4.3 | -7.4 | 35% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TORNTPHARM | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TORNTPHARM |
| 181 | [SHRIRAMFIN](stocks/SHRIRAMFIN.md) | Shriram Finance Ltd. | Financial Services | -5.1 | -7.3 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SHRIRAMFIN | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → SHRIRAMFIN |

## Nifty Next 50 — all 50 ranked
| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |
|---|---|---|---|---|---|---|---|---|
| 1 | [MAZDOCK](stocks/MAZDOCK.md) | Mazagoan Dock Shipbuilders Ltd. | Capital Goods | +8.0 | +16.3 | 65% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → MAZDOCK | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → MAZDOCK |
| 9 | [IOC](stocks/IOC.md) | Indian Oil Corporation Ltd. | Oil Gas & Consumable Fuels | +5.6 | +11.2 | 70% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → IOC |
| 10 | [JINDALSTEL](stocks/JINDALSTEL.md) | Jindal Steel Ltd. | Metals & Mining | +5.6 | +10.7 | 75% | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL |
| 12 | [ENRIN](stocks/ENRIN.md) | Siemens Energy India Ltd. | Capital Goods | +6.3 | +10.5 | 68% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ENRIN | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ENRIN |
| 13 | [BPCL](stocks/BPCL.md) | Bharat Petroleum Corporation Ltd. | Oil Gas & Consumable Fuels | +4.5 | +10.4 | 65% | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL |
| 14 | [POWERINDIA](stocks/POWERINDIA.md) | Hitachi Energy India Ltd. | Capital Goods | +4.6 | +9.6 | 57% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POWERINDIA | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → POWERINDIA |
| 16 | [SOLARINDS](stocks/SOLARINDS.md) | Solar Industries India Ltd. | Chemicals | +4.0 | +9.4 | 57% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → SOLARINDS | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → SOLARINDS |
| 18 | [CGPOWER](stocks/CGPOWER.md) | CG Power and Industrial Solutions Ltd. | Capital Goods | +4.4 | +8.6 | 78% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CGPOWER | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → CGPOWER |
| 22 | [POLYCAB](stocks/POLYCAB.md) | Polycab India Ltd. | Capital Goods | +3.0 | +8.0 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → POLYCAB | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → POLYCAB |
| 26 | [IDEA](stocks/IDEA.md) | Vodafone Idea Ltd. | Telecommunication | +3.2 | +6.4 | 42% | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA |
| 27 | [HAL](stocks/HAL.md) | Hindustan Aeronautics Ltd. | Capital Goods | +1.9 | +6.4 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → HAL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HAL |
| 31 | [ABB](stocks/ABB.md) | ABB India Ltd. | Capital Goods | +3.3 | +6.3 | 72% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ABB | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → ABB |
| 33 | [TATAPOWER](stocks/TATAPOWER.md) | Tata Power Co. Ltd. | Power | +3.7 | +6.0 | 57% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATAPOWER | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATAPOWER |
| 36 | [SIEMENS](stocks/SIEMENS.md) | Siemens Ltd. | Capital Goods | +2.0 | +4.8 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SIEMENS | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → SIEMENS |
| 41 | [TMCV](stocks/TMCV.md) | Tata Motors Ltd. | Capital Goods | +0.7 | +4.0 | 55% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → TMCV | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → TMCV |
| 43 | [ADANIGREEN](stocks/ADANIGREEN.md) | Adani Green Energy Ltd. | Power | +2.6 | +3.9 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIGREEN | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIGREEN |
| 48 | [GAIL](stocks/GAIL.md) | GAIL (India) Ltd. | Oil Gas & Consumable Fuels | +1.3 | +3.3 | 50% | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GAIL | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GAIL |
| 49 | [ADANIPOWER](stocks/ADANIPOWER.md) | Adani Power Ltd. | Power | +2.4 | +3.3 | 57% | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIPOWER | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → ADANIPOWER |
| 50 | [ADANIENSOL](stocks/ADANIENSOL.md) | Adani Energy Solutions Ltd. | Power | +3.0 | +3.3 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENSOL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIENSOL |
| 53 | [AMBUJACEM](stocks/AMBUJACEM.md) | Ambuja Cements Ltd. | Construction Materials | +1.4 | +3.0 | 60% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → AMBUJACEM | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → AMBUJACEM |
| 61 | [HINDZINC](stocks/HINDZINC.md) | Hindustan Zinc Ltd. | Metals & Mining | +0.7 | +2.4 | 60% | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → HINDZINC | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC |
| 66 | [CUMMINSIND](stocks/CUMMINSIND.md) | Cummins India Ltd. | Capital Goods | +0.8 | +2.1 | 57% | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CUMMINSIND | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → CUMMINSIND |
| 68 | [IRFC](stocks/IRFC.md) | Indian Railway Finance Corporation Ltd. | Financial Services | +0.5 | +2.1 | 52% | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → IRFC | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IRFC |
| 74 | [VBL](stocks/VBL.md) | Varun Beverages Ltd. | Fast Moving Consumer Goods | +0.5 | +1.7 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VBL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → VBL |
| 75 | [GODREJCP](stocks/GODREJCP.md) | Godrej Consumer Products Ltd. | Fast Moving Consumer Goods | +1.0 | +1.6 | 57% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GODREJCP | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GODREJCP |
| 77 | [TVSMOTOR](stocks/TVSMOTOR.md) | TVS Motor Company Ltd. | Automobile and Auto Components | +0.6 | +1.5 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TVSMOTOR | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TVSMOTOR |
| 94 | [MOTHERSON](stocks/MOTHERSON.md) | Samvardhana Motherson International Ltd. | Automobile and Auto Components | +0.0 | +0.3 | 52% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MOTHERSON | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MOTHERSON |
| 99 | [VAML](stocks/VAML.md) | Vedanta Aluminium Metal Ltd. | Metals & Mining | -0.2 | +0.2 | 68% | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → VAML | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → VAML |
| 102 | [PNB](stocks/PNB.md) | Punjab National Bank | Financial Services | +1.0 | +0.1 | 70% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PNB | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → PNB |
| 103 | [HDFCAMC](stocks/HDFCAMC.md) | HDFC Asset Management Company Ltd. | Financial Services | +0.5 | +0.1 | 52% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HDFCAMC | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → HDFCAMC |
| 109 | [UNIONBANK](stocks/UNIONBANK.md) | Union Bank of India | Financial Services | +1.0 | -0.2 | 25% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → UNIONBANK | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → UNIONBANK |
| 110 | [BRITANNIA](stocks/BRITANNIA.md) | Britannia Industries Ltd. | Fast Moving Consumer Goods | -0.3 | -0.3 | 38% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BRITANNIA | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → BRITANNIA |
| 111 | [BAJAJHLDNG](stocks/BAJAJHLDNG.md) | Bajaj Holdings & Investment Ltd. | Financial Services | +0.3 | -0.3 | 62% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJHLDNG | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → BAJAJHLDNG |
| 112 | [PFC](stocks/PFC.md) | Power Finance Corporation Ltd. | Financial Services | -0.8 | -0.4 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PFC | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → PFC |
| 118 | [VEDL](stocks/VEDL.md) | Vedanta Ltd. | Metals & Mining | -0.0 | -0.7 | 50% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VEDL | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → VEDL |
| 128 | [PIDILITIND](stocks/PIDILITIND.md) | Pidilite Industries Ltd. | Chemicals | -1.4 | -1.8 | 38% | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → PIDILITIND | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → PIDILITIND |
| 131 | [BOSCHLTD](stocks/BOSCHLTD.md) | Bosch Ltd. | Automobile and Auto Components | -1.7 | -2.3 | 50% | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BOSCHLTD |
| 137 | [DLF](stocks/DLF.md) | DLF Ltd. | Realty | -1.7 | -2.6 | 38% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DLF | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → DLF |
| 138 | [DMART](stocks/DMART.md) | Avenue Supermarts Ltd. | Consumer Services | -1.3 | -2.6 | 35% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DMART | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → DMART |
| 141 | [BANKBARODA](stocks/BANKBARODA.md) | Bank of Baroda | Financial Services | -0.4 | -2.9 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKBARODA | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BANKBARODA |
| 146 | [DIVISLAB](stocks/DIVISLAB.md) | Divi's Laboratories Ltd. | Healthcare | -1.4 | -3.4 | 55% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DIVISLAB | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → DIVISLAB |
| 148 | [CHOLAFIN](stocks/CHOLAFIN.md) | Cholamandalam Investment and Finance Company Ltd. | Financial Services | -2.5 | -3.8 | 42% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CHOLAFIN | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → CHOLAFIN |
| 152 | [CANBK](stocks/CANBK.md) | Canara Bank | Financial Services | -0.5 | -4.1 | 38% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CANBK | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → CANBK |
| 155 | [WIPRO](stocks/WIPRO.md) | Wipro Ltd. | Information Technology | -2.2 | -4.5 | 35% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → WIPRO | EV_ANTHROPIC_IPO_LISTING ⇒ T_GENAI_SERVICES → WIPRO |
| 157 | [HYUNDAI](stocks/HYUNDAI.md) | Hyundai Motor India Ltd. | Automobile and Auto Components | -2.6 | -4.5 | 45% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HYUNDAI | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → HYUNDAI |
| 158 | [LTM](stocks/LTM.md) | LTM Ltd. | Information Technology | -2.1 | -4.6 | 30% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTM | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → LTM |
| 162 | [MUTHOOTFIN](stocks/MUTHOOTFIN.md) | Muthoot Finance Ltd. | Financial Services | -2.2 | -5.0 | 32% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → MUTHOOTFIN |
| 172 | [ZYDUSLIFE](stocks/ZYDUSLIFE.md) | Zydus Lifesciences Ltd. | Healthcare | -3.1 | -6.3 | 32% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ZYDUSLIFE | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ZYDUSLIFE |
| 182 | [TORNTPHARM](stocks/TORNTPHARM.md) | Torrent Pharmaceuticals Ltd. | Healthcare | -4.3 | -7.4 | 35% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TORNTPHARM | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TORNTPHARM |
| 199 | [TATACAP](stocks/TATACAP.md) | Tata Capital Ltd. | Financial Services | -9.1 | -17.0 | 18% | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → TATACAP |

## Sector view (average of member stocks)
| industry | stocks | exp 3m | exp 12m | best | worst |
|---|---|---|---|---|---|
| Oil Gas & Consumable Fuels | 9 | +3.9 | +7.7 | HINDPETRO | ATGL |
| Capital Goods | 24 | +3.3 | +7.0 | MAZDOCK | APARINDS |
| Construction | 2 | +2.0 | +5.1 | LT | RVNL |
| Metals & Mining | 12 | +2.4 | +5.0 | TATASTEEL | VEDL |
| Chemicals | 5 | +1.7 | +3.9 | SOLARINDS | PIDILITIND |
| Power | 9 | +1.9 | +3.3 | NLCINDIA | JSWENERGY |
| Construction Materials | 3 | +1.1 | +2.6 | ULTRACEMCO | GRASIM |
| Automobile and Auto Components | 14 | +0.9 | +1.7 | TMPV | HYUNDAI |
| Consumer Durables | 8 | +0.8 | +1.4 | BLUESTARCO | ASIANPAINT |
| Telecommunication | 4 | +0.5 | +1.4 | IDEA | TATACOMM |
| Fast Moving Consumer Goods | 14 | +0.1 | +0.5 | GODFRYPHLP | RADICO |
| Services | 4 | -1.3 | -2.1 | CONCOR | GMRAIRPORT |
| Healthcare | 15 | -1.3 | -2.2 | LUPIN | TORNTPHARM |
| Textiles | 1 | -1.7 | -2.3 | PAGEIND | PAGEIND |
| Consumer Services | 12 | -1.9 | -3.6 | VMM | ETERNAL |
| Financial Services | 48 | -2.1 | -4.9 | LICHSGFIN | BAJFINANCE |
| Realty | 6 | -3.1 | -5.6 | DLF | PRESTIGE |
| Information Technology | 10 | -2.9 | -5.7 | OFSS | PERSISTENT |

## Upcoming and risk events that matter most (impact if the event happens, % equity, raw)
| event | status | P(12m) | biggest winners | biggest losers |
|---|---|---|---|---|
| [Hormuz effectively closed for >2 weeks (Brent > $150)](events/EV_HORMUZ_FULL_CLOSURE.md) | risk_scenario | 0.06 | OIL +48.4, ONGC +37.8, JSWSTEEL +10.1, SAIL +9.6, COALINDIA +9.0 | MOTILALOFS -36.8, YESBANK -36.7, INDIGO -35.8, IDFCFIRSTB -32.9, IREDA -32.8 |
| [Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action](events/EV_YEN_CARRY_UNWIND_RISK.md) | risk_scenario | 0.18 | JSWSTEEL +4.6, SAIL +4.5, TATACONSUM +3.6, HINDZINC +3.5, TATASTEEL +3.3 | MOTILALOFS -35.0, JIOFIN -32.4, ICICIAMC -31.2, IREDA -30.8, 360ONE -27.7 |
| [AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes](events/EV_AI_CAPEX_RESET_RISK.md) | risk_scenario | 0.28 | JSWSTEEL +3.9, SAIL +3.8, TATACONSUM +3.1, ASTRAL +3.0, TMPV +2.8 | MOTILALOFS -29.7, JIOFIN -26.2, ICICIAMC -26.0, IREDA -25.0, 360ONE -22.8 |
| [Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110](events/EV_IRAN_TALKS_FAIL_ESCALATE.md) | risk_scenario | 0.36 | OIL +20.8, ONGC +16.2, JSWSTEEL +4.2, SAIL +4.0, COALINDIA +3.6 | INDIGO -15.3, YESBANK -15.2, MOTILALOFS -15.0, IDFCFIRSTB -13.5, IREDA -13.4 |
| [Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027)](events/EV_INDIA_STAGFLATION_SCARE.md) | risk_scenario | 0.12 | UPL +0.2, NATIONALUM +0.2, OIL +0.2, VAML +0.1, TECHM +0.0 | YESBANK -19.1, INDUSINDBK -17.1, IDFCFIRSTB -16.4, AUBANK -13.5, TATACAP -13.4 |
| [Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response)](events/EV_RUPEE_BREAK_98_RESERVE_STRESS.md) | risk_scenario | 0.22 | NATIONALUM +3.4, OIL +3.4, ONGC +3.3, JSWSTEEL +3.3, VAML +2.8 | YESBANK -15.9, MOTILALOFS -14.2, BAJFINANCE -12.4, GMRAIRPORT -12.1, TATACAP -11.5 |
| [FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief](events/EV_FPI_INFLOW_REBOUND.md) | anticipated | 0.50 | MOTILALOFS +19.4, ICICIAMC +14.0, PAYTM +13.4, 360ONE +12.1, INDUSINDBK +11.6 | JSWSTEEL -2.1, SAIL -2.0, TATASTEEL -1.5, OIL -1.4, ONGC -1.4 |
| [US recession (two negative quarters or NBER-style) beginning by mid-2027](events/EV_US_RECESSION_RISK_2027.md) | risk_scenario | 0.25 | ASTRAL +5.4, SWIGGY +4.5, BSE +4.3, UPL +3.7, SRF +3.2 | LTM -14.8, NAUKRI -14.8, MOTILALOFS -14.0, 360ONE -13.7, MPHASIS -13.1 |
| [US-Iran ceasefire/peace framework agreed and holding](events/EV_US_IRAN_CEASEFIRE_DEAL.md) | anticipated | 0.58 | INDIGO +9.9, YESBANK +8.5, GMRAIRPORT +8.4, AXISBANK +7.9, MOTILALOFS +7.6 | OIL -14.0, ONGC -11.0, COCHINSHIP -2.9, MCX -2.7, JSWSTEEL -2.3 |
| [Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil](events/EV_RUSSIA_TARIFF_ENFORCED.md) | risk_scenario | 0.15 | OIL +4.8, ONGC +3.4, JINDALSTEL +3.1, JSWSTEEL +3.0, SAIL +2.8 | YESBANK -9.1, BPCL -8.8, MOTILALOFS -8.6, IDFCFIRSTB -7.6, INDUSINDBK -7.4 |
| [Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk](events/EV_PULSES_VEG_SPIKE_WINTER.md) | risk_scenario | 0.25 | PIIND +0.2, UPL +0.1 | YESBANK -10.7, BAJFINANCE -9.8, TATACAP -9.6, GMRAIRPORT -8.2, PRESTIGE -8.0 |
| [Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027](events/EV_FED_H1_2027_FURTHER_HIKES.md) | anticipated | 0.30 | JSWSTEEL +0.9, SAIL +0.8, TMPV +0.7, OIL +0.7, LICHSGFIN +0.6 | BSE -10.7, MOTILALOFS -8.3, SWIGGY -7.3, POLICYBZR -6.6, ICICIAMC -6.0 |
| [India-Pakistan military crisis (terror attack, cross-border strikes) after Op Sindoor (May 2025)](events/EV_INDIA_PAK_CRISIS.md) | risk_scenario | 0.09 | MAZDOCK +5.5, SOLARINDS +5.4, HAL +5.1, BDL +5.1, BEL +4.4 | MOTILALOFS -8.0, JIOFIN -6.9, ICICIAMC -6.7, IREDA -6.7, 360ONE -5.9 |
| [Fed cuts >=25 bp by Apr 2027 (growth scare / AI bust / lower inflation)](events/EV_FED_H1_2027_CUTS.md) | anticipated | 0.25 | BSE +8.5, MOTILALOFS +6.6, SWIGGY +5.6, POLICYBZR +5.1, YESBANK +4.8 | JSWSTEEL -0.7, SAIL -0.6, TMPV -0.5, OIL -0.5, ONGC -0.5 |
| [RBI MPC Apr 2027 (~8 Apr): cuts 25 bp (hiking cycle reversed)](events/EV_RBI_APR27_CUT25.md) | anticipated | 0.10 | YESBANK +5.4, PRESTIGE +5.4, TATACAP +5.3, BAJFINANCE +5.2, GODREJPROP +5.1 | LICHSGFIN -1.2, PAYTM -0.5, BANKINDIA -0.0 |

## Events since June 2026 with the widest footprint (model impact, % equity, raw)
| event | winners | losers |
|---|---|---|
| [Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct)](events/EV_IRAN_WAR_HORMUZ_OIL.md) | OIL +35.8, ONGC +27.5, MCX +7.7, COALINDIA +6.5 | YESBANK -24.0, INDIGO -23.2, BPCL -20.7, GMRAIRPORT -19.2 |
| [Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October](events/EV_FPI_RECORD_OUTFLOW_26.md) | JSWSTEEL +1.9, SAIL +1.8, TATASTEEL +1.3, OIL +1.3 | MOTILALOFS -17.3, ICICIAMC -12.5, PAYTM -11.9, 360ONE -10.8 |
| [CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74%](events/EV_CPI_REACCEL_SEP26.md) | PIIND +0.2, UPL +0.1 | YESBANK -12.2, BAJFINANCE -11.2, TATACAP -10.9, GMRAIRPORT -9.4 |
| [US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004](events/EV_UST_SELLOFF_SEP26.md) | TMPV +1.3, JSWSTEEL +1.2, SAIL +1.2, ONGC +0.8 | MOTILALOFS -5.8, BSE -4.9, YESBANK -4.7, MUTHOOTFIN -4.6 |
| [RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026)](events/EV_RBI_OCT26_HIKE25.md) | LICHSGFIN +1.2, BANKINDIA +0.6, PAYTM +0.5, MAHABANK +0.0 | BAJFINANCE -5.4, TATACAP -5.3, PRESTIGE -5.3, YESBANK -5.0 |
| [Gold and silver slump from January 2026 peaks (silver -53%, gold -24%)](events/EV_PRECIOUS_METALS_CRASH_2026.md) | PREMIERENE +3.3, WAAREEENER +1.6, TMPV +1.4, JSWSTEEL +1.2 | HINDZINC -8.8, MCX -6.3, MUTHOOTFIN -5.6, MOTILALOFS -5.3 |
| [RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high](events/EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26.md) | HDFCLIFE +0.6, SBILIFE +0.3, MFSL +0.3, RVNL +0.1 | YESBANK -6.2, ADANIGREEN -5.7, BAJFINANCE -5.7, TATACAP -5.4 |
| [Fed delivers first hike in years (16 Sep 2026), new chair Warsh](events/EV_FED_SEP26_HIKE.md) | JSWSTEEL +0.5, SAIL +0.4, OIL +0.4, TMPV +0.4 | BSE -5.9, MOTILALOFS -4.6, SWIGGY -3.8, POLICYBZR -3.4 |
| [2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015](events/EV_SWMONSOON26_DEFICIT.md) | ADANIPOWER +3.4, COALINDIA +1.0, AMBUJACEM +0.9, ENRIN +0.6 | INDUSINDBK -8.7, IDFCFIRSTB -7.5, YESBANK -6.2, BANKINDIA -5.0 |
| [Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners](events/EV_OMC_FUEL_FREEZE_LOSSES.md) | PRESTIGE +1.6, JSWENERGY +1.4, BAJFINANCE +1.4, GODREJPROP +1.3 | HINDPETRO -36.0, IOC -19.5, BPCL -17.9, BANKINDIA -3.2 |

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
| COCHINSHIP | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → C_RED_SEA → F_SHIPPING_RATES → COCHINSHIP | -1.75% | -1.02% |
| JINDALSTEL | 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → JINDALSTEL | +2.84% | +1.02% |
| JINDALSTEL | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → JINDALSTEL | -1.71% | -0.99% |
| SAIL | 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → SAIL | +2.67% | +0.95% |
| SAIL | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → SAIL | -1.60% | -0.93% |
| INDUSINDBK | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +1.28% | +0.87% |
| JINDALSTEL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → JINDALSTEL | -1.66% | -0.83% |
| YESBANK | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → YESBANK | +0.86% | +0.78% |
| JINDALSTEL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL | +2.22% | +0.78% |
| SAIL | 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → SAIL | -1.55% | -0.78% |
| VAML | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → F_ALUMINIUM → VAML | +2.20% | +0.77% |
| IDFCFIRSTB | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +1.12% | +0.76% |
| COCHINSHIP | 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → C_RED_SEA → F_SHIPPING_RATES → COCHINSHIP | +2.10% | +0.75% |
| SAIL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL | +2.08% | +0.73% |
| COALINDIA | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_COAL_INDIA → COALINDIA | -1.03% | -0.70% |
| POWERINDIA | 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | -1.03% | -0.70% |
| FEDERALBNK | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.78% | +0.70% |
| AXISBANK | 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → AXISBANK | +0.73% | +0.66% |
| PRESTIGE | 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → PRESTIGE | -1.02% | -0.66% |
| INDUSINDBK | 3 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +0.92% | +0.65% |
| PRESTIGE | 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → PRESTIGE | -1.79% | -0.64% |
| JINDALSTEL | 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → JINDALSTEL | +1.80% | +0.63% |
| PRESTIGE | 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → PRESTIGE | +1.07% | +0.62% |

## Strongest 2nd–4th-order chains from what already moved since 1 June 2026 (raw model impact)
| company | order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|---|
| ENRIN | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ENRIN | +1.50 | events | +2.88% |
| LODHA | 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → LODHA | +1.70 | events | -2.45% |
| GODREJPROP | 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → GODREJPROP | +1.70 | events | -2.45% |
| BSE | 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → BSE | -1.60 | events | -2.30% |
| GROWW | 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → GROWW | -1.60 | events | -2.30% |
| POWERINDIA | 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERINDIA | +1.20 | events | +2.30% |
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
| POLYCAB | 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → POLYCAB | +1.70 | events | -1.22% |
| ABB | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ABB | +1.50 | events | +1.20% |
| CGPOWER | 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → CGPOWER | +1.50 | events | +1.20% |
| GVT&D | 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → GVT&D | +0.50 | events | +1.20% |

## Files
- `RANKINGS.md` — all 200 stocks; `stocks/<TICKER>.md` — per-stock deep dive (drivers by order, events, chains, analyst profile); `events/<EVENT>.md` — per-event winners/losers by order; `EVENTS.md`; `DRIVERS.md`.
- Data: `results/rankings.csv`, `results/sensitivity_by_order.csv`, `results/event_impacts.csv`, `results/edges_all.csv`.
- Method: `PLAN.md`, `docs/AGENT_SPEC.md`; review trail: `review/`, `graph/*overrides*.json`.
