from pydantic import BaseModel
from typing import Optional
from datetime import date
import uuid

class PostBase(BaseModel):
    title: str
    content: str

class PostRead(PostBase):
    id: uuid.UUID
    created_at: date

    class Config:
        orm_mode = True