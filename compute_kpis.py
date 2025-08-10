import pandas as pd, json, matplotlib.pyplot as plt, os
os.makedirs('reports', exist_ok=True)
df = pd.read_json('data/telemetry.jsonl', lines=True)
kpis = {
    'chan_util_avg': float(df['chan_util'].mean()),
    'clients_p95': float(df['clients'].quantile(0.95)),
    'retries_avg': float(df['retries_pct'].mean()),
    'rssi_avg': float(df['rssi_avg'].mean())
}
with open('reports/kpis.json','w') as f: json.dump(kpis, f, indent=2)
plt.figure(); df['chan_util'].plot(); plt.title('Channel Utilization'); plt.savefig('reports/chan_util.png', dpi=160)
print('Saved reports/kpis.json and plot.')
