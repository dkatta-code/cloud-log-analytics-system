from datetime import datetime

REQUIRED_FIELDS = [
    "log_id",
    "service_name",
    "log_level",
    "endpoint",
    "response_time",
    "status_code",
    "message",
    "ip_address",
    "environment",
    "created_at"
]

VALID_LOG_LEVELS = [
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL"
]

def validate_log_record(record):

    for field in REQUIRED_FIELDS:

        if field not in record:
            return False

        if record[field] is None:
            return False

    if record["log_level"] not in VALID_LOG_LEVELS:
        return False

    if not isinstance(
        record["response_time"],
        (int, float)
    ):
        return False

    if record["response_time"] < 0:
        return False

    try:
        datetime.fromisoformat(
            record["created_at"]
        )
    except Exception:
        return False

    return True
