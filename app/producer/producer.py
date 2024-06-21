import os
import requests
from kafka import KafkaProducer
import json
import time

# API URL ve Parametreler
api_url = "https://newsapi.org/v2/everything"
api_key = os.getenv('NEWS_API_KEY', 'your_default_api_key_here')  # Replace 'your_default_api_key_here' with a default or remove it

params = {
    "q": "*",
    "apiKey": api_key
}

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
topic = 'news-data'

def fetch_data_from_api():
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API Error: {response.status_code}")
        return None

def produce_to_kafka(data):
    for article in data.get('articles', []):
        producer.send(topic, value=article)
    producer.flush()

while True:
    data = fetch_data_from_api()
    if data:
        print(data)
        produce_to_kafka(data)
    time.sleep(10)
