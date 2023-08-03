import token
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from backend import schemas, token
from backend.database import get_db
from backend.models import models
from ..repository import user

router = APIRouter(
    prefix= '/user',
    tags= ['User']
)


@router.post('/signup')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    access_token = token.create_access_token(data={"sub": request.email})
    user.create_user(request, db)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/{id}', response_model= schemas.showuser)
def get_user(id:int , db: Session = Depends(get_db)):
    return user.get_user(id, db)