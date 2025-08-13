from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import models
from app.schemas.telemetry import TelemetryCreate

def create_telemetry(db: Session, telemetry: TelemetryCreate) -> models.Telemetry:
    """
    Saves a new telemetry record to the database.
    
    Args:
        db: The database session.
        telemetry: The telemetry data to save.
        
    Returns:
        The newly created telemetry database object.
    """
    db_telemetry = models.Telemetry(**telemetry.model_dump())
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry

def get_telemetry_paginated(db: Session, skip: int = 0, limit: int = 100) -> List[models.Telemetry]:
    """
    Retrieves a paginated list of telemetry records.
    
    Args:
        db: The database session.
        skip: The number of records to skip.
        limit: The maximum number of records to return.
        
    Returns:
        A list of telemetry database objects.
    """
    return db.query(models.Telemetry).order_by(models.Telemetry.timestamp.desc()).offset(skip).limit(limit).all()

def get_telemetry_by_device_id(db: Session, device_id: str) -> List[models.Telemetry]:
    """
    Retrieves all telemetry records for a specific device.
    
    Args:
        db: The database session.
        device_id: The ID of the device to query.
        
    Returns:
        A list of telemetry database objects for the given device.
    """
    return db.query(models.Telemetry).filter(models.Telemetry.device_id == device_id).order_by(models.Telemetry.timestamp.desc()).all()
