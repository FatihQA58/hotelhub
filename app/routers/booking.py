# app/routers/booking.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.booking import Booking
from app.models.hotel import Hotel
from app.schemas import BookingCreate, BookingOut
from typing import List

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BookingOut)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.id == booking.hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")

    # Dates:
    overlapping_bookings = db.query(Booking).filter(
        Booking.hotel_id == booking.hotel_id,
        Booking.check_out > booking.check_in,
        Booking.check_in < booking.check_out
    ).count()

    if overlapping_bookings >= hotel.total_rooms:
        raise HTTPException(status_code=400, detail="No rooms available for selected dates")

    db_booking = Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

