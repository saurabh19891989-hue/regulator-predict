# INDUSTOWER — Indus Towers Ltd.
*MIDCAP_100 · Telecommunication · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months +0.1%** (rank 132 / 96 of 200 for 3m / 12m); beta 0.88
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.0%): 3 months 49%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.4% … P90 +2.4%; plausible 12m relative-return range incl. stock-specific noise: -28.7% … +26.9%
- Decomposition (12m): 0.5 × forward event exposure -0.1% (3m -0.5%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -2.8% (beta-adjusted) vs a realised market-adjusted move of -15.9% — gap +13.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Mobile tariff hikes (`P_TELECOM_TARIFFS`) | +10% ARPU via tariff hike | +1.97 | +2.00 | +0.00 | -0.02 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.69 | +1.50 | +0.15 | +0.01 | +0.03 | — |
| Government AGR/spectrum dues relief for stressed telcos (`NEW_AGR_SPECTRUM_RELIEF`) | +1 = further material relief worth ~Rs20,000 cr NPV | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.40 | -0.80 | -0.25 | -0.20 | -0.14 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.30 | +0.00 | -0.93 | -0.39 | +0.02 | — |
| Net tenancy exits from towers (Jio/others) (`NEW_TOWER_TENANCY_EXITS`) | +1 = 5,000 net tenancy exits | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.15 | +0.00 | -0.36 | -0.47 | -0.32 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.01 | +0.00 | -0.66 | -0.32 | -0.03 | +3.5% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.97 | +0.00 | -0.80 | -0.14 | -0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.87 | -0.50 | -0.39 | +0.03 | -0.00 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.86 | +0.00 | -0.82 | -0.09 | +0.05 | +9.4% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.85 | +0.00 | +0.28 | +0.33 | +0.23 | — |
| Foreign portfolio flows into Indian government/corporate bonds (FAR, index-linked) (`NEW_FPI_DEBT_FLOWS`) | +US$5 bn net debt inflow per quarter | +0.79 | +0.00 | +0.72 | +0.05 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.7% | -3.7% | -3.3 | -0.3 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.3% | +2.1% | +3.8 | +0.4 | +0.0 | +0.1 |
| Broad mobile tariff hike by Jio/Airtel (12-15%) (`EV_TELECOM_TARIFF_HIKE_2027`) | anticipated | 0.75 | +2.4% | +1.8% | +2.4 | +0.0 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.1 | -0.5 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | -0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.2 | -0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.9 | -0.2 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -5.8% | -1.0% | -5.8 | +0.0 | -0.0 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.0% | +1.0% | +0.8 | +0.2 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.6% | -0.9% | +0.0 | -3.3 | -0.4 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → INDUSTOWER | +3.75% | +1.88% |
| 1 | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → INDUSTOWER | +2.40% | +1.80% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → INDUSTOWER | -1.60% | -0.80% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → INDUSTOWER | -1.50% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → INDUSTOWER | -2.25% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDUSTOWER | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDUSTOWER | -1.44% | -0.36% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → INDUSTOWER | -0.40% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → INDUSTOWER | -0.60% | -0.36% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → INDUSTOWER | -0.60% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → INDUSTOWER | -2.00% | -0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → INDUSTOWER | -1.40% | -0.35% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → INDUSTOWER | +0.60% | +0.31% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_GSEC_10Y_IN → INDUSTOWER | -0.40% | -0.28% |
| 1 | EV_RBI_FEB27_HOLD ⇒ F_GSEC_10Y_IN → INDUSTOWER | +0.40% | +0.26% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → INDUSTOWER | +1.55 | director_override | -3.10% |
| 1 | F_FPI_FLOWS → INDUSTOWER | -1.60 | events | -2.40% |
| 1 | F_POWER_PRICE_IN → INDUSTOWER | +1.90 | director_override | -0.95% |
| 1 | F_REPO_IN → INDUSTOWER | +1.00 | events | -0.50% |
| 1 | F_USDINR → INDUSTOWER | -0.37 | observed | +0.30% |
| 1 | F_GDP_IN → INDUSTOWER | +0.50 | events | +0.25% |
| 1 | P_TELECOM_TARIFFS → INDUSTOWER | +0.05 | events | +0.10% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → INDUSTOWER | +0.50 | director_override | +0.02% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → INDUSTOWER | -0.30 | events | -0.02% |
| 1 | F_BRENT → INDUSTOWER | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Interim/final dividend declarations (dividend yield 3.7%) | corporate_action | 0.50 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (net tenancy additions, Vi payments, Africa) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Jio tenancy exits (~5,000 by H2 FY27 per Motilal Oswal assumption) | other | 0.40 | -2.2% | -0.90% |
| 2027-03 | Vodafone Idea funding close / default-risk resolution | other | 0.60 | +2.2% | +1.35% |

## Analyst profile (agent research, sourced)
# INDUSTOWER — Indus Towers Ltd. (Midcap 100) — profile as of 2026-11-05

## Business
India's largest passive telecom infrastructure company: 270,480 towers and 440,153 co-locations at 30-Sep-2026 (sharing factor 1.63). Revenue is contracted with operators (Airtel, Vodafone Idea, Jio), escalated annually, and energy is largely passed through. Airtel is the largest tenant and ~50% shareholder (model knowledge). Q2 FY27 (company release, 2026-10-27): revenue Rs8,516 cr (+4.0% y/y), EBITDA Rs4,633 cr (+0.4%, margin 54.4%), PAT Rs1,793 cr (-2.5%), AFFO Rs3,023 cr (-0.5%). Growth is volume-led (co-locations +5.9% y/y) with falling sharing revenue per operator (-1.6% y/y).

## What moves the stock (ranked)
1. **Vodafone Idea's solvency and rollouts (company link 0.10 per 1% Vi equity move; NEW_AGR_SPECTRUM_RELIEF +1.5).** Vi is a large tenant (est. ~30% of revenue); funding close supports 5G loadings (Motilal assumed ~50,000 Vi 5G loadings over FY26-29 and ~30,000 Vi tenancies).
2. **Tenancy exits and pricing (-1.2 per 5,000 exits).** Jio exits of ~5,000 in H2 FY27 are assumed by Motilal Oswal; lean-tower and multi-tenancy pricing is already compressing revenue per operator.
3. **Discount rate (-2.0 per +25bp G-sec).** A 3.7% yielder trading at 14x P/E behaves like a bond proxy.
4. **Energy pass-through leakage (-0.5), rupee (-0.8), flows (+1.5).**

## Transmission examples
- Telecom tariff hike -> Vi ARPU up -> Vi can fund rollout and pay Indus on time -> Indus tenancy ratio up and provisions low (3rd order) -> AFFO and dividend capacity up -> Airtel's ~50% stake value up (company link on BHARTIARTL, 0.039).
- Middle East escalation -> Brent up -> diesel for off-grid sites up -> pass-through lag leaves small cost leakage; simultaneously INR weaker -> imported battery/equipment capex up; RBI on hold -> G-sec yield up -> bond-proxy de-rating.
- Government AGR relief -> Vi survives -> Vi's 5G densification -> Indus loadings (2nd) -> tenancy ratio >1.65 (3rd) -> EBITDA growth reaccelerates (4th).
- Jio own-tower consolidation -> tenancy exits -> sharing factor falls -> operating leverage works in reverse (high drop-through).

## Current situation and upcoming
Nomura raised target to Rs510 on strong tenancy adds (2026-10-29); stock at Rs380, flat over 12m, 52-week range Rs356-482. FIIs sold (25.1% -> 21.7%) while DIIs bought (19.7% -> 22.9%). Africa initial rollouts "progressing as planned" per CEO (2026-10-27). Next: Q3 results (Jan 2027), Vi funding close, any Jio exits.

## Bull and bear
Bull: Vi funding closes, 5G loadings accelerate, AFFO growth plus capital returns, Nomura Rs510. Bear: Jio exits, Vi stress, per-operator price erosion, energy margin leakage, bond-yield rise.

## Gaps
Customer concentration shares (Airtel ~40-45%, Vi ~30%, Jio ~15-20%) are model-knowledge estimates and should be verified from the annual report.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.