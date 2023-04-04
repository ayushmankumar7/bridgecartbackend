from fastapi import APIRouter,Request, Response
from db.models.product.product import Product
router = APIRouter()

@router.get("/product/")
async def create_product(request: Request, response: Response):
    return {"message":"No get yet"}
@router.post("/product/")
async def create_product(request: Request, response: Response):
    try:    
        data = await request.json()
        Product.create(**data)
        return {"message":"succesfully created"}
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
async def get_product_by_id(username : str,category: str,response:Response):
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
