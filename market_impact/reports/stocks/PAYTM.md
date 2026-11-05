# PAYTM — One 97 Communications Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +2.5%**, **12 months +2.1%** (rank 5 / 30 of 200 for 3m / 12m); beta 0.88
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +32.5%): 3 months 56%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.2% … P90 +9.0%; plausible 12m relative-return range incl. stock-specific noise: -45.0% … +47.3%
- Decomposition (12m): 0.5 × forward event exposure +1.2% (3m +1.8%; half assumed priced) + 0.5 × company-specific catalysts +3.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.3% (beta-adjusted) vs a realised market-adjusted move of +60.0% — gap -63.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| UPI merchant discount rate / incentive policy (`NEW_UPI_MDR`) | +1 = MDR or take-rate introduced on UPI merchant payments (~+5bp) | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.99 | +5.00 | +0.00 | -0.01 | -0.00 | — |
| Digital payments / UPI disruption of incumbents (`T_DIGITAL_PAYMENTS`) | +1 | +4.00 | +4.00 | +0.00 | +0.02 | -0.02 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.62 | -2.00 | -1.15 | -0.47 | -0.00 | +3.5% |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.13 | -3.00 | -0.14 | +0.02 | -0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.88 | +2.50 | +0.00 | +0.44 | -0.06 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.68 | +0.00 | +2.34 | +0.28 | +0.06 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.66 | -2.50 | -0.12 | +0.02 | -0.07 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.42 | +0.00 | -0.80 | -1.18 | -0.44 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.36 | +0.00 | -0.64 | -0.95 | -0.77 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.36 | +0.00 | +2.00 | +0.22 | +0.14 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.96 | +0.00 | +0.40 | +1.42 | +0.14 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.82 | +1.00 | +0.80 | +0.02 | +0.00 | +1.2% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.80 | +0.00 | -1.80 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -11.0% | -11.0% | -11.0 | +0.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +13.4% | +6.7% | +13.3 | +0.1 | -0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -13.4% | -3.3% | -8.0 | -5.2 | -0.3 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.0 | -0.0 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -13.2% | -2.0% | -6.5 | -7.1 | +0.3 | +0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.0% | +2.0% | +0.0 | +1.4 | +0.4 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -0.5 | -0.9 | -0.5 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.7% | +1.7% | +0.5 | +1.2 | +0.1 | +0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.0 | -0.7 | -0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -6.6% | -1.7% | -3.0 | -4.1 | +1.0 | -0.5 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.9% | +1.6% | +0.8 | +1.2 | +0.8 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -6.2% | -1.5% | -2.0 | -2.4 | -1.8 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PAYTM | +12.50% | +6.25% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → PAYTM | -7.50% | -1.35% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → PAYTM | -5.00% | -1.25% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → PAYTM | +2.50% | +0.88% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → PAYTM | -0.90% | -0.81% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → PAYTM | +1.00% | +0.80% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → PAYTM | -3.00% | -0.75% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → PAYTM | -3.00% | -0.75% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → PAYTM | -5.00% | -0.75% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → PAYTM | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → PAYTM | -2.40% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PAYTM | -2.33% | -0.58% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ NEW_USDJPY → F_FPI_FLOWS → PAYTM | -3.60% | -0.54% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → PAYTM | -2.00% | -0.50% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → PAYTM | +0.80% | +0.50% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → PAYTM | -1.60 | events | -8.00% |
| 1 | F_REPO_IN → PAYTM | +1.00 | events | +0.80% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → PAYTM | -1.56 | events | -0.62% |
| 1 | T_GENAI_SERVICES → PAYTM | +0.50 | director_override | +0.50% |
| 1 | F_URBAN_DEMAND → PAYTM | +0.20 | events | +0.50% |
| 1 | F_COAL_INTL → PAYTM | +0.70 | director_override | +0.35% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → PAYTM | +1.15 | events | -0.35% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → PAYTM | +0.50 | events | +0.26% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → PAYTM | +0.50 | events | -0.24% |
| 1 | F_US_EQUITIES → PAYTM | +0.23 | observed | +0.23% |
| 1 | F_RISK_SENTIMENT → PAYTM | +0.11 | observed | -0.22% |
| 2 | F_GDP_IN → F_UNSECURED_STRESS → PAYTM | +0.50 | events | +0.20% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Investor meetings across four cities (announced 2026-11-03) | other | 0.90 | +0.5% | +0.45% |
| 2026-12-31 | NPCI 30% UPI market-share cap deadline for third-party apps (extension to date repeatedly deferred; no later change found) | regulatory | 0.60 | +4.0% | +2.40% |
| 2027 | Policy change on UPI MDR/incentives for merchant payments | regulatory | 0.10 | +9.5% | +0.95% |
| 2027-01 | Q3 FY27 results (date approximate; Q2 on 2026-10-26) | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# PAYTM - One 97 Communications (as of 2026-11-05)

