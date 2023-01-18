FROM python:3.11-slim

ENV PYTHONUNBUGGERED 1 \
    PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade setuptools pip
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends build-essential

WORKDIR app/

COPY requirements.txt .
COPY prepare.sh .

RUN pip install -r requirements.txt

COPY fanreceive/ .

ENTRYPOINT ["/bin/sh", "prepare.sh"]
