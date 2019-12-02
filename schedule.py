# noinspection PyUnresolvedReferences
import pandas as pd
# noinspection PyUnresolvedReferences
import numpy as np
# noinspection PyUnresolvedReferences
import time
# noinspection PyUnresolvedReferences
import datetime as dt
# noinspection PyUnresolvedReferences
import timedelta as td
# noinspection PyUnresolvedReferences
import schedule
# noinspection PyUnresolvedReferences
import random

#no inspection PyUnresolvedReferences has to do with using PyCharm...


desired_width = 300
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)


def load_data():
    global dataf
    global df


    print("Welcome to ShakeItUpSchedule. \n Please make sure the excel file includes the following categories in the columns: \n Serial Number, Event Title, Event Description, Day, Location, Start Time, End Time, Categories, and Subcategories")
    while True:
        try:
            filename = input("Enter the path of the excel file (be sure to include .xlsx): ")
            df = pd.read_excel(filename)
            dataf = df.copy()           #created in case I accidentally mess up the original dataframe
            print(dataf)
        except:
            print("Error! Did you enter the path correctly?")
            continue
        break


def day_time():
    global dateofday
    global dateofdaya
    global start_time
    global start_timea
    global end_timea
    global end_time

    dateofdaya = []
    start_timea = [] #creates list of start time
    end_timea = []   #creates list of end time

    while True:
        try:
            day = int(input("How many days of the event are you planning to attend?"))
            print(day)
        except:
            print("Error! Did you enter the number correctly?")
            continue
        break

    for x in range(0, day):
        while True:
            try:
                dateofday = input("What date is it on day " + str(x+1) + "? (in MM/DD/YYYY format)")
                dateofday = dt.datetime.strptime(dateofday,"%m/%d/%Y")
                dateofday.strftime("%m/%d/%Y")
                dateofdaya.append(dateofday.strftime("%m/%d/%Y"))
                print(dateofdaya)
            except:
                print("\nERROR! Please enter the date of day " + str(x+1) +" in MM/DD/YYYY format. \nPossible Errors may include:\n- Missing slashes\n")
                continue
            break
        while True:
            try:
                start_time = input("Enter your arrival time in HH:MM format for day "+ str(x+1)+ ":")
                start_time = dt.datetime.strptime(start_time,"%H:%M")
                if start_time.strftime('%H:%M'):
                    while True:
                        try:
                            end_time = input("Enter your end time in HH:MM format for day "+ str(x+1)+ ":")
                            end_time = dt.datetime.strptime(end_time,"%H:%M")
                            dur = end_time - start_time
                            if dur > dt.timedelta(0):
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
    print("Arrival Time: ", start_timea)
    print("End Time: ", end_timea)
    print("\n Noted. \n")


def survey():
    global interest
    global in_interests
    global category
    global is_day
    global possible_events
    global filt_category
    global new_dataf


    possible_events = []
    filt_category = pd.DataFrame()
    new_dataf = pd.DataFrame()

    category = ["Artist Alley", "Dealer's Room", "Featured Panels", "Concerts", "Arcade", "Manga Library", "Contests", "Maid Cafe" , "Guest Autographs"]


    for x in category:
        interest = input("Are you interested in " + str(x) + "?\nEnter yes or no.")
        if interest == "yes":
            filt_category = dataf["Categories"].isin([x])   #filters the events that are in said category
            temp_dataf = dataf[filt_category].copy()
            new_dataf = new_dataf.append(temp_dataf)
            print(new_dataf)
            filter_date()                                   #calls function filter_date
        elif interest == "no":
            pass
        else:
            print("Not an accepted answer.")
            break

def filter_date():
    global in_day_dataf
    global in_date

    in_date = pd.DataFrame()
    in_day_dataf = pd.DataFrame()


    interval = dt.timedelta(minutes = 15)
    for j in dateofdaya:
        in_date = new_dataf["Day"].isin([j])            #filters the events that are in said day
        temp_dataf = dataf[in_date].copy()              #copies the printed date
        in_day_dataf = in_day_dataf.append(temp_dataf)  #add to new dataframe called in_day_dataf
        print(df[in_day_dataf])
        scheduling()

def scheduling():
    global current_time
    global interval
    global duration

    in_day_dataf = pd.DataFrame()

    duration = df[in_day_dataf["Start Time"]] - df[in_day_dataf["Start Time"]]            #HERE! Try to set AA/DR/GR/MC to 1 hour each

    current_time = start_timea[:]                       #give current_time a copy of start_time (so it change current time without moving start_time)
    for x,y,z in start_timea, end_timea, current_time:
        while z < y:
            add_events()
            y += interval

def add_events():
    print(a)


load_data()
day_time()
survey()
scheduling()
