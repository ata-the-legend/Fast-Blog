from repository import users
from utils import Hash
from sqlalchemy.orm import Session

def authenticate_user(db: Session, username: str, password: str):
    user = users.get_user_by_email(db, username)
    if not user:
        return False
    if not Hash.verify_password(password, user.password):
        return False
    return user