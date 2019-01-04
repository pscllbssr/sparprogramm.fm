from news import newsspeaker, researcher
from music import music
from boulevard import diecheese
import radio_config
import facility_manager

import sys
import time

time_string = time.strftime('%Y%m%d_%H')
log_file = "/home/pi/radio/logs/" + time_string + "_log.txt"
sys.stdout = open(log_file, "w")

# make weather forecast
weather_text = researcher.getWeather()
#print('Weather: ' + weather_text)
newsspeaker.readWithGoogle(weather_text, "weather_forecast")

# produce news
news_text = researcher.getNewsMix()
#print('News:' + news_text)
newsspeaker.readWithGoogle(news_text, "news")

# get music files from server
music.fetchMusic()

# Most popular diecheese article
article_text = diecheese.getMostPopularArticle()
newsspeaker.readWithGoogle(article_text, "most_popular_cheese")

sys.stdout.close()

facility_manager.sendReport(log_file)