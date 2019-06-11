FROM python:3.7-alpine
LABEL MAINTAINER="Yannic Schencking <info@yannic.io>"

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app

RUN apk --no-cache add --virtual build-env \
    build-base \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del build-env

COPY ./scraper.py /usr/src/app
COPY immo_scraper /usr/src/app/immo_scraper

CMD ["python", "/usr/src/app/scraper.py"]
