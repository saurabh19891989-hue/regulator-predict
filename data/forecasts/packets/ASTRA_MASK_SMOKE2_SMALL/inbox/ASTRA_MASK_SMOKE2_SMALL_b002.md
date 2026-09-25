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
## SNAPSHOT S6df9df0851
CUTOFF DATE (today): 2022-06-15
Regulator: a US federal regulator (identity withheld)
Matter: [title withheld — see evidence]
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-07-02 | official-forward (B) | draft_guidance_availability_notice | [TITLE WITHHELD] | 
   Claims: The the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry entitled [TITLE WITHHELD] This dr
   Excerpt: The the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry entitled [TITLE WITHHELD] This draft guidance provides recommendations for developing the content and format of an Instructions for Use (IFU) document for human prescription drugs and biological products and drug-device or biologic-device combination products submitted under a new drug application (NDA) or a biologics license application (BLA). The IFU is developed by applicants for patients who use drug products that have complicated or detailed patient-use instructions. The recommendations in this draft guidance are intended to help develop consistent content and format across IFUs and to help ensure that patients receive clear, concise information that is easily understood for the safe and effective use of prescription drug products.
---
## SNAPSHOT Sb9b8b67309
CUTOFF DATE (today): 2023-09-28
Regulator: an Indian regulator (identity withheld)
Matter: [title withheld — see evidence]
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (2 item(s), chronological):
[E1] 2023-02-08 | official-soft (C) | official_statement | [TITLE WITHHELD] | 
   Claims: the Regulator announced it would permit lending and borrowing of Government securities to augment the special repo market, with draft Directions to follow separately.
   Excerpt: I. Financial Markets 1. Introduction of Securities Lending and Borrowing in Government Securities A well-functioning market for securities lending and borrowing will add depth and liquidity to the Government securities market, aiding efficient price discovery. It is, therefore, proposed to permit lending and borrowing of Government securities which will augment the existing market for 'special repos'. The system is expected to facilitate wider participation in the securities lending market by providing investors an avenue to deploy idle securities and enhance portfolio returns. Draft Directions will be issued separately for stakeholder comments.
[E2] 2023-02-17 | official-forward (B) | draft_directions | [TITLE WITHHELD] | 
   Claims: In pursuance of the Statement on Developmental and Regulatory Policies dated February 8, 2023, the Regulator placed draft Government Securities Lending Directions, 2023 on its website. / Proposal permits lending and borrowing of Government securities, expected to augment the existing 'special repo' market and provide investors an avenue to deploy idle securities. / Comments invited by March 17, 2023.
   Excerpt: In pursuance of the announcement made in the Statement on Developmental and Regulatory Policies issued as a part of the Bi-monthly Monetary Policy Statement for 2022-23 dated February 08, 2023 , the the Regulator has today placed on its website Draft the Regulator (Government Securities Lending) Directions, 2023 for comments from banks, market participants and other interested parties. A well-functioning market for Securities Lending and Borrowing (SLB) in Government securities (G-Sec) will add depth and liquidity to the G-Sec market, aid efficient price discovery, improve secondary market liquidity for a wider set of securities and facilitate wider participation. The comments on the Draft Directions are invited from banks, market participants and other interested parties by March 17, 2023.
---
## SNAPSHOT Sb3df4e3bc0
CUTOFF DATE (today): 2024-11-27
Regulator: an Indian regulator (identity withheld)
Matter: [title withheld — see evidence]
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (2 item(s), chronological):
[E1] 2023-12-08 | official-soft (C) | official_statement | [TITLE WITHHELD] | 
   Claims: the Regulator announced, following a Working Group on Digital Lending recommendation accepted August 10, 2022, that it would bring loan aggregation services by LSPs under a regulatory framework focused on transparency and customer centricity.
   Excerpt: 3. Regulatory Framework for Web-Aggregation of loan products the Regulator had accepted, vide its Press Release dated August 10, 2022, the recommendation of the Working Group on Digital Lending (Chairman: Shri Jayant Kumar Dash) to come up with a regulatory framework for web-aggregators of loan products (WALP). WALP entails aggregation of loan offers from multiple lenders on an electronic platform which enables the borrowers to compare and choose the best available option to avail loan from one of the available lenders. Based on the recommendation of the Working Group, it has been decided to bring such loan aggregation services offered by the Lending Service Providers (LSPs) under a comprehensive regulatory framework. The framework will focus on enhancing the transparency in the operations of WALPs, increase customer centricity and enable the borrowers to make informed choices. The detailed guidelines will be issued separately.
[E2] 2024-04-26 | official-forward (B) | draft_circular | [TITLE WITHHELD] | 
   Claims: In pursuance of the Statement on Developmental and Regulatory Policies dated December 8, 2023, the Regulator placed a draft circular on Digital Lending - Transparency in Aggregation of Loan Products from Multiple Lenders. / Addresses issuance of a regulatory framework for aggregation of loan products by Lending Service Providers (LSPs). / Comments invited by May 31, 2024.
   Excerpt: In pursuance of the announcement made in the Statement on Developmental and Regulatory Policies dated December 08, 2023 regarding issuance of a regulatory framework for aggregation of loan products by lending service providers (LSPs), the the Regulator has today placed on its website the Draft Circular on 'Digital Lending – Transparency in Aggregation of Loan Products from Multiple Lenders'. Comments/feedback, if any, may be sent by e-mail with the subject line [TITLE WITHHELD], by May 31, 2024.
---
## SNAPSHOT Sc0f3dab048
CUTOFF DATE (today): 2020-10-06
Regulator: a US federal regulator (identity withheld)
Matter: [title withheld — see evidence]
Decisive action for this matter = the regulator's first official publication adopting the proposal at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-12-09 | official-forward (B) | draft_guidance_availability_notice | [TITLE WITHHELD] | 
   Claims: The the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry entitled [TITLE WITHHELD] This draft guidance will serv
   Excerpt: The the Regulator (the Regulator or Agency) is announcing the availability of a draft guidance for industry entitled [TITLE WITHHELD] This draft guidance will serve as a focus for continued discussions among the Division of Gastroenterology and Inborn Error Products, pharmaceutical sponsors, the academic community, and the public.