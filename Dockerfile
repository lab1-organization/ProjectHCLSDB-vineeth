# -------- Base Image --------
FROM python:3.13.7-slim

WORKDIR /app

# System dependencies (minimal, no mysql libs needed for PyMySQL)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

# Run Django
CMD ["python", "HclsPro/manage.py", "runserver", "0.0.0.0:8000"]
