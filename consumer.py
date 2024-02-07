from confluent_kafka import Consumer, KafkaError
from datetime import datetime

# Kafka consumer configuration
conf = {
 'bootstrap.servers': 'localhost:9092', # Replace with your Kafka broker address
 'group.id': 'my-group',
 'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to a Kafka topic
topic = 'conn-events' # Replace with your topic name
consumer.subscribe([topic])

while True:

    msg = consumer.poll()
 
    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error: {msg.error()}')

    else:
        print(f'received {msg.value().decode("utf-8")}')
        data_price = [(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg.value().decode("utf-8"))]
