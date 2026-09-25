"""Render blind-forecaster packets and output stubs for a forecasting run.

Packets are written OUTSIDE the repository (RPE_FC_ROOT) so an isolated forecaster, which only knows its packet
path, has no pointer into the repo's outcome store. Each batch holds at most one snapshot per thread.

Usage:
  python3 -m rpe.packets make <run_name> --arms ALL --designs T,K --size 20 [--cutoffs T-365,T-180,...] [--threads-file f]
"""
import argparse
import json
import os
import random
import re
from collections import defaultdict

from .common import DATA, read_jsonl, sha256_text
from .snapshots import available_date

FC_ROOT = os.environ.get(
    "RPE_FC_ROOT", "/tmp/claude-0/-home-user-regulator-predict/91e5b9f5-d683-5b72-a27c-87c3694866b1/scratchpad/fc")
STUB = '{"status": "PENDING_FORECAST"}'

DECISIVE = {
    "nprm_to_final": "the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part",
    "consultation_to_regulation": "the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation)",
    "draft_direction_to_final": "the central bank issues FINAL directions/circular adopting the draft at least in substantial part",
    "exposure_draft_to_regulation": "the regulator notifies FINAL regulations/circular (or formally approves them) adopting the draft at least in substantial part",
    "consultation_to_recommendation": "the regulator RELEASES its recommendations (or final regulation/order) on this consultation",
    "draft_guidance_to_final": "the agency publishes the FINAL version of this guidance",
    "investigation_to_duty": "the Government (Ministry of Finance) NOTIFIES the definitive duty recommended by the investigating authority",
    "other": "the regulator's first official publication adopting the proposal at least in substantial part",
}

HEADER = """# BLIND POINT-IN-TIME FORECASTING TASK
You are a professional regulatory forecaster. This file contains {n} independent forecasting snapshots about
DIFFERENT regulatory matters. Treat each snapshot on its own; do not carry information between snapshots.

Rules:
1. For each snapshot, "today" is its CUTOFF DATE. Nothing after the cutoff is known. Use only the evidence shown
   plus general knowledge of how that regulator and process usually behave (base rates, typical durations).
2. Do NOT use any specific memory of what happened to this particular matter after the cutoff. If you recognise the
   matter and believe you know its later outcome, still forecast as of the cutoff and set "recognised_outcome": true.
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
{{"forecasts": [
  {{"id": "<snapshot id>",
   "p": {{"7d": 0.00, "30d": 0.00, "60d": 0.00, "90d": 0.00, "180d": 0.00}},
   "next": {{"final_action": 0.00, "revised_or_further_consultation": 0.00, "formal_withdrawal": 0.00, "no_further_official_step": 0.00}},
   "content": {{"as_proposed": 0.00, "softened": 0.00, "tightened": 0.00, "mixed": 0.00, "different_mechanism": 0.00}},
   "scenarios": [{{"s": "short label", "p": 0.00, "mech": "mechanism, <=25 words", "params": {{"parameter": "predicted range"}}, "ev": ["E1"], "contra": []}}],
   "notes": "<=40 words: main drivers of your forecast",
   "missing": ["<=3 items of missing information that would most change the forecast"],
   "recognised_outcome": false,
   "insufficient_evidence": false}}
]}}
One entry per snapshot, in any order, using the exact snapshot ids below.
"""


def render_snapshot(snap, thread, items):
    lines = [f"\n---\n## SNAPSHOT {snap['snapshot_id']}",
             f"CUTOFF DATE (today): {snap['cutoff_date']}",
             f"Regulator: {thread['regulator']} ({thread['jurisdiction']})",
             f"Matter: {thread['neutral_title']}",
             f"Decisive action for this matter = {DECISIVE.get(thread['process_type'], DECISIVE['other'])}."]
    if not items:
        lines.append("Evidence: none provided for this snapshot.")
        return "\n".join(lines)
    agenda = [e for e in items if e["document_type"] == "regulatory_agenda_entry"]
    if len(agenda) > 4:  # cost control: keep the 4 most recent agenda editions
        drop = {id(e) for e in agenda[:-4]}
        items = [e for e in items if id(e) not in drop]
        lines.append(f"(Note: {len(agenda) - 4} earlier regulatory-agenda editions omitted; the 4 most recent are shown.)")
    lines.append(f"Evidence available as of the cutoff ({len(items)} item(s), chronological):")
    for i, e in enumerate(items, 1):
        dom = e["source_url"].split("/")[2] if "://" in e["source_url"] else ""
        tier = {"B": "official-forward (B)", "C": "official-soft (C)", "S": "stakeholder (S)", "D": "news (D)"}[e["tier"]]
        lines.append(f"[E{i}] {available_date(e)} | {tier} | {e['document_type']} | \"{e['title'][:220]}\" | {dom}")
        cl = [c for c in e.get("extracted_claims", []) if c][:5]
        if cl:
            lines.append("   Claims: " + " / ".join(c[:300] for c in cl))
        ex = (e.get("content_excerpt") or "").strip().replace("\n", " ")
        if ex:
            lines.append("   Excerpt: " + ex[:1200])
    return "\n".join(lines)


