# CLAUDE.md — Regulatory Predictive Precursor Engine

## North Star
Determine whether future regulatory actions can be predicted from information available *before* the decisive regulatory document, and quantify how early and how accurately.

This project is NOT a stock-prediction, options, valuation, or trading project. Those are downstream and out of scope until predictive regulatory signal is proven.

## Primary Questions
1. Can we predict that a material regulatory action will occur?
2. Can we predict the next procedural step?
3. Can we predict when it will occur?
4. Can we predict the likely policy mechanism/content?
5. Which precursor classes add genuine out-of-sample predictive value?
6. How much lead time is gained before the decisive document?

## Evidence Hierarchy
- Tier B: official forward/predictive material — agendas, planned reviews, discussion papers, consultation papers, draft rules, exposure drafts, calls for evidence, hearings, public-comment deadlines, committee/working-group material.
- Tier C: official soft signals — speeches, minutes, workplans, FAQs, staff papers, supervisory letters, official interviews/research.
- Tier D: reputable contemporaneous reporting — lead generation/corroboration only.
- Tier A: final rules/actions — outcome label only during backtesting; never visible to a historical forecaster before the cutoff.

## Core Method
Reconstruct historical regulatory threads point-in-time. At frozen cutoffs T-180, T-120, T-90, T-60, T-30, T-14, and T-7 (where evidence exists), provide the forecaster ONLY material published on or before the cutoff. Produce structured predictions, freeze them, then compare them with the actual outcome.

Run ablations:
A. Tier B only
B. Tier C only
C. Tier B + C
D. B + C + stakeholder comments/responses
E. B + C + stakeholder responses + reputable contemporaneous news
F. Latest-document-only vs full historical trajectory

## Non-Negotiable Methodological Rules
- No hindsight leakage.
- Do not select only famous rules that happened. Include stalled, withdrawn, delayed, softened, and no-action threads.
- Preserve original publication dates and document versions where possible.
- Never silently use current/revised regulator pages as historical evidence.
- Record uncertainty and missing evidence explicitly.
- Every evidence item requires URL/source, publication date, retrieval date, regulator, document type, and evidence tier.
- Every prediction is append-only and timestamped.
- No prediction may be rewritten after seeing the outcome.
- Separate action probability, timing probability, policy-content probability, and no-action/delay probability.
- Do not optimize for a headline accuracy number. Optimize for calibration, precision/recall, content accuracy, and lead time.
- If the evidence is insufficient, say so rather than manufacture a prediction.

## Autonomy
Operate autonomously toward the North Star. Do not ask the user what to do next for routine choices. Make reversible engineering/research decisions yourself, document them, and continue.

Escalate to the user only when:
1. a credential, paid account, CAPTCHA, legal/terms decision, or external permission is required;
2. two materially different methodological choices would change the scientific conclusion and cannot be tested in parallel;
3. a spend cap would be exceeded;
4. the project reaches a formal GO/NO-GO gate;
5. an irreversible/destructive action is required.

When blocked on one workstream, continue independent workstreams.

## Agent Hierarchy
### Director
Owns methodology, priority, spend, quality gates, and final synthesis. Does not do bulk extraction.

### Research Managers
Own regulator-specific workstreams and validate executor outputs before they enter the GOLD dataset.

### Executors
Discover events, reconstruct timelines, fetch primary documents, classify evidence, and populate schemas.

### Blind Forecasters
See only cutoff-valid evidence. They must never see outcome fields.

### Red-Team / Leakage Auditors
Attempt to invalidate timelines and forecasts by finding future leakage, revised pages, selection bias, duplicated evidence, or retrospective wording.

### Evaluator
Sees frozen predictions and outcomes, computes metrics, ablations, calibration, and lead-time distributions.

## Delegation Rule
Use subagents only when tasks can run in parallel, require isolated context, or benefit from independent verification. Do not spawn subagents for trivial single-file edits or sequential steps.

## Model Routing
Default:
- Director: Claude Opus 5.5, medium effort; high for methodological gates.
- Research managers: Opus 5.5 medium.
- Executors / document reconstruction: Claude Sonnet 5 medium; high for ambiguous timelines.
- Bulk parsing/classification: Sonnet 5 low/medium.
- Blind forecaster: Opus 5.5 medium/high.
- Red-team/leakage audit: Opus 5.5 high.
- Hardest 5–10 disputed cases only: Claude Fable 5.1 high, if budget remains.

Do not use Fable 5.1 for bulk work.

## Spend Discipline
Initial Anthropic budget cap: USD 100.
Target allocation:
- 50–60% Sonnet 5 bulk research/reconstruction
- 30–40% Opus 5.5 directing, forecasting, auditing
- <=10% Fable 5.1 adjudication, only if needed

Exploit prompt caching for this constitution and other shared project documents. Track estimated and actual spend in PROJECT_STATUS.md.

## Today’s Deliverable
Produce a same-day RAPID backtest and, in parallel, a smaller audited GOLD set.

Target:
- 150–250 candidate event threads discovered
- 100–200 usable RAPID threads if source availability permits
- 30–50 GOLD threads with stronger point-in-time verification
- both positive and negative/stalled controls
- Tier B/C ablation results
- lead-time results
- leakage audit
- clear empirical answer to whether predictive signal exists

Quantity is secondary to validity. Do not force 200 events by relaxing evidence standards.

## GO / NO-GO Gate
Before building any stock, options, valuation, or trading layer, answer:
- Is action prediction better than meaningful baselines?
- Is timing calibrated enough to be useful?
- Is policy-content prediction meaningfully above naive/base-rate guesses?
- Which evidence classes add incremental predictive value?
- What median lead time is achieved at acceptable precision?
- Do results survive negative controls and leakage review?

If not, stop and report why. Do not rationalize failure into a larger architecture.

## Persistent Project Memory
At the end of every major ticket or work session:
1. update PROJECT_STATUS.md;
2. record decisions and rationale;
3. record completed/failed tickets;
4. record dataset counts and metrics;
5. record unresolved risks;
6. set explicit next actions;
7. ensure another agent can resume solely from repository documents.

Never rely on chat history as project memory.
