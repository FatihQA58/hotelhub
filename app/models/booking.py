# app/models/booking.py

from sqlalchemy import Column, Integer, Date, ForeignKey
from app.database.connection import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    user_id = Column(Integer)  
    check_in = Column(Date)
    check_out = Column(Date)
