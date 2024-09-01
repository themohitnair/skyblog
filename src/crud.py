from sqlmodel import Session, select
from src.models import Post
from src.database import get_session
from datetime import datetime

def add_post(title: str, content: str, thumbnail: str):
    with get_session() as session:
        statement = select(Post).where(Post.title == title)
        existing_post = session.exec(statement).first()        
        if existing_post:
            return "Post with the same title already exists."        
        new_post = Post(
            title=title,
            content=content,
            thumbnail=thumbnail
        )        
        session.add(new_post)
        session.commit()
        session.refresh(new_post)        
        return new_post 

def get_posts_by_date_range(start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
    with get_session() as session:
        query = select(Post)        
        if start_date:
            query = query.where(Post.created_at >= start_date)        
        if end_date:
            query = query.where(Post.created_at <= end_date)        
        posts = session.exec(query).all()
        return posts

def delete_post(title: str):
    with get_session() as session:
        query = select(Post).where(Post.title == title)
        post = session.exec(query).first()
        if post:
            session.delete(post)
            session.commit()
            return f"Post titled '{title}' was deleted successfully"
        return f"Post titled '{title}' does not exist"