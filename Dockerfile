# Use a slim, ARM-compatible Python image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create directories for static and media files
# This ensures Nginx has a target to look for
RUN mkdir -p /app/staticfiles /app/uploads

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose app port
EXPOSE 8000

# Use the entrypoint script to start the container
ENTRYPOINT ["/app/entrypoint.sh"]