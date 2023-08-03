from fastapi import APIRouter, Depends, status, HTTPException
from ..models import models
from backend.database import get_db
from backend.oauth2 import get_current_user
from .. import schemas
from typing import List
from sqlalchemy.orm import Session
from ..repository import annonce


router = APIRouter(
    prefix= '/Annonce',
    tags = ['Annonces']
)

@router.get('/get',response_model=List[schemas.showAnnonce])
def get_annonce(db: Session = Depends(get_db)):
    return annonce.get_all(db)

@router.post('/add/ann', status_code=status.HTTP_201_CREATED)
def add_annonce(ann: schemas.AnnonceBase, db: Session = Depends(get_db)):
    return annonce.create(ann, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    return annonce.delete(id, db)

@router.get('/{uid}',response_model=List[schemas.Annonce])
def get_selfannonces(uid:str, db: Session = Depends(get_db)):
    return annonce.get_by_userid(uid, db)