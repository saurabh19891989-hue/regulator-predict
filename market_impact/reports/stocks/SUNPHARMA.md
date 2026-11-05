# SUNPHARMA — Sun Pharmaceutical Industries Ltd.
*NIFTY_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.9%**, **12 months -1.3%** (rank 133 / 126 of 200 for 3m / 12m); beta 0.69
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.9%): 3 months 46%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.5% … P90 +0.8%; plausible 12m relative-return range incl. stock-specific noise: -21.3% … +28.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.0 pp (model impact -1.4% beta-adjusted vs realised market-adjusted move -1.3%); forward event exposure -0.0% (3m +0.0%; half assumed priced); company-specific events -0.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US tariffs on pharmaceuticals (`P_US_PHARMA_TARIFF`) | +10 pp on Indian pharma exports | -1.82 | -2.00 | +0.18 | +0.00 | +0.00 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -1.70 | -2.00 | +0.30 | +0.00 | +0.00 | — |
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.31 | +1.50 | +0.00 | -0.11 | -0.08 | -1.1% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -0.86 | -0.80 | -0.04 | -0.05 | +0.03 | +11.2% |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.64 | -0.60 | -0.04 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +0.62 | +1.00 | -0.26 | -0.06 | -0.07 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.44 | +0.00 | +0.35 | +0.13 | -0.04 | +2.2% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.44 | +0.00 | -0.41 | -0.05 | +0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.43 | +0.00 | +0.16 | -0.51 | -0.08 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -0.40 | -0.40 | +0.00 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.38 | -0.40 | +0.00 | +0.00 | +0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -1.7% | -1.7% | -2.0 | +0.3 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | +0.0 | +0.0 | +0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -7.5% | -0.9% | -7.5 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | -0.0 | +0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +0.7% | +0.7% | +0.8 | +0.0 | -0.1 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | -0.1 | +0.0 | +0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -0.8% | -0.6% | -0.8 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | +0.2 | -0.6 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.4% | +0.4% | +0.0 | +0.5 | -0.0 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.4% | -0.4% | -0.3 | -0.1 | -0.0 | +0.0 |
| US Section 232 pharma tariff (100%) takes effect 29 Sep 2026; select Indian speciality drugs/ingredients exempted (`EV_US_PHARMA_232_SEP26`) | occurred | 1.00 | -0.4% | -0.4% | -0.4 | +0.0 | +0.0 | +0.0 |
| Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027 (`EV_FED_H1_2027_FURTHER_HIKES`) | anticipated | 0.40 | -0.8% | -0.3% | -0.8 | +0.0 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → SUNPHARMA | -3.00% | -0.75% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → SUNPHARMA | -6.00% | -0.72% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → SUNPHARMA | +2.40% | +0.60% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → SUNPHARMA | -0.80% | -0.58% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → SUNPHARMA | +0.71% | +0.39% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → SUNPHARMA | +1.95% | +0.35% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → SUNPHARMA | -0.69% | -0.35% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → SUNPHARMA | -0.62% | -0.34% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → SUNPHARMA | -0.80% | -0.32% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → SUNPHARMA | -1.20% | -0.30% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → SUNPHARMA | +1.04% | +0.26% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → SUNPHARMA | -0.48% | -0.24% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ F_US_GENERIC_PRICING → SUNPHARMA | -1.50% | -0.18% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → SUNPHARMA | -0.30% | -0.18% |
| 1 | EV_FED_H1_2027_CUTS ⇒ F_FED_FUNDS → SUNPHARMA | +1.20% | +0.14% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_USFDA_ENFORCEMENT → SUNPHARMA | +1.00 | events | -2.00% |
| 1 | F_FED_FUNDS → SUNPHARMA | +1.62 | observed | -1.30% |
| 1 | F_US_GDP → SUNPHARMA | +1.20 | events | +1.20% |
| 1 | F_GSEC_10Y_IN → SUNPHARMA | +1.55 | director_override | -0.93% |
| 1 | F_USDINR → SUNPHARMA | -0.37 | observed | -0.55% |
| 1 | P_US_PHARMA_TARIFF → SUNPHARMA | +0.20 | events | -0.40% |
| 2 | P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → SUNPHARMA | +1.00 | events | +0.30% |
| 1 | F_CREDIT_SPREADS_IN → SUNPHARMA | +0.50 | events | -0.20% |
| 1 | F_CHINA_GDP → SUNPHARMA | +0.30 | events | -0.12% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → SUNPHARMA | +0.40 | events | -0.06% |
| 2 | P_US_PHARMA_TARIFF → F_US_GENERIC_PRICING → SUNPHARMA | +0.20 | events | +0.04% |
| 2 | F_BRENT → F_CHEM_FEEDSTOCK → SUNPHARMA | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Closing of Innovcare Lifesciences acquisition (Rs271.2 cr, announced 2026-11-02) | corporate_action | 0.70 | +0.1% | +0.03% |
| 2026-12 | Rs10,000 cr NCD issue to refinance Organon acquisition loan | corporate_action | 0.80 | -0.1% | -0.08% |
| 2026-12 | US tariff implementation details / carve-outs for generics and Sun's specialty products | regulatory | 0.40 | -1.0% | -0.40% |
| 2027-02 | Q3 FY27 results (late Jan/early Feb) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Organon acquisition closes (Q4 FY27 per mgmt); regulatory approvals and financing done | corporate_action | 0.80 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Sun Pharmaceutical Industries Ltd. (SUNPHARMA) - company profile, as of 2026-11-05

