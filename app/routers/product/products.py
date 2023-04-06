from fastapi import APIRouter, Depends,Request, Response
from db.models.product.product import Product
from fastapi_pagination import paginate,Params
from db.models.user.user import User
from typing import Annotated
from utils.user.auth import IsAuthenticated
router = APIRouter()

@router.get("/{username}/product/")
async def create_product(username: str,request: Request, response: Response):
    try:    
        productList = Product.get_by_username(username=username)
        resList = []
        for product in productList:
            resList.append(product.dict())
        return paginate(resList,params=Params(size=10))
    except Exception as e:
        response.status_code = 400
        return {"error":str(e)}

@router.get("/product/")
async def view_product(request: Request, 
                         response: Response,
                         auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                         ):
    try:    
        print(auth)
        productList = Product.get_by_username(username=auth.id)
        resList = []
        for product in productList:
            resList.append(product.dict())
        return paginate(resList,params=Params(size=10))
    except Exception as e:
        response.status_code = 400
        return {"error":str(e)}

@router.post("/product/")
async def create_product(request: Request, 
                         response: Response, 
                         auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)):
    try:    
        data = await request.json()
        data["username"]=auth.id
        Product.create(**data)
        return {"message":"succesfully created"}
    except Exception as e:
        response.status_code = 400
        return {"message":"Provide proper json","error":str(e)}
@router.patch("/product/")
async def update_product(request: Request, 
                         response: Response, 
                         auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)):
    try:    
        data = await request.json()
        data["username"]=auth.id
        Product(**data).save()
        return {"message":"succesfully updated"}
    except Exception as e:
        response.status_code = 400
        return {"message":"Provide proper json","error":str(e)}
@router.delete("/product/")
async def delete_product(request: Request, 
                         response: Response, 
                         auth :Annotated[User,"Authentication"]=Depends(IsAuthenticated)):
    try:    
        data = await request.json()
        data["username"]=auth.id
        Product(**data).delete()
        return {"message":"succesfully deleted"}
    except Exception as e:
        response.status_code = 400
        return {"message":"Provide proper json","error":str(e)}



@router.get("/{username}/product/{id}")
async def get_product_by_id(username : str,id: str,response:Response):
    try:
        obj = Product.get_by_id(username=username,id=id)
        return obj.dict()
    except Exception as e:
        print(e)
        response.status_code = 400
        return {"error":str(e)}



@router.get("/{username}/product-by-category/{category}")
async def get_product_by_category(username : str,category: str,response:Response):
    try:
        productList = Product.get_by_category(username=username,category=category)
        resList = []
        for product in productList:
            resList.append(product.dict())
        return resList

    except Exception as e:
        print(e)
        response.status_code = 400
        return {"error":str(e)}
