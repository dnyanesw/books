from sqlalchemy import CheckConstraint

from db import db
from models.base_model import BaseModel


class BooksBookshelfModel(db.Model, BaseModel):
    __tablename__: str = "books_bookshelf"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(16), unique=True, nullable=False)

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksBookshelfModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
