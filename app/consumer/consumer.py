from kafka import KafkaConsumer
import json
import logging
import mysql.connector
from datetime import datetime

try:
    consumer = KafkaConsumer(
        'news-data',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='latest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # MySQL bağlantısı oluştur
    mysql_connection = mysql.connector.connect(
        host='mysql',
        database='kafka',
        user='kafka',
        password='kafka'
    )
    mysql_cursor = mysql_connection.cursor()

    for message in consumer:
        data = message.value
        print("Received data:", data)

        source_id = data['source']['id']
        source_name = data['source']['name']
        author = data['author']
        title = data['title']
        description = data['description']
        url = data['url']
        urlToImage = data['urlToImage']
        publishedAt = datetime.strptime(data['publishedAt'], '%Y-%m-%dT%H:%M:%SZ') 
        content = data['content']

        insert_query = "INSERT INTO news_data (source_id, source_name, author, title, description, url, urlToImage, publishedAt, content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        record_to_insert = (source_id, source_name, author, title,
                            description, url, urlToImage, publishedAt, content)
        mysql_cursor.execute(insert_query, record_to_insert)
        mysql_connection.commit()

except Exception as e:
    print("Error:", e)

finally:
    if 'consumer' in locals():
        consumer.close()
    if 'mysql_connection' in locals():
        mysql_connection.close()
