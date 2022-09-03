from fastapi import APIRouter

from fastapi_blog.auth.api import auth_router
from fastapi_blog.user.api import user_router
from fastapi_blog.blog.endpoint.post import post_router
from fastapi_blog.blog.endpoint.comment import comment_router


routes = APIRouter()


routes.include_router(user_router, prefix='/user', tags=['user'])
routes.include_router(auth_router, prefix='/auth', tags=['auth'])
routes.include_router(post_router, prefix='/post', tags=['post'])
routes.include_router(comment_router, prefix='/comment', tags=['comment'])
