import pyttsx3
import speech_recognition as sr
import datetime
import re
import subprocess
from urllib.parse import quote_plus

import wikipedia
import webbrowser
import os

engine = None

def get_engine():
    global engine
    if engine is None:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[0].id)
    return engine

def speak(text):
    print("Jarvis:", text)
    try:
        speaker = get_engine()
        speaker.say(text)
        speaker.runAndWait()
    except Exception as error:
        print(f"Text-to-speech unavailable: {error}")

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print("User said:", query)
        return query.lower()
    except:
        print("Could not understand. Please say again.")
        return ""

def clean_search_text(query, keywords):
    filler_words = [
        "open",
        "search",
        "find",
        "play",
        "on",
        "in",
        "for",
        "about",
        "please",
        "karo",
        "kar",
        "khojo",
    ]
    text = query
    cleanup_words = sorted(keywords + filler_words, key=len, reverse=True)
    for keyword in cleanup_words:
        text = re.sub(rf"\b{re.escape(keyword)}\b", " ", text)
    return " ".join(text.split())

def open_url(url, app_name=None):
    if app_name == "edge":
        path = find_edge()
    elif app_name == "opera gx":
        path = find_opera_gx()
    else:
        path = None

    if path:
        subprocess.Popen([path, url])
        return

    webbrowser.open(url)

def find_edge():
    paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def find_opera_gx():
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    paths = [
        os.path.join(local_app_data, "Programs", "Opera GX", "opera.exe"),
        r"C:\Program Files\Opera GX\opera.exe",
        r"C:\Program Files (x86)\Opera GX\opera.exe",
    ]
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def handle_site_command(query, name, keywords, home_url, search_url, browser_name=None):
    if not any(keyword in query for keyword in keywords):
        return False

    search_text = clean_search_text(query, keywords)
    wants_search = any(word in query for word in ["search", "find", "play", "khojo"]) or bool(search_text)

    if wants_search and search_text:
        open_url(search_url.format(quote_plus(search_text)), browser_name)
        speak(f"Searching {search_text} on {name}")
    else:
        open_url(home_url, browser_name)
        speak(f"Opening {name}")

    return True

if __name__ == "__main__":
    wish_user()

    while True:
        query = take_command()

        if "wikipedia" in query or "wikipidia" in query:
            search_text = clean_search_text(query, ["wikipedia", "wikipidia"])
            if search_text:
                speak("Searching Wikipedia")
                try:
                    result = wikipedia.summary(search_text, sentences=2)
                    speak(result)
                except:
                    open_url(f"https://en.wikipedia.org/wiki/Special:Search?search={quote_plus(search_text)}")
                    speak("No summary found. Opening Wikipedia search")
            else:
                open_url("https://wikipedia.org")
                speak("Opening Wikipedia")

        elif handle_site_command(
            query,
            "YouTube",
            ["youtube", "you tube"],
            "https://youtube.com",
            "https://www.youtube.com/results?search_query={}",
        ):
            pass

        elif handle_site_command(
            query,
            "Google",
            ["google"],
            "https://google.com",
            "https://www.google.com/search?q={}",
        ):
            pass

        elif handle_site_command(
            query,
            "Stack Overflow",
            ["stackoverflow", "stack overflow"],
            "https://stackoverflow.com",
            "https://stackoverflow.com/search?q={}",
        ):
            pass

        elif handle_site_command(
            query,
            "WhatsApp",
            ["whatsapp", "whatapp", "whats app", "what's app"],
            "https://web.whatsapp.com",
            "https://web.whatsapp.com/send?text={}",
        ):
            pass

        elif handle_site_command(
            query,
            "Edge",
            ["edge", "microsoft edge"],
            "https://www.google.com",
            "https://www.google.com/search?q={}",
            browser_name="edge",
        ):
            pass

        elif handle_site_command(
            query,
            "Opera GX",
            ["opera gx", "opera"],
            "https://www.google.com",
            "https://www.google.com/search?q={}",
            browser_name="opera gx",
        ):
            pass

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "exit" in query or "stop" in query:
            speak("Goodbye")
            break

        else:
            speak("Command not recognized")
