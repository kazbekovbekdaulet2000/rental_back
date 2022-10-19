FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev ffmpeg

RUN pip install --upgrade pip
RUN mkdir /app

COPY . /app

WORKDIR /app
COPY ./requirements.txt /requirements.txt
COPY ./scripts /scripts
COPY ./.env ./.env
COPY ./.env.dev ./.env.dev


RUN pip install -r requirements.txt
RUN chmod +x /scripts/*

CMD ["scripts/entrypoint.sh"]
