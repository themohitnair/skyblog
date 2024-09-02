from pydantic import BaseModel, constr, field_validator
from datetime import datetime
from typing import Optional

class PostCreate(BaseModel):
    title: str = constr(strip_whitespace=True, min_length=5, max_length=64)
    content: str
    thumbnail: str

    @field_validator('thumbnail')
    def validate_thumbnail(cls, v):
        if not v.endswith(('.jpg', '.jpeg', '.png')):
            raise ValueError('Thumbnail must be a valid image file (.jpg, .jpeg, .png)')
        return v

class DateRange(BaseModel):
    start_date: Optional[datetime]
    end_date: Optional[datetime]

    @field_validator('start_date', 'end_date', mode='before')
    def check_not_future(cls, v):
        if v and v > datetime.now():
            raise ValueError('Date cannot be in the future.')
        return v

    @model_validator(mode='before')
    def check_date_order(cls, values):
        start_date = values.get('start_date')
        end_date = values.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise ValueError('start_date must be before or equal to end_date.')
        return values