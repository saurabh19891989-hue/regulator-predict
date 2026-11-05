# APLAPOLLO — APL Apollo Tubes Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months -0.4%** (rank 113 / 129 of 200 for 3m / 12m); beta 1.00
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.0%): 3 months 50%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.7% … P90 +2.4%; plausible 12m relative-return range incl. stock-specific noise: -31.8% … +30.1%
- Decomposition (12m): 0.5 × forward event exposure +0.2% (3m -0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +4.1% (beta-adjusted) vs a realised market-adjusted move of +17.9% — gap -13.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.19 | -0.00 | +0.19 | -0.05 |
| Regulatory | +0.00 | -0.01 | -0.01 | -0.00 |
| Sector | +0.25 | +0.16 | +0.41 | +0.15 |
| Theme | +0.00 | +0.04 | +0.04 | +0.03 |
| Geopolitics | +0.05 | -0.00 | +0.05 | +0.05 |
| Company catalysts | -0.39 | +0.00 | -0.39 | +0.12 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.57 | -0.26 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.42** | **-0.06** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.80 | +2.50 | +0.23 | +0.08 | -0.01 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.01 | +2.00 | +0.00 | -0.00 | +0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.58 | +1.50 | +0.00 | +0.05 | +0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.55 | -1.20 | -0.27 | -0.05 | -0.02 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +1.51 | +1.50 | +0.02 | -0.01 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.13 | +1.00 | +0.00 | +0.14 | -0.01 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.95 | +0.00 | -0.80 | -0.12 | -0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.91 | -0.80 | -0.10 | +0.05 | -0.07 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.80 | +0.00 | -0.61 | -0.11 | -0.08 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +0.75 | +0.00 | +0.74 | +0.01 | +0.00 | +20.6% |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +0.64 | +0.00 | +0.64 | +0.00 | -0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.60 | +0.00 | +0.23 | +0.17 | +0.20 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +0.58 | +0.00 | +0.47 | +0.15 | -0.03 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -0.58 | +0.00 | -0.38 | -0.19 | -0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.9% | +2.9% | +2.5 | +0.5 | -0.0 | -0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +1.7% | +1.7% | +1.7 | +0.0 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.2 | -0.4 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.8 | -0.1 | -0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -0.9% | -0.9% | -0.8 | -0.1 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.3 | -0.2 | -0.3 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.6% | -0.7% | -1.2 | -0.4 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.2% | +0.6% | +1.0 | -0.1 | +0.2 | +0.1 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | +0.6% | +0.6% | +0.6 | +0.0 | -0.0 | +0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +0.6% | +0.5% | +0.5 | +0.0 | +0.0 | -0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -3.8% | -0.5% | -2.0 | -1.4 | -0.3 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -1.8% | -0.4% | -1.6 | +0.2 | -0.2 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → APLAPOLLO | -1.20% | -0.50% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → APLAPOLLO | +0.50% | +0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → APLAPOLLO | +0.80% | +0.44% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → APLAPOLLO | -1.50% | -0.38% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → APLAPOLLO | +0.60% | +0.33% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → APLAPOLLO | -1.20% | -0.32% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → APLAPOLLO | -0.96% | -0.24% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → APLAPOLLO | -1.50% | -0.22% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ P_STEEL_DUTY_IN → APLAPOLLO | -0.40% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → APLAPOLLO | -1.20% | -0.22% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → APLAPOLLO | +0.30% | +0.21% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → APLAPOLLO | -0.74% | -0.19% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_GOVT_CAPEX → APLAPOLLO | +0.25% | +0.17% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → APLAPOLLO | +0.30% | +0.17% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → APLAPOLLO | +0.23% | +0.15% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → APLAPOLLO | +1.35 | events | +2.03% |
| 1 | F_REPO_IN → APLAPOLLO | +1.00 | events | -1.20% |
| 1 | C_MIDEAST_CONFLICT → APLAPOLLO | +1.00 | events | -0.80% |
| 1 | F_GOVT_CAPEX → APLAPOLLO | +0.20 | director_override | +0.50% |
| 1 | F_RURAL_DEMAND → APLAPOLLO | -0.25 | events | -0.25% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → APLAPOLLO | +1.55 | director_override | -0.25% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → APLAPOLLO | +0.50 | events | +0.24% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → APLAPOLLO | +1.00 | events | -0.21% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → APLAPOLLO | +0.50 | events | +0.15% |
| 1 | F_USDINR → APLAPOLLO | -0.37 | observed | -0.15% |
| 2 | F_CREDIT_SPREADS_IN → F_PRIVATE_CAPEX → APLAPOLLO | +0.50 | events | -0.09% |
| 2 | F_STEEL_INDIA → P_STEEL_DUTY_IN → APLAPOLLO | +1.35 | events | +0.08% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further product price revisions tracking HRC (steel +20.6% since 2026-06-01) | guidance | 0.50 | +0.5% | +0.25% |
| 2027-01 | Q3 FY27 volume update (company releases quarterly volumes in first days of quarter-end month+1) and results late Jan | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Safeguard duty / anti-dumping decision on flat steel (policy) | regulatory | 0.25 | -0.5% | -0.12% |
| 2027-03 | FY27 volume target (company guidance; Livemint 2026-10-06 asks if achievable) scored at Q4 | guidance | 0.60 | -1.5% | -0.90% |

## Analyst profile (agent research, sourced)
# APLAPOLLO - APL Apollo Tubes (Capital Goods / steel tubes)

## Business
APL Apollo converts hot-rolled and galvanised coil into branded structural tubes, hollow sections and pipes. Steel is about 90% of cost, so the earnings driver is EBITDA per tonne (about Rs6,000 in Q2 FY27) times volume (record 9.63 lakh tonnes, +13% YoY), not the steel price level. The company has almost no debt and trades at 46x earnings with 28% promoter holding and 34% FIIs.

## What moves the stock, ranked
1. **Volume demand** from housing, government and private capex (F_HOUSING_DEMAND +2.0, F_GOVT_CAPEX +2.5, F_PRIVATE_CAPEX +1.5 per SSU): the volume-growth narrative is the valuation.
2. **Domestic steel price** (F_STEEL_INDIA +1.5 per +7%): rising HRC gives short-lived inventory gains and price-hike momentum, but sustained high prices slow dealer buying. Global HRC is +20.6% since June, so the near-term tailwind has been strong.
3. **Rates** (-1.2 per +25bp): repo went to 5.50% on 2026-10-07; direct interest cost is trivial, but the multiple and dealer/builder credit are sensitive.
4. **Steel trade policy** (-0.5, wide range): safeguard duty raises HRC but also feeds integrated competitors.
5. **Geopolitics** (Middle East, -0.8): the call cited UAE disruptions.

## Transmission examples
- **China steel exports fall / global HRC up -> Indian HRC up -> APL raises prices (Sep 23, Oct 1) -> channel pre-buys ahead of hikes -> Q2 volume rebound -> later destocking if prices stall** (1st to 4th order including channel inventory).
- **Brent up -> INR weaker and inflation up -> RBI tighter (already 5.50%) -> housing finance costs up -> housing starts down -> tube volumes lower** (4th order, 6-12 months).
- **Government capex push -> railway and station projects -> hollow-section demand -> operating leverage lifts EBITDA/t.**
- **Safeguard duty on flat steel -> HRC up -> APL inventory gain but JSW/Tata branded tubes gain relative pricing power -> share contest.**

## Current situation
Q2 FY27 beat estimates on EBITDA; EBITDA/t held near Rs6,000 despite supply issues. Q1 had been weak (volume disruption). Stock is +12.6% over three months and +23% over twelve. DIIs have been the buyers (20.8%) while FIIs trimmed.

## Upcoming
Q3 volume update (early Jan 2027) and results late Jan; potential further price revisions; FY27 volume target scrutiny.

## Bull and bear
Bull: structural conversion of unorganised tubes to branded; steady 15-20% volume growth with EBITDA/t rising on value-added products. Bear: HRC retreat causes inventory losses and price cuts, competition from integrated mills, 46x P/E leaves no room for a volume miss.

Uncertainties: UAE exposure details, distributor count and export share are not verified from primary sources; the empirical +gas/+coal sensitivities have no fundamental channel and are ignored.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.