#!/bin/bash

date >> /tmp/dingle-bot-service-ngrok.out
echo "Starting ngrok...." >> /tmp/dingle-bot-service-ngrok.out 
/home/pi/apps/ngrok http --subdomain=dinglebot 5000 >> /tmp/dingle-bot-service-ngrok.out 2>&1 
