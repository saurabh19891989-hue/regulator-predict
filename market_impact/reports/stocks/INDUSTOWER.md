# INDUSTOWER — Indus Towers Ltd.
*MIDCAP_100 · Telecommunication · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months -0.5%** (rank 124 / 115 of 200 for 3m / 12m); beta 0.88
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.0%): 3 months 48%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.9% … P90 +2.1%; plausible 12m relative-return range incl. stock-specific noise: -24.7% … +27.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -3.0% beta-adjusted vs realised market-adjusted move -15.9%); forward event exposure -0.2% (3m -0.7%; half assumed priced); company-specific events +1.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.30 | +0.00 | -1.22 | -1.07 | -0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.01 | -2.00 | +0.00 | -0.01 | -0.00 | — |
| Mobile tariff hikes (`P_TELECOM_TARIFFS`) | +10% ARPU via tariff hike | +1.95 | +2.00 | +0.00 | -0.03 | -0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.87 | +0.00 | -0.36 | -0.79 | -0.72 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.71 | +1.50 | +0.15 | +0.01 | +0.05 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.58 | -0.80 | -0.25 | -0.33 | -0.20 | -1.1% |
| Government AGR/spectrum dues relief for stressed telcos (`NEW_AGR_SPECTRUM_RELIEF`) | +1 = further material relief worth ~Rs20,000 cr NPV | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.29 | +0.00 | +0.00 | -0.69 | -0.59 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.25 | +0.00 | -0.85 | -0.26 | -0.14 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.20 | +0.00 | -0.66 | -0.43 | -0.12 | +3.5% |
| Net tenancy exits from towers (Jio/others) (`NEW_TOWER_TENANCY_EXITS`) | +1 = 5,000 net tenancy exits | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.03 | +0.00 | -0.82 | -0.18 | -0.03 | +9.4% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.98 | +0.00 | -0.80 | -0.14 | -0.04 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +0.95 | +0.00 | +0.48 | +0.38 | +0.09 | +1.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.3% | -5.3% | -1.5 | -1.2 | -1.4 | -1.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.8% | -3.8% | -3.3 | -0.4 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -1.4 | -1.3 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -2.0 | -0.2 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.4% | +2.2% | +3.8 | +0.4 | +0.0 | +0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.8 | -0.2 | -0.0 |
| Broad mobile tariff hike by Jio/Airtel (12-15%) (`EV_TELECOM_TARIFF_HIKE_2027`) | anticipated | 0.75 | +2.3% | +1.8% | +2.4 | +0.0 | -0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -5.5% | -1.6% | +0.0 | -4.3 | -1.1 | -0.1 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.1% | -1.5% | -0.8 | -1.5 | -1.0 | -0.8 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.1 | -0.3 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → INDUSTOWER | -3.30% | -3.30% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → INDUSTOWER | -2.80% | -2.80% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → INDUSTOWER | +3.75% | +1.88% |
| 1 | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → INDUSTOWER | +2.40% | +1.80% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_PRICE_IN → INDUSTOWER | -1.50% | -1.50% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → INDUSTOWER | -1.49% | -1.49% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → INDUSTOWER | -1.05% | -1.05% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → INDUSTOWER | -0.88% | -0.88% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → INDUSTOWER | -1.60% | -0.80% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_GSEC_10Y_IN → INDUSTOWER | -0.78% | -0.78% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → INDUSTOWER | +0.75% | +0.75% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → INDUSTOWER | -0.66% | -0.66% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → INDUSTOWER | -2.24% | -0.63% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → INDUSTOWER | -0.63% | -0.63% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → INDUSTOWER | -1.50% | -0.60% |

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