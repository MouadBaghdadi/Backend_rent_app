from sqlalchemy.orm import Session
from backend import schemas
from fastapi import Depends, HTTPException, status
from backend.database import get_db
from backend.models import models

def get_all(db: Session = Depends(get_db)):
    annonces = db.query(models.Annonce).all()
    for i in range(len(annonces)):
        images = db.query(models.Images).filter(models.Images.annid == annonces[i].id).first()
        annonces[i].image = [f'{images}']
    return annonces

def create(ann: schemas.AnnonceBase, db: Session = Depends(get_db)):
    new_annonce = models.Annonce(
        title = ann.title,
        nom_prenom = ann.nom_prenom,
        user_adresse = ann.user_adresse,
        user_email = ann.user_email,
        user_phone = ann.user_phone,
        type = ann.type,
        publish_date = ann.publish_date,
        commune = ann.commune,
        wilaya = ann.wilaya,
        # image = ann.image,
        sqft = ann.sqft,
        nb_bath = ann.nb_bath,
        nb_bed = ann.nb_bed,
        descr = ann.descr,
        prix = ann.prix,
        uid = ann.uid,
    )
    db.add(new_annonce)
    db.commit()
    for i in ann.image:
        new_image = models.Images(
            annid = new_annonce.id,
            image = i,
            # ownerr = new_annonce,
        )
        db.add(new_image)
        db.commit()
    db.refresh(new_annonce)
    return new_annonce

def delete(id: int, db: Session = Depends(get_db)):
    ann = db.query(models.Annonce).filter(models.Annonce.id == id)  
    if not ann.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"annonce with id = {id} not found")
    ann.delete(synchronize_session=False)
    db.commit()
    return 'deleted succefully'

def get_by_userid(uid:str, db: Session = Depends(get_db)):
    annonces = db.query(models.Annonce).filter(models.Annonce.uid == uid).all()
    for i in range(len(annonces)):
        images = db.query(models.Images).filter(models.Images.annid == annonces[i].id).first()
        annonces[i].image = [f'{images}']
    if annonces == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ther is no annonces")
    return annonces