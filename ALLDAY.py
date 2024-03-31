import datetime     #for using current date and time 
import pyttsx3      #for speaking text
import shutil       #for os control
import speech_recognition as sr     #converting audio into text
# import pyaudio      #for listening audio form microphone in rel time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print("Good Morning Sir !")
        speak("Good Morning Sir !")
    elif hour>= 12 and hour<18:
        print("Good Afternoon Sir !") 
        speak("Good Afternoon Sir !") 
  
    else:
        print("Good Evening Sir !")
        speak("Good Evening Sir !") 
  
    assname =("ALLDAY")
    print("I am your Assistant")
    speak("I am your Assistant")
    print(assname, " 1.0")
    speak(assname)
     
 
def username():
    speak("What should i call you sir")
    uname = takeCommand()
    print("Welcome Mister")
    speak("Welcome Mister")
    print(uname)
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("                     ".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("                     ".center(columns))
     
    speak("How can i Help you, Sir")
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query