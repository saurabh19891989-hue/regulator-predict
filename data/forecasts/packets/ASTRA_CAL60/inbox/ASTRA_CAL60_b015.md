# BLIND POINT-IN-TIME FORECASTING TASK
You are a professional regulatory forecaster. This file contains 12 independent forecasting snapshots about
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
## SNAPSHOT Sd96c6a19ab
CUTOFF DATE (today): 2024-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sa0107950c0
CUTOFF DATE (today): 2020-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Mitigation Strategies To Protect Food Against Intentional Adulteration
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S8ec7ac9d11
CUTOFF DATE (today): 2026-07-26
Regulator: SEBI (IN)
Matter: SEBI consultation: standardising the process for opening mutual fund folios and executing the first investment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S5743a3c426
CUTOFF DATE (today): 2022-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-01-13 | official-forward (B) | draft_guidance_availability_notice | "Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration S
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff." The FDA is issuing this draft guidance document to provide recommendations for 510(k) submissions for peripheral percutaneous transluminal angioplasty (PTA) balloons and specialty catheters (e.g., infusion catheters, PTA balloon catheters for in-stent restenosis (ISR), scoring/cutting balloons). This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT Sfc069bd052
CUTOFF DATE (today): 2021-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sc73bb3f04c
CUTOFF DATE (today): 2020-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S29fec09723
CUTOFF DATE (today): 2022-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Sponsor Responsibilities-Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/Bioequivalence Studies
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-06-28 | official-forward (B) | draft_guidance_availability_notice | "Sponsor Responsibilities-Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/Bioequivalence Studies; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Sponsor Responsibilities--Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/ Bioequivalence Studies." The draft gu
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Sponsor Responsibilities--Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/ Bioequivalence Studies." The draft guidance provides recommendations for sponsors and sponsor-investigators to comply with the requirements of investigational new drug application (IND) safety reporting and safety reporting for bioavailability (BA) and bioequivalence (BE) studies. In doing so, the guidance provides recommendations related to the two IND safety reporting provisions that require assessment of aggregate data to facilitate appropriate IND safety reporting practices. An earlier draft guidance for industry entitled "Safety Assessment for IND Safety Reporting" (December 2015) (the 2015 draft guidance) has been incorporated into this draft guidance. However, this content was revised to address feedback from stakeholders and comments received on the 2015 draft guidance. Concurrent with the publication of this draft guidance, we are withdrawing the 2015 draft guidance. Additionally, this draft guidance incorporates c
---
## SNAPSHOT Sdce7f746f5
CUTOFF DATE (today): 2021-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Instructions for Use-Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products-Content and Format
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S1078115b60
CUTOFF DATE (today): 2022-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S0b788adc50
CUTOFF DATE (today): 2021-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Biomarkers and Surrogate Endpoints in Clinical Studies To Support Effectiveness of New Animal Drugs
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S0d6bd4b5ed
CUTOFF DATE (today): 2026-06-26
Regulator: SEBI (IN)
Matter: SEBI consultation: enhancements to the Straight-Through Processing framework for institutional trade messaging
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S7da21a3e16
CUTOFF DATE (today): 2026-08-25
Regulator: SEBI (IN)
Matter: SEBI consultation: ease-of-doing-business modifications to master circular provisions on administration of stock exchanges
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.