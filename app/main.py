# app/main.py

from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models import hotel, booking, user, review

app = FastAPI()

from app.routers import hotel as hotel_router, booking as booking_router
app.include_router(hotel_router.router)
app.include_router(booking_router.router)

# from app.routers import user as user_router
# app.include_router(user_router.router)

# from app.routers import review as review_router
# app.include_router(review_router.router)


# Import All Models to Create Tables:

# Create Tables:
Base.metadata.create_all(bind=engine)

# Router:
app.include_router(hotel_router.router)

@app.get("/")
def root():
    return {"message": "🚀 FastAPI Hotel Project gestart!"}