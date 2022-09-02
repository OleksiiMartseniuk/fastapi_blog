from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Boolean,
    Table
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from fastapi_blog.db.database import Base


post_tag_table = Table(
    'post_tag',
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    # Автоматически создаст временную метку на стороне базы данных
    created = Column(DateTime(timezone=True), server_default=func.now())
    # Изменит временную метку при обновлении на стороне базы данных
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    tags = relationship(
        'Tag', secondary=post_tag_table, back_populates='posts'
    )


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    active = Column(Boolean, default=True, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    owner = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())

    posts = relationship(
        'Post', secondary=post_tag_table, back_populates='tags'
    )
