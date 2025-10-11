import pandas as pd
import numpy as np

# Generate timestamps
timestamps = pd.date_range(start='2025-10-11', periods=1000, freq='min')

# Normal ranges
heart_rate = np.random.normal(75, 5, size=len(timestamps))
spo2 = np.random.normal(98, 1, size=len(timestamps))
temperature = np.random.normal(36.6, 0.3, size=len(timestamps))

# Introduce anomalies
for i in np.random.choice(len(timestamps), 10, replace=False):
    heart_rate[i] += np.random.choice([-20, 20])
    spo2[i] += np.random.choice([-5, 5])
    temperature[i] += np.random.choice([-2, 2])

df = pd.DataFrame({
    'timestamp': timestamps,
    'heart_rate': heart_rate,
    'spo2': spo2,
    'temperature': temperature
})

df.to_csv('synthetic_data.csv', index=False)
print(df.head())
