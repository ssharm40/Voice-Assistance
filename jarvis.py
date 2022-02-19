import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    elif hour>=16 and hour<20:
        speak("Good Evening!")   

    else:
        speak("Good Night!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ssharma86099@gmail.com', '************')
    server.sendmail('ssharma86099@gmail.com',to,content)
    server.close()
    speak("Mail Sent")

def msg():
    speak("What should I say?")
    content=takeCommand()
    return content


if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query or 'pedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                speak("One")
                print(query)
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                #print(results)
                speak(results)
            except Exception as e:
                speak("There Are Some issue")



        elif 'youtube' in query or 'tube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            speak("Opening Stack Oveflow")
            webbrowser.open("stackoverflow.com")   


        elif 'music' in query or 'song' in query :
            import random
            music_dir = 'E:\OLd Laptop\H drive\h\songs\Fvrt'
            songs = os.listdir(music_dir)
            speak("Playing Song..........")   
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query or 'visual studio' in query or 'vs' in query:
            codePath = "E:\Microsoft VS Code\Code"
            speak("Opening VS Code")
            os.startfile(codePath)

        elif 'microsoft' in query or 'micro' in query or 'soft' in query or 'word' in query or 'world' in query or 'excel' in query or 'sl' in query or 'point' in query or 'power' in query:
            speak("Please tell us name of specific software that you want to open : ")
            print('''
            Excel
            Word
            Power Point
            Access
            ''')
            sel=takeCommand().lower()
            if 'excel' in sel or 'sl' in sel or 'xl' in sel:
                speak("Opening Microsoft Excel")
                Path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007"
                os.startfile(Path)
            elif 'word' in sel or 'world' in sel :
                speak("Opening Microsoft Word")
                Path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007"
                os.startfile(Path)
            elif 'point' in sel or 'power' in sel :
                speak("Opening Microsoft Power Point")
                Path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007"
                os.startfile(Path)
            elif 'access' in sel:
                speak("Opening Microsoft Access")
                Path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Access 2007"
                os.startfile(Path)
            else:
                speak("Sorry, I did not get you")


        elif 'mail' in query or 'male' in query or 'mel' in query :
            speak("To whom you want to send the mail : ")
            d1={'Shubham':'ss86099@gmail.com','Apoorva':'apoorvasharma699@gmail.com','Shikha':'shikhamzn555@gmail.com'}
            l=d1.keys()
            for i in l:
                speak(i)
                print(i)
            nm=takeCommand().lower()
            if 'shubham' in nm or 'shu' in nm:
                content=msg()
                sendEmail(d1['Shubham'],content)
            elif 'apoorva' in nm or 'apporva' in nm or 'appu' in nm:
                content=msg()
                sendEmail(d1['Apoorva'],content)
            elif 'shikha' in nm or 'mini' in nm or 'minni' in nm:
                content=msg()
                sendEmail(d1['Shikha'],content)    
            else:
                speak("Sorry I did not get you.")
        elif 'internet' in query or 'speed' in query or 'test' in query:
            import speedtest
            st=speedtest.Speedtest()
            speak("Checking Speed")
            d=(st.download())/(1025*1025)
            u=(st.upload())/(1025*1025)
            d=round(d,2)
            u=round(u,2)
            speak("Downloading Speed is "+str(d)+"MBPS")
            speak("Uploading Speed is "+str(u)+"MBPS")
                
        elif 'quit' in query or 'exit' in query or 'bhar' in query:
            speak("Do you really want to Shut Down your PC ?")
            choice=takeCommand().lower()
            if 'yes' in choice or 'ha' in choice:
                speak("Logging  Of")
                os.system("shutdown /s /t 1")
            else:
                speak("Thankyou for using Jarvis, we will see you soon here")
                break
