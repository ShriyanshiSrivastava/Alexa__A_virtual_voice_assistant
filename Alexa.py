import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

alexa_hears= sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

engine.say('Hello,I am Alexa , your virtual assistant. Excited to meet you all')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        talk('Tell me what you want to ask..')
        voice = alexa_hears.listen(source)
        command = alexa_hears.recognize_google(voice)
        command = command.lower()
    if 'alexa' in command:
            command = command.replace('alexa', "")
            print(command)
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'search' in command:
        command = command.replace('search', '')
        search= pywhatkit.search(command)
        print(search)
        talk(search)
    elif 'bye' in command:
        exit
    else:
        talk('Please say the command again.')


while True:
    run_alexa()