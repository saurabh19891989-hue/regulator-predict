# JINDALSTEL — Jindal Steel Ltd.
*NIFTY_NEXT_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +5.7%**, **12 months +11.0%** (rank 7 / 10 of 200 for 3m / 12m); beta 1.20
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.6%): 3 months 69%, 12 months 80%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +4.6% … P90 +19.8%; plausible 12m relative-return range incl. stock-specific noise: -6.6% … +49.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.1 pp (model impact +6.2% beta-adjusted vs realised market-adjusted move -10.2%); forward event exposure +11.9% (3m +4.7%; half assumed priced); company-specific events +6.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +15.98 | +16.00 | -0.02 | +0.00 | -0.01 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +7.88 | +0.00 | +7.89 | -0.01 | +0.00 | +20.6% |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | +6.39 | +0.00 | +6.40 | -0.01 | +0.00 | — |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -4.86 | -7.50 | +1.60 | +1.04 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +4.00 | +0.00 | -3.69 | +4.89 | +2.80 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -3.18 | -0.80 | -1.60 | -0.78 | +0.00 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.50 | +1.50 | +1.12 | +0.00 | -0.12 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.45 | +1.00 | +1.90 | -0.26 | -0.19 | -1.1% |
| EU steel safeguard / CBAM burden on imports (`NEW_EU_STEEL_ACCESS`) | +1 = tightening step (quota cut / higher out-of-quota tariff / CBAM cost) | -1.92 | +0.00 | -1.92 | +0.00 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.77 | +0.00 | -1.08 | -0.77 | +0.08 | — |
| Iron ore price (`F_IRON_ORE`) | +15% iron ore | -1.69 | -2.50 | +0.00 | +0.81 | +0.00 | -12.5% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.60 | -1.50 | -0.10 | +0.00 | +0.00 | — |
| Red Sea / Suez shipping disruption (`C_RED_SEA`) | +1 = disruption | -1.56 | +0.00 | -1.56 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +13.4% | +13.4% | +13.4 | -0.0 | +0.0 | -0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -6.1% | -6.1% | -6.1 | -0.0 | +0.0 | -0.0 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | +6.4% | +3.5% | +6.4 | -0.0 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +2.9% | +2.9% | -1.2 | -0.4 | +5.1 | -0.7 |
| Chinese steel/aluminium export surge floods Asia as China demand stays weak (`EV_CHINA_STEEL_EXPORT_FLOOD`) | risk_scenario | 0.25 | -10.8% | -2.7% | -1.2 | -10.3 | +0.7 | +0.0 |
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | -2.6% | -2.6% | -2.6 | +0.0 | +0.0 | +0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -1.1 | -1.4 | +0.0 |
| EU quota-halving steel regime and CBAM cut Indian steel exports to EU (`EV_EU_STEEL_REGIME_CBAM_HITS_INDIA`) | occurred | 1.00 | -2.4% | -2.4% | -2.4 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -2.1 | -0.1 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -2.2% | -2.2% | -1.8 | -0.4 | +0.0 | +0.0 |
| China enforces steel output cuts / export licensing discipline ('anti-involution') (`EV_CHINA_STEEL_OUTPUT_CURB_2027`) | anticipated | 0.50 | +4.3% | +2.1% | +1.2 | +3.3 | -0.3 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +1.5 | +1.1 | -0.4 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → JINDALSTEL | +22.40% | +22.40% |
| 1 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_COKING_COAL → JINDALSTEL | -12.52% | -12.52% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_COKING_COAL → JINDALSTEL | -9.00% | -9.00% |
| 1 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_STEEL_INDIA → JINDALSTEL | +6.40% | +6.40% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → JINDALSTEL | +5.63% | +5.63% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JINDALSTEL | +6.40% | +3.52% |
| 1 | EV_EU_STEEL_REGIME_CBAM_HITS_INDIA ⇒ F_STEEL_INDIA → JINDALSTEL | -2.40% | -2.40% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → JINDALSTEL | -2.10% | -2.10% |
| 1 | EV_IRON_ORE_TWO_YEAR_LOW ⇒ F_IRON_ORE → JINDALSTEL | +2.07% | +2.07% |
| 1 | EV_UNION_BUDGET_FEB27_METALS ⇒ F_COKING_COAL → JINDALSTEL | +2.25% | +2.02% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JINDALSTEL | -7.89% | -1.97% |
| 1 | EV_INDIA_COAL_CRUNCH ⇒ F_COAL_INDIA → JINDALSTEL | -1.95% | -1.95% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_PRICE_IN → JINDALSTEL | -1.80% | -1.80% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → JINDALSTEL | +1.56% | +1.56% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_RED_SEA → F_SHIPPING_RATES → JINDALSTEL | -1.56% | -1.56% |

