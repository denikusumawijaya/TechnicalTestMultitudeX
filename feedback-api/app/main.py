from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import SessionLocal, engine, Base
from app.schemas import FeedbackCreate
from app.crud import create_feedback

app = FastAPI()

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/feedback/")
async def create_feedback_endpoint(feedback: FeedbackCreate, db: AsyncSession = Depends(get_db)):
    return await create_feedback(db, feedback)
