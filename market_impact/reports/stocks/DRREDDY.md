# DRREDDY — Dr. Reddy's Laboratories Ltd.
*NIFTY_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +0.1%** (rank 96 / 102 of 200 for 3m / 12m); beta 0.69
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 50%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.2% … P90 +4.8%; plausible 12m relative-return range incl. stock-specific noise: -37.8% … +27.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.8 pp (model impact -3.6% beta-adjusted vs realised market-adjusted move +2.3%); forward event exposure +3.6% (3m +1.7%; half assumed priced); company-specific events +2.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -4.00 | -4.00 | +0.00 | +0.00 | +0.00 | — |
| GLP-1 / obesity drug adoption (`T_GLP1`) | +1 | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.93 | +3.20 | -0.16 | -0.10 | -0.01 | -1.1% |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -2.20 | -3.00 | +0.80 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.99 | -0.80 | -0.16 | -0.04 | +0.00 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +0.80 | +0.00 | +0.94 | -0.05 | -0.09 | +0.0% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.78 | +0.00 | -0.39 | -0.33 | -0.05 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.75 | +0.00 | -0.34 | -0.28 | -0.13 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.75 | +0.00 | +0.49 | +0.28 | -0.03 | +2.2% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +0.59 | +0.70 | +0.00 | -0.05 | -0.07 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | -0.57 | +0.00 | +0.00 | -0.56 | -0.00 | — |
| Foreign portfolio flows into Indian government/corporate bonds (FAR, index-linked) (`NEW_FPI_DEBT_FLOWS`) | +US$5 bn net debt inflow per quarter | -0.54 | +0.00 | -0.64 | +0.06 | +0.04 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +0.50 | +0.00 | +0.32 | +0.23 | -0.05 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +3.0% | +3.0% | -1.0 | +4.6 | -0.2 | -0.4 |
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -2.2% | -2.2% | -3.0 | +0.8 | +0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.2 | +0.1 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.0% | -1.0% | -0.8 | -0.2 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.5 | -0.4 | -0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -6.4% | -0.8% | -6.4 | +0.0 | +0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.2 | -0.5 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +0.6% | +0.6% | +0.0 | +0.2 | +0.5 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +1.6% | +0.6% | -0.8 | +2.5 | +0.0 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.6% | -0.6% | -1.3 | +0.8 | -0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | +0.5% | +0.5% | +0.0 | +0.2 | +0.4 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | +2.4% | +0.5% | +2.5 | -0.0 | -0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → DRREDDY | +5.01% | +5.01% |
| 1 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → DRREDDY | -3.00% | -3.00% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → DRREDDY | -1.32% | -1.32% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → DRREDDY | -1.18% | -1.18% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → DRREDDY | -1.06% | -1.06% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → DRREDDY | -1.05% | -1.05% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → DRREDDY | +4.16% | +0.92% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → DRREDDY | +2.53% | +0.90% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → DRREDDY | -1.52% | -0.88% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → DRREDDY | -0.80% | -0.80% |
| 2 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → DRREDDY | +0.80% | +0.80% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DRREDDY | +1.50% | +0.75% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_USDINR → DRREDDY | +0.74% | +0.74% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → DRREDDY | -0.71% | -0.71% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → DRREDDY | +0.65% | +0.65% |

## Analyst profile (agent research, sourced)
# DRREDDY (Dr. Reddy's Laboratories) — Nifty 50, as of 2026-11-05

## Business
Dr. Reddy's is a global generics and active-ingredient house with growing biosimilars and branded franchises. Approximate sales mix (model knowledge): North America ~38%, India ~27%, Emerging markets ~17%, Europe ~10%, PSAI ~8%. Q2 FY27 (2026-10-23): sales Rs 8,698 cr (about -1.5%), EBITDA Rs 1,723 cr (20%), net profit Rs 913-925 cr (-36% YoY), ahead of consensus. Margin has rebounded from 5% (Mar-26 quarter) and 11% (Jun-26) as the semaglutide supply disruption (Obeda) fades; management guides about 20% EBITDA for FY27 and 25% long term (Sahi 2026-09-29).

## What moves the stock (ranked)
1. **Generic semaglutide** (T_GLP1 +4.0 per unit): Canada relaunch in November 2026, Brazil ANVISA approval on 2026-11-05, India oral tablets and new generic Ozempic brands from late October. It is the largest identifiable earnings option and the main reason for the recent +16% 3-month move.
2. **US generic pricing and the gRevlimid fade** (-4.0 per +5pp erosion): the TTM profit has halved from FY25 because lenalidomide sales declined; replacements (US launches, double-digit growth guidance) decide whether FY28 EPS recovers.
3. **USD/INR** (+3.2 per +3%): the largest simple translation channel; rupee strength in October is a Q3 headwind. Pack empirical +1.73 (t=1.4) is lower.
4. **USFDA** (-3.0): FTO-9 Visakhapatnam PAI closed with three Form 483 observations in mid-October; classification due in coming weeks.
5. **Tariffs** (-0.8): generics are outside the US branded-pharma tariff so far.
6. Rates, China APIs, India demand, Middle East, flows (each under 1).

## Transmission examples
- **Semaglutide patent expiry (Canada/Brazil/India) -> multiple generic entrants -> price erosion on semaglutide -> DRL's first-mover premium shrinks -> margin gains from the launch fade within 12-18 months** (2nd to 3rd order; the launch benefit is front-loaded).
- **Middle East escalation -> Brent up -> INR weaker -> DRL's USD-linked earnings up -> EBITDA up; but freight, solvent and Russia/CIS payment risks offset** (net slightly positive; consistent with the pack's Brent +0.79).
- **US generic competition up -> gRevlimid and base price erosion -> US EBITDA down -> FY28 EPS cuts -> P/E derates from 40x** (3rd order).
- **USFDA 483 at Visakhapatnam -> OAI -> delayed biosimilar/semaglutide filings -> abatacept and Canada supply slip -> growth narrative loses 2027 legs** (3rd/4th order).
- **US tariff expansion to generics -> US customers push price cuts -> DRL absorbs half -> US margin falls; rupee weakens in response -> partial offset** (low probability).

## Current situation
Stock +13% over 12m, +16% over 3m, supported by Citi (Buy, 2026-09-29), BNP (Outperform), and a JPMorgan upgrade after Q2. DRL announced three semaglutide-related milestones within one week of Q2. Debt has risen with the acquisition spree (interest Rs 125 cr/qtr vs Rs 83 cr a year earlier).

## Upcoming events
Canada semaglutide relaunch (Nov), FTO-9 classification (Dec), Q3 results (late Jan 2027), abatacept filings, possible tariffs on generics.

## Bull and bear
Bull: semaglutide scales across Canada, Brazil, India; US grows double digits; EBITDA returns to 23-25%; EPS Rs 60+ by FY28 makes 40x TTM look like 22x forward. Bear: price war in semaglutide, a plant OAI, gRevlimid cliff and a strong rupee; EPS stalls near Rs 35-40 and the 40x multiple compresses. Confidence medium: call content came from headlines, segment shares are model knowledge.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.