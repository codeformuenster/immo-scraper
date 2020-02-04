FROM python:3.7-slim

# system dependencies
RUN apt-get update && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

# python dependencies
WORKDIR /app
COPY ./setup.py /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# project source
COPY bin /app/bin
COPY immo_scraper /app/immo_scraper
