#!/bin/bash

/home/pi/apps/ngrok http --subdomain=dinglebot 5000 > /dev/null &

/usr/bin/python3 /home/pi/apps/dingle-bot/dingle-bot.py > /dev/null &
