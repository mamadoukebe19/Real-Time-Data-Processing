from kafka import KafkaConsumer
import psycopg2
import json

# Set up the Kafka consumer to listen to the 'sensor_data' topic
consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda v: json.loads(v)
)

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="user",
    password="password",
    host="db"
)

cur = conn.cursor()

# Create the table for storing sensor data if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
    sensor_id INT,
    temperature FLOAT
);''')
conn.commit()

# Process messages from the Kafka topic
for message in consumer:
    data = message.value
    cur.execute(
        "INSERT INTO sensor_data (sensor_id, temperature) VALUES (%s, %s)",
        (data['sensor_id'], data['temperature'])
    )
    conn.commit()
    print(f"Inserted: {data}")

