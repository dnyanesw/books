from db import db
from models.base_model import BaseModel


class BooksSubjectModel(db.Model, BaseModel):
    __tablename__: str = "books_subject"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), unique=True)

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksSubjectModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()
