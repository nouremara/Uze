from confluent_kafka import Producer


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def kafka_producer(data):
    config = {'bootstrap.servers': 'localhost:9092'}
    producer = Producer(config)
    producer.produce('sensor_topic', key='sensor_data', value=data, callback=delivery_report)
    producer.flush()
