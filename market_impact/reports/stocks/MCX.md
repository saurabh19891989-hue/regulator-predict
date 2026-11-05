# MCX — Multi Commodity Exchange of India Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.1%**, **12 months -1.6%** (rank 187 / 175 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +33.1%): 3 months 47%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.5% … P90 +4.8%; plausible 12m relative-return range incl. stock-specific noise: -45.2% … +41.6%
- Decomposition (12m): 0.5 × forward event exposure -2.3% (3m -0.9%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.1% (beta-adjusted) vs a realised market-adjusted move of +11.5% — gap -11.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| SEBI F&O / market-structure tightening (`P_SEBI_DERIVATIVES`) | +1 = tightening step | -5.91 | -5.00 | -0.93 | +0.00 | +0.02 | — |
| Competition in commodity derivatives (`NEW_COMMODITY_EXCHANGE_COMPETITION`) | +1 = credible entrant/launch capturing ~10% of bullion/energy options volume | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +2.39 | +2.00 | +0.36 | +0.13 | -0.11 | — |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +2.37 | +3.00 | -0.60 | -0.03 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +2.34 | +0.00 | +2.24 | +0.26 | -0.16 | — |
| Gold price (`F_GOLD`) | +8% gold (USD) | +2.10 | +1.50 | +0.60 | -0.00 | +0.00 | -8.4% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.69 | +1.50 | +0.37 | -0.18 | +0.00 | — |
| Silver price (`F_SILVER`) | +12% silver | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | -30.0% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +1.29 | +1.30 | +0.11 | -0.09 | -0.03 | +0.0% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.24 | +0.00 | -1.17 | -0.16 | +0.09 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.18 | +0.00 | -0.88 | -0.32 | +0.03 | +2.2% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.97 | +0.00 | -0.66 | -0.27 | -0.04 | +9.4% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.91 | -0.50 | -0.15 | -0.24 | -0.02 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +0.90 | +1.20 | -0.24 | -0.12 | +0.07 | -1.1% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -5.3% | -5.3% | -5.3 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.7% | -3.7% | -3.3 | -0.8 | +0.4 | +0.0 |
| SEBI partly reverses derivative expiry-settlement rule after closing-auction (CAS) volatility (`EV_SEBI_CAS_DERIV_REVERSAL`) | occurred | 1.00 | +2.6% | +2.6% | +2.6 | +0.0 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.4% | +2.2% | +4.0 | +0.9 | -0.5 | +0.0 |
| Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`) | risk_scenario | 0.30 | -5.8% | -1.8% | -5.8 | +0.0 | +0.0 | +0.0 |
| Gold/silver rebound as Fed hike fears fade or Iran war ends (`EV_PRECIOUS_METALS_REBOUND_H1_2027`) | anticipated | 0.45 | +3.7% | +1.7% | +3.8 | +0.0 | -0.0 | +0.0 |
| SEBI tightens F&O further (weekly-expiry scrapping, higher margins/lot sizes) (`EV_SEBI_FNO_CURBS_RISK`) | risk_scenario | 0.20 | -8.0% | -1.6% | -8.0 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -2.3% | -1.3% | -1.5 | -0.9 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.1 | -0.2 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.9 | -0.3 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.9% | +0.9% | +0.8 | +0.2 | -0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -3.7% | -0.9% | -1.2 | -1.8 | -0.9 | +0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MCX | +3.75% | +1.88% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → MCX | +2.25% | +1.01% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ P_SEBI_DERIVATIVES → MCX | -5.00% | -1.00% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → MCX | -1.69% | -0.93% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → MCX | -3.00% | -0.90% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MCX | -2.85% | -0.85% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MCX | +2.86% | +0.72% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → MCX | +1.50% | +0.68% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → MCX | +1.20% | +0.60% |
| 1 | EV_SEBI_FNO_CURBS_RISK ⇒ F_EQUITY_ACTIVITY_IN → MCX | -3.00% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MCX | -2.25% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MCX | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → MCX | -1.44% | -0.36% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → MCX | -1.25% | -0.31% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → MCX | +5.85% | +0.29% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_SILVER → MCX | -2.50 | observed | -3.74% |
| 1 | P_SEBI_DERIVATIVES → MCX | -0.50 | events | +2.50% |
| 1 | F_FPI_FLOWS → MCX | -1.60 | events | -2.40% |
| 1 | F_GOLD → MCX | -1.05 | observed | -1.57% |
| 1 | F_EQUITY_ACTIVITY_IN → MCX | +0.20 | events | +0.60% |
| 1 | F_GAS_GLOBAL → MCX | +1.00 | director_override | +0.50% |
| 1 | F_USDINR → MCX | -0.37 | observed | -0.44% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → MCX | +0.30 | events | +0.10% |
| 1 | F_COPPER → MCX | -0.24 | observed | -0.07% |
| 1 | F_RISK_SENTIMENT → MCX | +0.11 | observed | -0.06% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → MCX | +0.50 | events | -0.02% |
| 3 | F_REPO_IN → F_CREDIT_GROWTH_IN → P_RBI_PRUDENTIAL → MCX | +1.00 | events | +0.02% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | SEBI board meeting on derivatives (options structure, expiry rules) | regulatory | 0.30 | -3.5% | -1.05% |
| 2027-01 | Q3 FY27 results (Q2 declared 3 Nov 2026) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Launch of coal and minerals trading platforms after Rs 200 cr investment | capex | 0.40 | +1.5% | +0.60% |

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