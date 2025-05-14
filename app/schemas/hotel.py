# app/schemas/hotel.py

from pydantic import BaseModel
from typing import Optional

# Enter Data
class HotelCreate(BaseModel):
    name: str
    city: str
    description: Optional[str] = None
    total_rooms: int

# Data From Database
class HotelOut(HotelCreate):
    id: int

    class Config:
        from_attributes = True
