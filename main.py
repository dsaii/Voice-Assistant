
import time
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import sys
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate', 180)

def speak(audio):       # this func simply converts text to audio
    engine.say(audio)
    engine.runAndWait() 

def wish_me():          # according to time of the day it will give diff greetings
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        a = "Morning"

    elif hour>=12 and hour<18:
        a = "Afternoon"

    else:
        a = "Evening"

    print(f"Good {a} Sir, how may I assist you...!")
    speak(f"Good {a} Sir, how may I assist you...!")

def take_command():   # this is the heart of our program it handles the mic input and recognization of the speech

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 5000
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except: 
        print("Say that again please...")  
        return "None"
    return query


def task_execution():     # it recognize what is the intent of the command
    
    while True:
  
        query = take_command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            try:
                query = query.replace("wikipedia","")
                print(f"{query.upper()} : ")
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                speak("If you want more details, let me know")

                while True:
                    more_details = take_command()
                    if "more details" in more_details:
                        results = wikipedia.summary(query, sentences=3)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                        
                    elif "thank you" in more_details:
                        speak("What's your next command !")
                        break

            except:
                print("I'm sorry Sir, I cannot connect to the Wikipedia server right now, can I do anything else for you...!")
                speak("I'm sorry Sir, I cannot connect to the Wikipedia server right now, can I do anything else for you...!")    

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')

        elif 'open stack overflow' in query:
            webbrowser.open('https://stackoverflow.com/')   

        elif 'the time' in query:
            tm = time.strftime("%I:%M %p")
            print(tm)  
            speak(f"Sir, the time is {tm}")
            
        elif 'play music' in query:
            speak('Okay, here is your music! Enjoy!')
            playsound("path to song")                         #  ------ for windows 
         #  subprocess.call(["afplay", "Path to song"])       #  ------ for mac users
          
        elif 'take me to our college erp' in query:
            webbrowser.open('https://engg.dpuerp.in/Login.aspx')

        elif 'what is our college name' in query:
            speak("Our college name is :")
            print("Dr. D. Y. Patil Institute of Technology Pimpri Pune")
            speak("Dr. D. Y. Patil Institute of Technology Pimpri Pune")

        elif 'wake up' in query :
            speak("I'm active and listening, Sir..!")
            print("I'm active and listening, Sir..!")

        elif 'go offline' in query or 'go to sleep' in query:            
            print("going offline..!, you can call me anytime. I'm always there to help you Sir..!")
            speak("going offline..!, you can call me anytime. I'm always there to help you Sir..!")
            break

        elif 'good bye' in query or 'goodbye' in query:
            print("Have a good Time sir, Buh-Bye...!")
            speak("Have a good Time sir, Buh-Bye...!")
            sys.exit()

        elif 'give your introduction' in query:
            playsound("Jarvis Startup - Introduction.mp3") # put the audio file in cwd.                   ---for windows 
            
          # subprocess.call(["afplay", "/Users/sahilbhor/songs/Jarvis Startup - Introduction.mp3"]).      ---for mac users
            
          # you can use speak function rather than the audio file

if __name__ == '__main__':
    while True:
        
        permission = take_command()
        if 'wake up' in permission:
            wish_me()
            task_execution()

        elif 'good bye' in permission or 'goodbye' in permission:
            print("Have a good Time sir, Buh-Bye...!")
            speak("Have a good Time sir, Buh-Bye...!")
            sys.exit()

        elif 'are you there' in permission:
            print("yes sir. I'm always there to help you.....!")
            speak("yes sir. I'm always there to help you.....!")
            task_execution()

        
"""
  Commands :-
  1) wake up - Initial Command
  2) what is our college name
  3) give your introduction
  4) take me to our college erp
  5) the time
  6) play music
  7) open stack overflow
  8) open youtube
  9) open google
  10) wikipedia
  11) go offline 
  12) good bye - To quit the program

"""  
    
