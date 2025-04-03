import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import wikipediaapi
import pyjokes
from wikipedia.exceptions import DisambiguationError, PageError

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty("voices")

# Print available voices
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Set the desired voice
alexa.setProperty("voice", voices[0].id)
alexa.setProperty("rate", 150)
alexa.setProperty("volume", 1)

def talk(Text):
    print("Alexa will say:", Text)
    alexa.say(Text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print("Command Received:", command)
            if "alexa" in command:
                command = command.replace("alexa", "").strip()
                return command
            else:
                print("Wake word not detected.")
                return ""
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        print("Sorry, I am having trouble connecting to the internet.")
        return ""

def run_alexa():
    command = take_command()
    if command:
        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            talk("Current time is " + time)

        elif "play" in command:
            song = command.replace("play", "").strip()
            talk("Playing " + song)
            pywhatkit.playonyt(song)

        elif "tell me about" in command:
            look_for = command.replace("tell me about", "").strip()
            try:
                info = wikipedia.summary(look_for, sentences=1)
                print(info)
                talk(info)
            except DisambiguationError as e:
                print(e.options)
                talk("There are multiple results. Please specify.")
            except PageError:
                talk("Sorry, I couldn't find any information.")

        elif "what is" in command:
            look_for = command.replace("what is", "").strip()
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page = wiki_wiki.page(look_for)
            if page.exists():
                info = page.summary[:300]
                print(info)
                talk(info)
            else:
                talk("Sorry, I couldn't find any information.")

        elif "joke" in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        else:
            talk("Please say the command again.")
    else:
        print("No command detected.")

run_alexa()