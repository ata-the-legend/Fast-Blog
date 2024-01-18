from database import SessionLocal

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from schemas.authentications import TokenData
from repository.users import get_user_by_email
import config

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Oauth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")        

async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token_data = verify_token(token, credentials_exception)

    user = get_user_by_email(db, email=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return TokenData(username=username)
    except JWTError:
        raise credentials_exception