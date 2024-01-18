from fastapi import APIRouter, Depends, HTTPException, status
from schemas import authentications as schemas
from dependencies import get_db
from sqlalchemy.orm import Session
from repository import authentications as repo
from datetime import timedelta
from utils import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(
    tags=['Authenticaton']
)

@router.post('/login/')
def login(request: schemas.LoginUser, db: Session = Depends(get_db)) -> schemas.Token:
    user = repo.authenticate_user(db=db, username=request.username, password=request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")