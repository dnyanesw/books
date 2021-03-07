from db import db
from models.base_model import BaseModel


class BooksLanguageModel(db.Model, BaseModel):
    __tablename__: str = "books_language"

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(4), unique=True)

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksLanguageModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
