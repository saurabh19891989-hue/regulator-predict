# Anthropic IPO prices and lists (proposed ticker ANT), Nov 2026-Q1 2027 (`EV_ANTHROPIC_IPO_LISTING`)
*global_macro · status anticipated · date 2026-12-15 · P(3m) 0.65 · P(12m) 0.85 · confidence low*

Anthropic S-1 reported (WSJ 20 Oct; Reuters 29 Sep); public filing expected as early as 23 Oct; IPO talked of at ~US$2 trn (Equiti 17 Oct, unverified). On 27-28 Oct Indian IT fell 2-5% as the IPO sparked a global AI-stock rally -- a signal the market sees frontier-AI success as negative for IT outsourcers. Listing date unknown; P(listed by Feb 2027)=0.65, by 12m 0.85. Also tests AI-funding appetite.

**Review override applied:** The event's own description says Indian IT already fell 2-5% on 27-28 Oct when the S-1/IPO news sparked the global AI rally. The listing re-uses the same narrative, and an IPO does not change the substitution rate of IT labour. A further +0.5 SSU at p 0.85 counts the already-realised reaction twice: it books -1.9% expected for MPHASIS, -1.4% NAUKRI and -1.05% COFORGE. The T_GENAI shock is cut to 0.2.

**Already moved:** Nifty IT -2% to -5% on 27-28 Oct.

## Entry shocks (conditional on the event)
- `T_GENAI_SERVICES` GenAI substitution of IT/BPO labour (higher = more substitution): 0.2 SSU (range 0.0…0.5) residual narrative shock at listing; the S-1 reaction (27-28 Oct) is already in prices
- `F_AI_CAPEX` Global AI / data-centre capex: 0.2 SSU (range 0.0…0.5) fresh capital for compute

## Causal chains (agent)
- order 2: EV_ANTHROPIC_IPO_LISTING → T_GENAI_SERVICES → F_US_TECH_SPEND — enterprise budgets shift to AI vendors
- order 3: EV_ANTHROPIC_IPO_LISTING → T_GENAI_SERVICES → I_IT_SERVICES — pricing deflation in IT outsourcing
- order 4: EV_ANTHROPIC_IPO_LISTING → T_GENAI_SERVICES → F_WAGES_IN → TCS — fresher hiring and utilisation reset

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| POWERINDIA | +1.0 | +0.7 | +0.3 | +0.1 | +0.0 |
| TATACOMM | +0.7 | +0.5 | +0.2 | +0.0 | +0.0 |
| ENRIN | +0.7 | +0.5 | +0.2 | +0.0 | +0.0 |
| CUMMINSIND | +0.5 | +0.0 | +0.5 | +0.0 | -0.0 |
| CGPOWER | +0.5 | +0.3 | +0.1 | +0.0 | +0.0 |
| ABB | +0.4 | +0.2 | +0.2 | +0.0 | -0.0 |
| SIEMENS | +0.3 | +0.0 | +0.3 | +0.0 | -0.0 |
| PAYTM | +0.3 | +0.2 | +0.0 | +0.0 | -0.0 |
| ADANIGREEN | +0.3 | +0.0 | +0.2 | +0.0 | +0.0 |
| KEI | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| GVT&D | +0.2 | +0.0 | +0.2 | +0.1 | +0.0 |
| ADANIENSOL | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| LT | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| POLYCAB | +0.2 | +0.0 | +0.1 | +0.0 | -0.0 |
| APARINDS | +0.1 | +0.0 | +0.1 | +0.1 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| WIPRO | -1.0 | -1.2 | +0.2 | +0.0 | -0.0 |
| INFY | -0.8 | -1.0 | +0.1 | +0.0 | -0.0 |
| HCLTECH | -0.6 | -0.8 | +0.2 | +0.0 | -0.0 |
| LTM | -0.6 | -0.8 | +0.2 | +0.0 | -0.0 |
| MPHASIS | -0.5 | -0.7 | +0.2 | +0.0 | -0.0 |
| NAUKRI | -0.5 | -0.8 | +0.2 | +0.1 | -0.0 |
| TECHM | -0.4 | -0.8 | +0.3 | +0.0 | +0.0 |
| TCS | -0.4 | -0.8 | +0.3 | +0.0 | +0.0 |
| BOSCHLTD | -0.3 | +0.0 | -0.2 | -0.1 | -0.0 |
| OFSS | -0.3 | -0.4 | +0.1 | +0.0 | -0.0 |
| MARUTI | -0.2 | +0.0 | -0.1 | -0.1 | -0.0 |
| HYUNDAI | -0.2 | +0.0 | -0.1 | -0.1 | -0.0 |
| LGEINDIA | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| INDIGO | -0.2 | +0.0 | -0.1 | -0.1 | -0.0 |
| GMRAIRPORT | -0.2 | +0.0 | -0.1 | -0.1 | -0.0 |

Share of absolute impact by order: 1: 37%, 2: 42%, 3: 15%, 4: 5%

## Sources
- 2026-10-20 Anthropic S-1 Shows Red-Hot Growth, Risks and Massive Computing Costs - WSJ https://news.google.com/rss/search?q=Anthropic%20S-1%20Shows%20Red-Hot%20Growth%2C%20Risks%20and%20Massive%20Computing%20Costs%20-%20WSJ&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-27 TCS, Infosys, other IT stocks drop up to 3% as Anthropic IPO sparks rally in global AI stocks - ET https://news.google.com/rss/search?q=TCS%2C%20Infosys%2C%20other%20IT%20stocks%20drop%20up%20to%203%25%20as%20Anthropic%20IPO%20sparks%20rally%20in%20global%20AI%20stocks%20-%20ET&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-22 Anthropic could file for IPO Friday - TradingView https://news.google.com/rss/search?q=Anthropic%20could%20file%20for%20IPO%20Friday%20-%20TradingView&hl=en-IN&gl=IN&ceid=IN:en