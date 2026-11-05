# HINDZINC — Hindustan Zinc Ltd.
*NIFTY_NEXT_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +2.4%** (rank 80 / 63 of 200 for 3m / 12m); beta 1.14
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +36.9%): 3 months 51%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.3% … P90 +13.5%; plausible 12m relative-return range incl. stock-specific noise: -32.6% … +37.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -11.4% beta-adjusted vs realised market-adjusted move -14.0%); forward event exposure +8.6% (3m +3.7%; half assumed priced); company-specific events -1.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Windfall / export taxes on commodities (`P_WINDFALL_EXPORT_TAX`) | +1 = imposition | -4.01 | -4.00 | +0.00 | +0.00 | -0.01 | — |
| Zinc / lead price (`F_ZINC_LEAD`) | +10% zinc | +3.80 | +3.80 | +0.00 | +0.00 | +0.00 | — |
| Silver price (`F_SILVER`) | +12% silver | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | -30.0% |
| Gold price (`F_GOLD`) | +8% gold (USD) | +2.74 | +0.00 | +2.80 | -0.03 | -0.03 | -8.4% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.10 | +2.20 | +0.10 | -0.12 | -0.08 | -1.1% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.70 | +0.00 | +1.52 | +0.16 | +0.02 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +1.42 | +0.00 | +0.00 | +1.34 | +0.08 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.24 | +0.80 | +0.44 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.13 | +0.00 | -0.96 | +0.14 | -0.31 | — |
| Gold import duty (`P_GOLD_IMPORT_DUTY`) | +5 pp | +0.97 | +1.00 | +0.00 | -0.03 | +0.00 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.94 | +0.00 | -0.21 | -0.58 | -0.14 | +9.4% |
| US dollar index (`F_DXY`) | +3% DXY | -0.88 | +0.00 | -0.09 | -0.77 | -0.03 | +2.2% |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +0.87 | +0.00 | +0.44 | +0.43 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -8.8% | -8.8% | -8.8 | -0.4 | +0.3 | -0.0 |
| Windfall/export levy re-set: petrol nil, diesel Rs11.5/l, ATF ~Rs11/l (31 Oct); excise reportedly cut (3 Nov, unverified) (`EV_EXPORT_LEVY_REVISIONS`) | occurred | 1.00 | -4.0% | -4.0% | -4.0 | +0.0 | -0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +3.9% | +3.9% | +0.0 | +2.7 | +2.0 | -0.8 |
| Gold/silver rebound as Fed hike fears fade or Iran war ends (`EV_PRECIOUS_METALS_REBOUND_H1_2027`) | anticipated | 0.45 | +5.3% | +2.4% | +5.3 | +0.2 | -0.1 | -0.1 |
| Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`) | risk_scenario | 0.30 | -7.0% | -2.1% | -7.0 | +0.0 | -0.1 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -0.4 | -1.5 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -0.8 | -0.6 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -1.1% | -1.1% | -0.9 | -0.2 | +0.0 | +0.0 |
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.2 | -0.8 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -1.6% | -0.9% | +0.0 | -0.8 | -1.2 | +0.3 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_SILVER → HINDZINC | -8.75% | -8.75% |
| 1 | EV_EXPORT_LEVY_REVISIONS ⇒ P_WINDFALL_EXPORT_TAX → HINDZINC | -4.00% | -4.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → HINDZINC | +3.44% | +3.44% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → HINDZINC | +5.25% | +2.36% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → HINDZINC | -7.00% | -2.10% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_GOLD → F_SILVER → HINDZINC | +1.26% | +1.26% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → HINDZINC | -1.12% | -1.12% |
| 3 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GOLD → F_SILVER → HINDZINC | -1.07% | -1.07% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_FOOD_INFLATION_IN → P_WINDFALL_EXPORT_TAX → HINDZINC | -1.06% | -1.06% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_PRICE_IN → HINDZINC | -0.90% | -0.90% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → HINDZINC | +0.89% | +0.89% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → HINDZINC | -0.81% | -0.81% |
| 1 | EV_INDIA_COAL_CRUNCH ⇒ F_COAL_INDIA → HINDZINC | -0.75% | -0.75% |
| 3 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_GOLD → F_SILVER → HINDZINC | -0.73% | -0.73% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_REFINING_MARGIN → P_WINDFALL_EXPORT_TAX → HINDZINC | -0.72% | -0.72% |

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