## Analyst profile (agent research, sourced)
# JINDALSTEL — Jindal Steel Ltd. (Nifty Next 50) — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast. No expected-return number is given here (the Director computes it from the graph). Facts are tagged with source files in `JINDALSTEL.json`; model-estimated quantities (coking-coal intensity, power-purchase share, iron-ore cost share) are flagged as estimates.

## 1. Business
Integrated steel maker in Chhattisgarh and Odisha (Raigarh, Angul). Crude capacity reached 15.6 Mtpa after the second Angul blast furnace; FY27 production is guided at ~11 Mt (6 Mt in H2, ~0.96 Mt a month) and sales at 10.5-11 Mt. Mix is ~60:40 flats to longs, heading for 65:35: plates (>220 kt a month, sold to defence, shipbuilding, wind), HRC, rails, structurals and TMT. Value-added share was 57% in Q2. Backward integration: Kasia iron-ore mine (33% of ore burn), OMC long-term ore contract (13.5 Mt), ~15 Mtpa of captive coal blocks (50-55% of coal need, target 65-70%), a Mozambique coking-coal mine, coal-gasification-based DRI, and a 192 km Barbil-Angul slurry pipeline. Consolidated Q2 FY27: sales Rs16,610 cr (+45%), volume 2.38 Mt (+27%), NSR Rs70,078/t, adjusted EBITDA Rs2,504 cr, EBITDA/t Rs10,522 (-12% q/q), net debt Rs14,790 cr (1.51x). (The screener pack shows lower, standalone-style numbers; the brokers' consolidated figures are used for weights.)

## 2. What moves the stock, ranked by sensitivity x current shock
1. **Domestic steel price (F_STEEL_INDIA), w ~ +16 per +7%.** HRC and TMT moved from ~Rs52,000 to ~Rs60,000/t after Q2. About 94% of revenue is steel, so price is the dominant driver. HRC at a four-year high and global HRC +20.6% since 1 June are partly in the share price already.
2. **Coking coal (F_COKING_COAL), gross w ~ -7.5 per +15%.** The largest input (~22% of costs, estimate). Management guides +US$12-15/t in Q2 and a further +US$20-25/t in Q3. The net effect after price pass-through is much smaller (~-2.7), which is why EBITDA/t fell only 12% while coal rose.
3. **Safeguard duty and the anti-dumping probe** (P_ANTI_DUMPING_IN +3, plus the safeguard embedded in the steel price). The 12% safeguard steps to 11.5% in April 2027; the HR flat AD case concludes ~June 2027.
4. **Iron ore (-2.5), domestic coal (-1.3), power (-0.6), freight (-0.8).** Iron ore is currently a tailwind (two-year low).
5. **Rates and risk sentiment** (10y G-sec -1.5, VIX -0.7, repo -0.3). The stock has market beta ~1.3.
6. **China and imports** (direct volume channel -0.8, plus the larger price path via the backbone).

## 3. Transmission chains (the user's worked example)
**A. China steel dumping (4th order).** China property stays weak and the dollar is firm -> Chinese exports rise (Sept 10.49 Mt, +3.3% m/m; F_CHINA_STEEL_EXPORTS +15%) -> Asian export HRC falls (-5%, F_STEEL_GLOBAL) -> India's import parity price falls and imports rise (H1 FY27 +24%) -> Indian HRC -2.6% (F_STEEL_INDIA) -> JSP realisation falls ~Rs1,800/t, EBITDA ~-17% -> equity ~-2.9 on the backbone path, plus a small direct export/volume hit. Dampeners: 12% safeguard, the AD probe, Europe's quota/CBAM regime pushing Chinese tonnes elsewhere (3rd-order negative for Asia, because EU-bound Indian exports fall 20%). Upside twin: Beijing's 'anti-involution' output curbs (event-catalogue odds 0.5 by 12 months) lift HRC and lower iron ore.

**B. Coal prices (up to 4th order).** Weak monsoon and El Nino -> hydro/solar shortfall and record peak demand -> Indian thermal stocks critical (74 plants <=7 days, September) -> Coal India e-auction premia ~94%, rail rakes prioritised to power -> JSP's non-captive coal cost rises (F_COAL_INDIA -1.3) and iron-ore/coal logistics tighten (offset by the new slurry pipeline replacing ~500 trucks a day). Separately, seaborne coking coal +25% in August after supply shocks -> imported coking coal +US$20-25/t in Q3 -> unit EBITDA down ~Rs1,100/t -> partly recovered through steel prices (backbone pass-through 0.3 SSU per +15%) -> net -2.7. If Russian Black Sea supply returns in Dec-Jan, the chain reverses (+2 to +6).

**C. Electricity prices.** IEX hit the Rs20/unit ceiling on 19 Sep -> mills buying open-access power face higher cost (direct -0.6) -> government orders captive plants to run at full capacity and prioritises grid supply (a 3rd-order risk of captive-power diversion) -> if El Nino summer 2027 repeats shortfalls (event odds 0.4), curtailment risk for Angul's new blast furnaces. JSP's partial immunity: captive coal power and BF-gas, plus coal-gas syngas replacing propane (Rs30/kg vs Rs100/kg), which also made the West Asia fuel shock only US$4-5/t.

**D. Interest rates.** RBI hiked to 5.50% (7 Oct) and drained liquidity -> 10y G-sec ~7.4% -> (i) discount-rate hit on a stock re-rating on FY28-29 earnings (-1.5 per +25 bp), (ii) direct interest bill rises only ~Rs25 cr per 25 bp (net debt 1.5x EBITDA, capex funded from accruals), (iii) mortgage rates up -> housing sales down -> TMT/rebar demand weaker, the 2nd/3rd-order link that JSP is already reducing by cutting TMT output to 120 kt/month and shifting to plates. (iv) Rate hike + weaker rupee (95-96 per USD, heavy RBI defence) -> import parity supports steel prices while raising coking-coal rupee costs: net small positive.

**E. Middle East.** Hormuz/Iran escalation -> Brent up -> diesel, freight and propane costs -> competitors on LPG/propane suffer more than JSP (relative positive); risk-off hits the high-beta stock (-0.8 net).

## 4. Current situation
Q2 was a volume story: Angul ramp-up, record revenue, but margin pressure from coking coal, freight and other expenses. Management kept ~11 Mt production, said the new Angul BF-II runs ~10 ktpd (target 12 ktpd by December), and flagged better H2 realisations. Net debt fell to Rs14,790 cr (1.51x) from Rs15,930 cr. Brokers (MOFSL TP Rs1,270, PL TP Rs1,245) both Buy; PL EBITDA Rs3,150 cr for Q3 and Rs4,410 cr for Q4. The price has risen ~14% since the results (Rs1,153 vs ~Rs1,016 on 24 Oct), so some of the improvement is already priced. Promoter group bought shares on the open market on 30 Oct.

## 5. Upcoming events
Q3 FY27 results (late Jan 2027); Angul BF-II at 12 ktpd and slurry pipeline commercial start (Dec); Roida mine clearance (Dec-Jan); RBI MPC 4 Dec (0.40 hike odds); India-EU FTA signing 16 Dec; Union Budget 1 Feb (coking-coal duty, protection); DGTR HR flat finding (by ~Jun 2027); safeguard step-down 21 Apr 2027; DRI-2 and pellet plant by Jun 2027.

## 6. Bull and bear
**Bull:** 11 Mt volumes with 65% value-added mix, Rs700/t pipeline saving, falling iron ore, Russian coking coal return, AD duty, and EBITDA doubling into FY28 (PL FY28E EBITDA Rs17,300 cr, 6.3x EV/EBITDA).
**Bear:** coking coal outruns prices in Q3, China export flood and import share gains, safeguard relaxation under 5.5% inflation, execution slippage, power/coal crunch, hawkish RBI with a high-beta stock after a +14% post-result rally.

Confidence: medium. Weak spots: coking-coal intensity and price level, bought-power share, post-result consolidated vs standalone data mismatch, no empirical significance for steel or coal factors.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.