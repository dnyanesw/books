from marshmallow import EXCLUDE, fields
from ma import ma
from models.books_book import BooksBookModel
from schemas.books_book_authors import BooksBookAuthorsSchema
from schemas.books_book_bookshelves import BooksBookBookshelvesSchema
from schemas.books_book_languages import BooksBookLanguagesSchema
from schemas.books_book_subjects import BooksBookSubjectsSchema
from schemas.books_format import BooksFormatSchema


class BooksBookSchema(ma.ModelSchema):
    class Meta:
        model = BooksBookModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)

    books_author = fields.Nested(BooksBookAuthorsSchema, many = True, exclude = ('books_book',))
    book_shelf = fields.Nested(BooksBookBookshelvesSchema, many = True, exclude = ('books_bookshelf',))
    book_language = fields.Nested(BooksBookLanguagesSchema, many = True, exclude = ('books_book_language',))
    book_subject = fields.Nested(BooksBookSubjectsSchema, many = True, exclude = ('books_book_subject',))
    book_format = fields.Nested(BooksFormatSchema, many = True, exclude = ('format',))
