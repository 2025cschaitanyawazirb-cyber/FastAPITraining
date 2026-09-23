from fastapi import FastAPI
from app.config import settings
from app.database import ping_database

app = FastAPI(title=settings.APP_Name)

@app.on_event("startup")
async def startup_event() -> None:
    if not ping_database():
        raise RuntimeError("could not connect to mongodb database")
    print(f"Connected to MongoDB database: {settings.APP_Name}")

@app.get("/")
def health_check() -> dict:
    return {"status":"ok", "API":settings.APP_Name}

