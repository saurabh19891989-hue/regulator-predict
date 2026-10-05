# Daily collection check — 2026-10-04

The recurring collection found in the user's existing workspace belongs to the NNML market-data programme.
It is separate from the historical regulatory-prediction dataset.

Read-only checks directly contacted the configured OVH collector and its authenticated rclone Google Drive
remote. No credentials were printed or modified. The connected Drive search did not locate these files;
the collector's own authenticated remote provided direct confirmation.

- Current health record: checked2026-10-04T04:00:10Z, no alerts,56.3GiB disk free,292.7token days remaining.
- October1 session: CLOSED,24,080,470feed updates, successful immutable Drive-copy receipt.
- October2 session: CLOSED,3,127,212feed updates,213/213stock spot and options coverage,6/6index spot/options
  coverage,6,556/6,556instruments with data. Coverage here means instruments observed; it does not independently
  establish freshness or research usability of every observation.
- Google Drive directly lists daily session folders fromSeptember22 throughOctober2, excludingSeptember26/27.
- October2 Drive folder contains CAPTURE_RESULT.json, COVERAGE.json, PLAN.json, DRIVE_RECEIPT.json and four slot
  folders. Its Drive-side receipt is PASS_IMMUTABLE_COPY_ONEWAY_CHECK, verified2026-10-02T10:33:01Z,
  with3,826objects and361,101,867bytes (344.374MiB).
- Capture and post-close timers are armed forMondayOctober5; the capture service is inactive onSundayOctober4.

Remote archive path:
`UpstoxMarketDBArchive/research/ml-prediction/native-universe/lean-capture-v1/`.
The existing health-check task is nnml-capture-health-check (Monday/Thursday17:00IST).

For the regulatory project, no daily collection/upload automation was found in its repository or local Codex
automation directory. Its current frozen 327 threads and 1,785 evidence records remain in the local/Git
workspace. This check does not claim that regulatory cases are being collected every day or uploaded to Drive.

## Follow-up check — 2026-10-05, about05:07IST

Direct systemd timer inspection confirms capture scheduled today09:05IST, health09:30IST and post-close
15:50IST. At this early-morning check the latest health snapshot was October4 at16:15IST; it still records
October2 as the latest closed session and successful Drive receipt, with no alerts. October5 capture was not
yet due, so this check does not assert that today's data has already been captured or uploaded.

## Follow-up check — 2026-10-05, about10:08IST

The09:30IST health snapshot now reports capture_service active, no alerts and an open October5 session with
65,271,181 local bytes. A live systemctl check confirms the capture service is active. The October5 Google
Drive session directory is not present yet; post-close processing remains scheduled15:50IST. Latest verified
completed upload remains October2. Current collection is confirmed; today's completed Drive upload is pending.

## Follow-up check — 2026-10-05, about15:36IST

Live journal confirms today's capture CLOSED successfully at15:31IST, with24,167,141 feed updates
across four slots. The service is inactive after normal completion. Next capture isOctober6 09:05IST;
today's post-close Drive copy remains scheduled15:50IST. The09:30 health snapshot is stale and does not
represent current capture status. Today's Drive upload is still pending at this check.

## Follow-up check — 2026-10-05, 15:50IST

Today's CAPTURE_RESULT.json confirms CLOSED withzero slot/decode errors and24,167,141feed updates.
The automatic nnml-lean-postclose.service started precisely15:50IST and is activating/start at15:50:09.
No October5 DRIVE_RECEIPT.json exists yet. Automatic post-close upload is running; completed copy verification
is pending. October2 remains the latest verified completed Drive receipt. The09:30 health snapshot is stale.

## Completed 15-day collection/storage audit — 2026-10-05

October5 Drive copy is now verified: automatic receipt at15:52:27IST; fresh checksum comparison
at16:18:59IST passes620 files withzero differences. Ten dailyDrivefolders (September22–October5)
are present, totalling13.13GB. Forty sampled closed chunks pass SHA256/MD5/CRC/decoding.
Important qualifications: September22 index coverage is incomplete and4raw partials remain; October2
is an NSE holiday whose stored sampled prices haveOctober1last-trade timestamps despitegreen coverage;
the dated instrument masters remain local and are absent fromdailyDrivearchives. Eight normal sessions
fromSeptember23 onward havefull reported plannedcoverage. Full audit: docs/DAILY_COLLECTION_AUDIT_20261005.md.
Regulatory research remains paused byuser; no production collection changes were made.
