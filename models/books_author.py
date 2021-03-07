from db import db
from models.base_model import BaseModel


class BooksAuthorModel(db.Model, BaseModel):
    __tablename__: str = "books_author"

    id = db.Column(db.Integer, primary_key = True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    name = db.Column(db.String(128))

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksAuthorModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
