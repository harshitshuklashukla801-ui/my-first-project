import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import subprocess
import urllib.parse
import requests
import wikipedia
import random
import math


# ============================================================
# JARVIS SETTINGS
# ============================================================

engine = pyttsx3.init()

engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)


# ============================================================
# SPEAK
# ============================================================

def speak(text):
    print("JARVIS:", text)

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)


# ============================================================
# LISTEN
# ============================================================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.pause_threshold = 0.8

        try:
            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        except sr.WaitTimeoutError:
            return ""

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("YOU:", command)

        return command.lower()

    except sr.UnknownValueError:

        speak("Sorry, I didn't understand that.")

        return ""

    except sr.RequestError:

        speak("Speech recognition service is unavailable.")

        return ""


# ============================================================
# OPEN WEBSITE
# ============================================================

def open_website(url, name):

    speak("Opening " + name)

    webbrowser.open(url)


# ============================================================
# GOOGLE SEARCH
# ============================================================

def google_search(query):

    speak("Searching Google for " + query)

    query = urllib.parse.quote_plus(query)

    url = "https://www.google.com/search?q=" + query

    webbrowser.open(url)


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(query):

    speak("Searching YouTube for " + query)

    query = urllib.parse.quote_plus(query)

    url = (
        "https://www.youtube.com/results?search_query="
        + query
    )

    webbrowser.open(url)


# ============================================================
# OPEN CHROME
# ============================================================

def open_chrome():

    chrome_paths = [

        r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",

        r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe"
    ]

    for path in chrome_paths:

        path = os.path.expandvars(path)

        if os.path.exists(path):

            speak("Opening Chrome")

            subprocess.Popen(path)

            return

    speak("Chrome was not found on this computer.")


# ============================================================
# OPEN WHATSAPP
# ============================================================

def open_whatsapp():

    speak("Opening WhatsApp")

    webbrowser.open(
        "https://web.whatsapp.com"
    )


# ============================================================
# WINDOWS APPLICATIONS
# ============================================================

def open_windows_app(command):

    if "calculator" in command:

        speak("Opening calculator")

        os.system("calc")

    elif "notepad" in command:

        speak("Opening Notepad")

        os.system("notepad")

    elif "paint" in command:

        speak("Opening Paint")

        os.system("mspaint")

    elif "command prompt" in command or "open cmd" in command:

        speak("Opening Command Prompt")

        os.system("start cmd")

    elif "file explorer" in command or "explorer" in command:

        speak("Opening File Explorer")

        os.system("explorer")

    elif "control panel" in command:

        speak("Opening Control Panel")

        os.system("control")

    elif "task manager" in command:

        speak("Opening Task Manager")

        os.system("taskmgr")

    else:

        return False

    return True


# ============================================================
# WINDOWS SETTINGS
# ============================================================

def open_settings():

    speak("Opening Windows Control Panel")

    os.system("control")


# ============================================================
# OPEN FOLDERS
# ============================================================

def open_folder(folder):

    home = os.path.expanduser("~")

    folders = {

        "downloads":
            os.path.join(home, "Downloads"),

        "documents":
            os.path.join(home, "Documents"),

        "pictures":
            os.path.join(home, "Pictures"),

        "music":
            os.path.join(home, "Music"),

        "videos":
            os.path.join(home, "Videos"),

        "desktop":
            os.path.join(home, "Desktop")
    }

    if folder in folders:

        path = folders[folder]

        if os.path.exists(path):

            speak("Opening " + folder)

            os.startfile(path)

        else:

            speak("That folder does not exist.")

    else:

        speak("I don't know that folder.")


# ============================================================
# CREATE FOLDER
# ============================================================

def create_folder(name):

    desktop = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    path = os.path.join(
        desktop,
        name
    )

    if not os.path.exists(path):

        os.makedirs(path)

        speak(
            "I created the folder "
            + name
            + " on your desktop."
        )

    else:

        speak("That folder already exists.")


# ============================================================
# MUSIC
# ============================================================

def play_music():

    music_folder = os.path.join(
        os.path.expanduser("~"),
        "Music"
    )

    if not os.path.exists(music_folder):

        speak("Your Music folder was not found.")

        return

    files = []

    for filename in os.listdir(music_folder):

        if filename.lower().endswith(
            (".mp3", ".wav", ".m4a", ".wma")
        ):

            files.append(
                os.path.join(
                    music_folder,
                    filename
                )
            )

    if len(files) == 0:

        speak("I could not find any music files.")

        return

    song = random.choice(files)

    speak(
        "Playing "
        + os.path.basename(song)
    )

    os.startfile(song)


# ============================================================
# TIME
# ============================================================

def tell_time():

    current_time = datetime.datetime.now().strftime(
        "%I:%M %p"
    )

    speak(
        "The time is "
        + current_time
    )


# ============================================================
# DATE
# ============================================================

