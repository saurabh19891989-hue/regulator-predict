# TORNTPHARM — Torrent Pharmaceuticals Ltd.
*NIFTY_NEXT_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.3%**, **12 months -7.4%** (rank 186 / 182 of 200 for 3m / 12m); beta 0.64
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.9%): 3 months 33%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.4% … P90 -4.0%; plausible 12m relative-return range incl. stock-specific noise: -26.8% … +13.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.7 pp (model impact -7.3% beta-adjusted vs realised market-adjusted move +4.9%); forward event exposure -4.7% (3m -2.5%; half assumed priced); company-specific events -0.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India NPPA/NLEM drug price control and trade-margin regulation (`NEW_NPPA_DRUG_PRICE_CONTROL`) | +1 = one tightening step (NLEM expansion or trade-margin cap) | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.99 | +0.00 | -1.82 | -1.11 | -0.05 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -2.30 | -2.50 | +0.20 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.08 | +2.00 | -0.00 | +0.01 | +0.06 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.80 | -1.80 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.61 | +0.00 | +0.00 | -1.00 | -0.60 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.58 | +0.00 | +0.00 | -0.79 | -0.79 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.46 | -1.00 | -0.47 | +0.02 | -0.01 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.40 | +0.00 | -0.53 | -0.49 | -0.38 | +0.0% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.34 | +1.50 | +0.00 | -0.05 | -0.11 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.24 | +0.00 | -0.93 | -0.16 | -0.15 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.17 | +0.00 | -0.65 | -0.42 | -0.10 | +3.5% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.02 | +0.00 | +0.42 | +0.37 | +0.23 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.02 | +0.00 | -0.87 | -0.12 | -0.03 | +9.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -7.6% | -7.6% | +0.0 | -2.6 | -2.7 | -2.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.6% | -4.6% | -4.4 | +0.0 | -0.0 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -2.1 | -1.3 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.2% | +2.6% | +5.0 | -0.0 | +0.0 | +0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.5% | -2.5% | -2.5 | +0.0 | -0.0 | +0.0 |
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.5 | +0.2 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -2.2 | -0.0 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -2.0 | +0.1 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.1% | -1.8% | +0.0 | -2.1 | -1.7 | -1.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.5 | -0.1 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.8% | +1.6% | +0.0 | +1.1 | +0.9 | +0.7 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.2 | -0.2 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → TORNTPHARM | -4.40% | -4.40% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → TORNTPHARM | -2.69% | -2.69% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → TORNTPHARM | -2.52% | -2.52% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TORNTPHARM | +5.00% | +2.50% |
| 1 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → TORNTPHARM | -2.50% | -2.50% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → TORNTPHARM | -1.32% | -1.32% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → TORNTPHARM | +1.25% | +1.25% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → TORNTPHARM | -1.19% | -1.19% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → TORNTPHARM | +1.00% | +1.00% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → TORNTPHARM | -1.00% | -1.00% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → TORNTPHARM | -0.94% | -0.94% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → TORNTPHARM | -0.94% | -0.94% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → TORNTPHARM | -0.89% | -0.89% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TORNTPHARM | -2.99% | -0.84% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → TORNTPHARM | -0.80% | -0.80% |

## Analyst profile (agent research, sourced)
# TORNTPHARM - Torrent Pharmaceuticals Ltd. (Nifty Next 50, domestic pharma)

## Business
Torrent is a branded-generics specialist: chronic cardiac, CNS, gastro-intestinal and diabetes brands in India, plus Brazil, Germany, the US and rest-of-world. The June-2026-quarter consolidation of JB Chemicals & Pharmaceuticals (acquired in 2025-26; model knowledge on deal details, financial effect verified in screener) lifted quarterly sales from Rs 3,302 cr (Sep-25) to Rs 4,979 cr (Sep-26), a 51% rise, and total assets from Rs 14.4k cr to Rs 44.6k cr. Borrowings are now Rs 14,107 cr (from Rs 3,202 cr), quarterly interest Rs 300 cr and depreciation+amortisation Rs 609 cr. Operating margin is steady at 33%.

