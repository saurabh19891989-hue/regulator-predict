# ICICIBANK — ICICI Bank Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.2%**, **12 months -5.1%** (rank 158 / 164 of 200 for 3m / 12m); beta 0.97
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +13.6%): 3 months 37%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.8% … P90 -0.7%; plausible 12m relative-return range incl. stock-specific noise: -20.2% … +8.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.8 pp (model impact -1.6% beta-adjusted vs realised market-adjusted move +15.0%); forward event exposure -7.0% (3m -2.7%; half assumed priced); company-specific events +0.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -4.25 | -4.20 | +0.00 | -0.03 | -0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.44 | +0.00 | -1.00 | -1.30 | -1.14 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.32 | +0.00 | +2.40 | +1.50 | -0.58 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.29 | +0.00 | -1.44 | -1.78 | -0.07 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.09 | +2.50 | +1.15 | -0.46 | -0.09 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.80 | -2.00 | -0.45 | -0.28 | -0.07 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.59 | -1.20 | -0.47 | -0.54 | -0.39 | -1.1% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.53 | +0.00 | +0.79 | +1.23 | +0.50 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.51 | +0.00 | +1.92 | +1.25 | -0.66 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -2.42 | -1.50 | -1.10 | +0.15 | +0.02 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.29 | +0.00 | -0.80 | -0.93 | -0.56 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.27 | +0.00 | +1.60 | +0.54 | +0.13 | +1.2% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.26 | +2.00 | +0.16 | +0.03 | +0.08 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.06 | +0.00 | +0.00 | -0.97 | -1.09 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.6% | -8.6% | -1.5 | -3.2 | -2.4 | -1.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.8% | -5.8% | -5.2 | -0.4 | -0.1 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.1% | -4.1% | +0.0 | -1.7 | -2.2 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -12.6% | -3.5% | -8.0 | -3.7 | -0.9 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.5% | +3.3% | +5.8 | +0.4 | +0.1 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -1.0 | -1.6 | -0.6 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -15.3% | -2.8% | -10.0 | -4.6 | -0.6 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -4.4% | -2.7% | -4.6 | +0.2 | +0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -7.0% | -2.5% | -3.1 | -1.7 | -1.3 | -0.8 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -2.1 | -0.1 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.4% | -2.4% | -2.0 | -0.1 | -0.2 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.9 | -0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ICICIBANK | +5.00% | +2.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ICICIBANK | -8.00% | -2.24% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ICICIBANK | -10.00% | -1.80% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → ICICIBANK | -2.10% | -1.30% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → ICICIBANK | -1.50% | -0.93% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → ICICIBANK | -2.40% | -0.86% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → ICICIBANK | -2.88% | -0.72% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ICICIBANK | -3.00% | -0.66% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → ICICIBANK | +0.72% | +0.65% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_CREDIT_GROWTH_IN → ICICIBANK | -1.00% | -0.62% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → ICICIBANK | +1.00% | +0.58% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → ICICIBANK | -0.90% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ICICIBANK | -1.92% | -0.54% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → ICICIBANK | +0.80% | +0.50% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ICICIBANK | -1.92% | -0.48% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ICICIBANK | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → ICICIBANK | +1.70 | events | -2.04% |
| 1 | F_GDP_IN → ICICIBANK | +0.50 | events | +1.25% |
| 1 | F_LIQUIDITY_IN → ICICIBANK | -0.90 | events | -0.54% |
| 1 | F_REPO_IN → ICICIBANK | +1.00 | events | -0.50% |
| 1 | F_USDINR → ICICIBANK | -0.37 | observed | +0.44% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → ICICIBANK | +0.50 | events | +0.34% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → ICICIBANK | +1.00 | events | -0.23% |
| 1 | F_RISK_SENTIMENT → ICICIBANK | +0.11 | observed | -0.22% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → ICICIBANK | -1.56 | events | -0.20% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → ICICIBANK | +0.50 | events | +0.17% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → ICICIBANK | -0.25 | events | -0.17% |

