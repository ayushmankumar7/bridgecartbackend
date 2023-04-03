from fastapi import APIRouter,Request, Response
from db.models.user.user import User
from utils.user.user import create_jwt
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
@router.post("/me")
async def me(request: Request,response: Response):
    token = request.headers.get("Authorization").split(" ")[-1]
    user = User.get_by_token(token)
    user.password = ""
    return user.dict()
