# Use the official Python image as the base image
FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    mariadb-client \
    build-essential \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Django project files from the src directory to the container
COPY src/ .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=settings.production



# Define build arguments
ARG DB_NAME
ARG DB_USER
ARG DB_PASS
ARG DB_HOST

# Set environment variables using the build arguments
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PASS=$DB_PASS
ENV DB_HOST=$DB_HOST

# Expose the port the app runs on
EXPOSE 8000

RUN python manage.py migrate --settings=settings.development

# Use gunicorn to run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "propfeed.wsgi:application"]