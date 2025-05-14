from sqlalchemy.orm import Session
from app.models.hotel import Hotel
from app.database.connection import engine, Base, SessionLocal

def seed_hotels():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    hotels = [
        Hotel(name="Grand Tower Hotel", city="Amsterdam", total_rooms=30, description="Luxury stay near canal"),
        Hotel(name="Sea Breeze Inn", city="Rotterdam", total_rooms=20, description="Cozy hotel by the harbor"),
        Hotel(name="Desert Rose Lodge", city="Utrecht", total_rooms=15, description="Peaceful nature retreat"),
        Hotel(name="Skyview Apartments", city="The Hague", total_rooms=25, description="City view and modern room"),
        Hotel(name="Forest Hill Resort", city="Groningen", total_rooms=10, description="Nature and relaxation"),
    ]

    db.add_all(hotels)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_hotels()
