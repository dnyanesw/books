import os
SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping': True}
SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URI")
SECRET_KEY=os.environ.get("SECRET_KEY")
JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
JWT_BLACKLIST_ENABLED = False
SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping': True}
PAGE_SIZE = int(os.environ.get("PAGE_SIZE"))
ENVIRONMENT = os.environ.get('ENVIRONMENT')
CORS_URL = os.environ.get('CORS_URL')
