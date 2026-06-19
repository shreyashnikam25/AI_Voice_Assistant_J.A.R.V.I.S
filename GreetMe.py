import pyttsx3
import datetime


engine = pyttsx3.init("sapi5") 
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  
engine.setProperty("rate", 170)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning sir,"
        "I am Jarvis, a virtual artificial intelligence, "
        "and I am here to assist you with a variety of tasks, "
        "twenty four hours a day, seven days a week, "
        "System is now fully operational,"
        "tell me how can i help you.")

    elif 12 < hour <= 18:
        speak("good afternoon sir,"
        "I am Jarvis, a virtual artificial intelligence, "
        "and I am here to assist you with a variety of tasks, "
        "twenty four hours a day, seven days a week, "
        "System is now fully operational,"
        "tell me how can i help you.")

    else:
        speak("Good Evening sir,"
        "I am Jarvis, a virtual artificial intelligence, "
        "and I am here to assist you with a variety of tasks, "
        "twenty four hours a day, seven days a week, "
        "System is now fully operational,"
        "tell me how can i help you.")


def intro():
    speak(
        "Now let me introduce myself, "
        "I am Jarvis, a virtual artificial intelligence, "
        "and I am here to assist you with a variety of tasks, "
        "twenty four hours a day, seven days a week, "
        "System is now fully operational."
    )


greetMe()
intro()
