# CANBK — Canara Bank
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months -0.5%** (rank 84 / 132 of 200 for 3m / 12m); beta 1.27
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.0%): 3 months 51%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.3% … P90 +2.3%; plausible 12m relative-return range incl. stock-specific noise: -16.8% … +37.0%
- Decomposition (12m): 0.5 × forward event exposure -0.2% (3m +1.1%; half assumed priced) + 0.5 × company-specific catalysts +0.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -2.2% (beta-adjusted) vs a realised market-adjusted move of -10.3% — gap +8.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.00 | -7.00 | +0.00 | -0.02 | +0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -5.67 | -4.50 | -1.41 | +0.15 | +0.09 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.79 | +0.00 | +1.18 | +1.92 | -0.32 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.51 | +2.40 | +0.07 | -0.01 | +0.05 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.50 | +0.00 | +3.04 | -0.50 | -0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.82 | -1.80 | +0.00 | -0.02 | -0.00 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.53 | +0.00 | +0.19 | +1.72 | -0.38 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.40 | +0.00 | -0.86 | -0.49 | -0.06 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.32 | +0.00 | -0.70 | -0.32 | -0.29 | -1.1% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.23 | +0.80 | +0.00 | +0.53 | -0.09 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.21 | +0.00 | -0.98 | -0.06 | -0.18 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.18 | +0.00 | +0.16 | -0.58 | -0.76 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.14 | +0.00 | -1.07 | -0.12 | +0.04 | +9.4% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.13 | +0.40 | +0.03 | +0.60 | +0.10 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.5% | -5.5% | -5.3 | -0.2 | +0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.3% | +3.1% | +6.0 | +0.2 | -0.0 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.7 | -0.1 | +0.0 | -0.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.5% | -2.3% | -2.6 | +0.0 | +0.0 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +0.8 | +1.5 | -0.3 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -0.5 | -0.9 | -0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.6 | +0.0 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.4% | -1.4% | -0.5 | -0.0 | -0.8 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.4% | +1.4% | +1.2 | +0.2 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.2 | -0.2 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.0% | -1.2% | +0.0 | -4.4 | -0.5 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -5.7% | -1.0% | -5.6 | -0.5 | +0.4 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CANBK | +6.00% | +3.00% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → CANBK | -1.35% | -1.21% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → CANBK | -1.05% | -0.95% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → CANBK | -1.44% | -0.72% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → CANBK | -3.60% | -0.65% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → CANBK | -2.30% | -0.58% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → CANBK | -2.30% | -0.58% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → CANBK | -2.24% | -0.56% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → CANBK | -0.90% | -0.54% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → CANBK | -1.80% | -0.54% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → CANBK | +1.20% | +0.42% |
| 2 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → CANBK | -3.36% | -0.40% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → CANBK | +0.48% | +0.38% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → CANBK | -0.60% | -0.36% |
| 2 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → CANBK | +0.45% | +0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → CANBK | -1.60 | events | -3.84% |
| 1 | F_GSEC_10Y_IN → CANBK | +1.55 | director_override | -2.79% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → CANBK | +0.50 | events | +1.12% |
| 1 | F_MONSOON → CANBK | -1.56 | events | -0.62% |
| 1 | F_GOLD → CANBK | -1.05 | observed | -0.52% |
| 1 | F_REPO_IN → CANBK | +1.00 | events | +0.40% |
| 1 | F_LIQUIDITY_IN → CANBK | -0.90 | events | -0.36% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → CANBK | +0.50 | events | -0.36% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → CANBK | -0.25 | events | -0.28% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → CANBK | +1.00 | events | -0.28% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → CANBK | +0.50 | events | +0.20% |
| 1 | F_GOVT_CAPEX → CANBK | +0.20 | director_override | +0.16% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Q3 FY27 results (Q2 declared 2026-10-14; typical late-Jan timing) | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Canara Bank (CANBK) - Market Impact profile, as of 2026-11-05

