# Dockerfile for HeatAware AI - Advisory & Early Warning Microservice
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency definition
COPY microservices/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source & core analytics engine
COPY weather_analytics.py ./weather_analytics.py
COPY microservices/advisory_service.py ./advisory_service.py

# Expose microservice port
EXPOSE 8001

# Healthcheck probe
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8001/health || exit 1

# Launch microservice via Uvicorn ASGI server
CMD ["uvicorn", "advisory_service:app", "--host", "0.0.0.0", "--port", "8001"]
