import requests
import time
import random
import uuid

API_URL = 'http://localhost:8000/telemetry'

def send_once(device_id):
    payload = {
        "device_id": device_id,
        "ts": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "metrics": {
            "vibration": round(random.uniform(0.5, 5.0), 3),
            "temp": round(random.uniform(30, 90), 2)
        }
    }
    r = requests.post(API_URL, json=payload)
    print(device_id, r.status_code, r.text)

if __name__ == '__main__':
    device = f"pump-{str(uuid.uuid4())[:8]}"
    while True:
        send_once(device)
        time.sleep(1)