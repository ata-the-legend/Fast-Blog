from fastapi import FastAPI
from routers import users, blogs, authentications

app = FastAPI()

app.include_router(authentications.router)
app.include_router(users.router)
app.include_router(blogs.router)

# JWT
SECRET_KEY = "09d25e094faa6ca2556c818166b7hso3b93f7099f6f0f4caa6cf63b88e8d3e9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30