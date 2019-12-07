#!/usr/bin/python3

from flask import request, Flask
from flask_api import FlaskAPI
from flask_httpauth import HTTPBasicAuth
import RPi.GPIO as GPIO
import time
import hashlib

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    print("Password: ",password, "User: ",username)
    if username == "brad":
        h = hashlib.md5(password.encode())
        return h.hexdigest() == "8d673af8e528a362f742a93c43aea153"
    return False
        

bell = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(bell, GPIO.OUT)

app = FlaskAPI(__name__)

@app.route('/', methods=["GET"])
@auth.login_required
def api_root():
    return {
           "bell": request.url + "bell/",
      		 "led_url_POST": {"action": "(ring)"},
                 "user": request.data.get("username") 
    			 }
  
@app.route('/bell/', methods=["GET", "POST"])
@auth.login_required
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
