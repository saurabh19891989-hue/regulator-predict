# US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`)
*global_macro · status occurred · date 2026-09-23 · P(3m) 1 · P(12m) 1 · confidence medium*

10y briefly rose above 5.05%, a 19-year high (ET/CNBC 23 Sep), driven by oil-led inflation (CPI 3.7% in Sept), Fed hikes and deficit/term-premium worries; 30y hit highest since 2004 (24 Sep). By 5 Nov the 10y was ~4.89% (factor_state.md). French 10y near 5% too (9 Oct).

**Review override applied:** Double count. US 10Y occurred-event shocks summed to +3.5 SSU (Fed hike 0.8 + selloff 1.7 + precious-metals 1.5 - 0.3 - 0.2) against +1.68 realised since 1 Jun. DXY summed to +1.83 against +0.73 realised. After this fix and the precious-metals fix: 10Y 0.8+1.2-0.3-0.2 = 1.5 SSU (realised 1.68); DXY 0.73 (realised 0.73).

**Already moved:** US 10y: 4.47% (1 Jun) -> ~5.05% peak (23 Sep) -> 4.89% (5 Nov). DXY 101.4, +2.2% since 1 Jun. India: FPI outflow CY26 ~Rs 3.1 trn; USD/INR touched ~96+ then 94.49.

## Entry shocks (conditional on the event)
- `F_US_10Y` US 10-year Treasury yield: 1.2 SSU (range 0.9…1.5) residual after +0.8 SSU booked in EV_FED_SEP26_HIKE
- `F_DXY` US dollar index: 0.33 SSU (range 0.2…0.5) residual after +0.4 booked in EV_FED_SEP26_HIKE

## Causal chains (agent)
- order 2: EV_UST_SELLOFF_SEP26 → F_US_10Y → F_FPI_FLOWS — yield gap vs India shrinks; EM equity/debt funds sell
- order 3: EV_UST_SELLOFF_SEP26 → F_FPI_FLOWS → F_USDINR → F_GSEC_10Y_IN — outflows weaken rupee and lift G-sec yields
- order 4: EV_UST_SELLOFF_SEP26 → F_US_10Y → F_US_EQUITIES → F_RISK_SENTIMENT → F_FPI_FLOWS — valuation hit to US equities raises VIX, amplifying EM outflows

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PREMIERENE | +0.4 | +0.0 | -0.0 | +0.4 | +0.0 |
| MANKIND | +0.4 | +0.5 | -0.2 | +0.0 | +0.0 |
| JSWSTEEL | +0.3 | +0.0 | +0.1 | +0.2 | +0.0 |
| TMPV | +0.3 | +0.0 | +0.3 | +0.1 | -0.0 |
| COCHINSHIP | +0.3 | +0.0 | +0.1 | +0.3 | -0.0 |
| LTM | +0.3 | +0.5 | -0.4 | +0.2 | +0.1 |
| ONGC | +0.3 | +0.0 | +0.2 | +0.2 | -0.1 |
| OIL | +0.3 | +0.0 | +0.2 | +0.2 | -0.1 |
| SAIL | +0.3 | +0.0 | +0.1 | +0.2 | +0.1 |
| RVNL | +0.3 | +0.0 | +0.0 | +0.3 | -0.0 |
| LICI | +0.2 | +0.0 | -0.3 | +0.5 | +0.0 |
| NMDC | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| SRF | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| PIIND | +0.1 | +0.0 | +0.1 | +0.1 | -0.0 |
| ENRIN | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MUTHOOTFIN | -2.4 | +0.0 | -2.4 | -0.1 | +0.1 |
| NYKAA | -2.3 | -1.8 | -0.6 | -0.0 | +0.1 |
| BSE | -2.3 | +0.0 | -2.1 | -0.5 | +0.3 |
| ADANIGREEN | -2.1 | +0.0 | -2.1 | -0.1 | +0.2 |
| VEDL | -1.9 | -1.0 | -0.5 | -0.0 | -0.3 |
| YESBANK | -1.8 | +0.0 | -2.0 | -0.0 | +0.2 |
| INDUSINDBK | -1.8 | -1.0 | -1.2 | +0.3 | +0.1 |
| MOTILALOFS | -1.8 | +0.0 | -2.4 | +0.3 | +0.3 |
| INDIGO | -1.7 | -0.8 | -0.9 | -0.1 | +0.1 |
| PFC | -1.6 | +0.0 | -1.7 | -0.1 | +0.2 |
| ADANIENT | -1.6 | +0.0 | -1.6 | -0.1 | +0.1 |
| TATACAP | -1.5 | +0.0 | -1.4 | -0.2 | +0.1 |
| SHRIRAMFIN | -1.5 | -0.7 | -0.8 | -0.1 | +0.1 |
| ADANIENSOL | -1.5 | +0.0 | -1.6 | -0.1 | +0.2 |
| PHOENIXLTD | -1.5 | +0.0 | -1.6 | -0.0 | +0.1 |

Share of absolute impact by order: 1: 6%, 2: 73%, 3: 14%, 4: 7%

## Sources
- 2026-09-23 10-year Treasury yield rockets to 19-year high - CNBC https://news.google.com/rss/search?q=10-year%20Treasury%20yield%20rockets%20to%2019-year%20high&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-24 US 30-Year Yield Hits Highest Since 2004 as Bond Selloff Deepens - Bloomberg https://news.google.com/rss/search?q=US%2030-Year%20Yield%20Hits%20Highest%20Since%202004%20as%20Bond%20Selloff%20Deepens%20-%20Bloomberg&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-04 Treasury Yields Fall as Democrats Sweep Congress - TradingView https://news.google.com/rss/search?q=Treasury%20Yields%20Fall%20as%20Democrats%20Sweep%20Congress%20-%20TradingView&hl=en-IN&gl=IN&ceid=IN:en