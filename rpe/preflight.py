"""Read-only validation of a forecast run before ledger ingestion.

Usage: python -m rpe.preflight RUN
Exit status is zero only when every batch is ready and valid.
"""

import argparse
from collections import Counter
import hashlib
import json
import os
import re

from .common import DATA
from .ledger import canonicalise


def _packet_candidates(run, batch):
    archived = os.path.join(DATA, "forecasts", "packets", run, "inbox", batch["batch_id"] + ".md")
    return list(dict.fromkeys([batch["packet"], archived]))


def _labels_by_snapshot(packet_bytes):
    """Read only the evidence labels actually printed for each snapshot."""
    body = packet_bytes.decode("utf-8")
    sections = re.split(r"(?m)^## SNAPSHOT (\S+)\s*$", body)
    return {
        sid: set(re.findall(r"(?m)^\[E(\d+)\]", section))
        for sid, section in zip(sections[1::2], sections[2::2])
    }


def preflight(run):
    path = os.path.join(DATA, "forecasts", "runs", f"{run}.json")
    with open(path, encoding="utf-8") as f:
        manifest = json.load(f)
    problems, pending, recognised = [], [], []
    batch_reports = []
    if manifest.get("run") != run:
        problems.append(f"manifest run is {manifest.get('run')!r}, expected {run!r}")
    if manifest.get("invalidated"):
        problems.append(f"run was invalidated: {manifest.get('invalid_reason', 'no reason recorded')}")
    all_expected = [sid for b in manifest["batches"] for sid in b["snapshot_ids"]]
    duplicate_expected = sorted(sid for sid, count in Counter(all_expected).items() if count > 1)
    if duplicate_expected:
        problems.append(f"manifest has duplicate snapshot ids: {duplicate_expected}")

    for batch in manifest["batches"]:
        bid = batch["batch_id"]
        batch_problems = []
        packet_bytes = None
        packet_paths = []
        for candidate in _packet_candidates(run, batch):
            if not os.path.isfile(candidate):
                continue
            packet_paths.append(candidate)
            try:
                with open(candidate, "rb") as f:
                    content = f.read()
                digest = hashlib.sha256(content).hexdigest()
                if digest != batch["packet_sha256"]:
                    batch_problems.append(f"{bid}: packet SHA-256 mismatch at {candidate}")
                elif packet_bytes is None:
                    packet_bytes = content
            except OSError as exc:
                batch_problems.append(f"{bid}: cannot read packet {candidate}: {exc}")
        if not packet_paths:
            batch_problems.append(f"{bid}: no packet found at manifest or archived path")
        labels = {}
        if packet_bytes is not None:
            try:
                labels = _labels_by_snapshot(packet_bytes)
            except UnicodeDecodeError as exc:
                batch_problems.append(f"{bid}: packet is not UTF-8: {exc}")
        if packet_bytes is not None and set(labels) != set(batch["snapshot_ids"]):
            batch_problems.append(f"{bid}: packet snapshot ids differ from manifest")

        output = batch["output"]
        if not os.path.isfile(output):
            pending.append(bid)
            batch_reports.append({"batch_id": bid, "state": "pending", "packets_checked": packet_paths})
            problems.extend(batch_problems)
            continue
        try:
            with open(output, encoding="utf-8") as f:
                obj = json.load(f)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            batch_problems.append(f"{bid}: output cannot be read as JSON: {exc}")
            obj = None
        if isinstance(obj, dict) and obj.get("status") == "PENDING_FORECAST":
            pending.append(bid)
            batch_reports.append({"batch_id": bid, "state": "pending", "packets_checked": packet_paths})
            problems.extend(batch_problems)
            continue
        forecasts = obj.get("forecasts") if isinstance(obj, dict) else None
        if not isinstance(forecasts, list):
            batch_problems.append(f"{bid}: output must contain a forecasts array")
            forecasts = []
        ids = [raw.get("id") if isinstance(raw, dict) else None for raw in forecasts]
        if any(not isinstance(sid, str) for sid in ids):
            batch_problems.append(f"{bid}: every forecast id must be a string")
        ids = [sid if isinstance(sid, str) else None for sid in ids]
        duplicates = sorted((sid for sid, n in Counter(ids).items() if n > 1), key=str)
        if duplicates:
            batch_problems.append(f"{bid}: duplicate output ids {duplicates}")
        expected, actual = set(batch["snapshot_ids"]), set(ids)
        if expected != actual:
            batch_problems.append(f"{bid}: missing ids {sorted(expected - actual)}; unexpected ids {sorted(actual - expected, key=str)}")
        for raw in forecasts:
            if not isinstance(raw, dict) or raw.get("id") not in expected:
                continue
            sid = raw["id"]
            if type(raw.get("recognised_outcome")) is not bool:
                batch_problems.append(f"{bid}: {sid}: recognised_outcome must be boolean")
            elif raw["recognised_outcome"]:
                recognised.append(sid)
            try:
                forecast, repairs = canonicalise(raw)
            except Exception as exc:
                batch_problems.append(f"{bid}: {sid}: invalid forecast ({exc})")
                continue
            if repairs:
                batch_problems.append(f"{bid}: {sid}: coherence repairs required: {repairs}")
            valid_labels = {"E" + n for n in labels.get(sid, set())}
            scenarios = raw.get("scenarios") or []
            if not isinstance(scenarios, list):
                batch_problems.append(f"{bid}: {sid}: scenarios must be an array")
                continue
            for scenario in scenarios:
                if not isinstance(scenario, dict):
                    batch_problems.append(f"{bid}: {sid}: scenario must be an object")
                    continue
                ev, contra = scenario.get("ev", []), scenario.get("contra", [])
                if not isinstance(ev, list) or not isinstance(contra, list):
                    batch_problems.append(f"{bid}: {sid}: scenario evidence references must be arrays")
                    continue
                cited = ev + contra
                bad = sorted({str(c) for c in cited if not isinstance(c, str) or c not in valid_labels})
                if bad:
                    batch_problems.append(f"{bid}: {sid}: scenario cites unavailable evidence labels {bad}")
        problems.extend(batch_problems)
        batch_reports.append({"batch_id": bid, "state": "invalid" if batch_problems else "ready",
                              "packets_checked": packet_paths, "forecasts": len(forecasts)})
    return {"run": run, "ok": not problems and not pending, "batches": batch_reports,
            "pending_batches": pending, "recognised_outcome_ids": sorted(set(recognised)),
            "recognised_outcome_count": len(set(recognised)), "problems": problems}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run")
    args = parser.parse_args()
    report = preflight(args.run)
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["ok"] else 1)
