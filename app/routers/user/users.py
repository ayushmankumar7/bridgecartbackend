from fastapi import APIRouter,Request, Response , Depends
from db.models.user.user import User
from utils.user.user import create_jwt,verify_google_token
from typing import Annotated
from utils.user.auth import IsAuthenticated
# from schemas.user import User

router = APIRouter()

@router.post("/signup")
async def sign_up(request: Request,response: Response):
    try:
        data = await request.json()
        User.create(**data)
        return {"message":"Registration successful"}
    except Exception as e:
        response.status_code = 400
        return {"error":str(e)}
    

@router.post("/login")
async def login(request: Request,response: Response):
    try:
        data =await request.json()
        user = User.get_by_email(data["email"],data["password"])
        return {
            "access":create_jwt(user),
        }
    except Exception as e:
        print(e)
        response.status_code = 400
        return {"error":str(e)}
    
@router.get("/me")
async def me(request: Request,response: Response,auth: Annotated[User,"Authentication"] =Depends(IsAuthenticated)):
    auth.password = ""
    return auth.dict()

@router.post("/google/login")
async def googlelogin(request: Request,response: Response):
    try:
        data =await request.json()
        
        a=verify_google_token(data["token"])
        user={}
        if(a is not None): 
            user = User.get_by_firebaseId(a["uid"])
            return {
                    "access":create_jwt(user),
                }
    except Exception as e:
        print(e)
        response.status_code = 400
        return {"error":str(e)}

