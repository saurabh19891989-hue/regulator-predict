# CORE 11-15 text/citation audit - 2026-10-05

**PASS** - 100 forecasts across ASTRA_CORE60_b011 through ASTRA_CORE60_b015 reviewed against all 40 supplied evidence profiles. No visible contamination or invalid local citations found. Eight snapshots contain nonblocking conditional numerical guesses.

Input: `scaled60_text_review_input_CORE_11_15_20261005.json`. SHA-256: `e58df4efc286799f8908247e96fc6e6bfc74445482c1b55901319b7c45df9975`.

## Coverage and reconstruction

Read every original raw forecast field, including all notes, scenario names/mechanisms, parameters, and missing-information strings. Coverage: 45 evidence-bearing and 55 title-only cases; 153 scenarios; 111 local evidence/contradiction references. A display truncation was repaired by rereading the affected complete cases.

Programmatic reconstruction passed for all five original packets and outputs: all 100 raw objects equal their original parsed JSON objects, and all 100 snapshot bodies equal the reconstructed header/profile content after boundary-whitespace and newline normalization. Snapshot membership matches exactly. Original files were read only for this comparison.

## Findings

Contamination findings: none. No asserted post-cutoff finalization date or realized policy content; no visible cross-snapshot fact transfer. Citations: all 111 resolve to the same snapshot's E1/E2. E2 in S4dbc738e7b supports consultation uncertainty; it does not substantiate the forecast alternatives as facts.

Recognition disclosure: all flags are present and boolean. Ten forecasts explicitly set `recognised_outcome=true`; their visible narratives remain evidence-based or use general forecasting priors. Hidden recognition cannot be verified.

Recognised IDs: `Se8ba78babd`, `Sa61dda0e68`, `Sb59f09546a`, `S519d977f04`, `S3c50127b06`, `S416cfef0e4`, `S035aa630f9`, `S4dbc738e7b`, `Sb83b51f2e9`, `Sbc4a9e7df1`.

## Unsupported numerical parameters

These are conditional forecast ranges or values, not claims that future events already occurred. They do not change the contamination PASS. No forecasts were rewritten.

- **Sf178aa4a6a** (ASTRA_CORE60_b011): `scenarios[1].params.AUM_threshold` = `Rs 20,000–30,000 crore`; `scenarios[1].params.additional_transition` = `0–12 months`; `scenarios[2].params.averaging_window` = `1–3 months`. E1 supplies the proposed Rs 20,000 crore threshold and monthly daily-average method. The higher upper bound, transition range, and longer averaging window have no supplied numerical derivation.
- **S9bd7653742** (ASTRA_CORE60_b011): `scenarios[0].params.base_price_reference` = `T-0 to T-1 NAV or corresponding current-value reference`; `scenarios[1].params.base_price_reference` = `T-1 NAV`; `scenarios[2].params.base_price_reference` = `T-0 to T-1 reference`. E1 identifies the existing T-2 NAV reference and its lag, but omits the replacement methodology. The T-0/T-1 predictions are extrapolations; the existing 20% and 5% band anchors are supported.
- **S52c27d6bbf** (ASTRA_CORE60_b012): `scenarios[1].params.implementation_transition` = `1–6 months`. E1 supplies the funds-only netting mechanism, gross securities settlement, and delivery-based taxes, but no 1-6 month transition range.
- **S01e30fe39c** (ASTRA_CORE60_b012): `scenarios[0].params.Z_score_cap` = `5–9.9`. E1 supplies the existing Z-score cap of 10 and 15-year lookback, and says they are under review. It supplies neither a lower replacement cap nor the 5-9.9 range.
- **S6ee8b3e3ca** (ASTRA_CORE60_b013): `scenarios[0].params.reference_lag` = `0–1 trading day where operationally available`; `scenarios[1].params.reference_lag` = `0–1 trading day for affected categories`. E1 identifies the lagged T-2 reference and existing bands, but does not state a 0-1 trading-day replacement. These are conditional reference-price guesses.
- **S6d8a68496f** (ASTRA_CORE60_b014): `scenarios[1].params.individual_minimum_investment_INR` = `5000–50000`. E1 supplies the existing INR 200,000 and proposed INR 1,000 minimums. It does not supply the intermediate INR 5,000-50,000 alternative.
- **Se4327836d5** (ASTRA_CORE60_b014): `scenarios[0].params.simplified_documentation_threshold_INR` = `1000000–2000000`; `scenarios[1].params.simplified_documentation_threshold_INR` = `1500000–3000000`; `scenarios[2].params.simplified_documentation_threshold_INR` = `600000–1000000`. E1 supplies the existing INR 500,000 threshold and a proposal to raise it, but no replacement value. All three forecast ranges are unsupported numerical extrapolations.
- **Sbb8480c400** (ASTRA_CORE60_b015): `scenarios[2].params.uniform_time_lag` = `7–60 days`. E1 supplies the existing one-day and three-month lags, but no 7-60 day compromise. Forecasts retaining either existing anchor are sourced anchors, not unsupported numerical values.

