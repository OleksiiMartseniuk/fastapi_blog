from pydantic import BaseModel

from datetime import datetime

from fastapi_blog.user.schemas import UserName


class Post(BaseModel):
    id: int
    title: str
    body: str
    created: datetime
    updated: datetime
    status: str
    owner: UserName
    comments: list[int] = []
    tags: list[int] = []

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    body: str


class CreatePost(PostBase):
    pass


class UpdatePost(PostBase):
    pass


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
