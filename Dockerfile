# Use a base image with the desired operating system and runtime
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .