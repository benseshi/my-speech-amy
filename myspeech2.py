from gtts import gTTS
import requests
import time
import smtplib
from pygame import mixer
mixer.init()
import string
import webbrowser
import speech_recognition as sp
import os
import turtle

t=turtle.Pen()
t.left(90)
t.up()
t.forward(50)
t.right(145)
t.down()

t.forward(100)
t.left(145)
t.forward(150)
t.left(160)
t.forward(220)
t.right(145)
t.forward(220)
t.left(160)
t.forward(150)
t.left(145)
t.forward(120)
t.right(105)
t.forward(35)
t.up()
t.right(90)
t.forward(110)
t.left(150)
t.down()
t.forward(150)


#assigning the r value with speech recogniser
r=sp.Recognizer()
with sp.Microphone() as source:
    print("loading your virtual AI :P")
    r.adjust_for_ambient_noise(source,duration=1)
   
    tts=gTTS(text="master im AMY and im ready for your command",lang="en-us")
    tts.save("amy.mp3")
    mixer.music.load("amy.mp3")
    mixer.music.play()
    
    time.sleep(5)
    print("now listening")
    time.sleep(5)
    audio=r.listen(source)
   
#assing the value and instructions to open the value given as audio
    if "Wikipedia" in r.recognize_google(audio):
        
        tts=gTTS(text="master you selected Wikipedia",lang="en-us")
        tts.save("amy2.mp3")    
        mixer.music.load("amy2.mp3")
        mixer.music.play()
        time.sleep(3)
        r2=sp.Recognizer()
        url="https://en.wikipedia.org/wiki/"
        with sp.Microphone() as source:
            print("hey u selected wikipedia tell what i want to search")
            audio2=r2.listen(source)
            tts=gTTS(text="you asked me to search for ..."+r.recognize_google(audio2).lower()+" opening it please wait",lang='en-us')
            tts.save("amy1.mp3")
            mixer.music.load("amy1.mp3")
            mixer.music.play()
            time.sleep(1)

            try:
                print("friday thinks you said "+str(r2.recognize_google(audio2)))
                webbrowser.open_new(url+r2.recognize_google(audio2))
            except sp.UnknownValueError:
                print("fiday didnt get what you said")
               
            except sp.RequestError as e:
                print("friday unable reach request".format(e))
                
    
    #assigning the search with instructions 

    if "search" in r.recognize_google(audio):
       
        r.adjust_for_ambient_noise(source,duration=1)
        tts=gTTS(text="master you selected google search tell me what to search",lang="en-us")
        tts.save("amy7.mp3")
        mixer.music.load("amy7.mp3")    
        mixer.music.play()
        time.sleep(5)
        r7=sp.Recognizer()
        url7="https://www.google.co.in/"
        with sp.Microphone() as source:
        
            print("friday: opening google search")
            audio7=r7.listen(source)
            
            tts=gTTS(text="hey u selected google search"+r.recognize_google(audio7).lower()+"please wait while i process it",lang="en-us")
            tts.save("amy7_1.mp3")
            mixer.music.load("amy7_1.mp3")
            mixer.music.play()
            time.sleep(1)
            try:
                print("the word you want to search in google :"+r7.recognize_google(audio7))
                webbrowser.open_new.lower(url7+r7.recognize_google(audio7))
            except sp.UnknownValueError:
                print("friday cant get u said in google")
            except sp.RequestError as e:
                print("friday is not reachable ".format(e))

    #assining the hotels value with speech recognizer
            
    if "hotels" in r.recognize_google(audio):
        r.adjust_for_ambient_noise(source,duration=1)
        tts=gTTS(text="master you selected to search hotels",lang="en-us")
        tts.save("amy2.mp3")
        mixer.music.load("amy2.mp3")
        mixer.music.play()
        time.sleep(3)

        r1=sp.Recognizer()
        url1="https://en.wikipedia.org/wiki/"
        with sp.Microphone() as source:
            print("hey u selected restaurents tell what i want to search")
            audio1=r1.listen(source,timeout=1,phrase_time_limit=10)
            r.adjust_for_ambient_noise(source,duration=1)
            tts=gTTS(text="im opening hotels near"+r.recognize_google(audio1)+"so please wait",lang="en-us")
            tts.save("amy1.mp3")
            mixer.music.load("amy1.mp3")
            mixer.music.play()
            time.sleep(0.5)

            try:
                print("friday thinks you said "+r1.recognize_google(audio1))
                webbrowser.open_new(url1+r1.recognize_google(audio1))
            except sp.UnknownValueError:
                print("fiday didnt get what you said")
            except sp.RequestError as e:
                print("friday unable reach request".format(e))

            
        


    #assigning the location value with instructions
    if "where Am I" or "my location" in r.recognize_google(audio):
        r3=sp.Recognizer()
        r3.adjust_for_ambient_noise(source,duration=1)
        url3='https://mycurrentlocation.net/'
        with sp.Microphone() as source:
            tts=gTTS(text="make sure you turned your GPS on",lang="en-us")
            tts.save("amy3.mp3")
            mixer.music.load("amy3.mp3")
            mixer.music.play()
            print(" friday :location is loading wait")
           
            try:
                print("your loaction is loading")
                webbrowser.open_new(url3)
            except sp.UnknownValueError:
                print("friday checking your server can be reached")
            except sp.RequestError as e:
                print("error has occured".format(e))
    #assining the value to open mail
    if "mail" in r.recognize_google(audio):
        r4=sp.Recognizer()
        r4.adjust_for_ambient_noise(source,duration=1)
        with sp.Microphone() as source:
            print("friday :intialising gmail ")
            audio4=r4.listen(source,timeout=1,phrase_time_limit=10)
            tts=gTTS(text="you selected mail please say which kind of mail to access",lang="en-us")
            tts.save("amy4.mp3")
            mixer.music.load("amy4.mp3")
            mixer.music.play()
    if "gmail" in r.recognize_google(audio4):
            tts=gTTS(text="you selected to open gmail",lang="en-us")
            tts.save("amy4_1.mp3")
            mixer.music.load("amy4_1.mp3")
            mixer.music.play()
            r4=sp.Recognizer()
            mail=smtp.lib.SMTP('smtp.gmail.com')
            mail.ehlo()
            mail.starttls()
            mail.login('bentenseshu@gmail.com')
            mail.sendmaiil(r.recognise_google(audio),content)
    elif "outlook"in r.recognize_google(audio4):
            tts=gTTS(text="you asked to open the outlook",lang="en-us")
            tts.save("outlook.mp3")
            mixer.music.load("outlook.mp3")
            mixer.music.play()
            time.sleep(0.3)
            print("done!")
    try:
        print("friday:gmail is opening wait"+r4.recognize_google(audio4))
        webbrowser.open_new(url4)
    except sp.UnknownValueError:
        print("friday cant search it")
    except sp.RequestError as e:
        print("friday cant reach url".format(e))

    #assinging the value to open facebook
    if "Facebook" in r.recognize_google(audio):
        r5=sp.Recognizer()
        r.adjust_for_ambient_noise(source,duration=1)
        url5='https://en-gb.facebook.com'
        with sp.Microphone() as source:
            print("friday:u selected for fb right?")
            audio5=r5.listen(source,timeout=1,phrase_time_limit=10)
            try:
                print("your fb is loadiing")
                webbrowser.open_new(url5)
            except sp.UnknownValueError:
                    
                print("friday cant understandyou")
            except sp.RequestError as e:
                print("friday cant reach the page".format(e))

    #assingning values to open microsoft.com
    if "Microsoft" in r.recognize_google(audio):
        r6=sp.Recognizer()
        r6.adjust_for_ambient_noise(source,duration=1)
        url6='https://www.microsoft.com/en-in/'
        with sp.Microphone() as source:
            print("friday: accessig microsoft server")
            try:
                print("friday :opening microsoft")
                webbrowser.open_new(url6)
            except sp.UnknownValueError:
                print("friday cant understand")
            except sp.RequestError as e:
                print("friday cant reach server".format(e))

    #assining the value to open weather report
    if "Weather" in r.recognize_google(audio):
        r8=sp.Recognizer()
        r.adjust_for_ambient_noise(source,duration=1)
        url8="https://www.msn.com/en-us/weather"
        with sp.Microphone as source:
            print("friday: accesing weather report")
            audio8=r8.listen(source,timeout=1,phrase_time_limit=10)
            try:
                print("friday thinks you said"+r8.recognize_google(audio8))
                webbrowser.open_new(url8+r8.recognize_google(audio8))
            except sp.UnknownValueError:
                print("friday cant recognize what you said")

            except sp.RequestError:
                print("friday unable to reach the website")
    #asssining the value to open the browser
    if "Share it" in r.recognize_google(audio):
        r9=sp.Recognizer()
        r.adjust_for_ambient_noise(source,duration=1)
        tts=gTTS(text="im opening the SHAREit app please wait")
        tts.save("share.mp3")
        mixer.music.load("share.mp3")
        mixer.music.play()
        with sp.Microphone() as source:
            print("friday recognising what you said")
            audio9=r9.listen(source,timeout=1,phrase_time_limit=10)
            try:
                print("friday is opening shareit")
                f=os.startfile('C:\\Program Files (x86)\\SHAREit Technologies\\SHAREit\\SHAREit.exe')
            except sp.UnknownValueError:
                print("friday cant recognise what you said"+f)
            except sp.RequestError:
                print("fridat cant reach to what you said".format(e))
    #assigning the value to open explorer
    if "explorer" in r.recognize_google(audio):
        r10=sp.Recognizer()
        r.adjust_for_ambient_noise(source,duration=1)
        with sp.Microphone() as source:
            print("friday: recognising what you said")
            audio10=r10.listen(source,timeout=1,phrase_time_limit=10)
            try:
                print("friday opening what you said")
                tts=gTTS(text="maser you just selected explorer and im opening it")
                tts.save("amy10.mp3")
                mixer.music.load("amy10.mp3")
                mixer.music.play()
            except sp.UnknownValueError:
                print("friday cant understand your command")
            except sp.RequestError as e:
                print("friday cant reach what you asked".format(e))
    if "my facebook" in r.recongnieze_google(audio):
        r11=sp.Recognizer()
        r.adjust_for_ambient_noise(source,duration=1)
        with sp.recognizer as source:
            print("you selected fb login")
            audio11=r.listen(source,timeout=1,phrase_time_limit=10)
            
            
                
            
   
    
    '''if "" in r.recognize_google(audio):
        r12.sp.recognizer()
        r.adjust_for_ambient_noise(source,duration=1)
        with sp.Microphone as source:
            print("you selected ")
            tts.gTTS(text="master you selected ")
            tts.save("amy11.mp3")
            mixer.music.load("amy11.mp3")
            mixer.music.play()
            audio11=r11.listen(source,timeout=1,phrase_time_limit=10)
        try:
            print("im opening"+text="")
        except sp.UnknownValueError:
            print("error")
        except sp.RequestError:
            print("error")'''
             
