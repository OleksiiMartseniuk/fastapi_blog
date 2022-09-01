from fastapi_blog.base.crud import CRUD
from fastapi_blog.db.base import User

from sqlalchemy.orm import Session

from .security import get_password_hash
from . import schemas


class UserService(CRUD[User, schemas.UserCreate, schemas.UserUpdate]):
    def create(self, db: Session, item: schemas.UserCreate, **kwargs) -> User:
        hash_password = get_password_hash(item.password)
        item.password = hash_password
        return super().create(db, item, **kwargs)


user_service = UserService(User)
