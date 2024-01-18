from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
import config

# Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


    def bcrypt(password: str):
        return pwd_context.hash(password)
    
# JWT
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt

