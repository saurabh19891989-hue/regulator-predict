# HDFCAMC — HDFC Asset Management Company Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.5%**, **12 months +0.1%** (rank 88 / 103 of 200 for 3m / 12m); beta 1.30
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.5%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.6% … P90 +2.2%; plausible 12m relative-return range incl. stock-specific noise: -26.8% … +32.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.2 pp (model impact +0.5% beta-adjusted vs realised market-adjusted move -5.0%); forward event exposure +2.1% (3m +2.2%; half assumed priced); company-specific events -0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +5.38 | +4.00 | +1.24 | +0.17 | -0.02 | — |
| SEBI mutual fund fee / TER / brokerage regulation (`NEW_SEBI_MF_FEE_REG`) | -5bp on active-equity gross fee yield | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| AMC competition intensity (passives, new entrants) (`NEW_AMC_COMPETITION`) | +1 = 0.5pp loss of active-equity AUM market share | -3.50 | -3.50 | +0.00 | +0.00 | +0.00 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -3.46 | -2.50 | -0.76 | -0.19 | -0.01 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +2.72 | +2.50 | +0.24 | -0.01 | -0.01 | — |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +1.88 | +2.00 | -0.05 | -0.06 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.87 | +1.50 | +0.37 | -0.02 | +0.01 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.49 | +0.00 | +0.86 | +0.49 | +0.14 | +1.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.43 | -0.80 | -0.28 | -0.28 | -0.07 | +3.5% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.37 | +0.00 | -0.63 | -0.71 | -0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.32 | +0.00 | -0.53 | -0.57 | -0.21 | -1.1% |
| Digital payments / UPI disruption of incumbents (`T_DIGITAL_PAYMENTS`) | +1 | +1.30 | +0.00 | +0.64 | +0.52 | +0.14 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.27 | +0.00 | -0.26 | -0.37 | -0.65 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.21 | -1.20 | +0.00 | +0.00 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.1% | -5.1% | +0.0 | -1.3 | -2.1 | -1.8 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.4% | -4.4% | -3.6 | -0.8 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.0% | +2.5% | +4.1 | +0.9 | -0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -7.1% | -2.0% | -3.2 | -2.6 | -1.4 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.5 | -0.4 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.4 | -0.4 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -0.7 | -0.8 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -8.5% | -1.5% | -4.0 | -3.2 | -1.4 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.9% | -1.4% | -1.0 | -0.8 | -1.2 | -0.9 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.8 | -0.4 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.0% | +1.2% | +0.4 | +0.4 | +0.7 | +0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HDFCAMC | +3.75% | +1.88% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → HDFCAMC | -3.20% | -0.90% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → HDFCAMC | -4.00% | -0.72% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → HDFCAMC | -2.25% | -0.49% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → HDFCAMC | -0.96% | -0.48% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ P_CAPITAL_GAINS_TAX → HDFCAMC | +1.25% | +0.44% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → HDFCAMC | -1.44% | -0.40% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → HDFCAMC | +0.80% | +0.40% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → HDFCAMC | -2.00% | -0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → HDFCAMC | -1.44% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → HDFCAMC | -0.60% | -0.36% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → HDFCAMC | -0.96% | -0.34% |
| 1 | EV_SEBI_CAS_DERIV_REVERSAL ⇒ F_EQUITY_ACTIVITY_IN → HDFCAMC | +0.40% | +0.34% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HDFCAMC | -1.12% | -0.31% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → HDFCAMC | -1.15% | -0.29% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → HDFCAMC | -1.60 | events | -2.40% |
| 1 | F_GSEC_10Y_IN → HDFCAMC | +1.70 | events | -2.04% |
| 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → HDFCAMC | -1.60 | events | -0.51% |
| 1 | F_REPO_IN → HDFCAMC | +1.00 | events | -0.30% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → HDFCAMC | +0.30 | events | +0.19% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → HDFCAMC | +0.30 | events | +0.09% |
| 1 | F_RISK_SENTIMENT → HDFCAMC | +0.11 | observed | -0.09% |
| 1 | P_SEBI_DERIVATIVES → HDFCAMC | -0.10 | events | -0.08% |
| 3 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → HDFCAMC | -1.60 | events | +0.07% |
| 2 | P_SEBI_DERIVATIVES → F_EQUITY_ACTIVITY_IN → HDFCAMC | -0.10 | events | +0.06% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_EQUITY_ACTIVITY_IN → HDFCAMC | +0.30 | events | +0.02% |
| 4 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → F_EQUITY_ACTIVITY_IN → HDFCAMC | +0.30 | events | +0.02% |

## Analyst profile (agent research, sourced)
# HDFC Asset Management (HDFCAMC) - Market Impact profile, as of 2026-11-05

