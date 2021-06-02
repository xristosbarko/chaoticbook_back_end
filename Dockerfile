FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /chaoticbook
COPY . /chaoticbook/
RUN pip install -r requirements.txt
