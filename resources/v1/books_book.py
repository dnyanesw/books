from flask import request
from flask_restful import Resource

from config import PAGE_SIZE
from models.books_book import BooksBookModel
from schemas.books_book import BooksBookSchema


class BooksBook(Resource):
    @classmethod
    def get(cls):
        page = request.args.get('page', type = int, default = 1)

        params = request.args
        search_filter = {}
        if "book_id" in params:
            search_filter["book_id"] = params["book_id"]

        if "language" in params:
            search_filter["language"] = [data for data in params["language"].split(",")]

        if "mime_type" in params:
            search_filter["mime_type"] = params["mime_type"]

        if "topic" in params:
            search_filter["topic"] = params["topic"]

        if "author" in params:
            search_filter["author"] = params["author"]

        if "title" in params:
            search_filter["title"] = params["title"]

        data = BooksBookModel.get_all(page, search_filter)
        next_page = (data.total - page * PAGE_SIZE) > 0
        result = {"books": BooksBookSchema(many = True).dump(data.items), "next_page": next_page,
                  "total": data.total}
        return result, 200
