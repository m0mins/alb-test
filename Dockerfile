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

RUN apt-get update && apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

RUN rm /etc/nginx/nginx.conf
COPY scripts/nginx/default.conf /etc/nginx/nginx.conf
# COPY scripts/nginx/default.conf /etc/nginx/conf.d/default.conf
# Set working directory
WORKDIR /app

# Copy application code
COPY ./ /app

# Expose Nginx port
EXPOSE 80

CMD sh -c "uvicorn main:app --host 0.0.0.0 --port $PORT & nginx -g 'daemon off;'"
