FROM python:3.7-slim
LABEL MAINTAINER="Yannic Schencking <info@yannic.io>"

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app

RUN apt-get update && \
    apt-get install -y gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY ./scraper.py /usr/src/app
COPY immo_scraper /usr/src/app/immo_scraper

CMD ["python", "/usr/src/app/scraper.py"]
