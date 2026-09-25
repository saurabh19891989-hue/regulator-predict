# BACKTEST_PROTOCOL.md — Frozen Point-in-Time Regulatory Forecasting

## Purpose
Measure whether regulatory actions and policy contents could have been predicted using only information genuinely available before the outcome.

## Unit of Analysis
One `regulatory_thread`, representing a coherent policy issue through time.

## Thread Outcome Classes
At minimum:
- material action/final rule;
- draft/consultation but no final action within evaluation horizon;
- delayed/postponed;
- withdrawn/abandoned;
- materially softened;
- materially tightened;
- still unresolved at censoring date.

## Sampling
Do not build the sample by searching only for final rules.

Construct it from historical precursor populations where feasible:
- consultations;
- discussion papers;
- board agendas;
- working groups;
- planned reviews;
- speeches/workplans that announced or strongly implied review;
- public dockets;
- regulatory calendars.

Include at least ~30% negative/stalled/altered controls in the RAPID sample unless regulator-specific source availability makes this impossible; report the actual ratio.

## Frozen Cutoffs
Where evidence exists, create snapshots at:
T-180, T-120, T-90, T-60, T-30, T-14, T-7.

Do not fabricate empty cutoffs. A snapshot is valid only if contemporaneous evidence exists.

## Evidence Record
Each item must contain:
- evidence_id
- regulator
- jurisdiction
- thread_id
- title
- source_url
- publication_date
- first_known_date if different
- retrieval_date
- document_type
- tier (B/C/D; Tier A only in outcome store)
- original_or_revised status
- archive/version confidence
- extracted claims
- source hash or stored copy where permitted

## Forecaster Isolation
The blind forecaster receives:
- thread title phrased neutrally;
- cutoff date;
- evidence published on/before cutoff;
- regulator/process metadata available at cutoff.

It must NOT receive:
- final outcome;
- future document titles;
- future dates;
- retrospective articles;
- post-outcome summaries;
- labels derived from the outcome.

## Required Forecast Schema
{
  "thread_id": "",
  "cutoff_date": "",
  "action_probability_180d": 0.0,
  "timing": {
    "7d": 0.0,
    "30d": 0.0,
    "60d": 0.0,
    "90d": 0.0,
    "180d": 0.0
  },
  "next_step_probabilities": {},
  "policy_scenarios": [
    {
      "scenario": "",
      "probability": 0.0,
      "mechanism": "",
      "parameter_ranges": {},
      "supporting_evidence_ids": [],
      "contrary_evidence_ids": []
    }
  ],
  "delay_or_no_action_probability": 0.0,
  "confidence_notes": "",
  "missing_information": []
}

Probabilities must be coherent and normalized where mutually exclusive.

## Ablation Runs
For each eligible snapshot run:
- B_ONLY
- C_ONLY
- B_PLUS_C
- B_C_STAKEHOLDERS
- B_C_STAKEHOLDERS_PLUS_NEWS
- LATEST_DOCUMENT_ONLY
- FULL_TRAJECTORY

If a required evidence class is absent, mark that ablation unavailable instead of inventing inputs.

## Baselines
At minimum compare against:
1. regulator historical base rate at the observed process stage;
2. naive stage-transition baseline;
3. simple recency/deadline heuristic;
4. where possible, no-LLM feature model.

A model beating a straw-man baseline is not sufficient.

## Metrics
Action:
- Brier score
- log loss
- calibration curve
- precision/recall at declared probability thresholds
- AUROC/AUPRC where class balance permits

Timing:
- probability calibration by horizon
- median/mean timing error
- survival/hazard calibration where feasible

Content:
- top-1/top-k scenario accuracy
- semantic/mechanism accuracy
- parameter-range coverage
- severity-direction accuracy

Lead time:
- earliest cutoff reaching >=50%, >=70%, >=80% action probability
- lead time at accepted precision levels
- median lead time by precursor class and regulator

Ablation:
- incremental change in Brier/log loss/calibration and lead time when adding C, stakeholder responses, news, or full trajectory.

## Leakage Audit
Red-team every GOLD thread and a risk-weighted sample of RAPID threads.

Check:
- modified current pages masquerading as historical pages;
- revised/replaced PDFs;
- publication timestamps added later;
- post-outcome snippets in search results;
- archive timestamps;
- documents explicitly referring to future material unavailable at cutoff;
- model/system prompt containing the outcome;
- thread name giving away the outcome.

Any contaminated snapshot is excluded or rebuilt.

## RAPID vs GOLD
RAPID:
- broad;
- same-day;
- reasonable timestamp verification;
- intended to estimate whether a large signal exists.

GOLD:
- smaller;
- archived/original documents where possible;
- stronger version validation;
- independent leakage review;
- intended to test whether the signal survives scientific scrutiny.

Never combine RAPID and GOLD quality labels silently.

## Stop / Go Criteria
Stop expansion and report if:
- usable point-in-time reconstruction is systematically impossible;
- predictive performance is indistinguishable from strong baselines;
- apparent gains vanish after leakage controls;
- only post-consultation/final-draft stages are predictable with negligible lead time.

Proceed to live precursor monitoring if:
- predictive lift is reproducible across multiple regulators;
- calibration is acceptable;
- useful lead time exists;
- incremental value of specific precursor classes is identifiable;
- results survive GOLD leakage review.

Do not define numeric GO thresholds after seeing results. The Director should freeze threshold bands before final evaluation or report sensitivity over plausible thresholds.
