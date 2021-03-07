from marshmallow import EXCLUDE, fields
from ma import ma
from models.books_book_subjects import BooksBookSubjectsModel
from schemas.books_subject import BooksSubjectSchema


class BooksBookSubjectsSchema(ma.ModelSchema):
    class Meta:
        model = BooksBookSubjectsModel
        unknown = EXCLUDE
        # load_only = ()
        dump_only = ("id",)

    subject = fields.Nested(BooksSubjectSchema)
