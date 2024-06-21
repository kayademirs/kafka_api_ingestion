# Kafka API to MySQL Project

This project demonstrates how to read data from an API using Kafka and write it to a MySQL database. We will create a Kafka producer to fetch data from the NewsAPI and a Kafka consumer to process and store the data in a MySQL database. The entire setup will be Dockerized for easy deployment and management.

## Prerequisites

- Docker
- Docker Compose
- API Token from [NewsAPI](https://newsapi.org/docs/get-started)

## Setup

### 1. Create API Token

First, sign up at [NewsAPI](https://newsapi.org/docs/get-started) to get your API token.

To test the token, you can use the following URL by replacing `YOUR_TOKEN`:
<https://newsapi.org/v2/everything?q=*&apiKey=YOUR_TOKEN>

### 2. Project Structure

```
git clone [...](https://github.com/kayademirs/kafka_api_ingestion.git)
cd kafka_api_ingestion
```

Here's the directory structure of the project:

```bash
kafka_api_ingestion
├── app
│   ├── consumer
│   │   ├── consumer.py
│   │   └── Dockerfile
│   ├── producer
│   │   ├── producer.py
│   │   └── Dockerfile
│   └── requirements.txt
├── docker-compose.yaml
├── etc
│   └── config
│       └── server.properties
└── README.md
```

### 4. Create the MySQL Table

Connect to the MySQL container and create the `news_data` table:

1. Connect to the MySQL container:

   ```bash
   docker exec -it mysql bash
   ```

2. Start the MySQL client and login as root (password: `kafka`):

   ```bash
   mysql -u root -p
   ```

3. Select the database (default is `kafka`):

   ```sql
   use kafka;
   ```

4. Create the `news_data` table:

   ```sql
   CREATE TABLE news_data (
       id INT AUTO_INCREMENT PRIMARY KEY,
       source_id VARCHAR(255),
       source_name VARCHAR(255),
       author VARCHAR(255),
       title TEXT,
       description TEXT,
       url TEXT,
       urlToImage TEXT,
       publishedAt DATETIME,
       content TEXT
   );
   ```

5. Exit:

   ```sql
   exit;
   ```

6. Exit the MySQL container:

   ```bash
   exit
   ```

### 5. Build and Run

1. **Set your NewsAPI token:**

    Add your token to the producer service in the docker-compose file.

2. **Build and start the containers:**

    ```bash
    docker-compose up -d --build
    ```

### 6. Verify MySQL Database

Connect to the MySQL container and verify the data:

```bash
docker exec -it mysql bash
mysql -u root -p
# Enter password: kafka
use kafka;
select * from news_data;
```

## Conclusion

This setup fetches news articles from NewsAPI using a Kafka producer, processes the data through a Kafka consumer, and stores it in a MySQL database. The entire setup is Dockerized for ease of deployment and management.
