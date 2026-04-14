# AI based Anomaly Detection with Sensor Data & AWS IoT core

## 🔹 Project Overview
Industrial machines generate continuous sensor data, and undetected anomalies can lead to costly downtime. This project presents a Proof of Concept (PoC) for an IIoT-based anomaly detection system to identify such issues early.  
This PoC simulates sensor data, processes it using Python, and detects anomalies in real time using ML based algorithms. The system is integrated with
 **MQTT** for sensor data streaming, **AWS IoT** for cloud communication and **Node Red** for visualization.  

**Key Features:**
- Real-time sensor data collection and publishing
- AI-based anomaly detection
- Integration with AWS IoT for cloud monitoring
- Dashboard-ready data outputs for visualization

**Industrial Integration (Implemented)**

Integrated MQTT protocol for real-time data streaming between sensor simulation and processing module
Implemented cloud-compatible architecture aligned with AWS IoT services
Demonstrated anomaly detection in both edge (local Python processing) and cloud-ready setup

## 🔹 Demo
📹 https://www.youtube.com/watch?v=z6vmKsaQvAs – See the project in action.

## 🔹 Folder Structure
```text
AI-based-IIoT-Anomaly-Detection-platform
📂 AI-based-IIoT-Anomaly-Detection-platform
├─ 📄 README.md
├─ 📄 requirements.txt
├─ 📂 src
│  ├─ 🐍 Sensor_AI_publisher.py
│  └─ 🐍 AI_anomalydetector.py
├─ 📂 aws_lambda
│  └─ 🐍 lambda_function.py
├─ 📂 screenshots
│  ├─ 🖼 dashboard.png
│  ├─ 🖼 dashboard_Flow.png
│  ├─ 🖼 SQL_DB.png
│  ├─ 🖼 dynamodb_logs.png
│  ├─ 🖼 aws-iot-mqtt.png
│  └─ 🖼 anomaly_email.png
└─ 🖼 architecture.png



## 🔹 Installation

1. **Clone the repository**
```bash
git clone https://github.com/muhammadazhar1991/AI-based-IIoT-Anomaly-Detection.git
cd AI-based-IIoT-Anomaly-Detection

## 🔹 Create a virtual environment (optional)

python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows#

## 🔹 Install dependencies

pip install -r requirements.txt

## 🔹 How to Run

python Sensor_AI_publisher.py

## 🔹 Requirements

Python 3.12

MQTT broker ( AWS IoT)

Libraries listed in requirements.txt

## 🔹 Contact

GitHub: https://github.com/muhammadazhar1991

Email: engr.azher.ma@gmail.com
