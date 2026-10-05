"""Read-only audit of known NNML daily capture archive; never accesses token contents."""
import json
from pathlib import Path
import subprocess

REMOTE_CODE = r'''
import concurrent.futures, datetime, hashlib, io, json, struct, subprocess, sys, zlib
from collections import Counter
sys.path.insert(0, '/opt/nnml-lean-capture')
import zstandard
from leancap import MarketDataFeed_pb2 as pb
R=['rclone','--config','/etc/rclone-ovh/rclone.conf']
BASE='gdrive_marketdb:UpstoxMarketDBArchive/research/ml-prediction/native-universe/lean-capture-v1'
def run(*args):
 p=subprocess.run(R+list(args),capture_output=True,timeout=120)
 if p.returncode: raise RuntimeError(p.stderr.decode()[-500:])
 return p.stdout
def fetch(path): return run('cat', BASE+'/'+path)
def job(date):
 prefix='session_date='+date
 inv=json.loads(run('lsjson',BASE+'/'+prefix,'--recursive','--files-only','--hash'))
 paths={x['Path']:x for x in inv}
 meta={name:json.loads(fetch(prefix+'/'+name)) for name in ['CAPTURE_RESULT.json','COVERAGE.json','DRIVE_RECEIPT.json','PLAN.json']}
 c=meta['CAPTURE_RESULT.json']; cov=meta['COVERAGE.json'];plan=meta['PLAN.json']
 plan_bytes=fetch(prefix+'/PLAN.json')
 raw=sorted(x for x in paths if x.endswith('.raw.zst'))
 manifests=[x for x in paths if x.endswith('.raw.zst.manifest.json')]
 partial=[x for x in paths if x.endswith('.partial')]
 spots={x['underlying_key']:x['symbol'] for x in plan['stock_table']}
 sample=[]
 midnight=int(datetime.datetime.fromisoformat(date).replace(tzinfo=datetime.timezone(datetime.timedelta(hours=5,minutes=30))).timestamp()*1000)
 for slot in range(1,5):
  candidates=[x for x in raw if x.startswith('slot='+str(slot)+'/')]
  if not candidates: continue
  # Date/slot-dependent first/middle/last selection; four chunks per day, not a full raw audit.
  pick=candidates[[0,len(candidates)//2,len(candidates)-1][(int(date[-2:])+slot)%3]]
  manifest=json.loads(fetch(prefix+'/'+pick+'.manifest.json'))
  binary=fetch(prefix+'/'+pick)
  row={'slot':slot,'path':pick,'bytes':len(binary),'sha256_ok':hashlib.sha256(binary).hexdigest()==manifest['sha256'],
       'md5_ok':hashlib.md5(binary).hexdigest()==paths[pick].get('Hashes',{}).get('md5'),
       'size_ok':len(binary)==manifest['compressed_bytes']==paths[pick]['Size'],
       'manifest_frames':manifest['frames'],'frames':0,'crc_errors':0,'decode_errors':0,'truncated_records':0,
       'spot_updates':0,'spot_updates_trade_same_day':0,'spot_keys':set(),'same_day_spot_keys':set(),
       'spot_trade_date_counts':Counter(),'current_ts_min':None,'current_ts_max':None,'recv_ns_min':None,'recv_ns_max':None}
  assert binary[:8]==b'UMDBRAW1'
  with zstandard.ZstdDecompressor().stream_reader(io.BytesIO(binary[8:])) as stream:
   while True:
    head=stream.read(12)
    if not head: break
    if len(head)!=12: row['truncated_records']+=1;break
    nh,np,crc=struct.unpack('>III',head);h=stream.read(nh);payload=stream.read(np)
    if len(h)!=nh or len(payload)!=np: row['truncated_records']+=1;break
    header=json.loads(h);row['frames']+=1
    if zlib.crc32(payload)&0xffffffff!=crc:row['crc_errors']+=1
    ts=header.get('current_ts');ns=header.get('recv_utc_ns')
    for field,val in [('current_ts',ts),('recv_ns',ns)]:
     if val:
      row[field+'_min']=val if row[field+'_min'] is None else min(row[field+'_min'],val)
      row[field+'_max']=val if row[field+'_max'] is None else max(row[field+'_max'],val)
    try:
     message=pb.FeedResponse();message.ParseFromString(payload)
     for key,feed in message.feeds.items():
      if key not in spots:continue
      which=feed.WhichOneof('FeedUnion')
      if which=='ltpc':ltpc=feed.ltpc
      elif which=='fullFeed':
       union=feed.fullFeed.WhichOneof('FullFeedUnion')
       if union=='marketFF':ltpc=feed.fullFeed.marketFF.ltpc
       elif union=='indexFF':ltpc=feed.fullFeed.indexFF.ltpc
       else:continue
      elif which=='firstLevelWithGreeks':ltpc=feed.firstLevelWithGreeks.ltpc
      else:continue
      row['spot_updates']+=1;row['spot_keys'].add(key)
      if ltpc.ltt:
       day=datetime.datetime.fromtimestamp(ltpc.ltt/1000,datetime.timezone(datetime.timedelta(hours=5,minutes=30))).date().isoformat()
       row['spot_trade_date_counts'][day]+=1
       if midnight<=ltpc.ltt<midnight+86400000:
        row['spot_updates_trade_same_day']+=1;row['same_day_spot_keys'].add(key)
    except Exception as exc:
     row['decode_errors']+=1;row.setdefault('decode_error_examples',[])
     if len(row['decode_error_examples'])<2:row['decode_error_examples'].append(repr(exc))
  row['frame_count_ok']=row['frames']==manifest['frames']
  row['spot_keys']=len(row['spot_keys']);row['same_day_spot_keys']=len(row['same_day_spot_keys'])
  sample.append(row)
 per=cov.get('per_underlying',{})
 stocks=[v for v in per.values() if v.get('kind')=='EQUITY']
 return {'session_date':date,'file_count':len(inv),'bytes':sum(x['Size'] for x in inv),'raw_files':len(raw),'manifest_files':len(manifests),
 'raw_without_manifest':[x for x in raw if x+'.manifest.json' not in paths],'orphan_manifest':[x for x in manifests if x[:-14] not in paths],
 'partial_files':partial,'receipt':meta['DRIVE_RECEIPT.json'],'capture_result':c,
 'coverage':{k:v for k,v in cov.items() if k!='per_underlying'},
 'stock_spot_minutes_min':min((v['spot_minutes'] for v in stocks),default=None),
 'stock_spot_minutes_max':max((v['spot_minutes'] for v in stocks),default=None),
 'plan_hash_ok':hashlib.sha256(plan_bytes).hexdigest()==c['plan_sha256'],
 'plan_stocks':plan['stocks'],'plan_total_keys':plan['total_keys'],
 'root_files':sorted(x for x in paths if '/' not in x),
 'sampled_raw_chunks':sample}
dates=sorted(x['Name'].split('=',1)[1] for x in json.loads(run('lsjson',BASE,'--dirs-only')) if x['Name'].startswith('session_date=') and '2026-09-21'<=x['Name'].split('=',1)[1]<='2026-10-05')
result={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'window_start':'2026-09-21','window_end':'2026-10-05','archive':BASE,'dates':dates,'sessions':[],'errors':[],'method':'Full Drive inventories and daily metadata; four sampled raw chunks per session, SHA256/MD5/CRC/protobuf/freshness checks. Not a full archive byte-level or all-instrument freshness audit.'}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 futures={pool.submit(job,d):d for d in dates}
 for f in concurrent.futures.as_completed(futures):
  try:result['sessions'].append(f.result())
  except Exception as exc:result['errors'].append({'date':futures[f],'error':repr(exc)})
result['sessions'].sort(key=lambda x:x['session_date'])
print(json.dumps(result))
'''

result = subprocess.run([
    "ssh", "-i", "C:/Users/saura/.ssh/id_ed25519_smc", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15",
    "root@57.129.151.13", "/opt/nnml-lean-capture/venv/bin/python -"
], input=REMOTE_CODE, capture_output=True, text=True, encoding="utf-8", timeout=900)
if result.returncode:
    raise SystemExit(result.stderr[-2000:])
obj = json.loads(result.stdout)
target = Path(__file__).resolve().parents[1] / "data/audits/DAILY_COLLECTION_STORAGE_20261005.json"
target.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"sessions": len(obj["sessions"]), "errors": obj["errors"], "output": str(target)}, indent=2))
