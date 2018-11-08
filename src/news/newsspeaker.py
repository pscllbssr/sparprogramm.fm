# -*- coding: utf-8 -*-

# HTTP + URL packages
# import httplib2
# import urllib # For URL creation

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
    
def readWithGoogle(text, filename):

    from google.cloud import texttospeech

    '''
    Google Cloud Path Variable must be set, according to
    https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries#before-you-begin
    '''
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='de-DE',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    
    full_filename = tts_audio_location + filename + '.mp3'
    
    # The response's audio_content is binary.
    with open(full_filename, 'wb') as out:
    # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file ' + full_filename)
    
