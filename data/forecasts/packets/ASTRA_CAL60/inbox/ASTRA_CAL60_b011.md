# BLIND POINT-IN-TIME FORECASTING TASK
You are a professional regulatory forecaster. This file contains 20 independent forecasting snapshots about
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
## SNAPSHOT S58e604a0f8
CUTOFF DATE (today): 2021-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sab984e9981
CUTOFF DATE (today): 2021-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-08-31 | official-forward (B) | draft_guidance_availability_notice | "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakehol" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and integration of patient perspectives in the development, evaluation, and surveillance of medical devices, including digital health technologies. Patient-reported outcome (PRO) instruments facilitate the systematic collection of patient perspectives as scientific evidence to support the regulatory and healthcare decision-making process. This draft guidance describes principles that should be considered when using PRO instruments in the evaluation of medical devices and provides recommendations about the importance of ensuring the measures are "fit-for-purpose." This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT S18100606aa
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-08-11 | official-forward (B) | draft_guidance_availability_notice | "International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1); Draft Guidance f" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the Int
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products (VICH). This revision clarifies the definition of adequate infection in individual animals, updates considerations for field studies, and makes additional clarifying changes.
---
## SNAPSHOT S6a0103f548
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Charging for Investigational Drugs Under an Investigational New Drug Application: Questions and Answers
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-08-23 | official-forward (B) | draft_guidance_availability_notice | "Charging for Investigational Drugs Under an Investigational New Drug Application: Questions and Answers; Revised Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance for industry entitled "Charging for Investigational Drugs Under an IND: Questions and Answers." Since issuance of the final guidance in 2016, FDA has received questions from stakeholders throu
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance for industry entitled "Charging for Investigational Drugs Under an IND: Questions and Answers." Since issuance of the final guidance in 2016, FDA has received questions from stakeholders through the docket and in the form of communications with review divisions. These questions relate to the implementation of FDA's regulation on charging for investigational drugs under an investigational new drug application (IND) for the purpose of either clinical trials or expanded access for treatment use. FDA is providing this revised draft guidance in a question-and-answer format, addressing the most recently asked questions. When finalized, this revised draft guidance will replace the final guidance of the same title issued in June 2016.
---
## SNAPSHOT Sc4b916b289
CUTOFF DATE (today): 2026-07-26
Regulator: SEBI (IN)
Matter: SEBI consultation: harmonizing base price for pre-open call auction and price bands for stocks listed on multiple exchanges
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT Se57da07c52
CUTOFF DATE (today): 2020-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-09-23 | official-forward (B) | draft_guidance_availability_notice | "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations." The Patient Engagement Advisory Committee (PEAC) recommended that FDA and industry develop some typ
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations." The Patient Engagement Advisory Committee (PEAC) recommended that FDA and industry develop some type of framework to clarify how patient advisors can engage in the clinical investigation process. This draft guidance focuses on the applications, perceived barriers, and common challenges of patient engagement in the design and conduct of medical device clinical investigations. This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT S4dab5dc115
CUTOFF DATE (today): 2026-08-25
Regulator: SEBI (IN)
Matter: SEBI consultation: standardising the process for opening mutual fund folios and executing the first investment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2025-10-23 | official-forward (B) | consultation_paper | "Consultation Paper on Standardisation of process for Opening of Mutual Fund Folios and Execution of First Investment" | www.sebi.gov.in
   Claims: Proposes that a new mutual fund folio's first transaction/investment be permitted only after KYC verification is completed by the KRA and the folio is marked KYC-compliant. / Notes current practice: AMCs conduct internal KYC checks and process the investment while simultaneously forwarding documents to the KRA, sometimes resulting in KYC non-compliant folios if the KRA, on review, finds deficiencies. / Describes resulting investor impediments, including inability to execute further transactions or receive redemption/dividend proceeds until KYC status is marked compliant in the KRA system.
   Excerpt: The objective of this consultation paper is to solicit comments on the proposed standardization of process for opening of Mutual Fund Folios and execution of first investment. It is proposed that first new folios be ascertained to be fully Know Your Client (KYC) compliant both at the Asset Management Company (AMC) level as well as in the KYC Registration Agency (KRA) system. Investors may commence transactions or investments once the KYC verification is successfully completed by the KRA and the folio is accordingly marked as KYC compliant.
---
## SNAPSHOT S462ce63c73
CUTOFF DATE (today): 2022-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Mitigation Strategies To Protect Food Against Intentional Adulteration
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-02-13 | official-forward (B) | draft_guidance_availability_notice | "Mitigation Strategies To Protect Food Against Intentional Adulteration; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA, we, or Agency) is announcing the availability of a supplemental draft guidance for industry entitled "Mitigation Strategies to Protect Food Against Intentional Adulteration: Guidance for Industry." This supplemental draft guidance document, when finalized, will
   Excerpt: The Food and Drug Administration (FDA, we, or Agency) is announcing the availability of a supplemental draft guidance for industry entitled "Mitigation Strategies to Protect Food Against Intentional Adulteration: Guidance for Industry." This supplemental draft guidance document, when finalized, will help food facilities that manufacture, process, pack, or hold food, and that are required to register under the Federal Food, Drug, and Cosmetic Act (FD&C Act) comply with the requirements of our regulation entitled "Mitigation Strategies to Protect Food Against Intentional Adulteration."
