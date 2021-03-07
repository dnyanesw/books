from marshmallow import EXCLUDE
from ma import ma
from models.books_bookshelf import BooksBookshelfModel


class BooksBookshelfSchema(ma.ModelSchema):
    class Meta:
        model = BooksBookshelfModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)
