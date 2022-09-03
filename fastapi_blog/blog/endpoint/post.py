from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from fastapi_blog.auth.service import get_current_active_user
from fastapi_blog.db.utils import get_db

from fastapi_blog.user.schemas import User

from ..service import service_post
from .. import schemas


post_router = APIRouter()


@post_router.post('/', response_model=schemas.PostResponse)
def create_post(
    post: schemas.CreatePost,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    return service_post.create(db, post, owner_id=user.id, status='publish')


@post_router.get('/', response_model=schemas.Post)
def get_post(
    id: int,
    db: Session = Depends(get_db)
):
    return service_post.get(db, id)


@post_router.get('/all/', response_model=list[schemas.PostResponse])
def all_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service_post.all(db, skip, limit)


@post_router.put('/', response_model=schemas.UpdatePost)
def update_post(
    id: int,
    post: schemas.UpdatePost,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    return service_post.update(db, id, post, owner_id=user.id)
