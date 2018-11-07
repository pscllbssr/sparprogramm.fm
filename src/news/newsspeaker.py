# -*- coding: utf-8 -*-

# HTTP + URL packages
import httplib2
import urllib # For URL creation

# Mary server informations
tts_host = "mary.dfki.de"
tts_port = "59125"

tts_audio_location = "/home/pi/radio/rendered/news/"

def readWithMary(text, filename):

    # Build the query
    query_hash = {"INPUT_TEXT":text,
                  "INPUT_TYPE":"TEXT", # Input text
                  "LOCALE":"de",
                  "VOICE":"bits3-hsmm", # Voice informations  (need to be compatible)
                  "OUTPUT_TYPE":"AUDIO",
                  "AUDIO":"WAVE", # Audio informations (need both)
                  }
    query = urllib.urlencode(query_hash)
    print("query = \"http://%s:%s/process?%s\"" % (tts_host, tts_port, query))

    # Run the query to mary http server
    h_mary = httplib2.Http()
    resp, content = h_mary.request("http://%s:%s/process?" % (tts_host, tts_port), "POST", query)

    #  Decode the wav file or raise an exception if no wav files
    if (resp["content-type"] == "audio/x-wav"):

        # Write the wav file
        f = open(tts_audio_location + filename + ".wav", "wb")
        f.write(content)
        f.close()

    else:
        raise Exception(content)
