from fastapi import FastAPI, Depends, APIRouter

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Greetings from skyblog!"}
