from gtts import gTTS
greeting = ("Please make a journal entry")
tts = gTTS(text=greeting, lang='en')
tts.save("alert.mp3")
