import pyttsx3
import speech_recognition 
import webbrowser
import os
import pyautogui
import keyboard
from pynput.keyboard import Key, Controller


keyboard = Controller()


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
        return query
    except:
        print("Say that again...")
        return "none"


def alarm(query):
    timehere = open("Alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

#jarvis main function starts here:
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

#Start Jarvis loop
            while True:

                query = takeCommand().lower()


                if "hello" in query:
                    speak("Hello sir, how can I help you?")

                elif "thank you" in query:
                    speak("You are welcome sir.")

#start|stop palying youtube videos
                elif "stop playing" in query:
                    pyautogui.press("k")
                    speak("video paused") 

                elif "start playing" in query:    
                    pyautogui.press("k")
                    speak("video palyed") 
    
#mute/unmute youtube videos    
                elif "mute the video" in query:
                     keyboard.press(Key.media_volume_mute)
                     keyboard.release(Key.media_volume_mute)
                     speak("system muted")

                elif "unmute the video" in query:
                     keyboard.press(Key.media_volume_mute)
                     keyboard.release(Key.media_volume_mute)
                     speak("system unmuted")

#systems volume up/volume down
                elif "volume up" in query:
                    from keyboard import volume_up
                    speak("Turning volume up")       
                    volume_up()
                
                elif "volume down" in query:
                    from keyboard import volume_down
                    speak("Turning volume down")       
                    volume_down()

#open/close any (.com extension) apps on web
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

#search any info on google
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

#search any video,songs,movie on youtube
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

#search any info on wikipedia
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "chat" in query:
                    from SearchNow import searchChat
                    searchChat(query)

#search for temperature & wheather in pune
                elif "weather" in query:
                     webbrowser.open("https://www.google.com/search?q=pune+weather")

#set an ringing alarm                   
                elif "set an alarm" in query:
                     print("Input time for example:- 10:10:10")
                     speak("Set the time")
                     a = input("Please tell the time:- ")
                     from alarm import ring
                     ring(a)  

#system stops listning, goes to sleep
                elif "go to sleep" in query:
                     speak("Going to sleep")
                     exit()
#Reminder function / jarvis will remind you about your tasks                     

                elif "remind me to" in query:
                    rememberMessage = query.replace("remind me that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("you told me to"+rememberMessage)
                    remember = open("Reminder.txt","w")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what did i told you to remind me" in query:
                    remember = open("Reminder.txt","r")
                    speak("you told me to remind that" + remember.read())



 
                
                