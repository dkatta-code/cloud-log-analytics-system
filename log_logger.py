from loguru import logger

import sys

logger.remove()

logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO"
)

logger.add(
    "cloud_log_analytics.log",
    rotation="100 MB",
    retention="14 days",
    compression="zip",
    enqueue=True,
    level="DEBUG"
)

logger.add(
    "cloud_log_errors.log",
    rotation="50 MB",
    retention="30 days",
    level="ERROR"
)
