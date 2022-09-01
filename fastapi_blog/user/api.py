from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from fastapi_blog.db.utils import get_db
from fastapi_blog.auth.service import get_current_active_user

from .service import user_service
from . import schemas


user_router = APIRouter()


@user_router.post('/', response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_service.create(db, user, is_active=True, is_admin=False)


@user_router.get('/', response_model=schemas.User)
def get_user(current_user: schemas.User = Depends(get_current_active_user)):
    return current_user


@user_router.put('/', response_model=schemas.User)
def update_user(
    user: schemas.UserUpdate,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return user_service.update(db, current_user.id, user)


@user_router.delete('/', response_model=schemas.User)
def delete_user(
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return user_service.delete(db, current_user.id)
