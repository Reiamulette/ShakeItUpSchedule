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

# no inspection PyUnresolvedReferences has to do with using PyCharm...


desired_width = 300
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)


def load_data():                                # loads the excel file
    global dataf
    global df


    print("Welcome to ShakeItUpSchedule. \n Please make sure the excel file includes the following categories in the columns: \n Serial Number, Event Title, Event Description, Day, Location, Start Time, End Time, Categories, and Subcategories")
    while True:
        try:
            filename = input("Enter the path of the excel file (be sure to include .xlsx): ")
            df = pd.read_excel(filename)
            dataf = df.copy()                   # created in case I accidentally mess up the original dataframe
            print(dataf)
        except:
            print("Error! Did you enter the path correctly?")
            continue
        break


def day_time():                                 # finds out when you are going to be at the event
    global dateofday
    global dateofdaya
    global start_time
    global start_timea
    global end_timea
    global end_time

    dateofdaya = []         # creates list of dates
    start_timea = []        # creates list of start time
    end_timea = []          # creates list of end time

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


def survey():                       # figure out your interests (and eventually builds your schedule)
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
        while True:
            try:
                if interest == "yes":
                    filt_category = dataf["Categories"].isin([x])                   # filters the events that are in said category
                    temp_dataf = dataf[filt_category].copy()
                    new_dataf = new_dataf.append(temp_dataf,sort = True)            # sort has to be true to keep index numbers *important because they are labels*

                    obscure = pd.DataFrame(columns = ['to','fr','ans'])             # track duration
                    obscure.to = new_dataf["Start Time"].to_timestamp
                    obscure.fr = new_dataf["End Time"].to_timestamp
                    duration = (obscure.fr - obscure.to).astype('timedelta64[h]')
                    new_dataf["Duration"]= duration

                elif interest == "no":
                    pass
                else:
                    print("Not an acceptable answer. Moving on.")
                    break
                break

            except:
                print("Return")
                continue
            break
    if new_dataf.shape[0]<6:
            print("Featured Panels will be automatically added because you do not have enough interest in our specially planned event.\nYou're here using this program to try new things!")
            filt_category = dataf["Categories"].isin(["Featured Panels"])   # filters the events that are in said category
            temp_dataf = dataf[filt_category].copy()
            new_dataf = new_dataf.append(temp_dataf,sort = True)            # sort has to be true to keep index numbers *important because they are labels*

            obscure = pd.DataFrame(columns = ['to','fr','ans'])             # track duration
            obscure.to = new_dataf["Start Time"].to_timestamp
            obscure.fr = new_dataf["End Time"].to_timestamp
            duration = (obscure.fr - obscure.to).astype('timedelta64[h]')
            new_dataf["Duration"]= duration
    else:
        pass
    filter_date()                                                           # calls function filter_date

def filter_date():                                                          # filters day the date and starts scheduling (adding events to final schedule)
    global in_day_dataf
    global in_date
    global interval
    global new_dataf

    in_date = pd.DataFrame()
    in_day_dataf = pd.DataFrame()
    interval = dt.timedelta(minutes=15)

    for j in dateofdaya:
        in_date = new_dataf["Day"].isin([j])                                # Filters events that aren't in the Day
        temp_dataf = new_dataf[in_date].copy()                              # copies the printed dataframe
        in_day_dataf = in_day_dataf.append(temp_dataf)                      # add to new dataframe called in_day_dataf
        print(in_day_dataf)
        scheduling()

def scheduling():                                                           # starts trying to schedule
    global current_time
    global interval
    global duration
    global in_day_dataf
    global crop_time
    global randomize
    global act_sched
    global rand_number

    interval = dt.timedelta(minutes=15)
    act_sched = pd.DataFrame()                                  # the schedule!

    rand_number = 0
    in_day_dataf_count_row = in_day_dataf.shape[0]              # count number of rows of the in_day_dataf
    act_sched_count_row = act_sched.shape[0]                    # count number of rows in actual schedule
    current_time = start_timea[:]                               # give current_time a copy of start_time (so it change current time without moving start_time)
    randomize = random.randint(0,in_day_dataf_count_row-1)      # randomly choose event


    for (x,y,z) in zip(start_timea, end_timea, current_time):
        if act_sched_count_row < 3:                             # attending 3 "prioritized" events minimum
            while z < y:                                        # if current time is less than end time we want to add events                                   # random number generator
                while True:
                    try:
                        rnumber = int(input("Input a Random Number to randomly generate which event should be put into the category"))
                    except:
                        print("Error! Did you enter a number?")
                        continue
                    break
                for i in range(rnumber):
                    rand_number = random.randint(0,in_day_dataf_count_row-1)
                act_sched = act_sched.append(in_day_dataf.iloc[rand_number])    # add row to schedule
                print(rand_number)
                print(act_sched)
                check_time()                                                    # check if row satisfy duration


                y += interval                                                               # to help break while loop.
        else:
            pass

def check_time():
    global in_day
    timeframe = pd.to_timedelta(act_sched["Duration"],unit = "h")

    if (timeframe > dt.timedelta(hours = 3)).bool():
        act_sched.at('Start Time')[act_sched.iloc(rand_number)] = current_time
        new_end = dt.dt(current_time) + dt.timedelta(hours =1)
        act_sched.at('End Time')[act_sched.iloc(rand_number)] = new_end
        print(act_sched["Start Time"])
        print(act_sched["End Time"])
    if act_sched["Start Time"] >= in_day_dataf.iloc(rand_number)["Start Time"]:          # Errors here: if the event isn't open yet, move on to next hour to check
        if act_sched["End Time"] >= in_day_dataf.iloc(rand_number)["End Time"]:
            print(act_sched)

#def add_panel():
    #figure out how to sort the events by tim

load_data()
day_time()
survey()
