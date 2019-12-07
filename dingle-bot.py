#!/usr/bin/python3

from flask import request, Flask
from flask_api import FlaskAPI
import RPi.GPIO as GPIO
import time
import hashlib
import atexit

HASH = "93e62131edd94907ce1aa0da0a2a5b96"
        

bell = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(bell, GPIO.OUT)

app = FlaskAPI(__name__)

def check_pass(key):
    if hashlib.md5(key.encode()).hexdigest() == HASH:
        return True
    return False


@app.route('/<key>', methods=["GET"])
def api_root(key):
    if check_pass(key):
        return {
           "bell": request.url + "bell/<key>",
    			 }
    return {"error": "Not Authorized" }
  
@app.route('/bell/<key>', methods=["GET", "POST"])
def api_leds_control(key):
    if check_pass(key):
        if request.method == "POST":
            GPIO.output(bell, 1)
            time.sleep(0.2)
            GPIO.output(bell, 0)
            time.sleep(0.5)
            GPIO.output(bell, 1)
            time.sleep(0.2)
            GPIO.output(bell, 0)
        return {"error": "Only POST supported"}
    return {"error": "Not Authorized" }

def cleanup():
    print("Running GPIO.cleanuop()")
    GPIO.cleanup()

if __name__ == "__main__":
    atexit.register(cleanup)
    app.run(host='0.0.0.0')
    GPIO.cleanup()


