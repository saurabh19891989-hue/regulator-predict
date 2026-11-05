# US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`)
*global_macro · status occurred · date 2026-09-23 · P(3m) 1 · P(12m) 1 · confidence medium*

10y briefly rose above 5.05%, a 19-year high (ET/CNBC 23 Sep), driven by oil-led inflation (CPI 3.7% in Sept), Fed hikes and deficit/term-premium worries; 30y hit highest since 2004 (24 Sep). By 5 Nov the 10y was ~4.89% (factor_state.md). French 10y near 5% too (9 Oct).

**Already moved:** US 10y: 4.47% (1 Jun) -> ~5.05% peak (23 Sep) -> 4.89% (5 Nov). DXY 101.4, +2.2% since 1 Jun. India: FPI outflow CY26 ~Rs 3.1 trn; USD/INR touched ~96+ then 94.49.

## Entry shocks (conditional on the event)
- `F_US_10Y` US 10-year Treasury yield: 1.7 SSU (range 1.4…2.4) net +42 bp since 1 Jun (peak +58 bp)
- `F_DXY` US dollar index: 0.73 SSU (range 0.5…1.0) +2.2% since 1 Jun

## Causal chains (agent)
- order 2: EV_UST_SELLOFF_SEP26 → F_US_10Y → F_FPI_FLOWS — yield gap vs India shrinks; EM equity/debt funds sell
- order 3: EV_UST_SELLOFF_SEP26 → F_FPI_FLOWS → F_USDINR → F_GSEC_10Y_IN — outflows weaken rupee and lift G-sec yields
- order 4: EV_UST_SELLOFF_SEP26 → F_US_10Y → F_US_EQUITIES → F_RISK_SENTIMENT → F_FPI_FLOWS — valuation hit to US equities raises VIX, amplifying EM outflows

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| TMPV | +1.3 | +0.0 | +0.9 | +0.5 | +0.0 |
| JSWSTEEL | +1.2 | +0.0 | +0.4 | +0.7 | +0.1 |
| SAIL | +1.2 | +0.0 | +0.2 | +0.7 | +0.3 |
| ONGC | +0.8 | +0.0 | +0.5 | +0.4 | -0.1 |
| OIL | +0.8 | +0.0 | +0.5 | +0.4 | -0.1 |
| MANKIND | +0.8 | +1.1 | -0.3 | +0.1 | +0.0 |
| NMDC | +0.7 | +0.0 | +0.3 | +0.3 | +0.0 |
| DRREDDY | +0.5 | +0.0 | +0.2 | +0.4 | -0.0 |
| PREMIERENE | +0.5 | +0.0 | -0.1 | +0.6 | +0.0 |
| PIIND | +0.5 | +0.0 | +0.3 | +0.1 | -0.0 |
| SRF | +0.4 | +0.0 | +0.3 | +0.1 | -0.0 |
| TATASTEEL | +0.4 | +0.0 | -0.2 | +0.5 | +0.1 |
| JINDALSTEL | +0.4 | +0.0 | -0.5 | +0.6 | +0.3 |
| LTM | +0.4 | +0.7 | -0.5 | +0.2 | +0.0 |
| LUPIN | +0.4 | +0.0 | -0.0 | +0.4 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -5.8 | +0.0 | -4.7 | -1.5 | +0.4 |
| BSE | -4.9 | +0.0 | -3.5 | -2.0 | +0.6 |
| YESBANK | -4.7 | +0.0 | -3.4 | -0.6 | -0.7 |
| MUTHOOTFIN | -4.6 | +0.0 | -4.2 | -0.3 | -0.1 |
| GROWW | -4.3 | +0.0 | -3.0 | -1.8 | +0.5 |
| NYKAA | -4.1 | -2.5 | -1.4 | -0.2 | +0.0 |
| SHRIRAMFIN | -4.1 | -2.0 | -1.6 | -0.3 | -0.2 |
| INDUSINDBK | -3.9 | -1.4 | -2.5 | -0.0 | -0.0 |
| BAJFINANCE | -3.9 | +0.0 | -2.7 | -0.8 | -0.4 |
| SBIN | -3.9 | +0.0 | -3.5 | -0.2 | -0.2 |
| ICICIAMC | -3.8 | +0.0 | -3.7 | -0.4 | +0.2 |
| TATACAP | -3.7 | +0.0 | -2.4 | -0.8 | -0.5 |
| JIOFIN | -3.7 | +0.0 | -3.0 | -0.5 | -0.3 |
| INDIGO | -3.5 | -1.2 | -1.9 | -0.4 | -0.0 |
| ADANIENSOL | -3.5 | +0.0 | -2.9 | -0.5 | -0.1 |

Share of absolute impact by order: 1: 7%, 2: 73%, 3: 16%, 4: 5%

## Sources
- 2026-09-23 10-year Treasury yield rockets to 19-year high - CNBC https://news.google.com/rss/search?q=10-year%20Treasury%20yield%20rockets%20to%2019-year%20high&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-24 US 30-Year Yield Hits Highest Since 2004 as Bond Selloff Deepens - Bloomberg https://news.google.com/rss/search?q=US%2030-Year%20Yield%20Hits%20Highest%20Since%202004%20as%20Bond%20Selloff%20Deepens%20-%20Bloomberg&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-04 Treasury Yields Fall as Democrats Sweep Congress - TradingView https://news.google.com/rss/search?q=Treasury%20Yields%20Fall%20as%20Democrats%20Sweep%20Congress%20-%20TradingView&hl=en-IN&gl=IN&ceid=IN:en