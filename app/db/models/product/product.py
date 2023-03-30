from datetime import datetime
from uuid import UUID
from typing import Union,Optional
from pydantic import BaseModel
from core.firebase import db


class Product(BaseModel):
    id :Union[UUID,int]
    title: str
    caption : Optional[str]
    image : str
    price : Optional[float]
    created_at : datetime = datetime.now()
    category : Optional[str]

    @classmethod
    def create(cls,**kwargs):
        obj = cls(**kwargs)
        db.collection("Users").document(f"{kwargs['username']}").collection("Products").document(f"{obj.id}").set(obj.dict())
        return obj

    


