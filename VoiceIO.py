import pyttsx3  # for converting text to speech
import speech_recognition as sr  # for converting speech to text
from time import sleep  # for pause the execution

# sampling frequency rate .for converting the analog signal to digital signal
sample_rate = 20000
chunk_size = 2048  # it is a buffer..It stores 2048 samples (bytes of data)

# initializing the engine
engine = pyttsx3.init()
# providing a voice to the engine from which It will speak
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()


# this function converts voice to text


def takeCommand(instruction="Listening for your next instruction"):
    # initializing the recognizer..It will recognize the human audio
    r = sr.Recognizer()
    sleep(0.1)
    with sr.Microphone(device_index=1, sample_rate=sample_rate, chunk_size=chunk_size) as source:
        # wait for 0.2 second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=0.1)
        # calling speak function to tell the user to say instruction
        if "Again Listening" not in instruction:
            Speak(instruction)
        sleep(0.10)
        # it will record/capture out audio
        audio = r.listen(source)
    try:
        # it is a google api
        # it will send the captured audio and send to google
        # in will return text as output
        text = r.recognize_google(audio)
        # this convert the string all characters lower case
        text = text.lower()
        # to print the instruction given by user
        print(text)
        return text
    except Exception:
        # some exception handling to handle the situation if we got exception while converitng audio to speech
        print("Unable to recognize you voice")
        return "none"
