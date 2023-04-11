from datetime import datetime
from uuid import UUID
from typing import Union,Optional
from pydantic import BaseModel
from core.firebase import db

class Category(BaseModel):
    id: str
    image: Optional[str]
    description: Optional[str]

    @classmethod 
    def set_category(cls,username,category,data):
        db.collection("Users").document(f"{username}").collection("Categories").document(category).set(data,merge=True)

    @classmethod
    def delete_category(cls,username,category):
        db.collection("Users").document(f"{username}").collection("Categories").document(category).delete()

class Variant(BaseModel):
    name:str
    value:list[str]
class Product(BaseModel):
    id :Union[UUID,int]
    title: Optional[str]
    caption : Optional[str]
    description: Optional[str]
    image : Optional[list]
    price : Optional[float]
    created_at : Optional[datetime] = datetime.now()
    category : Optional[str]
    variant: Optional[list[Variant]]
    username: Optional[str]

    @classmethod
    def create(cls,**kwargs):
        obj = cls(**kwargs)
        db.collection("Users").document(obj.username).collection("Products").document(f"{obj.id}").set(obj.dict())
        db.collection("Users").document(obj.username).collection("Categories").document(obj.category).collection("Products").document(f"{obj.id}").set({"is_active":True})
        return obj
    
    @classmethod
    def get_by_id(cls,username,id):
        itemDict = db.collection("Users").document(f"{username}").collection("Products").document(f"{id}").get().to_dict()
        return cls(**itemDict)
    
    @classmethod
    def get_by_category(cls,username,category):
        products = db.collection("Users").document(f"{username}").collection("Categories").document(category).collection("Products").stream()
        product_obj= []
        
        for product in products:        
            product_obj.append(cls.get_by_id(username,product.id))
       
        return product_obj
    
    @classmethod
    def get_by_username(cls,username):
        products = db.collection("Users").document(f"{username}").collection("Products").stream()
        product_obj= []
        for product in products:        
            try:
                product_obj.append(cls(**product.to_dict()))
            except Exception as e:
                pass
        product_obj.sort(key=lambda x:x.created_at, reverse=True)
        return product_obj


    @classmethod
    def get_all_categories(cls,userId):
        categories = db.collection("Users").document(f"{userId}").collection("Categories").stream()
        return [{"category":i.id,"metadata":i.to_dict()} for i in categories]

    def save(self):
        data = self.dict()
        for key in self.dict():
            if(data[key]==None):
                data.pop(key)
        db.collection("Users").document(self.username).collection("Products").document(f"{self.id}").update(data)
        db.collection("Users").document(self.username).collection("Categories").document(self.category).collection("Products").document(f"{self.id}").set({"is_active":True})

    def delete(self):
        db.collection("Users").document(self.username).collection("Products").document(f"{self.id}").delete()
        db.collection("Users").document(self.username).collection("Categories").document(self.category).collection("Products").document(f"{self.id}").delete()


