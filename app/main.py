import threading
import time
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import telemetry_simulator
from .db import models, database
from .schemas.telemetry import Telemetry, TelemetryCreate
from .services import telemetry_service
from .utils.config import settings
from .utils.logger import log

# Create database tables on startup
try:
    models.Base.metadata.create_all(bind=database.engine)
    log.info("Database tables verified/created.")
except Exception as e:
    log.error(f"Error creating database tables: {e}")


app = FastAPI(
    title="Predictive Maintenance API",
    description="An API for ingesting and retrieving IoT telemetry data.",
    version="1.0.0",
)

@app.on_event("startup")
def startup_event():
    """
    Actions to perform on application startup.
    This starts the telemetry simulator in a background thread.
    """
    log.info("Application startup...")
    simulator_thread = threading.Thread(
        target=telemetry_simulator.run_simulator,
        args=(settings.SIMULATOR_INTERVAL_SECONDS,),
        daemon=True  # Allows main thread to exit even if this thread is running
    )
    simulator_thread.start()
    log.info("Telemetry simulator started in a background thread.")

@app.post("/telemetry", response_model=Telemetry, status_code=201)
def create_telemetry_endpoint(
    telemetry: TelemetryCreate,
    db: Session = Depends(database.get_db)
):
    """
    Endpoint to manually create a new telemetry record.
    """
    log.info(f"Received request to create telemetry for device: {telemetry.device_id}")
    return telemetry_service.create_telemetry(db=db, telemetry=telemetry)

@app.get("/telemetry", response_model=List[Telemetry])
def read_telemetry_endpoint(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db)
):
    """
    Endpoint to retrieve a paginated list of the latest telemetry records.
    """
    log.info(f"Fetching paginated telemetry data with skip={skip} and limit={limit}")
    telemetry_data = telemetry_service.get_telemetry_paginated(db, skip=skip, limit=limit)
    return telemetry_data

@app.get("/telemetry/{device_id}", response_model=List[Telemetry])
def read_device_telemetry_endpoint(
    device_id: str,
    db: Session = Depends(database.get_db)
):
    """
    Endpoint to retrieve all telemetry records for a specific device.
    """
    log.info(f"Fetching telemetry data for device_id: {device_id}")
    db_telemetry = telemetry_service.get_telemetry_by_device_id(db, device_id=device_id)
    if not db_telemetry:
        log.warning(f"No telemetry data found for device_id: {device_id}")
        raise HTTPException(status_code=404, detail="Telemetry data not found for this device")
    return db_telemetry
