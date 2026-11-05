# KOTAKBANK — Kotak Mahindra Bank Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.8%**, **12 months -2.6%** (rank 127 / 136 of 200 for 3m / 12m); beta 0.83
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.6%): 3 months 47%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.8% … P90 +4.2%; plausible 12m relative-return range incl. stock-specific noise: -23.0% … +28.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.2 pp (model impact -0.5% beta-adjusted vs realised market-adjusted move +19.8%); forward event exposure -3.1% (3m -0.6%; half assumed priced); company-specific events +0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.06 | -7.00 | +0.00 | -0.04 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.83 | +0.00 | +3.28 | +3.00 | -0.45 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.83 | +3.00 | +2.31 | -0.37 | -0.11 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +4.46 | +0.00 | +2.40 | +2.65 | -0.59 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.58 | -2.00 | -1.74 | +0.14 | +0.02 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.55 | +0.00 | +1.04 | +2.09 | +0.42 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.13 | +0.00 | +1.08 | +1.92 | +0.14 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.77 | -2.20 | -0.35 | -0.22 | +0.00 | +3.5% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.65 | +0.00 | +1.20 | +1.73 | -0.28 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.60 | +0.00 | +0.24 | +1.45 | +0.91 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.56 | -1.50 | -0.80 | -0.14 | -0.12 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | +2.37 | +3.00 | -0.39 | -0.31 | +0.08 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.35 | +0.00 | -0.70 | -0.97 | -0.67 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.33 | +0.00 | -0.88 | -0.83 | -0.62 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.7% | -8.7% | +0.0 | -4.4 | -2.7 | -1.7 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.1% | -5.1% | -4.8 | -0.4 | +0.1 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.5% | -4.5% | +0.0 | -1.3 | -2.6 | -0.5 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -6.8% | -4.2% | -7.0 | +0.2 | -0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -12.5% | -3.5% | -8.8 | -3.1 | -0.8 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.7% | +2.9% | +5.4 | +0.5 | -0.1 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -15.2% | -2.7% | -11.0 | -3.9 | -0.5 | +0.2 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.9% | +2.6% | +0.0 | +1.0 | +2.1 | +0.8 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -7.0% | -2.5% | -2.6 | -2.1 | -1.4 | -0.8 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.5% | +2.5% | +1.5 | +1.2 | -0.1 | -0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.4% | +2.4% | -0.1 | +1.0 | +1.4 | +0.3 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.5% | +2.3% | +0.0 | +0.9 | +1.5 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → KOTAKBANK | -3.96% | -3.96% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → KOTAKBANK | -8.80% | -2.46% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → KOTAKBANK | +4.50% | +2.25% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → KOTAKBANK | -3.50% | -2.17% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → KOTAKBANK | -11.00% | -1.98% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → KOTAKBANK | -1.78% | -1.78% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → KOTAKBANK | +1.50% | +1.50% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → KOTAKBANK | +1.32% | +1.32% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_ASSET_QUALITY_IN → KOTAKBANK | -1.25% | -1.25% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → KOTAKBANK | -2.00% | -1.24% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → KOTAKBANK | -1.07% | -1.07% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → KOTAKBANK | -1.06% | -1.06% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_GDP_IN → KOTAKBANK | -1.01% | -1.01% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → KOTAKBANK | +1.00% | +1.00% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → KOTAKBANK | -0.98% | -0.98% |

## Analyst profile (agent research, sourced)
# KOTAKBANK - Kotak Mahindra Bank (Nifty 50, private bank)

## Business
Kotak is a universal-bank-led financial group: a mid-large private bank (retail, SME, corporate, treasury) with fully owned or majority subsidiaries in vehicle finance, securities, investment banking, asset management and life/general insurance. Revenue Rs 73.5k cr TTM, net profit Rs 21.5k cr TTM; Q2 FY27 consolidated PAT Rs 5,645 cr (+26% y/y), standalone Rs 4,212 cr (+29%). Promoter holding ~25.9% (Uday Kotak), FIIs 24.65% (down from 26.4% in March), DIIs 38.5%.

## What moves the stock (ranked)
1. **Credit growth and funding cost (NIM)** - advances +24.7%, deposits +23.2% (5 Oct update). The debate is margin, not volume: management said FCNR(B) deposits will pressure Q3 margins while repo repricing and deployment help later (ET BFSI, 26 Oct).
2. **Asset quality / credit cost** - a +50bp credit cost shock is roughly a 10% hit to PBT, so this is the biggest downside lever (weight about -7% equity per SSU).
3. **Regulatory/idiosyncratic governance** - the April 2024 RBI restriction episode (model knowledge) shows how fast a one-notch tightening can cut 5-10%; the CEO transition to Anup Saha (RBI-approved 30 Sep 2026) removed an overhang but adds execution uncertainty.
4. **Foreign flows and risk sentiment** - high FII ownership makes the stock sensitive to FPI flows (+1.8 per +US$5bn/qtr) and VIX spikes.
5. **Macro growth** - GDP forecast raised to 7.1% by RBI on 7 Oct; each +1pp GDP is worth about +3%.

## Transmission examples
- **Middle East escalation -> Brent up -> inflation and rupee pressure -> RBI stays hawkish (already hiked 7 Oct to 5.50%) -> deposit rates rise faster than EBLR loan resets -> NIM compresses and P/B de-rates.** Counter-effect: higher repo lifts EBLR yields on about 35-40% of the book within a quarter, so first-order NIM is mildly positive; the 3rd-order effect (slower housing/auto demand and higher stress in unsecured loans) dominates after 2-3 quarters.
- **US yields up (10y at 4.89%) -> FPI outflow from Indian financials -> Kotak (24.65% FII) underperforms -> FCNR(B) inflows become harder to roll (the US$133bn system build-up was driven by RBI's swap window, closed 31 Aug) -> banks must replace swap-supported deposits -> funding cost up -> NIM down (4th order).**
- **Strong monsoon/food disinflation -> RBI pause -> yields fall -> AFS gains and lower deposit cost -> NIM recovery; unsecured stress eases -> credit cost down.**

## Current situation
Stock +18.5% over 3m and at 52-week high on loan growth, brokerage upgrades (HSBC buy, Goldman, Citi), and CEO clarity. Q2 beat on asset quality. Valuation P/E 21.9 is the highest among large banks ex-HDFC/ICICI, leaving less room for FCNR-led margin disappointments.

## Upcoming
Q3 FY27 results in late January 2027; RBI MPC early December; CEO transition and first strategy signals; possible further FCNR pressure.

## Bull / bear
Bull: NIM trough in Q3, loan growth 20%+, credit cost below 0.6%, new CEO unlocks subsidiaries, FPI return. Bear: FCNR refinancing and rising deposit costs squeeze NIM below 4.2%, unsecured/commercial vehicle stress, regulatory surprise, valuation compression after the 3m rally.

Uncertainty: segment shares, EBLR share and unsecured share are model knowledge and marked low confidence; Q2 headline numbers come from news headlines (Hindu, Business Standard), not the filing.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.