## Business
Canara Bank is one of India's largest public-sector banks (government 62.93%), headquartered in Bengaluru, with a dense South-India branch network, a large agri and gold-loan book, retail/MSME lending and a corporate portfolio. It also owns stakes in asset-management and life-insurance subsidiaries (Canara Robeco AMC, Canara HSBC Life - listed in 2025 per model knowledge, unverified here). Q2 FY27 (Sep 2026): PAT Rs5,175cr (+8.4% y/y), NII ~Rs11,005cr, NIM 2.55%, gross NPA 1.33%, net NPA 0.30% (23rd straight quarterly improvement), global advances +19.5% y/y and total business Rs30.72 lakh cr (+15.9%). The quarter was dented by treasury losses as the 10-year G-sec rose to ~7.4-7.5%, and on 15 Oct management said the expected-credit-loss (ECL) transition could cost Rs12-15k cr, recognised over about two years, absorbed without fresh equity (CET1 12.80%).

## What moves the stock, ranked
1. **Asset quality (-7.0 per +50bp credit cost)** - the largest sensitivity, though GNPA is at a record low.
2. **ECL / prudential regulation (-4.5)** - management-disclosed scale equals ~13% of market cap pre-tax; the stock already fell 6%.
3. **G-sec yield (-1.8 per +25bp)** - the highest AFS/FVTPL sensitivity among the batch banks; treasury losses already reported.
4. **FPI flows (+2.4)** - beta 1.40-1.46 and FII stake falling.
5. **Credit growth (+1.2), deposit growth (+0.9), repo (+0.4), liquidity (+0.4)**.
6. Secondary: agri/monsoon (+0.4), gold (+0.5), govt capex (+0.8), subsidiaries/domestic flows (+0.5), unsecured stress (-0.4).
Empirical check: no factor in the pack reaches |t|>=2 (the strongest are edible oil +1.44 t 1.3 and Fed funds +1.86 t 1.2, both spurious beta-type co-movements), so we rely on fundamentals; the high market beta (1.4) means this stock amplifies any broad risk-on/off move.

## Transmission examples
- **Middle East escalation -> Brent up -> CPI up -> RBI tightens again -> 10y yield up -> Canara's AFS book marks down and the ECL phasing becomes costlier** (HTM MTM is Rs2-3k cr of the ECL estimate and is yield-sensitive). Fourth order: lower CET1 -> equity raise risk -> dilution.
- **Brent up -> INR weaker -> FPI selling -> PSU bank multiples compress** (FIIs already sold from 14.2% to 12.3%); at the same time, higher funding costs squeeze a NIM already at its 2.5% floor.
- **Good monsoon -> rural incomes up -> agri slippages down -> credit cost down**, and higher gold prices lift gold-loan balances.
- **RBI hike -> repo-linked loans (~50% of domestic book) reprice quickly -> NIM up temporarily -> deposits catch up and credit demand cools** - a short-lived positive that fades.

## Current situation
Rs122, near its 52-week low (Rs115), down 12% over 12 months. Q2 initially lifted the stock 5% on 14 Oct (core income +20%, asset quality better) before the next-day ECL and treasury-loss disclosure sank it 6%. 

## Upcoming
Q3 results (late Jan 2027), RBI Dec MPC, ECL effective date and phasing, subsidiary value events, possible capital raise (low probability).

## Bull and bear
**Bull:** 19.5% advances growth, spotless NPAs, 0.86x book, 3.5% yield, subsidiary value, ECL absorbable organically. **Bear:** ECL hit, rising yields, NIM at floor, FII exodus, and growth reliant on costlier funding.

## Valuation and positioning notes
At Rs122 and 0.86x book, the market capitalises Canara at roughly 5.5x trailing earnings with a 16.1% ROE (screener.in). That multiple implicitly assumes the ECL charge is largely one-off and that credit costs rise from today's very low base. The main swing factor is capital: with CET1 at 12.80% and CRAR at 17.19%, a Rs15,000cr charge phased over two years is covered by roughly Rs20,000cr of annual earnings, which is why management sees no need for equity. The risk case is a faster phase-in or a yield spike that forces HTM mark-to-market into the same window, which would compress CET1 toward 12% and reopen the dilution debate.

Ownership flows matter in the short run: promoters 62.93% (unchanged), FIIs 12.27% (down 2 points in six months) and DIIs 12.37% (up 1.5 points). Any reversal of the FII selling would be a cheap catalyst for a high-beta PSU stock. The Director's propagation should net out the market component of the FPI edge, and should treat the G-sec, ECL and asset-quality edges as overlapping stress channels for the same capital buffer rather than additive shocks.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.