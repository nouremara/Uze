from kafka import consumer
from sensoren.gas_sensor import read_gas_sensor
import threading

if __name__ == "__main__":
    producer_thread = threading.Thread(target=read_gas_sensor)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()