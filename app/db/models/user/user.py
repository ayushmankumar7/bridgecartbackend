from datetime import datetime
from typing import Optional, Union
from uuid import UUID
from core.firebase import db,auth
from pydantic import BaseModel
from utils.user.user import (
    verify_password,
    hash_password,
    create_jwt,
    decode_jwt    
)

class User(BaseModel):
    id: Union[UUID,int,str]
    firebase_id : Optional[str]
    email : str
    password: str
    name: Optional[str]
    note: Optional[str]
    active: bool = True
    #created_date: datetime = datetime.now()
    @classmethod
    def create(cls,**kwargs):
        kwargs["password"]=hash_password(kwargs["password"])
        instance = cls(**kwargs)
        db.collection("Accounts").document(instance.id).set(instance.dict())
    @classmethod
    def verify_by_email(cls,email,password):
        userDocument = db.collection("Accounts").where("email","==",email).get()[0]
        if userDocument is None:
            raise ValueError("User does not exist")
        if verify_password(password,userDocument.get("password")) or password == userDocument.get("password"):
            return True
        return False
    @classmethod
    def get_by_email(cls,email,password):
        if cls.verify_by_email(email,password):
            userDocument = db.collection("Accounts").where("email","==",email).get()[0].to_dict()
            return cls(**userDocument)
        else:
            raise ValueError("Given credentials are incorrect")
    @classmethod
    def get_by_token(cls,token):
        data = decode_jwt(token)
        try:
            return cls.get_by_email(data["email"],data["password"])
        except Exception as e:
            raise ValueError(str(e))
