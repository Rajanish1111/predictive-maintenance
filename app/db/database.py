from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.utils.config import settings
from app.utils.logger import log

try:
    # Create the SQLAlchemy engine using the URL from settings
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    # Create a configured "Session" class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # Create a base class for declarative models
    Base = declarative_base()
    log.info("Database engine created successfully.")
except Exception as e:
    log.error(f"Failed to create database engine: {e}")
    raise

def get_db():
    """
    FastAPI dependency to get a database session.
    This will create a new session for each request and close it when done.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
