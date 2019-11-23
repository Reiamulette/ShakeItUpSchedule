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
def
load_data()
