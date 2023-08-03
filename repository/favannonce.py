from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.models import models
from backend.database import get_db


def add_fav(id, db: Session = Depends(get_db)):
    ann = db.query(models.Annonce).filter(models.Annonce.id == id).first()
    new_annonce = models.AnnonceFavoris(
        uid = "current user",
        nom_prenom = ann.nom_prenom,
        user_adresse = ann.user_adresse,
        user_email = ann.user_email,
        user_phone = ann.user_phone,
        type = ann.type,
        publish_date = ann.publish_date,
        commune = ann.commune,
        wilaya = ann.wilaya,
        image = ann.image,
        sqft = ann.sqft,
        nb_bath = ann.nb_bath,
        nb_bed = ann.nb_bed,
        descr = ann.descr,
        prix = ann.prix,
    )
    db.add(new_annonce)
    db.commit()
    db.refresh(new_annonce)
    return new_annonce

def get_fav(db: Session = Depends(get_db)):
    AnnoncesFav = db.query(models.AnnonceFavoris).all()
    return AnnoncesFav

def delete_fav(id, db: Session = Depends(get_db)):
    ann = db.query(models.AnnonceFavoris).filter(models.AnnonceFavoris.id == id)
    if not ann.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"annonce with id = {id} not found")
    ann.delete(synchronize_session=False)
    db.commit()
    return 'deleted succefully'