---
## SNAPSHOT Sde7308fc02
CUTOFF DATE (today): 2026-07-26
Regulator: SEBI (IN)
Matter: SEBI consultation: framework for an IT Resilience Index for market infrastructure institutions
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-03-25 | official-forward (B) | consultation_paper | "Consultation Paper on Framework of IT Resilience Index for Market Infrastructure Institutions (MIIs)" | www.sebi.gov.in
   Claims: Proposes creation of an 'IT Resilience Index' (ITRI) for market infrastructure institutions, computed periodically on a pre-decided set of parameters. / States the objective is to let MIIs compare the health/efficacy of their IT systems over time and to create a uniform set of metrics and weights to compare ITRI across MIIs. / Notes MIIs had already built a working model of the index, discussed in meetings of SEBI's Technical Advisory Committee (TAC).
   Excerpt: The objective of the consultation paper is to seek views on creation of IT Resilience Index (ITRI) for MIIs that would be computed periodically on a pre-decided set of parameters and which would provide insights to the MII on health of its IT systems across various dimensions. Based on the discussions with MIIs, an initial framework of ITRI for MIIs was formulated. The MIIs have implemented a working model of such index and the results were subsequently discussed in various meetings of SEBI's Technical Advisory Committee (TAC).
---
## SNAPSHOT S0f962eab29
CUTOFF DATE (today): 2023-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S35d1afd0f7
CUTOFF DATE (today): 2020-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-08-01 | official-forward (B) | draft_guidance_availability_notice | "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products." This draft guidance is intended to assist sponsors of new drug applications
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products." This draft guidance is intended to assist sponsors of new drug applications (NDAs), biologics license applications (BLAs) for therapeutic biologics, and supplements who are planning to conduct clinical studies in neonatal populations. The issuance of this draft guidance on clinical pharmacology considerations for neonatal studies for drugs and biological products is stipulated under the FDA Reauthorization Act of 2017 (FDARA).
---
## SNAPSHOT S8c471bd62e
CUTOFF DATE (today): 2022-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Donor Eligibility for Animal Cells, Tissues, and Cell- and Tissue-Based Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sea0775a9f3
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Voluntary Malfunction Summary Reporting Program for Manufacturers
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sfc3de432c1
CUTOFF DATE (today): 2021-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-01-13 | official-forward (B) | draft_guidance_availability_notice | "Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration S
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff." The FDA is issuing this draft guidance document to provide recommendations for 510(k) submissions for peripheral percutaneous transluminal angioplasty (PTA) balloons and specialty catheters (e.g., infusion catheters, PTA balloon catheters for in-stent restenosis (ISR), scoring/cutting balloons). This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT Sa746a2a3e4
CUTOFF DATE (today): 2021-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Drug Products Labeled as Homeopathic
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (2 item(s), chronological):
[E1] 2019-10-24 | official-forward (B) | draft_guidance_availability_notice | "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance for FDA staff and industry entitled "Drug Products Labeled as Homeopathic." The revised draft guidance, like the original version, describes how FDA intends to prioritize enforcement and regul
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance for FDA staff and industry entitled "Drug Products Labeled as Homeopathic." The revised draft guidance, like the original version, describes how FDA intends to prioritize enforcement and regulatory action with regard to drug products, including biological products, labeled as homeopathic and marketed in the United States without the required FDA approval that potentially pose higher risk to public health. In response to comments received, we have revised the draft guidance and are reissuing it in draft form to enable the public to review and comment before it is finalized.
[E2] 2020-03-13 | official-forward (B) | comment_period_extension_notice | "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry; Extension of Comment Period" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is extending the comment period for the notice entitled "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry" that appeared in the Federal Register of October 25, 2019. The Agency is taking this act
   Excerpt: The Food and Drug Administration (FDA or Agency) is extending the comment period for the notice entitled "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry" that appeared in the Federal Register of October 25, 2019. The Agency is taking this action to allow interested persons additional time to submit comments.
---
## SNAPSHOT S65fc3ce096
CUTOFF DATE (today): 2024-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S373531433d
CUTOFF DATE (today): 2026-06-26
Regulator: SEBI (IN)
Matter: SEBI consultation: ease-of-doing-business modifications to master circular provisions on administration of stock exchanges
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S9ee1174d84
CUTOFF DATE (today): 2023-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Digital Health Technologies for Remote Data Acquisition in Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-23 | official-forward (B) | draft_guidance_availability_notice | "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations; Draft Guidance for Industry, Investigators, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, investigators, and other stakeholders on the use of digital health technologies (DHTs) to acquire data remotely from participants in clinical investigations evaluating medical products. DHTs may take the form of hardware and/or software and may be used to gather health-related information from study participants and transmit that information to study investigators and/or other authorized parties to evaluate the safety and effectiveness of medical products.
---
## SNAPSHOT Sc756504928
CUTOFF DATE (today): 2021-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Technical Considerations for Demonstrating Reliability of Emergency-Use Injectors Submitted Under a Biologics License Application, New Drug Application, or Abbreviated New Drug ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S7e96583194
CUTOFF DATE (today): 2023-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-10 | official-forward (B) | draft_guidance_availability_notice | "Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Chronic Rhinosinusitis with Nasal Polyps: Developing Drugs for Treatment." The purpose of this draft guidance is to assist sponsors in the clinical development of drugs for the 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Chronic Rhinosinusitis with Nasal Polyps: Developing Drugs for Treatment." The purpose of this draft guidance is to assist sponsors in the clinical development of drugs for the treatment of chronic rhinosinusitis with nasal polyps (CRSwNP). Specifically, this draft guidance addresses FDA's current recommendations regarding trial design, safety, and efficacy considerations for CRSwNP clinical trials.