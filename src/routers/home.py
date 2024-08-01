from crud import get_post, get_posts
from sqlmodel import Session
from typing import Optional
from database import get_session
from models import Post, DateRange
from fastapi import APIRouter, HTTPException, Depends, Body
import uuid
from datetime import date

home_router = APIRouter()

@home_router.get("/posts/")
async def all_posts(start_date: Optional[date] = date.today(), end_date: Optional[date] = date.today(), session: Session = Depends(get_session)):
    try:
        date_range = DateRange(start_date=start_date, end_date=end_date) if start_date and end_date else None
        posts = get_posts(date_range, session)
        return posts
    except HTTPException as e:
        raise e

@home_router.get("/post/")
async def view_post(post_id: uuid.UUID, session: Session = Depends(get_session)):
    try:
        post = get_post(post_id, session)
        return post
    except HTTPException as e:
        raise e