FROM apache/airflow:2.7.0

USER root

# (opcional) instalar libs de sistema
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

USER airflow

COPY requirements-airflow.txt .

RUN pip install --no-cache-dir -r requirements-airflow.txt