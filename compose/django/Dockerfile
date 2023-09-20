FROM arm64v8/python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app/

SHELL ["/bin/bash", "-c"]

RUN apt update && apt install libpq-dev python3-dev -y

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
