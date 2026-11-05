# Banking system liquidity turns to sustained deficit by end-March 2027 (`EV_BANKING_LIQUIDITY_DEFICIT_MAR27`)
*india_macro · status anticipated · date 2027-03-31 · P(3m) 0.3 · P(12m) 0.6 · confidence low*

Governor (7 Oct): surplus 'may not persist beyond FY27', 'surplus seen easing by March'. Drains: FX sales (reserves -~US$56bn from peak), CRR maintenance 99% (16 Oct), bond sales, credit growth ~19.4% outpacing deposits (CD ratio ~85%), March advance-tax outflows. Offsets: RBI may inject via OMO/swaps if yields spike. Current surplus size not retrieved (missing information). P(deficit on average in Mar 2027) 0.60.

## Entry shocks (conditional on the event)
- `F_LIQUIDITY_IN` Indian banking system liquidity: -1.5 SSU (range -3.0…-0.5) swing from surplus to deficit
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.3 SSU (range 0.0…0.7) 
- `F_CREDIT_SPREADS_IN` Indian corporate credit spreads: 0.3 SSU (range 0.0…0.7) 
- `F_DEPOSIT_GROWTH_IN` Bank deposit growth / funding ease: 0.3 SSU (range 0.0…0.8) banks raise deposit rates

## Causal chains (agent)
- order 2: EV_BANKING_LIQUIDITY_DEFICIT_MAR27 → F_LIQUIDITY_IN → F_GSEC_10Y_IN — Liquidity deficit raises short-term and term yields
- order 3: EV_BANKING_LIQUIDITY_DEFICIT_MAR27 → F_LIQUIDITY_IN → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN — Spreads widen
- order 3: EV_BANKING_LIQUIDITY_DEFICIT_MAR27 → F_LIQUIDITY_IN → F_CREDIT_SPREADS_IN → BAJFINANCE — NBFC funding cost
- order 3: EV_BANKING_LIQUIDITY_DEFICIT_MAR27 → F_DEPOSIT_GROWTH_IN → F_CREDIT_GROWTH_IN → F_GDP_IN — Deposit competition raises cost of funds and slows credit

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HDFCBANK | +0.2 | +0.5 | -0.3 | -0.1 | -0.0 |
| RVNL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SBILIFE | +0.0 | +0.1 | +0.0 | -0.0 | -0.0 |
| MFSL | +0.0 | +0.1 | +0.0 | -0.0 | -0.0 |
| SOLARINDS | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SUZLON | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| APARINDS | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| PREMIERENE | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| POWERINDIA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| GVT&D | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MEESHO | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| MAZDOCK | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SRF | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| WAAREEENER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -3.5 | -3.3 | -0.1 | -0.0 | -0.0 |
| BAJFINANCE | -3.4 | -3.5 | +0.0 | +0.0 | +0.0 |
| TATACAP | -3.1 | -3.2 | +0.0 | +0.0 | +0.0 |
| CHOLAFIN | -2.1 | -2.1 | -0.0 | -0.0 | -0.0 |
| JIOFIN | -1.9 | -1.8 | -0.1 | +0.0 | -0.0 |
| BAJAJFINSV | -1.9 | -1.8 | -0.1 | +0.0 | -0.0 |
| ADANIGREEN | -1.8 | -1.8 | +0.0 | +0.0 | -0.0 |
| IDEA | -1.8 | -1.8 | +0.0 | -0.0 | +0.0 |
| IREDA | -1.8 | -1.8 | +0.0 | +0.0 | +0.0 |
| IDFCFIRSTB | -1.7 | -1.5 | -0.1 | -0.1 | -0.0 |
| LTF | -1.6 | -1.6 | +0.0 | +0.0 | +0.0 |
| JSWENERGY | -1.5 | -1.5 | +0.0 | +0.0 | +0.0 |
| AUBANK | -1.5 | -1.4 | -0.1 | +0.0 | -0.0 |
| INDIANB | -1.5 | -1.3 | -0.1 | -0.1 | -0.0 |
| SBIN | -1.5 | -1.3 | -0.1 | -0.0 | -0.0 |

Share of absolute impact by order: 1: 86%, 2: 7%, 3: 4%, 4: 2%

## Sources
- 2026-10-07 Surplus liquidity may not persist beyond FY27: RBI Governor - Business Standard https://news.google.com/rss/search?q=Surplus+liquidity+may+not+persist+beyond+FY27+Malhotra+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-10 Bank Credit Growth Hits 19.4%, Outpaces Deposits - BW Businessworld https://news.google.com/rss/search?q=Bank+credit+growth+19.4%25+outpaces+deposits+when:120d&hl=en-IN&gl=IN&ceid=IN:en