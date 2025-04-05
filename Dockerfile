# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port and run gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
