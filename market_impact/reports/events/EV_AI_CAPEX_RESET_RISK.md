# AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`)
*global_macro · status risk_scenario · date 2027-02-15 · P(3m) 0.1 · P(12m) 0.25 · confidence low*

Signals: Google/Microsoft deferring capex-forecast raises (29 Oct), CoreWeave -25% (16 Oct), $3.5 trn 'shadow financing' (MacroMicro), Nvidia-OpenAI $250 bn guarantee talks (WSJ 26 Jul), October Nasdaq -5%. Trigger window: Nvidia 17 Nov, Q4 megacap results late Jan 2027. P(material cut to 2027 capex growth or credit event, Nasdaq drawdown >15%) = 0.12 by Feb, 0.28 by 12m (our judgment; includes Nvidia disappointment).

**Review override applied:** The VIX shock is inconsistent with the paired S&P shock. Hyperscalers deferred raising guidance but have not cut it (CNBC 29 Oct). Nvidia reports 17 Nov.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_AI_CAPEX` Global AI / data-centre capex: -3.0 SSU (range -5.0…-1.5) capex growth -30 pp
- `F_US_EQUITIES` US equity market: -3.0 SSU (range -5.0…-1.5) S&P -15%
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 2.5 SSU (range 1.5…4.0) VIX to ~29-30 (+12.5 pts), consistent with a -15% S&P drawdown (2022 analogue); +20 pts was inconsistent

## Causal chains (agent)
- order 2: EV_AI_CAPEX_RESET_RISK → F_US_EQUITIES → F_RISK_SENTIMENT → F_FPI_FLOWS — EM outflows
- order 3: EV_AI_CAPEX_RESET_RISK → F_AI_CAPEX → F_US_TECH_SPEND → C_USA — US tech budgets
- order 4: EV_AI_CAPEX_RESET_RISK → F_US_EQUITIES → F_US_GDP → F_FED_FUNDS — wealth effect slows US growth; Fed eases, helping EM later

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| TMPV | +2.2 | +0.0 | +1.4 | +0.6 | +0.1 |
| BOSCHLTD | +2.1 | +0.0 | +2.6 | -0.6 | +0.1 |
| MARUTI | +2.1 | +0.0 | +2.1 | -0.0 | +0.1 |
| JSWSTEEL | +2.1 | +0.0 | +0.8 | +1.0 | +0.3 |
| ASTRAL | +2.0 | +2.0 | -0.1 | -0.0 | +0.1 |
| MOTHERSON | +2.0 | +0.0 | +1.9 | +0.1 | +0.1 |
| TATACONSUM | +1.9 | +2.0 | -0.1 | -0.0 | +0.0 |
| NATIONALUM | +1.8 | +0.0 | +0.9 | +0.9 | +0.0 |
| M&M | +1.7 | +0.0 | +1.5 | +0.1 | +0.1 |
| SAIL | +1.6 | +0.0 | +0.3 | +0.8 | +0.5 |
| HINDZINC | +1.5 | +0.0 | +0.7 | +1.0 | -0.2 |
| SRF | +1.5 | +0.0 | +0.6 | +0.8 | +0.1 |
| NMDC | +1.4 | +0.0 | +0.6 | +0.8 | +0.1 |
| ONGC | +1.4 | +0.0 | +0.9 | +0.5 | -0.0 |
| TATASTEEL | +1.3 | +0.0 | +0.4 | +0.5 | +0.3 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -21.5 | -13.3 | -5.9 | -2.7 | +0.4 |
| POWERINDIA | -19.4 | -14.3 | -4.1 | -0.9 | -0.1 |
| ICICIAMC | -18.2 | -13.0 | -4.3 | -1.3 | +0.4 |
| NAUKRI | -16.5 | -13.8 | -2.0 | -0.8 | +0.1 |
| IREDA | -16.2 | -12.5 | -3.0 | -0.6 | -0.1 |
| 360ONE | -15.2 | -8.8 | -4.9 | -1.7 | +0.1 |
| INDUSINDBK | -14.6 | -8.8 | -5.7 | -0.5 | +0.3 |
| PAYTM | -13.4 | -8.0 | -5.2 | -0.3 | +0.1 |
| TATACOMM | -13.2 | -8.8 | -4.0 | -0.5 | +0.0 |
| MAHABANK | -12.4 | -8.8 | -3.6 | -0.3 | +0.2 |
| IDFCFIRSTB | -12.2 | -7.5 | -4.4 | -0.5 | +0.1 |
| ENRIN | -11.9 | -10.0 | -1.2 | -0.7 | -0.1 |
| PERSISTENT | -11.5 | -9.0 | -1.8 | -0.6 | -0.1 |
| GROWW | -11.3 | -8.0 | -0.9 | -2.9 | +0.5 |
| LICI | -11.0 | -8.8 | -2.2 | -0.2 | +0.1 |

Share of absolute impact by order: 1: 41%, 2: 49%, 3: 8%, 4: 2%

## Sources
- 2026-10-21 Either AI or public debt could crash markets. But probably not both - The Economist https://news.google.com/rss/search?q=Either%20AI%20or%20public%20debt%20could%20crash%20markets.%20But%20probably%20not%20both%20-%20The%20Economist&hl=en-IN&gl=IN&ceid=IN:en
- 2026-08-18 The AI buildout rests on hidden debt - GIS Reports https://news.google.com/rss/search?q=The%20AI%20buildout%20rests%20on%20hidden%20debt%20-%20GIS%20Reports&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-30 AI hyperscalers are expected to finish the year spending $828 billion on capex - Business Insider https://news.google.com/rss/search?q=AI%20hyperscalers%20are%20expected%20to%20finish%20the%20year%20spending%20%24828%20billion%20on%20capex%20-%20Business%20Insider&hl=en-IN&gl=IN&ceid=IN:en