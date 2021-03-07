from marshmallow import EXCLUDE, fields
from ma import ma
from models.books_book_languages import BooksBookLanguagesModel
from schemas.books_language import BooksLanguageSchema


class BooksBookLanguagesSchema(ma.ModelSchema):
    class Meta:
        model = BooksBookLanguagesModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)

    language = fields.Nested(BooksLanguageSchema)
