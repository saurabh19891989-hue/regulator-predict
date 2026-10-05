# Daily data collection and Google Drive storage audit

**Checked 2026-10-05. Regulatory research is paused at the user's request.** This audit concerns the separate NNML daily market collector.

## Result

**Collection and automatic Drive copying work, with data-quality and archive-lineage exceptions.** Eight normal sessions have full reported coverage for the configured subset and passed representative fresh-spot/integrity checks. All 10 saved daily sessions are present on Drive. Do not interpret every saved day as usable trading data.

Window: **September 21–October 5, 2026**, 15 calendar days. The most recent 10 calendar days contain 5 normal trading days; all 5 are present. No September 21 session exists in this archive, whose earliest date is September 22. Weekends require no market session; October 2 is an official NSE holiday.

## Evidence

- Drive inventories: 9,430 objects, 13,129,092,725 bytes (13.13 GB / 12.23 GiB), 4,653 closed raw chunks across 10 daily folders.
- All 10 Drive-side daily receipts report PASS_IMMUTABLE_COPY_ONEWAY_CHECK. Daily upload logs and historical one-way check logs agree. Receipt counts precede receipt/coverage uploads, explaining 620 current objects versus 618 in normal-day receipts.
- Fresh October 5 rclone checksum check at 16:18:59 IST: 620 matching files, 0 differences, exit 0. Today's original verification was 15:52:27 IST.
- Sample audit: 4 closed raw chunks per day, 40 total; 51,179 frames. Every sample passes SHA-256 versus sidecar, MD5 versus Drive metadata, file-size/frame-count checks, CRC and protobuf decoding. Zero sample truncation/errors.
- Every closed raw chunk has a listed manifest; no orphan manifests. All 10 saved PLAN.json hashes match CAPTURE_RESULT plan hashes.
- Eight normal sessions from September 23 onward: 210 stocks before September 30, 213 thereafter; 6 indices and all 6,480/6,556 planned instruments observed. Reported minimum stock-spot coverage is 372–373 minutes. Every sampled spot trade timestamp on those 8 days belongs to its session date.
- October 5 closed at 15:31 IST: 24,167,141 feed updates, zero slot/decode errors, 213 stocks / 6 indices / 6,556 instruments with reported coverage; health at 16:15 IST has no alerts, 55.6 GiB free. Next capture: October 6 at 09:05 IST; upload at 15:50 IST.

## Day-by-day review

| Date | Drive objects | Updates | Collection assessment |
|---|---:|---:|---|
| 2026-09-21 | — | — | No folder in this archive; earliest archived date is September 22 |
| 2026-09-22 | 642 | 7,469,123 | PARTIAL: index gaps and 4 unfinished raw files |
| 2026-09-23 | 620 | 24,174,570 | PASS for planned subset: full reported coverage and sampled fresh spot data |
| 2026-09-24 | 620 | 24,997,795 | PASS for planned subset: full reported coverage and sampled fresh spot data |
| 2026-09-25 | 620 | 25,424,671 | PASS for planned subset: full reported coverage and sampled fresh spot data |
| 2026-09-26 | — | — | Weekend: no session expected |
| 2026-09-27 | — | — | Weekend: no session expected |
| 2026-09-28 | 620 | 25,863,861 | PASS for planned subset: full reported coverage and sampled fresh spot data |
| 2026-09-29 | 620 | 23,883,072 | PASS for planned subset: full reported coverage and sampled fresh spot data |
| 2026-09-30 | 620 | 22,626,776 | PASS for planned subset: full reported coverage and sampled fresh spot data |
| 2026-10-01 | 620 | 24,080,470 | PASS for planned subset: full reported coverage and sampled fresh spot data |
| 2026-10-02 | 3828 | 3,127,212 | NSE holiday: stored reconnect snapshots, not normal trading data |
| 2026-10-03 | — | — | Weekend: no session expected |
| 2026-10-04 | — | — | Weekend: no session expected |
| 2026-10-05 | 620 | 24,167,141 | PASS for planned subset: full reported coverage and sampled fresh spot data |

## Concrete exceptions

### September 22: incomplete first archived session

Stock coverage reports 210/210, but index coverage is only 1/6 spots and 0/6 options, with 11 alerts. Drive also contains 4 unfinished `.raw.zst.partial` files, one per slot. These bytes are preserved, but their integrity/completeness is not certified by the closed-chunk sidecar sample checks. Do not treat this as a fully clean index/options day.

### October 2: holiday snapshots falsely appear healthy

The official [NSE F&O holiday circular](https://nsearchives.nseindia.com/content/circulars/FAOP71777.pdf) lists October 2 as a holiday. The weekday timer still ran. The session recorded 3,127,212 feed updates, 477 connections per slot and 1,908 reconnect errors across 4 slots. Each of the 4 sampled chunks has 2 frames; all 219 sampled spot entries have last-trade dates of October 1, with zero October 2 last trades.

Coverage nevertheless reports 6,556/6,556 instruments and no alerts. The decoder buckets observations using feed `currentTs`; the coverage checker counts those minutes and observed keys, without testing `ltpc.ltt` freshness. Repeated holiday initial snapshots can therefore pass the 300-minute coverage test. Preserve this archive as holiday diagnostic data; exclude it from normal trading-session research.

### Dated contract master missing from Drive backups

All 10 daily Drive roots contain CAPTURE_RESULT, COVERAGE, DRIVE_RECEIPT, PLAN and 4 subscription lists, but no dated instrument master. The postclose script copies only PLAN/subscriptions into the capture archive. The 10 dated `instrument-master-YYYY-MM-DD.json.gz` files still exist under `/var/lib/nnml-lean-capture/plan/` on the server.

PLAN maps chosen keys to underlyings but does not fully preserve per-contract expiry/strike/option-type identity. This previously recorded archive-lineage gap remains unresolved. Those historical master files should be preserved on Drive before any later local-plan cleanup.

### September 21

No folder was found for September 21 in this exact archive. Its earliest folder is September 22. This is not evidence that every other archive lacks September 21 data, and no data was manufactured to fill it.

## Recommended corrections

1. Back up dated instrument masters with each daily session, including the 10 historical files still held locally.
2. Make collection/health checks exchange-calendar aware and validate source trade/quote freshness, rather than message time alone.
3. Mark incomplete raw closure or index coverage explicitly in session status.

This request was an inspection: production services, schedules, archive contents and credentials were not changed. No model research was restarted. Older local capture copies were automatically released by the existing pipeline after PASS receipts; their corresponding Drive folders are present.

## Scope and limits

Full Drive inventories and metadata were read for all 10 sessions. Historical full-copy receipts were corroborated; only October 5 received a new full local-to-Drive checksum comparison because older local raw sessions have been released. Forty representative closed chunks were decoded, not every historical byte. Raw downloads were transient in memory on the server; audit outputs contain metadata and findings.

Coverage applies to the configured F&O universe: spot, front future and ATM ± 3 strike CE/PE options for 2 nearest expiries. It is not every listed strike/expiry. Instrument presence is not proof all option quotes/Greeks are fresh or usable, and these samples do not prove uninterrupted every-minute coverage.

Machine evidence: `data/audits/DAILY_COLLECTION_STORAGE_20261005.json`, `DAILY_COLLECTION_FRESH_CHECK_20261005.json`, `DAILY_COLLECTION_SUMMARY_20261005.json`; repeatable read-only script: `tools/audit_daily_storage_20261005.py`.
