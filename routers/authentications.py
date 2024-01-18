from fastapi import APIRouter, Depends, HTTPException, status
from schemas import users as schemas
from dependencies import get_db
from sqlalchemy.orm import Session
from repository import authentications as repo

router = APIRouter(
    tags=['Authenticaton']
)

@router.post('/login/', response_model=schemas.ReadUser)
def login(request: schemas.LoginUser, db: Session = Depends(get_db)):
    user = repo.authenticate_user(db=db, username=request.username, password=request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user