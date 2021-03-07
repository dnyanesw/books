from marshmallow import EXCLUDE, fields
from ma import ma
from models.books_book_bookshelves import BooksBookBookshelvesModel
from schemas.books_bookshelf import BooksBookshelfSchema


class BooksBookBookshelvesSchema(ma.ModelSchema):
    class Meta:
        model = BooksBookBookshelvesModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)

    shelf = fields.Nested(BooksBookshelfSchema)
