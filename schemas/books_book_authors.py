from marshmallow import EXCLUDE, fields
from ma import ma
from models.books_book_authors import BooksBookAuthorsModel
from schemas.books_author import BooksAuthorSchema


class BooksBookAuthorsSchema(ma.ModelSchema):
    class Meta:
        model = BooksBookAuthorsModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)

    author = fields.Nested(BooksAuthorSchema)
