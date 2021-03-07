import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from sqlalchemy import exc
from config import CORS_URL
from db import db
from ma import ma
from resources.v1.books_book import BooksBook

app = Flask(__name__)
app.config.from_envvar("APPLICATION_SETTINGS")

CORS(app, origins=CORS_URL, allow_headers=["Content-Type", "Authorization"])

api = Api(app)
db.init_app(app)

# API V1 Start
api_v1 = "/api/v1"
api.add_resource(BooksBook, api_v1 + "/books")
# API V1 End
ma.init_app(app)


@app.errorhandler(exc.SQLAlchemyError)
def internal_error():
    db.session.rollback()


db.app = app


if __name__ == "__main__" and os.environ.get('ENVIRONMENT') == "dev":
    # To suppress twice call of cron job in debug mode
    app.run(port=8081, host="0.0.0.0")
