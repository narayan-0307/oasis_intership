import speech_recognition as sr  #Library for performing speech recognition, with support for several engines and APIs, online and offline.

import webbrowser
import pyttsx3  #pyttsx3 is a text-to-speech conversion library in Python

import musicLibrary

newsApi = "824443020d174a1491db80abac72f0a0"
import requests

#This function gives us to recognite the speech recognize functionality
recognizer = sr.Recognizer() 

#Enitialize the ttsx engine 
engine = pyttsx3.init()


#Created the function that speak like text-to-speech.
def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    # print(c)
    print(f"command: {c}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsApi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])

    else:
        speak("Sorry, I can't understand")


if __name__ == "__main__":
    speak("Initializing Jarvis........")
    while True:     
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing....")
        
            
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                # audio = r.listen(source)
            word = r.recognize_google(audio)

            if(word.lower() == "are you audible"):
                speak("Yeah")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    # recognizer.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    command = r.recognize_google(audio, language="hi-IN")

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))




#Stopped 10:00:19