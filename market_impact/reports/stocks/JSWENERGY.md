# JSWENERGY — JSW Energy Ltd.
*MIDCAP_100 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months +0.1%** (rank 107 / 101 of 200 for 3m / 12m); beta 0.96
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +29.7%): 3 months 49%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.1% … P90 +6.2%; plausible 12m relative-return range incl. stock-specific noise: -45.9% … +29.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.0 pp (model impact +6.0% beta-adjusted vs realised market-adjusted move -15.2%); forward event exposure -6.7% (3m -3.7%; half assumed priced); company-specific events +3.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -6.31 | +0.00 | -4.22 | -1.87 | -0.22 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +4.14 | +3.50 | +0.71 | -0.07 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.56 | -3.00 | -0.60 | -0.01 | +0.05 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.31 | +0.00 | +0.00 | -2.32 | -0.99 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.82 | +3.00 | -0.14 | +0.00 | -0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.73 | -2.50 | -0.25 | +0.00 | +0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.71 | -0.80 | -0.53 | -0.87 | -0.51 | -1.1% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -2.53 | +0.00 | -1.13 | -0.79 | -0.60 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.45 | -2.50 | +0.00 | +0.00 | +0.05 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.18 | +1.80 | +0.17 | +0.06 | +0.15 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.99 | +1.20 | +0.67 | +0.11 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.95 | +0.00 | -0.47 | -0.79 | -0.69 | +0.0% |
| Indian power exchange (IEX) prices (`F_POWER_PRICE_IN`) | +15% average spot power price | +1.80 | +1.80 | +0.00 | +0.00 | +0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.75 | +0.00 | -0.98 | -0.39 | -0.37 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -9.0% | -9.0% | +0.9 | -2.3 | -3.9 | -3.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -7.2% | -7.2% | +0.0 | -4.8 | -2.2 | -0.2 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +6.5% | +6.5% | +6.6 | -0.1 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.0% | -5.0% | -4.0 | -0.4 | -0.2 | -0.4 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +4.8% | +4.8% | +5.0 | -0.1 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -4.2% | -4.2% | -4.2 | +0.0 | +0.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.2% | -4.2% | -4.2 | +0.0 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -2.4 | -0.5 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.6% | +2.8% | +4.5 | +0.5 | +0.2 | +0.5 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +6.9% | +2.7% | +7.0 | -0.1 | +0.1 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -2.2 | -0.2 | -0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.6 | -0.5 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_PRICE_IN → JSWENERGY | +5.40% | +5.40% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → JSWENERGY | -3.97% | -3.97% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → JSWENERGY | -3.96% | -3.96% |
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → JSWENERGY | +3.50% | +3.50% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → JSWENERGY | -3.50% | -3.50% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → JSWENERGY | -3.00% | -3.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → JSWENERGY | -2.66% | -2.66% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JSWENERGY | +4.50% | +2.25% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → JSWENERGY | +5.40% | +2.16% |
| 1 | EV_INDIA_COAL_CRUNCH ⇒ F_POWER_PRICE_IN → JSWENERGY | +1.80% | +1.80% |
| 1 | EV_SOLAR_ALMM2_CELL_MANDATE ⇒ P_RENEWABLE_SUPPORT → JSWENERGY | +1.75% | +1.75% |
| 1 | EV_BESS_VGF_NOV26 ⇒ T_ENERGY_TRANSITION → JSWENERGY | +1.50% | +1.50% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → JSWENERGY | -1.31% | -1.31% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → JSWENERGY | -1.25% | -1.25% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → JSWENERGY | -3.00% | -1.20% |

## Analyst profile (agent research, sourced)
# JSWENERGY — JSW Energy Ltd. (as of 2026-11-05)

*Scenario/exposure analysis relative to the Nifty 200; not a validated forecast. Primary sources: Q2 FY27 earnings call (28 Oct 2026) and results presentation (BSE filings), screener.in, headline searches; sources in `JSWENERGY.json`.*

