import smtplib
from VoiceIO import Speak, takeCommand


# this function send e-mail
def sendEmail():
    # connecting to the server of gmail
    # creating a session with smtp server of google
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # first parameter is address/location  of google's smtp server and second it port number ..for google we use port
    # number 22
    server.starttls()
    # For security reasons,  putting the SMTP connection in the TLS mode. TLS (Transport Layer Security) encrypts all
    # the SMTP commands our e-mail id and password
    server.login('rkt574154@gmail.com', 'ydgxsufkukluayef')
    # email id of receiver
    Speak("Type the receiver email id")
    receiver = input("Enter the email-id of the receiver-:")
    # to take choice from user that he want to speak or type the message
    choice = takeCommand("Do you want to send the message by speaking or do you want to type")
    if ("speak" in choice) or ("speaking" in choice) or ("saying" in choice):
        subject = takeCommand("Speak the subject of the email")
        content = takeCommand("Speak  the message you want to send to the sender")
    else:
        Speak("Enter the subject of the email")
        subject = input("Enter the subject of the email-:")
        Speak("Type the message")
        content = input("Enter message : ")
    # sending the message
    server.sendmail("rkt574154@gmail.com", receiver, "Subject :{} \n\n {}".format(subject, content))
    # closing the connection
    server.close()
    Speak("email sent successfully")
