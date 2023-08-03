from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from backend.models import models
from backend.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from .. import schemas, database, token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["authentification"]
)

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated= "auto",)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"incorrect password")
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}