def tell_date():

    today = datetime.datetime.now().strftime(
        "%d %B %Y"
    )

    speak(
        "Today's date is "
        + today
    )


# ============================================================
# CALCULATOR
# ============================================================

def calculator(command):

    try:

        expression = command

        expression = expression.replace(
            "calculate",
            ""
        )

        expression = expression.replace(
            "what is",
            ""
        )

        expression = expression.replace(
            "plus",
            "+"
        )

        expression = expression.replace(
            "minus",
            "-"
        )

        expression = expression.replace(
            "multiplied by",
            "*"
        )

        expression = expression.replace(
            "multiply",
            "*"
        )

        expression = expression.replace(
            "divided by",
            "/"
        )

        expression = expression.replace(
            "divide",
            "/"
        )

        expression = expression.replace(
            "x",
            "*"
        )

        expression = expression.strip()

        allowed = "0123456789+-*/(). %"

        if not all(
            character in allowed
            for character in expression
        ):

            speak("I can only calculate mathematical expressions.")

            return

        answer = eval(
            expression,
            {
                "__builtins__": None
            },
            {}
        )

        speak(
            "The answer is "
            + str(answer)
        )

    except Exception:

        speak(
            "Sorry, I could not calculate that."
        )


# ============================================================
# WIKIPEDIA
# ============================================================

def wikipedia_search(query):

    query = query.strip()

    if query == "":

        speak("What should I search on Wikipedia?")

        return

    speak(
        "Searching Wikipedia for "
        + query
    )

    try:

        wikipedia.set_lang("en")

        result = wikipedia.summary(
            query,
            sentences=2
        )

        print("\nWikipedia:")
        print(result)

        speak(result)

    except wikipedia.exceptions.DisambiguationError as e:

        speak(
            "There are multiple results. "
            "Please be more specific."
        )

    except Exception:

        speak(
            "I could not find that on Wikipedia."
        )


# ============================================================
# WEATHER
# ============================================================

def weather(city):

    speak(
        "Getting the weather for "
        + city
    )

    try:

        url = (
            "https://wttr.in/"
            + urllib.parse.quote(city)
            + "?format=j1"
        )

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]

        humidity = current["humidity"]

        description = current[
            "weatherDesc"
        ][0]["value"]

        answer = (
            "The weather in "
            + city
            + " is "
            + description
            + ". Temperature is "
            + str(temperature)
            + " degrees Celsius. "
            + "Humidity is "
            + str(humidity)
            + " percent."
        )

        speak(answer)

    except Exception:

        speak(
            "Sorry, I could not get the weather."
        )


# ============================================================
# AI QUESTION ANSWERING
# ============================================================

def ask_ai(question):

    api_key = os.environ.get(
        "OPENAI_API_KEY"
    )

    if not api_key:

        speak(
            "The AI API key is not configured. "
            "I can still perform my other commands."
        )

        print(
            "\nTo enable AI answers, set "
            "OPENAI_API_KEY in Windows."
        )

        return

    try:

        url = "https://api.openai.com/v1/responses"

        headers = {
            "Content-Type":
                "application/json",

            "Authorization":
                "Bearer " + api_key
        }

        data = {
            "model": "gpt-5.6",
            "input": question
        }

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

        if response.status_code != 200:

            print(
                "AI API error:",
                response.text
            )

            speak(
                "The AI service returned an error."
            )

            return

        result = response.json()

        answer = result.get(
            "output_text",
            ""
        )

        if not answer:

            # Fallback extraction
            output = result.get(
                "output",
                []
            )

            answer_parts = []

            for item in output:

                content = item.get(
                    "content",
                    []
                )

                for part in content:

                    if part.get("type") == "output_text":

                        answer_parts.append(
                            part.get("text", "")
                        )

            answer = " ".join(
                answer_parts
            )

        if answer:

            print(
                "\nAI:",
                answer
            )

            speak(answer)

        else:

            speak(
                "I received an empty answer."
            )

    except Exception as e:

        print(
            "AI error:",
            str(e)
        )

        speak(
            "I could not connect to the AI service."
        )


# ============================================================
# HELP
# ============================================================

def show_help():

    print("""
============================================================
                    JARVIS COMMANDS
============================================================

WEBSITES
    Open Google
    Open YouTube
    Open Chrome
    Open WhatsApp

SEARCH
    Search Google for Python
    Search YouTube for Python tutorial
    Search Wikipedia for Albert Einstein

WINDOWS
    Open Settings
    Open Calculator
    Open Notepad
    Open Paint
    Open CMD
    Open File Explorer
    Open Control Panel
    Open Task Manager

FOLDERS
    Open Downloads
    Open Documents
    Open Pictures
    Open Music
    Open Videos
    Open Desktop

FILES
    Create folder called Projects

MUSIC
    Play music

INFORMATION
    What is the time?
    What is today's date?
    Weather in Lucknow

CALCULATOR
    Calculate 25 multiplied by 8
    Calculate 100 divided by 4
    Calculate 50 plus 25

AI
    Explain photosynthesis
    What is Python?
    Ask any question

EXIT
    Goodbye
    Exit
    Quit
============================================================
""")


