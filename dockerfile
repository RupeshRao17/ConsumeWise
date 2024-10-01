# Use the official Python image as the base
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libzbar0 && apt-get clean

# Set the working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Command to run your application
CMD ["python", "main.py"]