## Business
Paytm earns from payment services (merchant acquiring, soundbox/POS device rentals, subscriptions), financial-services distribution (loans, insurance, wealth through partners) and marketing/cloud. It cannot use its own payments bank for UPI since the 2024 RBI curbs. Q2 FY27: revenue Rs2,648cr (+28.5% YoY), consolidated PAT ~Rs225cr vs Rs21cr (Free Press Journal, Inc42, 2026-10-26; the screener standalone row shows Rs169cr). Q1 FY27 GMV Rs7.1 lakh cr (+31%). The stock is Rs1,797 (+50% in 6m) at ~8.5x book.

## What moves the stock (ranked)
1. **Regulation/policy (NEW_UPI_MDR +6.0, RBI prudential -3.0).** UPI is zero-MDR; any take-rate or incentive is a large lever, and regulatory risk (PA/wallet/lending directions) is the main tail.
2. **Digital-payments adoption (+4.0)** and **urban consumption (+2.5).**
3. **Flows/sentiment: FPI (+5.0), VIX (-2.0), US equities (+1.0).**
4. **Credit distribution: unsecured stress (-2.5), credit growth (+1.5).**
5. **Rates/cash yield (+0.8)**, AI cost savings (+1.0).
Pack empirics: coal (+8.84, t 2.5; beta only 0.44) has no mechanism; shrunk to +0.5.

## Transmission examples
- **RBI/NPCI action on UPI share cap (deadline 2026-12-31) -> PhonePe/Google Pay must stop onboarding -> Paytm UPI share rises ~1-2pp -> QR/soundbox attach increases -> payment revenue +, EBITDA +; 4th order, partner banks gain more P2M volume.**
- **Middle East escalation -> Brent +10% -> CPI +0.25pp -> RBI 'calibrated tightening' (hiked 2026-10-07) -> consumer credit slows -> loan distribution (22% of revenue) slows and unsecured delinquencies rise -> partner banks cut small-ticket disbursals -> Paytm financial-services revenue -> EBITDA -10%.**
- **Equity rally (FPI inflow) -> high-beta growth names re-rate (Morgan Stanley upgrade 2026-10-28) -> equity currency for ESOP and M&A.**
- **Government introduces UPI MDR (low odds 10%) -> merchant take-rate 5bp -> +Rs140cr post-tax -> +6%.**

## Current situation
Strong profitability trajectory with growth ~28%. Brokers raised targets (Emkay Rs2,300; ICICI Sec Rs1,945). Stake in Little Internet raised to 77.42% (2026-09-25). Management plans investor meetings in four cities (2026-11-03).

## Upcoming events
UPI cap deadline 2026-12-31, Q3 results (~Jan 2027), Budget (2027-02-01), MDR policy (prob 0.1).

## Bull and bear
**Bull:** operating leverage (PAT x10), take-rate optionality, upgrade cycle.
**Bear:** P/B 8.5, regulatory shock risk, zero-MDR economics, rival scale.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.