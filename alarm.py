import pyttsx3
import datetime
import time
import pygame
import threading

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ring_alarm(alarm_time):
    pygame.mixer.init()
    speak("Alarm set, sir")
    print("Alarm set for:", alarm_time)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            speak("Alarm ringing, sir")
            pygame.mixer.music.load("C:\\Users\\nikam\\Music\\annoying_alarm_clock.mp3")
            pygame.mixer.music.play()
            time.sleep(30)  # Alarm duration
            pygame.mixer.music.stop()
            break
        time.sleep(1)

def ring(alarm_time):
    # Run the alarm in a separate thread
    t = threading.Thread(target=ring_alarm, args=(alarm_time,))
    t.start()
