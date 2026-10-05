"""Require complete independent text-audit coverage before releasing scaled ingestion."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / "data/audits"
manifests = {r: json.loads((ROOT / f"data/forecasts/runs/{r}.json").read_text()) for r in ("ASTRA_CORE60", "ASTRA_CAL60")}
expected = {b["batch_id"]: set(b["snapshot_ids"]) for m in manifests.values() for b in m["batches"]}
covered = set()
sources = []
for filename, numbers in (("scaled60_first_output_audit_20261004.md", (1,)), ("scaled60_second_output_audit_20261004.md", (2, 3))):
    text = (A / filename).read_text(encoding="utf-8")
    assert "PASS" in text
    batches = [f"{run}_b{n:03d}" for run in manifests for n in numbers]
    covered.update(batches)
    sources.append({"report": filename, "batch_ids": batches})
old = json.loads((A / "scaled60_remaining_output_audit_20261004.json").read_text())
for b in old["batches"]:
    assert b["status"] == "PASS" and b["text_review_complete"]
    assert not b["observed_contamination_findings"] and not b["mechanical_findings"]
    assert b["forecast_count"] == len(expected[b["batch_id"]])
    assert b["batch_id"] not in covered
    covered.add(b["batch_id"])
sources.append({"report": "scaled60_remaining_output_audit_20261004.json", "batch_ids": [b["batch_id"] for b in old["batches"]]})
for stem in ("core_11_15", "core_16_20", "cal_11_18"):
    p = A / f"{stem}_text_audit_20261005.json"
    o = json.loads(p.read_text(encoding="utf-8"))
    assert o.get("status") == "PASS" or o.get("verdict") in ("PASS", "PASS_WITH_CAVEATS"), p
    assert not o.get("contamination_findings", []) and not o.get("citation_issues", [])
    scope = {"core_11_15": "CORE_11_15", "core_16_20": "CORE_16_20", "cal_11_18": "CAL_11_18"}[stem]
    review_input = A / f"scaled60_text_review_input_{scope}_20261005.json"
    assert hashlib.sha256(review_input.read_bytes()).hexdigest() == o["input_sha256"]
    batches = o["audited_batch_ids"]
    assert not covered.intersection(batches)
    ids = set(o["audited_snapshot_ids"])
    assert ids == set().union(*(expected[b] for b in batches))
    covered.update(batches)
    sources.append({"report": p.name, "batch_ids": batches})
assert covered == set(expected)
for source in sources:
    source["sha256"] = hashlib.sha256((A / source["report"]).read_bytes()).hexdigest()
execution = json.loads((A / "scaled60_execution_preflight_20261005.json").read_text())
assert execution["status"] == "PASS"
recognized = []
for run, manifest in manifests.items():
    for b in manifest["batches"]:
        obj = json.loads((ROOT / f"data/forecasts/packets/{run}/outbox/{b['batch_id']}.json").read_text(encoding="utf-8"))
        recognized.extend(f["id"] for f in obj["forecasts"] if f["recognised_outcome"])
out = {"status": "PASS", "audited_batches": len(covered), "audited_distinct_forecasts": sum(map(len, expected.values())), "observable_contamination": 0, "observable_contamination_rate": 0, "recognised_distinct_forecasts": len(recognized), "recognised_ids": recognized, "reports": sources, "limits": ["Hidden memory cannot be certified absent.", "Unsupported conditional parameter guesses are preserved; parameter coverage and mechanism accuracy unassessed.", "Zero GOLD cases; source version immutability is not established."]}
(A / "scaled60_full_acceptance_20261005.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k not in ("reports", "recognised_ids")}, indent=2))
