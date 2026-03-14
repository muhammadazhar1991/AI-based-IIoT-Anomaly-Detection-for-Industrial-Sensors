import json
import boto3
from datetime import datetime
from decimal import Decimal

# connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses', region_name='us-east-2')

event_table = dynamodb.Table('IOT_EvEntLog')
alarm_table = dynamodb.Table('IOT_AlarmsLog')


# -------------------------
# Email Function
# -------------------------
def send_email(message):

    ses.send_email(
        Source='engr.azher.ma@gmail.com',
        Destination={
            'ToAddresses': ['engr.azher.ma@gmail.com']
        },
        Message={
            'Subject': {
                'Data': 'IIoT Alarm Notification'
            },
            'Body': {
                'Text': {
                    'Data': message
                }
            }
        }
    )


def lambda_handler(event, context):

    print("EVENT RECEIVED:", event)

    device_id = event.get("device_id", "tank_1")

    pressure = Decimal(str(event.get("pressure", 0)))
    temperature = Decimal(str(event.get("temperature", 0)))
    level = Decimal(str(event.get("level", 0)))
    anomaly = int(event["anomaly"])

    timestamp = datetime.utcnow().isoformat()

    # -------------------------
    # 1. Store Event Log
    # -------------------------
    event_table.put_item(
        Item={
            "device_id": device_id,
            "timestamp": timestamp,
            "pressure": pressure,
            "temperature": temperature,
            "level": level,
            "anomaly": anomaly
        }
    )

    print("Event stored")

    if anomaly == 1:
        send_email(f"Anomaly detected in device: {device_id}")

    # -------------------------
    # 2. Check Alarm Conditions
    # -------------------------
    alarm_triggered = False
    alarm_type = ""

    if pressure > 6.5:
        alarm_triggered = True
        alarm_type = "High Pressure"

    elif temperature < 48:
        alarm_triggered = True
        alarm_type = "Low Temperature"

    elif level > 55:
        alarm_triggered = True
        alarm_type = "High Level"

    # -------------------------
    # 3. Store Alarm Log
    # -------------------------
    if alarm_triggered:

        alarm_table.put_item(
            Item={
                "device_id": device_id,
                "timestamp": timestamp,
                "alarm_type": alarm_type,
                "pressure": pressure,
                "temperature": temperature,
                "level": level,
                "severity": "critical"
            }
        )

        print("Alarm stored:", alarm_type)

        send_email(f"Alarm detected: {alarm_type}\nPressure: {pressure}\nTemperature: {temperature}\nLevel: {level}")
        

    return {
        "statusCode": 200,
        "body": json.dumps("Processed")
    }