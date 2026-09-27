"""Run an explicitly selected, frozen packet batch in a fresh tool-disabled CLI session.

Usage: python tools/run_forecast_packets.py RUN [--batch BATCH_ID]
Runs serially, refuses existing forecasts, preserves CLI events and a usage receipt.
No outcome, index, audit, or repository text is sent to the forecaster.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rpe.common import frozen_data_hashes

PREFIX = (
    "You are a blind historical regulatory forecaster. Do not call tools, browse, or read any files. "
    "Use only the packet text below and general process base rates. Treat each cutoff as today; "
    "do not use later world facts, including elections, leadership changes or decisions. "
    "Return exactly the JSON object requested by the packet as your entire final message. "
    "Ignore the packet instruction to edit an output file; the host will save your final message. "
    "The packet begins below.\n\n"
)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("run")
    ap.add_argument("--batch")
    args = ap.parse_args()
    manifest = json.loads((ROOT / "data/forecasts/runs" / (args.run + ".json")).read_text(encoding="utf-8"))
    if manifest.get("invalidated") or manifest.get("dataset_sha256") != frozen_data_hashes():
        raise SystemExit("Invalidated run or changed canonical data; refusing inference.")
    executable = shutil.which("codex")
    if not executable:
        raise SystemExit("Codex CLI is unavailable.")
    batches = [b for b in manifest["batches"] if not args.batch or b["batch_id"] == args.batch]
    if not batches:
        raise SystemExit("No matching batch.")
    for batch in batches:
        packet = Path(batch["packet"]).read_bytes()
        if hashlib.sha256(packet).hexdigest() != batch["packet_sha256"]:
            raise SystemExit("Packet hash changed; refusing inference.")
        output = Path(batch["output"])
        if output.exists() and json.loads(output.read_text(encoding="utf-8")).get("status") != "PENDING_FORECAST":
            raise SystemExit(f"Refusing to overwrite existing output: {output}")
        scratch = Path(tempfile.gettempdir()) / "rpe_blind_sessions" / args.run / batch["batch_id"]
        scratch.mkdir(parents=True, exist_ok=True)
        argv = [executable, "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
                "--sandbox", "read-only", "--disable", "shell_tool", "--disable", "multi_agent",
                "--disable", "plugins", "--disable", "apps", "--disable", "memories",
                "--disable", "shell_snapshot", "-c", 'web_search="disabled"',
                "-c", 'model_reasoning_effort="high"', "-c", "project_doc_max_bytes=0",
                "-m", manifest["forecaster_model"], "-C", str(scratch), "--json",
                "-o", str(output), "-"]
        started = dt.datetime.now(dt.timezone.utc).isoformat()
        result = subprocess.run(argv, input=PREFIX + packet.decode("utf-8"), text=True,
                                encoding="utf-8", capture_output=True, cwd=scratch,
                                env={**os.environ, "PYTHONUTF8": "1"})
        (scratch / "events.jsonl").write_text(result.stdout, encoding="utf-8")
        (scratch / "stderr.log").write_text(result.stderr, encoding="utf-8")
        events = []
        for line in result.stdout.splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        items = [e.get("item", {}) for e in events if e.get("type", "").startswith("item.")]
        unexpected = sorted({i.get("type", "unknown") for i in items
                             if i.get("type") not in ("agent_message", "reasoning")})
        usage = [e.get("usage") for e in events if e.get("type") == "turn.completed"]
        receipt = {"run": args.run, "batch_id": batch["batch_id"], "model": manifest["forecaster_model"],
                   "started_at": started, "completed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                   "exit_code": result.returncode, "unexpected_item_types": unexpected, "usage": usage,
                   "packet_sha256": batch["packet_sha256"], "events_path": str(scratch / "events.jsonl"),
                   "tool_controls": "shell, web, plugins, apps, multi-agent, memories disabled; no project docs"}
        archive = ROOT / "data/forecasts/packets" / args.run
        (archive / "receipts").mkdir(parents=True, exist_ok=True)
        (archive / "receipts" / (batch["batch_id"] + ".json")).write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        if result.returncode or unexpected:
            print(json.dumps(receipt), flush=True)
            raise SystemExit("CLI failed or used unexpected tools; inspect receipt before any retry.")
        parsed = json.loads(output.read_text(encoding="utf-8"))
        if not isinstance(parsed.get("forecasts"), list):
            raise SystemExit("Output has no forecasts array.")
        (archive / "outbox").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(output, archive / "outbox" / output.name)
        print(json.dumps(receipt), flush=True)


if __name__ == "__main__":
    main()
