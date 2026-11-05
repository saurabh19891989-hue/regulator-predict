# RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`)
*india_macro · status occurred · date 2026-10-09 · P(3m) 1 · P(12m) 1 · confidence medium*

After the hike RBI raised the daily CRR maintenance requirement to 99% from 16 Oct and scheduled a Rs 25,000 crore bond sale (13 Oct) to drain surplus liquidity; Governor said surplus may not persist beyond FY27. 10y yield crossed 7% on 11 Sep, 7.40% on 12 Oct, >7.45% (multi-year high) on 21 Oct, 7.44% on 3 Nov; India-US 10y spread near a 22-year low. SBI Research sees 6.75-7.0% by March 2027; another report sees 7.25-7.35% in November. Size of the current surplus not retrieved (missing information).

**Already moved:** 10y: ~7.00% (11 Sep) -> ~7.44% (3 Nov) = about +44 bp (+1.8 SSU), of which ~+0.3 SSU attributed to the hike event. FPI G-sec outflows halved to Rs 5,400 cr in October.

## Entry shocks (conditional on the event)
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 1.4 SSU (range 1.0…1.7) residual of the +44 bp run-up since 11 Sep
- `F_LIQUIDITY_IN` Indian banking system liquidity: -0.5 SSU (range -1.0…-0.1) surplus shrinking; size unknown so low confidence
- `F_CREDIT_SPREADS_IN` Indian corporate credit spreads: 0.3 SSU (range 0.1…0.6) corporate bond spreads widen with G-sec

## Causal chains (agent)
- order 2: EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN — Benchmark yield feeds corporate bond and bank lending spreads
- order 3: EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN → BAJFINANCE — Wider spreads raise NBFC borrowing cost faster than lending repricing
- order 4: EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 → F_LIQUIDITY_IN → F_GSEC_10Y_IN → F_CREDIT_GROWTH_IN → F_GDP_IN — Liquidity drain adds to term-premium; tighter credit eventually weighs on growth
- order 4: EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 → F_GSEC_10Y_IN → F_HOUSING_DEMAND → F_URBAN_DEMAND → TITAN — Higher mortgage/consumer-loan rates cut big-ticket urban spend (jewellery, durables)

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HDFCLIFE | +0.6 | +0.7 | +0.0 | -0.1 | -0.0 |
| SBILIFE | +0.3 | +0.4 | +0.0 | -0.1 | -0.0 |
| MFSL | +0.3 | +0.4 | +0.0 | -0.1 | -0.0 |
| RVNL | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| SOLARINDS | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| APARINDS | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| PREMIERENE | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| SUZLON | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| POWERINDIA | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| SRF | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MEESHO | +0.0 | +0.0 | +0.0 | -0.0 | +0.1 |
| TATASTEEL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MAZDOCK | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| GVT&D | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -6.2 | -5.6 | -0.3 | -0.2 | -0.1 |
| ADANIGREEN | -5.7 | -5.7 | +0.0 | +0.0 | -0.0 |
| BAJFINANCE | -5.7 | -5.4 | -0.2 | -0.0 | +0.0 |
| TATACAP | -5.4 | -5.1 | -0.3 | -0.0 | +0.0 |
| JIOFIN | -5.3 | -5.1 | -0.1 | -0.1 | +0.0 |
| IREDA | -5.0 | -5.1 | +0.0 | +0.0 | +0.0 |
| BANKINDIA | -4.9 | -4.2 | -0.3 | -0.2 | -0.2 |
| GMRAIRPORT | -4.7 | -4.5 | +0.0 | -0.1 | -0.0 |
| POWERGRID | -4.2 | -4.2 | +0.0 | +0.0 | -0.0 |
| JSWENERGY | -4.2 | -4.2 | +0.0 | +0.0 | +0.0 |
| BAJAJFINSV | -4.1 | -4.0 | -0.1 | -0.0 | +0.0 |
| TATAPOWER | -4.0 | -4.0 | +0.0 | +0.0 | -0.0 |
| IDEA | -4.0 | -4.0 | +0.0 | -0.0 | +0.0 |
| ADANIENT | -4.0 | -4.0 | +0.0 | +0.0 | -0.0 |
| PFC | -3.9 | -4.0 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 87%, 2: 8%, 3: 3%, 4: 2%

## Sources
- 2026-10-21 India's 10-year bond yield climbs above 7.45% to multi-year high - Investing.com https://news.google.com/rss/search?q=India+10-year+bond+yield+multi-year+high+October+2026+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-09 RBI raises daily CRR maintenance requirement to 99% from October 16 - Moneycontrol https://news.google.com/rss/search?q=RBI+raises+daily+CRR+maintenance+99%25+October+16+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-01 Indian 10-year bond yield may ease to 6.75-7% by March - SBI Research https://news.google.com/rss/search?q=India+10-year+bond+yield+November+2026+SBI+Research+6.75-7%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en