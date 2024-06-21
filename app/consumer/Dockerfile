# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the application code
COPY ./app/consumer .

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Command to run the consumer.py script
CMD ["python", "consumer.py"]
