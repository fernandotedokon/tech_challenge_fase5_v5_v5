FROM python:3.10

WORKDIR /app

COPY requirements-ml.txt .

RUN pip install -r requirements-ml.txt

COPY src/ ./src/
