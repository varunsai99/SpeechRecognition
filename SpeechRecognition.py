import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import time

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Varun!!")
        
    elif hour>=12 and hour<=17:
        speak("Good Afternoon Varun!!")
        
    else:
        speak("Good Night Varun")
        
    speak("How can I help You")




def takeCommand():
    
    r=sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=800
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("I can't recognize say that again please")
        return "None"
    
    return query



def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('******@gmail.com','**********')
    server.sendmail('*********@gmail.com',to,content)
    server.close()
    
def path_select(dir_name):
    if dir_name in ["conda",'c']:
        return 'C'
    elif dir_name in ["data",'d']:
        return 'D'
    elif dir_name in ["elephant",'e','energy','hi']:
        return 'E'
    elif dir_name in ['f','famous']:
        return 'F'
    else:
        return None

    
def opening_files():
    speak("In which directory")
    print("C:\nD:\nE:\nF:")
                
    while(True):
        
        dir_name=takeCommand()
        
        dir_name=path_select(dir_name)
        
        if dir_name in ['C','D','E','F']:            
            break
        
        else:
            speak("path is not in folder select again")
            
    dir_name+=':/'
    
    while(True):
        
        try:
            
            j=1
            for i in os.listdir(dir_name):
                
                print(j,i)
                j+=1
            speak("select id of a folder that you want to open")
                        
            while(True):
                try:
                    req = takeCommand()
                    
                    if int(req)<=j:
                        dir_name = os.path.join(dir_name,os.listdir(dir_name)[int(req)-1])
                        if dir_name.endswith('.mp4') or dir_name.endswith('.mp3') or dir_name.endswith('.pdf') or dir_name.endswith('.doc') or dir_name.endswith('.txt') or dir_name.endswith('.png') or dir_name.endswith('.jpeg') or dir_name.endswith('jpg'):
                            os.startfile(dir_name)
                            break
                        break
                    else:
                        speak("selected id is not in a folder please select again!")
                except:
                    speak("selected id is not in a folder please select again!")
                                
                
                        
        except:
            break

if __name__ == "__main__":
    
    while(True):
        query=takeCommand().lower()
        if 'max' in query:
            break
        else:
            speak("I think you are not Varun")
    if 'max' in query:
        
        wishme()
        while True:
            query=takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching in wikipedia")
                query=query.replace("wikipedia",'')
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                chromedir="C:\ProgramData\Microsoft\Windows\Start Menu\Programs/chrome.exe %s"
                webbrowser.get(chromedir).open("youtube.com")
                
            elif 'open google' in query:
                chromedir="C:\ProgramData\Microsoft\Windows\Start Menu\Programs/chrome.exe %s"
                webbrowser.get(chromedir).open("google.com")
                
            elif 'open stackoverflow' in query:
                chromedir="C:\ProgramData\Microsoft\Windows\Start Menu\Programs/chrome.exe %s"
                webbrowser.get(chromedir).open("stackoverflow.com")
                
            elif 'play music'in query:

                music_dir=r'D:\son'
                songs=os.listdir(music_dir)
                rand=random.randint(0,len(songs)-1)
                os.startfile(os.path.join(music_dir,songs[rand]))
                
            elif 'the time' in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir,thetime is {strtime}")
                     
            elif 'email to aditya' in query:
                try:
                    speak("What should I send")
                    content=takeCommand()
                    to='***********@gmail.com'
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)

            elif 'wait for sometime' in query:
                time.sleep(200)

            elif "whatsapp jarvis" in query:
                speak("I am doing my job!!")

            elif 'go to sleep' in query:
                speak("Okay! jith I am leaving..")
                break

            elif 'open a file' in query:
                opening_files()
            elif 'open your file' in query:
                opening_files()
            elif 'open my file' in query:
                opening_files()
            elif 'open file' in query:
                opening_files()
                    
             
