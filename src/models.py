from sqlmodel import SQLModel, Field, TIMESTAMP, Column, LargeBinary
from datetime import datetime
from typing import Optional
from sqlalchemy import func

class Post(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    title: str = Field(unique=True, min_length=1, max_length=64, nullable=False, index=True)
    content: str = Field(nullable=False, min_length=1, index=True)
    thumbnail: str = Field(max_length=255, nullable=False)
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, nullable=False), default=func.now(), index=True)