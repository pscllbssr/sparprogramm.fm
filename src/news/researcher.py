import news_config

def getWeather():
    import pyowm
    
    owm = pyowm.OWM(news_config.OWM_API_KEY)
    
    observation = owm.weather_at_place('Bern,CH')
    weather = observation.get_weather()
    
    weather_text = "Die Tempereaturen in Bern bewegen sich heute zwischen " + str(weather.get_temperature('celsius')['temp_min']) + " und " + str(weather.get_temperature('celsius')['temp_max']) + " Grad"
    
    # forecast
    forecaster = owm.three_hours_forecast('Bern,CH')
    forecast = forecaster.get_forecast()
    for weather in forecast:
        print (weather.get_reference_time('iso') + ": " + str(weather.get_temperature('celsius')['temp']))
    
    #print(weather_text)
    return (weather_text) 