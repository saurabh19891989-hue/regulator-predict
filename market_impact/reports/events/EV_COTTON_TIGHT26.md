# Cotton: kharif sowing down sharply, MSP +7.2%, record 2026-27 imports expected, cotton price firm (`EV_COTTON_TIGHT26`)
*agri_rural · status occurred · date 2026-07-10 · P(3m) 1.0 · P(12m) 1.0 · confidence low*

Fibre2Fashion (10 Jul): India's kharif cotton sowing fell 23%, 2026/27 balance sheet at risk; (31 Aug CMB): tight balance, firm prices, rising imports; (1 Oct): cotton MSP up 7.2% and 'what changes when the duty returns' (the import-duty exemption status is unclear: articles titled 'duty relief' and 'duty returns'; verify the exact date and rate before use). BusinessLine (2 Nov): 2026-27 cotton imports to scale a new peak amid crop concerns and duty relief. Deficient rain adds yield risk in Maharashtra, Telangana, Karnataka. ICE cotton 78.11 c/lb: +19.7% 12m, +1.9% since 1 Jun.

**Already moved:** ICE cotton +1.9% since 1 Jun, -4.7% 3m, +0.8% 1m (factor_state).

## Entry shocks (conditional on the event)
- `F_COTTON` Cotton price: 0.2 SSU (range -0.3…0.8) Domestic cotton firm vs ICE; the import pull supports ICE modestly.
- `F_RURAL_DEMAND` Rural consumption growth: 0.0 SSU (range -0.1…0.1) Higher cotton MSP supports farmers, but the crop is down.

## Causal chains (agent)
- order 2: EV_COTTON_TIGHT26 → F_COTTON → I_TEXTILES — Yarn spreads squeezed if cotton cost rises faster than yarn prices.
- order 3: EV_COTTON_TIGHT26 → F_COTTON → F_USDINR — Higher imports add to import bill; minor.
- order 4: EV_COTTON_TIGHT26 → F_COTTON → F_RURAL_DEMAND — Cotton-belt farm income down in Maharashtra/Telangana where yield is lost.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| GRASIM | +0.1 | +0.1 | +0.0 | +0.0 | +0.0 |
| APLAPOLLO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ASIANPAINT | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| AUBANK | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| BRITANNIA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| CHOLAFIN | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| COLPAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| DABUR | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| GODFRYPHLP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| GODREJCP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HEROMOTOCO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HINDUNILVR | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ITC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| KALYANKJIL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| LTF | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PAGEIND | -0.2 | -0.2 | +0.0 | +0.0 | +0.0 |
| TRENT | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| MEESHO | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| VMM | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| BIOCON | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| APLAPOLLO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ASIANPAINT | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| AUBANK | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| BRITANNIA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| CHOLAFIN | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| COLPAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| DABUR | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| GODFRYPHLP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| GODREJCP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HEROMOTOCO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 100%, 2: 0%, 3: 0%, 4: 0%

## Sources
- 2026-11-02 India's 2026-27 cotton imports to scale new peak - BusinessLine https://www.thehindubusinessline.com/economy/agri-business/indias-2026-27-cotton-imports-to-scale-new-peak-amid-crop-concerns-duty-relief/article71649049.ece
- 2026-10-01 Indian cotton MSP up 7.2% - Fibre2Fashion (headline only; paywalled) https://www.fibre2fashion.com/news/prime-content/textile-news/indian-cotton-msp-up-7-2-what-changes-when-the-duty-returns-313917-newsdetails.htm