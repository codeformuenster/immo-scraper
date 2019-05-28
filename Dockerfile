FROM python:3.7-alpine
LABEL MAINTAINER="Yannic Schencking <info@yannic.io>"

WORKDIR /usr/src/app

RUN apk --no-cache add --virtual build-env \
    build-base \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev \
  && pip install --no-cache-dir \
    scrapy \
    bs4 \
  && apk del build-env

COPY ./scraper.py /usr/src/app

CMD ["python", "/usr/src/app/scraper.py"]