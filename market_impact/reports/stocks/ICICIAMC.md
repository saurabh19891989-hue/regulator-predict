# ICICIAMC — ICICI Prudential Asset Management Company Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.7%**, **12 months -6.1%** (rank 168 / 170 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.5%): 3 months 43%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -21.7% … P90 +3.1%; plausible 12m relative-return range incl. stock-specific noise: -29.6% … +36.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -3.6% beta-adjusted vs realised market-adjusted move -16.4%); forward event exposure -7.5% (3m -1.5%; half assumed priced); company-specific events -2.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +7.48 | +6.00 | +1.36 | +0.20 | -0.08 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -6.64 | -5.00 | -1.40 | -0.25 | +0.01 | — |
| SEBI mutual fund fee / TER / brokerage regulation (`NEW_SEBI_MF_FEE_REG`) | -5bp on active-equity gross fee yield | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -5.75 | -4.00 | -1.06 | -0.62 | -0.07 | +3.5% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.94 | +4.50 | +0.52 | -0.11 | +0.02 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -4.60 | +0.00 | -1.60 | -1.94 | -1.06 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.21 | +0.00 | -1.28 | -1.65 | -1.28 | — |
| US growth (`F_US_GDP`) | +1 pp | +3.99 | +0.00 | +1.92 | +1.92 | +0.14 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +3.73 | +0.00 | +2.68 | +0.73 | +0.32 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.37 | +1.00 | +1.68 | +0.58 | +0.11 | +1.2% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.25 | +3.00 | +0.37 | -0.04 | -0.08 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +2.77 | +2.50 | +0.36 | -0.07 | -0.02 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.74 | +0.00 | -1.98 | -0.70 | -0.05 | +2.2% |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +2.58 | +3.00 | -0.30 | -0.12 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -13.2% | -13.2% | +0.0 | -6.4 | -4.7 | -2.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -12.5% | -12.5% | -11.5 | -1.2 | +0.2 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -26.0% | -7.3% | -19.0 | -5.5 | -1.9 | +0.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +14.0% | +7.0% | +12.8 | +1.4 | -0.3 | +0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -31.2% | -5.6% | -21.5 | -8.5 | -1.7 | +0.5 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +4.9% | +4.9% | +0.0 | +2.2 | +2.0 | +0.7 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -11.9% | -4.3% | -4.8 | -3.5 | -2.6 | -1.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.8% | -3.8% | +0.0 | -3.7 | -0.4 | +0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.5% | -3.5% | +0.0 | -3.4 | -0.3 | +0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.9% | +3.4% | +2.0 | +1.9 | +1.4 | +0.6 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -3.3% | -3.3% | +0.0 | -2.1 | -0.9 | -0.3 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -11.8% | -3.0% | -3.0 | -8.4 | +0.3 | -0.8 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → ICICIAMC | -9.90% | -9.90% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ICICIAMC | +11.25% | +5.62% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ICICIAMC | -16.00% | -4.48% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ICICIAMC | -20.00% | -3.60% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → ICICIAMC | -2.67% | -2.67% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → ICICIAMC | +2.25% | +2.25% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → ICICIAMC | -2.11% | -2.11% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → ICICIAMC | -1.92% | -1.92% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → ICICIAMC | -1.78% | -1.78% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → ICICIAMC | -4.80% | -1.71% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_RISK_SENTIMENT → ICICIAMC | -1.60% | -1.60% |
| 3 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_US_EQUITIES → F_RISK_SENTIMENT → ICICIAMC | +1.56% | +1.56% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → ICICIAMC | -1.53% | -1.53% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → ICICIAMC | +1.50% | +1.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ICICIAMC | -6.75% | -1.49% |

## Analyst profile (agent research, sourced)
# ICICIAMC - ICICI Prudential Asset Management Company Ltd. (as of 2026-11-05)

## Business
ICICI Prudential AMC manages the ICICI Prudential Mutual Fund (equity, hybrid, debt, passive), plus PMS, AIFs and offshore advisory. As a fee business on assets it earns ~73% operating margins; revenue is a function of average AUM and the mix toward equity (higher fee). The company was listed recently, and ICICI Bank (~51%, model knowledge) and Prudential plc (~34.6%) are the promoter group, now 85.60% after Prudential plc sold up to 2% (about Rs3,190cr) via a block on 2026-08-26, which knocked the stock down 5%. Q2 FY27 PAT was Rs889cr (+6.1%); the interim dividend is Rs30 per share.

## What moves the stock (ranked)
1. **Equity market level and flows (FPI +4.5, retail activity +3.0, VIX -4.0)**: AUM and fees move one-for-one with the market and the stock trades at ~50x earnings, so multiple sensitivity doubles the effect.
2. **Structural financialisation (+6.0) and GDP (+3.0)**: the long-run growth leg.
3. **Domestic SIP flows (+2.5)**: stable monthly flows underpin AUM in downturns.
4. **Regulation: SEBI fee regime (-6.0)** and **capital-gains tax (-5.0)**: the main policy tails.
5. **Promoter sell-down overhang** (event), **rates and valuation (repo -0.8, G-sec -1.0)**.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker -> FPI outflow -> Nifty -5%**: equity AUM -5% -> revenue -3.8% -> PAT -5% (73% OPM so near full drop-through) -> 50x P/E de-rates by ~10% as growth expectations fall -> total -10 to -12. 4th order: SIP stoppage/redemptions accelerate if drawdown lasts, reducing the next 12 months' flows.
- **RBI hike -> higher debt-fund yields -> money-market inflows** (+0.4) but equity multiples compress (-1.2): near-zero net.
- **SEBI cuts TER by 5bp -> blended revenue yield -11% -> partly offset by lower distributor commissions and volumes** (-6 central).
- **Budget raises LTCG tax** -> equity MF inflows -5%, sentiment, multiple -1x -> -5.

## Current situation
Stock 52-week range Rs2,529-3,611; last Rs2,963, -10% in 6m. Sep-2026 shareholding: promoters 85.60%, FIIs 3.26%, DIIs 8.41% (DII buying the block). The Q2 print was a beat per brokers, with up to 25% upside targeted by Motilal Oswal (NDTV Profit, 2026-10-13).

## Upcoming
Q3 FY27 results mid-January 2027; Budget Feb 2027; SEBI consultations on fees; possible further stake sales by Prudential plc; lock-in expiries of pre-IPO holders (model knowledge, verify).

## Bull case
Market recovers, SIP flows rise, equity share gains: AUM +20%, PAT growth 15-20%, premium multiple preserved (+20%).
## Bear case
Equity drawdown, SEBI fee cut and a tax hit with continuing sell-down: -25% to -30%.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.