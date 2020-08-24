# Voice Speech Assistant (version 0.1)
from tkinter import *
import speech_recognition as sr
import webbrowser as web
import wikipedia
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


# Root Window
app = Tk()
# Change assistants name here..
assistant_name = 'Emma'
win_size = '320x140+0-34'
# Change Default Colors
bg_color = '#296296'
fg_color = '#fff'

# --- FUNCTIONS ---

# Search Wikipedia
def search_wiki(mic=False):

    voice_assistant('What will I search wikipedia 4')

    # Initialize Speech Recognition
    rec = sr.Recognizer()

    with sr.Microphone() as user_input:
        # rec.adjust_for_ambient_noise(user_input)
        
        if mic:
            voice_assistant(mic)
            
        audio = rec.listen(user_input, phrase_time_limit = 5)
        
        searched_wiki_for = ''
        
        try:
            searched_wiki_for = rec.recognize_google(audio)
        except sr.UnknownValueError:
            voice_assistant("Sorry, I didn't get that!")
        except sr.RequestError:
            voice_assistant("Sorry, I've got a sore throat!")


    results = wikipedia.summary(searched_wiki_for, sentences = 1)
    voice_assistant(results)


# Search the Internet
def search_internet(mic=False):

    voice_assistant('What will I search the internet 4')

    # Initialize Speech Recognition
    rec = sr.Recognizer()

    with sr.Microphone() as user_input:
        # rec.adjust_for_ambient_noise(user_input)
        
        if mic:
            voice_assistant(mic)
            
        audio = rec.listen(user_input, phrase_time_limit = 5)
        
        searched_internet_for = ''
        
        try:
            searched_internet_for = rec.recognize_google(audio)
        except sr.UnknownValueError:
            voice_assistant("Sorry, I didn't get that!")
        except sr.RequestError:
            voice_assistant("Sorry, I've got a sore throat!")


    responded(searched_internet_for)

# Microphone for: General input/output
def open_mic(mic=False):
    
    phrase = ['how can I help you?', \
              'hey there! what\'s your query?', \
              'yes mate?']
    
    x = random.choice(phrase)
    voice_assistant(x)

    # Initialize Speech Recognition
    rec = sr.Recognizer()

    with sr.Microphone() as user_input:
        # rec.adjust_for_ambient_noise(user_input)
        
        if mic:
            voice_assistant(mic)
            
        audio = rec.listen(user_input, phrase_time_limit = 5)
        
        asked_query = ''
        
        try:
            asked_query = rec.recognize_google(audio)
        except sr.UnknownValueError:
            voice_assistant("Sorry, I didn't get that!")
        except sr.RequestError:
            voice_assistant("Sorry, I've got a sore throat!")


    response(asked_query)


# Voive Assistant Audio Responses
# Save audio to file / Play audio from file / Delete file
def voice_assistant(audio_string):
    
    tts = gTTS(text=audio_string, lang='en', slow=False)
    r = random.randint(1, 1000000)
    filename = 'audio-' + str(r) + '.mp3'
    
    tts.save(filename)
    playsound.playsound(filename)
    
    os.remove(filename)


# Respond to Internet Searches
def responded(searched_internet_for):
    
    url = 'https://duckduckgo.com/?q=' + searched_internet_for
    web.get().open(url)
    voice_assistant('ok! Opening ' + searched_internet_for)


