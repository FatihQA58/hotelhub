from typing import Optional, List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from app.models.hotel import Hotel
from app.schemas import HotelOut
from app.database.connection import get_db

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)

@router.get("/", response_model=List[HotelOut])
def get_hotels(
    city: Optional[str] = Query(None),
    check_in: Optional[date] = Query(
        None, description="YYYY-MM-DD"
    ),
    check_out: Optional[date] = Query(
        None, description="YYYY-MM-DD"
    ),
    min_rooms: Optional[int] = Query(1),
    db: Session = Depends(get_db)
):
    query = db.query(Hotel)

    if city:
        query = query.filter(Hotel.city.ilike(f"%{city}%"))  # Upper or Lower

    if min_rooms:
        query = query.filter(Hotel.total_rooms >= min_rooms)

    # Date Auth
    if check_in and check_out:
        from app.models.booking import Booking

        overlapping = db.query(Booking.hotel_id).filter(
            Booking.check_out > check_in,
            Booking.check_in < check_out
        ).subquery()

        query = query.filter(~Hotel.id.in_(overlapping))

    return query.all()
