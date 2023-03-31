from fastapi import APIRouter,Request, Response
from db.models.product.product import Product
router = APIRouter()

@router.post("/product/")
async def create_product(request: Request, response: Response):
    try:    
        data = await request.json()
        Product.create(**data)
        return {"message":"succesfully created"}
    except Exception as e:
        print(e)
        response.status_code = 400
        return {"message":"Provide proper json","error":str(e)}
