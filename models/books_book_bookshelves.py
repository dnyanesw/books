from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

from db import db
from models.base_model import BaseModel


class BooksBookBookshelvesModel(db.Model, BaseModel):
    __tablename__: str = "books_book_bookshelves"

    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'), nullable=False)
    bookshelf_id = db.Column(db.Integer, db.ForeignKey('books_bookshelf.id'), nullable=False)

    shelf = relationship("BooksBookshelfModel", foreign_keys = bookshelf_id)
    books_bookshelf = relationship("BooksBookModel", foreign_keys = book_id, backref='book_shelf')

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksBookBookshelvesModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
