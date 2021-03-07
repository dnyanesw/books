from marshmallow import EXCLUDE
from ma import ma
from models.books_subject import BooksSubjectModel


class BooksSubjectSchema(ma.ModelSchema):
    class Meta:
        model = BooksSubjectModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)
