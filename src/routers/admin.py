from crud import add_post, delete_post, update_post
from sqlmodel import Session
from database import get_session
from models import Post
from schemas import PostBase
from fastapi import APIRouter, HTTPException, Depends, Body
import uuid

admin_router = APIRouter()

@admin_router.post("/post/")
async def create_post(post: PostBase = Body(...), session: Session = Depends(get_session)):
    try:
        new_post = Post(
            title=post.title,
            content=post.content
        )
        created_post = add_post(new_post, session)
        return {"message": f"New post with ID: {created_post.id} created successfully"}
    except HTTPException as e:
        raise e

@admin_router.delete("/post/{post_id}")
async def delete_post(post_id: uuid.UUID, session: Session = Depends(get_session)):
    try: 
        post = delete_post(post_id, session)
        return {"message": f"New post with ID: {post.id} deleted successfully"}
    except HTTPException as e:
        raise e

@admin_router.patch("/post/{post_id}")
async def modify_post(post_id: uuid.UUID, post: PostBase = Body(...), session: Session = Depends(get_session)):
    try:
        updated_post = update_post(post_id, post.title, post.content, session)
        return {"message": f"Post with ID: {updated_post.id} updated successfully"}
    except HTTPException as e:
        raise e