# BSE — BSE Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.9%**, **12 months +0.7%** (rank 69 / 89 of 200 for 3m / 12m); beta 1.28
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.7%): 3 months 53%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.5% … P90 +10.6%; plausible 12m relative-return range incl. stock-specific noise: -41.5% … +33.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -8.7% beta-adjusted vs realised market-adjusted move -12.0%); forward event exposure +4.0% (3m +3.7%; half assumed priced); company-specific events -0.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| BSE share of index-options premium turnover vs NSE (`NEW_NSE_BSE_OPTIONS_SHARE`) | +5 pp BSE market share | +12.00 | +12.00 | +0.00 | +0.00 | +0.00 | — |
| SEBI F&O / market-structure tightening (`P_SEBI_DERIVATIVES`) | +1 = tightening step | -10.52 | -8.00 | -2.79 | +0.21 | +0.06 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -8.28 | -6.00 | -1.87 | -0.55 | +0.14 | — |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +7.58 | +9.00 | -1.32 | -0.10 | +0.00 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +6.75 | +4.00 | +2.48 | +0.51 | -0.25 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +4.27 | +3.50 | +1.08 | -0.30 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.19 | +3.00 | +1.54 | -0.40 | +0.04 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -3.72 | -3.00 | -0.12 | -0.37 | -0.24 | +11.2% |
| US dollar index (`F_DXY`) | +3% DXY | -2.81 | +0.00 | -1.32 | -1.48 | -0.01 | +2.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.65 | +0.00 | -0.96 | -1.50 | -0.18 | -1.1% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.53 | +1.50 | +0.24 | +0.63 | +0.16 | +1.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.51 | -2.50 | +0.00 | +0.00 | -0.01 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -2.26 | +0.00 | -1.50 | -0.79 | +0.04 | +9.4% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.22 | +0.00 | -0.60 | -1.44 | -0.18 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.3% | -10.3% | +0.0 | -1.3 | -4.9 | -4.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.9% | -8.9% | -6.2 | -3.5 | +0.9 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -5.9% | -5.9% | -3.0 | -1.8 | -1.2 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.2% | +5.1% | +7.1 | +4.0 | -1.0 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -4.9% | -4.9% | +0.0 | -3.5 | -2.0 | +0.6 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -4.4% | -4.4% | +0.0 | -3.2 | -1.8 | +0.6 |
| SEBI partly reverses derivative expiry-settlement rule after closing-auction (CAS) volatility (`EV_SEBI_CAS_DERIV_REVERSAL`) | anticipated | 0.85 | +4.9% | +4.2% | +5.0 | -0.1 | -0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.5% | -3.5% | -3.5 | +0.0 | +0.0 | -0.0 |
| SEBI tightens F&O further (weekly-expiry scrapping, higher margins/lot sizes) (`EV_SEBI_FNO_CURBS_RISK`) | risk_scenario | 0.20 | -16.5% | -3.3% | -17.0 | +0.4 | +0.1 | +0.0 |
| Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027 (`EV_FED_H1_2027_FURTHER_HIKES`) | anticipated | 0.30 | -10.7% | -3.2% | -6.0 | -2.8 | -2.0 | +0.1 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.58 | -4.7% | -2.7% | -3.0 | -1.0 | -0.7 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -0.7 | -1.7 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BSE | +7.50% | +3.75% |
| 1 | EV_SEBI_CAS_DERIV_REVERSAL ⇒ P_SEBI_DERIVATIVES → BSE | +3.20% | +2.72% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → BSE | +9.00% | +2.25% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → BSE | +3.60% | +1.80% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → BSE | -9.00% | -1.80% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → BSE | -6.00% | -1.80% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → BSE | -3.00% | -1.74% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ P_SEBI_DERIVATIVES → BSE | -8.00% | -1.60% |
| 1 | EV_SEBI_CAS_DERIV_REVERSAL ⇒ F_EQUITY_ACTIVITY_IN → BSE | +1.80% | +1.53% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → BSE | -4.50% | -1.26% |
| 1 | EV_FED_H1_2027_CUTS ⇒ F_FED_FUNDS → BSE | +4.50% | +1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → BSE | -4.50% | -1.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BSE | +4.00% | +1.12% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ P_CAPITAL_GAINS_TAX → BSE | +3.00% | +1.05% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BSE | -2.00% | -1.00% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FED_FUNDS → BSE | +1.62 | observed | -4.86% |
| 1 | F_FPI_FLOWS → BSE | -1.60 | events | -4.80% |
| 1 | F_GSEC_10Y_IN → BSE | +1.70 | events | -4.25% |
| 2 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → BSE | -1.60 | events | -2.30% |
| 1 | P_SEBI_DERIVATIVES → BSE | -0.10 | events | +0.80% |
| 1 | F_US_EQUITIES → BSE | +0.23 | observed | +0.35% |
| 2 | P_SEBI_DERIVATIVES → F_EQUITY_ACTIVITY_IN → BSE | -0.10 | events | +0.28% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → BSE | +0.30 | events | +0.19% |
| 3 | F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → BSE | -1.60 | events | +0.17% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → BSE | +0.30 | events | +0.13% |
| 1 | F_RISK_SENTIMENT → BSE | +0.11 | observed | +0.11% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_EQUITY_ACTIVITY_IN → BSE | +0.30 | events | +0.10% |

