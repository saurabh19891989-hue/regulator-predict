# ASTRAL — Astral Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.5%**, **12 months +0.8%** (rank 119 / 87 of 200 for 3m / 12m); beta 0.89
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.3%): 3 months 48%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.7% … P90 +6.0%; plausible 12m relative-return range incl. stock-specific noise: -33.3% … +36.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.8% beta-adjusted vs realised market-adjusted move -13.4%); forward event exposure +4.0% (3m +0.2%; half assumed priced); company-specific events -0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.83 | +0.00 | -1.89 | -0.67 | -0.27 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.42 | +2.50 | +0.00 | -0.07 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.85 | -1.50 | -0.23 | -0.11 | -0.01 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | -1.58 | -1.50 | -0.08 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.39 | +0.00 | +0.00 | -1.04 | -0.35 | — |
| US growth (`F_US_GDP`) | +1 pp | -1.39 | +0.00 | -0.54 | -0.72 | -0.13 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.33 | +1.50 | +0.00 | -0.07 | -0.10 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.32 | +0.00 | -0.80 | -0.34 | -0.18 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.28 | -0.80 | -0.12 | -0.21 | -0.15 | -1.1% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.12 | +0.00 | +0.26 | -0.93 | -0.45 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.09 | +1.00 | +0.00 | -0.05 | +0.13 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.03 | +0.00 | -0.36 | -0.39 | -0.28 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.91 | -0.80 | +0.00 | -0.12 | +0.01 | +9.4% |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.3% | -6.3% | +0.0 | -3.6 | -1.7 | -1.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -2.2 | -0.8 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.9% | -1.9% | -1.5 | -0.4 | +0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | -1.4 | -0.1 | -0.3 | -0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -0.9 | -0.5 | -0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.5% | -1.5% | -1.2 | -0.1 | -0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.4% | -1.4% | -1.3 | +0.0 | +0.1 | -0.2 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | +5.4% | +1.4% | +0.0 | +4.1 | +0.4 | +0.8 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | -0.6 | -0.3 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.7% | +1.0% | -0.4 | +1.2 | +0.5 | +0.3 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.1% | +1.0% | +1.2 | +0.0 | -0.1 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.9% | +0.9% | +1.5 | -0.2 | -0.3 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → ASTRAL | -2.69% | -2.69% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → ASTRAL | -1.99% | -1.99% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → ASTRAL | -1.50% | -1.50% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → ASTRAL | +1.50% | +1.50% |
| 1 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → ASTRAL | -1.36% | -1.36% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → ASTRAL | -1.33% | -1.33% |
| 1 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → ASTRAL | -1.26% | -1.26% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → ASTRAL | -1.25% | -1.25% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → ASTRAL | -1.20% | -1.20% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ASTRAL | +1.20% | +1.08% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → ASTRAL | -1.08% | -1.08% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ASTRAL | +3.20% | +0.90% |
| 2 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → F_HOUSING_DEMAND → ASTRAL | -0.84% | -0.84% |
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → ASTRAL | -1.05% | -0.73% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ASTRAL | +4.00% | +0.72% |

## Analyst profile (agent research, sourced)
# ASTRAL - Astral Ltd. (Capital Goods / plastic pipes)

## Business
Astral is a branded plastic-plumbing leader (CPVC and PVC pipes and fittings, water tanks, bath ware) with growing adhesives, sealants and paints businesses. It is net cash and earns a 16% EBITDA margin, so cash flow is stable; the equity story is volume growth and margin expansion in new categories. The stock trades at 63x earnings, near its 52-week low (Rs1,312-1,769 range).

## What moves the stock, ranked
1. **PVC/CPVC resin cycle** (F_CHEM_FEEDSTOCK -0.8 per +10% with a wide range): falling resin leads to destocking and weaker pricing, rising resin gives short-term inventory gains but squeezes later; the net sign is genuinely uncertain.
2. **Housing and government water capex** (+2.5 per +10% housing sales, +1.5 per +10% capex).
3. **Multiple compression**: RBI repo 5.50% from 2026-10-07 and US 10Y yield at 4.89% weigh on a 63x P/E.
4. **Trade-remedy policy** (anti-dumping on PVC resin).
5. **USD/INR** (imported CPVC compound).

## Transmission examples
- **Middle East escalation -> Brent up -> ethylene and EDC costs up -> PVC resin up -> dealers pre-buy -> Astral raises prices -> inventory gain, then demand pause**: 1st-3rd order. In parallel Brent up -> INR weaker -> imported CPVC compound costlier -> margin down.
- **Rate hike -> home-loan EMIs up -> new housing starts slow -> plumbing volume growth slows (4th order, 6-12 months)** while the P/E de-rates immediately.
- **PVC anti-dumping duty -> resin up 5-10% -> pipe industry price increases -> unorganised players squeezed -> share gain for Astral over time.**
- **Jal Jeevan Mission funding released -> CPVC/PVC water-pipe tenders -> volume lift.**

## Current situation
Q1 FY27 PAT jumped 52% (CNBC TV18, 2026-08-12) on paints/adhesives and a better pipe quarter; the stock rose 9% then faded. Q2 results are imminent. On 2026-11-04 Investec kept Buy (target Rs1,710) citing the DSS acquisition; terms are not verified from a primary source. FIIs sold (14.5% to 11.1% since Mar), DIIs bought (20.9% to 23.8%).

## Upcoming
Q2 results (Nov), analyst meeting 2026-11-16, DSS acquisition updates, Q3 results Feb 2027.

## Bull and bear
Bull: pipes volume recovery with stable resin, paints scale-up, net-cash balance sheet funding M&A. Bear: 63x P/E leaves little room, ongoing pipe-price competition from Supreme/Finolex, housing slowdown after rate hikes, paints losses.

Uncertainties: resin-price sign, DSS deal details and segment mix are low confidence.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.