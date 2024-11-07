import datetime
import sys

import wikipedia
import webbrowser
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import requests
import firebase_admin
from firebase_admin import credentials, db

print('Loading your AI personal assistant')

# Initialize the Firebase app
cred = credentials.Certificate("your serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'your database url'
})

# Reference the database location where voice commands are stored
ref = db.reference('Data/voice_commands')


def send_to_database(text):
    outputRef = db.reference('Data/Result')
    outputRef.set({
        'Output': text
    })


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        print("Hello,Good Afternoon")
    else:
        print("Hello,Good Evening")


def takeCommand():
    return ref.get()


wishMe()


def listener(event):
    statement = takeCommand().lower()
    if statement == 0:
        return

    if "good bye" in statement or "ok bye" in statement or "stop" in statement:
        data = 'your personal assistant is shutting down,Good bye'
        send_to_database(data)
        print(data)
        sys.exit()

    if 'wikipedia' in statement:
        data = 'Searching Wikipedia...'
        send_to_database(data)
        print(data)

        statement = statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)

        data = "According to Wikipedia"
        send_to_database(data)
        print(data)

        data = results
        send_to_database(data)
        print(data)

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        send_to_database("youtube is open now")
        print("youtube is open now")
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        send_to_database("Google chrome is open now")
        print("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        send_to_database("Google Mail open now")
        print("Google Mail open now")
        time.sleep(5)

    # elif "weather" in statement:
    #     api_key = "8ef61edcf1c576d65d836254e11ea420"
    #     base_url = "https://api.openweathermap.org/data/2.5/weather?"
    #     print("whats the city name")
    #     city_name = takeCommand()
    #     complete_url = base_url+"appid="+api_key+"&q="+city_name
    #     response = requests.get(complete_url)
    #     x = response.json()
    #
    #     if x["cod"] != "404":
    #         y = x["main"]
    #         current_temperature = y["temp"]
    #         current_humidiy = y["humidity"]
    #         z = x["weather"]
    #         weather_description = z[0]["description"]
    #
    #         print(" Temperature in kelvin unit = " +
    #               str(current_temperature) +
    #               "\n humidity (in percentage) = " +
    #               str(current_humidiy) +
    #               "\n description = " +
    #               str(weather_description))
    #
    #     else:
    #         print("City Not Found")

    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        send_to_database(strTime)
        print(strTime)

    elif 'date' in statement:
        str = datetime.datetime.now().strftime('%d-%m-%Y')
        send_to_database(str)
        print(str)

    elif 'who are you' in statement or 'what can you do' in statement:
        data = 'I am Remote Voice Assistant version 1 point O your personal assistant. I am programmed to minor tasks like opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia, etc. get top headline news from times of india and you can ask me computational or geographical questions too!'

        send_to_database(data)
        print(data)

    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        send_to_database("I was built by Dhruv")
        print("I was built by Dhruv")

    elif "open stackoverflow" in statement:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        send_to_database("Here is StackOverFlow")
        print("Here is StackOverFlow")

    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        send_to_database('Here are some headlines from the Times of India,Happy reading')
        print('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif "camera" in statement or "take a photo" in statement:
        send_to_database("You can see the picture in your gallery now. In your Pc")
        ec.capture(0, "robo camera", "img.jpg")

    elif 'search' in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)

    # elif 'ask' in statement:
    #     print('I can answer to computational and geographical questions and what question do you want to ask now')
    #     question = takeCommand()
    #     app_id = "R2K75H-7ELALHR35X"
    #     client = wolframalpha.Client('R2K75H-7ELALHR35X')
    #     res = client.query(question)
    #     answer = next(res.results).text
    #     print(answer)

    elif "log off" in statement or "sign out" in statement:
        data = "Ok , your pc will log off in 10 sec make sure you exit from all applications"
        print(data)
        send_to_database(data)
        subprocess.call(["shutdown", "/l"])


ref.listen(listener)

time.sleep(3)
