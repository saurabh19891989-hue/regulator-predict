# APLAPOLLO — APL Apollo Tubes Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months +0.6%** (rank 109 / 90 of 200 for 3m / 12m); beta 1.00
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.0%): 3 months 49%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.2% … P90 +5.9%; plausible 12m relative-return range incl. stock-specific noise: -19.3% … +28.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +5.7% beta-adjusted vs realised market-adjusted move +17.9%); forward event exposure +4.3% (3m +0.7%; half assumed priced); company-specific events -0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.65 | +2.50 | +0.23 | +0.00 | -0.08 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.21 | +0.00 | -1.30 | -0.61 | -0.30 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.97 | +2.00 | +0.00 | -0.04 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.61 | -1.20 | -0.27 | -0.12 | -0.02 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +1.50 | +1.50 | +0.02 | -0.02 | -0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.36 | +1.50 | +0.00 | -0.09 | -0.05 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.13 | +0.00 | -0.80 | -0.31 | -0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.13 | +0.00 | -0.08 | -0.72 | -0.33 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.91 | -0.80 | -0.10 | +0.08 | -0.09 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.90 | +1.00 | +0.00 | +0.00 | -0.10 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +0.74 | +0.00 | +0.74 | +0.02 | -0.01 | +20.6% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +0.65 | +0.00 | -0.12 | +0.58 | +0.19 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.64 | +0.00 | +0.32 | +0.22 | +0.10 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +0.62 | +0.00 | +0.64 | +0.00 | -0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.6 | -0.7 | -0.3 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.4% | +2.4% | +2.5 | +0.2 | -0.2 | -0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -2.2% | -2.2% | -1.2 | +0.5 | -0.7 | -0.8 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +2.1% | +2.1% | +2.1 | +0.0 | -0.0 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.1% | +1.9% | +2.0 | +0.2 | +0.0 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.8 | -0.1 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.2 | -0.5 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.4% | +0.8% | +1.1 | -0.2 | +0.2 | +0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -2.1% | -0.8% | -1.7 | +0.3 | -0.3 | -0.4 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.7 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.7% | -0.7% | -1.2 | -0.5 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.3 | -0.1 | -0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → APLAPOLLO | +2.00% | +1.80% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → APLAPOLLO | +1.50% | +0.68% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → APLAPOLLO | -2.40% | -0.67% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → APLAPOLLO | -3.00% | -0.54% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → APLAPOLLO | -1.20% | -0.48% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → APLAPOLLO | +0.80% | +0.46% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → APLAPOLLO | +0.60% | +0.36% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → APLAPOLLO | -1.38% | -0.35% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → APLAPOLLO | -0.96% | -0.34% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → APLAPOLLO | +0.60% | +0.33% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → APLAPOLLO | -1.20% | -0.32% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → APLAPOLLO | -0.48% | -0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → APLAPOLLO | -1.20% | -0.26% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → APLAPOLLO | -0.72% | -0.26% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ P_STEEL_DUTY_IN → APLAPOLLO | -0.40% | -0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOVT_CAPEX → APLAPOLLO | +1.00 | events | +2.50% |
| 1 | F_STEEL_INDIA → APLAPOLLO | +1.65 | events | +2.47% |
| 1 | C_MIDEAST_CONFLICT → APLAPOLLO | +1.50 | events | -1.20% |
| 1 | F_REPO_IN → APLAPOLLO | +1.00 | events | -1.20% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → APLAPOLLO | +1.70 | events | -0.82% |
| 1 | F_RURAL_DEMAND → APLAPOLLO | -0.25 | events | -0.25% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → APLAPOLLO | +0.50 | events | +0.24% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → APLAPOLLO | +1.00 | events | -0.21% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → APLAPOLLO | +1.00 | events | -0.16% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → APLAPOLLO | +0.50 | events | +0.15% |
| 1 | F_USDINR → APLAPOLLO | -0.37 | observed | -0.15% |
| 2 | F_GOVT_CAPEX → F_PRIVATE_CAPEX → APLAPOLLO | +1.00 | events | +0.12% |

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