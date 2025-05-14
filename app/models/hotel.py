# app/models/hotel.py

from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    description = Column(String)
    total_rooms = Column(Integer, nullable=False)