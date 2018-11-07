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
news = single("~/radio/rendered/news/100sec.mp3")

# If something goes wrong, we'll play this
security = mksafe(single("~/radio/rendered/fallback/radio-fallback-no-music.mp3"))

# Start building the feed with music
radio = myplaylist

# Now add some jingles
radio = random(weights = [1, 2],[jingles, radio])

# Add news every hour
radio = fallback(track_sensitive = false, [switch([ ( {22m0s} , news) ]), radio ])

# And finally the security
radio = fallback(track_sensitive = false, [radio, security])


# Stream it out
output.icecast(%vorbis,
  host = "localhost", port = 8000,
  password = "fIvYfwcbA6QqCdyl8XPv", mount = "guerilla-radio.ogg",
  name = "Guerilla Radio",description = "Das Radio ohne Journalisten",
  radio)
output.icecast(%mp3(bitrate=128),
  host = "localhost", port = 8000,
  password = "fIvYfwcbA6QqCdyl8XPv", mount = "guerilla-radio.mp3",
  name = "Guerilla Radio",description = "Das Radio ohne Journalisten",
  radio)
