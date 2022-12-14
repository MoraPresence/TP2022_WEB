FROM python:3
RUN apt update -y && \
    apt install -y python3 python3-pip
RUN pip install --upgrade pip

RUN pip install asgiref
RUN pip install django-bootstrap-v5
RUN pip install Faker
RUN pip install requests
RUN pip install psycopg2-binary
RUN pip install Pillow
RUN pip install Django

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app


