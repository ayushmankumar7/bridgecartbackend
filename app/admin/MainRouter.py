from routers.product.products import router as product_router
from routers.user.users import router as user_router
from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(product_router)
main_router.include_router(user_router)
