#noinspection PyUnresolvedReferences
import pandas as pd
#noinspection PyUnresolvedReferences
import numpy as np
#noinspection PyUnresolvedReferences
import xlrd
#noinspection PyUnresolvedReferences
import time
#noinspection PyUnresolvedReferences
import datetime as dt
#noinspection PyUnresolvedReferences
import timedelta as td



#category = []
def load_data():
    print("Welcome to ShakeItUpSchedule. \n Please make sure the excel file includes the following categories in the columns: \n Serial Number, Event Title, Event Description, Day, Location, Start Time, End Time, and Categories")
    filename = input("Enter the path of the excel file: ")
    global df
    df = pd.read_excel(filename)
    print(df)
    b = []
    category = ["Artist Alley", "Dealer's Room", "Featured Panels", "Arcade", "Manga Library", "Contest", "Console Game", "Guests", "Panel", "Concert"]
    for x in category:
        a = input("Are you interested in participating in " + str(x) + "?")
        b.append(a)
    return df
def day_time():
    day = int(input("How many days of the event are you planning to attend?"))
    print(day)

    a = 1
    global dateofday
    global dateofdaya #creates list of dates
    global start_time
    global start_timea
    global end_timea
    global end_time
    start_timea = [] #creates list of start time
    end_timea = []   #creates list of end time
    for x in range(0, day):
        while True:
            try:
                dateofday = input("What date is it on day " + str(x+1) + "? (in MM/DD/YYYY format)")
                dateofday = dt.datetime.strptime(dateofday,"%m/%d/%Y")
                append.dateofdaya(dt.date.strftime(dateofday,"%m/%d/%Y"))
            except:
                print("\nERROR! Please enter the date of day " + str(x+1) +" in MM/DD/YYYY format. \nPossible Errors may include:\n- Missing slashes\n")
                continue
            break
    for x in range(0, day):
        while True:
            try:

                start_time = input("Enter your arrival time in HH:MM format for day "+ str(x+1)+ ":")
                start_time= dt.datetime.strptime(start_time,"%H:%M")
                if start_time.strftime('%H:%M'):
                    while True:
                        try:
                            end_time = input("Enter your end time in HH:MM format for day "+ str(x+1)+ ":")
                            end_time= dt.datetime.strptime(end_time,"%H:%M")
                            dur = end_time - start_time
                            if dur > dt.timedelta(0) :
                                start_timea.append(start_time.strftime('%H:%M'))
                                end_timea.append(end_time.strftime('%H:%M'))

                            else:
                                print("Duration Error!")
                                continue
                            break

                        except:
                            print("ERROR! Please enter the arrival time in HH:MM in 24-hour format. \nPossible Errors may include:\n- Missing Colons\n- Program does not accept AM/PM (must be in 24 hour format)\n")
                            continue
                        break
            except:
                print("ERROR! Please enter the arrival time in HH:MM in 24-hour format. \nPossible Errors may include:\n- Missing Colons\n- Program does not accept AM/PM (must be in 24 hour format)\n")
                continue
            break
    print("\n\n")
    print ("Arrival Time: ", start_timea)
    print ("End Time: ", end_timea)
    print("\n Noted. \n")

    return start_time
    return end_time
"""
    for x in range(0, day):
        while True:
            try:
                end_time = input("Enter your expected end time in HH:MM format for day "+ str(x+1)+":")
                end_time = dt.datetime.strptime(end_time,"%H:%M")
                if end_time.strftime('%H:%M'):
                    if
                    end_timea.append(end_time.strftime('%H:%M'))
                    print (end_timea)
                    print("\n Noted. \n")
            except:
                print ("ERROR! Please enter the start time in HH:MM format in 24-hour format.  \nPossible Errors may include:\n- Missing Colons\n- Program does not accept AM/PM (must be in 24 hour format)\n")
            break
"""

def event_on():
    filename = input("Enter the path of the excel file: ")
    df = pd.read_excel(filename)
    print(df["Start Time"])


    print(start_time)



def createSched():



    feature_panel == 5
    contest ==4
    concert == 3
    artist_alley == 2
    dealer_room == 2
    arcade == 2
    manga_library == 2
    maid_cafe == 2
    panel == 1




#load_data()
day_time()
#createSched()
event_on()
