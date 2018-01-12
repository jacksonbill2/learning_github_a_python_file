import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',90)
engine.setProperty('volumn',50)
TextToSpeak=' deep concept of data structure ,machine learning and artificial intell. using python'
engine.say(TextToSpeak)
engine.runAndWait()
