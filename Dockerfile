# Use official Python slim image
FROM python:3.13-slim

# Set env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

# copy and install requirements
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /app/

# collect static (optional) - will run at container start
CMD ["gunicorn", "job_board.wsgi.application", "--bind", "0.0.0.0:8000", "--workers", "3"]
