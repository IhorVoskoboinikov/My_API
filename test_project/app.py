from typing import List
from fastapi import FastAPI

from .database import engine
from .tables import Base
from .models import operations
from .api import router

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router)

# @app.post("/users/")
# def create_user(user: operations.User):
#     return operations.User
