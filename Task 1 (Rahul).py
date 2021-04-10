import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from requests import get

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#pprint(voice[0].id)
engine.setProperty('voice', voice[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")
       
    speak("I am Rahul sir. Please tell me how can I assist you. It will be an honour for me to assist you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: ,{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('rahulmondal2468@gmail.com','Rahul_mondal12345')
    server.sendmail('rahulmondalhit@gmail.com',to,content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        
        elif 'open facebook'in query:
            webbrowser.open("facebook.com")

        elif 'open google'in query:
            webbrowser.open("google.com")


        elif 'open stack overflow'in query:
            webbrowser.open("stackoverflow.com")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif 'play music'in query:
            music_dir = 'E:\MP3'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email to rahul' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "rahulmondalhit@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to rahul")

            except Exception as e:
                print(e)
                speak("sorry sir, I am not able to sent this mail to rahul")