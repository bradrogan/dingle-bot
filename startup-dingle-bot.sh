#!/bin/bash

date >> /tmp/dingle-bot-service.out
echo "Starting dingle-bot..." >> /tmp/dingle-bot-service.out 
/usr/bin/python3 /home/pi/apps/dingle-bot/dingle-bot.py >> /tmp/dingle-bot-service.out 2>&1 
