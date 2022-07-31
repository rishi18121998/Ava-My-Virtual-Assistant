from VoiceIO import Speak, takeCommand
from WebApplication import start_facebook, start_youtube, search_on_chrome, search_on_wikipedia
from System import play_song, close_application, start_application, start_camera
from Message import sendEmail
from Ava import calculator, wishMe, tellTime, reply, weather, todayNews

if __name__ == "__main__":
    # wishMe()
    message = "Listening"
    while True:
        # taking instruction from user
        input_from_user = takeCommand(message)
        if input_from_user == "none":
            print("Again Listening")
            message = ""
            continue
        message = "Listening"
        # local application part
        if ("launch" in input_from_user) or ("go to" in input_from_user) or ("start" in input_from_user) or (
                "get back" in input_from_user) or ("take me" in input_from_user) or (
                "open" in input_from_user and "file" not in input_from_user):
            if "chrome" in input_from_user:
                application = "chrome"
            elif "notepad" in input_from_user:
                application = "notepad"
            elif "media player" in input_from_user:
                application = "wmplayer"
            elif ("vlc" in input_from_user) or ("videoplayer" in input_from_user):
                application = "vlc"
            else:
                Speak("Sorry I Unable to understand  Can you please speak again")
                continue
            start_application(application)

        # searching on google
        elif "search" in input_from_user:
            search_on_chrome()
            continue

        # send mail
        elif ("send" in input_from_user) and ("email" in input_from_user):
            sendEmail()
            continue

        # asking the victor
        elif ("listening" in input_from_user or "listening" in input_from_user) and (
                ("me" in input_from_user) or ("us" in input_from_user)):
            Speak("I am listening to you sir waiting for your next instruction.")
            continue
        elif ((("hi" in input_from_user) or ("hello" in input_from_user)) and ("victor" in input_from_user)) or (
                "how are you" in input_from_user):
            reply()
            continue
        elif "good morning" in input_from_user or "good evening" in input_from_user or "good afternoon" in input_from_user:
            wishMe()
            continue
        elif ("what is time" in input_from_user) or ("tell me time" in input_from_user):
            tellTime()
            continue
        elif ("tell me about" in input_from_user) or ("do you know about" in input_from_user):
            search_on_wikipedia()
            continue

        # closing local application or victor
        elif ("close" in input_from_user) or ("exit" in input_from_user) or ("shut down" in input_from_user) or (
                "shut" in input_from_user) or ("stop" in input_from_user) or ("terminate" in input_from_user) or (
                "exit" in input_from_user):
            if ("application" not in input_from_user) and ("app" not in input_from_user):
                Speak("Okay! I am shutting down sir Have a nice day")
                exit()
            else:
                close_application()
                continue

        # take image
        elif ("take" in input_from_user) and (("image" in input_from_user) or ("photo" in input_from_user) or "picture" in input_from_user or "snapshot" in input_from_user):
            start_camera()
            continue

        # login to facebook
        elif ("login" in input_from_user) and ("facebook" in input_from_user):
            start_facebook()
            continue

        # play video on youtube
        elif ("play" in input_from_user) and ("youtube" in input_from_user):
            start_youtube()
            continue

        # play song for me
        elif ("play" in input_from_user) and (
                ("song" in input_from_user) or ("songs" in input_from_user) or ("music" in input_from_user) or (
                "musics" in input_from_user)):
            play_song()
            continue

        # do some calculations
        elif ("calculator" in input_from_user) or ("calculation" in input_from_user) or ("calculations" in input_from_user):
            calculator()
            continue

        elif ("weather" in input_from_user) or ("should i go outside" in input_from_user):
            weather()
            continue

        elif ("today's news" in input_from_user) or ("news" in input_from_user):
            todayNews()
            continue

        else:
            Speak("sorry I am unable to perform this task")
