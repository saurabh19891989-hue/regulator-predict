# BLIND POINT-IN-TIME FORECASTING TASK
You are a professional regulatory forecaster. This file contains 4 independent forecasting snapshots about
DIFFERENT regulatory matters. Treat each snapshot on its own; do not carry information between snapshots.

Rules:
1. For each snapshot, "today" is its CUTOFF DATE. Use only the evidence shown plus general knowledge of how the
   regulatory process usually behaves (base rates, typical durations). Do not use any world-state fact learned after
   the cutoff: later election results, leadership changes, court rulings, agency decisions, dates or outcomes are
   unknown, even if you remember them. A future event stated in cutoff-valid evidence may be considered only as an
   uncertain plan or possibility, never as a later-known result. Every factual driver in "notes" or "scenarios" must
   be supported by the shown evidence or be a general process base rate.
2. Do NOT use any specific memory of what happened to this particular matter after the cutoff. If you recognise the
   matter and believe you know its later outcome, set "recognised_outcome": true and forecast from cutoff-valid
   evidence only. Never state or hint at the remembered result.
3. The evidence shown may be only a subset of what was public; do not infer anything from the absence of a
   document type. Some snapshots show no documents at all — then forecast from title, regulator, process and date.
4. "Decisive action" is defined per snapshot. Probabilities in "p" are CUMULATIVE: probability the decisive action
   is published within 7/30/60/90/180 days AFTER the cutoff (non-decreasing; "180d" is the headline action
   probability). Delays, stalls, withdrawals and no-action outcomes are common in regulation: be calibrated, use
   the full 0–1 range when evidence warrants, and do not default to 0.5.
5. "next": the NEXT official step within 180 days (mutually exclusive, sums to 1): final_action,
   revised_or_further_consultation (revised draft, supplemental proposal, extended/reopened comment period,
   further consultation or hearing), formal_withdrawal, no_further_official_step.
6. "content": CONDITIONAL on the decisive action happening, its form relative to the most recent proposal visible
   (sums to 1): as_proposed (substantially as proposed), softened (narrower scope, lower stringency, higher
   thresholds, longer transition, carve-outs), tightened, mixed (some softened, some tightened),
   different_mechanism.
7. "scenarios": up to 3 concrete policy-content scenarios CONDITIONAL on action (probabilities sum ≤ 1), each with
   a short mechanism and, where the evidence has numbers (thresholds, rates, dates, amounts), predicted
   parameter ranges. Cite evidence labels (E1, E2 …) that support/contradict it.
8. If the evidence is too thin to forecast meaningfully, set "insufficient_evidence": true but still give your best
   base-rate probabilities.

OUTPUT: read the output file named in your instructions (it contains a placeholder) and replace its ENTIRE content
with ONE JSON object of exactly this shape (no comments, no trailing text):
{"forecasts": [
  {"id": "<snapshot id>",
   "p": {"7d": 0.00, "30d": 0.00, "60d": 0.00, "90d": 0.00, "180d": 0.00},
   "next": {"final_action": 0.00, "revised_or_further_consultation": 0.00, "formal_withdrawal": 0.00, "no_further_official_step": 0.00},
   "content": {"as_proposed": 0.00, "softened": 0.00, "tightened": 0.00, "mixed": 0.00, "different_mechanism": 0.00},
   "scenarios": [{"s": "short label", "p": 0.00, "mech": "mechanism, <=25 words", "params": {"parameter": "predicted range"}, "ev": ["E1"], "contra": []}],
   "notes": "<=40 words: main drivers of your forecast",
   "missing": ["<=3 items of missing information that would most change the forecast"],
   "recognised_outcome": false,
   "insufficient_evidence": false}
]}
One entry per snapshot, in any order, using the exact snapshot ids below.

---
## SNAPSHOT S6d81816d50
CUTOFF DATE (today): 2020-10-03
Regulator: a US federal regulator (identity withheld)
Matter: Developing locally applied steroid treatments for hemorrhoid symptoms
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-12-06 | official-forward (B) | draft_guidance_availability_notice | [TITLE WITHHELD] | 
   Claims: the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry entitled [TITLE WITHHELD] This draft guidance will serv
   Excerpt: the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry entitled [TITLE WITHHELD] This draft guidance will serve as a focus for continued discussions among the a specialist division, pharmaceutical sponsors, the academic community, and the public.
