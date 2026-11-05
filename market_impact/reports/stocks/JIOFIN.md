# JIOFIN — Jio Financial Services Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.2%**, **12 months -5.6%** (rank 195 / 196 of 200 for 3m / 12m); beta 1.35
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.6%): 3 months 35%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.4% … P90 +0.5%; plausible 12m relative-return range incl. stock-specific noise: -27.7% … +14.9%
- Decomposition (12m): 0.5 × forward event exposure -13.0% (3m -6.3%; half assumed priced) + 0.5 × company-specific catalysts +2.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -6.6% (beta-adjusted) vs a realised market-adjusted move of -8.4% — gap +1.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -5.98 | -5.00 | -0.47 | -0.39 | -0.12 | +3.5% |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +3.57 | +2.50 | +1.02 | +0.03 | +0.02 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.33 | -3.00 | -0.30 | -0.04 | +0.01 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -3.28 | +0.00 | -2.00 | -1.02 | -0.26 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -3.14 | -3.00 | -0.15 | +0.02 | -0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.05 | +0.00 | -1.70 | -1.21 | -0.14 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.01 | +2.50 | +0.41 | +0.04 | +0.06 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.88 | +0.00 | +2.60 | +0.16 | +0.12 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.85 | +0.00 | -1.60 | -0.48 | -0.77 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.76 | +0.00 | -1.04 | -0.71 | -1.01 | -1.1% |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -2.76 | -2.00 | -0.85 | +0.00 | +0.09 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.50 | -1.50 | -1.04 | +0.03 | +0.02 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +2.20 | +2.00 | +0.22 | +0.00 | -0.01 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.91 | +0.00 | -1.72 | -0.18 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.6% | -6.6% | -5.5 | -0.9 | -0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.3% | -5.3% | -5.1 | -0.1 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.5% | +4.8% | +8.2 | +1.0 | +0.1 | +0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -16.9% | -4.2% | -12.5 | -3.6 | -0.9 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.6% | -3.6% | +0.0 | -2.0 | -1.4 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.3% | -3.3% | -3.0 | -0.3 | +0.1 | -0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -17.4% | -2.6% | -12.5 | -4.2 | -0.7 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -2.3% | -2.3% | -1.8 | -0.4 | -0.1 | +0.0 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -4.5% | -2.3% | -4.3 | -0.1 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.9% | +2.2% | +2.0 | +0.6 | +0.9 | +0.5 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -8.6% | -2.2% | -5.0 | -1.1 | -1.6 | -0.8 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.6 | -0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → JIOFIN | -12.50% | -3.12% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JIOFIN | +6.25% | +3.12% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → JIOFIN | -12.50% | -1.88% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → JIOFIN | -5.00% | -1.25% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → JIOFIN | +2.00% | +1.24% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → JIOFIN | -2.40% | -1.20% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → JIOFIN | +2.00% | +1.10% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → JIOFIN | +2.00% | +1.00% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → JIOFIN | -3.60% | -0.90% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → JIOFIN | -1.50% | -0.90% |
| 1 | EV_UP_UPSET_OPPOSITION_WIN ⇒ F_RISK_SENTIMENT → JIOFIN | -4.00% | -0.80% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_RISK_SENTIMENT → JIOFIN | -15.00% | -0.75% |
| 1 | EV_US_CHINA_TRUCE_EXTENDED ⇒ F_RISK_SENTIMENT → JIOFIN | +1.00% | +0.72% |
| 1 | EV_BOJ_DEC26_HIKE_150 ⇒ F_RISK_SENTIMENT → JIOFIN | -1.00% | -0.70% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RISK_SENTIMENT → JIOFIN | +1.00% | +0.68% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → JIOFIN | +1.55 | director_override | -4.65% |
| 1 | F_FPI_FLOWS → JIOFIN | -1.60 | events | -4.00% |
| 1 | F_REPO_IN → JIOFIN | +1.00 | events | -1.50% |
| 1 | F_CREDIT_SPREADS_IN → JIOFIN | +0.50 | events | -1.50% |
| 1 | F_RISK_SENTIMENT → JIOFIN | +0.11 | observed | -0.56% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → JIOFIN | +0.50 | events | +0.43% |
| 1 | F_EQUITY_ACTIVITY_IN → JIOFIN | +0.20 | events | +0.36% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → JIOFIN | +1.00 | events | -0.29% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → JIOFIN | -1.56 | events | -0.25% |
| 2 | F_LIQUIDITY_IN → F_CREDIT_GROWTH_IN → JIOFIN | -0.90 | events | -0.18% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → JIOFIN | +0.50 | events | -0.16% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → JIOFIN | +1.15 | events | -0.14% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Jio Platforms listing / price discovery after Rs ~36k cr (US$3.8bn) IPO; group sentiment spillover | other | 0.85 | +0.5% | +0.42% |
| 2027-01 | Q3 FY27 results (mid-Jan 2027 est.; Q2 was 15 Oct 2026) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Closing of BofA investment into Jio Credit after regulatory approvals | corporate_action | 0.55 | +2.2% | +1.24% |
| 2027-03 | Launch of stock broking with BlackRock and Allianz insurance venture | other | 0.45 | +1.5% | +0.68% |

