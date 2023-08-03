import requests
from sqlalchemy.orm import Session
from ..models import models
from ..database import Base, engine, get_db
from bs4 import BeautifulSoup
from fastapi import Depends, APIRouter

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix= '/scraping',
    tags= ['scraping']
)

@router.get('/')
def scrap(db: Session = Depends(get_db)):
    url = "http://www.annonce-algerie.com/upload/flux/rss_1.xml"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    
    ads = soup.find_all("item")
    
    for ad in ads:
        desc : str
        desc = ad.description.text
        desc = desc.split('<br/>')[0]
        new_annonce = models.Annonce(
            title = ad.title.text,
            descr = desc,
            publish_date = ad.pubDate.text,
            nom_prenom = '',
            user_adresse = '',
            user_email = '',
            user_phone = '',
            type = '',
            commune = '',
            wilaya = '',
            sqft = 0,
            nb_bed = 0,
            nb_bath = 0,
            prix = 0,
        )
        annonces = db.query(models.Annonce).all()
        already = False
        for i in range(len(annonces)):
            if new_annonce.descr == annonces[i].descr :
                already = True
        if not already:
            db.add(new_annonce)
            db.commit()
            db.refresh(new_annonce)
        annonces = db.query(models.Annonce).all()
    return annonces