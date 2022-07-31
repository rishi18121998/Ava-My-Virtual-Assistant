import subprocess
from VoiceIO import Speak, takeCommand
import os
import random
import cv2

app_list = []


def start_application(application):
    global app_list
    if application in app_list:
        st = "automate.bat \"{}\"".format(application)
        subprocess.getoutput(st)
    else:
        app_list.append(application)
        subprocess.getoutput("start {}".format(application))


# this function kill the application running in computer
def close_application():
    global app_list
    application = takeCommand("Which Application do you want to close")
    # if "chrome" in app:
    #     app = "chrome"
    if "notepad" in application:
        application = "notepad"
    elif "media player" in application:
        application = "wmplayer"
    elif "vlc" in application:
        application = "vlc"
    elif "music" in application or "song" in application or "songs" in application:
        application = "Music.UI"
    subprocess.getoutput("taskkill /IM {}.exe /f".format(application))
    # removing that particular application from the list....
    if application in app_list:
        app_list.remove(application)
        Speak("{} killed".format(application))
    else:
        Speak("No such process is running")


def play_song():
    music_directory = "F:\\Download\\audios"  # Default music directory
    choice = takeCommand("Do you want to make the use of your default song directory")
    if "no" in choice or ("new" in choice and "directory" in choice):
        Speak("Enter the new directory path ")
        music_directory = input("Enter the new directory path-:")
    songs = os.listdir(music_directory)
    n = random.randint(0, len(songs))
    os.startfile(os.path.join(music_directory, songs[n]))
    global app_list
    app_list.append("Music.UI")


# this function take a image show and save
def start_camera():
    cam = cv2.VideoCapture(0)  # to start local web cam
    if not cam.isOpened():
        Speak("camera can't be opened")
        return
    while True:
        ret, image = cam.read()
        cv2.imshow("preview", image)
        if cv2.waitKey(5000):
            break
    cv2.imshow("image", image)  # to show image
    Speak("type file name")
    file_name = input("type file name hear :-")
    cv2.imwrite(os.path.join("E:\image", file_name), image)  # to save image
    cam.release()
    cv2.destroyAllWindows()
    Speak("image captured")
    print("saved at {}".format(os.path.join("E:\image", file_name)))
