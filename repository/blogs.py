from fastapi import HTTPException, status
from dependencies import get_db
from sqlalchemy.orm import Session
import models

def create_user_blog(db: Session, blog, user_id):
    db_blog = models.Blog(**blog, user_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blogs(db: Session, skip: int, limit: int):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def get_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {blog_id} is not available")
    return blog

def destroy_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(blog_id == blog_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {blog_id} is not available"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_blog(db: Session, blog_id: int ,request):
    blog = db.query(models.Blog).filter(blog_id == blog_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {blog_id} is not available"
        )
    blog.update(request, synchronize_session=False)
    db.commit()
    return 'updated'