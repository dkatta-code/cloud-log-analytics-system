from database import engine
from log_models import Base

def initialize_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initialize_tables()
