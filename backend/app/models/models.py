from pydantic import BaseModel # type: ignore
from typing import Any  

class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

class ResponseModel(BaseModel):
    message: str
    data: Any