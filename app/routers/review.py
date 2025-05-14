# app/routers/review.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.review import Review
from app.models.hotel import Hotel
from app.models.user import User
from app.schemas import ReviewCreate, ReviewOut
from app.auth.auth_handler import decode_token
from fastapi.security import OAuth2PasswordBearer
from typing import List

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# استخراج المستخدم من التوكن
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_token(token)
    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=ReviewOut)
def leave_review(review: ReviewCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    hotel = db.query(Hotel).filter(Hotel.id == review.hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")

    new_review = Review(**review.dict(), user_id=current_user.id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

@router.get("/", response_model=List[ReviewOut])
def get_all_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()
