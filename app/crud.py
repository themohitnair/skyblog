from sqlmodel import SQLModel, Session, select
import uuid
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from typing import Optional
from datetime import date
from database import get_session
from models import Post, DateRange
from fastapi import Depends, HTTPException

def add_post(post: Post, session: Session):
    try:
        if post:
            session.add(post)
            session.commit()
            session.refresh(post)
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
    except OperationalError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Operational error: {str(e)}")
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def delete_post(post_id: uuid.UUID, session: Session):
    try: 
        statement = select(Post).where(Post.id == post_id)
        post = session.exec(statement).one()
        if post:
            session.delete(post)
            session.commit()
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
    except OperationalError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Operational error: {str(e)}")
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def update_post(post_id: uuid.UUID, new_title: Optional[str], new_content: Optional[str], session: Session):
    try:
        statement = select(Post).where(Post.id == post_id)
        post = session.exec(statement).one_or_none()
        if post:
            if new_title:
                post.title = new_title
            if new_content:
                post.content = new_content
            post.created_at = date.today()
            session.add(post)
            session.commit()
            session.refresh(post)
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
    except OperationalError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Operational error: {str(e)}")
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def get_post(post_id: uuid.UUID, session: Session):
    try:
        statement = select(Post).where(Post.id == post_id)
        post = session.exec(statement).one_or_none()
        if post:
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
    except OperationalError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Operational error: {str(e)}")
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def get_posts(date_range: Optional[DateRange], session: Session):
    try:
        if date_range:
            start = date_range.start_date
            end = date_range.end_date
            statement = select(Post).filter(Post.created_at >= start, Post.created_at <= end)
            posts = session.exec(statement).all()
            if posts:
                return posts
            else:
                raise HTTPException(status_code=404, detail="No posts yet")  
        else:
            statement = select(Post)
            posts = session.exec(statement).all()
            if posts:
                return posts
            else:
                raise HTTPException(status_code=404, detail="No posts yet")  
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
    except OperationalError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Operational error: {str(e)}")
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))