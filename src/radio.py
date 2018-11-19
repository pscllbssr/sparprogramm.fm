# -*- coding: utf-8 -*-
from news import newsspeaker, researcher
from music import music
import radio_config
import facility_manager

import sys
import time

time_string = time.strftime('%Y%m%d_%H')
log_file = "/home/pi/radio/rendered/logs/" + time_string + "_log.txt"
sys.stdout = open(log_file, "w")

weather_text = researcher.getWeather()
print('Weather: ' + weather_text)
newsspeaker.readWithGoogle(weather_text, "weather_forecast")

news_text = researcher.getNewsMix()
#print('News:' + news_text)
newsspeaker.readWithGoogle(news_text, "news")

#music.fetchMusic()

sys.stdout.close()

facility_manager.sendReport(log_file)