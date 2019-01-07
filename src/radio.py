from news import newsspeaker, researcher
from music import music
import radio_config
import facility_manager

import sys
import time

time_string = time.strftime('%Y%m%d_%H')
log_file = "/home/pi/radio/logs/" + time_string + "_log.txt"
sys.stdout = open(log_file, "w")

# make weather forecast
try: 
    weather_text = researcher.getWeather()
    #print('Weather: ' + weather_text)
    newsspeaker.readWithGoogle(weather_text, "weather_forecast")
except SyntaxError as e:
    print 'Failed to prepare weather weather forecast'
    print e
except Exception, e:
    print 'Failed to prepare weather forecast:'
    print e

# produce news
try: 
    news_text = researcher.getNewsMix()
    #print('News:' + news_text)
    newsspeaker.readWithGoogle(news_text, "news")
except SyntaxError as e:
    print 'Failed to prepare news'
    print error
except Exception, e:
    print 'Failed to prepare news:'
    print e   

# get music files from server
music.fetchMusic()

# Most popular diecheese article
try:
    from boulevard import diecheese
    article_text = diecheese.getMostPopularArticle()
    newsspeaker.readWithGoogle(article_text, "most_popular_cheese")
except SyntaxError as e:
    print 'Failed to prepare digezz-shizzle:'
    print e
except Exception, e:
    print 'Failed to prepare weather digezz-shizzle:'
    print e

sys.stdout.close()

facility_manager.sendReport(log_file)