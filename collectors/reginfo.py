#!/usr/bin/env python3
"""
collectors/reginfo.py — us_reginfo workstream collector.

Builds point-in-time Tier-B precursor tables, keyed by RIN, from reginfo.gov
(the OMB/OIRA Unified Agenda + EO 12866 regulatory-review system) for later
merging into US Federal Register rulemaking threads built by another agent.

Writes ONLY under data/raw/us_reginfo/:
    agenda_entries.jsonl   one line per (pub_id, RIN) Unified Agenda entry
    agenda_editions.json   pub_id -> edition public-date registry
    oira_reviews.jsonl     one line per EO 12866 review record
    sources.json           source registry
    NOTES.md               coverage / method / gaps

Also exposes two pure functions for later merge steps (see bottom of file):
    agenda_evidence_for_rin(rin, before_date, ...)
    oira_evidence_for_rin(rin, before_date, ...)

Usage:
    python3 collectors/reginfo.py --collect-agenda
    python3 collectors/reginfo.py --collect-oira
    python3 collectors/reginfo.py --all
    python3 collectors/reginfo.py --selftest

Network: reginfo.gov's XMLViewFileAction endpoint appears to ignore HTTP
Range headers (it always returns the full body), so this script always
downloads whole files. Each Unified Agenda edition file (10-20MB) is deleted
immediately after it is parsed to keep the workstream's disk footprint small;
only the small extracted JSONL/JSON outputs are kept.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import date, datetime

WORKSTREAM_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(WORKSTREAM_DIR)
DATA_DIR = os.path.join(REPO_ROOT, "data", "raw", "us_reginfo")
CACHE_DIR = os.path.join(DATA_DIR, "cache")

AGENDA_ENTRIES_PATH = os.path.join(DATA_DIR, "agenda_entries.jsonl")
AGENDA_EDITIONS_PATH = os.path.join(DATA_DIR, "agenda_editions.json")
OIRA_REVIEWS_PATH = os.path.join(DATA_DIR, "oira_reviews.jsonl")

XML_BASE = "https://www.reginfo.gov/public/do/XMLViewFileAction?f="
USER_AGENT = "Mozilla/5.0"
RETRIEVAL_DATE = "2026-09-25"  # date this collector ran (today per task context)

# ---------------------------------------------------------------------------
# 1. Unified Agenda edition registry
# ---------------------------------------------------------------------------
# pub_id -> XML filename on reginfo.gov's XMLViewFileAction endpoint.
# Verified 2026-09-25 by listing https://www.reginfo.gov/public/do/eAgendaXmlReport
# (which enumerates every REGINFO_RIN_DATA_YYYYMM.xml / special-named file it
# currently serves) and by directly requesting each candidate id and checking
# for real <RIN_INFO> content vs. an HTML "not found" page.
#
# Two ID/labeling surprises found during verification (see NOTES.md):
#   - Spring 2018 is served under a special filename (not the YYYYMM pattern)
#     but its internal <PUBLICATION_ID> is 201804.
#   - There is NO "Fall 2025" or "Spring 2026" edition. pub_id 202510, which
#     the site's own historical-edition dropdown
#     (https://www.reginfo.gov/public/do/eAgendaHistory, <select id="currentPubId">)
#     labels "2026 The Regulatory Plan and the Unified Agenda ...", is the
#     terminal edition as of 2026-09-25: the administration collapsed the
#     usual Fall2025/Spring2026 biannual slots into one annual "2026" edition.
#     pub_id 202604 was probed directly and does not exist (reginfo.gov
#     returns its generic HTML error page, not XML, for that id).
EDITIONS = [
    {"pub_id": "201804", "season_label": "Spring 2018", "xml_file": "2018-SPRING-RIN-DATA.xml"},
    {"pub_id": "201810", "season_label": "Fall 2018", "xml_file": "REGINFO_RIN_DATA_201810.xml"},
    {"pub_id": "201904", "season_label": "Spring 2019", "xml_file": "REGINFO_RIN_DATA_201904.xml"},
    {"pub_id": "201910", "season_label": "Fall 2019", "xml_file": "REGINFO_RIN_DATA_201910.xml"},
    {"pub_id": "202004", "season_label": "Spring 2020", "xml_file": "REGINFO_RIN_DATA_202004.xml"},
    {"pub_id": "202010", "season_label": "Fall 2020", "xml_file": "REGINFO_RIN_DATA_202010.xml"},
    {"pub_id": "202104", "season_label": "Spring 2021", "xml_file": "REGINFO_RIN_DATA_202104.xml"},
    {"pub_id": "202110", "season_label": "Fall 2021", "xml_file": "REGINFO_RIN_DATA_202110.xml"},
    {"pub_id": "202204", "season_label": "Spring 2022", "xml_file": "REGINFO_RIN_DATA_202204.xml"},
    {"pub_id": "202210", "season_label": "Fall 2022", "xml_file": "REGINFO_RIN_DATA_202210.xml"},
    {"pub_id": "202304", "season_label": "Spring 2023", "xml_file": "REGINFO_RIN_DATA_202304.xml"},
    {"pub_id": "202310", "season_label": "Fall 2023", "xml_file": "REGINFO_RIN_DATA_202310.xml"},
    {"pub_id": "202404", "season_label": "Spring 2024", "xml_file": "REGINFO_RIN_DATA_202404.xml"},
    {"pub_id": "202410", "season_label": "Fall 2024", "xml_file": "REGINFO_RIN_DATA_202410.xml"},
    {"pub_id": "202504", "season_label": "Spring 2025", "xml_file": "REGINFO_RIN_DATA_202504.xml"},
    {"pub_id": "202510", "season_label": "2026 (annual; replaced the Fall2025/Spring2026 slots)",
     "xml_file": "REGINFO_RIN_DATA_202510.xml"},
]

# Edition public-date registry. online_release_date is approximated from the
# XML RUN_DATE attribute embedded in each edition's bulk file (the date OIRA
# says it generated/froze that edition's data feed for release) UNLESS a
# better-verified value is available; fr_publication_date is the date the
# Federal Register published that edition's "Introduction to the Unified
# Agenda ..." notice (Regulatory Information Service Center, agency
# regulatory-information-service-center), found via the FR API
# (https://www.federalregister.gov/api/v1/documents.json, verified 2026-09-25).
# conservative_public_date = later of the two when both exist, else whichever
# is verified. RUN_DATE always preceded the FR date in every edition where
# both exist, so conservative_public_date == fr_publication_date in every
# such case; this is a deliberate, checkable pattern, not an assumption.
AGENDA_EDITIONS = {
    "201804": {
        "season": "Spring 2018", "run_date": "2018-09-17",
        "online_release_date": "2018-09-17",
        "online_release_source": "XML RUN_DATE attribute, 2018-SPRING-RIN-DATA.xml",
        "fr_publication_date": "2018-06-11",
        "fr_source_doc": "FR 2018-11237, 'Unified Agenda of Federal Regulatory and Deregulatory "
                          "Actions-Spring 2018' (FCC entry for this edition)",
        "fr_source_url": "https://www.federalregister.gov/documents/2018/06/11/2018-11237/"
                          "unified-agenda-of-federal-regulatory-and-deregulatory-actions-spring-2018",
        "date_confidence": "medium",
        "note": "RUN_DATE (2018-09-17) is LATER than the verified FR publication date "
                "(2018-06-11), unlike every other edition in this table, where RUN_DATE < FR "
                "date. This is almost certainly because this file is a later re-export/refresh "
                "of the Spring 2018 dataset (reginfo.gov regenerates XML exports over time; "
                "RUN_DATE tracks the export, not the edition's original publication). The FR "
                "date is the trustworthy anchor here; conservative_public_date uses it.",
    },
    "201810": {
        "season": "Fall 2018", "run_date": "2018-10-14",
        "online_release_date": "2018-10-14",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_201810.xml",
        "fr_publication_date": "2018-11-16",
        "fr_source_doc": "FR 2018-24084, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Fall 2018' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2018/11/16/2018-24084/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-fall-2018",
        "date_confidence": "high",
        "note": "",
    },
    "201904": {
        "season": "Spring 2019", "run_date": "2019-05-22",
        "online_release_date": "2019-05-22",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_201904.xml",
        "fr_publication_date": "2019-06-24",
        "fr_source_doc": "FR 2019-12557, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions' (Regulatory Information "
                          "Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2019/06/24/2019-12557/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions",
        "date_confidence": "high",
        "note": "",
    },
    "201910": {
        "season": "Fall 2019", "run_date": "2019-11-16",
        "online_release_date": "2019-11-16",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_201910.xml",
        "fr_publication_date": "2019-12-26",
        "fr_source_doc": "FR 2019-26533, 'Introduction to the Fall 2019 Regulatory Plan' "
                          "(Regulatory Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2019/12/26/2019-26533/"
                          "introduction-to-the-fall-2019-regulatory-plan",
        "date_confidence": "high",
        "note": "Fall-year editions that include a Regulatory Plan are sometimes titled "
                "'Introduction to the Fall <year> Regulatory Plan' rather than 'Introduction "
                "to the Unified Agenda ...'; confirmed this is the Fall 2019 edition preamble "
                "by publication-date adjacency and RISC authorship.",
    },
    "202004": {
        "season": "Spring 2020", "run_date": "2020-06-30",
        "online_release_date": "2020-06-30",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202004.xml",
        "fr_publication_date": "2020-08-26",
        "fr_source_doc": "FR 2020-16754, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions' (Regulatory Information "
                          "Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2020/08/26/2020-16754/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions",
        "date_confidence": "high",
        "note": "",
    },
    "202010": {
        "season": "Fall 2020", "run_date": "2020-12-14",
        "online_release_date": "2020-12-14",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202010.xml",
        "fr_publication_date": "2021-03-31",
        "fr_source_doc": "FR 2021-04348, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Fall 2020' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2021/03/31/2021-04348/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-fall-2020",
        "date_confidence": "high",
        "note": "Large (~3.5 month) online-to-FR gap, consistent with the Jan 2021 "
                "administration transition delaying the FR notice for this edition.",
    },
    "202104": {
        "season": "Spring 2021", "run_date": "2021-06-14",
        "online_release_date": "2021-06-14",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202104.xml",
        "fr_publication_date": "2021-07-30",
        "fr_source_doc": "FR 2021-15272, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions' (Regulatory Information "
                          "Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2021/07/30/2021-15272/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions",
        "date_confidence": "high",
        "note": "",
    },
    "202110": {
        "season": "Fall 2021", "run_date": "2021-12-08",
        "online_release_date": "2021-12-08",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202110.xml",
        "fr_publication_date": "2022-01-31",
        "fr_source_doc": "FR 2022-00702, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Fall 2021' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2022/01/31/2022-00702/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-fall-2021",
        "date_confidence": "high",
        "note": "",
    },
    "202204": {
        "season": "Spring 2022", "run_date": "2022-07-01",
        "online_release_date": "2022-07-01",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202204.xml",
        "fr_publication_date": "2022-08-08",
        "fr_source_doc": "FR 2022-14654, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions' (Regulatory Information "
                          "Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2022/08/08/2022-14654/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions",
        "date_confidence": "high",
        "note": "",
    },
    "202210": {
        "season": "Fall 2022", "run_date": "2023-01-04",
        "online_release_date": "2023-01-04",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202210.xml",
        "fr_publication_date": "2023-02-22",
        "fr_source_doc": "FR 2023-02113, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Fall 2022' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2023/02/22/2023-02113/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-fall-2022",
        "date_confidence": "high",
        "note": "",
    },
    "202304": {
        "season": "Spring 2023", "run_date": "2023-07-19",
        "online_release_date": "2023-07-19",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202304.xml",
        "fr_publication_date": "2023-07-27",
        "fr_source_doc": "FR 2023-14540, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Spring 2023' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2023/07/27/2023-14540/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-spring-2023",
        "date_confidence": "high",
        "note": "",
    },
    "202310": {
        "season": "Fall 2023", "run_date": "2023-12-05",
        "online_release_date": "2023-12-05",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202310.xml",
        "fr_publication_date": "2024-02-09",
        "fr_source_doc": "FR 2024-00476, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Fall 2023' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2024/02/09/2024-00476/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-fall-2023",
        "date_confidence": "high",
        "note": "",
    },
    "202404": {
        "season": "Spring 2024", "run_date": "2024-07-03",
        "online_release_date": "2024-07-03",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202404.xml",
        "fr_publication_date": "2024-08-16",
        "fr_source_doc": "FR 2024-16445, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Spring 2024' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2024/08/16/2024-16445/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-spring-2024",
        "date_confidence": "high",
        "note": "",
    },
    "202410": {
        "season": "Fall 2024", "run_date": "2024-12-12",
        "online_release_date": "2024-12-12",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202410.xml "
                                  "(NOT independently corroborated by a second source)",
        "fr_publication_date": None,
        "fr_source_doc": None,
        "fr_source_url": None,
        "date_confidence": "low",
        "note": "GAP: no Federal Register 'Introduction to the Unified Agenda ...' notice for "
                "Fall 2024 was found. Searched the FR API for "
                "'Unified Agenda of Federal Regulatory and Deregulatory Actions' and "
                "'Semiannual Regulatory Agenda' over 2024-09-01..2025-10-01: zero matching "
                "documents. A per-RIN reginfo.gov page for this edition "
                "(eAgendaViewRule?pubId=202410&RIN=0503-AA80) explicitly shows "
                "'RIN Data Printed in the FR: No', consistent with this edition never having "
                "gone through Federal Register publication (most plausibly the Jan 2025 "
                "administration transition/regulatory freeze interrupted the normal "
                "online-then-FR publication sequence, and this edition was superseded by the "
                "next edition published as 'Spring 2025' on 2025-09-22 without ever separately "
                "appearing in the FR under its own name). Because there is no independently "
                "verified public date besides the XML RUN_DATE, conservative_public_date is "
                "set to the RUN_DATE with version_confidence=low. Forecasters using this "
                "edition for point-in-time cutoffs near Dec 2024-Sep 2025 should treat its "
                "public date as UNCERTAIN and prefer corroboration (e.g., a later edition or "
                "an FR document that mentions this RIN) before relying on it for a hard cutoff.",
    },
    "202504": {
        "season": "Spring 2025", "run_date": "2025-09-06",
        "online_release_date": "2025-09-06",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202504.xml",
        "fr_publication_date": "2025-09-22",
        "fr_source_doc": "FR 2025-18323, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-Spring 2025' (Regulatory "
                          "Information Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2025/09/22/2025-18323/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-spring-2025",
        "date_confidence": "high",
        "note": "",
    },
    "202510": {
        "season": "2026 (annual)", "run_date": "2026-07-03",
        "online_release_date": "2026-07-03",
        "online_release_source": "XML RUN_DATE attribute, REGINFO_RIN_DATA_202510.xml",
        "fr_publication_date": "2026-08-14",
        "fr_source_doc": "FR 2026-16603, 'Introduction to the Unified Agenda of Federal "
                          "Regulatory and Deregulatory Actions-2026' (Regulatory Information "
                          "Service Center)",
        "fr_source_url": "https://www.federalregister.gov/documents/2026/08/14/2026-16603/"
                          "introduction-to-the-unified-agenda-of-federal-regulatory-and-"
                          "deregulatory-actions-2026",
        "date_confidence": "high",
        "note": "This is the edition reginfo.gov's own historical-edition selector labels "
                "'2026 The Regulatory Plan and the Unified Agenda ...' (not 'Fall 2025'); it "
                "replaces both the usual Fall 2025 and Spring 2026 slots. As of 2026-09-25 "
                "(this collector's retrieval date) it is the terminal, most recent edition; "
                "pub_id 202604 does not exist yet.",
    },
}

for _pid, _ed in AGENDA_EDITIONS.items():
    _fr = _ed.get("fr_publication_date")
    _on = _ed.get("online_release_date")
    _ed["conservative_public_date"] = _fr if _fr else _on
    if _fr and _on and _fr < _on and not _ed.get("note"):
        # sanity: FR date earlier than the online/RUN_DATE proxy is only expected for
        # editions with a documented explanation (e.g. 201804's re-exported RUN_DATE)
        raise AssertionError(f"{_pid}: fr_publication_date earlier than online_release_date, undocumented")

# ---------------------------------------------------------------------------
# 2. EO 12866 review report registry
# ---------------------------------------------------------------------------
OIRA_YEARS = list(range(2018, 2026))  # EO_RULE_COMPLETED_2018.xml .. _2025.xml
OIRA_REPORTS = (
    [f"EO_RULE_COMPLETED_{y}.xml" for y in OIRA_YEARS]
    + ["EO_RULE_COMPLETED_YTD.xml"]  # current calendar year (2026) completed reviews
    + ["EO_RULES_UNDER_REVIEW.xml"]  # currently pending reviews (live snapshot)
)
AGENCY_LIST_XML = "AGY_AGENCY_LIST.xml"


# ---------------------------------------------------------------------------
# Download helper
# ---------------------------------------------------------------------------
def _download(xml_filename: str, dest_path: str, timeout_sec: int = 180) -> bool:
    """Download a reginfo.gov bulk XML report via curl. Returns True on a
    plausible XML payload, False otherwise (leaves no partial file behind)."""
    url = XML_BASE + xml_filename
    cmd = ["curl", "-sSL", "-m", str(timeout_sec), "-A", USER_AGENT, "-o", dest_path, url]
    try:
        subprocess.run(cmd, check=True, timeout=timeout_sec + 15)
    except Exception as exc:  # noqa: BLE001
        print(f"  download FAILED for {xml_filename}: {exc}", file=sys.stderr)
        if os.path.exists(dest_path):
            os.remove(dest_path)
        return False
    if not os.path.exists(dest_path) or os.path.getsize(dest_path) < 200:
        if os.path.exists(dest_path):
            os.remove(dest_path)
        return False
    with open(dest_path, "rb") as f:
        head = f.read(300)
    if b"<?xml" not in head and b"<REGINFO_RIN_DATA" not in head and b"<OIRA_DATA" not in head:
        os.remove(dest_path)
        return False
    return True


# ---------------------------------------------------------------------------
# 3. Unified Agenda parsing
# ---------------------------------------------------------------------------
_FINAL_ACTION_RE = re.compile(r"^\s*\d*(st|nd|rd|th)?\s*final\s*(rule|action)\b", re.IGNORECASE)
_WITHDRAW_RE = re.compile(r"withdraw", re.IGNORECASE)


def _text(el, tag, default=None):
    child = el.find(tag)
    if child is None or child.text is None:
        return default
    return child.text.strip()


def parse_agenda_edition(xml_path: str, pub_id: str):
    """Stream-parse one Unified Agenda bulk XML file with iterparse, yielding
    one dict per <RIN_INFO> element. Clears each element after use so peak
    memory stays roughly constant regardless of file size."""
    context = ET.iterparse(xml_path, events=("end",))
    for _event, elem in context:
        if elem.tag != "RIN_INFO":
            continue
        try:
            rin = _text(elem, "RIN")
            if not rin:
                continue
            agency_el = elem.find("AGENCY")
            parent_el = elem.find("PARENT_AGENCY")
            agency_name = _text(agency_el, "NAME") if agency_el is not None else None
            agency_acr = _text(agency_el, "ACRONYM") if agency_el is not None else None
            parent_name = _text(parent_el, "NAME") if parent_el is not None else None
            parent_acr = _text(parent_el, "ACRONYM") if parent_el is not None else None

            title = _text(elem, "RULE_TITLE", "")
            stage = _text(elem, "RULE_STAGE")
            priority = _text(elem, "PRIORITY_CATEGORY")
            rin_status = _text(elem, "RIN_STATUS")
            major = _text(elem, "MAJOR")

            timetable = []
            ttbl_list = elem.find("TIMETABLE_LIST")
            if ttbl_list is not None:
                for t in ttbl_list.findall("TIMETABLE"):
                    action = _text(t, "TTBL_ACTION", "")
                    date_text = _text(t, "TTBL_DATE")
                    fr_cites = [c.text.strip() for c in t.findall("FR_CITATION") if c.text]
                    fr_cite = fr_cites[0] if fr_cites else None
                    timetable.append({
                        "action": action.strip() if action else action,
                        "date_text": date_text,
                        "fr_cite": fr_cite,
                    })

            projected_final_action_date_text = None
            for t in timetable:
                if _FINAL_ACTION_RE.match(t["action"] or ""):
                    projected_final_action_date_text = t["date_text"]  # keep last match

            withdrawn = bool(rin_status and _WITHDRAW_RE.search(rin_status)) or any(
                _WITHDRAW_RE.search(t["action"] or "") for t in timetable
            )

            print_paper_flags = [
                (_text(elem, "PRINT_PAPER") or "").strip().lower() == "yes"
            ]

            yield {
                "pub_id": pub_id,
                "rin": rin,
                "agency": agency_name or agency_acr,
                "agency_acronym": agency_acr,
                "parent_agency": parent_name,
                "parent_agency_acronym": parent_acr,
                "title": title,
                "stage": stage,
                "priority": priority,
                "rin_status": rin_status,
                "major": major,
                "timetable": timetable,
                "projected_final_action_date_text": projected_final_action_date_text,
                "long_term": stage == "Long-Term Actions",
                "completed_action": stage == "Completed Actions",
                "withdrawn": withdrawn,
                "printed_in_fr": any(print_paper_flags) if print_paper_flags else None,
            }
        finally:
            elem.clear()


def collect_agenda(editions=None, limit_editions=None):
    """Download + parse every Unified Agenda edition, writing agenda_entries.jsonl.
    Deletes each downloaded XML immediately after it is parsed."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    editions = editions if editions is not None else EDITIONS
    if limit_editions:
        editions = editions[:limit_editions]

    counts = {}
    with open(AGENDA_ENTRIES_PATH, "w", encoding="utf-8") as out:
        for ed in editions:
            pub_id = ed["pub_id"]
            xml_file = ed["xml_file"]
            dest = os.path.join(CACHE_DIR, xml_file.replace("/", "_"))
            print(f"[agenda] downloading {xml_file} (pub_id={pub_id}) ...")
            ok = _download(xml_file, dest)
            if not ok:
                print(f"[agenda]   FAILED: {xml_file} did not return usable XML", file=sys.stderr)
                counts[pub_id] = 0
                continue
            n = 0
            try:
                for rec in parse_agenda_edition(dest, pub_id):
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n += 1
            except ET.ParseError as exc:
                print(f"[agenda]   XML parse error for {xml_file}: {exc}", file=sys.stderr)
            finally:
                if os.path.exists(dest):
                    os.remove(dest)  # keep disk footprint small
            counts[pub_id] = n
            print(f"[agenda]   {pub_id}: {n} RIN entries")
    return counts


