from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np


df = pd.read_csv('sensor_data.csv', sep=';')  
# Train model on normal data
normal_df = df.iloc[:800]
scaler = StandardScaler()
X_train = scaler.fit_transform(normal_df[['pressure','temperature','level']])
model = IsolationForest(contamination=0.03, random_state=42, n_estimators=100)
model.fit(X_train)

# Predict anomalies
X_all = scaler.transform(df[['pressure','temperature','level']])
df['anomaly'] = model.predict(X_all)
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})  # 1 = anomaly

df.to_csv('sensor_data.csv', index=False, sep=';')
df = pd.read_csv('sensor_data.csv', sep=';')
df.columns = df.columns.str.strip()


# Publish anomalies to MQTT / alert system
for i, row in df.iterrows():
    print(f"Pressure: {row['pressure']}, Temperature: {row['temperature']}, Level: {row['level']}, Anomaly: {row['anomaly']}")

