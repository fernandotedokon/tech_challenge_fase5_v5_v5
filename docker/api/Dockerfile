FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements-api.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements-api.txt

COPY src/ ./src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
