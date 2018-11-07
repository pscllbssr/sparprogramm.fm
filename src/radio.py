from news import newsspeaker, researcher

# Input text
weather_text = researcher.getWeather()
newsspeaker.readNews(weather_text, "weather_forecast")

#news_text = researcher.News()
newsspeaker.readNews(weather_text, "news")

