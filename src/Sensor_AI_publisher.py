import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt
import time
import json
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import logging
import uuid

# -------------------------------
# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
client_id = f"PythonPublisher-{uuid.uuid4()}"
# AWS IoT endpoint and topic
endpoint = "a2r13ho0t1y9ik-ats.iot.us-east-2.amazonaws.com"
topic = "AnomaliesDetect"

# Paths to certificates (use simple path, no spaces)
ca_path = r"C:\Users\engra\Desktop\AI-Anomaly-Detection\AmazonRootCA1.pem"
cert_path = r"C:\Users\engra\Desktop\AI-Anomaly-Detection\b6cffa52bccab626b5c42c6b25dd1c62a91ffe5db292ed890765204ec0765509-certificate.pem.crt"
key_path = r"C:\Users\engra\Desktop\AI-Anomaly-Detection\b6cffa52bccab626b5c42c6b25dd1c62a91ffe5db292ed890765204ec0765509-private.pem.key"

# Create MQTT client using callback API v2
client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv31)
client.tls_set(ca_certs=ca_path, certfile=cert_path, keyfile=key_path)

# -------------------------------
# Prepare Dataset & Train Model
# -------------------------------
np.random.seed(42)
pressure = np.random.normal(5, 0.4, 1000)
temperature = np.random.normal(58, 0.5, 1000)
level = np.random.normal(45, 0.5, 1000)

df = pd.DataFrame({'pressure': pressure, 'temperature': temperature, 'level': level})
df = df.round(3)

# Train IsolationForest on normal data
normal_df = df.iloc[:800]
scaler = StandardScaler()
X_train = scaler.fit_transform(normal_df[['pressure','temperature','level']])
model = IsolationForest(contamination=0.03, random_state=42, n_estimators=100)
model.fit(X_train)

# Inject anomalies
df.loc[100:149, 'pressure'] += 1.5
df.loc[200:249, 'level'] += 10
df.loc[300:349, 'temperature'] -= 10

# Predict anomalies
X_all = scaler.transform(df[['pressure','temperature','level']])
df['anomaly'] = model.predict(X_all)
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})  # 1 = anomaly

df.to_csv('sensor_data.csv', index=False, sep=';')
df = pd.read_csv('sensor_data.csv', sep=';')
df.columns = df.columns.str.strip()

#publish functoin
def publish_data():
    for row_index in range(1000):
        row = df.iloc[row_index]

        payload = {
            "pressure": float(row["pressure"]),
            "temperature": float(row["temperature"]),
            "level": float(row["level"]),
            "anomaly": float(row["anomaly"])
        }

        result = client.publish(topic, json.dumps(payload), qos=1)

        # wait until AWS IoT confirms delivery
        result.wait_for_publish()

        print(f"Published row {row_index}")

        time.sleep(0.1)

    print("All messages published.")

# -------------------------------
# MQTT Callbacks
# -------------------------------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to AWS IoT Core ✅")
        # Start publishing after connection
       
    else:
        print(f"Failed to connect, return code {rc}")

def on_disconnect(client, userdata, rc):
    print(f"Disconnected rc={rc}")

time.sleep(0.3)
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# -------------------------------
# Publish Function
# -------------------------------



# -------------------------------
# Connect & Start Loop
# -------------------------------
client.loop_start()

client.connect(endpoint, 8883, keepalive=60)

# wait until connection is established
time.sleep(3)

# start publishing
publish_data()

# Keep script running to allow async callbacks
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()