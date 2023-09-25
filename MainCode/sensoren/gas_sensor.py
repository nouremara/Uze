#!/usr/bin/env python3
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
from kafka import producer

import math

DO = 24    				# D0 pin og Gas Sensor module. Note this was changed from the schematic Pin17
Buzz = 18  				# SIG pin of Active Buzzer module
AIN = 1    				# AIN1 channel of PCF8591 module 
GPIO.setmode(GPIO.BCM)

def setup():
	ADC.setup(0x48)
	GPIO.setup	(DO, 	GPIO.IN)
	GPIO.setup	(Buzz, 	GPIO.OUT)
	GPIO.output	(Buzz,	1)

def Print(x):
	if x == 1:
		print ('')
		print ('   *********')
		print ('   * Safe~ *')
		print ('   *********')
		print ('')
	if x == 0:
		print ('')
		print ('   ***************')
		print ('   * Danger Gas! *')
		print ('   ***************')
		print ('')

def loop():
	status = 1
	count = 0
	while True:
		sensorValue = ADC.read(AIN)
		tmp = GPIO.input(DO)
		print ('sensor value : ', sensorValue)
		print ('sensor signal: ', tmp)
		
		if tmp == status:
			Print(tmp)
			status = tmp
		if status == 0:
			count += 1
			if count % 2 == 0:
				GPIO.output(Buzz, 1)
			else:
				GPIO.output(Buzz, 0)
		else:
			GPIO.output(Buzz, 1)
			count = 0
				
		time.sleep(0.2)

def destroy():
	GPIO.output(Buzz, 1)
	GPIO.cleanup()

def read_gas_sensor():
    # Simulieren Sie die Gas-Sensor-Daten
    gas_data = "Beispiel-Gas-Daten"
    producer(gas_data)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		destroy()
