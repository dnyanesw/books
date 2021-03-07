web: gunicorn app:app
worker: celery -A libs.tasks.celery worker -l info -c 5 -E
