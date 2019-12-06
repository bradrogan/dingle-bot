#!/usr/bin/python3

from flask import request
from flask_api import FlaskAPI
import RPi.GPIO as GPIO
import time

bell = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(bell, GPIO.OUT)

app = FlaskAPI(__name__)

@app.route('/', methods=["GET"])
def api_root():
    return {
           "bell": request.url + "bell/",
      		 "led_url_POST": {"action": "(ring)"}
    			 }
  
@app.route('/bell/', methods=["GET", "POST"])
def api_leds_control():
    if request.method == "POST":
        if request.data.get("action") == "ring":
            GPIO.output(bell, 1)
            time.sleep(0.2)
            GPIO.output(bell, 0)
            time.sleep(0.5)
            GPIO.output(bell, 1)
            time.sleep(0.2)
            GPIO.output(bell, 0)
    return "test" 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    GPIO.cleanup()