def write_agenda_editions():
    with open(AGENDA_EDITIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(AGENDA_EDITIONS, f, indent=2, sort_keys=True, ensure_ascii=False)
    print(f"[editions] wrote {AGENDA_EDITIONS_PATH} ({len(AGENDA_EDITIONS)} editions)")


# ---------------------------------------------------------------------------
# 4. OIRA EO 12866 review parsing
# ---------------------------------------------------------------------------
def _load_agency_map(agency_xml_path: str):
    mapping = {}
    try:
        tree = ET.parse(agency_xml_path)
    except ET.ParseError:
        return mapping
    for a in tree.getroot().findall("AGENCY"):
        code = _text(a, "AGENCY_CODE")
        name = _text(a, "NAME")
        acr = _text(a, "ACRONYM")
        if code:
            mapping[code] = {"name": name, "acronym": acr}
    return mapping


def parse_oira_report(xml_path: str, source_report: str, agency_map: dict):
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as exc:
        print(f"[oira]   XML parse error for {source_report}: {exc}", file=sys.stderr)
        return
    for act in tree.getroot().findall("REGACT"):
        rin = _text(act, "RIN")
        if not rin:
            continue
        agency_code = _text(act, "AGENCY_CODE")
        agency_info = agency_map.get(agency_code, {})
        date_completed = _text(act, "DATE_COMPLETED") or None
        decision = _text(act, "DECISION") or None
        yield {
            "rin": rin,
            "agency": agency_info.get("name") or agency_code,
            "agency_code": agency_code,
            "title": _text(act, "TITLE"),
            "stage": _text(act, "STAGE"),
            "date_received": _text(act, "DATE_RECEIVED"),
            "date_completed": date_completed,
            "decision": decision,
            "economically_significant": (_text(act, "ECONOMICALLY_SIGNIFICANT") or "").strip() == "Yes",
            "major": (_text(act, "MAJOR") or "").strip() or None,
            "date_published": _text(act, "DATE_PUBLISHED") or None,
            "review_status": "completed" if date_completed else "under_review",
            "source_report": source_report,
        }


def collect_oira(reports=None):
    os.makedirs(CACHE_DIR, exist_ok=True)
    reports = reports if reports is not None else OIRA_REPORTS

    agency_dest = os.path.join(CACHE_DIR, AGENCY_LIST_XML)
    print(f"[oira] downloading {AGENCY_LIST_XML} ...")
    agency_map = {}
    if _download(AGENCY_LIST_XML, agency_dest):
        agency_map = _load_agency_map(agency_dest)
        os.remove(agency_dest)
    print(f"[oira]   {len(agency_map)} agency codes loaded")

    counts = {}
    with open(OIRA_REVIEWS_PATH, "w", encoding="utf-8") as out:
        for report in reports:
            dest = os.path.join(CACHE_DIR, report)
            print(f"[oira] downloading {report} ...")
            ok = _download(report, dest)
            if not ok:
                print(f"[oira]   FAILED: {report} did not return usable XML", file=sys.stderr)
                counts[report] = 0
                continue
            n = 0
            for rec in parse_oira_report(dest, report, agency_map):
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n += 1
            if os.path.exists(dest):
                os.remove(dest)
            counts[report] = n
            print(f"[oira]   {report}: {n} review records")
    return counts


# ---------------------------------------------------------------------------
# 5. Pure evidence-builder functions for later merging (Tier-B)
# ---------------------------------------------------------------------------
def _parse_date(s):
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _read_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _summarize_timetable(timetable):
    parts = []
    for t in timetable:
        action = t.get("action") or "?"
        date_text = t.get("date_text") or "n.d."
        fr = f", {t['fr_cite']}" if t.get("fr_cite") else ""
        parts.append(f"{action}: {date_text}{fr}")
    return "; ".join(parts)


def agenda_evidence_for_rin(rin, before_date, agenda_entries=None, agenda_editions=None):
    """Pure function. Returns a list of Tier-B evidence dicts (docs/EXECUTOR_GUIDE.md
    evidence format) for `rin`, one per Unified Agenda edition whose
    conservative_public_date < before_date. `evidence_id` is left as None —
    the caller (thread-building agent) must assign the real id. Does not read
    or write any state besides the two input JSONL/JSON files (or the
    provided in-memory equivalents), and does not mutate its inputs.

    before_date: 'YYYY-MM-DD' string or datetime.date.
    """
    if agenda_entries is None:
        agenda_entries = _read_jsonl(AGENDA_ENTRIES_PATH)
    if agenda_editions is None:
        agenda_editions = _read_json(AGENDA_EDITIONS_PATH)

    before = before_date if isinstance(before_date, date) else _parse_date(before_date)
    if before is None:
        raise ValueError(f"before_date not parseable as YYYY-MM-DD: {before_date!r}")

    matches = [e for e in agenda_entries if e.get("rin") == rin]
    matches.sort(key=lambda e: e.get("pub_id", ""))

    results = []
    for e in matches:
        ed = agenda_editions.get(e["pub_id"])
        if not ed:
            continue
        cpd_text = ed.get("conservative_public_date")
        cpd = _parse_date(cpd_text)
        if cpd is None or cpd >= before:
            continue  # not yet public as of the cutoff, or unverifiable date

        stage = e.get("stage") or "unknown stage"
        priority = e.get("priority") or "unknown priority"
        timetable_str = _summarize_timetable(e.get("timetable") or [])
        proj = e.get("projected_final_action_date_text")
        flags = []
        if e.get("long_term"):
            flags.append("long-term action")
        if e.get("completed_action"):
            flags.append("marked completed in this edition")
        if e.get("withdrawn"):
            flags.append("withdrawal language present in this edition")
        flags_str = f" [{'; '.join(flags)}]" if flags else ""

        excerpt = (
            f"{ed.get('season', e['pub_id'])} Unified Agenda entry for RIN {rin} "
            f"({e.get('agency') or 'unknown agency'}): \"{e.get('title') or ''}\". "
            f"Stage: {stage}. Priority: {priority}.{flags_str} "
            f"Timetable as printed in this edition: {timetable_str or 'none listed'}."
        )
        if proj:
            excerpt += f" Projected final-action date as printed: {proj}."

        results.append({
            "evidence_id": None,
            "regulator": e.get("agency") or e.get("parent_agency") or "OIRA",
            "jurisdiction": "US",
            "title": f"Unified Agenda ({ed.get('season', e['pub_id'])}) entry: {e.get('title') or rin}",
            "source_url": f"https://www.reginfo.gov/public/do/eAgendaViewRule?pubId={e['pub_id']}&RIN={rin}",
            "publication_date": cpd_text,
            "first_known_date": None,
            "retrieval_date": RETRIEVAL_DATE,
            "document_type": "regulatory_agenda_entry",
            "tier": "B",
            "original_or_revised": "original",
            "version_confidence": ed.get("date_confidence", "medium"),
            "date_verification": (
                f"conservative_public_date = {'fr_publication_date' if ed.get('fr_publication_date') else 'online_release_date (approx.)'} "
                f"from data/raw/us_reginfo/agenda_editions.json pub_id={e['pub_id']}. "
                + (ed.get("note") or "")
            ).strip(),
            "extracted_claims": [
                f"Stage as of {ed.get('season', e['pub_id'])}: {stage}.",
                f"Priority category as of {ed.get('season', e['pub_id'])}: {priority}.",
            ] + ([f"Projected final-action date as printed: {proj}."] if proj else []),
            "content_excerpt": excerpt[:1200],
            "source_hash": None,
            "stored_copy": None,
        })
    return results


def oira_evidence_for_rin(rin, before_date, oira_reviews=None):
    """Pure function. Returns a list of Tier-B evidence dicts for `rin`, one
    per EO 12866 review whose date_received < before_date. date_completed is
    included in the excerpt ONLY if it is also < before_date; otherwise the
    review is described as still under review as of the cutoff. evidence_id
    is left as None for the caller to assign.
    """
    if oira_reviews is None:
        oira_reviews = _read_jsonl(OIRA_REVIEWS_PATH)

    before = before_date if isinstance(before_date, date) else _parse_date(before_date)
    if before is None:
        raise ValueError(f"before_date not parseable as YYYY-MM-DD: {before_date!r}")

    matches = [r for r in oira_reviews if r.get("rin") == rin]
    # de-duplicate identical (rin, date_received, source_report) rows that can
    # arise if a still-pending review is later re-emitted in a completed report
    seen = set()
    dedup = []
    for r in matches:
        key = (r.get("date_received"), r.get("date_completed"), r.get("source_report"))
        if key in seen:
            continue
        seen.add(key)
        dedup.append(r)
    dedup.sort(key=lambda r: r.get("date_received") or "")

    results = []
    for r in dedup:
        received = _parse_date(r.get("date_received"))
        if received is None or received >= before:
            continue

        completed = _parse_date(r.get("date_completed"))
        if completed is not None and completed < before:
            completion_text = (
                f"Review completed {r['date_completed']}, decision: {r.get('decision') or 'unspecified'}."
            )
            completed_visible = True
        else:
            completion_text = "Under review as of this cutoff (no completion visible yet)."
            completed_visible = False

        econ_sig = "economically significant" if r.get("economically_significant") else "not economically significant"
        excerpt = (
            f"OIRA EO 12866 review received {r['date_received']} for RIN {rin} "
            f"({r.get('agency') or r.get('agency_code') or 'unknown agency'}): "
            f"\"{r.get('title') or ''}\". Stage: {r.get('stage') or 'unspecified'}. "
            f"{econ_sig.capitalize()}. {completion_text}"
        )

        results.append({
            "evidence_id": None,
            "regulator": r.get("agency") or r.get("agency_code") or "OIRA",
            "jurisdiction": "US",
            "title": f"OIRA EO 12866 review received: {r.get('title') or rin}",
            "source_url": "https://www.reginfo.gov/public/do/eoAdvancedSearchMain",
            "publication_date": r["date_received"],
            "first_known_date": None,
            "retrieval_date": RETRIEVAL_DATE,
            "document_type": "oira_review_received",
            "tier": "B",
            "original_or_revised": "original",
            "version_confidence": "high" if r.get("source_report") else "medium",
            "date_verification": (
                f"date_received is the reginfo.gov EO 12866 review-tracking field, publicly "
                f"listed on the day OIRA receives the rule for review; taken from "
                f"data/raw/us_reginfo/oira_reviews.jsonl (source_report={r.get('source_report')})."
                + (
                    " date_completed is included only because it is also before the cutoff."
                    if completed_visible
                    else " date_completed is NOT included because it is on/after the cutoff "
                         "(or not yet completed); the review is reported as still pending."
                )
            ),
            "extracted_claims": [
                f"OIRA received this rule for EO 12866 review on {r['date_received']}.",
                completion_text,
            ],
            "content_excerpt": excerpt[:1200],
            "source_hash": None,
            "stored_copy": None,
        })
    return results


# ---------------------------------------------------------------------------
# 6. Self-test
# ---------------------------------------------------------------------------
def _selftest():
    ok = True

    print("== agenda_evidence_for_rin: RIN 3235-AM96 ==")
    ev = agenda_evidence_for_rin("3235-AM96", "2026-09-25")
    print(f"  {len(ev)} evidence items found")
    for item in ev:
        print(f"  - pub_date={item['publication_date']} tier={item['tier']} "
              f"doc_type={item['document_type']}")
        print(f"    excerpt: {item['content_excerpt'][:160]}...")
    if not ev:
        print("  WARNING: expected at least one Unified Agenda entry for 3235-AM96 "
              "(SEC) if agenda_entries.jsonl has been collected.")
        ok = False
    for item in ev:
        assert item["tier"] == "B"
        assert item["document_type"] == "regulatory_agenda_entry"
        assert item["evidence_id"] is None
        assert _parse_date(item["publication_date"]) < _parse_date("2026-09-25")

    print("\n== agenda_evidence_for_rin: leakage check (before_date before any edition) ==")
    ev_none = agenda_evidence_for_rin("3235-AM96", "2010-01-01")
    print(f"  {len(ev_none)} evidence items found (expected 0)")
    assert len(ev_none) == 0, "leakage: got evidence before any edition existed"

    print("\n== oira_evidence_for_rin: RIN 3235-AM96 ==")
    ev2 = oira_evidence_for_rin("3235-AM96", "2026-09-25")
    print(f"  {len(ev2)} evidence items found")
    for item in ev2:
        print(f"  - pub_date={item['publication_date']} doc_type={item['document_type']}")
        print(f"    excerpt: {item['content_excerpt'][:160]}...")
    for item in ev2:
        assert item["tier"] == "B"
        assert item["document_type"] == "oira_review_received"
        assert item["evidence_id"] is None

    # Second RIN: a finalized rule, chosen after collection (see NOTES.md for why).
    finalized_rin = os.environ.get("REGINFO_SELFTEST_FINALIZED_RIN", "1210-AB88")
    print(f"\n== agenda_evidence_for_rin: finalized RIN {finalized_rin} ==")
    ev3 = agenda_evidence_for_rin(finalized_rin, "2026-09-25")
    print(f"  {len(ev3)} evidence items found")
    for item in ev3:
        print(f"  - pub_date={item['publication_date']} excerpt: {item['content_excerpt'][:160]}...")
    if not ev3:
        print(f"  WARNING: no Unified Agenda entries found for {finalized_rin}.")
        ok = False

    print(f"\n== oira_evidence_for_rin: finalized RIN {finalized_rin}, completion visibility ==")
    all_reviews = _read_jsonl(OIRA_REVIEWS_PATH)
    completed = [r for r in all_reviews if r.get("rin") == finalized_rin and r.get("date_completed")]
    if completed:
        r0 = sorted(completed, key=lambda r: r["date_completed"])[0]
        cutoff_before = r0["date_completed"]  # before completion is visible
        ev_before = oira_evidence_for_rin(finalized_rin, cutoff_before)
        ev_after = oira_evidence_for_rin(finalized_rin, "2026-09-25")
        print(f"  cutoff={cutoff_before} (= completion date, so completion NOT yet visible): "
              f"{len(ev_before)} items")
        for item in ev_before:
            assert "Under review as of this cutoff" in item["content_excerpt"] or \
                   item["publication_date"] < cutoff_before
        print(f"  cutoff=2026-09-25 (completion visible): {len(ev_after)} items")
        for item in ev_after:
            print(f"    excerpt: {item['content_excerpt'][:160]}...")
        ok = ok and len(ev_after) >= len(ev_before)
    else:
        print(f"  WARNING: no completed OIRA review found for {finalized_rin} in oira_reviews.jsonl")
        ok = False

    print("\n== SELFTEST", "PASSED" if ok else "COMPLETED WITH WARNINGS", "==")
    return ok


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collect-agenda", action="store_true", help="download+parse Unified Agenda editions")
    parser.add_argument("--collect-oira", action="store_true", help="download+parse EO 12866 review reports")
    parser.add_argument("--write-editions", action="store_true", help="write agenda_editions.json")
    parser.add_argument("--all", action="store_true", help="run all collection steps")
    parser.add_argument("--selftest", action="store_true", help="run the self-test using RIN 3235-AM96 + a finalized RIN")
    parser.add_argument("--limit-editions", type=int, default=None, help="debug: only process the first N editions")
    args = parser.parse_args()

    if args.all:
        write_agenda_editions()
        collect_agenda(limit_editions=args.limit_editions)
        collect_oira()
        return

    if args.write_editions:
        write_agenda_editions()
    if args.collect_agenda:
        collect_agenda(limit_editions=args.limit_editions)
    if args.collect_oira:
        collect_oira()
    if args.selftest:
        success = _selftest()
        sys.exit(0 if success else 1)

    if not any([args.collect_agenda, args.collect_oira, args.write_editions, args.selftest]):
        parser.print_help()


if __name__ == "__main__":
    main()
