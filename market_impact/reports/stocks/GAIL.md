# GAIL — GAIL (India) Ltd.
*NIFTY_NEXT_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +1.1%** (rank 62 / 30 of 200 for 3m / 12m); beta 1.28
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.4%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.8% … P90 +5.7%; plausible 12m relative-return range incl. stock-specific noise: -20.0% … +26.1%
- Decomposition (12m): 0.5 × forward event exposure +1.2% (3m +0.9%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.5% (beta-adjusted) vs a realised market-adjusted move of +7.9% — gap -8.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.70 | +0.05 | +0.75 | +0.44 |
| Sector | +0.12 | +0.27 | +0.39 | +0.18 |
| Theme | +0.00 | +0.06 | +0.06 | +0.04 |
| Geopolitics | +0.03 | +0.13 | +0.16 | +0.12 |
| Company catalysts | +0.57 | +0.00 | +0.57 | +0.00 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.73 | -0.33 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+1.05** | **+0.35** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| PNGRB gas pipeline tariff regulation (`NEW_PNGRB_TARIFF`) | +1 = tariff cut / unified-tariff reduction of ~10% | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.45 | +1.50 | -0.03 | -0.00 | -0.02 | — |
| Global natural gas / LNG price (`F_GAS_GLOBAL`) | +15% gas/LNG price | -1.42 | -1.50 | +0.00 | +0.08 | +0.00 | +69.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.21 | -1.20 | +0.03 | -0.04 | -0.01 | -1.1% |
| Petrochemical / polymer spreads (`F_PETROCHEM_SPREADS`) | +10% polymer-naphtha spreads | +1.10 | +1.10 | +0.00 | +0.00 | +0.00 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +0.95 | +0.00 | +0.96 | -0.02 | +0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.92 | +0.00 | +0.96 | -0.04 | -0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.89 | -0.49 | +0.18 | -0.45 | -0.13 | — |
| Fertiliser subsidy generosity (`P_FERT_SUBSIDY`) | +1 = higher subsidy | +0.79 | +0.80 | +0.00 | +0.00 | -0.01 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +0.66 | +0.00 | +0.54 | +0.13 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.63 | -0.60 | +0.05 | -0.07 | -0.01 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +0.61 | +1.20 | -0.45 | -0.15 | +0.01 | +0.0% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.58 | +0.00 | -0.59 | -0.06 | +0.07 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +0.57 | +0.00 | +0.60 | -0.02 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| LNG supply disruption: ~90 delayed Qatar cargoes to Petronet; India re-sources to US/UAE; Henry Hub proxy only +12% in 3m (`EV_LNG_HORMUZ_DISRUPTION`) | occurred | 1.00 | -1.4% | -1.4% | -1.5 | +0.0 | +0.1 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -0.9% | -0.9% | -0.5 | -0.5 | +0.1 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.1 | -0.5 | -0.2 | -0.2 |
| Cabinet approves higher rabi-season NBS subsidy rates for P&K fertilisers (and DAP special package) (`EV_NBS_RABI_HIKE`) | anticipated | 0.95 | +0.8% | +0.8% | +0.8 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.7 | -0.1 | +0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.7% | +0.7% | +0.8 | -0.0 | -0.0 | -0.0 |
| Cold winter + low EU storage + Hormuz LNG loss: global gas/LNG spike (`EV_EU_WINTER_GAS_SPIKE`) | risk_scenario | 0.20 | -3.5% | -0.7% | -3.8 | +0.0 | +0.2 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.7% | -0.7% | -0.6 | +0.0 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.5 | +0.0 | +0.0 |
| Union Budget FY28 (1 Feb 2027) raises agri/rural spending and fertiliser subsidy; PM-Kisan/rural jobs top-up (`EV_BUDGET27_AGRI_RURAL`) | scheduled | 0.70 | +0.7% | +0.5% | +0.4 | +0.3 | -0.0 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | +0.4% | +0.4% | +0.4 | -0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +0.4% | +0.4% | +0.4 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GAIL | -1.56% | -0.86% |
| 1 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → GAIL | +0.80% | +0.76% |
| 1 | EV_EU_WINTER_GAS_SPIKE ⇒ F_GAS_GLOBAL → GAIL | -3.75% | -0.75% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GAIL | +2.64% | +0.66% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_GAS_GLOBAL → GAIL | -1.50% | -0.38% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ P_FERT_SUBSIDY → GAIL | +0.40% | +0.36% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_GAS_GLOBAL → GAIL | +0.54% | +0.30% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → GAIL | -1.56% | -0.28% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ P_FERT_SUBSIDY → GAIL | +0.40% | +0.28% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → GAIL | +0.55% | +0.28% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → GAIL | +0.49% | +0.27% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → GAIL | +0.40% | +0.27% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → GAIL | -2.25% | -0.27% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → GAIL | +5.40% | +0.27% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GAIL | -0.60% | -0.25% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GAS_GLOBAL → GAIL | +4.61 | observed | -6.92% |
| 1 | F_GDP_IN → GAIL | +0.50 | events | +0.75% |
| 1 | F_REPO_IN → GAIL | +1.00 | events | -0.60% |
| 1 | C_MIDEAST_CONFLICT → GAIL | +1.00 | events | -0.49% |
| 1 | F_POWER_DEMAND_IN → GAIL | +1.20 | events | +0.48% |
| 1 | F_USDINR → GAIL | -0.37 | observed | +0.44% |
| 1 | P_FERT_SUBSIDY → GAIL | +0.50 | events | +0.40% |
| 2 | F_CHINA_GDP → F_PETROCHEM_SPREADS → GAIL | +0.30 | events | +0.13% |
| 3 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → GAIL | -0.47 | observed | +0.03% |
| 3 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → GAIL | +0.40 | events | +0.03% |
| 3 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → GAIL | +0.30 | events | +0.03% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PETROCHEM_SPREADS → GAIL | +0.40 | events | -0.02% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-02 | Q3 FY27 results (GAIL typically reports late Jan/early Feb; exact date not announced) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Board declares interim dividend / record date for FY27 (payout ~41%; yield 2.95%) | corporate_action | 0.60 | +0.8% | +0.45% |
| 2027-03 | Normalisation (or re-escalation) of Hormuz LNG flows: spot LNG easing restores industrial/fertiliser volumes | other | 0.45 | +0.5% | +0.23% |
| 2027-06 | GAIL Gas IPO DRHP filing (board approved 30 Oct 2026; listing guided FY28, up to 25% dilution) | corporate_action | 0.35 | +1.8% | +0.61% |
| 2027-06 | PNGRB decision on revised unified/network tariffs | regulatory | 0.20 | -2.0% | -0.40% |
| 2028 | Usar (Maharashtra) petchem and Pata expansion commissioning (timing model knowledge) | capex | 0.15 | +1.8% | +0.26% |

## Analyst profile (agent research, sourced)
# GAIL (India) Ltd. — market impact profile (as of 2026-11-05)

## Business
GAIL is India's dominant gas midstream company. About half of the pipeline grid, a large share of imported-LNG marketing, LPG extraction (six plants), an 810 ktpa polyethylene plant at Pata and stakes in Petronet LNG, city-gas companies and OPaL make up the portfolio. Roughly 75% of revenue is gas trading, but profit is much more evenly split: transmission (regulated PNGRB tariffs, volume driven), marketing (spread between a blend of Henry-Hub-linked, oil-linked and spot supply and the price paid by fertiliser, power, refining and CGD customers), LPG/liquids (crude-linked), and petrochemicals (spread driven, loss-making in weak years). Segment shares are model knowledge (FY25) and should be refreshed from the Q2 FY27 investor presentation.

## What moves the stock (ranked, with arithmetic in the JSON)
1. **Gas marketing spread and LNG price (F_GAS_GLOBAL, C_MIDEAST_CONFLICT)** — the swing factor. High spot LNG hurts volumes; contracted cheap supply (US cargoes, Henry-Hub-linked) earns outsized margin when spot is high. Net weights are small and negative (-1.5) because volume destruction is a durable loss while margin windfalls fade.
2. **Liquid-fuel prices (F_BRENT)** — LPG, liquids and polymer realisations rise with crude, and industrial customers switch to gas when diesel/LPG/fuel oil are dear. H1 FY27 PAT of Rs 9.4k cr versus Rs 7.6k cr for the whole of FY26 shows how powerful this was while Brent exceeded $100; the pack shows no statistically significant Brent beta, so confidence is low.
3. **PNGRB tariff policy (NEW_PNGRB_TARIFF)** — transmission is ~30% of EBITDA and tariffs are regulated; a 10% cut costs about 3% of equity value.
4. **Volumes / GDP and fertiliser policy (F_GDP_IN, P_FERT_SUBSIDY, F_POWER_DEMAND_IN)**.
5. **Rates and rupee (F_REPO_IN, F_USDINR)** — small earnings impact, larger through the discount rate on a PSU dividend stock.
6. **Petchem spreads (F_PETROCHEM_SPREADS)**.

## Worked transmission examples
- **Geopolitics to gas volumes (4 orders).** Hormuz re-escalation (C_MIDEAST_CONFLICT, order 0) raises spot LNG (order 1) -> fertiliser plants and CGD industrial users cut offtake or switch to LPG/coal (order 2: GAIL transmission throughput falls, marketing sells less) -> lower regulated EBITDA and receivables stress at fertiliser/discom customers (order 3) -> GAIL trims dividend headroom and capex, and the stock de-rates (order 4). The offset path: the same escalation lifts Brent, raising LPG and petchem realisations (positive for GAIL) and pushing the government to maintain subsidy support for urea, which preserves pool-gas offtake.
- **Rupee to margin.** Crude shock -> INR weaker (F_USDINR up, as seen with Brent at $110) -> rupee cost of USD-priced LNG rises before price formulae reset -> marketing margin squeezed for 1-2 quarters -> RBI cannot cut because of imported inflation (repo unchanged) -> PSU dividend-yield stocks lose their rate-cut tailwind.
- **Regulatory chain.** Government wants cheaper gas for CGD/fertiliser -> PNGRB unified-tariff cut -> transmission EBIT -10% -> equity -3%; second-order, lower tariffs slow pipeline capex and delay the national grid completion.
- **Coal substitution.** Spot LNG up -> gas-based power and industrial users revert to coal/pet-coke (links to COALINDIA volumes) -> GAIL gas demand falls, domestic coal offtake rises (order 3), shifting equity value from GAIL to coal producers without any direct company-to-company edge (both attach to their own factor nodes).

## Current situation
Q2 FY27 (Sep 2026): consolidated sales Rs 47,139 cr, operating profit Rs 6,992 cr, net profit Rs 4,724 cr (EPS Rs 7.18) vs Rs 1,989 cr a year ago; standalone PAT Rs 4,650 cr. Management called out record volumes; analysts noted a slight miss. The board approved listing GAIL Gas with up to 25% dilution in FY28 and signed an MoU with RCF for a Maharashtra fertiliser project. FIIs have been buying (13.0% to 16.6% in two quarters) while DIIs sold. The stock is up 8.2% in a month and 2.5% in 12 months at ~9.6x trailing earnings; trailing P/E flatters because H1 FY27 included a marketing windfall. Brent is ~$95 after falling 5.6% in a month on US-midterm hopes for a Middle East settlement.

## Upcoming events
Q3 FY27 results (~Feb 2027), interim dividend, GAIL Gas DRHP (FY27-28), PNGRB tariff review, Hormuz normalisation, Petronet's renewed Qatar deal, Usar petchem project milestones.

## Bull case
Marketing margins remain elevated as liquid fuels stay dear; volumes recover as spot LNG eases; GAIL Gas IPO crystallises subsidiary value; dividend yield and FII inflows support re-rating towards 1.5x book.

## Bear case
Hormuz normalisation removes marketing windfall (Q4 FY26-type margins of 4% reappear); tariff cut; petchem losses; fertiliser offtake shrinks; H1 earnings prove non-recurring and P/E on normalised EPS (~Rs 14) is ~13x.

*Weights are exposure estimates with ranges, not return forecasts; the Director computes scenario-implied relative returns from the graph. Facts from model memory are labelled; dated facts cite the pack and the Google News RSS queries listed in the JSON.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.