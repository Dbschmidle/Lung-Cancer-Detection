# Use official lightweight Python image
FROM python:3.10-slim

WORKDIR /Lung-Cancer-Detection

# Install system dependencies (Pillow needs these)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py .
COPY model_downloader/ ./model_downloader/

# Run with Gunicorn for production
CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "5000", "app:app"]
