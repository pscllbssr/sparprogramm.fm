#!/bin/bash
timestamp=$( date '+%F %T' )
echo "$timestamp ausgeführt" >>/home/pi/radio/logs/archiver.txt
python /home/pi/radio/src/archiver.py -u >>/home/pi/radio/logs/archiver.txt
