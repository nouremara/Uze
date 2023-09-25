from confluent_kafka import Consumer, KafkaError
from postgres_connector import insert_into_db


def kafka_consumer():
    config = {'bootstrap.servers': 'localhost:9092', 'group.id': 'sensor_group', 'auto.offset.reset': 'earliest'}
    consumer = Consumer(config)
    consumer.subscribe(['sensor_topic'])

    while True:
        msg = consumer.poll(1)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        sensor_data = msg.value().decode('utf-8')
        insert_into_db(sensor_data)

    consumer.close()
