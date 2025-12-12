from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os

# Get database URL from environment variable
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/appdb"
)

# Create engine
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    pass


def get_session() -> Generator[Session, None, None]:
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session
