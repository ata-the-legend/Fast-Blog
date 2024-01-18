from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Annotated
from jose import jwt


# Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


    def bcrypt(password: str):
        return pwd_context.hash(password)
    
# JWT
SECRET_KEY = "09d25e094faa6ca2556c818166b7hso3b93f7099f6f0f4caa6cf63b88e8d3e9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

