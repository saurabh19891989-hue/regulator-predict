# HINDZINC — Hindustan Zinc Ltd.
*NIFTY_NEXT_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +1.2%** (rank 100 / 58 of 200 for 3m / 12m); beta 1.14
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +36.9%): 3 months 50%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.7% … P90 +8.4%; plausible 12m relative-return range incl. stock-specific noise: -53.6% … +57.9%
- Decomposition (12m): 0.5 × forward event exposure +4.9% (3m +2.0%; half assumed priced) + 0.5 × company-specific catalysts -1.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -7.1% (beta-adjusted) vs a realised market-adjusted move of -14.0% — gap +6.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Zinc / lead price (`F_ZINC_LEAD`) | +10% zinc | +3.80 | +3.80 | +0.00 | +0.00 | +0.00 | — |
| Silver price (`F_SILVER`) | +12% silver | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | -30.0% |
| Gold price (`F_GOLD`) | +8% gold (USD) | +2.76 | +0.00 | +2.80 | -0.03 | -0.02 | -8.4% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.16 | +2.20 | +0.10 | -0.08 | -0.06 | -1.1% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.63 | +0.00 | +1.52 | +0.09 | +0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +1.59 | +0.00 | +0.00 | +1.40 | +0.18 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.24 | +0.80 | +0.44 | +0.00 | +0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.10 | +0.00 | -0.26 | -0.85 | +0.01 | +2.2% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.02 | +0.00 | -0.21 | -0.61 | -0.20 | +9.4% |
| Gold import duty (`P_GOLD_IMPORT_DUTY`) | +5 pp | +0.97 | +1.00 | +0.00 | -0.03 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +0.66 | +0.00 | +0.44 | +0.22 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | +0.57 | +0.00 | +0.26 | +0.32 | -0.02 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -8.7% | -8.7% | -8.8 | +0.0 | +0.0 | +0.0 |
| Gold/silver rebound as Fed hike fears fade or Iran war ends (`EV_PRECIOUS_METALS_REBOUND_H1_2027`) | anticipated | 0.45 | +5.2% | +2.3% | +5.3 | +0.0 | -0.0 | -0.0 |
| Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`) | risk_scenario | 0.30 | -6.9% | -2.1% | -7.0 | +0.0 | +0.1 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.3 | -1.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.3 | -0.8 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -1.1% | -1.1% | -0.9 | -0.2 | +0.0 | +0.0 |
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.0% | +1.0% | +0.0 | +0.0 | +0.9 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -1.7% | -0.9% | +0.0 | -0.7 | -1.1 | +0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.9% | -0.9% | -0.8 | -0.1 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.7 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → HINDZINC | +5.25% | +2.36% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC | -7.00% | -2.10% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ZINC_LEAD → HINDZINC | +1.52% | +0.53% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → HINDZINC | +2.86% | +0.51% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → HINDZINC | -1.01% | -0.51% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_GOLD → F_SILVER → HINDZINC | -0.84% | -0.46% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → HINDZINC | -0.90% | -0.36% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → HINDZINC | -0.59% | -0.32% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → HINDZINC | -0.64% | -0.32% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_CHINA_GDP → F_ZINC_LEAD → HINDZINC | +0.61% | +0.27% |
| 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → F_GOLD → F_SILVER → HINDZINC | +1.01% | +0.25% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → HINDZINC | +1.00% | +0.25% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → HINDZINC | -0.40% | -0.24% |
| 3 | EV_FED_DEC26_HIKE25 ⇒ F_DXY → F_GOLD → F_SILVER → HINDZINC | -0.30% | -0.22% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → HINDZINC | +0.66% | +0.17% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_SILVER → HINDZINC | -2.50 | observed | -8.74% |
| 1 | F_GSEC_10Y_IN → HINDZINC | +1.55 | director_override | -1.24% |
| 1 | F_USDINR → HINDZINC | -0.37 | observed | -0.81% |
| 1 | F_COAL_INDIA → HINDZINC | +1.50 | events | -0.75% |
| 1 | F_POWER_PRICE_IN → HINDZINC | +1.90 | director_override | -0.57% |
| 2 | F_CHINA_GDP → F_ZINC_LEAD → HINDZINC | +0.30 | events | +0.46% |
| 2 | F_DXY → F_ZINC_LEAD → HINDZINC | +0.74 | observed | -0.45% |
| 1 | T_ENERGY_TRANSITION → HINDZINC | +0.30 | director_override | +0.24% |
| 2 | F_USDINR → P_GOLD_IMPORT_DUTY → HINDZINC | -0.37 | observed | -0.04% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Interim dividend declaration (H1 FY27 dividend already ~Rs11/share per press); payout drives Vedanta upstreaming | corporate_action | 0.50 | +0.5% | +0.25% |
| 2026-12 | Sulphuric acid realisations fall, reversing part of the Q2 cost gain | other | 0.30 | -1.8% | -0.53% |
| 2027-01 | Q3 FY27 results; silver realisation reset versus Q2 (spot US$52.5 vs implied Q2 ~US$75-80), cost guidance US$825-850/t test | results | 0.97 | -0.5% | -0.48% |
| 2027-02-01 | Windfall levy/export duty on zinc-silver earnings (tail; replaces conflated P_WINDFALL_EXPORT_TAX edge) *(review: [DIRECTOR_CE] RT_N50_A)* | regulatory | 0.05 | -6.0% | -0.30% |
| 2027-03 | Vedanta block/OFS sale of further HZL shares to delever (precedent: 1.6% sold Jun 2025; promoter holding -4.2 pp over 3 yrs) | corporate_action | 0.25 | -3.8% | -0.94% |
| 2027-03 | FY27 silver output of 680 t achieved (H1: 320-340 t); Chanderiya silver refinery ramp | guidance | 0.70 | +1.5% | +1.05% |
| 2027-06 | Government of India disinvestment OFS of part of its 27.9% stake | corporate_action | 0.10 | -4.0% | -0.40% |

## Analyst profile (agent research, sourced)
# HINDZINC — Hindustan Zinc Ltd. (Nifty Next 50) — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast; no expected-return number.

## 1. Business
Near-monopoly Indian zinc-lead producer (~75% of the domestic zinc market) and one of the world's largest integrated zinc and silver producers, with all mines and smelters in Rajasthan. Q2 FY27: refined metal 264 kt (+7%), mined metal 271 kt (+5%), silver 173 t (+20%); revenue Rs15,093 cr (+77%), EBITDA Rs9,285 cr (62% margin), PAT Rs6,412 cr (+142%). Zinc cost of production excluding royalty fell 29% to US$703/t and FY27 guidance was cut to US$825-850/t from US$975-1,000. Silver is ~27% of revenue (Rs4,111 cr) and, by press accounts, ~45% of profit. Vedanta Ltd owns ~61%, the Government of India 27.9%. Market cap Rs2.41 lakh cr, P/E 11.6, ROE 77%, dividend yield 2%.

## 2. What moves the stock, ranked
1. **Silver (w +3.5 per +12%).** Company disclosure: US$1/oz = Rs200-225 cr of annual EBITDA. That implies +2.5% equity per SSU from cash flow alone, but the empirical elasticity is +5.0 (t=5.7, the strongest in the pack): the share trades as a precious-metals proxy (silver, gold +4.8, t=3.8). Central weight sits between the two.
2. **Zinc (w +3.8 per +10%).** US$100/t = Rs725-750 cr; +10% is ~+6% EBITDA.
3. **Cost of production**, now falling (zinc COP -29%, driven by renewable power, higher volumes and sulphuric-acid by-product credits). A fall in acid prices would reverse part of this.
4. **USD/INR (+2.2 per +3%)** and **long rates (-0.8 per +25 bp)**.
5. **Policy/ownership tail risks:** royalty (-1.5), windfall levy (-4 if imposed), government OFS, further Vedanta stake sales.
6. Coal and power (-0.5, -0.3): small, partly hedged by captive and renewable supply.

## 3. Transmission chains
**Precious-metals crash chain (4th order).** Iran war lifts oil and inflation -> Fed hikes (Sept 16, 4.00% funds rate) and 10y UST above 4.9% -> real yields and the dollar rise -> silver falls 30% since June (-53% from the January peak) -> HZL's silver realisation drops from an implied ~US$75-80/oz in Q2 to US$52.5 spot (about Rs5,000+ cr annual EBITDA at the company sensitivity, ~14% of annualised EBITDA) -> the stock falls (observed: -10% in six months) -> Vedanta Ltd, which receives HZL dividends (and carries parent-level debt), falls by ~0.75x -> Vedanta group credit spreads widen, making refinancing of the pledged-share bond structure harder -> pressure for more HZL stake sales -> HZL falls again (group contagion). The reverse (US-Iran deal, lower yields) lifts the whole chain; event odds of a H1-2027 precious-metals rebound are 0.45.

**Zinc chain.** China property/infrastructure stimulus (CEWC Dec; event odds of a larger package 0.45) -> China GDP/steel galvanising demand and smelter-capacity discipline -> LME zinc up -> HZL EBITDA +6% per +10% -> plus lead/silver by-product and acid price co-movement -> dividend capacity up -> Vedanta Ltd stake value and dividend stream up -> Vedanta Resources deleverages.

**Energy chain.** Indian coal crunch and El Nino -> e-auction premium ~94% and spot power at the Rs20 ceiling -> coal-fired captive power costs rise -> HZL cost of production up a few US$/t, cushioned by renewable round-the-clock power contracts -> if summer 2027 curtails grid supply, smelter output risk (low probability).

**Rupee chain.** Fed/BOJ tightening and record FPI outflows -> rupee at 95-96 and heavy RBI defence -> +3% USD/INR = +4.9% EBITDA before hedges; but RBI tightening (repo 5.50%) trims valuation multiples (-0.8 per +25 bp).

## 4. Current situation
Q2 was a blow-out versus a year ago, helped by silver at much higher prices than now. Management cut cost guidance and reiterated 680 t silver for FY27 (320-340 t in H1); 8 t of Q3 silver is hedged at US$68/oz. The shares jumped 4% on results day and fell back; Motilal Oswal turned neutral on the Vedanta group. A data conflict remains on the Q2 average silver price (implied realisation far above Yahoo's silver path), so the size of the forward headwind is uncertain. Promoters hold 60.71% and Vedanta group shares in other entities are encumbered with GLAS Agency (security trustee) for dollar financings.

## 5. Upcoming events
Q3 FY27 results (~late Jan 2027); possible interim dividend (Dec); Union Budget 1 Feb (royalty/critical minerals); risk of a Vedanta block sale (probability 0.25 in 6 months); possible government OFS (0.10); Fed 9 Dec (hike odds 0.58) and China CEWC (Dec) as macro drivers.

## 6. Bull and bear
**Bull:** silver rebounds once the Fed pause/Iran deal arrives; zinc deficit; COP below US$825/t; high payout and ROE 77% at 8x annualised EPS; China stimulus.
**Bear:** silver stays near US$50 so Q3-Q4 EBITDA resets ~15% below Q2; acid prices fall; Vedanta parent leakage/OFS overhang; royalty or windfall levies; stock overshoots on sentiment given its precious-metal beta.

Confidence: medium. Weak spots: zinc price level (assumed), Q2 silver average, HZL net debt/cash, share of exports.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.