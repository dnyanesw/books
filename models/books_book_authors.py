from sqlalchemy.orm import relationship

from db import db
from models.base_model import BaseModel


class BooksBookAuthorsModel(db.Model, BaseModel):
    __tablename__: str = "books_book_authors"

    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('books_author.id'), nullable=False)

    author = relationship("BooksAuthorModel", foreign_keys = author_id)
    books_book = relationship("BooksBookModel", foreign_keys = book_id, backref='books_author')

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksBookAuthorsModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
