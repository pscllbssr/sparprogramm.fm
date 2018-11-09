# -*- coding: utf-8 -*-
import news_config

def getWeather():
    import pyowm
    
    owm = pyowm.OWM(news_config.OWM_API_KEY)
    
    observation = owm.weather_at_place('Bern,CH')
    weather = observation.get_weather()
    
    weather_text = "Die Temperaturen in Bern bewegen sich heute zwischen " + str(weather.get_temperature('celsius')['temp_min']) + " und " + str(weather.get_temperature('celsius')['temp_max']) + " Grad"
    
    # forecast to use later
    forecaster = owm.three_hours_forecast('Bern,CH')
    forecast = forecaster.get_forecast()
    for weather in forecast:
        print (weather.get_reference_time('iso') + ": " + str(weather.get_temperature('celsius')['temp']))
    
    #print(weather_text)
    return (weather_text)

def getNews():
    
    import json    
    import requests
    import time
    
    news = ''
    hour = time.localtime().tm_hour + 1
    news += "Es ist " + str(hour) +" Uhr, willkommen zu den News auf Sparprogramm.fm - Sparprogramm statt Radioprogramm "

    resp = requests.get('https://api.presseportal.ch/api/article/all?&format=json&lang=de&teaser=1&limit=3&api_key=' + news_config.PRESSEPORTAL_API_KEY)
    if resp.status_code != 200:
        # This means something went wrong.
        print('Keine News verfügbar (API-Error)')
    response = resp.json()
    
    for story in response['content']['story']:        
        news += story['teaser']
        
    return news

def getLatestTweets():
    return 'here we are'

def _getNewsIntro():
    news = ''
    hour = time.localtime().tm_hour + 1
    news += "Es ist " + str(hour) +" Uhr, willkommen zu den News auf Sparprogramm.fm - Sparprogramm statt Radioprogramm "
    return news

def getAlternativeFacts():
    import feedparser
    
    news_text = _getNewsIntro()
    news_feed = feedparser.parse("https://www.srf.ch/news/bnf/rss/1890")
    
    for i in '123':
        entry = news_feed.entries[i]
        news_text += entry['title'] + entry['description']
        
    return news_text
    
