# Fertiliser subsidy pressure: gas ~US$28/MMBtu, DAP >US$900/t, sulphur ~US$900/t; urea imports cheaper at ~US$390/t (`EV_FERT_COST_SQUEEZE26`)
*agri_rural · status occurred · date 2026-10-02 · P(3m) 1.0 · P(12m) 1.0 · confidence medium*

Industry estimates (RuralVoice, 2 Oct): subsidy could reach Rs 3 lakh crore in FY27; gas for urea rose from ~US$15 to ~US$28/MMBtu after the Iran-US war; domestic urea cost >Rs 62,000/t; DAP >US$900/t; sulphur ~US$900/t with supply below normal (Qatar gas/sulphur disruptions). Imported urea fell from >US$900/t to ~US$400 after China resumed exports: RCF tender (finalised 13 Aug) secured 17 lakh t at US$390.25-393.65/t vs US$444.9-449.3 and US$935-959 in earlier tenders; IPL tender for 17 lakh t (Dec 1 shipment) issued. Fertiliser ministry said in July that Rs 70K crore spent and funds were adequate. Rabi NBS (nutrient-based subsidy) rates for DAP/NPK still awaited as of 25 Oct (RuralVoice: delayed decisions keep DAP prices high). Rabi fertiliser requirement projected at 38 MT. Chambal Fertilisers Q2 results steady (4 Nov).

**Already moved:** F_GAS_GLOBAL (Henry Hub proxy) -7.0% since 1 Jun but +12% 3m; sulphur/DAP not in factor_state.

## Entry shocks (conditional on the event)
- `F_FERTILISER_INPUTS` Ammonia / urea / phosphate input prices: 1.0 SSU (range 0.5…1.6) Higher gas and DAP/sulphur costs (+15% SSU); partly offset by urea import prices at ~$390.
- `P_FERT_SUBSIDY` Fertiliser subsidy generosity: 0.5 SSU (range 0.2…1.0) Subsidy generosity rising (budget allocations being overshot); NBS revision pending.

## Causal chains (agent)
- order 2: EV_FERT_COST_SQUEEZE26 → F_FERTILISER_INPUTS → P_FERT_SUBSIDY — Government must raise NBS rates to avoid farm-gate price increases in a drought year.
- order 3: EV_FERT_COST_SQUEEZE26 → P_FERT_SUBSIDY → F_GDP_IN — Higher subsidy bill (Rs 3 lakh crore vs Rs 1.7-1.9 lakh crore budgeted, model knowledge) crowds out other spending.
- order 4: EV_FERT_COST_SQUEEZE26 → P_FERT_SUBSIDY → F_GSEC_10Y_IN — Wider fiscal deficit adds to G-sec supply/term premium.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| GAIL | +0.4 | +0.4 | +0.0 | +0.0 | -0.0 |
| HDFCLIFE | +0.1 | +0.0 | +0.1 | +0.0 | -0.0 |
| MFSL | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| SBILIFE | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| LAURUSLABS | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MARUTI | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SUZLON | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
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
| ADANIGREEN | -0.6 | +0.0 | -0.4 | -0.1 | -0.0 |
| BAJFINANCE | -0.5 | +0.0 | -0.3 | -0.2 | -0.0 |
| YESBANK | -0.5 | +0.0 | -0.4 | -0.1 | -0.1 |
| SOLARINDS | -0.5 | -0.5 | +0.0 | -0.0 | +0.0 |
| JIOFIN | -0.5 | +0.0 | -0.4 | -0.1 | -0.0 |
| TATACAP | -0.5 | +0.0 | -0.3 | -0.2 | -0.0 |
| IREDA | -0.5 | +0.0 | -0.4 | -0.1 | -0.0 |
| BANKINDIA | -0.5 | +0.0 | -0.4 | -0.1 | -0.1 |
| GMRAIRPORT | -0.5 | +0.0 | -0.3 | -0.1 | -0.0 |
| POWERGRID | -0.5 | +0.0 | -0.4 | -0.1 | -0.0 |
| PFC | -0.4 | +0.0 | -0.3 | -0.1 | -0.0 |
| JSWENERGY | -0.4 | +0.0 | -0.3 | -0.1 | -0.0 |
| ADANIENT | -0.4 | +0.0 | -0.3 | -0.1 | -0.0 |
| TATAPOWER | -0.4 | +0.0 | -0.3 | -0.1 | -0.0 |
| IDEA | -0.4 | +0.0 | -0.2 | -0.1 | -0.0 |

Share of absolute impact by order: 1: 3%, 2: 61%, 3: 28%, 4: 8%

## Sources
- 2026-10-02 High gas and sulphur prices could push fertiliser subsidy to Rs 3 lakh crore - RuralVoice https://eng.ruralvoice.in/national/high-gas-and-sulphur-prices-could-push-fertiliser-subsidy-to-rs-3-lakh-crore.html
- 2026-08-14 India locks in 1.7 mn t urea import at lower prices - Indian Express https://indianexpress.com/article/business/india-urea-imports-1-7-million-tonnes-lower-prices-rabi-season-10832540/
- 2026-09-29 Rabi fertiliser requirement 38 MT https://www.financialexpress.com/policy/economy-foodgrain-output-estimate-for-2026-27-reduced-marginally-4349877/