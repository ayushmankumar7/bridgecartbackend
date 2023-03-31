from datetime import datetime
from uuid import UUID
from typing import Union,Optional
from pydantic import BaseModel
from core.firebase import db

'''
1. Title 
2. Description 
3. Price
4. Product ID 
5. Category
6. Array of Image 
7. Variants - Can be color, size or Sets (2, 3, 5, 6 etc)
'''
class Product(BaseModel):
    id :Union[UUID,int]
    title: str
    caption : Optional[str]
    image : list
    price : Optional[float]
    created_at : datetime = datetime.now()
    category : Optional[str]
    variant: Optional[str]

    @classmethod
    def create(cls,**kwargs):
        obj = cls(**kwargs)
        db.collection("Users").document(f"{kwargs['username']}").collection("Products").document(f"{obj.id}").set(obj.dict())
        return obj

    


