from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "blog.db"
# SQLITE_DB_URL = f"sqlite:///{DB_PATH}"
SQLITE_DB_URL = "sqlite:///./blog.db"

engine = create_engine(SQLITE_DB_URL, connect_args={
                       "check_same_thread": False}, )

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create all defined tables


def create_db_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
