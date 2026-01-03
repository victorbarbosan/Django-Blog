#!/bin/sh

# Fail immediately if a command fails
set -e

echo ">>> Collecting static files..."
python manage.py collectstatic --noinput

echo ">>> Applying database migrations..."
python manage.py migrate --noinput

echo ">>> Starting Gunicorn..."
# Replace 'my_site' with your actual project folder name if different
exec gunicorn my_site.wsgi:application --bind 0.0.0.0:8000