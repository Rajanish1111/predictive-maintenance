import time
import random
from faker import Faker
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import Telemetry
from app.utils.logger import log

fake = Faker()

def generate_fake_data(device_id: str) -> dict:
    """Generates a single, realistic telemetry data point."""
    return {
        "device_id": device_id,
        "temperature": round(random.uniform(15.0, 45.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "latitude": float(fake.latitude()),
        "longitude": float(fake.longitude()),
        "status": random.choice(["active", "inactive", "maintenance_required", "error"])
    }

def run_simulator(interval_seconds: int):
    """
    Runs the telemetry data simulator.

    This function continuously generates data for a set of devices
    and inserts it into the database at a specified interval.
    """
    log.info(f"Telemetry simulator will run every {interval_seconds} seconds.")
    device_ids = [f"device_{i:03}" for i in range(1, 6)]  # 5 simulated devices

    while True:
        time.sleep(interval_seconds)
        db: Session = SessionLocal()
        try:
            device_to_update = random.choice(device_ids)
            data = generate_fake_data(device_to_update)
            telemetry_record = Telemetry(**data)
            db.add(telemetry_record)
            db.commit()
            log.info(f"Simulator inserted data for {device_to_update}: Temp={data['temperature']}°C, Hum={data['humidity']}%")
        except Exception as e:
            log.error(f"Simulator error: Failed to insert data. Reason: {e}")
            db.rollback()
        finally:
            db.close()
