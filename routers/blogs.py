from fastapi import APIRouter, Depends, status
from dependencies import get_db, get_current_user
from sqlalchemy.orm import Session
from schemas import blogs as schemas
from schemas.users import ReadUser
from repository import blogs as repo

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)

@router.post('/create/', response_model=schemas.ReadBlog)
def create_blog_for_user(
    blog: schemas.CreateBlog,
    current_user: ReadUser= Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return repo.create_user_blog(db=db, blog=blog, user_id=current_user.id)

@router.get('/', response_model=list[schemas.ListBlog])
def blogs_list(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return repo.get_blogs(db=db, skip=skip, limit=limit)

@router.get('/blog_id', response_model=schemas.ReadBlog)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return repo.get_blog(db = db, blog_id=blog_id)


@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    blog_id:int, 
    db: Session = Depends(get_db),
    current_user: ReadUser= Depends(get_current_user)
):
    return repo.destroy_blog(blog_id=blog_id, db=db)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    blog_id:int, 
    request: schemas.CreateBlog, 
    db: Session = Depends(get_db),
    current_user: ReadUser= Depends(get_current_user)    
):
    return repo.update_blog(blog_id=blog_id, db=db, request=request)