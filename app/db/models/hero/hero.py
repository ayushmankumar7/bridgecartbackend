from pydantic import BaseModel
from typing import Optional,Union
from random import random
from core.firebase import db

class Banner(BaseModel):
    image : str
    title : str
    subtitle : Optional[str]

    @classmethod 
    def create(cls,username,**kwargs):
        obj = cls(**kwargs)
        db.collection("Hero").document(username).collection("Banner").add(obj.dict())
    
    @classmethod
    def delete(cls,username,id):
        db.collection("Hero").document(username).collection("Banner").document(id).delete()
    
    @classmethod 
    def update(cls,username,id,data):
        db.collection("Hero").document(username).collection("Banner").document(id).update(data)
    
    @classmethod 
    def get_by_username(cls,username):
        colSnap = db.collection("Hero").document(username).collection("Banner").stream() 
        objList = [] 

        for doc in colSnap:
            objList.append(cls(**doc))
        return objList
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("Banner").document(id).get() 
        return cls(**docSnap)



class CTA(BaseModel):
    image : str
    title : str
    subtitle : Optional[str]
    buttonText : str
    buttonLink : str

    @classmethod 
    def create(cls,username,**kwargs):
        obj = cls(**kwargs)
        db.collection("Hero").document(username).collection("CTA").add(obj.dict())
    
    @classmethod
    def delete(cls,username,id):
        db.collection("Hero").document(username).collection("CTA").document(id).delete()
    
    @classmethod 
    def update(cls,username,id,data):
        db.collection("Hero").document(username).collection("CTA").document(id).update(data)
    
    @classmethod 
    def get_by_username(cls,username):
        colSnap = db.collection("Hero").document(username).collection("CTA").stream() 
        objList = [] 

        for doc in colSnap:
            objList.append(cls(**doc))
        return objList
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("CTA").document(id).get() 
        return cls(**docSnap)


class Social(BaseModel):
    facebook = Optional[str]
    instagram = Optional[str]
    website = Optional[str]
    linkedIn = Optional[str]
    telegram = Optional[str]
    facebook = Optional[str]

    @classmethod 
    def create(cls,username,**kwargs):
        obj = cls(**kwargs)
        db.collection("Hero").document(username).collection("Social").add(obj.dict())
    
    @classmethod
    def delete(cls,username,id):
        db.collection("Hero").document(username).collection("Social").document(id).delete()
    
    @classmethod 
    def update(cls,username,id,data):
        db.collection("Hero").document(username).collection("Social").document(id).update(data)
    
    @classmethod 
    def get_by_username(cls,username):
        colSnap = db.collection("Hero").document(username).collection("Social").stream() 
        objList = [] 

        for doc in colSnap:
            objList.append(cls(**doc))
        return objList
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("Social").document(id).get() 
        return cls(**docSnap)


class Faq(BaseModel):
    question: str
    answer: str

    @classmethod 
    def create(cls,username,**kwargs):
        obj = cls(**kwargs)
        db.collection("Hero").document(username).collection("FAQ").add(obj.dict())
    
    @classmethod
    def delete(cls,username,id):
        db.collection("Hero").document(username).collection("FAQ").document(id).delete()
    
    @classmethod 
    def update(cls,username,id,data):
        db.collection("Hero").document(username).collection("FAQ").document(id).update(data)
    
    @classmethod 
    def get_by_username(cls,username):
        colSnap = db.collection("Hero").document(username).collection("FAQ").stream() 
        objList = [] 

        for doc in colSnap:
            objList.append(cls(**doc))
        return objList
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("FAQ").document(id).get() 
        return cls(**docSnap)
