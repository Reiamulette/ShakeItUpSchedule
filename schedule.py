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



def load_data():
    print("Welcome to ShakeItUpSchedule. \n Please make sure the excel file includes the following categories in the columns: \n Serial Number, Event Title, Event Description, Day, Location, Start Time, End Time, Moderator, and Categories")
    filename = input("Enter the path of the excel file: ")
    df = pd.read_excel(filename)
    print(df)

def day_time():
    day = int(input("How many days of the event are there?"))
    print(day)
    a = 1
    start_timea = []
    end_timea = []
    for x in range(0, day):
        try:
            start_time = input("Input Beginning Time in HH:MM format for day:")
            start_time= dt.datetime.strptime(start_time,"%H:%M")
            start_timea.append(start_time.strftime('%H:%M'))
            print (start_timea)
        except:
            print ("ERROR! Please enter the start time in HH:MM in 24-hour format. \nPossible Errors may include:\n- Missing Colons\n- Program does not accept AM/PM (must be in 24 hour format)\n")
    print("\n Noted. \n")
    end_timea = []
    for x in range(0, day):
        try:
            end_time = input("Input End Time in HHMM format for day:")
            end_time = dt.datetime.strptime(end_time,"%H:%M")
            end_timea.append(end_time.strftime('%H:%M'))
            print (end_timea)
        except:
            print ("ERROR! Please enter the start time in HH:MM format in 24-hour format.  \nPossible Errors may include:\n- Missing Colons\n- Program does not accept AM/PM (must be in 24 hour format)\n")

def survey()




load_data()
day_time()
# survey()
