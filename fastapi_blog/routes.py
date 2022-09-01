from fastapi import APIRouter

from fastapi_blog.auth.api import auth_router
from fastapi_blog.user.api import user_router


routes = APIRouter()


routes.include_router(user_router, prefix='/user', tags=['user'])
routes.include_router(auth_router, prefix='/auth', tags=['auth'])
