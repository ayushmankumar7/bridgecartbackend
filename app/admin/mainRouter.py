from routers.product.products import router as product_router
from routers.user.users import router as user_router
from routers.hero.hero import router as hero_router
from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(product_router)
main_router.include_router(user_router)
main_router.include_router(hero_router)
