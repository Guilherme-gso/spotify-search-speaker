import speech_recognition as sr
import pyttsx3 

from unidecode import unidecode
from spotify import *

recognizer = sr.Recognizer()
microphone = sr.Microphone()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
language = ['pt_BR']

def speak(text: str):
  for voice in voices:
    current_language = voice.languages

    if(current_language == language):
      engine.setProperty('voice', voice.id)

  engine.say(text)
  engine.runAndWait()


with microphone as source:
  recognizer.adjust_for_ambient_noise(source)

  speak('Olá mestre, o que você deseja ouvir?: ')
  audio = recognizer.listen(source)

  try:
    text = recognizer.recognize_google(audio_data=audio, language='pt-BR')
    argumments = unidecode(text.lower()).split()

    type = argumments[1]
    search = ' '.join(argumments[2:])

    speak('Tudo bem, estou iniciando!')

    if type == 'album':
      speak('Iniciando o álbum: ' + search)
      uri = get_album_uri(search)
      play_album(uri)
      
    elif type == 'musica':
      speak('Iniciando a música: ' + search)
      uri = get_track_uri(search)
      play_track(uri)
    else:
      speak('Desculpe, comando não entendido')

  except sr.RequestError:
    speak('Perdão, não consigo te ajudar agora!')
  except sr.UnknownValueError:
    speak('Desculpe, não entendi')

