# MCX — Multi Commodity Exchange of India Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +0.9%** (rank 78 / 83 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +33.1%): 3 months 52%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.9% … P90 +12.6%; plausible 12m relative-return range incl. stock-specific noise: -46.9% … +51.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.8 pp (model impact -3.6% beta-adjusted vs realised market-adjusted move +11.5%); forward event exposure +8.3% (3m +6.2%; half assumed priced); company-specific events -0.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| SEBI F&O / market-structure tightening (`P_SEBI_DERIVATIVES`) | +1 = tightening step | -5.91 | -5.00 | -0.93 | +0.00 | +0.02 | — |
| Competition in commodity derivatives (`NEW_COMMODITY_EXCHANGE_COMPETITION`) | +1 = credible entrant/launch capturing ~10% of bullion/energy options volume | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +2.52 | +0.00 | +2.24 | +0.68 | -0.40 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +2.39 | +2.00 | +0.36 | +0.13 | -0.11 | — |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +2.37 | +3.00 | -0.60 | -0.03 | +0.00 | — |
| Gold price (`F_GOLD`) | +8% gold (USD) | +2.10 | +1.50 | +0.60 | -0.00 | +0.00 | -8.4% |
| US dollar index (`F_DXY`) | +3% DXY | -1.76 | +0.00 | -1.03 | -0.81 | +0.09 | +2.2% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.69 | +1.50 | +0.37 | -0.18 | +0.00 | — |
| Silver price (`F_SILVER`) | +12% silver | +1.65 | +1.50 | +0.15 | +0.00 | +0.00 | -30.0% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +1.32 | +1.30 | +0.18 | -0.12 | -0.05 | +0.0% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.29 | +0.00 | -0.66 | -0.54 | -0.09 | +9.4% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.15 | +0.00 | -1.17 | -0.16 | +0.18 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.13 | +0.00 | +0.72 | +0.39 | +0.02 | +1.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.92 | -0.50 | -0.15 | -0.25 | -0.03 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +7.7% | +7.7% | +6.4 | +1.9 | -0.2 | -0.4 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -6.3% | -6.3% | -5.3 | -0.8 | -0.4 | +0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.9% | -3.9% | -3.5 | -0.8 | +0.4 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -1.9 | -1.2 | +0.2 |
| SEBI partly reverses derivative expiry-settlement rule after closing-auction (CAS) volatility (`EV_SEBI_CAS_DERIV_REVERSAL`) | anticipated | 0.85 | +2.6% | +2.2% | +2.6 | +0.0 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.4% | +2.2% | +4.0 | +0.9 | -0.5 | +0.0 |
| Gold/silver rebound as Fed hike fears fade or Iran war ends (`EV_PRECIOUS_METALS_REBOUND_H1_2027`) | anticipated | 0.45 | +4.2% | +1.9% | +3.8 | +0.3 | +0.2 | -0.0 |
| Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`) | risk_scenario | 0.30 | -6.2% | -1.9% | -5.8 | +0.0 | -0.2 | -0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -0.9 | -0.8 | +0.0 |
| SEBI tightens F&O further (weekly-expiry scrapping, higher margins/lot sizes) (`EV_SEBI_FNO_CURBS_RISK`) | risk_scenario | 0.20 | -8.0% | -1.6% | -8.0 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -2.7% | -1.6% | -1.7 | -1.0 | -0.1 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -5.0% | -1.4% | -2.0 | -2.0 | -1.5 | +0.5 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → MCX | +6.44% | +6.44% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_SILVER → MCX | -3.75% | -3.75% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → MCX | -3.30% | -3.30% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MCX | +3.75% | +1.88% |
| 1 | EV_SEBI_CAS_DERIV_REVERSAL ⇒ P_SEBI_DERIVATIVES → MCX | +2.00% | +1.70% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_GOLD → MCX | -1.58% | -1.58% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MCX | +3.25% | +1.16% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → MCX | -1.95% | -1.13% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → MCX | -1.06% | -1.06% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → MCX | +2.25% | +1.01% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ P_SEBI_DERIVATIVES → MCX | -5.00% | -1.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → MCX | +0.94% | +0.94% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → MCX | -3.00% | -0.90% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MCX | -2.85% | -0.85% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → MCX | +0.75% | +0.75% |

## Analyst profile (agent research, sourced)
# MCX - Multi Commodity Exchange of India (midcap, market infrastructure)

## Business
MCX is India's near-monopoly commodity derivatives exchange (about 98% share of listed commodity futures and options). Bullion (gold, silver), energy (crude oil, natural gas) and base metals contracts generate fee income that scales with notional turnover and options volumes. Operating margin is 74-76% and the company is debt-free. Q2 FY27 revenue was about Rs 800 cr (+114% y/y), PAT Rs 455 cr (+130%); TTM profit Rs 1,799 cr; FIIs hold 27%, DIIs 55%.

## What moves the stock (ranked)
1. **Regulatory risk (SEBI/Budget)** - one SEBI tightening step or a CTT hike could cut options volumes and EBITDA sharply (about -5% expected, up to -12%). This is the largest idiosyncratic tail.
2. **Commodity volatility and turnover** - gold (-8.4% since June), silver (-30%), Brent ($95, +49.5% 12m) provide the volume boom. Direction matters less than volatility and notional; Brent +10% lifts equity about +1.3%.
3. **Retail/derivative participation** - risk-on (equity activity +20%) raises options turnover (+3%).
4. **Rupee** - weaker INR raises INR notional (+1.2% per +3%).
5. **Competition and platforms** - BSE/NSE competition in commodity derivatives, MCX's Rs 200 cr coal/minerals platforms.

## Transmission examples
- **Middle East escalation -> Brent spikes -> crude options volumes surge -> MCX revenue up (profit +130% y/y in Q2) -> but a regulator may react to speculative frenzy (SEBI tightening, 3rd-order) -> position limits/margin hikes -> volume drops -> earnings cut.**
- **US 10y 4.89% and DXY up -> gold/silver fall (silver -14% 1m) -> large intraday swings, margin calls -> hedging and trading volumes rise -> MCX benefits; 4th-order: retail losses lead to SEBI risk review and a reduction in lot/leverage.**
- **Weaker rupee -> INR gold up -> higher notional turnover -> revenue up without extra costs (fixed cost base).**
- **Equity F&O slump (CAS chaos, Sept) -> traders migrate to commodity options -> MCX gains (Bernstein prefers MCX over BSE).**

## Current situation
Stock is +81% in 12 months and fell 5-7% on 4 Nov despite a 130% profit jump, consistent with a valuation (P/E 47.8) already pricing the earnings. The specific reasons cited in press (CNBC TV18 'key factors') were not retrieved; plausibly sequential growth, cost or regulatory worries. Analysts remain constructive (Religare target Rs 3,700).

## Upcoming
Q3 FY27 results in January; Union Budget in February (CTT); SEBI derivatives decisions; coal/minerals platform launch.

## Bull / bear
Bull: sustained commodity volatility, new products, high operating leverage, market share ~98%. Bear: regulatory curbs, volume normalisation, valuation compression, competitor entry.

Uncertainty: revenue mix shares are model knowledge; competition edge relies on a proposed node; empirical wheat (+3.9, t 3.8) and aluminium sensitivities treated as commodity-volatility proxies, not modelled.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.