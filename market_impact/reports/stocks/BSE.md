# BSE — BSE Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.3%**, **12 months -1.6%** (rank 177 / 155 of 200 for 3m / 12m); beta 1.28
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.7%): 3 months 46%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -9.6% … P90 +4.8%; plausible 12m relative-return range incl. stock-specific noise: -46.9% … +26.0%
- Decomposition (12m): 0.5 × forward event exposure -1.9% (3m -1.7%; half assumed priced) + 0.5 × company-specific catalysts -0.3%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -1.7% (beta-adjusted) vs a realised market-adjusted move of -12.0% — gap +10.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

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
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.17 | +3.00 | +1.54 | -0.40 | +0.02 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -3.74 | -3.00 | -0.12 | -0.40 | -0.22 | +11.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.24 | +1.50 | +0.48 | +0.38 | -0.12 | +1.2% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.00 | +0.00 | -0.96 | -0.79 | -0.25 | -1.1% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.82 | +0.00 | -1.50 | -0.42 | +0.10 | +9.4% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.58 | +0.00 | -0.60 | -0.87 | -0.11 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.41 | +0.00 | -0.84 | -0.55 | -0.02 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -9.2% | -9.2% | -6.6 | -3.4 | +0.9 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -5.2% | -5.2% | -3.0 | -1.7 | -0.6 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.1% | +5.1% | +7.1 | +4.0 | -1.0 | +0.1 |
| SEBI partly reverses derivative expiry-settlement rule after closing-auction (CAS) volatility (`EV_SEBI_CAS_DERIV_REVERSAL`) | occurred | 1.00 | +4.9% | +4.9% | +5.0 | -0.1 | -0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.5% | -3.5% | -3.5 | +0.0 | +0.0 | -0.0 |
| SEBI tightens F&O further (weekly-expiry scrapping, higher margins/lot sizes) (`EV_SEBI_FNO_CURBS_RISK`) | risk_scenario | 0.20 | -16.5% | -3.3% | -17.0 | +0.4 | +0.1 | +0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -4.3% | -3.1% | -3.0 | -0.8 | -0.4 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -2.1 | -0.5 | +0.3 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +2.3% | +2.3% | +1.5 | +1.0 | -0.2 | +0.0 |
| Budget FY2027-28: LTCG/STT relief on listed equities (rate cut, exemption, or FPI-specific relief) (`EV_BUDGET_FY28_LTCG_RELIEF`) | scheduled | 0.35 | +6.4% | +2.2% | +6.3 | +0.1 | +0.0 | +0.0 |
| Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027 (`EV_FED_H1_2027_FURTHER_HIKES`) | anticipated | 0.40 | -4.7% | -1.9% | -3.0 | -1.2 | -0.5 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -0.7 | -1.0 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BSE | +7.50% | +3.75% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → BSE | +9.00% | +2.25% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → BSE | -3.00% | -2.16% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → BSE | +3.60% | +1.80% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → BSE | -9.00% | -1.80% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ P_SEBI_DERIVATIVES → BSE | -8.00% | -1.60% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → BSE | -3.00% | -1.20% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → BSE | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → BSE | -4.50% | -1.12% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ P_CAPITAL_GAINS_TAX → BSE | +3.00% | +1.05% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BSE | -2.00% | -1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BSE | -4.50% | -0.81% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BSE | -1.25% | -0.75% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_EQUITY_ACTIVITY_IN → BSE | +1.80% | +0.63% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BSE | +2.50% | +0.62% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FED_FUNDS → BSE | +1.62 | observed | -4.86% |
| 1 | F_FPI_FLOWS → BSE | -1.60 | events | -4.80% |
| 1 | P_SEBI_DERIVATIVES → BSE | -0.50 | events | +4.00% |
| 1 | F_GSEC_10Y_IN → BSE | +1.55 | director_override | -3.88% |
| 1 | F_EQUITY_ACTIVITY_IN → BSE | +0.20 | events | +1.80% |
| 1 | F_US_EQUITIES → BSE | +0.23 | observed | +0.35% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → BSE | +0.30 | events | +0.19% |
| 1 | F_RISK_SENTIMENT → BSE | +0.11 | observed | +0.11% |
| 2 | F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → BSE | +0.20 | events | -0.07% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → BSE | +0.30 | events | +0.06% |
| 3 | F_EQUITY_ACTIVITY_IN → P_CAPITAL_GAINS_TAX → F_DOMESTIC_FLOWS → BSE | +0.20 | events | -0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | SEBI outcome on CAS review / F&O settlement price methodology (consultation; panel view 2026-10-15) | regulatory | 0.60 | +1.0% | +0.60% |
| 2026-12 | Weekly expiry / contract-size rule changes by SEBI | regulatory | 0.15 | -9.0% | -1.35% |
| 2027-02-02 | Q3 FY27 results (inferred; Q2 on 2026-11-04) | results | 0.85 | +0.5% | +0.42% |

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