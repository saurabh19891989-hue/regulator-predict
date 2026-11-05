# AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`)
*global_macro · status occurred · date 2026-10-22 · P(3m) 1 · P(12m) 1 · confidence medium*

Nasdaq -5% in October ('AI stocks lost $5 trn', Yahoo 1 Nov); S&P/Nasdaq sharply lower 22 Oct on AI-spending doubts + Iran war; Alphabet worst week since 2011 and Intel record crash (week to 30 Oct); CoreWeave -25% (16 Oct); Google and Microsoft deferred raising capex forecasts (CNBC 29 Oct). Big-tech 2026 capex still ~US$725-828 bn (various estimates). Partial rebound 2-3 Nov.

**Already moved:** Nasdaq -5% (Oct); S&P 500 7,688.6 (-1.7% 1m, +1.2% since 1 Jun); VIX 16.6 (+10.7% 1m). Nifty IT: +11% in five sessions mid-Oct on 'reverse AI trade', then -2% to -5% on 27-28 Oct as global AI stocks rebounded (Anthropic IPO).

## Entry shocks (conditional on the event)
- `F_US_EQUITIES` US equity market: -0.35 SSU (range -1.0…-0.2) S&P 1m -1.7% (Nasdaq -5%)
- `F_AI_CAPEX` Global AI / data-centre capex: -0.3 SSU (range -0.6…0.0) capex guidance raise postponed, not cut
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 0.35 SSU (range 0.2…0.8) VIX +1.7pts 1m

## Causal chains (agent)
- order 2: EV_AI_SELLOFF_OCT26 → F_US_EQUITIES → F_RISK_SENTIMENT → F_FPI_FLOWS — US equity drawdown lifts VIX and cuts EM flows
- order 3: EV_AI_SELLOFF_OCT26 → F_AI_CAPEX → F_US_TECH_SPEND → C_USA — hyperscaler capex discipline spreads to enterprise tech budgets
- order 4: EV_AI_SELLOFF_OCT26 → F_AI_CAPEX → F_US_TECH_SPEND → C_USA → TCS — US tech-spend caution is a headwind for Indian IT discretionary demand; but 'AI winner' rotation out of AI hardware helped IT in mid-Oct

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | +0.4 | +0.0 | +0.1 | +0.2 | +0.1 |
| SAIL | +0.4 | +0.0 | +0.0 | +0.2 | +0.1 |
| TATACONSUM | +0.3 | +0.3 | -0.0 | -0.0 | +0.0 |
| ASTRAL | +0.3 | +0.3 | -0.0 | -0.0 | +0.0 |
| TMPV | +0.2 | +0.0 | +0.2 | +0.1 | +0.0 |
| TATASTEEL | +0.2 | +0.0 | +0.1 | +0.1 | +0.1 |
| NATIONALUM | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| HINDZINC | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| MOTHERSON | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| NMDC | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| ONGC | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| OIL | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| SRF | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| PIIND | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| MARUTI | +0.2 | +0.0 | +0.2 | -0.0 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -2.8 | -1.8 | -0.8 | -0.4 | +0.0 |
| ICICIAMC | -2.4 | -1.8 | -0.5 | -0.2 | +0.0 |
| JIOFIN | -2.4 | -1.8 | -0.4 | -0.2 | -0.0 |
| IREDA | -2.3 | -1.8 | -0.4 | -0.1 | -0.0 |
| POWERINDIA | -2.2 | -1.6 | -0.5 | -0.1 | -0.0 |
| 360ONE | -2.1 | -1.2 | -0.6 | -0.3 | +0.0 |
| NAUKRI | -2.1 | -1.8 | -0.3 | -0.1 | +0.0 |
| MEESHO | -2.0 | -1.4 | -0.6 | -0.0 | +0.0 |
| INDUSINDBK | -2.0 | -1.2 | -0.7 | -0.1 | +0.0 |
| IDFCFIRSTB | -1.7 | -1.0 | -0.5 | -0.1 | -0.0 |
| PAYTM | -1.7 | -1.0 | -0.7 | -0.0 | +0.0 |
| MAHABANK | -1.7 | -1.2 | -0.4 | -0.1 | +0.0 |
| GROWW | -1.7 | -1.0 | -0.3 | -0.4 | +0.1 |
| LENSKART | -1.6 | -1.0 | -0.5 | -0.0 | +0.0 |
| ETERNAL | -1.5 | -0.9 | -0.6 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 41%, 2: 45%, 3: 11%, 4: 3%

## Sources
- 2026-10-29 AI buildout hits snag as Google and Microsoft put off raising capex forecasts - CNBC https://news.google.com/rss/search?q=AI%20buildout%20hits%20snag%20as%20Google%20and%20Microsoft%20put%20off%20raising%20capex%20forecasts%20-%20CNBC&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-04 Nasdaq Sinks 5% in October as AI Stock Selloff Hits Tech - TradingView https://news.google.com/rss/search?q=Nasdaq%20Sinks%205%25%20in%20October%20as%20AI%20Stock%20Selloff%20Hits%20Tech%20-%20TradingView&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-30 Alphabet Posts Worst Week Since 2011, Intel Suffers Record Crash - TradingView https://news.google.com/rss/search?q=Alphabet%20Posts%20Worst%20Week%20Since%202011%2C%20Intel%20Suffers%20Record%20Crash%20-%20TradingView&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-16 Why CoreWeave's 25% Tumble Is A Warning To AI Financiers - Forbes https://news.google.com/rss/search?q=Why%20CoreWeave%27s%2025%25%20Tumble%20Is%20A%20Warning%20To%20AI%20Financiers%20-%20Forbes&hl=en-IN&gl=IN&ceid=IN:en