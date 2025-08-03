# Use official FastAPI base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set working directory
WORKDIR /app

# Copy current app (set by docker-compose) into the container
COPY ./ /app
