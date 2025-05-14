# app/routers/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.user import User
from app.schemas import UserCreate, UserOut, UserLogin
from app.auth.auth_handler import get_password_hash, verify_password, create_access_token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post("/register", response_model=UserOut)
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     if db.query(User).filter(User.username == user.username).first():
#         raise HTTPException(status_code=400, detail="Username already registered")
    
#     hashed_pw = get_password_hash(user.password)
#     db_user = User(
#         username=user.username,
#         email=user.email,
#         hashed_password=hashed_pw
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @router.post("/login")
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user or not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token(data={"sub": db_user.username})
#     return {"access_token": token, "token_type": "bearer"}
