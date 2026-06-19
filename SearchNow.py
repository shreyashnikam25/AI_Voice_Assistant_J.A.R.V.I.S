from jarvis_main import speak
import pywhatkit
import wikipedia
import webbrowser


def searchGoogle(query):
    query = query.replace("google", "").replace("search", "").replace("jarvis", "")
    speak("This is what I found on Google.")

    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, 1)
        speak(result)
    except:
        speak("No speakable output found.")


def searchYoutube(query):
    speak("Searching on YouTube.")
    query = query.replace("youtube", "").replace("search", "").replace("jarvis", "")
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done sir.")


def searchWikipedia(query):
    query = query.replace("wikipedia", "").replace("search", "").replace("jarvis", "")
    speak("Searching Wikipedia.")
    try:
        result = wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        speak(result)
    except:
        speak("Sorry, nothing found.")



def searchWeather(query):
    speak("Searching for Weather.")
    query = query.replace("Weather", "").replace("search", "").replace("jarvis", "")
    web = "https://www.google.com/search?q=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done sir.")                                                                


                                                                  