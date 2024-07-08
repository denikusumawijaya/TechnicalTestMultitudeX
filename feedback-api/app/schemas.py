from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    score: int
