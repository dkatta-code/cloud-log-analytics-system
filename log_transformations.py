import pandas as pd
import numpy as np

def normalize_log_dataframe(records):

    dataframe = pd.DataFrame(records)

    dataframe["response_category"] = pd.cut(
        dataframe["response_time"],
        bins=[0, 200, 800, 1500, 5000],
        labels=[
            "FAST",
            "MODERATE",
            "SLOW",
            "CRITICAL"
        ]
    )

    dataframe["is_server_error"] = np.where(
        dataframe["status_code"].astype(str).str.startswith("5"),
        1,
        0
    )

    dataframe["is_client_error"] = np.where(
        dataframe["status_code"].astype(str).str.startswith("4"),
        1,
        0
    )

    dataframe["event_date"] = pd.to_datetime(
        dataframe["created_at"]
    ).dt.date

    dataframe["event_hour"] = pd.to_datetime(
        dataframe["created_at"]
    ).dt.hour

    dataframe["normalized_service_name"] = (
        dataframe["service_name"]
        .str.lower()
        .str.replace("-", "_")
    )

    dataframe["severity_score"] = np.select(
        [
            dataframe["log_level"] == "INFO",
            dataframe["log_level"] == "WARNING",
            dataframe["log_level"] == "ERROR",
            dataframe["log_level"] == "CRITICAL"
        ],
        [
            1,
            2,
            3,
            4
        ]
    )

    return dataframe
