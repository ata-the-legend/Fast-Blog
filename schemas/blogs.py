from pydantic import BaseModel


class BaseBlog(BaseModel):
    title: str
    body: str

class CreateBlog(BaseBlog):
    pass

class BlogCreator(BaseModel):
    id: int
    name:str
    email: str

    class config:
        orm_mode = True

class ReadBlog(BaseBlog):
    id: int
    creator: BlogCreator

    class config:
        orm_mode = True
        
class ListBlog(BaseBlog):
    id: int
    class config:
        orm_mode = True