from typing import Optional
from pydantic import BaseModel
from enum import Enum


class OperationStatus(str, Enum):
    IN_GAME = 'in game'
    OUT_GAME = 'out game'


class OperationBase(BaseModel):
    name: str
    age: int
    email: str
    status: OperationStatus
    description: Optional[str]


class User(OperationBase):
    id: int

    class Config:
        orm_mode = True


class CreateUser(OperationBase):
    pass


class UpdateUser(OperationBase):
    pass


class DeleteUser(OperationBase):
    pass


class InGame(BaseModel):
    status: OperationStatus

