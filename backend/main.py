from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models import User
from database import get_db

@app.get("/search")
def search_user(email: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == email).first()
    except Exception as e:
        print("DB ERROR:", e)
        raise HTTPException(status_code=500, detail="Database error")

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "full_name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "organization": user.organization
    }


@app.post("/update")
def update(email: str, phone: str, organization: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Record not found")

    user.phone = phone
    user.organization = organization
    db.commit()
    return {"message": "Updated successfully"}
