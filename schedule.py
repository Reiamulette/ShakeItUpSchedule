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
import random

#no inspection PyUnresolvedReferences has to do with using PyCharm...


desired_width = 300
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)


def load_data():                    #loads the excel file
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


def day_time():                 #finds out when you are going to be at the event
    global dateofday
    global dateofdaya
    global start_time
    global start_timea
    global end_timea
    global end_time

    dateofdaya = []         #creates list of dates
    start_timea = []        #creates list of start time
    end_timea = []          #creates list of end time

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
                start_time = input("Enter your arrival time in HH:MM format for day "+ str(x+1)+ " in military time:")
                start_time = dt.datetime.strptime(start_time,"%H:%M")
                if start_time.strftime('%H:%M'):
                    while True:
                        try:
                            end_time = input("Enter your end time in HH:MM format for day "+ str(x+1)+ " in miliary time:")
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


def survey():                       #figure out your interests (and eventually builds your schedule)
    global category
    global possible_events
    global filt_category
    global new_dataf
    global duration

    duration = pd.Series()
    possible_events = []
    filt_category = pd.DataFrame()
    new_dataf = pd.DataFrame()

    category = ["Featured Panels","Artist Alley", "Dealer's Room","Concerts", "Arcade", "Manga Library", "Contests", "Maid Cafe" , "Guest Autographs"]

    for x in category:
        interest = input("Are you interested in " + str(x) + "?\nEnter yes or no.")
        if interest == "yes":
            filt_category = dataf["Categories"].isin([x])       #filters the events that are in said category
            temp_dataf = dataf[filt_category].copy()
            new_dataf = new_dataf.append(temp_dataf)
            print(new_dataf)                                    #new_dataf IS a dataframe
            obscure = pd.DataFrame(columns = ['to','fr','ans'])
            obscure.to = new_dataf["Start Time"].to_timestamp
            obscure.fr = new_dataf["End Time"].to_timestamp
            duration = (obscure.fr - obscure.to).astype('timedelta64[h]')
            print(type(duration))
            # new_dataf["Start Time"] = new_dataf["Start Time"].apply(pd.Timestamp)
            # new_dataf["End Time"] = new_dataf["End Time"].apply(pd.Timestamp)
            # new_dataf[Duration] = (new_dataf["End Time"]- new_dataf["Start Time"]).dt.days
            new_dataf.insert(7,"Duration",duration,True)

            filter_date()                                      #calls function filter_date
        elif interest == "no":
            pass
        else:
            print("Not an acceptable answer. Try Again.")
            break

def filter_date():                                              #filters day the date
    global in_day_dataf
    global in_date
    global interval

    in_date = pd.DataFrame()
    in_day_dataf = pd.DataFrame()


    interval = dt.timedelta(minutes=15)

    for j in dateofdaya:
        in_date = new_dataf["Day"].isin([j])                    #filters the events that are in said day
        temp_dataf = dataf[in_date].copy()                      #copies the printed date
        in_day_dataf = in_day_dataf.append(temp_dataf)          #add to new dataframe called in_day_dataf


    print(df[in_day_dataf])
    #scheduling()

def scheduling():                                               #starts trying to schedule
    global current_time
    global interval
    global duration
    global in_day_dataf
    global crop_time
    global randomize
    global act_sched
    global rand_number

    rand_number = 0
    in_day_dataf = pd.DataFrame()
    in_day_dataf_count_row = in_day_dataf.shape[0]              #count number of rows of the in_day_dataf
    act_sched_count_row = in_day_dataf.shape[0]                 #count number of rows in actual schedule
    current_time = start_timea[:]                               #give current_time a copy of start_time (so it change current time without moving start_time)
    randomize = random.randint(0,in_day_dataf_count_row - 1)    #randomly choose event
    act_sched = pd.DataFrame()                                  # the schedule!

    for x,y,z in start_timea, end_timea, current_time:
        if act_sched_count_row < 3:                             # attending 3 "prioritized" events minimum
            while z < y:                                        #if current time is less than end time we want to add events
                while True:                                     #random number generator
                    try:
                        rnumber = int(input("Input a Random Number to randomly generate which event should be put into the category"))
                        print(rnumber)
                        for j in range(rnumber):
                            rand_number = randomize
                        act_sched = act_sched.append(in_day_dataf.iloc(rand_number))    #add row to schedule
                        duration_limit()                                                #check if row satisfy duration
                    except:
                        print("Error! Did you enter a number?")
                        continue
                    break
            y += interval                                       # to help break while loop.
        else:
            print(b)

def duration_limit():
    crop_time = dt.timedelta(minutes = 60)

    if in_day_dataf["Duration"] > dt.timedelta(minutes = 180):

        act_sched.update()
    if act_sched["Start Time"] >= in_day_data.iloc(rand_number)["Start Time"]:        #if the event isn't open yet, move on to next hour to check
        if act_sched["End Time"] >= in_day_data.iloc(rand_number)["End Time"]:
            print(act_sched)

load_data()
day_time()
survey()
