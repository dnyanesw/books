from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

from db import db
from models.base_model import BaseModel


class BooksFormatModel(db.Model, BaseModel):
    __tablename__: str = "books_format"

    id = db.Column(db.Integer, primary_key = True)
    mime_type = db.Column(db.String(32), nullable=False)
    url = db.Column(db.String(256))
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'), nullable=False)

    format = relationship("BooksBookModel", foreign_keys = book_id, backref='book_format')

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksFormatModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