def make_run(run, arms, designs, size, offsets=None, thread_ids=None, strata=None, families=None, seed=0):
    idx = read_jsonl(os.path.join(DATA, "snapshots", "index.jsonl"))
    threads = {t["thread_id"]: t for t in read_jsonl(os.path.join(DATA, "threads", "threads.jsonl"))}
    ev = {e["evidence_id"]: e for e in read_jsonl(os.path.join(DATA, "evidence", "evidence.jsonl"))}
    sel = [r for r in idx if r["available"] and r["arm"] in arms and r["design"] in designs
           and (offsets is None or r["offset"] in offsets)
           and (thread_ids is None or r["thread_id"] in thread_ids)
           and (strata is None or r["stratum"] in strata)
           and (families is None or r["family"] in families)]
    # dedupe identical packets (same thread, cutoff, evidence set) across arms — score once, map to all arms
    uniq, alias = {}, {}
    for r in sel:
        k = (r["thread_id"], r["cutoff_date"], tuple(r["evidence_ids"]))
        if k in uniq:
            alias[r["snapshot_id"]] = uniq[k]["snapshot_id"]
        else:
            uniq[k] = r
    todo = list(uniq.values())
    random.Random(seed).shuffle(todo)
    batches = []
    for r in todo:  # greedy: first batch without this thread and with room
        for b in batches:
            if len(b) < size and all(x["thread_id"] != r["thread_id"] for x in b):
                b.append(r)
                break
        else:
            batches.append([r])
    inbox = os.path.join(FC_ROOT, run, "inbox")
    outbox = os.path.join(FC_ROOT, run, "outbox")
    os.makedirs(inbox, exist_ok=True)
    os.makedirs(outbox, exist_ok=True)
    manifest = {"run": run, "arms": arms, "designs": designs, "size": size, "offsets": offsets, "batches": [],
                "aliases": alias}
    for i, b in enumerate(batches, 1):
        bid = f"{run}_b{i:03d}"
        body = HEADER.format(n=len(b)) + "".join(
            render_snapshot(r, threads[r["thread_id"]], [ev[x] for x in r["evidence_ids"]]) for r in b)
        for r in b:  # soft guard: ISO dates after the cutoff inside a snapshot's text → logged for audit
            snap_txt = render_snapshot(r, threads[r["thread_id"]], [ev[x] for x in r["evidence_ids"]])
            late = sorted({m for m in re.findall(r"\b20\d\d-\d\d-\d\d\b", snap_txt) if m > r["cutoff_date"]})
            if late:
                manifest.setdefault("future_iso_dates", []).append({"snapshot_id": r["snapshot_id"], "dates": late[:5]})
        for r in b:  # hard guard: internal ids encode frame/stratum and must never reach a forecaster
            bad = [x for x in [r["thread_id"]] + r["evidence_ids"] if x in body]
            if bad:
                raise RuntimeError(f"internal id leaked into packet {bid}: {bad[:3]}")
        pin = os.path.join(inbox, bid + ".md")
        pout = os.path.join(outbox, bid + ".json")
        with open(pin, "w") as f:
            f.write(body)
        if not os.path.exists(pout):
            with open(pout, "w") as f:
                f.write(STUB)
        manifest["batches"].append({"batch_id": bid, "packet": pin, "output": pout,
                                    "snapshot_ids": [r["snapshot_id"] for r in b],
                                    "packet_sha256": sha256_text(body), "approx_tokens": len(body) // 4})
    os.makedirs(os.path.join(DATA, "forecasts", "runs"), exist_ok=True)
    with open(os.path.join(DATA, "forecasts", "runs", f"{run}.json"), "w") as f:
        json.dump(manifest, f, indent=1)
    return manifest


PROMPT = ("This is a research task, not a status line task. Read the task file {packet} and follow its "
          "instructions exactly. Then Read the output file {output} (it contains a placeholder) and use Edit to "
          "replace its ENTIRE content with your JSON. Do not read or edit any other file. When done reply with one "
          "line: WROTE <n> forecasts.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("run")
    ap.add_argument("--arms", default="ALL")
    ap.add_argument("--designs", default="T,K")
    ap.add_argument("--size", type=int, default=20)
    ap.add_argument("--offsets", default=None)
    ap.add_argument("--strata", default=None)
    ap.add_argument("--families", default=None)
    ap.add_argument("--threads-file", default=None)
    a = ap.parse_args()
    tids = set(json.load(open(a.threads_file))) if a.threads_file else None
    m = make_run(a.run, a.arms.split(","), a.designs.split(","), a.size,
                 offsets=a.offsets.split(",") if a.offsets else None, thread_ids=tids,
                 strata=a.strata.split(",") if a.strata else None,
                 families=a.families.split(",") if a.families else None)
    tot = sum(len(b["snapshot_ids"]) for b in m["batches"])
    print(json.dumps({"run": a.run, "batches": len(m["batches"]), "snapshots": tot, "aliases": len(m["aliases"]),
                      "snapshots_with_future_iso_dates": len(m.get("future_iso_dates", [])),
                      "approx_tokens_total": sum(b["approx_tokens"] for b in m["batches"])}, indent=1))
