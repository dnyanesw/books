from marshmallow import EXCLUDE
from ma import ma
from models.books_format import BooksFormatModel


class BooksFormatSchema(ma.ModelSchema):
    class Meta:
        model = BooksFormatModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)
