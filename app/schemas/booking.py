# app/schemas/booking.py

from pydantic import BaseModel
from datetime import date

class BookingCreate(BaseModel):
    hotel_id: int
    guest_name: str
    check_in: date
    check_out: date

class BookingOut(BookingCreate):
    id: int

    class Config:
        from_attributes = True
