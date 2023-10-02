import psycopg2
import json


def insert_into_db(data):
    try:
        connection = psycopg2.connect(host='localhost', port=5432, user='nour', password='123', dbname='Streetsense')
        cursor = connection.cursor()

        # Assuming data comes as a JSON object
        sensor_data = json.loads(data)

        cursor.execute("""
            INSERT INTO sensor_data (gas_sensor, humiture_sensor, lidar_sensor, sound_sensor) 
            VALUES (%s, %s, %s, %s)
        """, (sensor_data['gas'], sensor_data['humiture'], sensor_data['lidar'], sensor_data['sound']))

        connection.commit()
    except Exception as error:
        print(f"Database error: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()