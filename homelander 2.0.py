import subprocess
import pyttsx3 
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
import smtplib
import playsound
import pywhatkit
import pyjokes
import shutil
import ctypes
import time
import pyautogui
from  keyboard import volumeup
from  keyboard import volumedown
from pygame import mixer
from plyer import notification




from Intro import play_gif
play_gif  
  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
    
    else:
        speak("Good Evening!!")

def username():

    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome Master")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome .", uname.center(columns))
    print("#####################".center(columns))


    speak("Hi, I am Home Lander. How may i help you ?")


def takeCommand():
    r = sr.Recognizer()
    my_mic = sr.Microphone(device_index=1)
    with my_mic as source:
        print("Listening........")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    

    try:
        print("Recognising.......")
        query= r.recognize_google(audio, language="en-in")
        print(f"User said:{query}\n")


    except Exception as e:
        print(e)
        print("Say that again..........")
        return "None"

    return query
            
                  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('@gmail.com', 'pwd')
    server.sendmail('@gmail.com', to, content)
    server.close()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

    
if __name__ == "__main__":
    wishMe() 
    username()
    while True:
    
        query = takeCommand().lower()
        if 'wikipedia express' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            
            print(results)
            speak("According to Wikipedia")
            speak(results)

        elif 'search' in query:
            query = query.replace("search", "")         
            webbrowser.open(query)
    
        elif "temperature" in query:
            search = "temperature in Mumbai"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
        elif "weather" in query:
            search = "temperature in Mumbai"
            url = f"https://www.google.com/search?q={search}"
            r   = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm("a")
            speak("Done,sir") 
         
        
        elif 'thank you' in query:
            speak(f"you are welcome")
            print("you are welcome")

        elif 'are you single' in query:
            speak(f"only for you my baby!")

        
        elif 'say hello to' in query:
            name = query.replace('say hello to', '')
            speak('hello' + name)

        elif 'say hi to' in query:
            name = query.replace('say hi to', '')
            speak('hi' + name)

        elif 'say hai to' in query:
            name = query.replace('say hai to', '')
            speak('hai' + name)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com//")


        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query or 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            

        elif 'play music' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The Time is {strTime}")


        elif 'email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "yadavniki418@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend cannot send mail")
           
        #yt automation
        elif "stop" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")

        elif "volume up" in query:
        
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
        
            speak("Turning volume down, sir")
            volumedown()

        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()

        elif "news" in query:
            from NewsRead import latestnews
            latestnews() 

        elif "calculate" in query:
            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("homelander","")
            Calc(query)     

            

        
        
        elif 'who made you' in query:
            speak(f"master Geeta made me")
            print("master Geeta made me")

        elif 'who created you' in query:
            speak(f"master Nikita created me")
            print("master Nikita created me")

        elif 'who invented you' in query:
            speak(f"master Hardik invented me")
            print("master Hardik invented me")

        
        elif 'who is your enemy' in query:
            speak(f"anyone who is smarter than me is my enemy")
            print("anyone who is smarter than me is my enemy")
        
        elif 'how much loyal you are to master' in query:
            speak(f"as loyal as son to dad")
            print("as loyal as son to dad")
        
        elif 'favourite dialouge' in query:
            speak(f"scorched the earth")
            print("scorched the earth")

        
        elif 'are you better than google assistant' in query:
            speak(f"well that is a debatable topic, you can speak to my master regarding that")
            print("well that is a debatable topic, you can speak to my master regarding that")
        
        elif 'are you better than alexa' in query:
            speak(f"well that is a debatable topic, you can speak to my master regarding that")
            print("well that is a debatable topic, you can speak to my master regarding that")
            
        elif 'what is universe' in query:
            speak(f"I dont have much idea about that, but according to my master there exists two universe one is marvel and the other one is D C")
            print("I dont have much idea about that, but according to my master there exists two universe one is marvel and the other one is D C")

        

        elif 'date of birth' in query or 'd o b' in query:
            print("thursday 14th july 2022")
            speak(f"thursday 14th july 2022") 
              

        elif 'born' in query:
            print("thursday 14th july 2022")
            speak(f"thursday 14th july 2022")
            

        

        elif 'who are you' in query:
            print("I am Home Lander, an AI")
            speak(f"I am Home Lander, an AI")

        elif 'prime minister of india' in query:
            speak(f"Mr. Narendra Modi")
            print("Mr. Narendra Modi")

        elif 'purpose' in query:
            speak(f"being relaxation for human race")
            print("being relaxation for human race")

        elif 'look like' in query:
            speak(f"wait a second let me show you")
            webbrowser.open("https://wallpapercave.com/w/wp4807581")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            print("It's good to know that your fine")

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "new name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
            print("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to master. further It's a secret")
            print("Thanks to master. further It's a secret")
        
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\pexels-pixabay-210186.jpg", 0)
            speak("Background changed successfully")
            print("Background changed successfully")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
                     
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('homelander.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note) 
      
        elif "show note" in query:
            speak("Showing Notes")
            file = open("homelander.txt", "r") 
            print(file.read())
            speak(file.read(6))

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()


