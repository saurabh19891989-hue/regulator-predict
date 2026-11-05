# Robustness of the rankings (analysis date 2026-11-05)

Each row changes one arbitrary modelling choice and compares the resulting ranking with the baseline. Spearman = rank correlation of expected relative returns across 200 stocks; overlaps count shared names in the top or bottom 20. 'Without …' rows remove one source of expected return using the exact attribution.

Note: the forward-event 'priced share' multiplies every forward exposure equally, so it changes the size of the expected returns but not the ranking; it is therefore not listed. Company catalysts are varied separately.

| variant | 12m Spearman | 3m Spearman | top-20 overlap (12m) | bottom-20 overlap (12m) | base top-10 still top-20 | spread (sd, 12m) |
|---|---|---|---|---|---|---|
| Company catalysts weighted 0.25 (vs 0.5) | 0.96 | 0.96 | 18/20 | 17/20 | 10/10 | 1.17 |
| Company catalysts weighted 0.75 (vs 0.5) | 0.99 | 0.98 | 19/20 | 16/20 | 10/10 | 1.65 |
| No company catalysts | 0.80 | 0.65 | 16/20 | 15/20 | 9/10 | 1.04 |
| Higher-order damping ×0.8 | 0.99 | 1.00 | 18/20 | 18/20 | 10/10 | 1.38 |
| Higher-order damping ×1.2 | 0.99 | 1.00 | 19/20 | 19/20 | 10/10 | 1.40 |
| Overlap damping 0.25 (vs 0.5) | 0.99 | 1.00 | 19/20 | 20/20 | 10/10 | 1.38 |
| Overlap damping 0.75 (vs 0.5) | 0.99 | 1.00 | 19/20 | 20/20 | 10/10 | 1.40 |
| 1st order only (depth 1) | 0.86 | 0.92 | 17/20 | 13/20 | 10/10 | 1.49 |
| Up to 2nd order (depth 2) | 0.93 | 0.96 | 18/20 | 16/20 | 10/10 | 1.45 |
| Up to 3rd order (depth 3) | 0.99 | 1.00 | 19/20 | 18/20 | 10/10 | 1.39 |
| No market-priced neutralisation | 0.68 | 0.67 | 10/20 | 10/20 | 7/10 | 1.88 |
| No beta adjustment | 0.99 | 0.99 | 19/20 | 17/20 | 10/10 | 1.41 |
| Edge weights ×lognormal(0.3), seed 1 | 0.97 | 0.98 | 18/20 | 18/20 | 10/10 | 1.46 |
| Edge weights ×lognormal(0.3), seed 2 | 0.97 | 0.98 | 16/20 | 18/20 | 10/10 | 1.35 |
| Edge weights ×lognormal(0.3), seed 3 | 0.97 | 0.97 | 18/20 | 17/20 | 10/10 | 1.44 |
| Event probabilities ×U(0.7,1.3), seed 1 | 0.99 | 0.99 | 19/20 | 18/20 | 10/10 | 1.35 |
| Event probabilities ×U(0.7,1.3), seed 2 | 0.99 | 0.99 | 18/20 | 19/20 | 10/10 | 1.36 |
| Event probabilities ×U(0.7,1.3), seed 3 | 0.99 | 0.99 | 18/20 | 18/20 | 10/10 | 1.44 |
| Without policy | 0.94 | 0.95 | 15/20 | 16/20 | 10/10 | 1.21 |
| Without regulatory | 0.97 | 0.99 | 19/20 | 17/20 | 10/10 | 1.33 |
| Without sector | 0.89 | 0.89 | 12/20 | 14/20 | 6/10 | 1.14 |
| Without theme | 0.97 | 0.92 | 17/20 | 17/20 | 8/10 | 1.30 |
| Without geopolitics | 1.00 | 0.99 | 19/20 | 19/20 | 10/10 | 1.36 |
| Without company catalysts | 0.80 | 0.65 | 16/20 | 15/20 | 9/10 | 1.04 |

## Most stable names (in the top or bottom 20 in at least 80% of re-run variants)
- Top: IDEA, HINDPETRO, BHARTIARTL, IOC, LAURUSLABS, MAZDOCK, DIXON, JSWENERGY, TATAPOWER, BDL, ADANIPOWER, ENRIN, POWERINDIA, RELIANCE, SOLARINDS, ADANIENSOL, NLCINDIA, NHPC
- Bottom: MCX, MFSL, INFY, COFORGE, TCS, MPHASIS, SWIGGY, MUTHOOTFIN, BIOCON, ETERNAL, PERSISTENT, FORTIS, GROWW, HINDCOPPER, POLICYBZR

## Reading
- Edge-weight and probability noise test whether the ranking depends on precise numbers the agents could not know; depth variants show how much the 2nd–4th-order links change the answer; 'without …' rows show which source of expected return drives the ranking.
- Per-stock best, worst and median rank across variants: `results/robustness_ranks.csv`.
