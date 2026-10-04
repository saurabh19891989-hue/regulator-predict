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
## SNAPSHOT S2411a4e2c5
CUTOFF DATE (today): 2021-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Mitigation Strategies To Protect Food Against Intentional Adulteration
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sdca6d9ae65
CUTOFF DATE (today): 2020-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-09-23 | official-forward (B) | draft_guidance_availability_notice | "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations." The Patient Engagement Advisory Committee (PEAC) recommended that FDA and industry develop some typ
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations." The Patient Engagement Advisory Committee (PEAC) recommended that FDA and industry develop some type of framework to clarify how patient advisors can engage in the clinical investigation process. This draft guidance focuses on the applications, perceived barriers, and common challenges of patient engagement in the design and conduct of medical device clinical investigations. This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT S07fecfccad
CUTOFF DATE (today): 2026-01-01
Regulator: SEBI (IN)
Matter: SEBI consultation: standardising the process for opening mutual fund folios and executing the first investment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2025-10-23 | official-forward (B) | consultation_paper | "Consultation Paper on Standardisation of process for Opening of Mutual Fund Folios and Execution of First Investment" | www.sebi.gov.in
   Claims: Proposes that a new mutual fund folio's first transaction/investment be permitted only after KYC verification is completed by the KRA and the folio is marked KYC-compliant. / Notes current practice: AMCs conduct internal KYC checks and process the investment while simultaneously forwarding documents to the KRA, sometimes resulting in KYC non-compliant folios if the KRA, on review, finds deficiencies. / Describes resulting investor impediments, including inability to execute further transactions or receive redemption/dividend proceeds until KYC status is marked compliant in the KRA system.
   Excerpt: The objective of this consultation paper is to solicit comments on the proposed standardization of process for opening of Mutual Fund Folios and execution of first investment. It is proposed that first new folios be ascertained to be fully Know Your Client (KYC) compliant both at the Asset Management Company (AMC) level as well as in the KYC Registration Agency (KRA) system. Investors may commence transactions or investments once the KYC verification is successfully completed by the KRA and the folio is accordingly marked as KYC compliant.
---
## SNAPSHOT S7aadc22a74
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.