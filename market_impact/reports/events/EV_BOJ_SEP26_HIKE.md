# BoJ hikes to 31-year high (18 Sep 2026); yen near 160 in Aug (`EV_BOJ_SEP26_HIKE`)
*global_macro · status occurred · date 2026-09-18 · P(3m) 1 · P(12m) 1 · confidence low*

BoJ raised its policy rate to a 31-year high (BBC 18 Sep); a Reuters poll (23 Oct) expects 1.50% in December, implying the current rate is ~1.25% (inferred, not verified). Yen had neared/breached 160 per USD in Aug; USD/JPY broke support on 22 Oct as US yields fell. Takaichi government supports hikes.

**Already moved:** USD/JPY ~160 (Aug) -> lower after BoJ hike and falling UST yields (no price series in factor_state.md; unquantified). JGB yields at multi-decade highs (Sept).

## Entry shocks (conditional on the event)
- `NEW_USDJPY` USD/JPY exchange rate: -0.5 SSU (range -1.0…-0.2) yen firmer vs August peak; approx -1.5% (unverified level)
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 0.2 SSU (range 0.0…0.5) carry-unwind jitters

## Causal chains (agent)
- order 2: EV_BOJ_SEP26_HIKE → NEW_USDJPY → F_RISK_SENTIMENT — yen strength forces carry-trade deleveraging, lifting VIX
- order 3: EV_BOJ_SEP26_HIKE → F_RISK_SENTIMENT → F_FPI_FLOWS → F_USDINR — risk-off reduces EM equity allocations
- order 4: EV_BOJ_SEP26_HIKE → NEW_USDJPY → F_DXY → F_GOLD — weaker dollar side effect supports gold/metals

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HINDZINC | +0.2 | +0.0 | +0.1 | +0.1 | +0.1 |
| NATIONALUM | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| JSWSTEEL | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| SAIL | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| TATASTEEL | +0.2 | +0.0 | +0.0 | +0.1 | +0.0 |
| HINDALCO | +0.2 | +0.0 | +0.0 | +0.1 | +0.0 |
| TATACONSUM | +0.1 | +0.2 | -0.0 | -0.0 | +0.0 |
| ASTRAL | +0.1 | +0.2 | -0.0 | -0.0 | -0.0 |
| ONGC | +0.1 | +0.0 | +0.1 | +0.1 | -0.0 |
| OIL | +0.1 | +0.0 | +0.1 | +0.1 | -0.0 |
| NMDC | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| PIIND | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| UPL | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| SRF | +0.1 | +0.0 | +0.0 | +0.0 | -0.0 |
| HINDCOPPER | +0.1 | +0.0 | -0.1 | +0.2 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -1.9 | -0.7 | -1.0 | -0.3 | +0.1 |
| ICICIAMC | -1.6 | -0.8 | -0.8 | -0.1 | +0.1 |
| JIOFIN | -1.5 | -1.0 | -0.4 | -0.1 | -0.0 |
| 360ONE | -1.4 | -0.7 | -0.5 | -0.2 | +0.0 |
| IREDA | -1.4 | -1.0 | -0.3 | -0.0 | -0.0 |
| MEESHO | -1.3 | -0.8 | -0.6 | +0.0 | +0.0 |
| INDUSINDBK | -1.3 | -0.7 | -0.6 | +0.0 | +0.0 |
| PAYTM | -1.1 | -0.4 | -0.8 | +0.1 | +0.0 |
| GROWW | -1.1 | -0.4 | -0.4 | -0.4 | +0.2 |
| IDFCFIRSTB | -1.1 | -0.6 | -0.5 | +0.0 | -0.0 |
| NAUKRI | -1.1 | -0.5 | -0.6 | -0.0 | +0.0 |
| MAHABANK | -1.1 | -0.7 | -0.4 | +0.0 | +0.0 |
| LENSKART | -1.0 | -0.6 | -0.5 | +0.0 | +0.0 |
| POLICYBZR | -1.0 | -0.5 | -0.6 | +0.1 | +0.0 |
| ETERNAL | -1.0 | -0.5 | -0.6 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 28%, 2: 58%, 3: 10%, 4: 4%

## Sources
- 2026-09-18 Japan raises interest rate to new 31-year high to curb rising prices - BBC https://news.google.com/rss/search?q=Japan%20raises%20interest%20rate%20to%20new%2031-year%20high%20to%20curb%20rising%20prices%20-%20BBC&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-23 BOJ to raise rates to 1.50% in December, sticking to quarterly pace: Reuters poll https://news.google.com/rss/search?q=BOJ%20to%20raise%20rates%20to%201.50%25%20in%20December%2C%20sticking%20to%20quarterly%20pace%3A%20Reuters%20poll&hl=en-IN&gl=IN&ceid=IN:en
- 2026-08-31 Yen's Breach of 160 to Dollar Puts Traders on Intervention Watch - Bloomberg https://news.google.com/rss/search?q=Yen%27s%20Breach%20of%20160%20to%20Dollar%20Puts%20Traders%20on%20Intervention%20Watch%20-%20Bloomberg&hl=en-IN&gl=IN&ceid=IN:en