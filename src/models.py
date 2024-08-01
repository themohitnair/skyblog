from typing import Optional
import uuid
from sqlmodel import SQLModel, Field
from datetime import datetime
from dataclasses import dataclass
from datetime import date

@dataclass
class DateRange:
    start_date: date
    end_date: date

class Post(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(nullable=False, unique=True, index=True)
    content: str = Field(nullable=False)
    created_at: date = Field(default_factory=date.today)