## Business
Sun Pharma is India's largest pharmaceutical company and a global specialty player. Of Q2 FY27 sales of Rs16,199 cr, roughly a third comes from India branded formulations, a quarter from the US ($455m in the quarter, down), a fifth from emerging markets and the rest from Europe, Canada, Japan, Israel and APIs (the split is approximate, model knowledge). Operating margin was 29%. Profit fell 36% to Rs1,995 cr because of one-time charges for the ~$12bn Organon acquisition, which shareholders approved on 2026-07-24 and management guides to close in Q4 FY27. Specialty drugs (Ilumya, Winlevi, Cequa, Leqselvi) drive growth, but Ilumya slowed.

## What moves the stock (ranked)
1. **Organon execution (company event)**: leverage and integration are the largest swing; financing is under way (a Rs10,000 cr bond, board had considered Rs15,000 cr). Impact -5% to +5% depending on terms, synergies and closure.
2. **US tariffs and pricing**: P_US_PHARMA_TARIFF -2.0 per +10pp and US generic price erosion -1.5 per +5pp. The 100% pharma tariff began 2026-09-29, with select Indian specialty drugs exempt; coverage of Sun's SKUs is unverified.
3. **USD/INR**: +1.5 per +3% (net long USD ~40% of revenue).
4. **USFDA enforcement**: -2 per stricter episode.
5. **Funding costs**: Fed funds, India G-sec yields and credit spreads matter more after the Organon debt.
6. **Input costs (feedstock) and China**: -0.8 and -0.4.
7. **India premiumisation**: +1.

## Transmission examples
- **US tariff escalation -> P_US_PHARMA_TARIFF -> generic exports to the US become uneconomic for some SKUs -> shortages and US price increases (2nd order) -> partial pass-through or exemptions -> Sun's US earnings -> Sun's ability to service Organon debt (4th order)**.
- **Middle East conflict -> Brent up -> solvent and logistics cost up -> margin -> also INR weaker -> export margin up**; net mildly positive for exporters.
- **Fed higher for longer -> US floating-rate debt on Organon more costly -> interest cover -> rating risk**.
- **China growth up -> intermediate prices up -> Sun's API costs rise with a lag**.

## Current situation
The stock fell to a 5-month low on 2026-10-14, rose after Q2 on 2026-10-30, then slipped 3% on 2026-11-02 despite brokerages (Prabhudas Lilladher Rs2,150 target). A promoter reclassification (Valia family) cut promoter holding to 52.68%. The Rs271.2 cr Innovcare buy is small.

## Upcoming
Organon close (Q4 FY27), NCD issuance, Q3 FY27 results around early February 2027, tariff details.

## Bull case
Organon closes cleanly, Leqselvi and Winlevi ramp, specialty tariff exemption holds, P/E normalises as one-time charges roll off.

## Bear case
Ilumya fades, US generics erode faster, FDA action hits a site, and leverage rises after Organon.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.