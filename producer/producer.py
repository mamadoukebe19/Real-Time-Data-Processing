from kafka import KafkaProducer
import time
import random
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        'sensor_id': random.randint(1, 100),
        'temperature': random.uniform(20.0, 30.0)
    }
    producer.send('sensor_data', data)
    print(f'Sent: {data}')
    time.sleep(2)

