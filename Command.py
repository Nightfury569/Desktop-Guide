from gtts import gTTS
import os

text = "Good night"
command = gTTS(text=text,lang='en',slow=False)

command.save("command.mp3")
