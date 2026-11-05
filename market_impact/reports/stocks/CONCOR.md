# CONCOR — Container Corporation of India Ltd.
*MIDCAP_100 · Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.2%**, **12 months -0.5%** (rank 85 / 126 of 200 for 3m / 12m); beta 1.36
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.7%): 3 months 51%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.8% … P90 +2.8%; plausible 12m relative-return range incl. stock-specific noise: -27.5% … +26.4%
- Decomposition (12m): 0.5 × forward event exposure +1.8% (3m +0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -2.3%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +3.9% (beta-adjusted) vs a realised market-adjusted move of -11.2% — gap +15.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian Railways freight/haulage tariff changes (`NEW_RAIL_FREIGHT_TARIFF`) | +1 = +5% haulage/terminal access charges | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Private container train operators and road competition (`NEW_CONTAINER_LOGISTICS_COMPETITION`) | +1 = 2pp rail container market share loss for CONCOR | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.60 | +2.50 | +0.14 | -0.01 | -0.03 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -1.98 | -1.50 | -0.43 | -0.03 | -0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.69 | +0.00 | +1.60 | +0.08 | +0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.67 | +0.00 | +1.60 | +0.08 | -0.00 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +1.58 | +1.50 | +0.02 | +0.06 | +0.01 | — |
| Red Sea / Suez shipping disruption (`C_RED_SEA`) | +1 = disruption | -1.58 | -1.00 | -0.58 | +0.00 | +0.00 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -1.24 | +0.00 | -1.02 | -0.21 | -0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.20 | +0.00 | +0.90 | +0.29 | +0.01 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.20 | +0.00 | +0.67 | +0.37 | +0.15 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.09 | +0.00 | -0.31 | -0.67 | -0.10 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.05 | +0.00 | +1.00 | +0.05 | -0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.05 | +1.00 | +0.07 | -0.02 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | -0.2 | +0.1 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -0.8 | -0.5 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.6% | +1.3% | +2.5 | +0.2 | -0.1 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.3% | +1.3% | +1.2 | +0.1 | -0.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.2% | -1.2% | -1.1 | +0.0 | -0.1 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.2% | -1.2% | -0.5 | -0.5 | -0.1 | -0.1 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.0% | +1.0% | +0.8 | +0.2 | +0.1 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.3 | -0.5 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.2% | +0.8% | +0.0 | +0.7 | +0.4 | +0.1 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +1.0% | +0.8% | +0.9 | +0.0 | +0.1 | +0.0 |
| India-US interim trade agreement formally signed/announced (`EV_INDIA_US_INTERIM_DEAL_SIGNED`) | anticipated | 0.55 | +1.4% | +0.8% | +1.2 | +0.1 | +0.0 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.7% | +0.7% | +0.7 | +0.1 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CONCOR | +2.50% | +1.25% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → CONCOR | +0.90% | +0.72% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → CONCOR | -3.75% | -0.56% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → CONCOR | +0.67% | +0.45% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → CONCOR | -3.75% | -0.45% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → CONCOR | +0.75% | +0.41% |
| 1 | EV_INDIA_US_TALKS_COLLAPSE ⇒ P_US_TARIFF_INDIA → CONCOR | -2.25% | -0.40% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → CONCOR | +0.50% | +0.40% |
| 1 | EV_RED_SEA_CLOSURE ⇒ C_RED_SEA → CONCOR | -1.50% | -0.38% |
| 1 | EV_RED_SEA_SUEZ_NORMALISATION ⇒ C_RED_SEA → CONCOR | +0.80% | +0.36% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → CONCOR | +0.48% | +0.34% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → CONCOR | -0.64% | -0.32% |
| 2 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → P_US_TARIFF_INDIA → CONCOR | +0.96% | +0.29% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_GDP_IN → CONCOR | +0.33% | +0.28% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → CONCOR | -1.50% | -0.27% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → CONCOR | -1.60 | events | -1.60% |
| 1 | F_GDP_IN → CONCOR | +0.50 | events | +1.25% |
| 1 | F_GSEC_10Y_IN → CONCOR | +1.55 | director_override | -1.24% |
| 1 | C_RED_SEA → CONCOR | +1.00 | events | -1.00% |
| 1 | P_US_TARIFF_INDIA → CONCOR | -0.60 | events | +0.90% |
| 1 | F_SHIPPING_RATES → CONCOR | +0.30 | events | -0.18% |
| 2 | P_FDI_RULES → T_CHINA_PLUS_ONE → CONCOR | +0.50 | events | +0.15% |
| 1 | F_USDINR → CONCOR | -0.37 | observed | +0.15% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → CONCOR | -0.60 | events | +0.11% |
| 2 | C_US_CHINA_DECOUPLING → T_CHINA_PLUS_ONE → CONCOR | -0.10 | events | -0.07% |
| 1 | F_BRENT → CONCOR | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-11 | Record date for second interim dividend Rs1.90/share | corporate_action | 1.00 | -0.2% | -0.25% |
| 2027-01 | Q3 FY27 volumes (provisional throughput) and results (Feb) | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | FY27 volume guidance 9.5% vs H1 4.5%: miss/ revision risk | guidance | 0.60 | -3.5% | -2.10% |
| 2027-03 | Railway freight tariff / land licence fee policy changes | regulatory | 0.20 | -2.0% | -0.40% |

## Analyst profile (agent research, sourced)
# CONCOR — Container Corporation of India Ltd. (Midcap 100) — profile as of 2026-11-05

## Business
Government-controlled (54.8%) rail container logistics company: it hauls EXIM and domestic containers on Indian Railways, runs inland container depots and terminals, warehousing and cold chain. Debt-free. TTM revenue Rs9.1k cr (+1%), EBITDA Rs1.94k cr (21%), PAT Rs1.22k cr. Q2 FY27 throughput was 14.48 lakh TEU (+0.53% y/y; PSU Connect, Oct 2026), H1 +4.48%; Q2 consolidated profit Rs353.7 cr vs Rs380.0 cr a year earlier, with a Rs1.90 interim dividend (record date 2026-11-11, Indian Masterminds 2026-11-02). FY27 guidance of 9.5% volume growth (domestic +15%) looks hard to reach.

## What moves the stock (ranked)
1. **Rail haulage tariff and pass-through (-3.0 per +5%).** Haulage is ~58% of costs; railways set the price.
2. **Competition from private container train operators (-3.0)** and road; margins fell from 23% to 21% (FY23-26).
3. **EXIM trade volumes**: GDP (+2.5 per +1pp), US tariffs (-1.5 per +10pp), China+1 (+1.5), Red Sea (-1.0).
4. **Discount rate/ownership**: G-sec -0.8, FPI +1.0; government stake sale or policy changes (land licence fee) are event risks not priced here.

## Transmission examples
- US tariffs on Indian goods up -> India's US-bound exports fall -> export container bookings at JNPT/Mundra down (1st: -1.5) -> fewer EXIM rakes, higher fixed-cost burden (2nd) -> margin falls from 21% toward 18% (3rd) -> FY27 volume guidance cut; stock de-rates (4th).
- Middle East escalation -> Brent up -> diesel truck costs up -> modal shift to rail (+) but Red Sea/Gulf disruption cuts trade and raises shipping rates (-) -> INR weaker -> RBI on hold -> domestic demand slower.
- Railway ministry hikes haulage 5% -> CONCOR passes ~50% in 6 months -> EBITDA -5% -> private CTOs face same cost, limiting share loss, so impact fades.
- Pipavav container volumes +17% in Q2 (2026-10-07 headline) vs CONCOR flat suggests share pressure from port-linked logistics.

## Current situation and upcoming
Stock Rs441, -18.7% 12m and -13.9% 3m, 52w low Rs404. Pack's empirical sensitivities to wheat (+2.39, t +2.9) and iron ore (+3.67, t +2.2) are bulk-commodity/market-beta proxies with no mapped fundamental channel and are not modelled. Upcoming: Q3 volumes and results, guidance revision risk (prob 0.6), railway tariff decisions.

## Bull and bear
Bull: EXIM recovery, DFC double-stack, margin return to 24-25%, strategic sale. Bear: share loss to private operators, cost pass-through failure, US tariff impact, guidance miss.

## Gaps
Segment revenue split, haulage cost share and disinvestment status are estimates; Google News coverage for the ticker was noisy (non-India results).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.