# Respond to User Input/Output
def response(asked_query):

    # --- WIKI QUERIES ---
    if 'wiki' in asked_query \
       or 'wikipedia' in asked_query:
        search_wiki()

    # --- INTERNET SEARCHES ---
    if 'search' in asked_query \
       or 'internet' in asked_query \
       or 'search the internet' in asked_query:
        search_internet()
    

    # --- GENERAL QUESTIONS TO ASSISTANT ---
    
    if 'what is your name' in asked_query \
       or 'what\'s your name' in asked_query:
        voice_assistant('My name is ' + assistant_name + '!')

    if 'how old are you' in asked_query \
       or 'what\'s your age' in asked_query:
        voice_assistant('you shouldn\'t ask a lady that!')

    if 'how are you' in asked_query \
       or 'how you doing today' in asked_query \
       or 'how are you doing' in asked_query \
       or 'how are you doing today' in asked_query \
       or 'how\'s things with you today' in asked_query:
        voice_assistant('All good today, thanks for asking!')

    if 'tell me about yourself' in asked_query \
       or 'what can you do' in asked_query \
       or 'who are you' in asked_query \
       or 'help' in asked_query:
        voice_assistant('Hi! I\'m ' + assistant_name + '! '\
                        'Your personal voice assisant, to help you with your queries. '\
                        'I can open apps, browse the internet, '\
                        'like open your favorite shopping websites. '\
                        'You can even ask me the time. '\
                        'I can open a location on the map, '\
                        'calculate sums, and lot\'s more. Have fun!')
    
    
    if 'what is the time' in asked_query \
       or 'what\'s the time' in asked_query \
       or 'what time is it' in asked_query:
        voice_assistant('Umm! let me think! The time is ' + ctime())

    if 'who\'s the boss' in asked_query \
       or 'who\'s in charge' in asked_query \
       or 'who\'s the best' in asked_query:
        voice_assistant('Well! I am, because you need me to assist you.')

    if 'who built you' in asked_query \
       or 'who created you' in asked_query:
        voice_assistant('I was created by Home Of Coding')

    if 'can you drive' in asked_query:
        voice_assistant('I can drive you mad!')
    
    if 'can you drive a car' in asked_query:
        voice_assistant('No, I can\'t drive a car, ' \
                       'but there are autonomous vehicles out there now!' \
                       'They are self driving cars that are safer than humans')


    # --- JOKES ---

    if 'tell me a joke' in asked_query \
       or 'tell me another joke' in asked_query:
        phrase = ['Bixby', \
                  'Siri', \
                  'Cortarna', \
                  'You think you can code']
        
        x = random.choice(phrase)
        voice_assistant(x)
    

    # --- OPEN APPS ---
    
    if 'notes app' in asked_query \
       or 'notes' in asked_query \
       or 'open notes' in asked_query:
        filename = 'C:/Program Files/Notepad++/notepad++.exe'
        os.startfile(filename)
        voice_assistant('ok! opening Notes App')
    

    # --- OPEN WEBSITE LINKS ---

    if 'Argos' in asked_query:
        url = 'https://www.argos.co.uk/'
        web.get().open(url)
        voice_assistant('ok! opening argos')
    
    if 'Twitter' in asked_query:
        url = 'https://www.twitter.com/'
        web.get().open(url)
        voice_assistant('ok! opening twitter')

    if 'John Lewis' in asked_query:
        url = 'https://www.johnlewis.com/'
        web.get().open(url)
        voice_assistant('ok! opening john lewis')

    if 'Marks and Spencer' in asked_query:
        url = 'https://www.marksandspencer.com/'
        web.get().open(url)
        voice_assistant('ok! opening marks and spencer')


    # --- EXIT-APP COMMANDS ---
    
    if 'exit' in asked_query \
       or 'close' in asked_query \
       or 'quit' in asked_query \
       or 'sleep' in asked_query:
        voice_assistant('ok! closing app')
        exit()
        app.destroy()
    
    if 'shut up' in asked_query:
        voice_assistant('that\'s rude! closing app')
        exit()
        app.destroy()
    
    if 'goodbye' in asked_query:
        voice_assistant('ok! goodbye!')
        exit()
        app.destroy()


# --- GUI ---

# Button Frame for Microphone
mic_frame = Frame(app, bg=bg_color)
mic_frame.pack(side='right', fill='x')

# Microphone Button
mic_photo = PhotoImage(file='images/mic.png')
mic_btn = Button(mic_frame, image=mic_photo, \
                 bg=bg_color, border=0, relief='flat', command=open_mic)
mic_btn.pack(side='right', padx=(0, 50), pady=20)

# Frame for Profile Image and Text
profile_frame = Frame(app, bg=bg_color)
profile_frame.pack(side='left', fill='x')

# Profile Image Label
profile_photo = PhotoImage(file='images/profile.png')
profile_label = Label(profile_frame, image=profile_photo, bg=bg_color, border=0)
profile_label.pack(padx=(50, 0), pady=(20, 0))

# Ask Anna Label
s_label = Label(profile_frame, text=('Ask ' + assistant_name), bg=bg_color, fg=fg_color, font=('arial', 8))
s_label.pack(padx=(50, 0))

# --- ROOT DEFAULTS ---
if __name__ == '__main__':
    app.title(assistant_name + ' Assistant')
    app.geometry(win_size)
    app.resizable(False, False)
    app.iconbitmap('images/mic.ico')
    app.configure(bg=bg_color)
    app.mainloop()
