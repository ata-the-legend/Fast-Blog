from pydantic import BaseModel
from typing import List, Optional
from schemas.blogs import ListBlog

class BaseUser(BaseModel):
    name:str
    email: str
    
class CreateUser(BaseUser):
    password: str

class ReadUser(BaseUser):
    id: int
    blogs: List[ListBlog]=[]
    
    class config:
        orm_mode = True

class ListUser(BaseUser):
    class config:
        orm_mode = True

class LoginUser(BaseModel):
    username: str
    password: str


