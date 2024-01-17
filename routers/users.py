from fastapi import APIRouter, Depends, HTTPException
from schemas import users as schemas
from dependencies import get_db
from sqlalchemy.orm import Session
from repository import users as repo

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/signup/', response_model=schemas.ReadUser)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = repo.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repo.create_user(db=db, user=user)

@router.get('/', response_model=list[schemas.ListUser])
def list_user(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = repo.get_users(db=db, skip=skip, limit=limit)
    return users

@router.get('/{user_id}', response_model= schemas.ReadUser)
def read_user(
    user_id: int, db : Session = Depends(get_db)
):
    db_user = repo.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

