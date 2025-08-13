from sqlalchemy import Column, Integer, String, DateTime, func, DECIMAL
from .database import Base

class Telemetry(Base):
    """
    SQLAlchemy ORM model for telemetry data.
    """
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String(255), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False, server_default=func.now())
    temperature = Column(DECIMAL(5, 2))
    humidity = Column(DECIMAL(5, 2))
    latitude = Column(DECIMAL(9, 6))
    longitude = Column(DECIMAL(9, 6))
    status = Column(String(50))
