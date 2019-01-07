#!/home/pi/.opam/system/bin/liquidsoap

# Stand: Alle Stunden wird das File in News Abgespielt, danach kommt musik abwechselnd mit jingles
# scheinbar können mp3/wav/ogg files von marytts nicht abgespielt werden. Falsch kodiert?
# Todo: Transitions vor News, autotisches reloaden der playlist

# Log dir
set("log.file.path","/tmp/basic-radio.log")

# Log to console
set("log.stdout", true)

# Music
# Playlist könnte  auch von einer Datei im Netz stammen:
# playlist(reload=600,"http://my/playlist.txt")
myplaylist = playlist(reload=60, "~/radio/rendered/music")

# Some jingles
jingles = playlist("~/radio/rendered/jingles")

# news
#news = single("~/radio/rendered/news/news.mp3")
news = audio_to_stereo(single("~/radio/rendered/news/news.mp3"))
weather = audio_to_stereo(single("~/radio/rendered/news/weather_forecast.mp3"))
die_cheese = audio_to_stereo(single("~/radio/rendered/news/most_popular_cheese.mp3"))

# If something goes wrong, we'll play this
security = mksafe(single("~/radio/rendered/fallback/radio-fallback-no-music.mp3"))

# Start building the feed with music
radio = myplaylist
infos = rotate(weights = [1,1,1], [jingles, weather, die_cheese])

# Now add some jingles
radio = rotate(weights = [1,1],[radio, infos])

# Add news every hour
# Try another: https://www.liquidsoap.info/doc-dev/cookbook.html (zweites fenster unter switch-based transitions)
radio = fallback(track_sensitive = false, [switch([ ( {00m0s} , news) ]), radio ])
# radio = add([radio,switch([({00m0s},news)])])

# And finally the security
radio = fallback(track_sensitive = false, [radio, security])


# Stream it out
output.icecast(%vorbis,
  host = "localhost", port = 8000,
  password = "fIvYfwcbA6QqCdyl8XPv", mount = "sparprogramm-fm.ogg",
  name = "Sparprogramm.fm",description = "Das automatische Radio",
  radio)
output.icecast(%mp3(bitrate=128),
  host = "localhost", port = 8000,
  password = "fIvYfwcbA6QqCdyl8XPv", mount = "sparprogramm-fm.mp3",
  name = "Sparprogramm.fm",description = "Das automatische Radio",
  radio)