## Business
JSW Energy is the JSW Group's power company. Installed capacity is 15.1 GW (61% renewable, including hydro at Karcham Wangtoo, Baspa, Kutehr and Tidong, plus wind and solar) with a thermal base (Ratnagiri, Vijayanagar, Nandyal, KSK Mahanadi, newly acquired Maruti). 15.3 GW is under construction with PPAs signed, aimed at a 30 GW target for 2030. It has vertically integrated into turbines (10.7% of Toshiba JSW), boilers (GE Power India's boiler business, NCLT-sanctioned 1 Oct 2026) and wind blades. Q2 FY27: revenue Rs 6,658 cr (+24%), EBITDA Rs 3,907 cr (+23%), PAT Rs 1,141 cr (+38%), net generation 17.5 bn units (+17%). Net debt is Rs 65,576 cr (5.55x TTM EBITDA) at an average cost of 8.28%. FY27 capex is about Rs 20,000 cr.

## What moves the stock
1. **Funding cost and leverage (repo -3.0, spreads -2.5, G-sec -2.5).** The RBI hiked 25bp on 7 Oct; about 75% of term debt is floating, but roughly 90% of that is MCLR-linked and lags repo. The sector's highest leverage makes this the dominant risk, partially offset by refinancing as projects commission.
2. **Spot power and demand (+1.8, +1.2).** Merchant realisation of Rs 6.9/unit versus Rs 5.7 on the exchange; demand growth +11.1% in Q2 and +21% in October to date.
3. **Renewable policy and curtailment (+3.5).** Curtailment is 4.8% of generation; 60% of curtailed capacity moves to permanent GNA by end-Q3.
4. **Fuel (domestic coal -0.6; seaborne coal +0.4).** Insulated from API4 at about US$115/t by domestic FSA coal and job-work contracts.
5. **Group and cash flows.** JSW Steel group RTC demand (3 GW to 7 GW by 2032) and the holding in JSW Steel (links of 0.04 and 0.15).

## Worked transmission examples
- **Middle East escalation -> LNG shortage and Brent up (1st) -> Indian inflation worries and RBI tightening (2nd) -> MCLR and bond yields rise (3rd) -> floating-rate interest on Rs 65.6k cr of net debt rises and the 40x P/E derates (4th); in parallel, energy-security policy favours JSW's domestic-coal thermal and new Salboni/KSK units.**
- **Weak monsoon (-13%) -> record demand and critical coal stocks (1st) -> exchange prices Rs 5.7+/unit, merchant tariffs above Rs 6.9 (2nd) -> higher thermal merchant margins and more long-term thermal tenders (17 GW awarded, 18 GW pending) (3rd) -> JSW's thermal pipeline (Salboni 3,200 MW, KSK units) becomes more valuable (4th).** Hydro also gains where the Sutlej and Ravi basins outperform.
- **JSW Steel expansion to 80 MTPA -> captive power demand rises (1st) -> group MoUs of 4.5 GW converted into PPAs (2nd) -> JSW Energy capex and returns visibility improves (3rd) -> steel-price weakness feeds back into JSW Steel's credit and group sentiment (4th).**

## Current situation
Strong H1 but ROE only 7.5% and promoters have reduced their stake from 69.4% to 66.5% in a Rs 10,150 cr capital-unlocking exercise in 2026. ICRA and India Ratings affirmed AA/Stable. Stock Rs 521, -10% over six months, +5% over the last month.

## Upcoming events
GE Power India boiler closure, GNA conversion by end-Q3, 3 GW RE commissioning by March 2027, Q3 results in late January 2027, further group C&I tie-ups, and possible equity raising for the capex gap. See `company_events`.

## Bull and bear
**Bull:** commissioning ahead of plan, thermal tenders won, MCLR lag cushions rate hikes, group demand doubles. **Bear:** leverage 5.55x with floating debt as rates rise, execution slippage, equity dilution, merchant prices normalising.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.