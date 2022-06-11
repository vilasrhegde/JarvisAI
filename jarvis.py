import datetime
import sys
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from datetime import date

print('Jarvis Activated.')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak('Good Morning!')
    elif(hour >=12 and hour <18):
        speak('Good Afternoon!')        
    else:
        speak('Good Evening!')    
    # speak("I'm Jarvis. How can I help you?")    

def  takeCommand():
    #takes mic input returns string object
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # r.energy_threshold = 300 
        r.pause_threshold = 1 #after 1sec delay pause taking input
        audio = r.listen(source)

    try:
        print('Recognising...')        
        query = r.recognize_google(audio)
        print(f"User said: {query}\\n")

    except Exception as e:
        # print(e)
        print('Say that agian please :>')
        return 'None'        
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('19c36@sdmit.in','sdmit@123')
    server.sendmail('19c36@sdmit.in',to,content)

def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age
if __name__ == '__main__':
    # speak('Vilas is genius!')
    wishMe()

    while True:
        query = takeCommand().lower()
        # Logic for executing task

        try:
            if 1:
                if 'wikipedia' in query:
                    
                        speak('Searching Wikipedia...')
                        query = query.replace('wikipedia', '')
                        results = wikipedia.summary(query,sentences = 2)
                        speak('According to wikipedia')
                        print(results)
                        speak(results)

                elif 'open youtube' in query:
                    webbrowser.open('youtube.com')
                elif 'open google' in query:
                    webbrowser.open('google.com')    
                elif 'open stack overflow' in query:
                    webbrowser.open('stackoverflow.com')   
                elif 'music' in query:
                    webbrowser.open('https://open.spotify.com/?utm_source=pwa_install')                  
                elif 'play song' in query:
                    music_dir = 'C:\\Users\\vilas\\Music'    
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif 'time' in query:
                    strtime = datetime.datetime.now().strftime('%H:%M:%S')
                    speak(f'Time is {strtime}')
                elif 'open code' in query:
                    vs_path = "C:\\Users\\vilas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(vs_path)
                elif 'search' in query:
                    q = query[7:]
                    webbrowser.open(f'google.com/search?q={q}')                    
                elif 'exit' in query:
                    sys.exit()

                elif 'send email' in query:
                    try:
                        print('What sould I write?')
                        speak('What should I write?')
                        content = takeCommand()
                        to = 'vilashegde36@sdmit.in'
                        sendEmail(to,content)
                        speak('Email has been sent!')
                    except Exception as er:
                        print(er)
                elif 'my age' in query:
                    print("Vilas, your age is",calculateAge(date(2001,5,23)))
                    speak(f'Vilas, your age is {calculateAge(date(2001, 5, 23))}')       
                   

        except Exception as e:
            print('Ah..Crap!')


