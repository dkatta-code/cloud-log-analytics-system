from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config

DATABASE_URL = (
    f"mysql+pymysql://{config.MYSQL_USER}:"
    f"{config.MYSQL_PASSWORD}@"
    f"{config.MYSQL_HOST}:"
    f"{config.MYSQL_PORT}/"
    f"{config.MYSQL_DATABASE}"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=25,
    max_overflow=50,
    pool_recycle=3600,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
