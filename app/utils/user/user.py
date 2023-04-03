from passlib.hash import pbkdf2_sha256
from jose import jwt
SECRET_KEY = "secret"
ALGORITHM = "HS256"
def verify_password(password,hash_password):
    return pbkdf2_sha256.verify(password,hash_password)

def hash_password(password):
    return pbkdf2_sha256.hash(password)

def create_jwt(user):
    return jwt.encode(user.dict(),SECRET_KEY,algorithm=ALGORITHM)

def decode_jwt(token):
    data = jwt.decode(token,SECRET_KEY,ALGORITHM)
    return data
