from fastapi_blog.base.crud import CRUD
from fastapi_blog.db.base import Post, Comment, Tag

from sqlalchemy.orm import Session

from . import schemas


class PostService(CRUD[Post, schemas.CreatePost, schemas.UpdatePost]):
    pass


class CommentService(CRUD[Comment, schemas.CreateComment, schemas.UpdateComment]):
    pass


class TagService(CRUD[Tag, schemas.CreateTag, schemas.UpdateTag]):

    def add_tag(
        self, db: Session, tag_id: int, post_id: int, owner_id: int
    ) -> None:
        post: Post = (
            db.query(Post).
            filter(Post.id == post_id, Post.owner_id == owner_id).
            first()
        )
        if not post:
            self._not_exist()
        tag = self.get(db, tag_id)
        post.tags.append(tag)
        db.add(post)
        db.commit()
        db.refresh(post)


service_tag = TagService(Tag)
service_comment = CommentService(Comment)
service_post = PostService(Post)
