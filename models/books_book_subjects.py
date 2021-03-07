from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

from db import db
from models.base_model import BaseModel


class BooksBookSubjectsModel(db.Model, BaseModel):
    __tablename__: str = "books_book_subjects"

    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('books_subject.id'), nullable=False)

    subject = relationship("BooksSubjectModel", foreign_keys = subject_id)
    books_book_subject = relationship("BooksBookModel", foreign_keys = book_id, backref='book_subject')

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksBookSubjectsModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
