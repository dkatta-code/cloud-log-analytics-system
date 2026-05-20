import redis

from config import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True
)

CACHE_EXPIRATION = 43200

def is_duplicate_log(log_id):

    existing_record = redis_client.get(
        log_id
    )

    if existing_record:
        return True

    redis_client.set(
        log_id,
        "processed",
        ex=CACHE_EXPIRATION
    )

    return False
