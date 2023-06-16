from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_HOST = "db"
POSTGRES_USER = "user"
POSTGRES_PASSWORD = "password"
POSTGRES_DB = "db"
PORT = 5432

# Create the SQLAlchemy engine and session
engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{PORT}/{POSTGRES_DB}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
