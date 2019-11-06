import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser as wb
import smtplib
import random
import shutil
import json,requests
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



#Enabling Jarvis to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Jarvis wish according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning!")
    elif 12<=hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening")
    speak("Hello! I am Jarvis. How may i help you")

#Takes input from user from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.8
        r.energy_threshold = 700
        #r.energy_threshold = 700
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en')        
        print('You: ',query)
        speak(query)
    except Exception as e:
        #print(e)
        print("Say again")
        speak("Say again")
        return "None"
    return query

#Copy one file to another folder
def fileCopy(sour , dest):    
    new_path = shutil.copy(sour,dest)        
    speak("Transfer Successful")

def copi_d():
    speak("Enter destination")
    dest = takeCommand().lower()
    while dest=='none':
        dest = takeCommand().lower()    
    li1=dest.split(" ")
    print(li1)
    if li1[0]=='app' or li1[0]=='f' or li1[0]=='apps':
        li1[0]='f:'
    elif li1[0]=='see' or li1[0]=='she' or li1[0]=='shri' or li1[0]=='c':
        li1[0]='c:'
    elif li1[0]=='ji' or li1[0]=='g':
        li1[0]='g:'
    elif li1[0]=='dp' or li1[0]=='di' or li1[0]=='de' or li1[0]=='dee' or li1[0]=='dree' or li1[0]=='d':
        li1[0]='d:'
    elif li1[0]=='in' or li1[0]=='n' or li1[0]=='e':
        li1.insert(0,'e:')            
    for i in range(len(li1)):
        if li1[i]=='in' or li1[i]=='n':
            li1[i]='/'            
    if len(li1)==1:
        li_dt=''.join(li1)
        li_dt+='/'
    else:
        li_dt=''.join(li1)
    print(li_dt)
    if os.path.isdir(li_dt)==False:
        copi_d()
    else:
        return li_dt

def copi_s():
    di=['jpg','txt','doc','jpeg','png','pdf','ppt','py','cpp','c','java','class','mp3','mp4','avi']
    speak("Enter source path")
    sour = takeCommand().lower()
    print(sour)
    li=sour.split(" ")
    print(li)
    if li[0]=='app' or li[0]=='f' or li[0]=='apps':
        li[0]='f:'
    elif li[0]=='see' or li[0]=='she' or li[0]=='shri' or li[0]=='c':
        li[0]='c:'
    elif li[0]=='ji' or li[0]=='g':
        li[0]='g:'
    elif li[0]=='dp' or li[0]=='di' or li[0]=='de' or li[0]=='dee' or li[0]=='dree' or li[0]=='d':
        li[0]='d:'
    elif li[0]=='in' or li[0]=='n' or li[0]=='e':
        li.insert(0,'e:')
    for i in range(len(li)):
        if li[i]=='in' or li[i]=='n':
            li[i]='/'
    print(li)        
    li.insert(len(li)-1,'.')
    li_st=''.join(li)
    print(li_st)
    if os.path.isfile(li_st)==False:
        copi_s()
    else:
        return li_st    

def Weather():
    api_key = "ba50fd2d95272750ddb2eedc4ff51d61"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    speak("Enter city name if possible with country code")
    city_name = takeCommand().lower()
    # city_name = input("Enter city name: ")

    complete_url = base_url +  "q=" + str(city_name) + "&appid=" + api_key + "&units=metric"

    response = requests.get(complete_url)
    x = response.json()
    #print(x)
    if x["cod"] != "404":
        y = x["main"]
        curr_temp = y["temp"]
        curr_pressure = y["pressure"]
        curr_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        country = x['sys']['country']
        print("Present weather in "+city_name+","+country)
        speak("Present weather in "+city_name+","+country)
        print(" Temperature = " +
                        str(curr_temp) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(curr_pressure) +
            "\n humidity (in percentage) = " +
                        str(curr_humidity) +
            "\n description = " +
                        str(weather_description)) 
        speak(" Temperature = " +
                        str(curr_temp) + "degree celsius"
            "\n atmospheric pressure (in hPa unit) = " +
                        str(curr_pressure) +
            "\n humidity= " +
                        str(curr_humidity) + "percent"
            "\n description = " +
                        str(weather_description))     
    else: 
        print(" City Not Found ") 
        speak(" City Not Found ") 

if __name__ == '__main__':
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    wb.register('google-chrome',None,wb.BackgroundBrowser(chrome_path))
    # print('Hi')
    #speak("Good morning tarushi how are you")
    wishMe()    
    # chatbot=ChatBot('Jarvis')
    # trainer=ChatterBotCorpusTrainer(chatbot)
    # tainer.train("chatterbot.corpus.english")    
    while True:
        query = takeCommand().lower()
        if query != "None":
            speak(query)

        if 'play music' in query:
            speak("Playing Music")
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            random.shuffle(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'wikipedia' in query:
            print("Searching Wikipedia")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open google' in query:
            wb.get('google-chrome').open_new('google.com')

        elif 'open youtube' in query:
            wb.get('google-chrome').open('youtube.com')

        elif 'open whatsapp' in query:
            wb.get('google-chrome').open('web.whatsapp.com')

        elif 'open codechef' in query:
            wb.get('google-chrome').open('codechef.com')                

        elif 'copy file' in query:
            source=copi_s()
            destination=copi_d()
            fileCopy(source,destination)
        
        elif 'weather' in query:
            Weather()
                
        elif 'quit' in query:
            speak("Exiting from Jarvis")
            exit()

        # else:
        #     response=trainer.get_response(query)
        #     print('Jarvis: ',response)
        #     speak(response)            


