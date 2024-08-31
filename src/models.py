from sqlmodel import SQLModel, Field, TIMESTAMP, Column, LargeBinary
from datetime import datetime
from typing import Optional
from sqlalchemy import func

class Post(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    title: str = Field(unique=True, min_length=1, max_length=128, nullable=False)
    content: str = Field(nullable=False, min_length=1)
    thumbnail: bytes = Field(max_length=255, nullable=False)
    created_at: datetime = Field(sa_column=Column(TIMESTAMP), default=func.now(), nullable=False)