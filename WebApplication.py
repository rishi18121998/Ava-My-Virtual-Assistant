from selenium import webdriver
from VoiceIO import Speak, takeCommand
from os import system
import wikipedia
from System import app_list
from webdriver_manager.chrome import ChromeDriverManager


# this function search on wikipedia
def search_on_wikipedia():
    x = takeCommand("what do you want to know about")
    Speak("let me search ...")
    try:
        topic = wikipedia.search(x)
        Speak(wikipedia.summary(topic[0], sentences=20))
    except Exception:
        Speak("Sorry i can't understand")


# this function open chrome to search something
def search_on_chrome():
    # to take input what user want to search
    x = takeCommand("What you want to search like to search like today weather or something")
    query = ""
    for i in range(0, len(x)):
        if x[i] == " ":
            query = query + "+"
        else:
            query = query + x[i]
    print(query)
    # url for searching something in the chrome..
    system("start chrome https://www.google.com/search?q={}".format(query))
    # global app_list
    app_list.append("chrome")


# this function login to facebook
def start_facebook():
    # taking detail of facebook id
    Speak("Enter your registered mobile number ")
    mobile_no = input("enter mobile no : ")
    Speak("Enter your password")
    passwd = input("enter password : ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # filling the information in facebook
    driver.get("https://facebook.com")
    driver.maximize_window()
    search_box = driver.find_element("xpath",'//*[@id="email"]')
    search_box.send_keys(mobile_no)
    password = driver.find_element("xpath",'//*[@id="pass"]')
    password.send_keys(passwd)
    enter_button = driver.find_element("xpath",'//*[@id="u_0_d_R/"]')
    enter_button.click()
    # global app_list
    app_list.append("chrome")
    Speak("welcome to facebook")


# this function search and play what we serch on youtube
def start_youtube():
    # asking user that what he want to search on youtube
    choice = takeCommand("what do you want to search on youtube : ")
    print(choice)
    # searching and playing the video on youtube
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://youtube.com")
    searchbox = driver.find_element("xpath", '//*[@id="search"]')
    searchbox.send_keys(choice)
    enter_but = driver.find_element("xpath",'//*[@id="search-icon-legacy"]')
    enter_but.click()
    play = driver.find_element("xpath",'//*[@id="video-title"]')
    play.click()
    # global app_list
    app_list.append("chrome")
