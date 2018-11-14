# -*- coding: utf-8 -*-
import news_config

def getWeather():
    import pyowm
    
    owm = pyowm.OWM(news_config.OWM_API_KEY)
    
    observation_berne = owm.weather_at_place('Bern,CH')
    observation_zurich = owm.weather_at_place('Zurich,CH')
    observation_chur = owm.weather_at_place('Chur,CH')

    weather_berne = observation_berne.get_weather().get_temperature('celsius')
    weather_zurich = observation_zurich.get_weather().get_temperature('celsius')
    weather_chur = observation_chur.get_weather().get_temperature('celsius')
    
    weather_text = news_config.WEATHER_TEXT.format(
        weather_berne['temp_min'], 
        weather_berne['temp_max'], 
        weather_chur['temp_min'], 
        weather_chur['temp_max'], 
        weather_zurich['temp_min'],
        weather_zurich['temp_max'])     


    # forecast to use later
    forecaster = owm.three_hours_forecast('Bern,CH')
    forecast = forecaster.get_forecast()
    for weather in forecast:
        w = weather
        #print (weather.get_reference_time('iso') + ": " + str(weather.get_temperature('celsius')['temp']))
    
    #print(weather_text)
    return weather_text

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
    
    import time
    
    news = ''
    hour = time.localtime().tm_hour + 1
    news += "Es ist " + str(hour) +" Uhr, willkommen zu den News auf Sparprogramm.fm - Sparprogramm statt Radioprogramm \n"
    return news

def getAlternativeFacts():
    import feedparser
    
    news_text = _getNewsIntro()
    news_feed = feedparser.parse("https://www.srf.ch/news/bnf/rss/1890")
    
    for i in '123':
        entry = news_feed.entries[int(i)]
        news_text += entry['title'] + " \n" + entry['description'] + "\n\n"
        
    return news_text
    
