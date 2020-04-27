FROM python:3.7.3

ENV PYTHONUNBUFFERED 1

RUN apt-get update

WORKDIR /app

ADD requirements /app/requirements

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements/base.txt
