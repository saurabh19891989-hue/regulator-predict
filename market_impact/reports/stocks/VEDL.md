# VEDL — Vedanta Ltd.
*NIFTY_NEXT_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.2%**, **12 months -0.3%** (rank 95 / 111 of 200 for 3m / 12m); beta 1.14
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +105.4%): 3 months 50%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.9% … P90 +4.6%; plausible 12m relative-return range incl. stock-specific noise: -58.3% … +60.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -3.5% beta-adjusted vs realised market-adjusted move -27.4%); forward event exposure +4.2% (3m +2.5%; half assumed priced); company-specific events -2.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.01 | -2.00 | +0.00 | +0.00 | -0.01 | — |
| Copper price (`F_COPPER`) | +10% copper | +1.60 | +1.50 | +0.10 | +0.00 | +0.00 | -2.4% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.39 | +1.50 | -0.15 | +0.01 | +0.03 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.36 | +0.00 | +1.13 | +0.27 | -0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.27 | +2.00 | -0.24 | -0.23 | -0.27 | -1.1% |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.12 | -0.80 | -0.25 | -0.06 | -0.01 | +9.4% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.08 | +0.00 | +0.21 | -1.05 | -0.23 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.01 | -0.80 | -0.20 | +0.00 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.95 | -0.70 | -0.16 | -0.10 | +0.02 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -0.92 | +0.00 | -0.81 | +0.01 | -0.11 | +2.2% |
| Zinc / lead price (`F_ZINC_LEAD`) | +10% zinc | +0.90 | +0.90 | +0.00 | +0.00 | +0.00 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +0.85 | +0.00 | +0.82 | +0.04 | -0.00 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.72 | +0.00 | -0.28 | -0.14 | -0.30 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.3% | -3.3% | -3.6 | +0.4 | -0.0 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | -1.4 | -1.0 | +0.0 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.1% | -2.1% | -1.2 | -1.0 | +0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.7% | +1.9% | +4.0 | -0.4 | +0.0 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | -0.6 | -0.5 | -0.2 | -0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | +0.2 | -1.2 | -0.3 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.5% | -1.2% | -2.8 | -2.1 | +0.4 | +0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -5.5% | -1.0% | -3.5 | -2.6 | +0.7 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.9% | +0.9% | +0.9 | -0.1 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.6 | -0.2 | -0.0 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → VEDL | -3.30% | -3.30% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → VEDL | +3.13% | +3.13% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → VEDL | +3.75% | +1.88% |
| 1 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → VEDL | -1.36% | -1.36% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → VEDL | -1.20% | -1.20% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → VEDL | -1.12% | -1.12% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → VEDL | -0.98% | -0.98% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → VEDL | -0.89% | -0.89% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → VEDL | -2.80% | -0.78% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → VEDL | +0.75% | +0.75% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → VEDL | -0.74% | -0.74% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → VEDL | -0.70% | -0.70% |
| 1 | EV_FED_SEP26_HIKE ⇒ F_US_10Y → VEDL | -0.64% | -0.64% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → VEDL | -3.50% | -0.63% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_CREDIT_SPREADS_IN → VEDL | -0.60% | -0.60% |

## Analyst profile (agent research, sourced)
# VEDL — Vedanta Ltd. (Nifty Next 50) — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast; no expected-return number. Confidence is LOW overall: the demerger broke the history, segment data for the residual business was not found, and the screener TTM is unreliable.

