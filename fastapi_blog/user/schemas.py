from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str | None
    created: datetime
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str
    email: str | None


class UserUpdate(BaseModel):
    username: str = None
    email: str = None
