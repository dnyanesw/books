from sqlalchemy import CheckConstraint, or_

from config import PAGE_SIZE
from db import db
from models.base_model import BaseModel
from models.books_author import BooksAuthorModel
from models.books_book_authors import BooksBookAuthorsModel
from models.books_book_bookshelves import BooksBookBookshelvesModel
from models.books_book_languages import BooksBookLanguagesModel
from models.books_book_subjects import BooksBookSubjectsModel
from models.books_bookshelf import BooksBookshelfModel
from models.books_format import BooksFormatModel
from models.books_language import BooksLanguageModel
from models.books_subject import BooksSubjectModel


class BooksBookModel(db.Model, BaseModel):
    __tablename__: str = "books_book"

    id = db.Column(db.Integer, primary_key = True)
    download_count = db.Column(db.Integer, CheckConstraint('download_count >= 0'))
    gutenberg_id = db.Column(db.Integer, CheckConstraint('gutenberg_id >= 0'), unique=True, nullable=False)
    media_type = db.Column(db.String(16), nullable=False)
    title = db.Column(db.String(1024))

    @classmethod
    def find_by_id(cls, _id: int) -> "BooksBookModel":
        return cls.query.filter_by(id = _id, deleted_at = None).first()

    @classmethod
    def get_all(cls, page, search_filter: dict) -> "BooksBookModel":
        query = cls.query

        # book_id
        if 'book_id' in search_filter:
            query = query.filter_by(gutenberg_id=search_filter["book_id"])

        # language
        if 'language' in search_filter:
            query = query.join(BooksBookLanguagesModel).join(BooksLanguageModel).filter(
                BooksLanguageModel.code.in_(search_filter['language']))

        # mime_type
        if 'mime_type' in search_filter:
            query = query.join(BooksFormatModel).filter(BooksFormatModel.mime_type == search_filter["mime_type"])

        # topic
        if 'topic' in search_filter:
            search_topic = "%{}%".format(search_filter['topic'])
            query = query.join(BooksBookSubjectsModel).join(BooksSubjectModel).join(BooksBookBookshelvesModel).join(
                BooksBookshelfModel).filter(BooksSubjectModel.name.ilike(search_topic) |
                                            BooksBookshelfModel.name.ilike(search_topic))

        # author
        if 'author' in search_filter:
            search_author = "%{}%".format(search_filter['author'])
            query = query.join(BooksBookAuthorsModel).join(BooksAuthorModel).filter(
                BooksAuthorModel.name.ilike(search_author))

        # title
        if 'title' in search_filter:
            search_title = "%{}%".format(search_filter['title'])
            query = query.filter(cls.title.ilike(search_title))

        query = query.order_by(cls.download_count.desc())
        return query.paginate(page, PAGE_SIZE, False)
