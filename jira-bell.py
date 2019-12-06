#!/usr/bin/sudo /usr/bin/python

import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)

time.sleep(1)

GPIO.output(pin, GPIO.HIGH)

time.sleep(1)

GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()
