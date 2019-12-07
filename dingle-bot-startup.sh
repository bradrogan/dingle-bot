#!/bin/bash

echo "Starting ngrok...." > /tmp/dingle-bot-service-ngrok.out 
/home/pi/apps/ngrok http --subdomain=dinglebot 5000 >> /tmp/dingle-bot-service-ngrok.out 2>&1 &

echo "Starting dingle-bot..." > /tmp/dingle-bot-service.out 
/usr/bin/python3 /home/pi/apps/dingle-bot/dingle-bot.py >> /tmp/dingle-bot-service.out 2>&1 &
