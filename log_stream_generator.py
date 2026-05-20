from confluent_kafka import Producer

from faker import Faker
from datetime import datetime

from config import config

import random
import json
import uuid
import time

fake = Faker()

producer = Producer({
    "bootstrap.servers": config.KAFKA_BOOTSTRAP_SERVERS
})

LOG_LEVELS = [
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL"
]

SERVICES = [
    "payment-service",
    "inventory-service",
    "user-service",
    "analytics-service",
    "gateway-service"
]

ENDPOINTS = [
    "/api/orders",
    "/api/payments",
    "/api/users",
    "/api/products",
    "/api/analytics"
]

ENVIRONMENTS = [
    "development",
    "staging",
    "production"
]

def generate_log_record():

    return {
        "log_id": str(uuid.uuid4()),
        "service_name": random.choice(SERVICES),
        "log_level": random.choice(LOG_LEVELS),
        "endpoint": random.choice(ENDPOINTS),
        "response_time": round(
            random.uniform(10, 3000),
            2
        ),
        "status_code": random.choice([
            "200",
            "201",
            "400",
            "401",
            "404",
            "500"
        ]),
        "message": fake.text(
            max_nb_chars=300
        ),
        "ip_address": fake.ipv4(),
        "environment": random.choice(
            ENVIRONMENTS
        ),
        "created_at": datetime.utcnow().isoformat()
    }

def stream_logs(batch_size=8000):

    for _ in range(batch_size):

        record = generate_log_record()

        producer.produce(
            "application_logs",
            json.dumps(record).encode(
                "utf-8"
            )
        )

    producer.flush()

if __name__ == "__main__":

    while True:
        stream_logs()
        time.sleep(1)
