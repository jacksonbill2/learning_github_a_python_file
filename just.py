import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',90)
engine.setProperty('volumn',50)
TextToSpeak=' deep concept of data structure'
engine.say(TextToSpeak)
engine.runAndWait()
