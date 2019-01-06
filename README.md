# sparpaket.fm
Sparpaket.fm is an autonomous radio station. A set of python scripts collects and processes data from the web, such as news, weather forecasts and music. It later stores it as audio-files which will be played by the radio station based on Liquidsoap. It was produced by Pascal Albisser and Alex Kälin at the HTW Chur and currently runs on a Raspberry Pi 3 Model B+.

## Setup
There are some dependencies. To start, install..
- Icecast
- Liquidsoap

Later on you should sign in to a Google Cloud Account for the text-to-speach functions to run. Alternatively you could install a MaryTTS-Server locally ([Instructions](https://github.com/marytts/marytts/wiki/Local-MaryTTS-Server-Installation)). 

Make sure the file is executabele and start the radio station with
```
$ ./radio.liq
```
Once started you may listen to your station stream at the configured icecast port which is `:8000` per default.
