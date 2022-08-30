from fastapi import APIRouter

from fastapi_blog.user.api import user_router


routes = APIRouter()


routes.include_router(user_router, prefix='/user', tags=['user'])
