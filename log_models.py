from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime,
    Float,
    Index
)

Base = declarative_base()

class ApplicationLog(Base):

    __tablename__ = "application_logs"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    log_id = Column(
        String(120),
        unique=True,
        nullable=False
    )

    service_name = Column(
        String(120),
        nullable=False
    )

    log_level = Column(
        String(50),
        nullable=False
    )

    endpoint = Column(
        String(255)
    )

    response_time = Column(
        Float
    )

    status_code = Column(
        String(20)
    )

    message = Column(
        String(5000)
    )

    ip_address = Column(
        String(120)
    )

    environment = Column(
        String(100)
    )

    created_at = Column(
        DateTime,
        nullable=False
    )

    __table_args__ = (
        Index("idx_log_id", "log_id"),
        Index("idx_service_name", "service_name"),
        Index("idx_log_level", "log_level"),
        Index("idx_created_at", "created_at"),
    )


class FailedLogRecord(Base):

    __tablename__ = "failed_log_records"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    log_id = Column(
        String(120)
    )

    failure_reason = Column(
        String(255)
    )

    payload = Column(
        String(10000)
    )

    created_at = Column(
        DateTime,
        nullable=False
    )
