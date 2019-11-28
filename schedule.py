#noinspection PyUnresolvedReferences
import pandas as pd
#noinspection PyUnresolvedReferences
import numpy as np
#noinspection PyUnresolvedReferences
import xlrd
#noinspection PyUnresolvedReferences
import time
#noinspection PyUnresolvedReferences
import datetime



def load_data():
    print("Welcome to ShakeItUpSchedule. \n Please make sure the excel file includes the following categories in the columns: \n Serial Number, Event Title, Event Description, Day, Location, Start Time, End Time, Moderator, and Categories")
    filename = input("Enter the path of the excel file: ")
    df = pd.read_excel(filename)
    print(df)


#def survey():
    #ask user time they will be present and expected time to leave


#def makeSched():

def day_time():
    day = int(input("How many days of the event are there?"))
    print(date)
    for i in day:
        day += 1
    try:
        start_time = datetime.strptime(input("Input Beginning Time in HHMM format:"),"%H%M")
        print (start_time.strftime("%H%M"))
    except:
        print("Please enter in correct time in HHMM format")

    #end_time = datetime.datetime.strptime(input("Input End Time in HHMM format:"))

    #date = input("What days of the week are you attending?: ")


#load_data()
# survey()
day_time()
