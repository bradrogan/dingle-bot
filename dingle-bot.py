#!/usr/bin/python3

from flask import request, Flask
from flask_api import FlaskAPI
import RPi.GPIO as GPIO
import time
import hashlib
import atexit

HASH = "Insert your own hash here - see README"
        

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
  
@app.route('/bell/<key>', methods=["POST"])
def api_leds_control(key):
    if check_pass(key):
        if request.method == "POST":
            GPIO.output(bell, 1)
            time.sleep(0.04)
            GPIO.output(bell, 0)
            time.sleep(0.2)
            GPIO.output(bell, 1)
            time.sleep(0.04)
            GPIO.output(bell, 0)
        else:
            return {"error": "Only POST supported"}
    else:
        return {"error": "Not Authorized" }
    return {"status": "success" }

def cleanup():
    print("Running GPIO.cleanuop()")
    GPIO.cleanup()

if __name__ == "__main__":
    atexit.register(cleanup)
    app.run(host='0.0.0.0')
    GPIO.cleanup()


