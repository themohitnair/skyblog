from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from pydantic_settings import BaseSettings
from routers.admin import admin_router
from routers.home import home_router

# Load environment variables
class Settings(BaseSettings):
    api_key: str

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI()

# Define API Key Header
api_key_header = APIKeyHeader(name="X-API-KEY")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key"
        )
    return api_key

@app.on_event("startup")
def startup():
    # Initialize database or other startup tasks
    pass

# Apply API Key Authentication to Admin Routes
app.include_router(admin_router, prefix="/admin", tags=["admin"], dependencies=[Depends(verify_api_key)])
app.include_router(home_router, prefix="/home", tags=["home"])
