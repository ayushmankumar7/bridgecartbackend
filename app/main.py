from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi_pagination import add_pagination
from admin.mainRouter import main_router
from core.config import config

from mangum import Mangum

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://192.168.0.113:3000",
    "http://192.168.0.104:3000",
    "http://192.168.0.113:8000",
    "http://192.168.0.104:8000",
   " https://4908-202-8-114-45.ngrok.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix=config.API_V1_STR)

add_pagination(app)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)