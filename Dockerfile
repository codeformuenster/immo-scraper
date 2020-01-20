FROM python:3.7-slim

# system dependencies
RUN apt-get update && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

# python dependencies
WORKDIR /usr/src/app
COPY ./setup.py /usr/src/app
COPY ./requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

# project source
COPY bin /usr/src/app/bin
COPY immo_scraper /usr/src/app/immo_scraper
COPY secret /usr/src/app/secret
