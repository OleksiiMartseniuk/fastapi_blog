from pydantic import BaseModel

from datetime import datetime

from fastapi_blog.user.schemas import UserName


class Post(BaseModel):
    id: int
    title: str
    body: str
    created: datetime
    updated: datetime | None
    status: str
    owner: UserName
    comments: list[int] = []
    tags: list[int] = []

    class Config:
        orm_mode = True


class CreatePost(BaseModel):
    title: str
    body: str


class UpdatePost(BaseModel):
    title: str = None
    body: str = None


class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    updated: datetime | None
    created: datetime
    status: str
    owner: UserName

    class Config:
        orm_mode = True
