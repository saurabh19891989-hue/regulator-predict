"""Reconcile immutable scaled-run archives and validate every output before ingestion."""
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rpe.common import frozen_data_hashes
from rpe.ledger import canonicalise

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
summary = {"status": "PASS", "runs": {}, "usage": {}, "batches": []}
sessions = set()
for run in ("ASTRA_CORE60", "ASTRA_CAL60"):
    manifest = json.loads((ROOT / f"data/forecasts/runs/{run}.json").read_text())
    assert manifest["dataset_sha256"] == frozen_data_hashes()
    archive = ROOT / f"data/forecasts/packets/{run}"
    (archive / "events").mkdir(exist_ok=True)
    ids = set()
    repairs = []
    for batch in manifest["batches"]:
        bid = batch["batch_id"]
        receipt = json.loads((archive / f"receipts/{bid}.json").read_text())
        assert receipt["exit_code"] == 0 and not receipt["unexpected_item_types"]
        assert receipt["model"] == "gpt-6-astra"
        assert receipt["packet_sha256"] == batch["packet_sha256"]
        assert sha(Path(batch["packet"])) == batch["packet_sha256"]
        assert sha(archive / f"inbox/{bid}.md") == batch["packet_sha256"]
        event = Path(receipt["events_path"])
        assert sha(event) == receipt["events_sha256"]
        dest = archive / f"events/{bid}.jsonl"
        if dest.exists():
            if sha(dest) != sha(event):
                failed = archive / f"failed_attempts/{bid}_usage_limit/events.jsonl"
                assert failed.exists() and sha(failed) == sha(dest), "Unpreserved conflicting event archive"
                shutil.copyfile(event, dest)
        else:
            shutil.copyfile(event, dest)
        events = [json.loads(s) for s in event.read_text(encoding="utf-8").splitlines() if s.strip()]
        assert len(receipt["session_ids"]) == 1
        assert not sessions.intersection(receipt["session_ids"])
        sessions.update(receipt["session_ids"])
        assert sum(e["type"] == "turn.completed" for e in events) == 1
        assert all(e.get("item", {}).get("type") in (None, "agent_message", "reasoning") for e in events)
        output = Path(batch["output"])
        assert sha(output) == sha(archive / f"outbox/{bid}.json")
        obj = json.loads(output.read_text(encoding="utf-8"))
        forecasts = obj["forecasts"]
        assert len(forecasts) == len(batch["snapshot_ids"])
        assert {f["id"] for f in forecasts} == set(batch["snapshot_ids"])
        assert not ids.intersection(batch["snapshot_ids"])
        ids.update(batch["snapshot_ids"])
        final_messages = [e["item"]["text"] for e in events if e["type"] == "item.completed" and e["item"]["type"] == "agent_message"]
        assert json.loads(final_messages[-1]) == obj
        for f in forecasts:
            _, rep = canonicalise(f)
            if rep:
                repairs.append({"id": f["id"], "repairs": rep})
        for usage in receipt["usage"]:
            for key, value in usage.items():
                summary["usage"][key] = summary["usage"].get(key, 0) + value
        summary["batches"].append({"batch_id": bid, "forecasts": len(forecasts), "output_sha256": sha(output), "events_sha256": sha(event)})
    assert all(target in ids for target in manifest["aliases"].values())
    assert not ids.intersection(manifest["aliases"])
    summary["runs"][run] = {"batches": len(manifest["batches"]), "distinct": len(ids), "aliases": len(manifest["aliases"]), "coherence_repairs": repairs}
summary["distinct_forecasts"] = sum(r["distinct"] for r in summary["runs"].values())
summary["logical_forecasts"] = sum(r["distinct"] + r["aliases"] for r in summary["runs"].values())
summary["dataset_sha256"] = frozen_data_hashes()
(ROOT / "data/audits/scaled60_execution_preflight_20261005.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in summary.items() if k not in ("batches", "dataset_sha256")}, indent=2))
