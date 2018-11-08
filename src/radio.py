from news import newsspeaker, researcher
from music import music
import radio_config

import sys
import time
import smtplib
from os.path import basename
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication

time_string = time.strftime('%Y%m%d_%H')
log_file = "/home/pi/radio/rendered/logs/" + time_string + "_log.txt"
sys.stdout = open(log_file, "w")

weather_text = researcher.getWeather()
print 'Weather: ' + weather_text
newsspeaker.readWithGoogle(weather_text, "weather_forecast")

news_text = researcher.getNews()
#print 'News:' + news_text
newsspeaker.readWithGoogle(news_text, "news")

music.fetchMusic()

sys.stdout.close()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(radio_config.EMAIL_USER, radio_config.EMAIL_PASSWORD)

message = MIMEMultipart()
message['From'] = radio_config.EMAIL_SENDER
message['To'] = radio_config.EMAIL_RECIPIENT
message['Subject'] = "Sparprogramm.fm Log"
body = "Sparprogramm.fm Log"
message.attach(MIMEText(body, 'plain'))

with open(log_file, "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name=basename(log_file)
    )
    # After the file is closed
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(log_file)
message.attach(part)

server.sendmail(radio_config.EMAIL_SENDER, radio_config.EMAIL_RECIPIENT, message.as_string())
