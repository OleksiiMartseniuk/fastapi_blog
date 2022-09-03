from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from fastapi_blog.auth.service import get_current_active_user
from fastapi_blog.db.utils import get_db

from fastapi_blog.user.schemas import User

from ..service import service_comment
from .. import schemas


comment_router = APIRouter()


@comment_router.post('/', response_model=schemas.Comment)
def create_comment(
    post_id: int,
    comment: schemas.CreateComment,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    comment = service_comment.create(
        db, comment, active=True, owner_id=user.id, post_id=post_id
    )
    return comment


@comment_router.put('/', response_model=schemas.Comment)
def update_comment(
    id: int,
    comment: schemas.UpdateComment,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    return service_comment.update(db, id, comment, owner_id=user.id)


@comment_router.delete('/', response_model=schemas.Info)
def delete_comment(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    service_comment.delete(db, id, owner_id=user.id)
    return {'message': 'comment remove'}
