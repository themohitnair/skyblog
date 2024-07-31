from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True)
session = Session(engine)

def init_db():
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Database and Tables created.")
    except Exception as e:
        logger.error(f"Error creating database and tables: {e}")

def get_session():
    return session