## 1. Business
After the 2026 demergers, Vedanta Ltd is a holding company anchored by Hindustan Zinc (~61%, 93% of Q2 EBITDA), with Zinc International, the copper business, nickel, ferroalloys and incubator ventures. Aluminium sits in Vedanta Aluminium Metal (VAML, listed June 2026); oil & gas, power and iron & steel are separate listed entities. Q2 FY27: revenue Rs26,356 cr, EBITDA ~Rs9,940 cr, profit from continuing operations Rs6,202 cr (+151%) but attributable profit Rs3,650 cr (-33% q/q, because ~39% of HZL's profit belongs to minorities and the quarters are not like-for-like). Net debt only Rs3,675 cr (0.1x), cash Rs26,622 cr, FCF before capex Rs5,803 cr. A Rs5 dividend (Rs1,955 cr) was declared in October, the first since the demerger.

## 2. What moves the stock, ranked
1. **Hindustan Zinc price (holding_stake, w 0.75 per 1%).** Look-through value of the stake (~Rs1.46 lakh cr at 60.7%) exceeds the whole market cap (Rs1.03 lakh cr), so VEDL is mostly a leveraged-discount proxy for HZL. Weekly beta of VEDL on HZL rose to 0.77 since July (corr 0.84). Therefore silver (HZL +3.5 per +12%) and zinc (+3.8 per +10%) enter through HZL, not as separate VEDL edges, to avoid double counting.
2. **Parent-level financing and governance (credit spreads -2.0, US 10y -0.8).** 54.72% of VEDL and 56.38% of VAML promoter shares are encumbered with GLAS Agency for US$1-2.25bn financings and a US$400m bond tap on 16 Sep 2026. Vedanta Resources lives off VEDL dividends and brand fees, so VEDL's payout is both a support (12.9% trailing yield) and a leakage.
3. **Copper (+1.5 per +10%) and Zinc International (+0.9)**: ex-HZL commodities.
4. **USD/INR (+2.0)**, FPI flows (+1.5), royalty (-1.2), rates (-0.8).
5. **Aluminium: effectively zero now.** The pack's strong empirical +7.2 (t=3.2) is a pre-demerger artefact, so the model should not shrink toward it; a residual +0.5 reflects group sentiment only.

## 3. Transmission chains
**Silver/Fed chain (4th order).** Iran war and food-led inflation -> Fed hike (16 Sep) and 10y UST ~4.9% -> real yields and dollar up -> silver falls 30% since June and zinc/copper soften -> HZL's EBITDA outlook is cut (company sensitivity Rs200-225 cr per US$1/oz) -> HZL stock down -> VEDL's holdco discount mechanically deepens (w 0.75) -> lower HZL dividends upstreamed to VEDL and then to Vedanta Resources -> parent leans harder on VEDL dividends or sells more HZL shares -> VEDL and HZL fall further, bonds widen (credit spreads edge).

**Parent credit chain.** Higher US yields + record FPI outflows from India (Rs3 lakh cr in CY2026) -> weaker rupee (95-96) and wider Indian credit spreads -> refinancing of the promoter-level US$ bonds becomes costlier -> encumbered 54.72% stake is a pressure point (a forced sale or margin call would hit both VEDL and VAML) -> contagion to HZL (0.2) and VAML.

**China/copper chain.** China stimulus at the December CEWC (odds 0.45 of a large package) -> China GDP and property -> copper and zinc demand -> Zambian copper and Zinc International earnings up; and the HZL stake re-rates.

**Rupee chain.** Rupee weakness helps USD-priced zinc/silver/copper (+2.0 per +3%) but hurts the parent's dollar debt service (outside VEDL), so the net equity effect for the stock is smaller than for HZL.

## 4. Current situation
Strong cash generation and de-leveraging (net debt -Rs4,624 cr q/q) are offset by a falling silver price and holdco/governance discount; shares fell 10% in a month (to 28 Sep), rebounded with the Vedanta group in October, and are -4.6% over three months. The rating is AA+/Stable (ICRA, CRISIL per a summary). Motilal Oswal is neutral on the group. Promoter holding fell from 56.38% to 54.72% in June 2026 and the public/FII share rose.

## 5. Upcoming events
Q3 FY27 results (~Feb 2027, date unconfirmed); possible second interim dividend (Dec); possible HZL block sale by VEDL (0.25 in 6 months); Vedanta Resources refinancing and GLAS encumbrance developments; Union Budget 1 Feb 2027; Fed 9 Dec; China CEWC.

## 6. Bull and bear
**Bull:** silver/zinc rebound, narrowing of the ~30% holdco discount (restructuring, large special dividend), net-cash balance sheet, copper upside.
**Bear:** HZL earnings reset lower, parent refinancing stress and forced sales, dividend leakage, royalty/Zambia tax, and an unclean data history; the stock can move more than HZL (vol is high) on any group credit news.

Weak spots: direct VEDL stake in HZL, copper/Zinc International segment sizes, standalone debt, Q2 segment table, and post-demerger price history.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.