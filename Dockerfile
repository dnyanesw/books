# Use the Python3.7.2 image
FROM python:3.7.4-stretch
#FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /eprocessify-backend

ADD . /eprocessify-backend

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev build-base linux-headers tzdata
RUN ["pip3", "install", "pipenv"]
RUN ["pipenv", "install"]
#CMD pipenv shell
#RUN ["pipenv", "run", "flask", "db", "upgrade"]
CMD pipenv run uwsgi app.ini
