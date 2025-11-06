from pydantic import BaseModel
from .blog import BlogBase


class UserBase(BaseModel):
    name: str
    email: str


class UserRequest(UserBase):
    password: str


class UserResponse(UserBase):
    blogs: list[BlogBase]

    class Config():
        from_attributes = True
