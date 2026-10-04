# Evaluation gate review — 2026-10-04

Scope: bounded, read-only review of the frozen preregistration, deviations, scaling plan, and current baseline/evaluator code before SEBI-R and FDA-H scaled scoring. No thresholds, forecasts, or canonical sources were changed here.

## Scoring repairs made before scaled evaluation

1. **G4 and primary comparator frame:** The root agent restricted Design-T precision to `k <= 180`, restored frozen thresholds 0.5/0.7/0.8, and restricted baseline training IDs to primary-arm precursor-population threads. These repairs were reviewed but not edited in this subtask.
2. **Declared logistic feature:** `rpe/baselines.py` now extracts `comment_deadline_passed` only from a visible Tier B/C item carrying a structured ISO `comment_deadline` or a clearly labelled ISO deadline in its excerpt. Later official extensions supersede earlier deadlines; invalid or prepublication dates are ignored. The feature enters the logistic vector. The fixed numerical heuristic is unchanged; its description is broader than its actual recency/stage rules. This extractor needs a dated protocol-deviation entry because it was implemented after diagnostic results.
3. **Gate slices:** `rpe/evaluate.py` now emits HIST-matched same-model TITLE_ONLY pairs, LATE C/T action blocks, RAPID/GOLD × HIST/LATE × C/T action blocks, pooled 30/90/180-day timing, self-recognition-excluded C/T strata, and a structured numeric gate-input summary with ±0.05 sensitivity checks where possible. Direction content adds an explicit majority-class rate. No threshold was changed.

## Gates that remain unassessed

- Blinded GOLD/LATE mechanism accuracy for G3 has no supplied judgment data.
- G5's audited-snapshot contamination numerator/denominator is outside the scored index; canonical build removes contaminated threads. Complete audit provenance and any exclusion sensitivity must be supplied separately. Zero or very small GOLD remains untested robustness.
- `gate_assessment` therefore never asserts GO from partial numeric checks. It reports available G1/G2/G4 checks and G5 subgroup inputs, preserving unassessed status for G3/G5 and the overall decision.

Focused verification: `.venv/Scripts/python.exe -m pytest -q tests/test_gate_inputs_20261004.py tests/test_evaluation_cohort.py` → **9 passed**. System Python lacked `jsonschema`; the project `.venv` was used. No scaled forecast results were used to tune this extractor or any threshold.

## Source and grouping check

`rpe/build.py` excludes low-confidence outcomes and `contaminated_exclude` whole-thread audits from canonical data, while `rpe/snapshots.py` uses only cutoff-visible evidence and censors horizons past 2026-09-24. `paired_arms` now keys by matter, cutoff, design, and model and rejects duplicate selected runs. These guards looked consistent with the stated plan; no additional source-leakage implementation blocker was identified in this bounded review. The complete SEBI-R then FDA-H source audits and a new frozen dataset/index remain prerequisites from `docs/SCALING_PLAN_20261004.md`.
