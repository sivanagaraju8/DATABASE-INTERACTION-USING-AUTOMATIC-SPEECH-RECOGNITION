  
'''
--------------------------
@ Author: Gamidi Siva Nagaraju
--------------------------
'''
#!/usr/bin/python3

#import necessary Python modules
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import mysql.connector as sql
import random
import pandas as pd


def speak(text):
    tts = gTTS(text=text, lang="en",slow = False)
    filename = str(random.choice(list(text)))+str(random.randint(1,100))+".mp3"
    tts.save(filename)
    playsound.playsound(filename)

def connection(status):
    if status:
        resp=("Yes! your Connection Estabilished .\n"
              "Now go head to explore your data world ! \n")
        print(resp)
        speak(resp)
        print(commands)
    else:
        print("There is a problem with Data Server, I am unable to reach it.")
        speak("There is a problem with Data Server, I am unable to reach it.")        
        exit(0)
def db_connect():
    try:

        db_connection = sql.connect(host='localhost', database='', user='root', password='ecell123')
        if db_connection:
            return(db_connection)
        else:
            # resp="Oh! sorry, something went Wrong! while estabilshing the Connection with Database"
            # print(resp)
            # speak(resp)
            return(False)
        
    except:
        connection(False)

def query_engine(query):
    
    def show_dbs():
            if 'connect to database'  not in recorded:
                speak('Please wait ! I am estabilishing secure connection to database !')
                print('Please wait ! I am estabilishing secure connection to database !')
                if db_connect() :
                    recorded.append('connect to database')
                    sce=db_connect()
                    db_cursor = sce.cursor()    
                    db_cursor.execute('show databases')
                    table_rows = db_cursor.fetchall()
                    df = pd.DataFrame(table_rows)
                    speak("Here is the list of Databases available in your store. ")
                    print(df)
                    return df.values.tolist()
            else:
                if db_connect() is not False:
            #global db_connection
                    sce=db_connect()
                    db_cursor = sce.cursor()    
                    db_cursor.execute('show databases')
                    table_rows = db_cursor.fetchall()
                    df = pd.DataFrame(table_rows)
                    speak("Here is the list of Databases available in your store. ")
                    print(df)
                    return df.values.tolist()
                else:
                    exit(0)
    def db_select():
        rows=show_dbs()
        l=[]
        for i in range(len(rows)):
            l.append(rows[i][0])
        #print("rows",l)
        print("Please Select any one of the given databases")
        speak("You can select any one of the given databases")
        return l
    def db_selected():
        rows=db_select()
        for i in range(5):
            dbname=ask()
            #print(rows)
            if dbname in  rows :
                print("Yes ,", dbname, " Database is in given list !")
                speak("Yes ,"+ dbname + " Database is in given list !")
                break
            else:
                print(dbname, " Not matched in given databases list")
                speak(dbname+ " Not matched in given databases list")

        db_connection2 = sql.connect(host='localhost', database=dbname, user='root', password='ecell123') 
        if db_connection2:
            print("{} Selected. Now you can access the TABLES".format(dbname))
            speak(str(dbname)+ " Selected . Now you can access the TABLES. ")
            return db_connection2, dbname
    def show_tables():
        conn,dtbname=db_selected()
        if conn is not False:
            #global db_connection
                    
                    db_cursor = conn.cursor()    
                    db_cursor.execute('show tables')
                    table_rows1 = db_cursor.fetchall()
                    df1 = pd.DataFrame(table_rows1)
                    speak("Here is the list of Tables available in "+ dtbname+ " Database.")
                    print(df1)
                    return df1.values.tolist(),conn
        else:
                    exit(0)        

    if query == 'connect to database':
        if query not in recorded:
            if db_connect():
                connection(True)
                recorded.append(query)
        else:
            print(' Hey! Cool. I already did that :)- ')
            speak(' Hey! Cool. I already did that !')

    if query == 'show databases':
        show_dbs()
    if query == 'select database':
        db_selected()
    if query == "show tables":
        show_tables()
    if query =='show table data':
        table,conn=show_tables()
        tables=[]
        for i in range(len(table)):
            tables.append(table[i][0])
        print("tables",tables)
        for i in range(5):
            tbname=ask()
            #print(rows)
            if tbname in  tables :
                print("Right! ", tbname, " table is in given list")
                speak("Right! "+tbname+" Table is in given list")
                break
            else:
                print(tbname," Not matched in given Tables list")
                speak(tbname +" Not matched in given Tables list")

        db_cursor = conn.cursor() 
        qry= 'select * from '+tbname
        db_cursor.execute(qry)
        table_rows2 = db_cursor.fetchall()
        df2 = pd.DataFrame(table_rows2)
        speak("Here is the Data of the "+ tbname+" Table available in your database.")
        print(df2)
    return query 


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


instructions = (
        "Hi There! I am your Database Interaction Voice Assistant:\n"
        
        "I love to help you to get the data avaliable in Database storages.\n"
        "I'm pleased to say, You can check the following example instructions.\n "
    )

commands=(
    " --- Connect to Database \n"
    " --- Show Databases \n"
    " --- Select Database [Name] \n"
    " --- Show TABLES \n"
    " --- Show TABLE Data \n"
    " --- Say abort or end or terminate to exit \n"
    )
# show instructions and wait 2 seconds before starting the game

print(instructions)
print(commands)
speak(instructions)
#db_connect()
time.sleep(2)

def ask () :
    recognizer1 = sr.Recognizer()
    microphone1 = sr.Microphone()
    for j in range(5):
            speak("I'm Listening ....")
            print("Speak : I'm Listening .... for Table/DB Name ")
            guess = recognize_speech_from_mic(recognizer1, microphone1)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            speak("Sorry. I didn't catch that. What did you say?")
            print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
    if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            exit()
        # show the user the transcription
    print("You said: {}".format(guess["transcription"]))
    return(guess['transcription'].lower())
if __name__ == "__main__":           
    recorded=[]
    queries=[ 'connect to database',
        'show databases',
        "select database",
        "show tables",
        "show table data"]
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:

        for j in range(5):
            speak("Please Speak. I'm Listening ....")
            print("Speak {}. I'm Listening .... ".format(j+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            speak("Sorry. I didn't catch that. What did you say?")
            print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        if guess["transcription"] is not None:
            guess_is_correct = guess["transcription"].lower() in queries # "Connect to Database".lower()
            if guess["transcription"].lower()  in ('abort', 'end', 'terminate'):
                speak( " Thanks for Using. Have a Good day !")
                print( " Thanks for Using. Have a Good day !")
                break
        if guess_is_correct:
            txt=query_engine(guess["transcription"]) + " Task Achieved successfuly !"
            print(txt)
            speak(txt)
        else:
            print("Sorry, I can't perform what you have said . Please try again! ")#.format(word))
            speak("Sorry, I can't perform what you have said . Please try again!")
