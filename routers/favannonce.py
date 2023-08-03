from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from backend import schemas
from backend.database import get_db
from backend.models import models
from backend.oauth2 import get_current_user
from ..repository import favannonce

router = APIRouter(
    prefix='/Favoris',
    tags= ['Favoris']
)

@router.post('/{id}', status_code=status.HTTP_201_CREATED)
def add_favoris(id, db: Session = Depends(get_db)):
    return favannonce.add_fav(id, db)

@router.get('/')
def get_favoris(db: Session = Depends(get_db)):
    return favannonce.get_fav(db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_Fav(id, db: Session = Depends(get_db)):
    return favannonce.delete_fav(id, db)