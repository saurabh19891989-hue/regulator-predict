# AUROPHARMA — Aurobindo Pharma Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.8%**, **12 months -4.3%** (rank 152 / 153 of 200 for 3m / 12m); beta 0.82
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 43%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.0% … P90 -1.8%; plausible 12m relative-return range incl. stock-specific noise: -38.4% … +21.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.6 pp (model impact -7.2% beta-adjusted vs realised market-adjusted move +18.6%); forward event exposure +2.8% (3m +1.9%; half assumed priced); company-specific events -1.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -3.00 | -4.00 | +1.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.56 | +3.20 | -0.34 | -0.18 | -0.11 | -1.1% |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +2.41 | +2.50 | -0.13 | +0.02 | +0.01 | — |
| US tariffs on pharmaceuticals (`P_US_PHARMA_TARIFF`) | +10 pp on Indian pharma exports | -2.40 | -3.00 | +0.60 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.78 | +2.00 | -0.25 | +0.00 | +0.02 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +1.61 | +0.00 | +1.42 | +0.24 | -0.05 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.60 | -1.60 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.25 | +0.00 | -0.48 | -0.47 | -0.30 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.21 | -1.20 | +0.00 | +0.00 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.04 | +0.00 | +0.01 | -1.01 | -0.04 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.01 | +1.00 | +0.00 | +0.01 | -0.01 | — |
| GLP-1 / obesity drug adoption (`T_GLP1`) | +1 | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.89 | +0.00 | -0.78 | -0.10 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.1% | -4.1% | -2.0 | -0.8 | -0.6 | -0.7 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.8% | -3.8% | -4.4 | +0.7 | +0.0 | -0.1 |
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -3.0% | -3.0% | -4.0 | +1.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.3% | +2.1% | +5.0 | -0.8 | -0.0 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -14.0% | -1.7% | -14.0 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | +0.0 | -1.2 | -0.1 |
| US Section 232 pharma tariff (100%) takes effect 29 Sep 2026; select Indian speciality drugs/ingredients exempted (`EV_US_PHARMA_232_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | -1.5 | +0.3 | +0.0 | +0.0 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +1.5% | +1.2% | +1.5 | -0.1 | +0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.2 | +0.1 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -1.3 | +0.4 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -2.6% | -0.9% | -1.0 | -0.8 | -0.5 | -0.4 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → AUROPHARMA | -4.40% | -4.40% |
| 1 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → AUROPHARMA | -4.00% | -4.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → AUROPHARMA | -2.69% | -2.69% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → AUROPHARMA | +2.50% | +2.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AUROPHARMA | +5.00% | +2.50% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → AUROPHARMA | -1.98% | -1.98% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → AUROPHARMA | -1.68% | -1.68% |
| 1 | EV_US_PHARMA_232_SEP26 ⇒ P_US_PHARMA_TARIFF → AUROPHARMA | -1.50% | -1.50% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → AUROPHARMA | +1.50% | +1.20% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → AUROPHARMA | -1.18% | -1.18% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → AUROPHARMA | -9.00% | -1.08% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → AUROPHARMA | +1.00% | +1.00% |
| 2 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → AUROPHARMA | +1.00% | +1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → AUROPHARMA | +4.16% | +0.92% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → AUROPHARMA | -2.99% | -0.84% |

## Analyst profile (agent research, sourced)
# AUROPHARMA - Aurobindo Pharma Ltd. (Midcap 100, US generics)

## Business
Aurobindo is a vertically integrated generics maker (oral solids, injectables through Eugia, antiretrovirals, APIs, penicillin chain, emerging biosimilars and CRDMO). The US is about 47% of sales and Europe about 28% (model estimates; not primary-source verified). Q2 FY27 sales were a record Rs 10,263 cr, operating profit Rs 2,153 cr (21%) and PAT Rs 1,124 cr (+32.5%). Fixed assets have expanded to Rs 21.4k cr, and ROE is only 10%.

## What moves the stock, ranked
1. **US generic pricing and launches (-5.0 per +5pp erosion).** Adquey ointment (US launch 2026-10-01, Nuvama sees US$300m peak) and perampanel tablets offset base erosion.
2. **USD/INR (+3.2 per +3%).**
3. **USFDA/regulatory and tariffs (-4.0, -3.0).** The Sep 29 US pharma tariff exempts Indian specialty drugs; generics are outside it (model knowledge).
4. **China dependence and China+1 (+0.8 / +2.5).**
5. **Input costs (-1.6, -0.4) and rates (-1.2, -0.3).**
6. **FPI flows (+2.0).**

## Transmission examples
- **Weak rupee (INR 94.5) -> export earnings up -> EBITDA +8% per 3% -> margin cushion offsets US price erosion.** If the Middle East escalation lifts Brent, INR weakens further (2nd), US-priced revenue becomes more valuable in INR (3rd), but Brent also raises solvent cost (4th); net positive.
- **US chain consolidation -> price erosion up -> Aurobindo US margin down -> capex discipline questioned.**
- **Section 232 extended to generics (low probability) -> US retailers seek price-sharing -> Aurobindo (47% US) is among the most exposed Indian generics names.**
- **China export controls or dumping -> KSM price swings -> Aurobindo input costs.** Dumping lowers costs, restrictions raise them; PLI Penicillin-G dampens it.

## Current situation
Strong Q2, new highs, FII stake up from 15.2% to 17.4% in two quarters. Pack: 12m +52.7%, 6m +18.7%. Management completed A1 Biochem acquisition to build a CRDMO platform.

## Upcoming events
Dividend payout by 2026-11-20; Q3 results Feb 2027; USFDA inspection cycle; tariff developments.

## Bull and bear
**Bull:** growth, launches, weak rupee, rising FII interest, biosimilar optionality. **Bear:** US price erosion, tariff tail, 52-week-high valuation versus low ROE. Confidence medium: no call transcript was read.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.