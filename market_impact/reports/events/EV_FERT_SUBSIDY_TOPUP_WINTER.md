# Supplementary demand for grants adds fertiliser subsidy top-up in winter session (`EV_FERT_SUBSIDY_TOPUP_WINTER`)
*agri_rural · status anticipated · date 2026-12-15 · P(3m) 0.6 · P(12m) 0.9 · confidence low*

Fertiliser subsidy running above budget: industry sees up to Rs 3 lakh crore for FY27. Parliament's winter session (typically late Nov-Dec) and the Budget-session supplementary grants (Feb) are the usual vehicles. Probability that supplementary demands incl. an extra fertiliser subsidy of at least Rs 50,000 crore are passed by end-March 2027: 90%; by mid-Dec: 60% (date of session not verified).

## Entry shocks (conditional on the event)
- `P_FERT_SUBSIDY` Fertiliser subsidy generosity: 0.5 SSU (range 0.2…1.0) Conditional: extra allocation passed.
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.2 SSU (range 0.0…0.5) Larger borrowing/fiscal slippage perception (SSU +25 bp).

## Causal chains (agent)
- order 2: EV_FERT_SUBSIDY_TOPUP_WINTER → P_FERT_SUBSIDY → F_GSEC_10Y_IN — Adds fiscal slippage.
- order 3: EV_FERT_SUBSIDY_TOPUP_WINTER → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN — Higher benchmark yields widen corporate spreads.
- order 4: EV_FERT_SUBSIDY_TOPUP_WINTER → F_CREDIT_SPREADS_IN → I_NBFC_VEHICLE_CONSUMER — NBFC funding costs rise.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| GAIL | +0.4 | +0.4 | +0.0 | -0.0 | -0.0 |
| HDFCLIFE | +0.1 | +0.1 | +0.0 | -0.0 | -0.0 |
| MFSL | +0.0 | +0.1 | +0.0 | -0.0 | -0.0 |
| SBILIFE | +0.0 | +0.1 | +0.0 | -0.0 | -0.0 |
| SUZLON | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MARUTI | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| LAURUSLABS | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| DRREDDY | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| GLENMARK | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HINDCOPPER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| LUPIN | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| OIL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ONGC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| COCHINSHIP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ADANIGREEN | -0.8 | -0.7 | -0.1 | +0.0 | +0.0 |
| JIOFIN | -0.7 | -0.6 | -0.1 | -0.0 | +0.0 |
| IREDA | -0.7 | -0.6 | -0.1 | +0.0 | -0.0 |
| BANKINDIA | -0.7 | -0.6 | +0.0 | -0.0 | -0.0 |
| POWERGRID | -0.6 | -0.6 | +0.0 | -0.0 | +0.0 |
| PFC | -0.6 | -0.5 | -0.0 | -0.0 | +0.0 |
| TATACAP | -0.6 | -0.5 | -0.1 | -0.0 | +0.0 |
| BAJFINANCE | -0.6 | -0.5 | -0.0 | -0.0 | +0.0 |
| ADANIENT | -0.6 | -0.5 | -0.0 | -0.0 | +0.0 |
| JSWENERGY | -0.6 | -0.5 | -0.1 | +0.0 | +0.0 |
| GMRAIRPORT | -0.5 | -0.5 | -0.0 | -0.0 | -0.0 |
| TATAPOWER | -0.5 | -0.5 | -0.0 | +0.0 | +0.0 |
| PHOENIXLTD | -0.5 | -0.5 | -0.0 | -0.0 | -0.0 |
| BSE | -0.5 | -0.5 | +0.0 | +0.0 | +0.0 |
| GROWW | -0.5 | -0.5 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 84%, 2: 6%, 3: 6%, 4: 3%

## Sources
- 2026-10-02 Subsidy to Rs 3 lakh crore https://eng.ruralvoice.in/national/high-gas-and-sulphur-prices-could-push-fertiliser-subsidy-to-rs-3-lakh-crore.html