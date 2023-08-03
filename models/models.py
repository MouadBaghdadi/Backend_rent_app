from ..database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, Boolean
from sqlalchemy.orm import relationship

class Annonce(Base):
    __tablename__ = 'annonces'

    id = Column(Integer, primary_key = True, index= True)
    nom_prenom = Column(String)
    user_adresse = Column(String)
    user_email = Column(String)
    user_phone = Column(String)
    type = Column(String)
    publish_date = Column(String)
    commune = Column(String)
    wilaya = Column(String)
    # image = Column(String)
    sqft = Column(Integer)
    nb_bed = Column(Integer)
    nb_bath = Column(Integer)
    descr = Column(String)
    prix = Column(Integer)
    title = Column(String)
    uid = Column(Integer, ForeignKey('users.uid'))

    owner = relationship("User", back_populates= "annonces")
    images = relationship("Images", back_populates= "annonce")

# class AnnonceFavoris(Base):
#     __tablename__ = 'fav'
    
#     id = Column(Integer, primary_key = True, index= True)
#     uid = Column(String)
#     nom_prenom = Column(String)
#     user_adresse = Column(String)
#     user_email = Column(String)
#     user_phone = Column(String)
#     type = Column(String)
#     publish_date = Column(String)
#     commune = Column(String)
#     wilaya = Column(String)
#     image = Column(String)
#     sqft = Column(Integer)
#     nb_bed = Column(Integer)
#     nb_bath = Column(Integer)
#     descr = Column(String)
#     prix = Column(Integer)
#     title = Column(String)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index= True)
    uid = Column(String)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    verified = Column(Boolean , default = False)
    onborded = Column(Boolean , default = False)
    provider = Column(Boolean , default = False)
    avatar = Column(String)

    annonces = relationship("Annonce", back_populates= "owner")

class Images(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key = True, index= True)
    annid = Column(Integer, ForeignKey('annonces.id'))
    image = Column(String)

    annonce = relationship("Annonce", back_populates= "images")

    