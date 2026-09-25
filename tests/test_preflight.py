import hashlib
import json

from rpe import preflight


def _forecast(sid):
    return {
        "id": sid,
        "p": {"7d": 0.1, "30d": 0.2, "60d": 0.3, "90d": 0.4, "180d": 0.5},
        "next": {"final_action": 0.5, "revised_or_further_consultation": 0.2,
                 "formal_withdrawal": 0.1, "no_further_official_step": 0.2},
        "content": {"as_proposed": 0.4, "softened": 0.3, "tightened": 0.1,
                    "mixed": 0.1, "different_mechanism": 0.1},
        "scenarios": [{"s": "base", "p": 0.5, "mech": "adoption", "params": {},
                       "ev": ["E1"], "contra": []}],
        "notes": "base case", "missing": [], "recognised_outcome": True,
        "insufficient_evidence": False,
    }


def _run(tmp_path, monkeypatch):
    monkeypatch.setattr(preflight, "DATA", str(tmp_path))
    run, bid, sid = "test", "test_b001", "S1"
    packet = tmp_path / "forecasts" / "packets" / run / "inbox" / (bid + ".md")
    packet.parent.mkdir(parents=True)
    packet.write_text("## SNAPSHOT S1\n[E1] evidence\n", encoding="utf-8")
    output = tmp_path / "forecast.json"
    output.write_text(json.dumps({"forecasts": [_forecast(sid)]}), encoding="utf-8")
    runs = tmp_path / "forecasts" / "runs"
    runs.mkdir(parents=True)
    manifest = {"run": run, "aliases": {}, "batches": [{
        "batch_id": bid, "packet": str(tmp_path / "missing.md"), "output": str(output),
        "snapshot_ids": [sid], "packet_sha256": hashlib.sha256(packet.read_bytes()).hexdigest(),
    }]}
    (runs / (run + ".json")).write_text(json.dumps(manifest), encoding="utf-8")
    return run, packet, output


def test_preflight_reads_archive_and_reports_recognition(tmp_path, monkeypatch):
    run, packet, output = _run(tmp_path, monkeypatch)
    before = output.read_bytes()
    packet_before = packet.read_bytes()
    report = preflight.preflight(run)
    assert report["ok"]
    assert report["recognised_outcome_ids"] == ["S1"]
    assert output.read_bytes() == before
    assert packet.read_bytes() == packet_before


def test_preflight_rejects_packet_drift_and_output_errors(tmp_path, monkeypatch):
    run, packet, output = _run(tmp_path, monkeypatch)
    packet.write_bytes(packet.read_bytes() + b"tamper")
    rows = [_forecast("S1"), _forecast("S1")]
    rows[0]["p"]["30d"] = 0.05
    rows[0]["scenarios"][0]["ev"] = ["E2"]
    output.write_text(json.dumps({"forecasts": rows}), encoding="utf-8")
    report = preflight.preflight(run)
    assert not report["ok"]
    assert any("SHA-256 mismatch" in p for p in report["problems"])
    assert any("duplicate output ids" in p for p in report["problems"])
    assert any("coherence repairs required" in p for p in report["problems"])
    assert any("unavailable evidence labels" in p for p in report["problems"])


def test_preflight_rejects_invalidated_run(tmp_path, monkeypatch):
    run, _, _ = _run(tmp_path, monkeypatch)
    path = tmp_path / "forecasts" / "runs" / (run + ".json")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["invalidated"] = True
    manifest["invalid_reason"] = "masking failed"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    report = preflight.preflight(run)
    assert not report["ok"]
    assert any("masking failed" in p for p in report["problems"])


def test_preflight_rejects_changed_snapshot_index(tmp_path, monkeypatch):
    run, _, _ = _run(tmp_path, monkeypatch)
    path = tmp_path / "forecasts" / "runs" / (run + ".json")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["snapshot_index_sha256"] = "0" * 64
    path.write_text(json.dumps(manifest), encoding="utf-8")
    index = tmp_path / "snapshots" / "index.jsonl"
    index.parent.mkdir()
    index.write_text("", encoding="utf-8")
    report = preflight.preflight(run)
    assert not report["ok"]
    assert any("snapshot index SHA-256 mismatch" in p for p in report["problems"])
