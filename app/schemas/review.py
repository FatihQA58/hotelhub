# app/schemas/review.py

from pydantic import BaseModel, Field
from typing import Optional

class ReviewCreate(BaseModel):
    hotel_id: int
    rating: int = Field(gt=0, lt=6)  # تقييم بين 1 و5
    comment: Optional[str] = None

class ReviewOut(ReviewCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True
