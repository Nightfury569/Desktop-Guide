import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()

#wav = sr.AudioFile('Recording (3).wav')
#with wav as source:

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening..")
    r.energy_threshold = 400
    audio = r.listen(source)
    try:
          text = r.recognize_google(audio)
          print('you said ='+ text)
    except Exception as e :
          print("Sorry could not recognize")


engine = pyttsx3.init()

engine.say("ttyyy")
engine.runAndWait()


