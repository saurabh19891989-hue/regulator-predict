# KOTAKBANK — Kotak Mahindra Bank Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.8%**, **12 months +0.7%** (rank 21 / 52 of 200 for 3m / 12m); beta 0.83
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.6%): 3 months 53%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.9% … P90 +4.9%; plausible 12m relative-return range incl. stock-specific noise: -24.1% … +24.4%
- Decomposition (12m): 0.5 × forward event exposure +0.9% (3m +0.9%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.1% (beta-adjusted) vs a realised market-adjusted move of +19.8% — gap -19.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.21 | +0.21 | -0.06 |
| Regulatory | -0.34 | -0.06 | -0.41 | -0.05 |
| Sector | -0.69 | +1.76 | +1.07 | +0.75 |
| Theme | +0.00 | +0.13 | +0.13 | +0.08 |
| Geopolitics | +0.00 | -0.06 | -0.06 | -0.05 |
| Company catalysts | +0.40 | +0.00 | +0.40 | +0.40 |
| Market-priced macro | -0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.47 | -0.21 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.72** | **+0.76** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.06 | -7.00 | +0.00 | -0.04 | -0.02 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.87 | +3.00 | +2.11 | -0.15 | -0.09 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.56 | +0.00 | +3.28 | +1.38 | -0.11 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.58 | -2.00 | -1.74 | +0.14 | +0.02 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.44 | +0.00 | +2.40 | +1.21 | -0.17 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.75 | -2.20 | -0.35 | -0.21 | +0.01 | +3.5% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.73 | +0.00 | +1.04 | +1.35 | +0.34 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.54 | -1.50 | -0.80 | -0.14 | -0.11 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | +2.36 | +3.00 | -0.39 | -0.31 | +0.06 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.29 | +0.00 | +1.08 | +1.07 | +0.14 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.93 | +0.00 | +1.20 | +0.79 | -0.06 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.92 | +1.80 | +0.18 | -0.04 | -0.02 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.92 | +0.00 | +0.24 | +1.24 | +0.44 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.84 | +0.00 | -0.70 | -0.82 | -0.31 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.2% | -4.2% | -4.0 | -0.4 | +0.1 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -1.3 | -1.7 | -0.4 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.7% | +2.8% | +5.4 | +0.5 | -0.1 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.5% | +2.5% | +1.5 | +1.1 | -0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.4% | -2.1% | -5.5 | -2.6 | -0.4 | +0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.8% | +1.9% | +0.0 | +1.0 | +1.4 | +0.4 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.1% | -1.8% | -2.1 | +0.1 | -0.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.0 | -0.3 | -0.1 | -0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.0 | -0.4 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.4% | +1.3% | +0.9 | +1.0 | +0.4 | +0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -8.6% | -1.3% | -5.5 | -3.0 | -0.2 | +0.1 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +1.5% | +1.2% | +0.0 | +0.5 | +0.7 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → KOTAKBANK | +4.50% | +2.25% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → KOTAKBANK | -5.50% | -1.38% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → KOTAKBANK | -1.05% | -0.95% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → KOTAKBANK | -5.50% | -0.82% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → KOTAKBANK | -2.20% | -0.55% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → KOTAKBANK | +0.88% | +0.55% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → KOTAKBANK | +0.80% | +0.54% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → KOTAKBANK | -4.50% | -0.54% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → KOTAKBANK | -0.60% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → KOTAKBANK | -2.70% | -0.49% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → KOTAKBANK | +0.88% | +0.48% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → KOTAKBANK | +0.60% | +0.48% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → KOTAKBANK | +0.88% | +0.44% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → KOTAKBANK | -1.73% | -0.43% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → KOTAKBANK | -1.73% | -0.43% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → KOTAKBANK | -1.60 | events | -2.88% |
| 1 | F_GDP_IN → KOTAKBANK | +0.50 | events | +1.50% |
| 1 | F_GSEC_10Y_IN → KOTAKBANK | +1.55 | director_override | -1.08% |
| 1 | F_REPO_IN → KOTAKBANK | +1.00 | events | +1.00% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → KOTAKBANK | +0.50 | events | +0.56% |
| 1 | F_FED_FUNDS → KOTAKBANK | +1.62 | observed | -0.49% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → KOTAKBANK | -1.56 | events | -0.37% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → KOTAKBANK | +1.00 | events | -0.35% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → KOTAKBANK | -0.25 | events | -0.28% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → KOTAKBANK | +1.00 | events | -0.28% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → KOTAKBANK | +0.50 | events | +0.26% |
| 1 | F_RISK_SENTIMENT → KOTAKBANK | +0.11 | observed | -0.25% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Anup Saha assumes office as MD & CEO (effective date unverified); first strategy communication | other | 0.80 | +1.0% | +0.80% |
| 2027-01 | Q3 FY27 results (date unconfirmed; Q2 was 24 Oct 2026); NIM guided to see FCNR pressure | results | 0.95 | +0.0% | +0.00% |

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