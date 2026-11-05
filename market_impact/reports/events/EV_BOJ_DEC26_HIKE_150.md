# BoJ Dec 2026 meeting: hike to 1.50% (quarterly pace) (`EV_BOJ_DEC26_HIKE_150`)
*global_macro · status scheduled · date 2026-12-18 · P(3m) 0.65 · P(12m) 0.7 · confidence low*

Reuters poll 23 Oct: BoJ to raise to 1.50% in December, keeping a quarterly pace; ex-BoJ official sees 2% by mid-2027 (BigGo 23 Sep). Exact meeting date (~17-18 Dec) not verified. P(hike by Dec meeting)=0.65 (our estimate; poll majority but yen/JGB sensitivity).

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `NEW_USDJPY` USD/JPY exchange rate: -0.5 SSU (range -1.2…0.0) yen firmer
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 0.2 SSU (range 0.0…0.6) carry jitters
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: -0.1 SSU (range -0.4…0.1) minor

## Causal chains (agent)
- order 2: EV_BOJ_DEC26_HIKE_150 → NEW_USDJPY → F_RISK_SENTIMENT — carry-trade deleveraging
- order 3: EV_BOJ_DEC26_HIKE_150 → F_RISK_SENTIMENT → F_FPI_FLOWS — EM outflows
- order 4: EV_BOJ_DEC26_HIKE_150 → F_FPI_FLOWS → F_USDINR → F_GSEC_10Y_IN — INR and yields

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HINDZINC | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| NATIONALUM | +0.2 | +0.0 | +0.1 | +0.0 | +0.0 |
| TATACONSUM | +0.1 | +0.2 | -0.0 | +0.0 | -0.0 |
| ASTRAL | +0.1 | +0.2 | -0.0 | +0.0 | -0.0 |
| HINDALCO | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| TATASTEEL | +0.1 | +0.0 | +0.1 | +0.1 | -0.0 |
| JSWSTEEL | +0.1 | +0.0 | +0.1 | +0.0 | -0.0 |
| SAIL | +0.1 | +0.0 | +0.0 | +0.1 | -0.1 |
| HINDCOPPER | +0.1 | -0.1 | +0.1 | +0.1 | -0.0 |
| ONGC | +0.1 | +0.0 | +0.1 | -0.0 | -0.0 |
| OIL | +0.1 | +0.0 | +0.1 | -0.0 | -0.0 |
| UPL | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| PIIND | +0.1 | +0.0 | +0.1 | -0.0 | +0.0 |
| AMBUJACEM | +0.1 | +0.0 | +0.1 | -0.0 | -0.0 |
| NMDC | +0.1 | +0.0 | +0.1 | -0.0 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -1.5 | -1.3 | -0.2 | +0.0 | -0.0 |
| ICICIAMC | -1.3 | -1.2 | -0.1 | +0.0 | -0.0 |
| JIOFIN | -1.3 | -1.2 | -0.0 | -0.0 | -0.0 |
| IREDA | -1.3 | -1.2 | -0.0 | +0.0 | -0.0 |
| MEESHO | -1.2 | -1.2 | +0.0 | -0.0 | -0.0 |
| 360ONE | -1.1 | -1.1 | -0.1 | -0.0 | -0.0 |
| INDUSINDBK | -1.1 | -1.1 | -0.0 | +0.0 | -0.0 |
| MAHABANK | -1.0 | -1.0 | -0.0 | +0.0 | -0.0 |
| IDFCFIRSTB | -0.9 | -0.9 | -0.0 | -0.0 | -0.0 |
| PAYTM | -0.9 | -0.9 | -0.0 | +0.0 | +0.0 |
| NAUKRI | -0.9 | -0.8 | -0.1 | +0.0 | -0.0 |
| LENSKART | -0.9 | -0.9 | -0.0 | -0.0 | -0.0 |
| POLICYBZR | -0.9 | -0.9 | +0.0 | -0.0 | +0.0 |
| LICI | -0.9 | -0.9 | -0.0 | -0.0 | -0.0 |
| ETERNAL | -0.9 | -0.9 | -0.0 | +0.0 | -0.0 |

Share of absolute impact by order: 1: 76%, 2: 13%, 3: 6%, 4: 5%

## Sources
- 2026-10-23 BOJ to raise rates to 1.50% in December, sticking to quarterly pace: Reuters poll https://news.google.com/rss/search?q=BOJ%20to%20raise%20rates%20to%201.50%25%20in%20December%2C%20sticking%20to%20quarterly%20pace%3A%20Reuters%20poll&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-23 Ex-BOJ Official Sees Quarterly Rate Hikes Pushing Policy to 2% by Mid-2027 https://news.google.com/rss/search?q=Ex-BOJ%20Official%20Sees%20Quarterly%20Rate%20Hikes%20Pushing%20Policy%20to%202%25%20by%20Mid-2027&hl=en-IN&gl=IN&ceid=IN:en