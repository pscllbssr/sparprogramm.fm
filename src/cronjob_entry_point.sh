#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/radio/src/news/google_config.json" 
timestamp=$( date '+%F %T' )
echo "$timestamp ausgeführt" >>/home/pi/radio/logs/cron.txt
python /home/pi/radio/src/radio.py >>/home/pi/radio/logs/cron.txt