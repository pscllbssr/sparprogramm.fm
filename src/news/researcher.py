# -*- coding: utf-8 -*-
import news_config
import datetime
import pytz

def getWeather():
    import pyowm
    
    owm = pyowm.OWM(news_config.OWM_API_KEY)
    
    observation_berne = owm.weather_at_place('Bern,CH')
    observation_zurich = owm.weather_at_place('Zurich,CH')
    observation_chur = owm.weather_at_place('Chur,CH')

    weather_berne = observation_berne.get_weather().get_temperature('celsius')
    weather_zurich = observation_zurich.get_weather().get_temperature('celsius')
    weather_chur = observation_chur.get_weather().get_temperature('celsius')

    # forecast to use later
    forecaster_berne = owm.three_hours_forecast('Bern,CH')
    forecast_berne = forecaster_berne.get_forecast()
    
    forecaster_chur = owm.three_hours_forecast('Chur,CH')
    forecast_chur = forecaster_chur.get_forecast()
    
    forecaster_zurich = owm.three_hours_forecast('Zurich,CH')
    forecast_zurich = forecaster_zurich.get_forecast()
   
    # desired forecast datetime (tomorrow 12:00)   
    utc = pytz.UTC
    desired_date = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=12)) + datetime.timedelta(days=1)
    desired_date= utc.localize(desired_date)
    
    for weather in forecast_berne:
        if weather.get_reference_time('date') == desired_date:
            berne_forecast_status = weather.get_status()
            berne_forecast_temp = weather.get_temperature(unit='celsius')['temp']
            
    for weather in forecast_chur:
        if weather.get_reference_time('date') == desired_date:
            chur_forecast_status = weather.get_status()
            chur_forecast_temp = weather.get_temperature(unit='celsius')['temp']
            
    for weather in forecast_zurich:
        if weather.get_reference_time('date') == desired_date:
            zurich_forecast_status = weather.get_status()
            zurich_forecast_temp = weather.get_temperature(unit='celsius')['temp']
            
    weather_text = news_config.WEATHER_TEXT.format(
        int(weather_berne['temp_min']), 
        int(weather_berne['temp_max']), 
        int(weather_chur['temp_min']), 
        int(weather_chur['temp_max']), 
        int(weather_zurich['temp_min']),
        int(weather_zurich['temp_max']),
        berne_forecast_status,
        int(berne_forecast_temp),
        chur_forecast_status,
        int(chur_forecast_temp),
        zurich_forecast_status,
        int(zurich_forecast_temp)) 
    
    for key, value in news_config.WEATHER_TRANSLATIONS.items():
        weather_text = weather_text.replace(key, value)
   
    #print(weather_text)
    return weather_text

def getNews():
    
    import json    
    import requests
    import time
    
    news = ''
    hour = time.localtime().tm_hour + 1
    #news += "Es ist " + str(hour) +" Uhr, willkommen zu den News auf Sparprogramm.fm"
    news += "Du hörst Sparprogramm.fm und es ist Zeit für die Nachrichten."

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
    #hour = time.localtime().tm_hour + 1
    #news += "Es ist " + str(hour) +" Uhr, willkommen zu den News auf Sparprogramm.fm \n"
    news += "Du hörst Sparprogramm.fm und es ist Zeit für die Nachrichten."
    
    return news

def getAlternativeFacts():
    import feedparser
    
    news_text = _getNewsIntro()
    news_feed = feedparser.parse("https://www.srf.ch/news/bnf/rss/1890")
    
    for i in '123':
        entry = news_feed.entries[int(i)]
        news_text += entry['title'] + " \n" + entry['description'] + "\n\n"
        
    return news_text

def getNewsMix():
    
    import scraper
    
    news_text = ""
    news_text = news_text + _getNewsIntro()
    
    news_text = news_text + scraper.scrapeTXT(news_config.NEWS_SOURCE_1, 2)
    news_text = news_text + scraper.scrapeTXT(news_config.NEWS_SOURCE_2, 1)
    news_text = news_text + scraper.scrapeTXT(news_config.NEWS_SOURCE_3, 1)
    
    news_text = news_text + news_config.NEWS_OUTRO
    
    return news_text

    
