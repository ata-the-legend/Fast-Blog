from fastapi import FastAPI
from routers import users, blogs, authentications

app = FastAPI()

app.include_router(authentications.router)
app.include_router(users.router)
app.include_router(blogs.router)