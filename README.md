# AI based Anomaly Detection with Sensor Data & AWS IoT core

## 🔹 Project Overview
This project demonstrates real-time AI based anomaly detection using sensor data.  
It integrates **AI algorithms** for anomaly prediction, **MQTT** for sensor data streaming, **AWS IoT** for cloud communication and **Node Red** for visualization.  

**Key Features:**
- Real-time sensor data collection and publishing
- AI-based anomaly detection
- Integration with AWS IoT for cloud monitoring
- Dashboard-ready data outputs for visualization

## 🔹 Demo
📹 [Loom Video Demo] https://www.loom.com/share/3d862475c23d4876a0a90bcfd973dc92 – See the project in action.

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

## 🔹 Future Improvements

Add web dashboard for live visualization

Deploy as a SaaS solution with multi-user support

Include alert notifications on anomaly detection

## 🔹 Contact

GitHub: https://github.com/muhammadazhar1991

Email: engr.azher.ma@gmail.com
