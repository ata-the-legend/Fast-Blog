from fastapi import APIRouter, Depends, status
from dependencies import get_db
from sqlalchemy.orm import Session
from schemas import blogs as schemas
from repository import blogs as repo
from repository import users as users_repo

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)

@router.post('/create/{user_id}', response_model=schemas.ReadBlog)
def create_blog_for_user(
    user_id: int, blog: schemas.CreateBlog, db: Session = Depends(get_db)
    ):
    return repo.create_user_blog(db=db, blog=blog, user_id=user_id)

@router.get('/', response_model=list[schemas.ListBlog])
def blogs_list(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return repo.get_blogs(db=db, skip=skip, limit=limit)

@router.get('/blog_id', response_model=schemas.ReadBlog)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return repo.get_blog(db = db, blog_id=blog_id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return repo.destroy_blog(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.CreateBlog, db: Session = Depends(get_db)):
    return repo.update_blog(id,request, db)