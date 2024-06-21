# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the application code
COPY ./app/producer .

# Copy and install the dependencies
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Command to run the producer.py script
CMD ["python", "producer.py"]



