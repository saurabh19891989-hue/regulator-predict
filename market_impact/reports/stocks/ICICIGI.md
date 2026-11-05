# ICICIGI — ICICI Lombard General Insurance Company Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.5%**, **12 months -4.5%** (rank 161 / 154 of 200 for 3m / 12m); beta 0.80
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.0%): 3 months 42%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.4% … P90 +0.7%; plausible 12m relative-return range incl. stock-specific noise: -42.8% … +18.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -1.4% beta-adjusted vs realised market-adjusted move -10.9%); forward event exposure -5.5% (3m -2.3%; half assumed priced); company-specific events -1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -4.12 | -4.00 | -0.12 | +0.00 | +0.00 | — |
| Natural catastrophe insured losses (India floods/cyclones) (`NEW_NAT_CAT_LOSSES`) | +1 = major cat year adding ~2pp to industry combined ratio | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.47 | +0.00 | -0.48 | -1.43 | -0.56 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.14 | -1.50 | -0.37 | -0.23 | -0.04 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.12 | -1.50 | -0.22 | -0.22 | -0.18 | -1.1% |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +1.99 | +2.00 | +0.00 | +0.00 | -0.01 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.95 | +2.00 | +0.13 | -0.16 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.94 | +0.80 | +0.63 | +0.36 | +0.14 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.88 | -1.00 | -0.33 | -0.52 | -0.03 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.80 | +0.00 | -0.60 | -0.77 | -0.43 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.79 | +0.00 | +1.20 | +0.49 | +0.10 | +1.2% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.73 | +1.50 | +0.20 | -0.00 | +0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.66 | +0.00 | -0.59 | -0.49 | -0.58 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.62 | +0.00 | -1.06 | -0.29 | -0.27 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -9.5% | -9.5% | +0.0 | -6.0 | -1.8 | -1.7 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.5% | -4.5% | -3.9 | -0.5 | +0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -9.7% | -2.7% | -6.0 | -2.9 | -0.9 | +0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.0% | +2.5% | +4.3 | +0.5 | -0.0 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.8% | -2.4% | -1.8 | -3.1 | -1.0 | -0.9 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | -1.1 | -0.4 | -0.7 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -2.1 | +0.0 | -0.1 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -11.7% | -2.1% | -7.5 | -3.7 | -0.7 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.6% | +2.1% | +0.8 | +1.8 | +0.6 | +0.5 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.9 | -0.1 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.7 | -0.2 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -0.7 | -0.8 | -0.3 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → ICICIGI | -3.30% | -3.30% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → ICICIGI | -2.35% | -2.35% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → ICICIGI | -2.10% | -2.10% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ICICIGI | +3.75% | +1.88% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ICICIGI | -6.00% | -1.68% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → ICICIGI | -2.80% | -1.40% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ICICIGI | -7.50% | -1.35% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → ICICIGI | -1.19% | -1.19% |
| 1 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → ICICIGI | -1.15% | -1.15% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → ICICIGI | +1.00% | +1.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → ICICIGI | -0.89% | -0.89% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → ICICIGI | -0.82% | -0.82% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → ICICIGI | +0.75% | +0.75% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → ICICIGI | -0.72% | -0.72% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → ICICIGI | -0.70% | -0.70% |

## Analyst profile (agent research, sourced)
# ICICIGI - ICICI Lombard General Insurance Company Ltd. (as of 2026-11-05)

## Business
ICICI Lombard is the largest private non-life insurer in India. Motor (own damage plus third party) is roughly 38% of premiums, health and personal accident about 27%, and fire/marine/engineering/commercial lines the rest (model estimate; the pack's fundamentals table was blank and these shares need verification). ICICI Bank owns 51.3% and is a key distributor. Profit depends on the combined ratio (claims plus expenses over earned premium) and on investment income on a ~Rs32k cr float (model estimate). Q2 FY27: PAT Rs946cr (+15.5%) per BusinessLine/Financial Express vs Rs1,031cr (+27.5%) per Moneycontrol - an unresolved difference; all sources agree the combined ratio stayed elevated and investment income carried earnings.

## What moves the stock (ranked)
1. **IRDAI regulation (-4.0)**: the 2026-09-23 commission-cap/dark-pattern proposal, plus motor third-party tariff decisions.
2. **GDP and financialisation (+2.0, +2.0)**: penetration and premium growth.
3. **INR and imported-parts inflation (-1.5)**: weaker rupee raises motor repair and reinsurance costs; empirical -2.11 per SSU (t=-1.6) agrees.
4. **Rates (G-sec -1.5)** and **catastrophe losses (-3.0 in a bad cat year)**.
5. **Auto demand (+1.2)**, **CPI/medical inflation (-1.0)**, **flows and risk (+1.5, -1.5)**.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker -> imported auto parts and reinsurance dearer**: Brent +10% -> USD/INR +3% -> motor claims +0.5% (spares ~40% of own-damage claims) -> combined ratio +0.5pp -> PAT -3%; 3rd: RBI hike (already begun) lowers car sales growth -> GWP -1pp; 4th: tariff-regulated TP pricing fixed so insurer cannot reprice.
- **IRDAI commission cap -> distributors shift focus -> premium growth down but expense ratio down**: first-order GWP -2%; second-order expense ratio -1pp; third-order broker renegotiation; fourth-order market consolidation to bancassurance-led insurers like ICICI Lombard (a possible advantage).
- **Monsoon floods -> cat claims in Q2/Q3** -> combined ratio +1-2pp -> reinsurance cost up next year.
- **Higher G-sec yields** -> MTM on trading portfolio (-0.5) but better reinvestment (+0.3) -> investment income supports margins in 2027.

## Current situation
Stock -2% in 3m, -12% in 6m, -20.5% in 12m. FIIs sold from 22.3% to 18.3% while DIIs bought (23.8%). Brokers remain positive (targets Rs1,985-2,000, ~16-23% upside). The market debate: whether the combined ratio can fall below ~102% and whether IRDAI's distribution rules hurt volume.

## Upcoming
Q3 FY27 results ~mid-Jan 2027; IRDAI final framework; Union Budget Feb 2027; cat season; ex-dividend of Rs7.

## Bull case
Combined ratio improves to ~101-102%, IRDAI softens, investment income grows: EPS +15-18%, re-rating to 35x earnings (+15-20%).
## Bear case
Health/motor claims inflation, bad cat year, weaker INR and distribution caps: EPS growth <8% and de-rating (-15%).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.