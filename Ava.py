from VoiceIO import Speak, takeCommand
import datetime
import requests
from bs4 import BeautifulSoup


# this function reply to user by speaking
def reply():
    Speak("Hi Sir! I am fine Hope you are gviood in this pandemic situation")


# this function tell current time
def tellTime():
    time = datetime.datetime.now()
    date = time.date()
    hour = time.hour
    minute = time.minute
    if hour < 12:
        if hour == 0:
            hour = 12
        Speak("today is {} and it is  {} {} AM".format(date, hour, minute))
    else:
        if hour != '12':
            hour = hour - 12
        Speak("today is {} and it is  {} {} PM".format(date, hour, minute))


# This function greet the user according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        Speak("Good Morning! Sir")
    elif (hour >= 12) and (hour < 18):
        Speak("Good Afternoon! Sir")
    else:
        Speak("Good Evening! Sir")
    Speak("I am Ava your virtual assistant . Please tell me how may I help you")


# for doing voice based calculation
def calculator():
    exp = takeCommand("tell me the expression")
    try:
        ans = eval(exp)
        Speak(exp + " is equal to " + ans)
    except Exception :  # exception handling in case of wrong input given by user
        Speak("can't evaluate expression")


def weather():
    url = "https://weather.com/en-IN/weather/today/l/27.55,76.63?par=google&temp=c"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")
    x = soup.find('div', class_="CurrentConditions--primary--3xWnK")
    temp = x.find('span', class_="CurrentConditions--tempValue--3KcTQ").text
    weatherStatus = x.find('div', class_="CurrentConditions--phraseValue--2xXSr").text
    Speak("Today temperature is " + temp + " Centigrade")
    Speak("weather is " + weatherStatus)
    if "cloudy" in weatherStatus:
        Speak("you should think before going outside")
    else:
        if int(temp[:2]) > 35:
            Speak("it is very hot outside you should drink water before going outside")
        elif int(temp[:2]) > 15:
            Speak("weather is pleasant outside you can go on a tour")
        else:
            Speak("it is very cold outside wear warm clothes")


def todayNews():
    key = "ff09ac0e6cab418ca2ee46c5f728f5dd"
    time = datetime.datetime.now()
    date = time.date()
    url = f"http://newsapi.org/v2/top-headlines?country=IN&from={date}&sortBy=publishedAt&apiKey={key}"
    x = requests.get(url).json()
    hour = int(time.hour)
    if (hour >= 0) and (hour < 12):
        Speak("Good Morning! Sir")
    elif (hour >= 12) and (hour < 18):
        Speak("Good Afternoon! Sir")
    else:
        Speak("Good Evening! Sir")
    Speak("today's highlights    click on link for more")
    for y in x['articles']:
        print("TITLE : ")
        print(y['title'])
        Speak(y['title'])
        print("DESCRIPTION : ")
        print(y['description'])
        print(y['url'])
        Speak("next news ")
    Speak("thank you sir")