## Analyst profile (agent research, sourced)
# ICICIBANK - ICICI Bank Ltd. (as of 2026-11-05)

## Business
ICICI Bank is a large private-sector universal bank: retail and SME lending (home, auto, personal, cards, business banking), corporate lending, a large low-cost deposit franchise, and treasury. It owns ~51% of ICICI Prudential Life, ICICI Lombard (51.3%) and ICICI Prudential AMC (~51%, model knowledge), which together are ~12-15% of its market value. Q2 FY27 profit was Rs14,843cr (+20%), NII +18%, NIM ~12bp lower YoY, provisions down (Fortune India/Business Standard, 2026-10-17). Note: the evidence pack has no screener fundamentals, so balance-sheet numbers (loan book ~Rs14 lakh cr, ROE ~17%) are model estimates to be verified.

## What moves the stock (ranked)
1. **Credit cost / asset quality** (-4.2 per +50bp): the largest swing factor; ICICI sits at a cyclical low in credit cost so the distribution is skewed negative.
2. **Credit growth and GDP** (+2.0 / +2.5): RBI itself expects credit growth to moderate from 18-19% after the hike.
3. **FPI flows and risk sentiment** (+2.0 / -2.0): ICICI is a core FII holding and trades as the quality large-cap bank proxy.
4. **Deposits/funding and NIM** (+1.2, repo -0.5, G-sec -1.2): the hike lifts yields on EBLR loans quickly, deposits lag - a 2-3 quarter NIM tailwind that has to be weighed against valuation compression and MTM.
5. **Regulation (RBI prudential -1.5)** and **payments policy (UPI MDR +0.5)**.
6. Macro: INR (-1.2), Brent (-0.3), liquidity (+0.6).

## Transmission examples
- **Middle East escalation -> Brent up -> INR down -> RBI hawkish**: Brent +10% (to ~$105) widens the CAD, USD/INR +3% to ~97, CPI +0.4pp, RBI follows its October hike with another 25bp. Loan repricing lifts NIM briefly (+0.5), but FPIs sell (-2.0), G-sec yields +25bp (-1.2) and housing/auto demand slows -> loan growth -1pp in 6-9 months (-0.7). Net approx -3 to -4 over 3-12 months.
- **Rate hike -> bank FD rates up -> deposit mobilisation eases -> credit growth rebounds**: hike (+25bp) -> deposit rates +20-30bp -> system deposit growth +1pp over 6-9 months (+0.4) -> more lendable resources -> credit growth supported; 4th order: higher credit growth with unchanged spreads raises ICICI NII but also raises 2027-28 credit cost if underwriting loosens.
- **UPI MDR**: 0.4% MDR on merchant payments >Rs2,000 -> acquirers/sponsor banks gain fee pool -> fintech competition shifts (Paytm, PhonePe pay more) -> ICICI's merchant ecosystem (POS/QR) monetises; 4th order: smaller merchants shift to cash for smaller amounts, limiting volume.
- **Unsecured stress in NBFC/MFI** -> tighter RBI prudential norms -> higher risk weights on bank loans to NBFCs -> ICICI's wholesale growth slows (small).

## Current situation
Results beat on provisions, but margins are the debate; stock fell 1% on result day, then rallied 10% in a month to near its 52-week high of Rs1,480, helped by the 2026-11-05 jump of 3.5%. Peers: HDFC Bank Q2 net +5% (missed); IndusInd NIM hit 7-8bp from FCNR(B). RBI reversed course on 2026-10-07 (repo 5.50%).

## Upcoming
Q3 FY27 results ~mid-Jan 2027 (estimated); RBI MPC December 2026 and Feb 2027; any FCNR(B)/liquidity measures; subsidiary dividends.

## Bull case
Hike lifts NIM from Q3, credit cost stays <0.5%, loan growth 14-16%, UPI MDR monetises, subsidiaries re-rate - ROE >17% sustained, premium multiple expands.
## Bear case
Hawkish RBI plus INR slide keep FPIs selling; credit growth slows to 10-11%, retail unsecured cycle turns, NIM stays compressed on deposit competition; valuation de-rates from ~3x P/B.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.