## What moves the stock, ranked
1. **Execution of the JB integration (company-specific).** Reported PAT fell 10% in Q2 even as EBITDA rose 53% (scanx) because of financing and amortisation costs; the quarter missed estimates (CNBC TV18, 2026-10-23). Synergy delivery and deleveraging decide whether EPS growth resumes.
2. **Indian pharma market growth and pricing (F_URBAN_DEMAND +1.5; NPPA price control -3.0).** About 55-60% of group sales are domestic; chronic therapies grow faster than the market.
3. **Valuation / rates (G-sec -1.8, repo -1.0, FPI +2.0).** A premium to the sector multiple makes the stock sensitive to discount rates; RBI's 2026-10-07 hike adds to leverage costs.
4. **US generics and regulatory (US pricing -1.0, USFDA -2.5, tariff -0.5, USD/INR +0.8).**
5. **Input costs and wages (-0.8, -0.5).** Annual WPI-linked price increases on NLEM products offset most input inflation with a lag.
6. **LatAm (+1.0) and Brazil FX.**

## Transmission examples
- **Oil spike -> petrochemical feedstock up -> solvent/intermediate costs up -> Torrent cost of goods +0.3-0.8% -> NLEM price increase only at next WPI reset -> 2-3 quarter margin drag.** Then Brent up -> INR down -> imported API cost up but US/EU revenue worth more rupees (net slightly positive).
- **RBI hikes -> debt-funded JB acquisition cost rises:** repo +25bp -> floating-rate loans (about half of Rs 14.1k cr) reprice -> interest +Rs 18 cr/yr -> PAT -0.8% (small); but more important, a higher discount rate hits the 80x P/E: G-sec +25bp -> value -2%. Fourth order: sustained high rates slow urban demand -> branded volumes -> mild.
- **Government price-control tightening (NPPA) -> NLEM expansion -> hits cardiac/diabetes chronic brands -> margin -100-200bp -> sector de-rating -> read-across to Mankind/Sun/Cipla.**
- **US tariff headlines (100% on branded since 2026-09-29, Indian specialty exempt) -> generic exemption holds -> relief rally; if extended to generics -> US 10% of sales at risk -> -2% EBITDA.**

## Current situation
Q2 FY27 (2026-10-23): revenue Rs 4,979 cr (+51%), EBITDA about Rs 1,656 cr, PAT Rs 534 cr (-10%). US revenue +24%. Brokerages: Geojit Buy (target Rs 5,581), Prabhudas Lilladher Buy (Rs 5,500), Nomura Neutral (Rs 4,670). Executive Director Amal Kelshikar resigned (2026-10-16). Torrent Urja captive-power stake increased to Rs 11.88 cr.

## Valuation context
Reported P/E of 82 overstates the multiple because amortisation of acquired brands (about Rs 400 cr/qtr incremental) depresses EPS; on EBITDA the stock trades closer to sector premium levels. Cash-flow from operations was Rs 3.0k cr in FY26, so debt service is comfortable, but Rs 14k cr borrowings equal about 2.4x TTM EBITDA.

## Upcoming events
Q3 FY27 results (late Jan 2027); NLEM/WPI price notifications (Apr 2027); USFDA inspections; possible further board changes.

## Bull and bear
**Bull:** best-in-class chronic franchise plus JB brands, deleveraging as cash flows (CFO Rs 3.0k cr) repay Rs 14k cr debt, interest drag peaks in FY27, US momentum. **Bear:** amortisation and interest keep EPS flat for 4-6 quarters, valuation premium, India price-control risk, management churn. Peers compared: Mankind and Sun Pharma trade at lower multiples, so relative de-rating is a live risk if EPS does not recover. Confidence medium: headline-level sourcing for the JB deal and segment mix; no primary conference-call transcript was read.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.