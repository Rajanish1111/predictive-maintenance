import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """
    Initializes and returns a standardized logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Prevent duplicate logs in Uvicorn

    # If handlers are already configured, don't add them again
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# A global logger instance for easy import
log = get_logger(__name__)
