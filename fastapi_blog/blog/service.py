from fastapi_blog.base.crud import CRUD
from fastapi_blog.db.base import Post

from . import schemas


class PostService(CRUD[Post, schemas.CreatePost, schemas.UpdatePost]):
    pass


service_post = PostService(Post)
