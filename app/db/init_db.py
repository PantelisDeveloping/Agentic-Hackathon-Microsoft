from sqlalchemy.orm import Session
from app.core.config import settings
from app.models.base import Base
from app.db.session import engine

def init_db() -> None:
    # Create all tables
    Base.metadata.create_all(bind=engine)

def init_db_test() -> None:
    # Create all tables for testing
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Creating initial data")
    init_db()
    print("Initial data created") 