## Analyst profile (agent research, sourced)
# BSE - BSE Ltd. (Nifty 50 per pack, exchange operator) - as of 2026-11-05

## Business
Exchange operator whose earnings come mostly from transaction charges on index options (Sensex/Bankex) plus cash market, MF distribution (StAR MF), listing, data and index services. TTM revenue Rs5,444cr, EBITDA Rs3,576cr (66% margin), debt-free, P/E 53x, stock +53% in 12 months.

## What moves the stock, ranked
1. **SEBI derivatives policy** - closing auction session (CAS) chaos in August, review of F&O settlement price methodology, possible switch to last-30-minute VWAP. One tightening step ~ -8 (volume -10% => EBITDA -10%, persistence 0.75, plus de-rating); a favourable review is positive.
2. **Equity trading activity** - +20% traded value ~ +9 (revenue 70% transaction-linked, incremental margin 90%, EBITDA +19%, persistence 0.5).
3. **Market share vs NSE** - NSE listed on 2026-09-21; a +5pp BSE share gain in index options ~ +12 (new driver node proposed: NEW_NSE_BSE_OPTIONS_SHARE).
4. **Tax/STT policy** - Budget on 1 Feb; STT step ~ -6.
5. **Flows** - FPI/DII flows (+3 / +3.5), sentiment, Fed funds (empirical -5.88, t -1.9, shrunk to -3).
6. **Discount rate** - 53x P/E.

Empirical pack: no |t| >= 2; Fed funds t -1.9 and iron ore +3.08 (t 1.0) are noise-heavy.

## Transmission examples
- **Middle East escalation -> VIX up -> options volumes initially spike (positive) -> Brent up, INR weaker, FPIs sell -> Nifty falls 5% -> retail participation drops with a 2-month lag -> volumes -15% -> BSE EBITDA -15% -> stock -7%; 4th-order: SEBI tightens F&O further to protect retail losses -> -8.**
- **Retail losses in F&O (SEBI study 2026-08-11) -> SEBI tightens contract size or expiries -> volumes -10% -> BSE revenue -7%.**
- **Brokers (Groww, Angel One) rally on regulatory relief -> client activity rises -> BSE volumes up (same shock hits both).**

## Current situation
Q2 revenue +34% y/y but -8% q/q; PAT Rs773-809cr. Stock reacted +4% on the day after results; analysts divided on growth outlook. NSE IPO at Rs1,800 lists with +1.85% gain.

## Upcoming
SEBI CAS/settlement decision, Budget (1 Feb 2027), Q3 results early February.

## Bull / bear
Bull: favourable SEBI review, market-share gains, volume recovery, diversification. Bear: expiry/contract curbs, NSE competition, tax hike, de-rating of high-multiple stock.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.