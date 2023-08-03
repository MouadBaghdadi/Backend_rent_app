from typing import Optional
from pydantic import BaseModel

# class Image(BaseModel):
#     images : str
#     class Config():
#         orm_mode = True

class AnnonceBase(BaseModel):
    uid: str
    nom_prenom : str
    user_adresse : str
    user_email: str
    user_phone: str
    publish_date: str
    commune : str
    wilaya: str
    image: list[str]
    type: str
    sqft: int
    nb_bath: int
    nb_bed: int
    title: str
    descr: str
    prix: int

class Annonce(AnnonceBase):
    class Config():
        orm_mode = True    

class showuser(BaseModel):
    name:str
    uid: str
    email:str
    annonces: list[Annonce] = []
    class Config():
        orm_mode = True

class showuserwithoutann(BaseModel):
    name:str
    uid:str
    email:str
    class Config():
        orm_mode = True

class showAnnonce(BaseModel):
    nom_prenom : str
    user_adresse : str
    user_email: str
    user_phone: str
    publish_date: str
    commune : str
    wilaya: str
    image: list[str] = []
    type: str
    sqft: int
    nb_bath: int
    nb_bed: int
    descr: str
    prix: int
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    # password: str
    avatar: str

class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
