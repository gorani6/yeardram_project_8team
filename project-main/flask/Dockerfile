FROM python:3.9-slim-bullseye

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

ENV PYTHONUNBUFFERED 1 

WORKDIR /flask

ADD . /flask

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uwsgi uwsgi.ini