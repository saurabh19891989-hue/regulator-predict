# CIPLA — Cipla Ltd.
*NIFTY_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.2%**, **12 months +0.0%** (rank 92 / 105 of 200 for 3m / 12m); beta 0.74
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +17.5%): 3 months 51%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.3% … P90 +2.9%; plausible 12m relative-return range incl. stock-specific noise: -26.9% … +21.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -1.4% beta-adjusted vs realised market-adjusted move -3.0%); forward event exposure +3.4% (3m +1.6%; half assumed priced); company-specific events -1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -3.50 | -3.50 | +0.00 | +0.00 | +0.00 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -1.30 | -2.00 | +0.70 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.29 | +1.20 | +0.16 | -0.03 | -0.04 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.21 | +1.40 | -0.10 | -0.09 | -0.00 | -1.1% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.91 | -1.00 | +0.00 | +0.15 | -0.05 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.89 | +0.00 | -0.60 | -0.20 | -0.10 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.78 | -0.60 | -0.10 | -0.06 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.66 | +0.00 | +0.34 | +0.33 | -0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +0.61 | +0.80 | -0.11 | -0.04 | -0.04 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +0.50 | +0.00 | +0.32 | +0.18 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.48 | +0.60 | -0.13 | +0.00 | +0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.47 | +0.00 | +0.00 | -0.37 | -0.10 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.42 | +0.00 | +0.38 | +0.12 | -0.09 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -1.3% | -1.3% | -2.0 | +0.7 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.7 | -0.3 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.0% | -1.0% | -1.3 | +0.4 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.0% | -1.0% | -1.5 | +1.4 | -0.5 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.6 | -0.1 | -0.1 | -0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -5.0% | -0.6% | -5.0 | +0.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.1% | +0.6% | +1.5 | -0.4 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.5% | +0.5% | +0.6 | -0.1 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +0.9% | +0.5% | +1.0 | -0.4 | +0.2 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.3 | -0.1 | -0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.5% | -0.5% | -0.5 | +0.0 | +0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -1.0% | -0.3% | -1.2 | +0.6 | -0.3 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → CIPLA | +2.19% | +2.19% |
| 1 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → CIPLA | -2.00% | -2.00% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → CIPLA | -1.50% | -1.50% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → CIPLA | -1.32% | -1.32% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → CIPLA | -0.79% | -0.79% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CIPLA | +1.50% | +0.75% |
| 2 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → CIPLA | +0.70% | +0.70% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → CIPLA | -0.60% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → CIPLA | +1.00% | +0.58% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → CIPLA | -0.53% | -0.53% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → CIPLA | -0.52% | -0.52% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → CIPLA | -0.48% | -0.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → CIPLA | -1.20% | -0.43% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ F_US_GENERIC_PRICING → CIPLA | -3.50% | -0.42% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → CIPLA | +1.82% | +0.40% |

## Analyst profile (agent research, sourced)
# CIPLA (Cipla Ltd.) — Nifty 50, as of 2026-11-05

## Business
Cipla is a diversified Indian pharma group: roughly 45% India (prescription chronic and acute therapies, trade generics, consumer health, strongest in respiratory), about 30% North America (generic inhalers, gRevlimid, peptides and complex generics; FY27 target ~US$1 bn per BusinessLine 2026-10-27), around 18% South Africa, Africa and other emerging markets, and the remainder Europe and API. The segment shares are model knowledge and should be verified against the investor presentation. It is almost debt free (interest ~Rs 17 cr a quarter) with Rs 28,139 cr TTM sales. Q2 FY27 (reported 2026-10-27): sales Rs 7,404 cr (-2.4% YoY), EBITDA Rs 1,388 cr (18.7% margin versus 25% a year ago), net profit about Rs 850-880 cr (-35%), R&D Rs 423 cr; India at a record.

## What moves the stock (ranked)
1. **US generic pricing and the gRevlimid / gAdvair cycle** (weight about -3.5 per +5pp erosion). The profit collapse from Rs 5,269 cr (FY25) to a TTM of Rs 2,854 cr is almost entirely a US mix story: lenalidomide volumes fade while launch costs and supply issues weigh. The US$1 bn US target is the key guidance marker.
2. **USFDA enforcement on its large sites** (-2.0 per stricter unit). An OAI at a core US-supply plant would take out a visible chunk of US revenue and the inhaler approvals that underpin H2 growth.
3. **USD/INR** (+1.4 per +3%). About 38% USD-linked revenue against ~10% imported inputs. The pack's empirical +0.83 (t=0.8) agrees on sign and is lower.
4. **India demand and the domestic franchise** (urban demand +1.2, GDP +0.8). Resilient but also exposed to NPPA price-control tightening after the Supreme Court's October 2026 remarks on medicine margins.
5. **Tariffs** (-0.5): branded drugs face a 100% US tariff from 2026-09-29 but India's speciality drugs were exempted and generics sit outside; the tail is a later generic extension.
6. Costs: Middle East tension (-1.0), China API (+0.8), rates (-0.6), FPI flows (+0.6).

## Transmission examples
- **Middle East escalation -> Brent up -> freight, solvents, packaging up -> Cipla input cost up -> margin down.** Management flagged this explicitly in Q2. Brent +10% adds ~0.8% to costs, EBITDA -4% on an 18-19% base, equity about -1% after persistence.
- **Brent up -> INR weaker (India imports oil) -> USD/INR up -> Cipla's USD-linked sales translate higher -> EBITDA up.** This partly offsets the first channel: net first/second-order effect of a Brent spike is near zero to slightly negative for Cipla.
- **US generic competition up -> price erosion on inhalers and gRevlimid base -> US EBITDA falls -> group guidance cut -> P/E derates from 36x** (3rd order). Since the stock already trades on depressed earnings, a guidance miss hits the multiple twice.
- **Supreme Court / NPPA tightening of trade margins (policy) -> India trade-generic and Rx pricing pressure -> One India growth slows -> India offset to US weakness shrinks -> group EBITDA falls** (3rd order), while the same ruling hits hospitals more directly (see MAXHEALTH, FORTIS).
- **US tariff escalation -> US buyers shift to Indian vs. US-made generics? / or pass costs -> Cipla negotiates price concessions -> US margin down; rupee weakens in response -> partial offset** (4th order, low probability).

## Current situation
Q2 was in line at the US line but margins are structurally below FY25. Stock 12m -7%, 1m +4%; DIIs have been buying (34.6%) and FIIs trimming. Nomura keeps Buy (TP Rs 1,510). A new Global CTOO joined on 2026-11-04. The wholesale-licence cancellation of a Cipla entity (Oct 2026) looks administrative but is unverified.

## Upcoming events
Q3 FY27 results (late Jan 2027), USFDA site outcomes, US inhaler launches, any extension of US tariffs to generics (10% in 12m), NPPA/Supreme Court margin-cap follow-up.

## Bull case
US respiratory launches ramp, margins return to 22-24%, rupee weaker, EPS recovers toward Rs 50+ and the 36x TTM multiple compresses to 25x forward. Bear case: gRevlimid cliff steeper, a core-site OAI, tariff extension; margin stalls at 17% and P/E stays high on falling earnings. Confidence is medium: segment shares and guidance figures are partly from model knowledge, and Q2 call details were only available as headlines.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.