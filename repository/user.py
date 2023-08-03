from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from backend import schemas
from passlib.context import CryptContext
from backend.database import get_db
from backend.models import models



pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated= "auto",)


def create_user(request: schemas.User, db: Session = Depends(get_db)):
    emails = db.query(models.User.email).all()
    for i in range(len(emails)):
        if request.email in emails[i]:
            raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
                            detail=f"Email already used")
    # hashedPassword = pwd_cxt.hash(request.password)  
    new_user = models.User(
            uid = f"#{request.name}",
            email = request.email,
            name = request.name,
            # password = hashedPassword,
            # verified = True,
            onborded = True,
            provider = True,
            avatar = request.avatar,
            )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id = {id} not found")
    return user