from pydantic import BaseModel
from typing import Optional,Union
from random import random
from core.firebase import db

class Banner(BaseModel):
    id : Optional[str]
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
        try:
            for doc in colSnap:
                 data = doc.to_dict()
                 data["id"]=doc.id 
                 objList.append(cls(**data))
            return objList
        except Exception as e:
            print(e)
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("Banner").document(id).get() 
        return cls(**docSnap)



class CTA(BaseModel):
    id : Optional[str]
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
        try:
            for doc in colSnap:
                 data = doc.to_dict()
                 data["id"]=doc.id 
                 objList.append(cls(**data))
            return objList
        except Exception as e:
            print(e)
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("CTA").document(id).get() 
        return cls(**docSnap)


class Social(BaseModel):
    id : Optional[str]
    facebook : Optional[str]
    instagram : Optional[str]
    website : Optional[str]
    linkedIn : Optional[str]
    telegram : Optional[str]
    facebook : Optional[str]

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
        try:
            for doc in colSnap:
                 data = doc.to_dict()
                 data["id"]=doc.id 
                 objList.append(cls(**data))
            return objList
        except Exception as e:
            print(e)
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("Social").document(id).get() 
        return cls(**docSnap)


class Faq(BaseModel):
    id : Optional[str]
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
        try:
            for doc in colSnap:
                 data = doc.to_dict()
                 data["id"]=doc.id 
                 objList.append(cls(**data))
            return objList
        except Exception as e:
            print(e)
    
    @classmethod 
    def get_by_id(cls,username,id):
        docSnap = db.collection("Hero").document(username).collection("FAQ").document(id).get() 
        return cls(**docSnap)
