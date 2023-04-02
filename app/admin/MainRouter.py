from routers.product.products import router as product_router
from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(product_router)
