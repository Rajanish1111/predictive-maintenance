from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TelemetryBase(BaseModel):
    """Base schema for telemetry data with all common fields."""
    device_id: str
    temperature: float
    humidity: float
    latitude: float
    longitude: float
    status: str

class TelemetryCreate(TelemetryBase):
    """Schema used for creating a new telemetry record via the API."""
    pass

class Telemetry(TelemetryBase):
    """Schema for returning a telemetry record from the API."""
    id: int
    timestamp: datetime

    class Config:
        """Pydantic configuration to enable ORM mode."""
        from_attributes = True
