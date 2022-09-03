from typing import TypeVar, Generic

from fastapi import HTTPException

from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.orm import Session
from pydantic import BaseModel


ModelType = TypeVar('ModelType', bound=Model)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: ModelType) -> None:
        self.model = model

    def _not_exist(self):
        raise HTTPException(status_code=404, detail="Object not found")

    def get(self, db: Session, id: int, **kwargs) -> ModelType:
        db_model: ModelType = (
            db.query(self.model).
            filter_by(id=id, **kwargs).
            first()
        )
        if not db_model:
            self._not_exist()
        return db_model

    def create(
        self, db: Session, item: CreateSchemaType, **kwargs
    ) -> ModelType:
        db_model = self.model(**item.dict(), **kwargs)
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        return db_model

    def update(
        self, db: Session, id: int, item: UpdateSchemaType, **kwargs
    ) -> ModelType:
        db_model = self.get(db, id, **kwargs)

        for key, value in item.dict(exclude_unset=True).items():
            if hasattr(db_model, key):
                setattr(db_model, key, value)

        db.commit()
        db.refresh(db_model)
        return db_model

    def delete(self, db: Session, id: int, **kwargs) -> ModelType:
        db_model = self.get(db, id, **kwargs)
        db.delete(db_model)
        db.commit()
        return db_model

    def all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        db_models: list[ModelType] = (
            db.query(self.model).
            order_by('id').
            offset(skip).
            limit(limit).
            all()
        )
        return db_models
