from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


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

    owner = relationship("User", back_populates="posts")
