# Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`)
*india_macro · status risk_scenario · date 2027-01-15 · P(3m) 0.05 · P(12m) 0.18 · confidence low*

Triggers: oil back >US$105 (US-Iran war flare-up, Hormuz/Kharg risk), further FPI exits, India-US trade breakdown. RBI has ~US$200bn net short forward book (record, Aug), reserves US$719.75bn and falling seven weeks; Reuters (15 Oct) says half of US$140bn capital haul spent. RBI response could include FCNR(B) schemes, import curbs, an out-of-cycle/50 bp hike, and CRR hikes. P(by 12m) 0.22 is a judgement.

**Review override applied:** The main trigger (Brent >$105) has receded: Brent is $95. The rupee is at a 2-week high of 94.33-94.55 on 5 Nov (Yahoo 94.49 confirmed).

## Entry shocks (conditional on the event)
- `F_USDINR` USD/INR exchange rate: 1.3 SSU (range 0.9…2.0) 94.5 -> ~98.3 (+4%)
- `NEW_FX_RESERVES_IN` India FX reserves (RBI intervention): -2.8 SSU (range -4.0…-2.0) -US$70bn to ~US$650bn
- `F_LIQUIDITY_IN` Indian banking system liquidity: -1.5 SSU (range -3.0…-0.5) 
- `F_REPO_IN` RBI repo rate: 1.0 SSU (range 0.0…2.0) emergency tightening
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: -1.5 SSU (range -3.0…-0.5) 
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 1.0 SSU (range 0.3…2.0) 

## Causal chains (agent)
- order 2: EV_RUPEE_BREAK_98_RESERVE_STRESS → F_USDINR → F_CPI_IN — Imported inflation
- order 3: EV_RUPEE_BREAK_98_RESERVE_STRESS → F_USDINR → F_CPI_IN → F_REPO_IN — Further tightening
- order 4: EV_RUPEE_BREAK_98_RESERVE_STRESS → F_USDINR → F_CPI_IN → F_REPO_IN → F_CREDIT_GROWTH_IN — Credit slowdown
- order 2: EV_RUPEE_BREAK_98_RESERVE_STRESS → F_USDINR → TCS — Exporters gain

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| NATIONALUM | +3.4 | +3.4 | +0.0 | +0.0 | +0.0 |
| OIL | +3.4 | +3.4 | +0.0 | +0.0 | +0.0 |
| ONGC | +3.3 | +3.3 | +0.0 | -0.0 | +0.0 |
| JSWSTEEL | +3.3 | +2.0 | +1.4 | -0.1 | -0.0 |
| VAML | +2.8 | +3.2 | -0.4 | +0.0 | +0.0 |
| PIIND | +2.6 | +2.6 | +0.0 | +0.0 | +0.0 |
| DRREDDY | +2.4 | +2.5 | -0.0 | -0.0 | +0.0 |
| SAIL | +2.3 | +0.1 | +2.4 | -0.1 | -0.0 |
| NMDC | +2.3 | +2.0 | +0.3 | -0.0 | +0.0 |
| HINDCOPPER | +2.2 | +2.2 | +0.0 | +0.0 | +0.0 |
| HINDZINC | +2.2 | +2.1 | +0.1 | +0.0 | +0.0 |
| TATASTEEL | +2.1 | +1.0 | +1.2 | -0.0 | -0.0 |
| LUPIN | +2.1 | +2.2 | -0.0 | -0.1 | +0.0 |
| JINDALSTEL | +1.8 | -0.5 | +2.3 | +0.0 | +0.0 |
| TMPV | +1.8 | +2.1 | -0.2 | -0.1 | -0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -15.9 | -14.2 | -1.4 | -0.1 | -0.3 |
| MOTILALOFS | -14.2 | -11.9 | -2.3 | +0.1 | -0.1 |
| BAJFINANCE | -12.4 | -10.3 | -2.2 | +0.1 | +0.1 |
| GMRAIRPORT | -12.1 | -10.1 | -1.3 | -0.5 | -0.3 |
| TATACAP | -11.5 | -9.7 | -2.1 | +0.4 | -0.0 |
| PRESTIGE | -11.2 | -9.5 | -1.8 | +0.1 | -0.0 |
| ADANIGREEN | -11.2 | -10.3 | -1.0 | +0.0 | +0.1 |
| AUBANK | -10.7 | -10.0 | -1.0 | +0.4 | -0.1 |
| IDEA | -10.7 | -9.2 | -1.4 | -0.1 | +0.0 |
| IREDA | -10.6 | -9.5 | -1.5 | +0.3 | +0.1 |
| JIOFIN | -10.4 | -8.2 | -2.2 | -0.1 | +0.1 |
| IDFCFIRSTB | -10.4 | -9.4 | -0.9 | +0.2 | -0.2 |
| SHRIRAMFIN | -10.4 | -8.1 | -1.7 | -0.3 | -0.2 |
| GODREJPROP | -10.2 | -7.6 | -2.6 | +0.0 | -0.0 |
| JSWENERGY | -10.1 | -9.2 | -1.0 | +0.0 | +0.1 |

Share of absolute impact by order: 1: 85%, 2: 11%, 3: 3%, 4: 1%

## Sources
- 2026-10-01 RBI's Net Short Dollar Position Soars to Record $200 Billion in August - Rediff https://news.google.com/rss/search?q=RBI+net+short+dollar+position+record+%24200+billion+forward+book+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-09 Rupee falls past 95/USD as oil climbs - Reuters https://news.google.com/rss/search?q=Rupee+falls+past+95+as+oil+climbs+RBI+swaps+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-10 India's central bank tries to shore up rupee as it nears record lows - Financial Times https://news.google.com/rss/search?q=India+central+bank+tries+to+shore+up+rupee+near+record+lows+when:120d&hl=en-IN&gl=IN&ceid=IN:en