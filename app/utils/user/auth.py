from utils.user.user import decode_jwt
from db.models.user.user import User
from fastapi import HTTPException,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


security = HTTPBearer()

async def IsAuthenticated(credentials: HTTPAuthorizationCredentials= Depends(security)):
    token = credentials.credentials

    try:
        payload = decode_jwt(token)
        user = User(**payload)
        return user
    except Exception as e:  # catches any exception
        raise HTTPException(
            status_code=401,
            detail=str(e))