## Analyst profile (agent research, sourced)
# JIOFIN - Jio Financial Services (Nifty 50, NBFC holding / fintech build-out)

## Business
JIOFIN is a young financial-services platform spun out of Reliance in 2023. Subsidiaries: Jio Credit/Jio Finance (home, LAP, securities-backed, digital loans; AUM above Rs 30,000 cr in Q1 FY27), JioBlackRock Asset Management (50:50, regular plans launched 17 Aug 2026), Jio Payments Solutions and a 50% payments bank, Jio Insurance Broking, an Allianz insurance venture and a coming BlackRock broking business. In August 2026 Bank of America agreed to take up to 49.9% of Jio Credit for Rs 18,268 cr. Promoters hold 50.99% (after 25 crore share allotment on 30 Oct 2026).

## What moves the stock (ranked)
1. **Risk sentiment and flows** - beta about 1.5 to Nifty 50, FIIs 10% (down from 11.3%), plus mechanical DII/index flows. VIX +5 points is worth roughly -5%.
2. **Discount rate / yields** - TTM ROE 1.2% against P/E 92 means value sits in the future; the Oct-2026 hike and 4.89% US 10y raise the discount rate on terminal value (-3% per +25bp 10y).
3. **Funding cost** - wholesale-funded; interest expense jumped from Rs 136 cr (Sep-25) to Rs 578 cr (Sep-26). Spread widening of 50bp is about 3.5% of annualised operating profit.
4. **Execution and deal news** - BofA deal closing, broking/insurance launches, AUM milestones.
5. **Group/Reliance sentiment** - Jio Platforms IPO (launched 22 Oct 2026) can drain or lift flows; JIOFIN fell 1% on 28 Oct.

## Transmission examples
- **Middle East escalation -> Brent up (94.99, +49.5% 12m) -> India inflation and INR pressure -> RBI hawkish (hiked to 5.50% on 7 Oct) -> G-sec and AAA spreads up -> JIOFIN wholesale funding cost up -> NIM and growth slower -> multiple compresses on a P/E-92 stock.**
- **US 10y up -> FPI outflow -> Nifty down -> JIOFIN (beta 1.5, FII 10%) drops more than market -> DII index funds buy, partly cushioning (4th-order: lower retail wealth effect reduces MF/broking flows for JioBlackRock).**
- **Jio Platforms listing -> Reliance group re-rating -> group_contagion lifts JIOFIN sentiment; but absorption of Rs ~36k cr (US$3.8bn) of retail/institutional demand may crowd out other group names for weeks.**
- **Unsecured stress in India (MFI/PL) -> NBFC spread widening -> investor haircut to all new lenders -> BofA deal valuation questioned.**

## Current situation
Q2 FY27 PAT Rs 340 cr (-51% y/y) because last year's quarter held a gain and costs scaled; but NII +165% and income more than doubled. MOFSL cut FY27 estimates yet kept target Rs 300. Stock -12.6% over 3m, -23.9% over 12m, 1m +5.5%.

## Upcoming
Jio Platforms listing, Q3 results mid-Jan 2027, BofA closing, broking and insurance launches.

## Bull / bear
Bull: AUM compounds 50%+, BofA validates valuation, ecosystem cross-sell, ROE climbs towards 10% by FY29. Bear: valuation (P/E 92) has no earnings support, funding costs rise, credit quality unseasoned, group IPO diverts flows.

Uncertainty: lending-mix and funding-mix shares are model-knowledge approximations; weights are low-confidence and the empirical USDCNY +4.3 (t=2.2) sensitivity was judged spurious and not modelled.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.