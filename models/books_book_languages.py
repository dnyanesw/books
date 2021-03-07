from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

from db import db
from models.base_model import BaseModel


class BooksBookLanguagesModel(db.Model, BaseModel):
    __tablename__: str = "books_book_languages"

    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('books_language.id'), nullable=False)

    language = relationship("BooksLanguageModel", foreign_keys = language_id)
    books_book_language = relationship("BooksBookModel", foreign_keys = book_id, backref='book_language')

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksBookLanguagesModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
