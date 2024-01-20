from fastapi import FastAPI
from routers import users, blogs, authentications

import os

app = FastAPI()

app.include_router(authentications.router)
app.include_router(users.router)
app.include_router(blogs.router)

# JWT
SECRET_KEY = os.environ.get("SECRET_KEY") 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30