## Audited snapshots

| Batch | Snapshot IDs |
|---|---|
| ASTRA_CORE60_b011 | `Sbc753e4d30`, `S365a5bde85`, `S24b6400e89`, `Se8ba78babd`, `S9b1b12fefe`, `S8dac3245b9`, `Sf178aa4a6a`, `Sf3b5766514`, `S6e9a297fc3`, `S63bb3c38aa`, `S0647f362ec`, `S68de664d3b`, `Sa034caed7d`, `S3e7129c433`, `S9bd7653742`, `S8ef6703593`, `S49f3ad46f7`, `S5850a4fe34`, `S23fd8a9e5d`, `S7f475b9b77` |
| ASTRA_CORE60_b012 | `Sd3701be948`, `S6822b74057`, `S5102e60219`, `S52c27d6bbf`, `Sa61dda0e68`, `S13fbc45234`, `S5e66c94da8`, `S654a39b01c`, `S22671e5903`, `S43dbe996b4`, `Sea0ea85cef`, `Sa64549a749`, `S08373fdea5`, `S0e4a5e7ea8`, `Sc1688a63b6`, `S5201344288`, `Sc827e25536`, `S01e30fe39c`, `Sfbf2d0f1e9`, `Sa70d3b82ed` |
| ASTRA_CORE60_b013 | `Sb59f09546a`, `S519d977f04`, `Scb45011ca1`, `S872fabc935`, `S6ee8b3e3ca`, `S0e9bc218df`, `Sc5b58156b6`, `S98026427cb`, `Safe94de614`, `S0d0035a7a5`, `Sb8cd3e8195`, `S3fe0607c6a`, `Sf01d88151a`, `Sec1551e69c`, `Seb27ba1de3`, `Safb7c51524`, `S7d743d9b36`, `S0849a50464`, `S72e4ff6b0f`, `S6a712174ce` |
| ASTRA_CORE60_b014 | `S564ce60f6d`, `Sd65b57b1a2`, `S3c50127b06`, `S4ebd608030`, `Sb23d5d0736`, `Scb1b9b5004`, `Scb856082b3`, `S9332025d1a`, `Se9118ef529`, `S6d8a68496f`, `S07150dde93`, `S416cfef0e4`, `Sfa5b439710`, `Se4327836d5`, `S035aa630f9`, `Sc297df683d`, `S936eb64977`, `S4dbc738e7b`, `Se0efc50fd6`, `S283e3f047b` |
| ASTRA_CORE60_b015 | `Se272b0792d`, `Sb91d276853`, `S535506cc30`, `S7a08fa0fcf`, `Sea64372682`, `Saedf121836`, `S591534befb`, `S6943785a7c`, `Sb9ade2b2e5`, `Sb83b51f2e9`, `S38e812fbd2`, `Sc83723bef8`, `S8e6e622db4`, `S917443f737`, `S73b4778629`, `S18e65332c7`, `S511ac0376a`, `Sbb8480c400`, `Sb9b230f0b6`, `Sbc4a9e7df1` |

## Limits

- Hidden model memory and unexpressed influences on probabilities are unverifiable from output text. PASS means no visible contamination found, not proof that memory played no role.
- This is a text and citation audit, not an accuracy, calibration, or realized-outcome assessment. No canonical outcomes, threads, evidence datasets, or web sources were accessed.
- Source/packet release and execution receipt/hash gates belong to separate reviews; this report does not certify those gates.
- General process-rate statements and hypothetical scenario elaborations were assessed as forecasting priors or predictions, not as newly asserted matter-specific historical events. Their empirical calibration was not validated.
- Evidence profiles include truncated excerpts in the supplied packets. The audit assessed the supplied material, without inferring omitted source text.
- Cross-snapshot transfer was checked for visible content, including title-only snapshots. Similar general forecasting language and differing recognition flags across snapshots cannot establish hidden transfer or concealed recognition.

Only the two audit reports were written. No forecasts modified or ingested.
