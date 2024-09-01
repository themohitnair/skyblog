from sqlmodel import SQLModel, create_engine, Session
from src.models import Post

db_file = "database.db"
db_url = f"sqlite:///{db_file}"

engine = create_engine(db_url, echo=True)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    with Session(engine) as session:
        yield session