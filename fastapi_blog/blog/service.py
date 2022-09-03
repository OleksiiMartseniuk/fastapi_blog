from fastapi_blog.base.crud import CRUD
from fastapi_blog.db.base import Post, Comment

from . import schemas


class PostService(CRUD[Post, schemas.CreatePost, schemas.UpdatePost]):
    pass


class CommentService(CRUD[Comment, schemas.CreateComment, schemas.UpdateComment]):
    pass


service_comment = CommentService(Comment)
service_post = PostService(Post)