---
## SNAPSHOT S0efb3316dd
CUTOFF DATE (today): 2023-07-19
Regulator: an Indian regulator (identity withheld)
Matter: Charges for breaches of loan terms
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (2 item(s), chronological):
[E1] 2023-02-08 | official-soft (C) | official_statement | [TITLE WITHHELD] | 
   Claims: the Regulator announced a review of penal-interest practices, citing supervisory findings of divergent, sometimes excessive, penal-interest levies and proposing a 'penal charges' framework -- draft guidelines said to follow shortly, two months ahead of this thread's anchor draft.
   Excerpt: II. Regulation 2. Recovery of Penal Charges on Loans In terms of extant guidelines, Regulated Entities (REs) have the operational autonomy to formulate Board approved policy for levy of penal interest on advances which shall be fair and transparent. The intent of penal interest was essentially to inculcate a sense of credit discipline among borrowers through negative incentives but such charges are not meant to be used as a revenue enhancement tool over and above the contracted rate of interest. Supervisory reviews have indicated divergent practices amongst REs with regard to levy of penal interest which were excessive in certain cases, leading to customer grievances and disputes. It has been decided that any penalty for delay/default in servicing of the loan or any other non-compliance of material terms and conditions of loan contract by the borrower shall be in the form of 'penal charges' in a reasonable and transparent manner and shall not be levied in the form of 'penal interest'. Draft guidelines to the above effect shall be placed on the Regulator website shortly, for comments from stakeholders.
[E2] 2023-04-12 | official-forward (B) | draft_circular | [TITLE WITHHELD] | 
   Claims: the Regulator released the draft on charges for breaches of loan terms on April 12, 2023, following its February 8, 2023 policy statement. / Comments on that draft were invited by May 15, 2023.
   Excerpt: [document title withheld]. In pursuance of the announcement made in the [policy statement] dated February 08, 2023 regarding the review of extant regulatory guidelines on levy of penal interest, the Regulator has released today the draft on charges for breaches of loan terms. Comments by stakeholders on the Draft Circular may be submitted by May 15, 2023. [release identifier withheld].
---
## SNAPSHOT S09e17ab563
CUTOFF DATE (today): 2025-02-07
Regulator: an Indian regulator (identity withheld)
Matter: Comparison and display of loan offers from multiple lenders
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (2 item(s), chronological):
[E1] 2023-12-08 | official-soft (C) | official_statement | [TITLE WITHHELD] | 
   Claims: the Regulator announced, following a Working Group on Digital Lending recommendation accepted August 10, 2022, that it would bring loan aggregation services by LSPs under a regulatory framework focused on transparency and customer centricity.
   Excerpt: 3. framework for comparing loan offers from multiple lenders the Regulator had accepted, vide its Press Release dated August 10, 2022, the recommendation of the Working Group on Digital Lending (Chairman: [person withheld]) to come up with a regulatory framework for web-aggregators of loan products (WALP). WALP entails aggregation of loan offers from multiple lenders on an electronic platform which enables the borrowers to compare and choose the best available option to avail loan from one of the available lenders. Based on the recommendation of the Working Group, it has been decided to bring such loan aggregation services offered by the Lending Service Providers (LSPs) under a comprehensive regulatory framework. The framework will focus on enhancing the transparency in the operations of WALPs, increase customer centricity and enable the borrowers to make informed choices. The detailed guidelines will be issued separately.
[E2] 2024-04-26 | official-forward (B) | draft_circular | [TITLE WITHHELD] | 
   Claims: In pursuance of the [policy statement] dated December 8, 2023, the Regulator placed a draft circular on loan aggregation transparency draft. / Addresses issuance of a regulatory framework for aggregation of loan products by Lending Service Providers (LSPs). / Comments invited by May 31, 2024.
   Excerpt: In pursuance of the announcement made in the [policy statement] dated December 08, 2023 regarding issuance of a regulatory framework for aggregation of loan products by lending service providers (LSPs), the Regulator has today placed on its website the Draft Circular on 'loan aggregation transparency draft'. Comments/feedback, if any, may be sent by e-mail with the subject line [TITLE WITHHELD], by May 31, 2024.
---
## SNAPSHOT S90f1844b45
CUTOFF DATE (today): 2021-06-13
Regulator: a US federal regulator (identity withheld)
Matter: Reliability testing for emergency injection devices
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-04-21 | official-forward (B) | draft_guidance_availability_notice | [TITLE WITHHELD] | 
   Claims: the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry and the Regulator entitled [TITLE WITHHELD] For injectable drug or biological products that a
   Excerpt: the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry and the Regulator entitled [TITLE WITHHELD] For injectable drug or biological products that are intended to treat emergent, life- threatening conditions, it is essential to ensure that the emergency- use injector will reliably deliver the drug or biological product as intended. This is particularly critical for drugs when failure of the injector may prevent adequate delivery of a life-saving drug to a patient. The draft guidance describes the technical considerations for demonstrating reliability of emergency-use injectors under a biologics license application (BLA), new drug application (NDA), or abbreviated new drug application (ANDA).