# ============================================================
# COMMAND PROCESSOR
# ============================================================

def process_command(command):

    if not command:

        return True


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if (
        command == "exit"
        or command == "quit"
        or command == "goodbye"
        or "stop jarvis" in command
    ):

        speak(
            "Goodbye. See you later."
        )

        return False


    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    if (
        command == "help"
        or "what can you do" in command
    ):

        show_help()

        speak(
            "I displayed my commands on the screen."
        )

        return True


    # --------------------------------------------------------
    # GREETING
    # --------------------------------------------------------

    if (
        command == "hello"
        or command == "hi"
        or "hello jarvis" in command
    ):

        speak(
            "Hello. I am Jarvis. "
            "How can I help you?"
        )

        return True


    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if "time" in command:

        tell_time()

        return True


    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    if "date" in command:

        tell_date()

        return True


    # --------------------------------------------------------
    # YOUTUBE SEARCH
    # --------------------------------------------------------

    if "search youtube for" in command:

        query = command.replace(
            "search youtube for",
            "",
            1
        ).strip()

        youtube_search(query)

        return True


    # --------------------------------------------------------
    # GOOGLE SEARCH
    # --------------------------------------------------------

    if "search google for" in command:

        query = command.replace(
            "search google for",
            "",
            1
        ).strip()

        google_search(query)

        return True


    # --------------------------------------------------------
    # WIKIPEDIA SEARCH
    # --------------------------------------------------------

    if "search wikipedia for" in command:

        query = command.replace(
            "search wikipedia for",
            "",
            1
        ).strip()

        wikipedia_search(query)

        return True


    # --------------------------------------------------------
    # OPEN YOUTUBE
    # --------------------------------------------------------

    if "open youtube" in command:

        open_website(
            "https://www.youtube.com",
            "YouTube"
        )

        return True


    # --------------------------------------------------------
    # OPEN GOOGLE
    # --------------------------------------------------------

    if "open google" in command:

        open_website(
            "https://www.google.com",
            "Google"
        )

        return True


    # --------------------------------------------------------
    # OPEN WHATSAPP
    # --------------------------------------------------------

    if "open whatsapp" in command:

        open_whatsapp()

        return True


    # --------------------------------------------------------
    # OPEN CHROME
    # --------------------------------------------------------

    if "open chrome" in command:

        open_chrome()

        return True


    # --------------------------------------------------------
    # SETTINGS
    # --------------------------------------------------------

    if (
        "open settings" in command
        or "open control panel" in command
    ):

        open_settings()

        return True


    # --------------------------------------------------------
    # WINDOWS APPS
    # --------------------------------------------------------

    if open_windows_app(command):

        return True


    # --------------------------------------------------------
    # FOLDERS
    # --------------------------------------------------------

    folder_names = [
        "downloads",
        "documents",
        "pictures",
        "music",
        "videos",
        "desktop"
    ]

    for folder in folder_names:

        if (
            "open " + folder
            in command
        ):

            open_folder(folder)

            return True


    # --------------------------------------------------------
    # CREATE FOLDER
    # --------------------------------------------------------

    if "create folder called" in command:

        name = command.replace(
            "create folder called",
            "",
            1
        ).strip()

        if name:

            create_folder(name)

        return True


    # --------------------------------------------------------
    # MUSIC
    # --------------------------------------------------------

    if (
        "play music" in command
        or "play a song" in command
    ):

        play_music()

        return True


    # --------------------------------------------------------
    # CALCULATOR
    # --------------------------------------------------------

    if (
        command.startswith("calculate")
        or "multiplied by" in command
        or "divided by" in command
    ):

        calculator(command)

        return True


    # --------------------------------------------------------
    # WEATHER
    # --------------------------------------------------------

    if "weather in" in command:

        city = command.split(
            "weather in",
            1
        )[1].strip()

        weather(city)

        return True


    if command == "weather":

        weather("Lucknow")

        return True


    # --------------------------------------------------------
    # WIKIPEDIA
    # --------------------------------------------------------

    if "who is " in command:

        query = command.replace(
            "who is",
            "",
            1
        ).strip()

        wikipedia_search(query)

        return True


    if "what is " in command:

        # First try calculator if mathematical
        if any(
            symbol in command
            for symbol in [
                "plus",
                "minus",
                "multiplied",
                "divided"
            ]
        ):

            calculator(command)

            return True


    # --------------------------------------------------------
    # AI
    # --------------------------------------------------------

    ask_ai(command)

    return True


# ============================================================
# MAIN
# ============================================================

def main():

    speak(
        "Jarvis is now online."
    )

    speak(
        "Say help to see what I can do."
    )

    while True:

        command = listen()

        if command == "":

            continue

        keep_running = process_command(
            command
        )

        if not keep_running:

            break


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    main()