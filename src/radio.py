from news import newsspeaker, researcher
from music import music

weather_text = researcher.getWeather()
print(weather_text)
#newsspeaker.readWithMary(weather_text, "weather_forecast")

news_text = researcher.getNews()
print(news_text)
#newsspeaker.readWithMary(news_text, "news")

music.fetchMusic()



