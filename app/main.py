from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from admin.mainRouter import main_router
from core.config import config

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://192.168.0.113:3000",
    "http://192.168.0.104:3000",
    "http://192.168.0.113:8000",
    "http://192.168.0.104:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix=config.API_V1_STR)