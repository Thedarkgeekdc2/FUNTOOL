import os
from gtts import gTTS
os.system("espeak 'please wait, we are working on it. fuck you RAAZ,BABU'")
os.system("mplayer term.mp3 > /dev/null 2>&1")
os.system("clear")
os.system("bash banner | lolcat")
mytext= input('Enter your text : ')

language = 'en'

myobj = gTTS(text=mytext, lang= language, slow=False)

myobj.save("temp.mp3")

os.system("mplayer temp.mp3 > /dev/null 2>&1")
