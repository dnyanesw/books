from marshmallow import EXCLUDE
from ma import ma
from models.books_author import BooksAuthorModel


class BooksAuthorSchema(ma.ModelSchema):
    class Meta:
        model = BooksAuthorModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)
