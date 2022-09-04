from fastapi_blog.base.crud import CRUD
from fastapi_blog.db.base import Post, Comment, Tag

from . import schemas


class PostService(CRUD[Post, schemas.CreatePost, schemas.UpdatePost]):
    pass


class CommentService(CRUD[Comment, schemas.CreateComment, schemas.UpdateComment]):
    pass


class TagService(CRUD[Tag, schemas.CreateTag, schemas.UpdateTag]):
    pass


service_tag = TagService(Tag)
service_comment = CommentService(Comment)
service_post = PostService(Post)
