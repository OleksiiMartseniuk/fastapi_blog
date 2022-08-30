from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True)
    # Автоматически создаст временную метку на стороне базы данных
    created = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, nullable=False)
    is_admin = Column(Boolean, nullable=False)

    posts = relationship('Post', back_populates='owner')
