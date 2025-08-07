# # Use official FastAPI base image
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# # Set working directory
# WORKDIR /app

# # Copy current app (set by docker-compose) into the container
# COPY ./ /app

# Use official FastAPI base image with Gunicorn + Uvicorn
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Switch to root to install packages
USER root

# Install Nginx
RUN apt-get update && apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

# Remove default Nginx config and copy your own
RUN rm /etc/nginx/sites-enabled/default
COPY scripts/nginx/default.conf /etc/nginx/sites-enabled/default

# Set working directory
WORKDIR /app

# Copy application code
COPY ./ /app

# Expose Nginx port
EXPOSE 80

# Start both Nginx and Gunicorn
CMD bash -c "service nginx start && gunicorn --workers 2 --timeout 100 --bind 0.0.0.0:8000 app.main:app"