## Business
HDFC AMC is India's largest active-equity mutual fund manager and one of the most profitable asset managers globally: 52.3% owned by HDFC Bank, debt-free, ROE of 33% and an operating margin near 80%. It earns a management fee on average AUM (blended yield ~47-48bp; active equity ~58bp). Q2 FY27 QAAUM was Rs9.69 lakh cr (+10% y/y, +4% q/q), of which equity-oriented Rs6.51 lakh cr; overall market share 11.1%, active-equity share 12.7% (down 10bp q/q, 20bp y/y, per Motilal Oswal). Revenue ~Rs1,170cr rose ~14% y/y while PAT (~Rs750cr) rose only ~4% as the SEBI fee reset (effective 1 Apr 2026: lower brokerage caps and TER restructuring) and higher costs bit. The shares trade at ~38x earnings and 13x book.

## What moves the stock, ranked
1. **Fee regulation (-5.0 per -5bp of active-equity yield)**: the biggest single idiosyncratic risk; largely priced after the final April 2026 rules.
2. **Competition / market share (-3.5 per 0.5pp share loss)**: drift is already negative.
3. **Domestic flows (+2.5), equity activity (+2.0), FPI flows (+1.5)**: AUM x yield mechanics; equity mark-to-market flows straight to revenue.
4. **Financialisation theme (+4.0)**: structural SIP culture; the long-term driver of valuation.
5. **Capital gains tax (-2.5)**, **G-sec yield (-1.2)** for a 38x stock, **VIX (-0.8)**, **SEBI F&O curbs (+0.8)**, **repo (-0.3)**.
Empirical check: gas (-0.86, t -2.4), Brent (-1.07, t -2.3) and refining margin (-0.98, t -2.2) are statistically significant market-adjusted co-movements, but they proxy global risk-off / energy-shock episodes that hit equity AUM, not a fundamental channel. We capture their common cause through F_RISK_SENTIMENT and F_FPI_FLOWS and do not add direct energy edges (a direct Brent edge would double-count the Brent -> INR -> FPI -> equity chain).

## Transmission examples
- **Middle East escalation -> Brent up (energy shock) -> inflation and RBI tightening (repo now 5.50%) -> equity market falls and FPI outflows -> equity AUM marked down -> management-fee revenue down at near-fixed costs -> PAT falls ~1.2x the AUM decline.** Third order: SIP stoppages and redemptions rise, cutting future flows.
- **Brent up -> INR weaker -> FPI selling -> Nifty down -> HDFC AMC AUM down** (the pack's significant Brent -1.07 coefficient is consistent with this).
- **SEBI cracks down on retail F&O -> retail money moves to SIPs -> industry flows up -> HDFC AMC share of flows (12.7%) -> revenue.** A positive 3rd-order path (+0.8 per step).
- **Rate hikes -> FDs more attractive -> savers shift from debt funds and balanced products; but liquid funds gain** - ambiguous, net small.
- **Higher capital gains tax in the Feb 2027 Budget -> lower post-tax returns -> lower inflows -> lower AUM growth.**

## Current situation
Stock Rs2,633 (+11.9% over a month; -2.6% over 12m). Q2 slightly missed consensus; SIP AUM was flat q/q (Motilal) while industry monthly SIP hit records. Market-share erosion and the fee reset are the two debates. The company took a 2.9% stake in EAAA India Alternatives (2 Nov), signalling push into alternatives.

## Upcoming
Q3 results (Jan 2027), Union Budget (1 Feb 2027), monthly AMFI data, possible SEBI follow-ups.

## Bull and bear
**Bull:** structural SIP growth, best-in-class returns on capital, distribution expansion, alternatives, benign regulatory outcome. **Bear:** 38x P/E leaves no room for a market drawdown, active share loss, fee compression, tax changes and slowing profit growth (+4% y/y).

## Sizing notes and caveats
Blended yield check: Q2 revenue ~Rs1,170cr x4 / QAAUM Rs9.69 lakh cr = ~48bp, consistent with the ~47bp reported for the prior year. PAT/AUM is ~31bp, so a 1% change in average AUM maps to roughly 1% in PAT given the 79% operating margin and largely fixed cost base. This is why the AUM-linked edges (flows, FPI, risk sentiment) are sized near 1:1 on earnings, then scaled by persistence and the EV/market-cap ratio (~0.97 given Rs8,000cr+ of treasury assets). Industry-level market effects are removed by the Director's cross-sectional demeaning, so only the beta above 1 and the flow-specific components should drive relative rankings.

Evidence gaps: no Q2 yield or HDFC-AMC-specific SIP inflow figure was found; SEBI impact estimates (Jefferies -8-10% FY27 PBT, Centrum -6-10% over FY25-28E) were made on the draft rules and may overstate the final impact; the stake edge to HDFC Bank is intentionally small. Two new nodes (NEW_SEBI_MF_FEE_REG, NEW_AMC_COMPETITION) are proposed for the vocabulary.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.