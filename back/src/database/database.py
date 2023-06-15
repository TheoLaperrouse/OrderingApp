from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_HOST = "db"
POSTGRES_PORT = 5432
POSTGRES_USER = "myuser"
POSTGRES_PASSWORD = "mypassword"
POSTGRES_DB = "mydatabase"

# Create the SQLAlchemy engine and session
engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()