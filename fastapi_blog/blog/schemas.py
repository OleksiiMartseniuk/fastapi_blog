from pydantic import BaseModel

from datetime import datetime

from fastapi_blog.user.schemas import UserName


class CommentId(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Post(BaseModel):
    id: int
    title: str
    body: str
    created: datetime
    updated: datetime | None
    status: str
    owner: UserName
    comments: list[CommentId]
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


class PostTitle(BaseModel):
    title: str

    class Config:
        orm_mode = True


class Info(BaseModel):
    message: str


class Comment(BaseModel):
    id: int
    body: str
    created: datetime
    updated: datetime | None
    active: bool
    owner: UserName
    post: PostTitle

    class Config:
        orm_mode = True


class CreateComment(BaseModel):
    body: str


class UpdateComment(BaseModel):
    body: str
