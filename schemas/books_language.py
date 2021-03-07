from marshmallow import EXCLUDE
from ma import ma
from models.books_language import BooksLanguageModel


class BooksLanguageSchema(ma.ModelSchema):
    class Meta:
        model = BooksLanguageModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)
