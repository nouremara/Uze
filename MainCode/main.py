

#main einmal ausklammern und vergessen fürs erste

from MainCode.street_sense_client.kafka_interface import consumer
from MainCode.street_sense_client.sensors.GasSensor import read_gas_sensor
import threading

if __name__ == "__main__":
    producer_thread = threading.Thread(target=read_gas_sensor)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
