from sqlmodel import SQLModel, create_engine, Session
from skyblog.models import Post

db_file = "database.db"
db_url = f"sqlite:///{db_file}"

engine = create_engine(db_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session