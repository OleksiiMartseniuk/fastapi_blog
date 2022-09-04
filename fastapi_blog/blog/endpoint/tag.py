from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from fastapi_blog.auth.service import (
    get_current_active_user,
    get_current_admin_user
)
from fastapi_blog.db.utils import get_db

from fastapi_blog.user.schemas import User

from ..service import service_tag
from .. import schemas


tag_router = APIRouter()


@tag_router.post('/', response_model=schemas.Tag)
def create_tag(
    tag: schemas.CreateTag,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    return service_tag.create(db, tag)


@tag_router.put('/')
def update_tag(
    id: int,
    tag: schemas.UpdateTag,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_admin_user)
):
    return service_tag.update(db, id, tag)


@tag_router.delete('/')
def delete_tag(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_admin_user)
):
    return service_tag.delete(db, id)
