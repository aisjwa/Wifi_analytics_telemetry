import json, random, os, time
os.makedirs('data', exist_ok=True)
with open('data/telemetry.jsonl','w') as f:
    for t in range(600):
        rec = {
            'ts': t,
            'chan_util': round(random.uniform(10,70),1),
            'clients': random.randint(2,15),
            'retries_pct': round(random.uniform(0,12),2),
            'rssi_avg': round(random.uniform(-70,-55),1)
        }
        f.write(json.dumps(rec)+'\n')
print('Wrote data/telemetry.jsonl')
