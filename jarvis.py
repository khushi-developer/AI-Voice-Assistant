import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
from PIL import Image, ImageGrab
import time

eng = pyttsx3.init()

def speak(msg):
    eng.say(msg)
    eng.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    
    if hour>0 and hour<=12:
        speak("Good morning!")

    elif hour>12 and hour<=17:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am jarvis miss khushi, how can i help you")

# code for chrome dino
def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    # for cactus
    for i in range(470,510):
        for j in range(240,290):
            if data[i,j] < 100:
                hit("up")
                return True
    # for bird
    for i in range(470,510):
        for j in range(180,240):
            if data[i,j] < 100:
                hit("down")
                return True

    return False


def takeCommand():
    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                print("Waiting to be called on")
                r.adjust_for_ambient_noise(source, duration = 1)
                r.pause_threshold=1
                audio = r.listen(source)
                query = str(r.recognize_google(audio,language="en-in"))
                query = query.lower()
                print("you said: ",query)
                if 'hey buddy' in query:
                    speak("yah")

                elif 'facebook' in query:
                    webbrowser.open('https://www.facebook.com') 
                        
                elif 'youtube' in query:
                    webbrowser.open('https://www.youtube.com')

                elif 'wikipedia' in query:
                    print("searching wikipedia....")
                    result=wikipedia.summary(r.recognize_google(audio,language="en-in"),sentences=2)
                    print(result)
                    speak("According to wikipedia")
                    speak(result)

                elif 'play game' in query:
                    print("game will start within 3 seconds")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open('https://chromedino.com/')
                    time.sleep(3)
                    # hit("up")
                    while True:
                        image = ImageGrab.grab().convert('L') 
                        data = image.load() 
                        isCollide(data)

                elif 'stop' in query:
                    break

                speak(query)
                
            
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    

if __name__ == "__main__":
    wishMe()
    takeCommand()
