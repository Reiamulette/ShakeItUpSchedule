#noinspection PyUnresolvedReferences
import pandas as pd
#noinspection PyUnresolvedReferences
import numpy as np
#noinspection PyUnresolvedReferences
import xlrd

def load_data():
    print("Welcome to ShakeItUpSchedule. \n Please make sure the excel file includes the following categories in the columns: \n Serial Number, Event Title, Event Description, Day, Location, Start Time, End Time, Moderator, and Categories")
    filename = input("Enter the path of the excel file: ")
    df = pd.read_excel(filename)
    print(df)
def survey():
    print("This is a survey to figure out what events you may be interested in.")
    a = input("Are you participating in any contests/tournaments? \n This includes cosplay contest and video gaming tournaments. \n Type y for Yes and n for No. ")
    if a == "y":
        print("Okay.")
    elif a == "n":
        print("Noted.")
    else:
        print("Not a valid response")


    b = input ("Are you interested in visiting the Artist Alley?")
    if b == "y":
        print("Okay.")
    elif b == "n":
        print("Noted.")
    else:
        print("Not a valid response")

    b = input ("Are you interested in visiting the Dealer's Room?")
    if b == "y":
        print("Okay.")
    elif b == "n":
        print("Noted.")
    else:
        print("Not a valid response")

    b = input ("Are you interested in playing at the Arcade?")
    if b == "y":
        print("Okay.")
    elif b == "n":
        print("Noted.")
    else:
        print("Not a valid response")

    b = input ("Are you interested in going to the Maid Cafe?")
    if b == "y":
        print("Okay.")
    elif b == "n":
        print("Noted.")
    else:
        print("Not a valid response")

    b = input ("Are you interested in any of the featured panels and guests?")
    if b == "y":
        print("Okay.")
    elif b == "n":
        print("Noted.")
    else:
        print("Not a valid response")

    b = input ("Are you interested in attending any of the dance/concerts?")
    if b == "y":
        print("Okay.")
    elif b == "n":
        print("Noted.")
    else:
        print("Not a valid response")

def makeSched():




load_data()
survey()
