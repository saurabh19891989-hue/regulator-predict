"""Shared IO helpers. JSONL everywhere; append-only where noted."""
import hashlib
import json
import os
from datetime import date, datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SCHEMAS = os.path.join(ROOT, "schemas")
CENSOR_DATE = "2026-09-25"          # outcome verification date for this Gate-0 run
MODEL_KNOWLEDGE_CUTOFF = "2026-06-30"  # forecaster (Opus 5.5) stated knowledge cutoff: June 2026
CUTOFF_OFFSETS = [180, 120, 90, 60, 30, 14, 7]
HORIZONS = [7, 30, 60, 90, 180]


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}:{i}: bad JSON: {e}") from e
    return out


def write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")


def append_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")


def d(s):
    return date.fromisoformat(s) if isinstance(s, str) else s


def add_days(s, n):
    return (d(s) + timedelta(days=n)).isoformat()


def days_between(a, b):
    return (d(b) - d(a)).days


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def stable_hash(obj):
    return sha256_text(json.dumps(obj, sort_keys=True, ensure_ascii=False))


def now_iso():
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def load_schema(name):
    with open(os.path.join(SCHEMAS, f"{name}.schema.json")) as f:
        return json.load(f)
