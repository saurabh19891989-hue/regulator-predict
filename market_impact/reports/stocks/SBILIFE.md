# SBILIFE — SBI Life Insurance Company Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -1.3%** (rank 112 / 123 of 200 for 3m / 12m); beta 0.92
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.8%): 3 months 49%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.8% … P90 +1.5%; plausible 12m relative-return range incl. stock-specific noise: -36.8% … +21.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.1 pp (model impact +0.2% beta-adjusted vs realised market-adjusted move -8.5%); forward event exposure -0.0% (3m +1.2%; half assumed priced); company-specific events -0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +3.29 | +3.00 | +0.32 | -0.01 | -0.02 | — |
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -2.72 | -2.50 | -0.18 | -0.04 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.48 | +2.50 | -0.01 | -0.02 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.36 | +0.00 | -0.84 | -1.01 | -0.51 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.21 | -1.50 | -0.47 | -0.25 | -0.00 | +3.5% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.11 | +2.00 | +0.14 | -0.03 | +0.00 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.02 | +0.00 | +1.52 | +0.45 | +0.05 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.84 | +0.00 | -0.60 | -0.82 | -0.42 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.52 | +0.00 | +1.20 | +0.18 | +0.15 | — |
| US growth (`F_US_GDP`) | +1 pp | +1.44 | +0.00 | +0.45 | +0.92 | +0.08 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.44 | +0.00 | +1.28 | +0.17 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.41 | +0.00 | +1.28 | +0.17 | -0.04 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.33 | -0.80 | -0.54 | +0.00 | +0.01 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.24 | +0.00 | -1.10 | -0.15 | +0.00 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.1% | -6.1% | -6.1 | +0.0 | +0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.3% | -5.3% | -1.5 | -2.3 | -1.3 | -0.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.8% | +3.4% | +6.8 | -0.0 | -0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -10.4% | -2.9% | -6.0 | -4.3 | -0.3 | +0.2 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -12.6% | -2.3% | -7.5 | -5.3 | +0.1 | +0.2 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.8% | +1.8% | +0.0 | +0.5 | +1.0 | +0.3 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -6.8% | -1.7% | +0.0 | -5.7 | -0.7 | -0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.7% | -1.7% | -2.5 | -1.4 | -0.7 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -0.7 | -0.6 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.3% | +1.3% | +1.2 | +0.7 | +0.4 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.5 | +0.1 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.2% | +1.2% | +1.2 | -0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SBILIFE | +6.25% | +3.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → SBILIFE | -6.00% | -1.68% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → SBILIFE | -7.50% | -1.35% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → SBILIFE | -1.75% | -0.88% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → SBILIFE | -3.75% | -0.82% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBILIFE | -2.40% | -0.67% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → SBILIFE | -1.80% | -0.64% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → SBILIFE | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → SBILIFE | -2.16% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → SBILIFE | -1.87% | -0.52% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → SBILIFE | +0.58% | +0.52% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → SBILIFE | +1.25% | +0.44% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → SBILIFE | +0.75% | +0.44% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → SBILIFE | -2.33% | -0.42% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → SBILIFE | +0.50% | +0.40% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → SBILIFE | -1.60 | events | -4.00% |
| 1 | F_GDP_IN → SBILIFE | +0.50 | events | +1.00% |
| 1 | F_CPI_IN → SBILIFE | +1.15 | events | -0.69% |
| 1 | F_GSEC_10Y_IN → SBILIFE | +1.70 | events | +0.51% |
| 1 | F_REPO_IN → SBILIFE | +1.00 | events | -0.50% |
| 1 | F_RISK_SENTIMENT → SBILIFE | +0.11 | observed | -0.17% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → SBILIFE | +0.30 | events | +0.14% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → SBILIFE | +0.30 | events | +0.03% |
| 3 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → SBILIFE | -1.60 | events | +0.02% |
| 3 | P_SEBI_DERIVATIVES → F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → SBILIFE | -0.10 | events | -0.01% |
| 4 | P_SEBI_DERIVATIVES → F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → F_DOMESTIC_FLOWS → SBILIFE | -0.10 | events | -0.00% |
| 1 | F_BRENT → SBILIFE | +0.00 | observed | -0.00% |

## Analyst profile (agent research, sourced)
# SBILIFE - SBI Life Insurance (as of 2026-11-05)

## Business
SBI Life is India's largest private life insurer by assets, ~55% owned by State Bank of India (model knowledge). Most individual new business comes through SBI's branch network; the rest through agents, brokers and direct. Products: non-par and par savings, ULIPs, credit life and group term protection, annuity. Q2 FY27: PAT Rs549cr (+11% YoY, ET), VNB Rs1,860cr (+12%), VNB margin 29.1% (+116bp), APE ~Rs6,390cr, H1 new business premium Rs20,259cr (company release via Yahoo Finance, 2026-10-28). The screener extract for this ticker was empty, so valuation fields here come from model estimates and broker targets (Rs2,100-2,217).

## What moves the stock (ranked)
1. **IRDAI commission/EoM reform (-2.5, range -8 to +2).** The 2026-09-23/24 draft caps product-wise commissions; SBI Life fell ~7% on the day but later reports put it within the proposed caps and credit-life attachment below 50% (ET BFSI, 2026-10-29), so it is the least exposed major listed insurer.
2. **Structural financialisation (+3.0) and GDP (+2.0).**
3. **FPI flows (+2.5) and risk sentiment (-1.5):** large-cap Nifty 50 beta ~0.85.
4. **Rates (repo -0.5, G-sec +0.3):** FD competition vs guaranteed-product pricing.
5. **Domestic flows (+0.8), capital gains tax (-0.8), CPI (-0.6).**
Pack empirics: Brent -0.69 per SSU (t -1.8, marginal), copper +1.76 (t 2.8) has no mechanism and is treated as spurious.

## Transmission examples
- **IRDAI cap finalised -> distributor commissions fall (banks/agents/brokers) -> private insurers lose bank push (e.g. HDFC Life, Max) -> SBI Life, captive to SBI and already inside caps, gains relative share -> VNB margin above the 26-28% guide -> re-rating.** Alternatively a harsher final rule hits credit-life margins.
- **Middle East escalation -> Brent up -> CPI up -> RBI 'calibrated tightening' after the 2026-10-07 hike -> FD rates +25bp -> savings substitution from non-par products -> APE below the 14-15% guidance; 4th order: lower VNB lowers P/EV.**
- **Equity sell-off (VIX +5) -> ULIP sales fall and AUM-linked fees drop -> SBIN's 10% look-through holding weakens -> SBIN sentiment feeds back (0.15).**
- **FM opens LTCG/STT review (2026-10-13) -> retail equity activity up -> ULIP appeal up and market multiples rise.**

## Current situation
Strong prints (VNB +12%, margin 29.1%) but the share price is -12% over 12 months and -6.8% in 3 months. Brokers (Motilal Rs2,100, ICICI Sec Rs2,217) are positive.

## Upcoming events
IRDAI final rules (prob ~0.5 by December, -6 to +4%), Budget (2027-02-01), Q3 results (Feb 2027).

## Bull and bear
**Bull:** captive distribution, highest margin among large insurers, within IRDAI caps, lowest VNB downside.
**Bear:** one-channel dependence, margin mean reversion, regulatory surprise, equity-market sensitivity.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.