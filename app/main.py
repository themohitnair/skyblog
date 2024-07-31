from fastapi import FastAPI
from database import engine, init_db, get_session
from sqlmodel import Session
from models import Post
from crud import add_post, delete_post, get_post
from routers.admin import admin_router
from routers.home import home_router

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(home_router, prefix="/home", tags=["admin"])